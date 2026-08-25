from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "course_text_parts"
OUT = ROOT / "study_pack"


CHAPTERS = [
    {
        "id": "01",
        "title": "Introduction",
        "file": PARTS / "03_lectures" / "01_introduction.txt",
        "themes": ["course goals", "graphics applications", "rendering overview", "models", "visibility", "illumination"],
        "must": [
            "Explain what interactive computer graphics studies and why real-time constraints matter.",
            "Distinguish modeling, rendering, visibility, illumination, and interaction at a high level.",
            "Describe the role of OpenGL and the GPU in the course.",
            "Connect later chapters to the rendering pipeline introduced here.",
        ],
        "pitfalls": [
            "Do not treat the introduction as only organizational; it frames the whole pipeline.",
            "Separate scene representation from image generation.",
            "Remember that interactivity implies performance constraints, not just image quality.",
        ],
    },
    {
        "id": "02",
        "title": "Rendering Pipeline",
        "file": PARTS / "03_lectures" / "02_rendering-pipeline.txt",
        "themes": ["object-based rendering", "OpenGL", "vertices", "primitives", "fragments", "pixels", "shaders", "framebuffer"],
        "must": [
            "Reproduce the pipeline order from vertices to pixels.",
            "Explain vertex processing, primitive assembly, rasterization, fragment processing, tests, and framebuffer operations.",
            "Differentiate vertex shader and fragment shader responsibilities.",
            "Explain how fragments differ from final pixels.",
            "Describe depth test, blending, and framebuffer purpose.",
        ],
        "pitfalls": [
            "Fragments are pixel candidates, not guaranteed final pixels.",
            "Rasterization and fragment shading are separate stages.",
            "OpenGL state influences rendering; do not describe it as purely functional code.",
        ],
    },
    {
        "id": "03",
        "title": "Geometric Transformations",
        "file": PARTS / "03_lectures" / "03_geometric-transformations.txt",
        "themes": ["matrices", "vectors", "affine transformations", "composition", "coordinate systems", "OpenGL transformations"],
        "must": [
            "Use homogeneous coordinates to represent translation, rotation, scaling, and affine transforms.",
            "Explain why transformation order matters.",
            "Compose model, world, view, and related coordinate transformations.",
            "Distinguish transforming points from transforming directions/normals.",
        ],
        "pitfalls": [
            "Matrix multiplication is not commutative.",
            "Normals usually require special handling under non-uniform scaling.",
            "Changing coordinates and moving objects can look algebraically similar but mean different things.",
        ],
    },
    {
        "id": "04",
        "title": "Geometric Projection",
        "file": PARTS / "03_lectures" / "04_geometric-projection.txt",
        "themes": ["linear perspective", "planar projections", "camera", "view volume", "orthographic projection", "perspective projection", "viewport"],
        "must": [
            "Explain perspective shortening and loss of depth in projection.",
            "Distinguish orthographic and perspective projection qualitatively and mathematically.",
            "Describe camera modeling and canonical view volume.",
            "Explain the role of projection matrices and homogeneous divide.",
        ],
        "pitfalls": [
            "Do not confuse view transformation with projection transformation.",
            "Perspective projection is not just scaling; the homogeneous divide is essential.",
            "Depth is transformed for later visibility tests, even though the image is 2D.",
        ],
    },
    {
        "id": "05",
        "title": "Clipping",
        "file": PARTS / "03_lectures" / "05_clipping.txt",
        "themes": ["analytical clipping", "pixel-based clipping", "canonical view volume", "visible parts", "optimized geometry processing"],
        "must": [
            "Explain why clipping is needed before costly later stages.",
            "Distinguish analytical clipping from pixel-based clipping.",
            "Describe clipping against a view volume and how primitives are modified or rejected.",
            "Explain how clipping interacts with rasterization and visibility.",
        ],
        "pitfalls": [
            "Clipping is not the same as culling.",
            "Clipping can create new vertices where primitives intersect clipping boundaries.",
            "Pixel-based clipping happens later and has different cost behavior.",
        ],
    },
    {
        "id": "06",
        "title": "Rasterization",
        "file": PARTS / "03_lectures" / "06_rasterization.txt",
        "themes": ["raster images", "pixels", "triangles", "fragments", "coverage", "interpolation", "barycentric coordinates"],
        "must": [
            "Explain how continuous primitives become discrete fragments.",
            "Describe triangle rasterization and inside/outside tests.",
            "Use interpolation across a primitive for depth and attributes.",
            "Explain why sampling causes artifacts and why pixel centers matter.",
        ],
        "pitfalls": [
            "A pixel is not a little square; be precise about samples and raster representation.",
            "Attribute interpolation must be distinguished from geometric transformation.",
            "Rasterization produces fragments before final visibility tests.",
        ],
    },
    {
        "id": "07",
        "title": "Visibility Determination",
        "file": PARTS / "03_lectures" / "07_visibility-determination.txt",
        "themes": ["visible surface determination", "hidden surface removal", "z-buffer", "depth", "culling", "occlusion"],
        "must": [
            "Define visibility determination / hidden surface removal.",
            "Explain z-buffering and depth comparison.",
            "Distinguish object-space and image-space approaches at a high level.",
            "Explain culling and why back-facing geometry can be rejected.",
        ],
        "pitfalls": [
            "Culling removes geometry based on orientation or volume tests; depth testing resolves occlusion per fragment.",
            "Depth precision can produce artifacts.",
            "Visibility is tied to the current camera/viewpoint.",
        ],
    },
    {
        "id": "08",
        "title": "Local Illumination",
        "file": PARTS / "03_lectures" / "08_local-illumination.txt",
        "themes": ["physics of light", "light sources", "material models", "ambient", "diffuse", "specular", "Phong", "Blinn"],
        "must": [
            "Explain local versus global illumination.",
            "Decompose common local illumination into ambient, diffuse, and specular components.",
            "Explain normals, light direction, view direction, and material coefficients.",
            "Compare Phong and Blinn-Phong style specular terms.",
        ],
        "pitfalls": [
            "Local illumination ignores indirect light effects unless explicitly approximated.",
            "Normals must be normalized and in the correct coordinate system.",
            "Diffuse and specular terms model different visual phenomena.",
        ],
    },
    {
        "id": "09",
        "title": "Texturing",
        "file": PARTS / "03_lectures" / "09_texturing.txt",
        "themes": ["texture mapping", "texture coordinates", "texels", "sampling", "filtering", "mipmaps", "normal mapping", "OpenGL textures"],
        "must": [
            "Explain textures as sampled data fields used during rendering.",
            "Map texture coordinates to texture lookups and fragment shading.",
            "Describe nearest and linear filtering qualitatively.",
            "Explain aliasing and why mipmaps help.",
            "Distinguish color textures from other texture uses such as normal maps.",
        ],
        "pitfalls": [
            "A texture is not only an image; it is sampled data for shading.",
            "Texture coordinates live in their own domain and must be interpolated.",
            "Filtering and mipmapping are about sampling quality, not geometry quality.",
        ],
    },
    {
        "id": "10",
        "title": "Shadows",
        "file": PARTS / "03_lectures" / "10_shadows.txt",
        "themes": ["shadows", "visibility from light", "shadow mapping", "depth map", "light space", "artifacts"],
        "must": [
            "Explain shadows as a visibility problem from the light source.",
            "Describe the two-pass idea of shadow mapping.",
            "Explain how a depth map from the light is compared during camera rendering.",
            "Name typical shadow-map artifacts and their causes.",
        ],
        "pitfalls": [
            "Shadow mapping stores depth from the light, not colors.",
            "Bias is needed to reduce self-shadowing but can cause detached shadows.",
            "Shadow quality depends on resolution, projection, and sampling.",
        ],
    },
]


EXERCISE_MAP = [
    ("00", "Introduction to C++", ["C++ basics", "build workflow", "OpenGL preparation"], ["01", "02"]),
    ("01", "Rendering Pipeline", ["pipeline implementation", "OpenGL rendering flow"], ["02"]),
    ("02", "Primitive Types / Shaders", ["primitives", "vertex shader", "fragment shader"], ["02", "06"]),
    ("03", "Geometric Transformations", ["matrix transforms", "model positioning"], ["03"]),
    ("04", "Projections and Clipping", ["projection matrices", "view volume", "clipping"], ["04", "05"]),
    ("05", "Rasterization", ["triangle coverage", "interpolation", "fragment generation"], ["06", "07"]),
    ("Bonus", "Rendering Contest", ["integrated rendering project", "visual quality", "performance"], ["02", "03", "04", "06", "08", "09", "10"]),
]


FLASHCARDS = [
    ("Rendering pipeline", "Ordered process that transforms scene primitives into fragments and final pixels."),
    ("Vertex", "Input point with attributes such as position, normal, color, and texture coordinates."),
    ("Primitive", "Geometric unit assembled from vertices, for example a triangle."),
    ("Fragment", "Pixel candidate generated by rasterization before all tests and framebuffer operations."),
    ("Framebuffer", "Storage for rendered image data and buffers such as color and depth."),
    ("Vertex shader", "Programmable stage that processes vertices and usually applies transformations."),
    ("Fragment shader", "Programmable stage that computes per-fragment output such as color."),
    ("Homogeneous coordinates", "Coordinate representation enabling affine transformations and perspective projection with matrices."),
    ("Affine transformation", "Transformation preserving lines and parallelism, including translation, rotation, scaling, and shear."),
    ("Transformation order", "Important because matrix multiplication is generally not commutative."),
    ("View transformation", "Transforms world coordinates into camera/view coordinates."),
    ("Projection transformation", "Maps view-space geometry into clip/canonical coordinates for projection."),
    ("Perspective projection", "Projection where distant objects appear smaller and homogeneous division is essential."),
    ("Orthographic projection", "Projection without perspective shortening; parallel lines remain parallel."),
    ("Clipping", "Removing or cutting primitive parts outside the view or clip region."),
    ("Analytical clipping", "Clipping before rasterization by modifying or rejecting primitives."),
    ("Pixel-based clipping", "Clipping during or after raster conversion using pixel/fragments regions."),
    ("Rasterization", "Conversion of geometric primitives into fragments on a raster grid."),
    ("Barycentric interpolation", "Interpolation over a triangle using weights relative to the triangle vertices."),
    ("Depth buffer", "Buffer storing depth values used for visibility decisions."),
    ("Z-buffer algorithm", "Per-fragment depth comparison approach for hidden surface removal."),
    ("Back-face culling", "Rejecting surfaces facing away from the camera for closed opaque objects."),
    ("Local illumination", "Lighting model considering direct light interaction at a surface point."),
    ("Ambient term", "Simple approximation of constant background light."),
    ("Diffuse term", "View-independent light reflection based on surface normal and light direction."),
    ("Specular term", "View-dependent highlight component modeling shiny reflection."),
    ("Phong model", "Local illumination model with ambient, diffuse, and specular components."),
    ("Blinn-Phong", "Specular variant using the half-vector between light and view directions."),
    ("Texture", "Sampled data field used during rendering, commonly image data mapped onto geometry."),
    ("Texel", "Texture element analogous to a sample in texture space."),
    ("Texture coordinates", "Coordinates used to look up texture data for a surface point."),
    ("Mipmapping", "Using prefiltered lower-resolution texture levels to reduce aliasing."),
    ("Aliasing", "Sampling artifact caused by insufficient sampling of high-frequency content."),
    ("Shadow mapping", "Two-pass shadow algorithm comparing camera fragments to depth from the light."),
    ("Shadow bias", "Offset used in shadow mapping to reduce self-shadowing artifacts."),
]


def heading(title: str, level: int = 1) -> str:
    mark = "=" if level == 1 else "-" if level == 2 else "~"
    return f"{title}\n{mark * len(title)}"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z][A-Za-z0-9+-]{2,}", text)


def top_terms(text: str, limit: int = 18) -> list[str]:
    stop = {
        "the", "and", "for", "with", "that", "this", "are", "from", "interactive", "computer", "graphics",
        "chapter", "source", "seite", "seiten", "metadata", "bilder", "rechtecke", "kurven", "linien",
        "summer", "term", "timo", "ropinski", "visual", "computing", "group", "institute", "media",
        "seiten-metadaten", "rechtecke", "kurven", "linien",
    }
    counts: dict[str, int] = {}
    for word in words(text.lower()):
        if word in stop or len(word) < 4:
            continue
        counts[word] = counts.get(word, 0) + 1
    return [term for term, _ in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]]


def page_count(text: str) -> int:
    return len(re.findall(r"^\[Seite ", text, flags=re.MULTILINE))


def extract_section(text: str, title: str, next_title: str | None = None) -> str:
    start = text.find(title)
    if start == -1:
        return ""
    if next_title is None:
        return text[start:]
    end = text.find(next_title, start + len(title))
    return text[start:] if end == -1 else text[start:end]


def chapter_guide(chapter: dict[str, object]) -> str:
    text = read(chapter["file"])  # type: ignore[arg-type]
    terms = top_terms(text)
    lines: list[str] = []
    title = f"Kapitel {chapter['id']}: {chapter['title']}"
    lines.append(heading(title))
    lines.append(f"Quelle: course_text_parts/03_lectures/{Path(chapter['file']).name}")  # type: ignore[arg-type]
    lines.append(f"Folienseiten in diesem Chunk: {page_count(text)}")
    lines.append("")
    lines.append(heading("Pruefungsfokus", 2))
    lines.append("Dieses Kapitel sollte so gelernt werden, dass du Definitionen, Pipeline-Rolle, typische Rechen-/Argumentationsschritte und Abgrenzungen erklaeren kannst.")
    lines.append("")
    lines.append(heading("Muss sitzen", 2))
    for item in chapter["must"]:  # type: ignore[union-attr]
        lines.append(f"- {item}")
    lines.append("")
    lines.append(heading("Themen und Begriffe", 2))
    for item in chapter["themes"]:  # type: ignore[union-attr]
        lines.append(f"- {item}")
    lines.append("")
    lines.append("Haeufige Terme aus dem Chunk:")
    lines.append(", ".join(terms))
    lines.append("")
    lines.append(heading("Typische Stolperfallen", 2))
    for item in chapter["pitfalls"]:  # type: ignore[union-attr]
        lines.append(f"- {item}")
    lines.append("")
    lines.append(heading("Exam Drill", 2))
    q_base = [
        f"Erklaere das Thema \"{chapter['title']}\" in eigenen Worten und ordne es in den Kurskontext ein.",
        f"Nenne die wichtigsten Eingaben, Ausgaben oder Begriffe aus \"{chapter['title']}\".",
        f"Beschreibe einen typischen Fehler, ein Artefakt oder eine Stolperfalle aus \"{chapter['title']}\".",
        f"Vergleiche \"{chapter['title']}\" mit einem vorherigen oder folgenden Pipeline-Schritt.",
        f"Formuliere ein Mini-Beispiel oder eine Skizzenbeschreibung zu \"{chapter['title']}\".",
    ]
    for index, question in enumerate(q_base, start=1):
        lines.append(f"{index}. {question}")
        lines.append("   Erwartung: Antwort mit Definition, Kursbegriffen und Verweis auf Seitenmarken im Kapitelchunk.")
    lines.append("")
    lines.append(heading("KI-Prompt fuer dieses Kapitel", 2))
    lines.append("Nutze ausschliesslich diesen Kapitelchunk und den Pruefungsanhang. Erstelle eine pruefungsorientierte Zusammenfassung, 15 Karteikarten, 10 Klausurfragen mit Musterantworten und eine Liste aller Formeln/Algorithmen mit Seitenmarken.")
    return "\n".join(lines)


def build_formula_file(exam_addendum: str) -> str:
    formulas = extract_section(exam_addendum, "Formel- und Notationskandidaten", "Visuelle Folien-Inventur")
    lines = [heading("Formula and Derivation Checklist")]
    lines.append("Ziel: Alles, was nach Formel, Notation, Matrix, Algorithmus oder Herleitung aussieht, separat wiederholen.")
    lines.append("")
    lines.append(heading("Pruefungsrelevante Themen", 2))
    groups = {
        "Transformationen": ["homogeneous coordinates", "translation", "rotation", "scaling", "matrix composition", "normal transformation"],
        "Projektion": ["perspective projection", "orthographic projection", "camera model", "homogeneous divide", "viewport mapping"],
        "Clipping": ["view volume tests", "line/primitive clipping", "new intersection vertices"],
        "Rasterization": ["inside test", "triangle coverage", "barycentric coordinates", "attribute interpolation"],
        "Visibility": ["z-buffer", "depth comparison", "culling", "depth precision"],
        "Illumination": ["ambient", "diffuse", "specular", "Phong", "Blinn-Phong", "normalization"],
        "Texturing": ["texture coordinates", "sampling", "filtering", "mipmaps", "aliasing"],
        "Shadows": ["shadow map", "light-space depth", "depth comparison", "bias"],
    }
    for group, items in groups.items():
        lines.append(f"- {group}: {', '.join(items)}")
    lines.append("")
    lines.append(heading("Aus dem Kurs extrahierte Formel-/Notationskandidaten", 2))
    lines.append(formulas.strip() if formulas.strip() else "[Keine Kandidaten extrahiert.]")
    lines.append("")
    lines.append(heading("So lernst du diese Datei", 2))
    lines.append("1. Jede Zeile mit Seitenmarke im Original-Kapitelchunk suchen.")
    lines.append("2. Bedeutung der Variablen notieren.")
    lines.append("3. Ein Minimalbeispiel rechnen oder verbal erklaeren.")
    lines.append("4. Pruefen, ob die Formel in einer Pipeline-Stufe verwendet wird.")
    return "\n".join(lines)


def build_visual_guide(exam_addendum: str) -> str:
    visual = extract_section(exam_addendum, "Visuelle Folien-Inventur", "Uebungsindex")
    lines = [heading("Visual Review Guide")]
    lines.append("Computergrafik-Folien enthalten viele Diagramme. Diese Datei markiert Seiten, die wegen PDF-Objekten wahrscheinlich visuell wichtig sind.")
    lines.append("")
    lines.append(heading("Arbeitsanweisung", 2))
    lines.append("- Oeffne die genannte PDF-Seite.")
    lines.append("- Schreibe in eigenen Worten: Was zeigt das Diagramm? Welche Achsen/Objekte/Pipeline-Schritte sind sichtbar?")
    lines.append("- Ergaenze die Beschreibung im jeweiligen Kapitelguide oder in deinen Notizen.")
    lines.append("- Frage eine KI danach erst, nachdem du die Bildbeschreibung mitgegeben hast.")
    lines.append("")
    lines.append(heading("Visuell dichte Seiten aus dem Audit", 2))
    lines.append(visual.strip() if visual.strip() else "[Keine visuell dichten Seiten extrahiert.]")
    return "\n".join(lines)


def build_exam_drill() -> str:
    lines = [heading("Exam Drill - Fragenkatalog")]
    lines.append("Antworten sollten immer mit Kursbegriffen und wenn moeglich Seitenmarken aus den Chunks belegt werden. Die Antwortanker sind keine vollstaendigen offiziellen Musterloesungen; sie nennen, was in einer guten Antwort vorkommen muss.")
    lines.append("")
    for chapter in CHAPTERS:
        lines.append(heading(f"Kapitel {chapter['id']}: {chapter['title']}", 2))
        must = chapter["must"]  # type: ignore[index]
        pitfalls = chapter["pitfalls"]  # type: ignore[index]
        themes = chapter["themes"]  # type: ignore[index]
        prompts = [
            (
                f"Definiere die wichtigsten Begriffe aus {chapter['title']}.",
                f"Antwortanker: {', '.join(themes[:5])}. Danach Begriffe mit Seitenmarken im Kapitelchunk belegen.",
            ),
            (
                f"Erklaere, welche Rolle {chapter['title']} im Kurs oder in der Rendering Pipeline spielt.",
                f"Antwortanker: {must[0]}",
            ),
            (
                f"Beschreibe einen typischen Algorithmus oder Ablauf aus {chapter['title']}.",
                f"Antwortanker: {must[1] if len(must) > 1 else must[0]}",
            ),
            (
                f"Nenne typische Fehler, Artefakte oder Missverstaendnisse bei {chapter['title']}.",
                f"Antwortanker: {'; '.join(pitfalls)}",
            ),
            (
                f"Erstelle eine kleine Skizzenbeschreibung zu {chapter['title']} und erklaere sie.",
                "Antwortanker: Diagramm/Skizze aus dem passenden Kapitelchunk oder Visual Review Guide waehlen, dann Achsen/Objekte/Pipeline-Schritte erklaeren.",
            ),
        ]
        for index, (prompt, answer) in enumerate(prompts, start=1):
            lines.append(f"{index}. {prompt}")
            lines.append(f"   {answer}")
        lines.append("")
    lines.append(heading("Mischfragen", 2))
    mixed = [
        "Vergleiche Clipping, Culling und Depth Testing.",
        "Erklaere den Weg eines Dreiecks von Objektkoordinaten bis zum sichtbaren Pixel.",
        "Warum braucht man homogene Koordinaten fuer Transformation und Projektion?",
        "Wie haengen Rasterization, Fragment Shader und Z-buffer zusammen?",
        "Wie beeinflussen Normalen sowohl Beleuchtung als auch Texturing/Normal Mapping?",
        "Warum sind Sampling, Aliasing und Mipmapping pruefungsrelevant?",
        "Erklaere Shadow Mapping als Sichtbarkeitsproblem aus Sicht der Lichtquelle.",
    ]
    for index, prompt in enumerate(mixed, start=1):
        lines.append(f"{index}. {prompt}")
    return "\n".join(lines)


def build_flashcards() -> str:
    rows = ["Front\tBack\tTags"]
    for front, back in FLASHCARDS:
        tag = re.sub(r"[^a-z0-9]+", "_", front.lower()).strip("_")
        rows.append(f"{front}\t{back}\tcs8165 {tag}")
    for chapter in CHAPTERS:
        chapter_tag = f"chapter_{chapter['id']}"
        for index, item in enumerate(chapter["must"], start=1):  # type: ignore[index]
            rows.append(
                f"Kapitel {chapter['id']} Must {index}\t{item}\tcs8165 {chapter_tag} must"
            )
        for index, item in enumerate(chapter["pitfalls"], start=1):  # type: ignore[index]
            rows.append(
                f"Kapitel {chapter['id']} Stolperfalle {index}\t{item}\tcs8165 {chapter_tag} pitfall"
            )
    return "\n".join(rows)


def build_exercise_map() -> str:
    lines = [heading("Exercise to Concept Map")]
    lines.append("Diese Zuordnung hilft, Uebungen als Pruefungsvorbereitung zu nutzen.")
    lines.append("")
    for number, title, concepts, chapters in EXERCISE_MAP:
        lines.append(heading(f"Uebung {number}: {title}", 2))
        lines.append(f"Zugehoerige Kapitel: {', '.join(chapters)}")
        lines.append("Konzepte:")
        for concept in concepts:
            lines.append(f"- {concept}")
        lines.append("KI-Aufgabe: Erstelle aus der Uebungsseite eine Loesungsstrategie, identifiziere benoetigte Kapitel und formuliere moegliche Pruefungsfragen.")
        lines.append("")
    return "\n".join(lines)


def build_ai_prompts() -> str:
    return """Master Prompt
=============

Nutze ausschliesslich die bereitgestellten Kursdateien aus diesem Repository. Wenn etwas nicht enthalten ist, sage klar "nicht im bereitgestellten Kursmaterial gefunden". Arbeite pruefungsorientiert, knapp, korrekt und mit Seiten-/Dateiverweisen.

Kapitel-Prompt
--------------
Ich gebe dir einen Kapitelchunk aus `course_text_parts/03_lectures/`. Erstelle:
1. eine kompakte Zusammenfassung,
2. Definitionen,
3. Formeln/Algorithmen,
4. typische Pruefungsfragen mit Musterantworten,
5. Stolperfallen,
6. eine Checkliste "kann ich / kann ich nicht".

Diagramm-Prompt
---------------
Ich gebe dir eine Folienseite oder meine Beschreibung eines Diagramms. Erklaere das Diagramm so, dass ich es in der Pruefung zeichnen und erlaeutern kann.

Drill-Prompt
------------
Pruefe mich muendlich. Stelle eine Frage, warte auf meine Antwort, bewerte streng, korrigiere Fehler und gib eine Musterantwort.
"""


def build_study_plan() -> str:
    lines = [heading("Study Plan for 100 Percent Preparation")]
    lines.append("Dieser Plan ist bewusst streng. Er setzt voraus, dass du jeden Tag aktiv abfragst, nicht nur liest.")
    lines.append("")
    schedule = [
        ("Tag 1", "Pipeline, OpenGL-Grundlagen, Kapitel 01-02"),
        ("Tag 2", "Transformationen und Projektion, Kapitel 03-04"),
        ("Tag 3", "Clipping, Rasterization, Visibility, Kapitel 05-07"),
        ("Tag 4", "Illumination, Texturing, Shadows, Kapitel 08-10"),
        ("Tag 5", "Uebungen, Formeln, visuelle Folien"),
        ("Tag 6", "Exam Drill: alle Mischfragen, Karteikarten, Schwachstellen"),
        ("Tag 7", "Simulation: 90 Minuten Pruefung mit Nachkorrektur"),
    ]
    for day, task in schedule:
        lines.append(f"- {day}: {task}")
    lines.append("")
    lines.append("Taegliche Pflicht: 20 Karteikarten, 5 freie Erklaerungen, 3 Zeichnungen/Diagramme, 1 Mini-Rechen- oder Algorithmusfrage.")
    return "\n".join(lines)


def build_readme(audit: dict[str, object]) -> str:
    summary = audit["summary"]  # type: ignore[index]
    return f"""Study Pack
==========

This folder contains exam-preparation material derived from the course export.

Coverage
--------
- Source files: {summary['source_file_count']}
- HTML files: {summary['html_file_count']}
- PDF files: {summary['pdf_file_count']}
- Extracted PDF pages: {summary['pdf_page_count']}
- Full text words: {summary['full_text_words']}

Recommended Order
-----------------
1. `ai_prompts.md`
2. `chapter_guides/`
3. `formulas_and_derivations.md`
4. `visual_review_guide.md`
5. `exam_drill.md`
6. `flashcards_anki.tsv`
7. `study_plan.md`

Limitations
-----------
This pack does not invent missing old exams, recordings, or official solutions. Visual slide interpretation still requires opening the original PDF pages listed in `visual_review_guide.md`.
"""


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)
    audit = json.loads((ROOT / "course_build_audit.json").read_text(encoding="utf-8"))
    exam_addendum = read(PARTS / "06_exam_preparation_addendum.txt")

    write(OUT / "README.md", build_readme(audit))
    write(OUT / "ai_prompts.md", build_ai_prompts())
    write(OUT / "formulas_and_derivations.md", build_formula_file(exam_addendum))
    write(OUT / "visual_review_guide.md", build_visual_guide(exam_addendum))
    write(OUT / "exam_drill.md", build_exam_drill())
    write(OUT / "flashcards_anki.tsv", build_flashcards())
    write(OUT / "exercise_concept_map.md", build_exercise_map())
    write(OUT / "study_plan.md", build_study_plan())

    for chapter in CHAPTERS:
        filename = f"{chapter['id']}_{re.sub(r'[^a-z0-9]+', '-', str(chapter['title']).lower()).strip('-')}.md"
        write(OUT / "chapter_guides" / filename, chapter_guide(chapter))

    print(f"Wrote {OUT.relative_to(ROOT).as_posix()}")
    print(f"Chapter guides: {len(CHAPTERS)}")
    flashcard_count = max(0, len((OUT / "flashcards_anki.tsv").read_text(encoding="utf-8").splitlines()) - 1)
    print(f"Flashcards: {flashcard_count}")


if __name__ == "__main__":
    main()
