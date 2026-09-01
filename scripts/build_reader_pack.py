from __future__ import annotations

import html
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reader_pack"


CHAPTERS = [
    {
        "id": "01",
        "title": "Introduction",
        "source": "course_text_parts/03_lectures/01_introduction.txt",
        "story": [
            "Computer graphics is the process of turning a model, a camera, light, material, and sampling decisions into pixels. The important exam habit is to avoid treating the final image as one magic step. Every visible result comes from a chain of coordinate changes, geometric decisions, sampling decisions, and shading decisions.",
            "The course starts by separating objects, scenes, cameras, displays, and algorithms. A scene contains geometric data and attributes. A camera defines what part of the world is observed. The rendering algorithm decides how visible surfaces are converted into samples and colors.",
            "For exam preparation, this chapter is the map. Later chapters fill in the transformations, projection, clipping, rasterization, visibility, illumination, texturing, and shadows that make the map operational.",
        ],
        "must": [
            "Explain graphics as a pipeline from scene data to image samples.",
            "Separate model data, camera setup, rendering algorithm, and output device.",
            "Use precise terms: vertex, primitive, fragment, pixel, shader, buffer, sample.",
        ],
        "pitfalls": [
            "Do not use pixel and fragment as synonyms without context.",
            "Do not explain an image only from the final color; account for visibility and sampling.",
        ],
        "try": "Draw a one-page map from object data to final image. Add one possible failure at each stage.",
        "check": [
            ("The output of rendering is best described as:", ["A set of final image samples", "Only a list of triangles", "Only a camera matrix"], 0),
            ("A fragment appears before final pixel update.", ["True", "False"], 0),
        ],
    },
    {
        "id": "02",
        "title": "Rendering Pipeline",
        "source": "course_text_parts/03_lectures/02_rendering-pipeline.txt",
        "story": [
            "The rendering pipeline organizes rendering into predictable stages. Application code supplies data and state. Vertex processing transforms vertices. Primitive assembly creates geometric primitives. Clipping removes parts outside the view. Rasterization creates fragments. Fragment processing computes candidate colors and depths. Per-fragment operations decide what reaches the framebuffer.",
            "A good mental model is that the pipeline keeps changing the representation: vertices become primitives, primitives become fragments, fragments become possible pixel updates. The pipeline is also a debugging map: if geometry is gone, ask whether it failed transformation, clipping, culling, rasterization, or depth testing.",
            "OpenGL exposes this pipeline through buffers, vertex attributes, shader programs, uniforms, textures, and framebuffer state. The exam can ask conceptually or through a small code/debugging scenario.",
        ],
        "must": [
            "Order the pipeline stages and name their inputs and outputs.",
            "Distinguish programmable stages from fixed-function decisions.",
            "Relate OpenGL objects to the stage where they matter.",
        ],
        "pitfalls": [
            "Do not blame the fragment shader for geometry that never rasterized.",
            "Do not forget state: depth test, face culling, viewport, and bound objects matter.",
        ],
        "try": "Given a black screen, list five pipeline checkpoints in the order you would inspect them.",
        "check": [
            ("Rasterization primarily converts:", ["Primitives into fragments", "Textures into vertices", "Pixels into triangles"], 0),
            ("Depth testing happens before primitive assembly.", ["True", "False"], 1),
        ],
    },
    {
        "id": "03",
        "title": "Geometric Transformations",
        "source": "course_text_parts/03_lectures/03_geometric-transformations.txt",
        "story": [
            "Transformations move geometry between coordinate systems. Object coordinates describe a model locally. World coordinates place the model in a scene. View coordinates describe the scene relative to the camera. Clip coordinates prepare geometry for projection and clipping.",
            "Homogeneous coordinates make translation, rotation, scaling, and projection fit into matrix multiplication. The order of multiplication matters because matrix multiplication is not commutative. A rotation followed by a translation is not the same as the reverse.",
            "For exam tasks, write the coordinate space before and after each matrix. This prevents most transformation mistakes and makes formula questions easier to check.",
        ],
        "must": [
            "Explain homogeneous coordinates and why they are useful.",
            "Apply translation, rotation, scaling, and composition conceptually.",
            "Track object, world, view, clip, normalized device, and screen coordinates.",
        ],
        "pitfalls": [
            "Do not swap transformation order casually.",
            "Do not mix vectors from different coordinate systems in lighting or camera formulas.",
        ],
        "try": "Create a small chain: model matrix, view matrix, projection matrix. Label the coordinate space after each multiplication.",
        "check": [
            ("Matrix order matters because:", ["Matrix multiplication is generally not commutative", "Vectors have no coordinates", "Projection removes all matrices"], 0),
            ("Translation is naturally represented in a 4x4 homogeneous matrix.", ["True", "False"], 0),
        ],
    },
    {
        "id": "04",
        "title": "Geometric Projection",
        "source": "course_text_parts/03_lectures/04_geometric-projection.txt",
        "story": [
            "Projection maps view-space geometry into a form that can become a 2D image. Orthographic projection keeps parallel lines parallel and does not shrink distant objects. Perspective projection models foreshortening: objects farther away appear smaller.",
            "The perspective divide is central. After projection, coordinates are divided by the homogeneous component to reach normalized device coordinates. This is why homogeneous coordinates are not just notation; they make perspective projection possible inside the pipeline.",
            "Projection also defines the viewing volume. Near and far planes, field of view, and aspect ratio affect what is visible and how depth precision is distributed.",
        ],
        "must": [
            "Compare orthographic and perspective projection.",
            "Explain the role of the perspective divide.",
            "Relate field of view, aspect ratio, near plane, and far plane to the viewing volume.",
        ],
        "pitfalls": [
            "Do not describe perspective as only a 2D scaling trick.",
            "Do not place the near plane at zero in a standard perspective setup.",
        ],
        "try": "Sketch the same cube under orthographic and perspective projection and label the difference.",
        "check": [
            ("Perspective projection usually makes distant objects:", ["Appear smaller", "Keep exactly the same apparent size", "Disappear before clipping"], 0),
            ("The perspective divide happens after projection to reach normalized device coordinates.", ["True", "False"], 0),
        ],
    },
    {
        "id": "05",
        "title": "Clipping",
        "source": "course_text_parts/03_lectures/05_clipping.txt",
        "story": [
            "Clipping removes parts of primitives outside the view volume. It is not the same as culling and not the same as depth testing. Clipping can create new vertices where a primitive crosses a clipping boundary.",
            "The reason clipping exists is practical: the rasterizer should receive geometry that can be meaningfully converted into fragments inside the view. Clipping also protects the pipeline from invalid geometry around projection boundaries.",
            "In exam answers, always state the clipping space or boundary being used. A vague statement like 'outside the screen is removed' loses precision because clipping normally happens before final screen mapping.",
        ],
        "must": [
            "Define clipping as cutting primitives against a volume or boundary.",
            "Distinguish clipping from culling and depth testing.",
            "Explain why clipping can introduce new vertices.",
        ],
        "pitfalls": [
            "Do not say clipping removes whole triangles only; partial primitives can be clipped.",
            "Do not confuse the view volume with the final framebuffer rectangle.",
        ],
        "try": "Draw a line crossing a rectangular window. Mark the kept segment and the two intersection points.",
        "check": [
            ("When a triangle crosses the view boundary, clipping may:", ["Create new boundary vertices", "Always delete the whole triangle", "Only change the texture image"], 0),
            ("Clipping and depth testing solve the same problem.", ["True", "False"], 1),
        ],
    },
    {
        "id": "06",
        "title": "Rasterization",
        "source": "course_text_parts/03_lectures/06_rasterization.txt",
        "story": [
            "Rasterization determines which samples or pixels are covered by a primitive and creates fragments for later processing. It bridges continuous geometry and the discrete image grid.",
            "This chapter is where sampling, interpolation, and aliasing become visible. Attributes such as depth, color, normals, and texture coordinates can be interpolated across a primitive before fragment shading.",
            "Exam questions often test the difference between the geometric primitive and the generated fragments. A triangle may cover many samples, no samples, or a pattern of samples depending on placement and sampling rules.",
        ],
        "must": [
            "Explain rasterization as primitive-to-fragment conversion.",
            "Describe attribute interpolation across a primitive.",
            "Connect sampling decisions to aliasing and image quality.",
        ],
        "pitfalls": [
            "Do not say rasterization computes final visibility by itself.",
            "Do not forget that interpolation happens before many fragment computations.",
        ],
        "try": "Place a small triangle over a pixel grid and mark which samples become fragments.",
        "check": [
            ("Rasterization produces:", ["Fragments", "Only final visible pixels", "Only vertex shader code"], 0),
            ("Texture coordinates can be interpolated across a primitive.", ["True", "False"], 0),
        ],
    },
    {
        "id": "07",
        "title": "Visibility Determination",
        "source": "course_text_parts/03_lectures/07_visibility-determination.txt",
        "story": [
            "Visibility determination decides what can be seen from the current viewpoint. Back-face culling can remove geometry based on orientation. View-frustum culling can reject objects outside the camera volume. Depth buffering resolves occlusion per fragment by comparing depth values.",
            "The Z-buffer is a central practical algorithm: keep a depth value for each sample or pixel and update the color only when a fragment is closer according to the chosen depth test.",
            "Visibility is view-dependent. The same object can be visible, hidden, clipped, or culled depending on the camera, projection, and state.",
        ],
        "must": [
            "Explain culling, clipping, and depth testing separately.",
            "Describe the Z-buffer idea and its update rule.",
            "Name depth precision issues and why near/far settings matter.",
        ],
        "pitfalls": [
            "Do not call culling a pixel-level decision.",
            "Do not ignore depth buffer initialization and depth test state in OpenGL debugging.",
        ],
        "try": "Simulate two overlapping fragments with depths 0.2 and 0.7 under a less-than depth test.",
        "check": [
            ("The Z-buffer stores:", ["Depth values used for visibility", "Only texture colors", "Shader source code"], 0),
            ("Back-face culling is based on orientation, not per-pixel depth.", ["True", "False"], 0),
        ],
    },
    {
        "id": "08",
        "title": "Local Illumination",
        "source": "course_text_parts/03_lectures/08_local-illumination.txt",
        "story": [
            "Local illumination estimates the color of a surface point from local information such as normal direction, light direction, view direction, material coefficients, and light intensity. It does not fully simulate indirect global light transport unless an approximation is added.",
            "Typical components are ambient, diffuse, and specular terms. Diffuse reflection depends on the angle between the normal and the light direction. Specular reflection models shiny highlights and also depends on the view direction.",
            "For exam work, normalize vectors and state the coordinate system. Many wrong lighting answers come from mixing spaces or using an unnormalized normal.",
        ],
        "must": [
            "Separate ambient, diffuse, and specular contributions.",
            "Explain the role of normals, light direction, view direction, and material parameters.",
            "Compare Phong-style and Blinn-Phong-style specular reasoning qualitatively.",
        ],
        "pitfalls": [
            "Do not use a normal from object space with a light vector in view space.",
            "Do not call local illumination a full solution for indirect light.",
        ],
        "try": "For a surface facing away from a light, decide what happens to the diffuse term.",
        "check": [
            ("Diffuse reflection mainly depends on:", ["The angle between normal and light direction", "Only the screen resolution", "Only the texture filename"], 0),
            ("Local illumination normally ignores full indirect light transport.", ["True", "False"], 0),
        ],
    },
    {
        "id": "09",
        "title": "Texturing",
        "source": "course_text_parts/03_lectures/09_texturing.txt",
        "story": [
            "A texture is sampled data used during rendering. It is often an image, but conceptually it can store many kinds of values. Texture coordinates map a point on a primitive to a lookup in texture space.",
            "Filtering decides how a texture value is reconstructed from discrete texels. Nearest filtering is simple but blocky. Linear filtering blends neighboring texels. Mipmapping helps reduce aliasing when a texture is seen at smaller scale.",
            "Texturing is connected to rasterization because interpolated texture coordinates are used per fragment. It is connected to shading because the sampled value can affect color, normals, material coefficients, or other shader inputs.",
        ],
        "must": [
            "Define texture coordinates and texture sampling.",
            "Compare nearest filtering, linear filtering, and mipmapping qualitatively.",
            "Name different uses of textures beyond color maps.",
        ],
        "pitfalls": [
            "Do not define a texture as only a picture pasted onto an object.",
            "Do not confuse geometry resolution with texture sampling quality.",
        ],
        "try": "Explain why a distant checkerboard texture can shimmer without mipmapping.",
        "check": [
            ("Mipmaps mainly help with:", ["Reducing aliasing for minified textures", "Replacing the projection matrix", "Deleting hidden triangles"], 0),
            ("Texture coordinates are interpolated during rasterization for fragment use.", ["True", "False"], 0),
        ],
    },
    {
        "id": "10",
        "title": "Shadows",
        "source": "course_text_parts/03_lectures/10_shadows.txt",
        "story": [
            "Shadows are another visibility problem: is a surface point visible from the light source? Shadow mapping answers this with two passes. First render depth from the light's point of view into a shadow map. Then render the camera view and compare each relevant point against the stored light-space depth.",
            "The method is practical and widely used, but it has artifacts. Shadow acne comes from self-shadowing precision issues. Peter panning can appear when bias is too large. Resolution and projection choices affect shadow sharpness and stability.",
            "The exam pattern is predictable: explain the two passes, identify what the shadow map stores, describe the comparison, and name common artifacts plus their causes.",
        ],
        "must": [
            "Explain shadows as light-source visibility.",
            "Describe the two-pass shadow mapping algorithm.",
            "Name shadow acne, bias, peter panning, resolution limits, and sampling issues.",
        ],
        "pitfalls": [
            "Do not say a shadow map stores final colors; it stores depth from the light.",
            "Do not treat bias as free: too little and too much both cause artifacts.",
        ],
        "try": "Write the two shadow-mapping passes as pseudocode with one line for the depth comparison.",
        "check": [
            ("A shadow map stores:", ["Depth from the light's view", "Final camera colors", "Only mesh filenames"], 0),
            ("Bias can reduce acne but may detach shadows.", ["True", "False"], 0),
        ],
    },
]


OPENGL_LABS = [
    {
        "title": "Black Screen Debugging",
        "prompt": "You render a triangle but the window is black. Choose the first checks in pipeline order.",
        "answer": "Check shader compilation/linking, vertex array/buffer binding and attribute layout, transformation/projection, viewport, draw call, face culling, depth test, and fragment output.",
    },
    {
        "title": "Depth Buffer Experiment",
        "prompt": "Render two overlapping triangles with and without depth testing. Predict the difference before running it.",
        "answer": "Without depth testing, later draw order can dominate. With depth testing, the nearer fragment wins according to the depth function and depth buffer contents.",
    },
    {
        "title": "Texture Filtering Toggle",
        "prompt": "Switch between nearest, linear, and mipmapped filtering on a checkerboard texture.",
        "answer": "Nearest looks blocky, linear blends neighboring texels, and mipmapping reduces shimmer/aliasing when the texture is minified.",
    },
    {
        "title": "Shadow Bias Slider",
        "prompt": "Increase and decrease shadow bias in a shadow-mapping example.",
        "answer": "Too little bias causes self-shadowing acne. Too much bias can detach the shadow from the caster.",
    },
]


SOURCE_BUNDLE_FILES = [
    "course_text_parts/01_course_overview.txt",
    "course_text_parts/02_organization.txt",
    "course_text_parts/03_lectures/00_lectures_index.txt",
    "course_text_parts/03_lectures/01_introduction.txt",
    "course_text_parts/03_lectures/02_rendering-pipeline.txt",
    "course_text_parts/03_lectures/03_geometric-transformations.txt",
    "course_text_parts/03_lectures/04_geometric-projection.txt",
    "course_text_parts/03_lectures/05_clipping.txt",
    "course_text_parts/03_lectures/06_rasterization.txt",
    "course_text_parts/03_lectures/07_visibility-determination.txt",
    "course_text_parts/03_lectures/08_local-illumination.txt",
    "course_text_parts/03_lectures/09_texturing.txt",
    "course_text_parts/03_lectures/10_shadows.txt",
    "course_text_parts/04_assignments/00_assignments_index.txt",
    "course_text_parts/04_assignments/00_introduction-to-cpp.txt",
    "course_text_parts/04_assignments/01_rendering-pipeline.txt",
    "course_text_parts/04_assignments/02_primitive-types-shaders.txt",
    "course_text_parts/04_assignments/03_geometric-transformations.txt",
    "course_text_parts/04_assignments/04_projections-and-clipping.txt",
    "course_text_parts/04_assignments/05_rasterization.txt",
    "course_text_parts/04_assignments/Bonus_rendering-contest.txt",
    "course_text_parts/05_opengl_starter_project.txt",
]


def heading(text: str, level: int = 1) -> str:
    return f"{'#' * level} {text}"


def write_markdown() -> None:
    lines: list[str] = []
    lines.append(heading("CS8165.001 Narrative Reader"))
    lines.append("")
    lines.append(heading("Pipeline Overview", 2))
    lines.append("")
    lines.append("The central route is: application data -> vertex processing -> primitive assembly -> clipping/culling decisions -> rasterization -> fragment shading -> per-fragment tests -> framebuffer. The same route explains most conceptual questions and most OpenGL debugging questions.")
    lines.append("")
    for chapter in CHAPTERS:
        lines.append(heading(f"{chapter['id']} - {chapter['title']}", 2))
        lines.append("")
        lines.append(f"Source chunk: `{chapter['source']}`")
        lines.append("")
        lines.append(heading("Narrative Explanation", 3))
        lines.append("")
        for paragraph in chapter["story"]:
            lines.append(paragraph)
            lines.append("")
        lines.append(heading("Must Know", 3))
        lines.append("")
        for item in chapter["must"]:
            lines.append(f"- {item}")
        lines.append("")
        lines.append(heading("Common Pitfalls", 3))
        lines.append("")
        for item in chapter["pitfalls"]:
            lines.append(f"- {item}")
        lines.append("")
        lines.append(heading("Try It", 3))
        lines.append("")
        lines.append(chapter["try"])
        lines.append("")
        lines.append(heading("Closed Checks", 3))
        lines.append("")
        for idx, (question, options, answer) in enumerate(chapter["check"], start=1):
            lines.append(f"{idx}. {question}")
            for opt_index, option in enumerate(options):
                marker = chr(ord("A") + opt_index)
                lines.append(f"   - {marker}. {option}")
            lines.append(f"   - Answer: {chr(ord('A') + answer)}")
        lines.append("")
    lines.append(heading("Software And OpenGL Try-Out Labs", 2))
    lines.append("")
    lines.append("These tasks are meant to be clicked through or tried in a minimal OpenGL project. Predict first, then run or inspect the code, then explain the result using pipeline language.")
    lines.append("")
    for lab in OPENGL_LABS:
        lines.append(heading(lab["title"], 3))
        lines.append("")
        lines.append(f"Task: {lab['prompt']}")
        lines.append("")
        lines.append(f"Expected reasoning: {lab['answer']}")
        lines.append("")
    (OUT / "narrative_reader.md").write_text("\n".join(lines), encoding="utf-8")


def write_language_audit() -> None:
    audit = {
        "raw_source_language_policy": "Preserve original extracted course text exactly as source material. The course is primarily English; Moodle interface or notification text may be German when exported that way.",
        "generated_reader_pack_language": "English, because it is the primary language of the lecture material.",
        "older_generated_pack_note": "Some earlier helper files contain German study instructions because they were generated from German user requests. They are support material, not raw source text. Use reader_pack for original-language guided reading.",
        "complete_source_anchor": "course_full_text.txt and course_text_parts/",
    }
    lines = [heading("Language Audit"), ""]
    for key, value in audit.items():
        lines.append(f"- `{key}`: {value}")
    lines.append("")
    lines.append("Practical rule: if you feed files to another AI and want original-language output, start with `reader_pack/narrative_reader.md`, then add the matching lecture chunk from `course_text_parts/03_lectures/`.")
    (OUT / "language_audit.md").write_text("\n".join(lines), encoding="utf-8")


def write_readme() -> None:
    lines = [
        heading("Reader Pack"),
        "",
        "- `narrative_reader.md` - chapter-by-chapter commented reader in English",
        "- `original_language_ai_bundle.txt` - AI-ready bundle with the English reader plus source chunks in their exported language",
        "- `icg_narrative_reader.pdf` - printable/browsable PDF version of the reader",
        "- `interactive_workbook.html` - self-contained clickable practice workbook",
        "- `language_audit.md` - source-language policy and what to feed into AI tools",
        "",
        heading("Reading Order", 2),
        "",
        "1. Read one chapter in `narrative_reader.md` or the PDF.",
        "2. Open the source chunk listed at the top of the chapter.",
        "3. Do the `Try It` task without notes.",
        "4. Use `interactive_workbook.html` for closed checks and software scenarios.",
        "5. Send wrong answers to `overprep_pack/mistake_log.md`.",
        "",
        "For AI input in original language, use `original_language_ai_bundle.txt` first. It avoids the older German helper prompts and keeps source chunks in their exported language.",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_ai_bundle() -> None:
    lines = [
        "CS8165.001 ORIGINAL-LANGUAGE AI BUNDLE",
        "",
        "",
        "=" * 80,
        "PART 1 - NARRATIVE READER",
        "=" * 80,
        "",
        (OUT / "narrative_reader.md").read_text(encoding="utf-8"),
        "",
        "=" * 80,
        "PART 2 - SOURCE CHUNKS IN EXPORTED LANGUAGE",
        "=" * 80,
    ]
    missing = []
    for rel in SOURCE_BUNDLE_FILES:
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)
            continue
        lines.extend(["", "-" * 80, f"SOURCE FILE: {rel}", "-" * 80, ""])
        lines.append(path.read_text(encoding="utf-8", errors="replace"))
    if missing:
        lines.extend(["", "MISSING SOURCE FILES", ""])
        lines.extend(f"- {item}" for item in missing)
    bundle = normalize_bundle_wrappers("\n".join(lines))
    (OUT / "original_language_ai_bundle.txt").write_text(bundle, encoding="utf-8")


def normalize_bundle_wrappers(text: str) -> str:
    """Translate generated wrapper labels while leaving source text otherwise intact."""
    replacements = {
        "Kapitel ": "Chapter ",
        " - Moodle-Seite": " - Moodle page",
        " - Folien": " - Slides",
        "(Aufgabe)": "(Assignment)",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def write_html() -> None:
    chapter_cards = []
    for chapter in CHAPTERS:
        checks = []
        for check_index, (question, options, answer) in enumerate(chapter["check"], start=1):
            buttons = []
            for option_index, option in enumerate(options):
                correct = option_index == answer
                buttons.append(
                    f'<button class="choice" data-correct="{str(correct).lower()}">{html.escape(chr(ord("A") + option_index) + ". " + option)}</button>'
                )
            checks.append(
                f"""
                <div class="question">
                  <p>{html.escape(str(check_index) + ". " + question)}</p>
                  <div class="choices">{''.join(buttons)}</div>
                  <p class="feedback" aria-live="polite"></p>
                </div>
                """
            )
        chapter_cards.append(
            f"""
            <section class="chapter" id="chapter-{chapter['id']}">
              <div class="chapter-head">
                <span>{chapter['id']}</span>
                <h2>{html.escape(chapter['title'])}</h2>
                <a href="../{html.escape(chapter['source'])}">source chunk</a>
              </div>
              <p>{html.escape(chapter['story'][0])}</p>
              <details>
                <summary>Must know</summary>
                <ul>{''.join(f'<li>{html.escape(item)}</li>' for item in chapter['must'])}</ul>
              </details>
              <details>
                <summary>Try it</summary>
                <p>{html.escape(chapter['try'])}</p>
              </details>
              <div class="checks">{''.join(checks)}</div>
            </section>
            """
        )
    labs = []
    for lab in OPENGL_LABS:
        labs.append(
            f"""
            <section class="lab">
              <h3>{html.escape(lab['title'])}</h3>
              <p>{html.escape(lab['prompt'])}</p>
              <button class="reveal">Reveal expected reasoning</button>
              <p class="answer" hidden>{html.escape(lab['answer'])}</p>
            </section>
            """
        )
    svg = """
    <svg class="pipeline-svg" viewBox="0 0 960 140" role="img" aria-label="Rendering pipeline overview">
      <defs>
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
          <path d="M0,0 L0,6 L9,3 z" fill="#284b63"></path>
        </marker>
      </defs>
      <g fill="#f2f6f8" stroke="#284b63" stroke-width="2">
        <rect x="20" y="45" width="110" height="50" rx="6"></rect>
        <rect x="165" y="45" width="110" height="50" rx="6"></rect>
        <rect x="310" y="45" width="110" height="50" rx="6"></rect>
        <rect x="455" y="45" width="110" height="50" rx="6"></rect>
        <rect x="600" y="45" width="110" height="50" rx="6"></rect>
        <rect x="745" y="45" width="170" height="50" rx="6"></rect>
      </g>
      <g stroke="#284b63" stroke-width="2" marker-end="url(#arrow)">
        <line x1="130" y1="70" x2="160" y2="70"></line>
        <line x1="275" y1="70" x2="305" y2="70"></line>
        <line x1="420" y1="70" x2="450" y2="70"></line>
        <line x1="565" y1="70" x2="595" y2="70"></line>
        <line x1="710" y1="70" x2="740" y2="70"></line>
      </g>
      <g fill="#111" font-family="Arial, sans-serif" font-size="15" text-anchor="middle">
        <text x="75" y="75">Vertices</text>
        <text x="220" y="75">Primitives</text>
        <text x="365" y="75">Clipping</text>
        <text x="510" y="75">Rasterize</text>
        <text x="655" y="75">Fragments</text>
        <text x="830" y="75">Tests + Framebuffer</text>
      </g>
    </svg>
    """
    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CS8165.001 Interactive Workbook</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #172026;
      --muted: #596870;
      --line: #cbd6dc;
      --bg: #f7f8f5;
      --panel: #ffffff;
      --accent: #2f6f73;
      --accent-2: #8a5a44;
      --ok: #1d7a46;
      --bad: #a33a33;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      color: var(--ink);
      background: var(--bg);
      line-height: 1.5;
    }}
    header {{
      padding: 28px max(20px, 6vw) 18px;
      background: #fff;
      border-bottom: 1px solid var(--line);
    }}
    h1 {{ margin: 0 0 8px; font-size: 30px; letter-spacing: 0; }}
    header p {{ margin: 0; max-width: 920px; color: var(--muted); }}
    nav {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      padding: 14px max(20px, 6vw);
      background: #edf3f1;
      border-bottom: 1px solid var(--line);
      position: sticky;
      top: 0;
      z-index: 2;
    }}
    nav a {{
      color: var(--ink);
      text-decoration: none;
      border: 1px solid var(--line);
      background: #fff;
      padding: 6px 9px;
      border-radius: 6px;
      font-size: 14px;
    }}
    main {{ padding: 22px max(20px, 6vw) 48px; }}
    .band {{
      max-width: 1120px;
      margin: 0 auto 22px;
      padding: 18px 0;
    }}
    .pipeline-svg {{
      width: 100%;
      max-width: 960px;
      display: block;
      margin: 12px 0 0;
      background: #fff;
      border: 1px solid var(--line);
    }}
    .chapter, .lab {{
      max-width: 1120px;
      margin: 0 auto 16px;
      padding: 18px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    .chapter-head {{
      display: grid;
      grid-template-columns: 48px 1fr auto;
      gap: 12px;
      align-items: center;
      border-bottom: 1px solid var(--line);
      padding-bottom: 10px;
      margin-bottom: 12px;
    }}
    .chapter-head span {{
      width: 40px;
      height: 40px;
      display: inline-grid;
      place-items: center;
      border-radius: 6px;
      color: #fff;
      background: var(--accent);
      font-weight: 700;
    }}
    h2, h3 {{ margin: 0; letter-spacing: 0; }}
    .chapter-head a {{ color: var(--accent); }}
    details {{
      border-top: 1px solid var(--line);
      padding-top: 10px;
      margin-top: 10px;
    }}
    summary {{ cursor: pointer; font-weight: 700; }}
    .checks {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
      margin-top: 14px;
    }}
    .question {{
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      background: #fbfcfc;
    }}
    .question p {{ margin: 0 0 10px; }}
    .choices {{
      display: grid;
      gap: 8px;
    }}
    button {{
      font: inherit;
      cursor: pointer;
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      border-radius: 6px;
      padding: 8px 10px;
      text-align: left;
    }}
    button:hover {{ border-color: var(--accent); }}
    button.correct {{ border-color: var(--ok); background: #eaf6ef; }}
    button.wrong {{ border-color: var(--bad); background: #faeeee; }}
    .feedback {{ min-height: 22px; font-weight: 700; }}
    .lab .answer {{
      border-left: 4px solid var(--accent-2);
      padding: 8px 12px;
      background: #f8f1ed;
    }}
    @media (max-width: 680px) {{
      .chapter-head {{ grid-template-columns: 44px 1fr; }}
      .chapter-head a {{ grid-column: 2; }}
      h1 {{ font-size: 25px; }}
      nav {{ position: static; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>CS8165.001 Interactive Workbook</h1>
    <p>Closed-format practice in the course's primary language. Predict first, click second, then repair every wrong answer in the mistake log.</p>
  </header>
  <nav>
    {''.join(f'<a href="#chapter-{c["id"]}">{c["id"]}</a>' for c in CHAPTERS)}
    <a href="#labs">Labs</a>
  </nav>
  <main>
    <section class="band">
      <h2>Pipeline Map</h2>
      {svg}
    </section>
    {''.join(chapter_cards)}
    <section class="band" id="labs">
      <h2>Software And OpenGL Labs</h2>
      <p>Use these as practical checks when you can open a starter project or inspect a minimal OpenGL example.</p>
    </section>
    {''.join(labs)}
  </main>
  <script>
    document.querySelectorAll(".choice").forEach((button) => {{
      button.addEventListener("click", () => {{
        const group = button.closest(".question");
        group.querySelectorAll(".choice").forEach((b) => b.classList.remove("correct", "wrong"));
        const ok = button.dataset.correct === "true";
        button.classList.add(ok ? "correct" : "wrong");
        group.querySelector(".feedback").textContent = ok ? "Correct." : "Not correct. Re-read the source chunk and try again.";
      }});
    }});
    document.querySelectorAll(".reveal").forEach((button) => {{
      button.addEventListener("click", () => {{
        const answer = button.nextElementSibling;
        answer.hidden = !answer.hidden;
        button.textContent = answer.hidden ? "Reveal expected reasoning" : "Hide expected reasoning";
      }});
    }});
  </script>
</body>
</html>
"""
    (OUT / "interactive_workbook.html").write_text(page, encoding="utf-8")


def add_wrapped_paragraph(story, text: str, style) -> None:
    from reportlab.platypus import Paragraph

    story.append(Paragraph(html.escape(text), style))


def write_pdf() -> None:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    pdf_path = OUT / "icg_narrative_reader.pdf"
    styles = getSampleStyleSheet()
    styles["Title"].fontName = "Helvetica-Bold"
    styles["Heading1"].fontName = "Helvetica-Bold"
    styles["Heading2"].fontName = "Helvetica-Bold"
    styles["BodyText"].fontName = "Helvetica"
    styles["BodyText"].fontSize = 10.5
    styles["BodyText"].leading = 14

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#596870"))
        canvas.drawString(1.7 * cm, 1.1 * cm, "CS8165.001 Narrative Reader")
        canvas.drawRightString(A4[0] - 1.7 * cm, 1.1 * cm, f"Page {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=1.7 * cm,
        rightMargin=1.7 * cm,
        topMargin=1.6 * cm,
        bottomMargin=1.6 * cm,
        title="CS8165.001 Narrative Reader",
    )
    story = []
    story.append(Paragraph("CS8165.001 Narrative Reader", styles["Title"]))
    story.append(Spacer(1, 10))
    add_wrapped_paragraph(
        story,
        "A readable original-language companion for Interactive Computer Graphics. Use it with the complete source export and lecture chunks.",
        styles["BodyText"],
    )
    story.append(Spacer(1, 12))
    overview_data = [
        ["Stage", "Question to ask"],
        ["Input", "What geometry, attributes, camera, material, and state are provided?"],
        ["Transform", "Which coordinate space is used now?"],
        ["Clip/Cull", "What is removed before rasterization?"],
        ["Rasterize", "Which fragments are generated and which attributes are interpolated?"],
        ["Shade/Test", "Which color/depth result reaches the framebuffer?"],
    ]
    table = Table(overview_data, colWidths=[3.2 * cm, 12.2 * cm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2f6f73")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#cbd6dc")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f2f6f8")]),
            ]
        )
    )
    story.append(table)
    story.append(PageBreak())

    for chapter in CHAPTERS:
        story.append(Paragraph(f"{chapter['id']} - {chapter['title']}", styles["Heading1"]))
        story.append(Paragraph(f"Source chunk: {chapter['source']}", styles["BodyText"]))
        story.append(Spacer(1, 8))
        story.append(Paragraph("Narrative explanation", styles["Heading2"]))
        for paragraph in chapter["story"]:
            add_wrapped_paragraph(story, paragraph, styles["BodyText"])
            story.append(Spacer(1, 5))
        story.append(Paragraph("Must know", styles["Heading2"]))
        for item in chapter["must"]:
            add_wrapped_paragraph(story, f"- {item}", styles["BodyText"])
        story.append(Paragraph("Common pitfalls", styles["Heading2"]))
        for item in chapter["pitfalls"]:
            add_wrapped_paragraph(story, f"- {item}", styles["BodyText"])
        story.append(Paragraph("Try it", styles["Heading2"]))
        add_wrapped_paragraph(story, chapter["try"], styles["BodyText"])
        story.append(Paragraph("Closed checks", styles["Heading2"]))
        for index, (question, options, answer) in enumerate(chapter["check"], start=1):
            add_wrapped_paragraph(story, f"{index}. {question}", styles["BodyText"])
            for opt_index, option in enumerate(options):
                add_wrapped_paragraph(story, f"   {chr(ord('A') + opt_index)}. {option}", styles["BodyText"])
            add_wrapped_paragraph(story, f"   Answer: {chr(ord('A') + answer)}", styles["BodyText"])
        story.append(PageBreak())

    story.append(Paragraph("Software And OpenGL Try-Out Labs", styles["Heading1"]))
    for lab in OPENGL_LABS:
        story.append(Paragraph(lab["title"], styles["Heading2"]))
        add_wrapped_paragraph(story, f"Task: {lab['prompt']}", styles["BodyText"])
        add_wrapped_paragraph(story, f"Expected reasoning: {lab['answer']}", styles["BodyText"])
        story.append(Spacer(1, 8))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def write_manifest() -> None:
    audit_path = ROOT / "course_build_audit.json"
    audit = json.loads(audit_path.read_text(encoding="utf-8")) if audit_path.exists() else {}
    manifest = {
        "pack": "reader_pack",
        "language": "English generated explanations; original source text remains in its exported language.",
        "chapters": len(CHAPTERS),
        "opengl_labs": len(OPENGL_LABS),
        "source_audit_checks": audit.get("checks", {}),
        "files": [
            "README.md",
            "narrative_reader.md",
            "original_language_ai_bundle.txt",
            "icg_narrative_reader.pdf",
            "interactive_workbook.html",
            "language_audit.md",
        ],
    }
    (OUT / "reader_pack_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    write_markdown()
    write_ai_bundle()
    write_language_audit()
    write_readme()
    write_html()
    write_pdf()
    write_manifest()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
