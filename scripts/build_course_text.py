from __future__ import annotations

import html
import json
import re
import shutil
import zipfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

import pdfplumber


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "course_full_text.txt"
CHUNKS_DIR = ROOT / "course_text_parts"
AUDIT_OUTPUT = ROOT / "course_build_audit.json"
MAX_SLICE_BYTES = 75_000
PDF_ANALYSIS: list[dict[str, object]] = []
TEXT_PARTS: list[tuple[str, str]] = []
TEXT_SLICES: list[tuple[str, str]] = []

LECTURES = [
    ("01", "Introduction", ROOT / "lectures" / "01-introduction"),
    ("02", "Rendering Pipeline", ROOT / "lectures" / "02-rendering-pipeline"),
    ("03", "Geometric Transformations", ROOT / "lectures" / "03-geometric-transformations"),
    ("04", "Geometric Projection", ROOT / "lectures" / "04-geometric-projection"),
    ("05", "Clipping", ROOT / "lectures" / "05-clipping"),
    ("06", "Rasterization", ROOT / "lectures" / "06-rasterization"),
    ("07", "Visibility Determination", ROOT / "lectures" / "07-visibility-determination"),
    ("08", "Local Illumination", ROOT / "lectures" / "08-local-illumination"),
    ("09", "Texturing", ROOT / "lectures" / "09-texturing"),
    ("10", "Shadows", ROOT / "lectures" / "10-shadows"),
]

ASSIGNMENTS = [
    ("00", "Introduction to C++", ROOT / "assignments" / "00-introduction-to-cpp" / "index.html"),
    ("01", "Rendering Pipeline", ROOT / "assignments" / "01-rendering-pipeline" / "index.html"),
    ("02", "Primitive Types / Shaders", ROOT / "assignments" / "02-primitive-types-shaders" / "index.html"),
    ("03", "Geometric Transformations", ROOT / "assignments" / "03-geometric-transformations" / "index.html"),
    ("04", "Projections and Clipping", ROOT / "assignments" / "04-projections-and-clipping" / "index.html"),
    ("05", "Rasterization", ROOT / "assignments" / "05-rasterization" / "index.html"),
    ("Bonus", "Rendering Contest", ROOT / "assignments" / "bonus-rendering-contest" / "index.html"),
]

COURSE_TERMS = [
    "aliasing",
    "ambient",
    "barycentric",
    "blinn",
    "camera",
    "clipping",
    "coordinate",
    "culling",
    "depth",
    "diffuse",
    "fragment",
    "framebuffer",
    "homogeneous",
    "illumination",
    "interpolation",
    "lighting",
    "matrix",
    "mipmap",
    "model",
    "normal",
    "opengl",
    "orthographic",
    "perspective",
    "phong",
    "pipeline",
    "projection",
    "rasterization",
    "rendering",
    "sampling",
    "shader",
    "shadow",
    "specular",
    "texture",
    "texel",
    "transformation",
    "triangle",
    "vertex",
    "visibility",
    "viewport",
    "z-buffer",
]

GENERATED_PATHS = {
    "course_full_text.txt",
    "course_build_audit.json",
}


class MoodleHTMLTextParser(HTMLParser):
    BLOCK_TAGS = {
        "address",
        "article",
        "aside",
        "blockquote",
        "br",
        "dd",
        "div",
        "dl",
        "dt",
        "fieldset",
        "figcaption",
        "figure",
        "footer",
        "form",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "hr",
        "li",
        "main",
        "nav",
        "ol",
        "p",
        "pre",
        "section",
        "table",
        "tbody",
        "td",
        "tfoot",
        "th",
        "thead",
        "tr",
        "ul",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.links: list[tuple[str, str]] = []
        self._skip_depth = 0
        self._current_link: str | None = None
        self._current_link_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {name: value or "" for name, value in attrs}
        if tag in {"script", "style"}:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")
        if tag == "a":
            self._current_link = attrs_dict.get("href", "")
            self._current_link_text = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self._skip_depth:
            self._skip_depth -= 1
            return
        if self._skip_depth:
            return
        if tag == "a" and self._current_link is not None:
            text = clean_text(" ".join(self._current_link_text))
            if self._current_link and text:
                self.links.append((text, html.unescape(self._current_link)))
            self._current_link = None
            self._current_link_text = []
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        if self._current_link is not None:
            self._current_link_text.append(data)
        self.parts.append(data)

    def text(self) -> str:
        return clean_text(" ".join(self.parts))


def clean_text(value: str) -> str:
    value = html.unescape(value)
    value = value.replace("\xa0", " ")
    value = re.sub(r"[ \t\r\f\v]+", " ", value)
    value = re.sub(r"\n\s+", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def heading(title: str, level: int = 1) -> str:
    marks = {1: "=", 2: "-", 3: "~"}
    mark = marks.get(level, "-")
    line = mark * len(title)
    return f"{title}\n{line}"


def slugify(value: str) -> str:
    value = value.lower().replace("++", "pp")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def lines_to_text(lines: list[str]) -> str:
    return "\n".join(lines).replace("\r\n", "\n").strip() + "\n"


def split_text_by_size(text: str, max_bytes: int = MAX_SLICE_BYTES) -> list[tuple[str, str]]:
    slices: list[tuple[str, str]] = []
    current: list[str] = []
    current_bytes = 0
    for line in text.splitlines(keepends=True):
        line_bytes = len(line.encode("utf-8"))
        if current and current_bytes + line_bytes > max_bytes:
            part_text = "".join(current)
            slices.append((f"98_size_limited_full_text_slices/full_text_part_{len(slices) + 1:03d}.txt", part_text))
            current = []
            current_bytes = 0
        current.append(line)
        current_bytes += line_bytes
    if current:
        part_text = "".join(current)
        slices.append((f"98_size_limited_full_text_slices/full_text_part_{len(slices) + 1:03d}.txt", part_text))
    return slices


def extend_with_part(all_lines: list[str], part_path: str, part_lines: list[str]) -> None:
    text = lines_to_text(part_lines)
    TEXT_PARTS.append((part_path, text))
    all_lines.extend(part_lines)
    all_lines.append("")


def read_html(path: Path) -> tuple[str, list[tuple[str, str]]]:
    parser = MoodleHTMLTextParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return parser.text(), parser.links


def append_html_section(lines: list[str], title: str, path: Path, level: int = 2) -> None:
    text, links = read_html(path)
    rel = path.relative_to(ROOT).as_posix()
    lines.append(heading(title, level))
    lines.append(f"Quelle: {rel}")
    lines.append("")
    lines.append(text if text else "[Kein extrahierbarer HTML-Text gefunden.]")
    external_links = [(label, url) for label, url in links if re.match(r"^https?://", url)]
    if external_links:
        lines.append("")
        lines.append("Externe Links:")
        for label, url in external_links:
            lines.append(f"- {label}: {url}")
    lines.append("")


def append_source_manifest(lines: list[str]) -> None:
    lines.append(heading("Quellen-Dateiliste", 2))
    lines.append("Diese Dateien wurden als Kursquellen beruecksichtigt:")
    lines.append("")
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if (
            rel in GENERATED_PATHS
            or rel.startswith(".git/")
            or rel.startswith("scripts/")
            or rel.startswith("course_text_parts/")
        ):
            continue
        size = path.stat().st_size
        lines.append(f"- {rel} ({size} bytes)")
    lines.append("")


def normalize_line(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def table_to_text(table: list[list[object]]) -> list[str]:
    rows: list[str] = []
    for row in table:
        cells = [normalize_line(str(cell or "")) for cell in row]
        if any(cells):
            rows.append(" | ".join(cells))
    return rows


def page_visual_counts(page: object) -> dict[str, int]:
    return {
        "images": len(getattr(page, "images", []) or []),
        "rects": len(getattr(page, "rects", []) or []),
        "curves": len(getattr(page, "curves", []) or []),
        "lines": len(getattr(page, "lines", []) or []),
    }


def collect_formula_candidates(text: str) -> list[str]:
    candidates: list[str] = []
    for raw_line in text.splitlines():
        line = normalize_line(raw_line)
        if not line or len(line) > 180:
            continue
        has_math_symbol = bool(re.search(r"(=|<=|>=|->|<-|\\bcos\\b|\\bsin\\b|\\btan\\b|\\bmin\\b|\\bmax\\b|\\bnorm\\b|\\bdot\\b|\\bcross\\b)", line, re.I))
        has_math_shape = bool(re.search(r"([A-Za-z][xyz]?\s*[=+\-*/]\s*[-A-Za-z0-9(])|(\[[^\]]+\])|(\([xyz],\s*[xyz])", line))
        if has_math_symbol or has_math_shape:
            candidates.append(line)
    return candidates


def collect_heading_candidates(text: str) -> list[str]:
    candidates: list[str] = []
    seen: set[str] = set()
    for raw_line in text.splitlines():
        line = normalize_line(raw_line)
        if not 4 <= len(line) <= 90:
            continue
        if line.endswith(".") or line.startswith("["):
            continue
        if sum(ch.isalpha() for ch in line) < 4:
            continue
        if line.lower() in seen:
            continue
        seen.add(line.lower())
        candidates.append(line)
        if len(candidates) >= 25:
            break
    return candidates


def extract_pdf_text(pdf_path: Path) -> list[str]:
    pages: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        for index, page in enumerate(pdf.pages, start=1):
            text = page.extract_text(x_tolerance=1.5, y_tolerance=3) or ""
            text = clean_text(text)
            if not text:
                text = "[Kein extrahierbarer Text auf dieser Seite. Inhalt kann bildbasiert sein.]"
            counts = page_visual_counts(page)
            tables_text: list[str] = []
            try:
                tables = page.extract_tables() or []
            except Exception:
                tables = []
            for table_index, table in enumerate(tables, start=1):
                table_rows = table_to_text(table)
                if table_rows:
                    tables_text.append(f"[Tabelle {table_index}]")
                    tables_text.extend(table_rows)
            PDF_ANALYSIS.append(
                {
                    "source": pdf_path.relative_to(ROOT).as_posix(),
                    "page": index,
                    "text": text,
                    "counts": counts,
                    "tables": len(tables_text),
                    "formulas": collect_formula_candidates(text),
                    "headings": collect_heading_candidates(text),
                }
            )
            page_lines = [
                f"[Seite {index}]",
                "Seiten-Metadaten: "
                f"Bilder={counts['images']}, Rechtecke={counts['rects']}, "
                f"Kurven={counts['curves']}, Linien={counts['lines']}",
                text,
            ]
            if tables_text:
                page_lines.append("Extrahierte Tabellen:")
                page_lines.extend(tables_text)
            pages.append("\n".join(page_lines))
    return pages


def append_lecture(lines: list[str], number: str, title: str, folder: Path) -> None:
    append_html_section(lines, f"Kapitel {number}: {title} - Moodle-Seite", folder / "index.html", 2)
    pdfs = sorted((folder / "slides").glob("*.pdf"))
    for pdf_path in pdfs:
        rel = pdf_path.relative_to(ROOT).as_posix()
        lines.append(heading(f"Kapitel {number}: {title} - Folien", 2))
        lines.append(f"Quelle: {rel}")
        lines.append("")
        lines.extend(extract_pdf_text(pdf_path))
        lines.append("")


def zip_member_is_text(name: str) -> bool:
    suffix = Path(name).suffix.lower()
    return suffix in {
        ".c",
        ".cc",
        ".cmake",
        ".cpp",
        ".cxx",
        ".h",
        ".hpp",
        ".inl",
        ".md",
        ".txt",
    } or Path(name).name in {"CMakeLists.txt"}


def append_zip_contents(lines: list[str], zip_path: Path) -> None:
    lines.append(heading("OpenGL Starter Project", 2))
    lines.append(f"Quelle: {zip_path.relative_to(ROOT).as_posix()}")
    lines.append("")
    with zipfile.ZipFile(zip_path) as archive:
        names = sorted(info.filename for info in archive.infolist() if not info.is_dir())
        lines.append("Dateien im Zip:")
        for name in names:
            lines.append(f"- {name}")
        lines.append("")
        for name in names:
            if not zip_member_is_text(name):
                continue
            lines.append(heading(f"Zip-Datei: {name}", 3))
            raw = archive.read(name)
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                text = raw.decode("latin-1", errors="replace")
            lines.append(text.rstrip())
            lines.append("")


def append_text_asset(lines: list[str], title: str, path: Path) -> None:
    lines.append(heading(title, 2))
    lines.append(f"Quelle: {path.relative_to(ROOT).as_posix()}")
    lines.append("")
    lines.append(path.read_text(encoding="utf-8", errors="replace").rstrip())
    lines.append("")


def chapter_entries(folder: Path) -> list[dict[str, object]]:
    prefix = folder.relative_to(ROOT).as_posix()
    return [entry for entry in PDF_ANALYSIS if str(entry["source"]).startswith(prefix)]


def count_terms(entries: list[dict[str, object]]) -> Counter[str]:
    counter: Counter[str] = Counter()
    combined = "\n".join(str(entry["text"]).lower() for entry in entries)
    for term in COURSE_TERMS:
        pattern = r"\b" + re.escape(term.lower()).replace(r"\-", r"[- ]") + r"s?\b"
        hits = len(re.findall(pattern, combined))
        if hits:
            counter[term] = hits
    return counter


def unique_preserve_order(values: list[str], limit: int | None = None) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        key = value.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(value)
        if limit is not None and len(result) >= limit:
            break
    return result


def append_exam_preparation_addendum(lines: list[str]) -> None:
    lines.append(heading("Pruefungsvorbereitungs-Anhang", 2))
    lines.append("Dieser Anhang ist aus den vorhandenen Kursdateien abgeleitet. Er ersetzt keine nicht vorhandenen Materialien wie Vorlesungsmitschnitte, Altklausuren oder Musterloesungen.")
    lines.append("")

    lines.append(heading("KI-Nutzungsempfehlung", 3))
    lines.extend(
        [
            "- Erst die Kursuebersicht und diesen Anhang laden, dann kapitelweise mit den Rohfolien arbeiten.",
            "- Bei Rechen- oder Beweisfragen immer die Quelle und die Seitenmarke aus der Datei nennen lassen.",
            "- Bei Diagrammfragen die visuelle Inventur nutzen und bei Bedarf die Original-PDF-Seite oeffnen.",
            "- Keine Aussage als Kursfakt akzeptieren, wenn sie nicht durch den Rohtext oder eine Originalfolie gedeckt ist.",
        ]
    )
    lines.append("")

    lines.append(heading("Kapitelindex mit Schwerpunkten", 3))
    for number, title, folder in LECTURES:
        entries = chapter_entries(folder)
        term_counts = count_terms(entries)
        headings = unique_preserve_order(
            [heading for entry in entries for heading in entry.get("headings", [])], limit=20
        )
        lines.append(f"Kapitel {number}: {title}")
        lines.append(f"- Folienseiten: {len(entries)}")
        if term_counts:
            terms = ", ".join(f"{term} ({count})" for term, count in term_counts.most_common(15))
            lines.append(f"- Haeufige pruefungsrelevante Begriffe: {terms}")
        if headings:
            lines.append("- Ueberschriften/Leitbegriffe aus Folien:")
            for value in headings:
                lines.append(f"  - {value}")
        lines.append("- Sinnvolle KI-Fragen:")
        lines.append(f"  - Erklaere Kapitel {number} ({title}) als pruefungsorientierte Zusammenfassung mit Definitionen, Algorithmen und typischen Stolperfallen.")
        lines.append(f"  - Erstelle Karteikarten zu Kapitel {number} nur aus den hier angegebenen Quellen.")
        lines.append(f"  - Formuliere moegliche Klausurfragen zu Kapitel {number} mit Musterantworten und verweise auf relevante Seitenmarken.")
        lines.append("")

    lines.append(heading("Formel- und Notationskandidaten", 3))
    formula_rows: list[str] = []
    seen_formulas: set[str] = set()
    for entry in PDF_ANALYSIS:
        source = str(entry["source"])
        page = entry["page"]
        for formula in entry.get("formulas", []):
            key = formula.lower()
            if key in seen_formulas:
                continue
            seen_formulas.add(key)
            formula_rows.append(f"- {source}, Seite {page}: {formula}")
    if formula_rows:
        lines.extend(formula_rows)
    else:
        lines.append("[Keine separaten Formel-/Notationskandidaten erkannt.]")
    lines.append("")

    lines.append(heading("Visuelle Folien-Inventur", 3))
    lines.append("Diese Liste markiert Seiten mit vielen visuellen PDF-Objekten. Die Objekte selbst sind in einer Textdatei nicht vollstaendig darstellbar; fuer Diagrammfragen die genannte Original-PDF-Seite pruefen.")
    visual_rows: list[str] = []
    for entry in PDF_ANALYSIS:
        counts = entry["counts"]
        assert isinstance(counts, dict)
        visual_score = int(counts["images"]) * 5 + int(counts["rects"]) + int(counts["curves"]) + int(counts["lines"])
        if visual_score < 20 and int(counts["images"]) == 0:
            continue
        visual_rows.append(
            f"- {entry['source']}, Seite {entry['page']}: "
            f"Bilder={counts['images']}, Rechtecke={counts['rects']}, "
            f"Kurven={counts['curves']}, Linien={counts['lines']}"
        )
    if visual_rows:
        lines.extend(visual_rows)
    else:
        lines.append("[Keine visuell dichten Seiten erkannt.]")
    lines.append("")

    lines.append(heading("Uebungsindex", 3))
    for number, title, path in ASSIGNMENTS:
        text, links = read_html(path)
        rel = path.relative_to(ROOT).as_posix()
        lines.append(f"Uebung {number}: {title}")
        lines.append(f"- Quelle: {rel}")
        lines.append(f"- Textumfang: {len(re.findall(r'\\S+', text))} Woerter")
        external_links = [url for _, url in links if re.match(r"^https?://", url)]
        if external_links:
            lines.append("- Externe Links:")
            for url in external_links:
                lines.append(f"  - {url}")
        lines.append("- Sinnvolle KI-Aufgabe: Extrahiere Aufgabenstellung, Abgabekriterien, benoetigte Konzepte und erstelle eine Loesungsstrategie ohne nicht belegte Annahmen.")
        lines.append("")


def source_files() -> list[Path]:
    files: list[Path] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if (
            rel in GENERATED_PATHS
            or rel.startswith(".git/")
            or rel.startswith("scripts/")
            or rel.startswith("course_text_parts/")
        ):
            continue
        files.append(path)
    return files


def pdf_page_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    for entry in PDF_ANALYSIS:
        source = str(entry["source"])
        counts[source] = counts.get(source, 0) + 1
    return counts


def zip_manifest(zip_path: Path) -> list[dict[str, object]]:
    with zipfile.ZipFile(zip_path) as archive:
        return [
            {"path": info.filename, "size": info.file_size, "text_extracted": zip_member_is_text(info.filename)}
            for info in archive.infolist()
            if not info.is_dir()
        ]


def build_audit(full_text: str) -> dict[str, object]:
    sources = source_files()
    html_files = [path for path in sources if path.suffix.lower() == ".html"]
    pdf_files = [path for path in sources if path.suffix.lower() == ".pdf"]
    zip_files = [path for path in sources if path.suffix.lower() == ".zip"]
    css_files = [path for path in sources if path.suffix.lower() == ".css"]
    source_rels = [path.relative_to(ROOT).as_posix() for path in sources]
    output_paths = [
        "course_full_text.txt",
        *[f"course_text_parts/{path}" for path, _ in TEXT_PARTS],
        *[f"course_text_parts/{path}" for path, _ in TEXT_SLICES],
    ]
    recombined_slices = "".join(text for _, text in TEXT_SLICES)
    checks = {
        "all_lecture_chunks_present": all(
            any(path == f"03_lectures/{number}_{slugify(title)}.txt" for path, _ in TEXT_PARTS)
            for number, title, _ in LECTURES
        ),
        "all_assignment_chunks_present": all(
            any(path == f"04_assignments/{number}_{slugify(title)}.txt" for path, _ in TEXT_PARTS)
            for number, title, _ in ASSIGNMENTS
        ),
        "all_pdf_pages_have_metadata": full_text.count("\nSeiten-Metadaten: ") == full_text.count("\n[Seite "),
        "no_pdf_page_without_extractable_text": "Kein extrahierbarer Text" not in full_text,
        "size_limited_slices_recombine_to_full_text": recombined_slices == full_text,
        "size_limited_slices_under_max_bytes": all(
            len(text.encode("utf-8")) <= MAX_SLICE_BYTES for _, text in TEXT_SLICES
        ),
    }
    return {
        "summary": {
            "source_file_count": len(sources),
            "html_file_count": len(html_files),
            "pdf_file_count": len(pdf_files),
            "pdf_page_count": len(PDF_ANALYSIS),
            "zip_file_count": len(zip_files),
            "css_file_count": len(css_files),
            "chunk_file_count": len(TEXT_PARTS),
            "size_limited_slice_count": len(TEXT_SLICES),
            "max_slice_bytes": MAX_SLICE_BYTES,
            "full_text_bytes": len(full_text.encode("utf-8")),
            "full_text_lines": full_text.count("\n"),
            "full_text_words": len(re.findall(r"\S+", full_text)),
        },
        "checks": checks,
        "source_files": source_rels,
        "pdf_page_counts": pdf_page_counts(),
        "zip_manifests": {
            path.relative_to(ROOT).as_posix(): zip_manifest(path)
            for path in zip_files
        },
        "outputs": output_paths,
    }


def write_outputs(full_text: str) -> dict[str, object]:
    OUTPUT.write_text(full_text, encoding="utf-8", newline="\n")
    TEXT_SLICES.clear()
    TEXT_SLICES.extend(split_text_by_size(full_text))
    if CHUNKS_DIR.exists():
        shutil.rmtree(CHUNKS_DIR)
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    index_lines = [
        heading("CS8165.001 SS26 - Text Chunks"),
        "Empfohlene Nutzung: zuerst 00_START_HERE.txt laden, danach den passenden Kapitel- oder Uebungs-Chunk.",
        "Die Datei ../course_full_text.txt enthaelt dieselben Kursinformationen in einer grossen Datei.",
        "Der Ordner 98_size_limited_full_text_slices/ enthaelt fortlaufende kleine Teile, die zusammen exakt die grosse Datei ergeben.",
        "",
        "Chunk-Dateien:",
    ]
    for part_path, part_text in TEXT_PARTS:
        target = CHUNKS_DIR / part_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(part_text, encoding="utf-8", newline="\n")
        rel = target.relative_to(CHUNKS_DIR).as_posix()
        part_lines = part_text.count("\n")
        part_words = len(re.findall(r"\S+", part_text))
        index_lines.append(f"- {rel}: {part_lines} Zeilen, {part_words} Woerter")
    index_lines.append("")
    index_lines.append("Fortlaufende size-limited Slices:")
    for part_path, part_text in TEXT_SLICES:
        target = CHUNKS_DIR / part_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(part_text, encoding="utf-8", newline="\n")
        rel = target.relative_to(CHUNKS_DIR).as_posix()
        index_lines.append(f"- {rel}: {len(part_text.encode('utf-8'))} bytes")
    (CHUNKS_DIR / "INDEX.txt").write_text(lines_to_text(index_lines), encoding="utf-8", newline="\n")
    audit = build_audit(full_text)
    audit["outputs"].append("course_text_parts/INDEX.txt")
    AUDIT_OUTPUT.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    return audit


def build() -> str:
    PDF_ANALYSIS.clear()
    TEXT_PARTS.clear()
    lines: list[str] = []
    start_lines: list[str] = []
    start_lines.append(heading("CS8165.001 SS26 - Interaktive Computergrafik"))
    start_lines.append("Volltextsammlung aus dem Moodle-Kursexport.")
    start_lines.append("Zweck: strukturierte Vorbereitung mit KI-Unterstuetzung.")
    start_lines.append("")
    start_lines.append("Hinweis: PDF-Text wurde automatisch extrahiert. Bildbasierte Diagramme, Formeln oder Grafiken koennen in reinem Text nur teilweise erfasst sein.")
    start_lines.append("")
    start_lines.append(heading("Inhaltsverzeichnis", 2))
    start_lines.extend(
        [
            "1. Kursuebersicht",
            "2. Organisatorisches",
            "3. Vorlesungen und Folien",
            "4. Uebungen",
            "5. OpenGL Starter Project",
            "6. Pruefungsvorbereitungs-Anhang",
            "7. Assets",
        ]
    )
    start_lines.append("")
    append_source_manifest(start_lines)
    extend_with_part(lines, "00_START_HERE.txt", start_lines)

    course_lines: list[str] = []
    append_html_section(course_lines, "Kursuebersicht", ROOT / "index.html", 2)
    extend_with_part(lines, "01_course_overview.txt", course_lines)

    org_lines: list[str] = []
    org_lines.append(heading("Organisatorisches", 2))
    append_html_section(org_lines, "Ankuendigungen", ROOT / "forums" / "announcements" / "index.html", 3)
    append_html_section(org_lines, "Students Forum", ROOT / "forums" / "students-forum" / "index.html", 3)
    append_html_section(org_lines, "Group Selection for Exercises", ROOT / "course" / "group-selection" / "index.html", 3)
    extend_with_part(lines, "02_organization.txt", org_lines)

    lectures_intro = [heading("Vorlesungen und Folien", 2)]
    extend_with_part(lines, "03_lectures/00_lectures_index.txt", lectures_intro)
    for number, title, folder in LECTURES:
        lecture_lines: list[str] = []
        append_lecture(lecture_lines, number, title, folder)
        extend_with_part(lines, f"03_lectures/{number}_{slugify(title)}.txt", lecture_lines)

    assignments_intro = [heading("Uebungen", 2)]
    extend_with_part(lines, "04_assignments/00_assignments_index.txt", assignments_intro)
    for number, title, path in ASSIGNMENTS:
        assignment_lines: list[str] = []
        append_html_section(assignment_lines, f"Uebung {number}: {title}", path, 3)
        extend_with_part(lines, f"04_assignments/{number}_{slugify(title)}.txt", assignment_lines)

    opengl_lines: list[str] = []
    append_zip_contents(opengl_lines, ROOT / "examples" / "opengl-rotating-cube.zip")
    extend_with_part(lines, "05_opengl_starter_project.txt", opengl_lines)

    exam_lines: list[str] = []
    append_exam_preparation_addendum(exam_lines)
    extend_with_part(lines, "06_exam_preparation_addendum.txt", exam_lines)

    asset_lines: list[str] = []
    append_text_asset(asset_lines, "Assets: Moodle CSS", ROOT / "assets" / "moodle.css")
    extend_with_part(lines, "07_assets_moodle_css.txt", asset_lines)

    return lines_to_text(lines)


def main() -> None:
    text = build()
    audit = write_outputs(text)
    line_count = text.count("\n")
    word_count = len(re.findall(r"\S+", text))
    print(f"Wrote {OUTPUT.relative_to(ROOT).as_posix()}")
    print(f"Wrote {CHUNKS_DIR.relative_to(ROOT).as_posix()}/")
    print(f"Wrote {AUDIT_OUTPUT.relative_to(ROOT).as_posix()}")
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Chunks: {audit['summary']['chunk_file_count']}")
    print(f"PDF pages: {audit['summary']['pdf_page_count']}")


if __name__ == "__main__":
    main()
