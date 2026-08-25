from __future__ import annotations

import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "practice_pack"


CHAPTERS = [
    ("01", "Introduction"),
    ("02", "Rendering Pipeline"),
    ("03", "Geometric Transformations"),
    ("04", "Geometric Projection"),
    ("05", "Clipping"),
    ("06", "Rasterization"),
    ("07", "Visibility Determination"),
    ("08", "Local Illumination"),
    ("09", "Texturing"),
    ("10", "Shadows"),
]


CLOZE_TEXTS = [
    (
        "Rendering Pipeline",
        "In object-based rendering, a scene is represented by primitives such as triangles. "
        "The rendering pipeline transforms vertices through several coordinate systems, assembles primitives, "
        "rasterizes them into fragments, executes fragment processing, applies tests such as the depth test, "
        "and finally writes surviving results into the framebuffer. A fragment is only a pixel candidate; "
        "it becomes visible only if it survives the later tests and operations.",
    ),
    (
        "OpenGL and Shaders",
        "OpenGL rendering is controlled by API calls, objects, buffers, state, and programmable shaders. "
        "A vertex shader usually transforms vertex positions and forwards attributes. A fragment shader computes "
        "per-fragment outputs such as color. The final image also depends on fixed-function operations such as "
        "depth testing, blending, and framebuffer configuration.",
    ),
    (
        "Geometric Transformations",
        "Geometric transformations position, orient, and scale models. Homogeneous coordinates make it possible "
        "to represent translation, rotation, scaling, and projection in matrix form. Transformation order matters "
        "because matrix multiplication is not commutative. Points, directions, and normals must be handled carefully, "
        "especially when non-uniform scaling is used.",
    ),
    (
        "Projection",
        "Projection maps three-dimensional geometry to a two-dimensional image. Orthographic projection preserves "
        "parallel lines and does not create perspective shortening. Perspective projection makes distant objects "
        "appear smaller and relies on homogeneous coordinates and the perspective divide. The camera model, view volume, "
        "projection matrix, and viewport mapping are all part of the path from world coordinates to screen coordinates.",
    ),
    (
        "Clipping",
        "Clipping removes or cuts parts of primitives outside the relevant view or clip region. Analytical clipping "
        "happens before rasterization and may create new vertices where a primitive intersects a clipping boundary. "
        "Pixel-based clipping happens later and keeps only pixels or fragments inside a clip region. Clipping is not "
        "the same as culling, because culling rejects whole primitives based on tests such as orientation or volume.",
    ),
    (
        "Rasterization",
        "Rasterization converts geometric primitives into fragments on a raster grid. For triangles, rasterization "
        "requires deciding which sample positions are covered by the triangle. Attributes such as depth, color, "
        "normals, and texture coordinates are interpolated across the primitive, often using barycentric coordinates. "
        "Rasterization happens before final visibility decisions such as the depth test.",
    ),
    (
        "Visibility",
        "Visibility determination decides which parts of a scene are visible from the current camera. The z-buffer "
        "algorithm stores depth values and compares incoming fragment depths against previously stored values. "
        "Back-face culling can reject surfaces pointing away from the camera for closed opaque objects. Depth precision, "
        "occlusion, and viewpoint dependence are common sources of mistakes.",
    ),
    (
        "Local Illumination",
        "Local illumination computes direct lighting at a surface point. Common models combine ambient, diffuse, "
        "and specular components. Diffuse reflection depends on the angle between the surface normal and the light "
        "direction. Specular reflection depends on the view direction and models highlights. Phong and Blinn-Phong "
        "are common local illumination models.",
    ),
    (
        "Texturing",
        "A texture is a sampled data field used during rendering. Texture coordinates map a surface point to a lookup "
        "in texture space. A texel is a texture sample. Filtering determines how texture values are reconstructed "
        "between samples, and mipmapping uses prefiltered levels to reduce aliasing when textures are minified.",
    ),
    (
        "Shadows",
        "Shadow computation can be treated as a visibility problem from the light source. In shadow mapping, the scene "
        "is first rendered from the light to store a depth map. During normal rendering, a fragment is transformed into "
        "light space and compared against the stored light-space depth. Bias, resolution, and sampling influence shadow "
        "artifacts such as acne or detached shadows.",
    ),
]


MATCHING_PAIRS = [
    ("Vertex", "A point with attributes such as position, normal, color, or texture coordinates.", "02"),
    ("Primitive", "A geometric unit assembled from vertices, commonly a triangle.", "02"),
    ("Fragment", "A pixel candidate produced by rasterization before final tests.", "02"),
    ("Framebuffer", "Storage for rendered output and related buffers such as color and depth.", "02"),
    ("Vertex shader", "Programmable stage that processes vertices and often applies transformations.", "02"),
    ("Fragment shader", "Programmable stage that computes per-fragment outputs such as color.", "02"),
    ("Homogeneous coordinates", "Coordinate representation enabling affine transformations and perspective projection.", "03"),
    ("Affine transformation", "Line-preserving transformation such as translation, rotation, scaling, or shear.", "03"),
    ("View transformation", "Transforms world-space coordinates into camera/view space.", "04"),
    ("Projection matrix", "Maps view-space geometry into clip or projection space.", "04"),
    ("Perspective divide", "Division by the homogeneous coordinate that creates perspective effects.", "04"),
    ("Clipping", "Cutting or removing primitive parts outside a clip region.", "05"),
    ("Culling", "Rejecting whole primitives or objects based on tests such as orientation.", "05"),
    ("Rasterization", "Conversion of primitives into fragments on a raster grid.", "06"),
    ("Barycentric coordinates", "Weights relative to triangle vertices used for interpolation.", "06"),
    ("Z-buffer", "Depth buffer method for hidden surface removal.", "07"),
    ("Back-face culling", "Rejecting surfaces facing away from the camera.", "07"),
    ("Ambient term", "Simple constant approximation of background light.", "08"),
    ("Diffuse term", "View-independent reflection based on normal and light direction.", "08"),
    ("Specular term", "View-dependent highlight component.", "08"),
    ("Texture", "Sampled data field used during rendering.", "09"),
    ("Texel", "A single sample in texture space.", "09"),
    ("Mipmapping", "Prefiltered texture levels used to reduce aliasing.", "09"),
    ("Shadow map", "Depth map rendered from the light source.", "10"),
    ("Shadow bias", "Offset used to reduce self-shadowing in shadow mapping.", "10"),
]


MC_QUESTIONS = [
    ("What is a fragment?", ["A final visible pixel", "A pixel candidate before final tests", "A vertex attribute", "A framebuffer attachment"], "B", "A fragment may be discarded by depth or other tests."),
    ("Why does transformation order matter?", ["Matrices are commutative", "Matrix multiplication is generally not commutative", "Only translations matter", "OpenGL ignores order"], "B", "Changing order changes the resulting transform."),
    ("What does clipping do?", ["Removes invisible light", "Cuts/removes geometry outside a clip region", "Computes shading", "Creates texture coordinates"], "B", "Clipping is a geometric visibility step before or around rasterization."),
    ("What does the z-buffer store?", ["Colors", "Normals", "Depth values", "Texture coordinates"], "C", "Depth values are compared for visibility."),
    ("What is a mipmap used for?", ["Perspective projection", "Reducing texture aliasing during minification", "Creating vertices", "Computing normals"], "B", "Mipmaps provide prefiltered lower-resolution texture levels."),
    ("What is shadow mapping based on?", ["Color comparison", "Visibility from the light source", "Only ambient light", "Back-face culling only"], "B", "A depth map from the light is compared during camera rendering."),
]


SEQUENCES = [
    ("Rendering pipeline order", ["Vertex input", "Vertex shader", "Primitive assembly", "Rasterization", "Fragment shader", "Depth/stencil/blending tests", "Framebuffer write"]),
    ("Shadow mapping high-level order", ["Render scene from light", "Store light-space depth map", "Render scene from camera", "Transform fragment into light space", "Compare fragment depth with shadow map", "Shade lit or shadowed result"]),
    ("Texture lookup order", ["Have/interpolate texture coordinates", "Select texture object/sampler", "Choose mip level/filter", "Sample texel values", "Use sampled value in shading"]),
    ("Projection path", ["Model coordinates", "World coordinates", "View/camera coordinates", "Clip coordinates", "Normalized device coordinates", "Viewport/screen coordinates"]),
]


MATH_DRILLS = [
    ("Matrix order", "Given a model point p, explain the difference between T*R*p and R*T*p. Describe the visual effect without calculating numbers."),
    ("Homogeneous point vs direction", "Write a short explanation for why a point can have w=1 and a direction can have w=0, and what translation does to each."),
    ("Perspective divide", "Explain what happens when clip coordinates (x, y, z, w) are divided by w. Why is this essential for perspective?"),
    ("Barycentric interpolation", "Given weights alpha, beta, gamma with alpha+beta+gamma=1, explain how to interpolate depth or color across a triangle."),
    ("Depth test", "Given old depth 0.4 and incoming depth 0.6 under a 'less' depth test, decide whether the fragment survives and explain why."),
    ("Diffuse lighting", "Explain qualitatively why max(0, dot(n, l)) appears in a diffuse lighting term."),
    ("Texture minification", "Explain why sampling a high-frequency texture far away can alias and how mipmapping helps."),
    ("Shadow comparison", "Explain the comparison between fragment light-space depth and the stored shadow-map depth."),
]


DIAGRAM_PROMPTS = [
    "Draw the rendering pipeline from vertices to framebuffer. Label programmable and fixed-function parts.",
    "Draw object, world, view, clip, NDC, and screen coordinate spaces as a chain.",
    "Draw orthographic versus perspective projection and explain the visual difference.",
    "Draw a triangle and mark barycentric weights, interpolated depth, and interpolated texture coordinates.",
    "Draw z-buffer visibility with two overlapping triangles at different depths.",
    "Draw ambient, diffuse, and specular components on a sphere.",
    "Draw texture mapping from a 2D image to a triangle or quad.",
    "Draw the two-pass shadow mapping algorithm with camera, light, shadow map, and depth comparison.",
]


OPENGL_DRILLS = [
    ("Shader role", "Explain what data should be computed in a vertex shader versus a fragment shader."),
    ("Buffer setup", "List the conceptual steps for sending vertex data to the GPU and drawing primitives."),
    ("Uniforms", "Explain what a uniform variable is and why transformation matrices are commonly uniforms."),
    ("Attributes", "Explain what vertex attributes are and name typical examples."),
    ("Depth test debugging", "Name symptoms when depth testing is disabled or configured incorrectly."),
    ("Texture debugging", "Name possible causes when a textured object renders black, white, or stretched."),
    ("Projection bug", "Describe what might be wrong if objects disappear when moving the camera."),
    ("Shadow bug", "Describe likely causes of shadow acne or detached shadows."),
]


def heading(title: str, level: int = 1) -> str:
    mark = "=" if level == 1 else "-" if level == 2 else "~"
    return f"{title}\n{mark * len(title)}"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")


def make_cloze_texts() -> str:
    lines = [heading("Cloze Source Texts")]
    lines.append("Copy one section into your cloze/Lueckentext generator. These texts are coherent and intentionally redundant enough for active recall.")
    for title, text in CLOZE_TEXTS:
        lines.append("")
        lines.append(heading(title, 2))
        lines.append(text)
    return "\n".join(lines)


def make_premade_cloze() -> str:
    lines = [heading("Premade Cloze Texts")]
    lines.append("Use these if your tool supports blanks directly. Answers are in parentheses after each paragraph.")
    for title, text in CLOZE_TEXTS:
        terms = [term for term in re.findall(r"\b[A-Za-z][A-Za-z-]{5,}\b", text)[:8]]
        cloze = text
        for index, term in enumerate(terms, start=1):
            cloze = re.sub(rf"\b{re.escape(term)}\b", f"____{index}____", cloze, count=1)
        lines.append("")
        lines.append(heading(title, 2))
        lines.append(cloze)
        lines.append("Answers: " + ", ".join(f"{i}={term}" for i, term in enumerate(terms, start=1)))
    return "\n".join(lines)


def make_matching_tsv() -> str:
    rows = ["term\tdefinition\tchapter"]
    rows.extend(f"{term}\t{definition}\t{chapter}" for term, definition, chapter in MATCHING_PAIRS)
    return "\n".join(rows)


def make_matching_tasks() -> str:
    lines = [heading("Matching Tasks")]
    lines.append("Use `matching_pairs.tsv` for generators. For manual practice: cover the right column and explain each term.")
    lines.append("")
    by_chapter: dict[str, list[tuple[str, str]]] = {}
    for term, definition, chapter in MATCHING_PAIRS:
        by_chapter.setdefault(chapter, []).append((term, definition))
    for chapter, items in sorted(by_chapter.items()):
        lines.append(heading(f"Chapter {chapter}", 2))
        lines.append("Terms:")
        for term, _ in items:
            lines.append(f"- {term}")
        lines.append("Definitions:")
        for _, definition in items:
            lines.append(f"- {definition}")
        lines.append("")
    return "\n".join(lines)


def make_multiple_choice() -> str:
    lines = [heading("Multiple Choice Practice")]
    for idx, (question, answers, correct, explanation) in enumerate(MC_QUESTIONS, start=1):
        lines.append("")
        lines.append(f"{idx}. {question}")
        for label, answer in zip(["A", "B", "C", "D"], answers):
            lines.append(f"   {label}. {answer}")
        lines.append(f"   Correct: {correct}")
        lines.append(f"   Explanation: {explanation}")
    return "\n".join(lines)


def make_sequences() -> str:
    lines = [heading("Sequencing Tasks")]
    lines.append("Shuffle the steps and restore the correct order.")
    for title, steps in SEQUENCES:
        lines.append("")
        lines.append(heading(title, 2))
        for idx, step in enumerate(steps, start=1):
            lines.append(f"{idx}. {step}")
    return "\n".join(lines)


def make_math_drills() -> str:
    lines = [heading("Math and Algorithm Drills")]
    lines.append("These are explanation-first drills. Add numeric examples after you can explain each concept verbally.")
    for idx, (title, prompt) in enumerate(MATH_DRILLS, start=1):
        lines.append("")
        lines.append(f"{idx}. {title}")
        lines.append(f"   Task: {prompt}")
        lines.append("   Check: answer should include variables, geometric meaning, and where it appears in the pipeline.")
    return "\n".join(lines)


def make_diagram_prompts() -> str:
    lines = [heading("Diagram and Graphics Prompts")]
    lines.append("Use these for drawing practice. After drawing, compare against the original lecture PDF pages listed in `study_pack/visual_review_guide.md`.")
    for idx, prompt in enumerate(DIAGRAM_PROMPTS, start=1):
        lines.append(f"{idx}. {prompt}")
    return "\n".join(lines)


def make_opengl_drills() -> str:
    lines = [heading("OpenGL and Software Drills")]
    lines.append("Answer these without code first, then inspect the OpenGL starter project.")
    for idx, (title, prompt) in enumerate(OPENGL_DRILLS, start=1):
        lines.append("")
        lines.append(f"{idx}. {title}")
        lines.append(f"   {prompt}")
    return "\n".join(lines)


def make_interactive_menu() -> str:
    return """Interactive Practice Menu
=========================

Use this as a rotation. Do not only read.

Daily 45-Minute Loop
--------------------
1. 10 minutes: cloze text from `cloze_source_texts.md`.
2. 10 minutes: matching from `matching_pairs.tsv`.
3. 10 minutes: one sequencing or diagram task.
4. 10 minutes: one math/OpenGL drill.
5. 5 minutes: write down what you could not answer.

Weekly Exam Simulation
----------------------
1. Pick two chapters randomly.
2. Do one cloze text, one matching round, one diagram, one math drill, and five oral questions.
3. Mark every weak answer and revisit the matching/flashcard material.

Copy-Paste Workflow
-------------------
For cloze generators: copy one section from `cloze_source_texts.md`.
For matching generators: import `matching_pairs.tsv`.
For MC or sequencing generators: copy from `multiple_choice.md` or `sequencing_tasks.md`.
For oral practice with AI: use `study_pack/ai_prompts.md` plus one chapter guide.
"""


def make_roadmap() -> str:
    return """Roadmap from 0 to 100 Percent
==============================

Phase 0 - Setup
---------------
Open `course_build_audit.json` and confirm the checks are true. Then start with `course_text_parts/00_START_HERE.txt`.

Phase 1 - Orientation
---------------------
Read `study_pack/README.md`, `study_pack/ai_prompts.md`, and `study_pack/study_plan.md`. Understand how the materials are organized.

Phase 2 - Core Understanding
----------------------------
Work through `study_pack/chapter_guides/` from chapter 01 to 10. For each chapter:
1. read the guide,
2. load the corresponding `course_text_parts/03_lectures/*.txt`,
3. answer the guide's Exam Drill,
4. add missed terms to flashcards.

Phase 3 - Active Recall
-----------------------
Use `practice_pack/cloze_source_texts.md`, `practice_pack/matching_pairs.tsv`, and `study_pack/flashcards_anki.tsv`. Your goal is fast recall of definitions, pipeline order, and conceptual distinctions.

Phase 4 - Repetition Variants
-----------------------------
Use `practice_pack/repetition_variants/round_01`, then `round_02`, then `round_03`. These rounds test the same concepts with different wording, so you do not only memorize one phrasing.

Phase 5 - Algorithms and Math
-----------------------------
Work through `study_pack/formulas_and_derivations.md` and `practice_pack/math_algorithm_drills.md`. For every formula or algorithm: explain variables, geometric meaning, and pipeline stage.

Phase 6 - Visual Understanding
------------------------------
Use `study_pack/visual_review_guide.md` and `practice_pack/diagram_graphics_prompts.md`. Draw each diagram yourself and explain it aloud.

Phase 7 - Software/OpenGL
-------------------------
Use `practice_pack/opengl_software_drills.md` and inspect the starter project in `course_text_parts/05_opengl_starter_project.txt`.

Phase 8 - Exam Simulation
-------------------------
Use `study_pack/exam_drill.md`, `practice_pack/multiple_choice.md`, and `practice_pack/sequencing_tasks.md`. Answer without notes first, then verify with chapter chunks.

Phase 9 - Final Pass
--------------------
Revisit only weak spots. If you cannot explain a topic with definition, diagram, algorithm, and typical pitfall, it is not finished.

End Condition
-------------
You are ready when you can:
- explain the full rendering pipeline without notes,
- derive or explain the main matrix/projection/rasterization/lighting ideas,
- answer matching and cloze tasks quickly,
- draw the key diagrams,
- debug conceptual OpenGL mistakes,
- and cite where in the course chunks the answer is supported.
"""


def make_readme() -> str:
    return """Practice Pack
=============

This folder is for active practice, not passive reading.

Files
-----
- `cloze_source_texts.md` - copy-paste texts for Lueckentext/cloze generators
- `premade_cloze_texts.md` - same topics with blanks already inserted
- `matching_pairs.tsv` - term/definition/chapter table for matching generators
- `matching_tasks.md` - manual matching grouped by chapter
- `multiple_choice.md` - MC questions with answers
- `sequencing_tasks.md` - order-the-steps tasks
- `math_algorithm_drills.md` - math and algorithm explanation drills
- `diagram_graphics_prompts.md` - drawing and visual explanation prompts
- `opengl_software_drills.md` - software/OpenGL checks
- `interactive_practice_menu.md` - daily practice rotation
- `roadmap_0_to_100.md` - complete suggested route through all materials
- `repetition_variants/` - repeated practice sets with the same concepts but different wording

Recommended start: `roadmap_0_to_100.md`.
"""


VARIANT_CLOZE_TEXTS = {
    "round_01": [
        ("Pipeline as a Factory", "Think of the rendering pipeline as a factory line. Vertex data enters first, shader stages transform and enrich it, primitives are formed, rasterization creates fragment candidates, tests decide which candidates survive, and the framebuffer stores the final output. The important distinction is that fragments are not automatically pixels."),
        ("Transform Chain", "A model normally starts in its own object coordinates. Transformations place it into the world, then into the camera view, then through projection into clip space. After the perspective divide and viewport mapping, the geometry can be related to screen positions. The order of these transformations changes the result."),
        ("Lighting Terms", "Local lighting is computed from direct interactions between light, material, normal, and view direction. Ambient light is a simple constant contribution, diffuse light depends on the normal-light angle, and specular light creates a view-dependent highlight."),
        ("Texture Sampling", "Texture mapping uses coordinates on a surface to sample a data field. The result may be a color or another value used by the shader. Filtering reconstructs values between texels, while mipmaps reduce aliasing when many texels project to a small screen area."),
        ("Shadow Map Idea", "Shadow mapping asks whether a camera fragment is visible from the light. A first pass stores light-space depths in a shadow map. A later pass transforms a fragment into light space and compares its depth with the stored depth."),
    ],
    "round_02": [
        ("Fragments and Tests", "Rasterization does not directly produce final image pixels. It produces fragments, which still have to pass tests such as depth and stencil operations. Only surviving fragments can update framebuffer attachments such as the color or depth buffer."),
        ("Projection Difference", "Orthographic projection keeps parallel lines parallel and does not shrink far objects. Perspective projection creates depth-dependent size changes and requires homogeneous coordinates. The perspective divide is the step that makes the projected coordinates usable for later viewport mapping."),
        ("Clipping vs Culling", "Clipping and culling both reduce later work, but they are not the same. Clipping cuts geometry against a boundary and can create new vertices. Culling rejects complete primitives or objects, for example because a face points away from the camera."),
        ("Visibility", "Visibility determination decides which surfaces are seen from a viewpoint. In z-buffering, each incoming fragment depth is compared to a stored depth value. The fragment survives only if it satisfies the selected depth comparison rule."),
        ("OpenGL Debugging", "A black or broken render can come from many pipeline stages. Common causes include missing uniforms, wrong shader outputs, disabled depth testing, bad texture coordinates, incorrect projection matrices, or normals in the wrong coordinate system."),
    ],
    "round_03": [
        ("Triangle Work", "A triangle becomes visible through several steps. Its vertices are transformed, the primitive is assembled and clipped if needed, rasterization finds covered sample positions, attributes are interpolated, and depth testing decides whether generated fragments remain visible."),
        ("Coordinate Spaces", "Object, world, view, clip, normalized device, and screen coordinates describe different stages of the same geometry. Confusing these spaces often leads to wrong matrices, disappearing objects, or lighting calculations in incompatible coordinate systems."),
        ("Illumination Pitfalls", "Lighting calculations depend on normalized vectors in a consistent coordinate system. The surface normal, light direction, view direction, and material parameters influence the final result. Diffuse and specular terms should not be treated as interchangeable."),
        ("Aliasing and Mipmaps", "Aliasing appears when high-frequency texture information is sampled too sparsely. Mipmaps store prefiltered texture levels, allowing the renderer to sample a level closer to the projected screen footprint."),
        ("Shadow Artifacts", "Shadow maps are practical but imperfect. Too little bias can cause self-shadowing artifacts, while too much bias can detach shadows from casters. Resolution and sampling also affect the final appearance."),
    ],
}


VARIANT_MATCHING = {
    "round_01": [
        ("Pixel candidate", "Fragment"),
        ("Stores final render buffers", "Framebuffer"),
        ("Cuts geometry at boundaries", "Clipping"),
        ("Rejects whole back-facing surfaces", "Back-face culling"),
        ("Sample in texture space", "Texel"),
        ("Light-space depth image", "Shadow map"),
        ("View-dependent highlight", "Specular term"),
        ("Prefiltered texture level", "Mipmap"),
    ],
    "round_02": [
        ("Local model coordinate system", "Object coordinates"),
        ("Camera-relative coordinate system", "View coordinates"),
        ("Division by homogeneous coordinate", "Perspective divide"),
        ("Weights over triangle vertices", "Barycentric coordinates"),
        ("Depth-based visibility buffer", "Z-buffer"),
        ("Constant background-light approximation", "Ambient term"),
        ("Matte normal-light reflection", "Diffuse term"),
        ("Sampled data field for shading", "Texture"),
    ],
    "round_03": [
        ("Programmable per-vertex stage", "Vertex shader"),
        ("Programmable per-fragment stage", "Fragment shader"),
        ("Geometry unit such as triangle", "Primitive"),
        ("Point plus attributes", "Vertex"),
        ("World-to-camera transform", "View transformation"),
        ("Maps toward clip space", "Projection matrix"),
        ("Offset against self-shadowing", "Shadow bias"),
        ("Conversion to fragments", "Rasterization"),
    ],
}


VARIANT_MC = {
    "round_01": [
        ("Which statement is true?", ["A fragment is guaranteed visible", "A fragment may still be discarded", "A texel is a vertex", "A framebuffer is a shader"], "B"),
        ("Which pair is easiest to confuse but different?", ["Clipping and culling", "CPU and keyboard", "PDF and shader", "Git and texture"], "A"),
        ("What does a projection matrix help produce?", ["Clip/projected coordinates", "Texture filenames", "CMake cache only", "Forum posts"], "A"),
        ("What does mipmapping address?", ["Texture sampling quality", "Git history", "Lecture dates", "Back-face orientation only"], "A"),
    ],
    "round_02": [
        ("Which data is commonly interpolated during rasterization?", ["Depth or texture coordinates", "Repository URL", "Exam room", "Compiler license"], "A"),
        ("What is the role of the normal in lighting?", ["Surface orientation for lighting", "Zip compression", "Branch naming", "Framebuffer size only"], "A"),
        ("What is shadow acne?", ["Self-shadowing artifact", "Texture coordinate system", "Vertex format", "Projection type"], "A"),
        ("What is a texel?", ["Texture sample", "Triangle edge", "Depth test", "Camera matrix"], "A"),
    ],
    "round_03": [
        ("What should be checked if depth ordering looks wrong?", ["Depth test/buffer", "Only texture wrap mode", "Only README title", "Only fragment color"], "A"),
        ("What does homogeneous w enable?", ["Translation/projection behavior", "Only file compression", "Only ambient light", "Only shader comments"], "A"),
        ("Which is view-dependent?", ["Specular highlight", "Diffuse Lambert term only", "Object filename", "CMake version"], "A"),
        ("Which pass creates the shadow map?", ["Light-view render pass", "Final color-only pass", "Git push", "HTML export"], "A"),
    ],
}


VARIANT_SEQUENCES = {
    "round_01": ("Fragment visibility path", ["Rasterization creates fragment", "Fragment shader computes output", "Depth test compares depth", "Surviving fragment updates framebuffer"]),
    "round_02": ("Coordinate space path", ["Object space", "World space", "View space", "Clip space", "NDC", "Viewport/screen"]),
    "round_03": ("Lighting calculation ingredients", ["Surface point", "Normal vector", "Light direction", "View direction", "Material parameters", "Ambient/diffuse/specular combination"]),
}


def make_variant_readme() -> str:
    return """Repetition Variants
===================

These files repeat the same core concepts with different wording and task layouts. Use them after the base practice files so you train recognition without memorizing only one phrasing.

Suggested use:
1. Round 01 after first chapter pass.
2. Round 02 after weak-spot review.
3. Round 03 before mock exams.

Each round includes cloze-ready texts, matching pairs, MC questions, and sequencing tasks.
"""


def make_variant_cloze(round_id: str) -> str:
    lines = [heading(f"Cloze Variants {round_id}")]
    lines.append("Copy sections into a cloze generator. Same concepts, different wording.")
    for title, text in VARIANT_CLOZE_TEXTS[round_id]:
        lines.append("")
        lines.append(heading(title, 2))
        lines.append(text)
    return "\n".join(lines)


def make_variant_matching(round_id: str) -> str:
    rows = ["prompt\tanswer"]
    rows.extend(f"{prompt}\t{answer}" for prompt, answer in VARIANT_MATCHING[round_id])
    return "\n".join(rows)


def make_variant_mc(round_id: str) -> str:
    lines = [heading(f"Multiple Choice Variants {round_id}")]
    for idx, (question, answers, correct) in enumerate(VARIANT_MC[round_id], start=1):
        lines.append("")
        lines.append(f"{idx}. {question}")
        for label, answer in zip(["A", "B", "C", "D"], answers):
            lines.append(f"   {label}. {answer}")
        lines.append(f"   Answer: {correct}")
    return "\n".join(lines)


def make_variant_sequence(round_id: str) -> str:
    title, steps = VARIANT_SEQUENCES[round_id]
    lines = [heading(f"Sequencing Variant {round_id}")]
    lines.append(f"Task: Restore the correct order for {title}.")
    lines.append("")
    for step in reversed(steps):
        lines.append(f"- {step}")
    lines.append("")
    lines.append("Answer: " + " -> ".join(steps))
    return "\n".join(lines)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)
    files = {
        "README.md": make_readme(),
        "cloze_source_texts.md": make_cloze_texts(),
        "premade_cloze_texts.md": make_premade_cloze(),
        "matching_pairs.tsv": make_matching_tsv(),
        "matching_tasks.md": make_matching_tasks(),
        "multiple_choice.md": make_multiple_choice(),
        "sequencing_tasks.md": make_sequences(),
        "math_algorithm_drills.md": make_math_drills(),
        "diagram_graphics_prompts.md": make_diagram_prompts(),
        "opengl_software_drills.md": make_opengl_drills(),
        "interactive_practice_menu.md": make_interactive_menu(),
        "roadmap_0_to_100.md": make_roadmap(),
        "repetition_variants/README.md": make_variant_readme(),
    }
    for round_id in ["round_01", "round_02", "round_03"]:
        files[f"repetition_variants/{round_id}/cloze_texts.md"] = make_variant_cloze(round_id)
        files[f"repetition_variants/{round_id}/matching_pairs.tsv"] = make_variant_matching(round_id)
        files[f"repetition_variants/{round_id}/multiple_choice.md"] = make_variant_mc(round_id)
        files[f"repetition_variants/{round_id}/sequencing.md"] = make_variant_sequence(round_id)
    for name, text in files.items():
        write(OUT / name, text)
    print(f"Wrote {OUT.relative_to(ROOT).as_posix()}")
    print(f"Files: {len(files)}")
    print(f"Matching pairs: {len(MATCHING_PAIRS)}")
    print(f"Cloze texts: {len(CLOZE_TEXTS)}")
    print("Repetition variant rounds: 3")


if __name__ == "__main__":
    main()
