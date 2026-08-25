from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "overprep_pack"


CONFUSION_PAIRS = [
    ("Fragment", "Pixel", "A fragment is a candidate produced before final tests; a pixel is final image storage/output."),
    ("Clipping", "Culling", "Clipping cuts primitives against a region; culling rejects whole primitives/objects based on tests."),
    ("View transform", "Projection transform", "View transform moves world into camera space; projection maps camera space into clip/projected space."),
    ("Texture", "Texel", "A texture is the sampled data field; a texel is one sample in that field."),
    ("Diffuse", "Specular", "Diffuse is broad view-independent reflection; specular is view-dependent highlight."),
    ("Z-buffer", "Shadow map", "Z-buffer stores camera-view depth; shadow map stores light-view depth."),
    ("Shadow acne", "Peter panning", "Acne is self-shadowing artifacts; peter panning is detached shadows from too much bias."),
    ("Rasterization", "Fragment shading", "Rasterization creates fragments; fragment shading computes fragment outputs."),
    ("Orthographic projection", "Perspective projection", "Orthographic lacks perspective shortening; perspective uses homogeneous divide."),
    ("Object coordinates", "World coordinates", "Object coordinates are local model coordinates; world coordinates place objects in the scene."),
]


MATCHING_PAIRS = [
    ("Vertex", "Point with attributes such as position or normal.", "02"),
    ("Primitive", "Geometric unit assembled from vertices.", "02"),
    ("Fragment", "Pixel candidate before final tests.", "02"),
    ("Framebuffer", "Storage for final render buffers.", "02"),
    ("Homogeneous coordinates", "Coordinate representation with w component.", "03"),
    ("Affine transformation", "Line-preserving transform such as translation or rotation.", "03"),
    ("Projection matrix", "Matrix mapping view space toward clip/projection space.", "04"),
    ("Perspective divide", "Division by w after projection.", "04"),
    ("Clipping", "Cutting/removing geometry outside a region.", "05"),
    ("Culling", "Rejecting whole objects or primitives based on a test.", "05"),
    ("Rasterization", "Converting primitives into fragments.", "06"),
    ("Barycentric coordinates", "Triangle-relative weights for interpolation.", "06"),
    ("Z-buffer", "Depth-based hidden surface removal buffer.", "07"),
    ("Back-face culling", "Rejecting surfaces facing away from camera.", "07"),
    ("Ambient term", "Constant approximation of indirect/background light.", "08"),
    ("Diffuse term", "Normal-light dependent matte reflection.", "08"),
    ("Specular term", "View-dependent highlight.", "08"),
    ("Texture", "Sampled data field used during rendering.", "09"),
    ("Texel", "Single texture sample.", "09"),
    ("Mipmap", "Prefiltered texture level.", "09"),
    ("Shadow map", "Light-space depth map.", "10"),
    ("Shadow bias", "Depth offset to reduce self-shadowing.", "10"),
]


MC_BANK = [
    ("A fragment is best described as:", ["A final visible pixel", "A pixel candidate before final tests", "A triangle vertex", "A texture sample"], "B"),
    ("The z-buffer primarily stores:", ["Color", "Depth", "Normals", "Texture coordinates"], "B"),
    ("Which operation can create new vertices?", ["Analytical clipping", "Back-face culling", "Depth testing", "Framebuffer clearing"], "A"),
    ("The perspective divide divides by:", ["x", "y", "z", "w"], "D"),
    ("Mipmaps mainly reduce:", ["Geometry count", "Texture aliasing", "Specular highlights", "Camera movement"], "B"),
    ("A shadow map stores:", ["Light-space depth", "Final colors", "Normals", "Texture coordinates"], "A"),
    ("Matrix multiplication order matters because:", ["Matrices are always diagonal", "It is generally not commutative", "Vectors have no direction", "OpenGL disables order"], "B"),
    ("A vertex shader usually processes:", ["Per-vertex data", "Final framebuffer pixels", "Only texture files", "Only UI events"], "A"),
    ("A fragment shader usually computes:", ["Per-fragment outputs", "CPU memory layout", "CMake settings", "Mesh topology only"], "A"),
    ("Back-face culling is usually valid for:", ["Closed opaque objects", "Transparent all-sided surfaces", "Audio buffers", "Texture files only"], "A"),
    ("Diffuse lighting depends most directly on:", ["Normal and light direction", "Framebuffer size only", "Filename extension", "Mouse input"], "A"),
    ("Specular lighting is:", ["View-dependent", "Always constant", "Only a clipping operation", "The same as ambient"], "A"),
    ("Texture coordinates are used to:", ["Index/sample texture data", "Choose the CPU compiler", "Replace the depth buffer", "Disable projection"], "A"),
    ("Clipping happens to:", ["Geometry or fragments outside a region", "Only shader source comments", "Only Git files", "Only final exam answers"], "A"),
    ("Rasterization converts:", ["Primitives to fragments", "Textures to compilers", "Pixels to vertices", "Light to camera"], "A"),
]


FILL_INS = [
    ("The pipeline transforms vertices, assembles primitives, rasterizes them into ____ and writes surviving results to the ____.", ["fragments", "framebuffer"]),
    ("In homogeneous coordinates, translation and projection can be represented using ____ multiplication.", ["matrix"]),
    ("Perspective projection relies on dividing by the homogeneous coordinate ____.", ["w"]),
    ("____ clipping may cut primitives and create new vertices at boundaries.", ["Analytical"]),
    ("The ____ buffer stores depth values for hidden surface removal.", ["z"]),
    ("A texture sample is called a ____.", ["texel"]),
    ("____ mapping renders depth from the light source first.", ["Shadow"]),
    ("The diffuse term often uses max(0, dot(n, l)) where n is the surface ____.", ["normal"]),
    ("Mipmapping helps reduce texture ____ during minification.", ["aliasing"]),
    ("Back-face ____ rejects surfaces pointing away from the camera.", ["culling"]),
]


SEQUENCE_TASKS = [
    ("Pipeline", ["Vertex input", "Vertex shader", "Primitive assembly", "Rasterization", "Fragment shader", "Depth/blend tests", "Framebuffer write"]),
    ("Coordinate path", ["Object coordinates", "World coordinates", "View coordinates", "Clip coordinates", "NDC", "Viewport coordinates"]),
    ("Shadow mapping", ["Render from light", "Store depth map", "Render from camera", "Transform fragment to light space", "Compare depth", "Apply lit/shadowed shading"]),
    ("Texture sampling", ["Interpolate texture coordinates", "Select texture/sampler", "Choose filter/mipmap", "Sample texels", "Use value in shading"]),
]


CODE_MC = [
    (
        "A model renders but nearer triangles do not hide farther triangles. What is most likely missing?",
        ["Depth testing or depth buffer setup", "Only mipmaps", "Only ambient lighting", "Only CMake comments"],
        "A",
    ),
    (
        "A shader expects a matrix uniform but objects ignore camera movement. What should you inspect?",
        ["Whether the view/projection uniform is updated and used", "Whether README exists", "Only texture file size", "Only back-face color"],
        "A",
    ),
    (
        "A textured object appears stretched. What is a likely issue?",
        ["Wrong or missing texture coordinates", "Too many Git commits", "Ambient term too high only", "No shadow bias only"],
        "A",
    ),
    (
        "Everything renders black after adding lighting. What should be checked first?",
        ["Normals, light direction, material values, shader outputs", "Only branch name", "Only PDF page count", "Only zip filename"],
        "A",
    ),
    (
        "Shadow acne appears. Which parameter is commonly adjusted?",
        ["Shadow bias", "Git remote", "Course title", "HTML viewport"],
        "A",
    ),
]


DIAGRAM_LABELS = [
    ("Rendering pipeline", ["Vertex input", "Vertex shader", "Primitive assembly", "Rasterization", "Fragment shader", "Tests/operations", "Framebuffer"]),
    ("Projection pipeline", ["Object", "World", "View", "Clip", "NDC", "Viewport/screen"]),
    ("Triangle rasterization", ["Vertices", "Edges", "Sample points", "Covered fragments", "Interpolated attributes", "Depth values"]),
    ("Local illumination", ["Surface normal", "Light direction", "View direction", "Diffuse component", "Specular component", "Material coefficient"]),
    ("Shadow mapping", ["Light", "Camera", "Depth map", "Light-space transform", "Depth comparison", "Shadowed fragment"]),
]


ONE_PAGERS = [
    ("01_introduction", "Know course purpose, real-time rendering motivation, OpenGL/GPU role, and how later chapters connect."),
    ("02_rendering_pipeline", "Know vertices -> primitives -> fragments -> pixels, shader roles, tests, framebuffer."),
    ("03_transformations", "Know homogeneous coordinates, matrix order, affine transforms, coordinate-system changes."),
    ("04_projection", "Know orthographic vs perspective, camera model, projection matrix, perspective divide."),
    ("05_clipping", "Know analytical vs pixel clipping, view volume, new vertices, difference from culling."),
    ("06_rasterization", "Know triangle coverage, samples, interpolation, barycentric coordinates, fragments."),
    ("07_visibility", "Know VSD/HSR, z-buffer, depth precision, culling, occlusion."),
    ("08_illumination", "Know ambient/diffuse/specular, normals, Phong/Blinn-Phong, local vs global."),
    ("09_texturing", "Know texture coordinates, texels, sampling, filtering, mipmaps, aliasing."),
    ("10_shadows", "Know light-space visibility, shadow map, depth compare, bias artifacts."),
]


def heading(title: str, level: int = 1) -> str:
    mark = "=" if level == 1 else "-" if level == 2 else "~"
    return f"{title}\n{mark * len(title)}"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")


def mock_exam(index: int) -> str:
    start = (index - 1) * 5
    mc = MC_BANK[start:start + 10] if index == 1 else MC_BANK[max(0, start - 2):max(0, start - 2) + 10]
    lines = [heading(f"Closed-Format Mock Exam {index}")]
    lines.append("No vague open answers. Use only selecting, matching, ordering, filling blanks, and labeling checklists.")
    lines.append("")
    lines.append(heading("Section A - Multiple Choice", 2))
    for qno, (question, answers, correct) in enumerate(mc, start=1):
        lines.append(f"{qno}. {question}")
        for label, answer in zip(["A", "B", "C", "D"], answers):
            lines.append(f"   {label}. {answer}")
        lines.append(f"   Answer: {correct}")
    lines.append("")
    lines.append(heading("Section B - Fill In", 2))
    for qno, (prompt, answers) in enumerate(FILL_INS[(index - 1): (index - 1) + 6], start=1):
        lines.append(f"{qno}. {prompt}")
        lines.append(f"   Answers: {', '.join(answers)}")
    lines.append("")
    lines.append(heading("Section C - Matching", 2))
    pairs = MATCHING_PAIRS[(index - 1) * 5: (index - 1) * 5 + 8]
    for number, (term, _, _) in enumerate(pairs, start=1):
        lines.append(f"{number}. {term}")
    for letter, (_, definition, _) in zip("ABCDEFGH", pairs):
        lines.append(f"{letter}. {definition}")
    lines.append("Answer key: " + ", ".join(f"{i + 1}-{chr(65 + i)}" for i in range(len(pairs))))
    lines.append("")
    lines.append(heading("Section D - Sequencing", 2))
    title, steps = SEQUENCE_TASKS[(index - 1) % len(SEQUENCE_TASKS)]
    lines.append(f"Task: Put these steps in order: {title}")
    for step in reversed(steps):
        lines.append(f"- {step}")
    lines.append("Answer: " + " -> ".join(steps))
    lines.append("")
    lines.append(heading("Section E - Diagram Label Checklist", 2))
    diagram, labels = DIAGRAM_LABELS[(index - 1) % len(DIAGRAM_LABELS)]
    lines.append(f"Diagram: {diagram}")
    lines.append("Your drawing is complete only if it includes:")
    for label in labels:
        lines.append(f"- [ ] {label}")
    return "\n".join(lines)


def mistake_log() -> str:
    return """Mistake Log
===========

Use this after every practice session. Keep entries short and concrete.

Template
--------
Date:
Source file:
Task type: MC / Matching / Cloze / Sequence / Diagram / Math / OpenGL
Topic:
Wrong answer:
Correct answer:
Why I missed it:
Fix rule:
Review date 1:
Review date 2:
Review date 3:

Example
-------
Date: 2026-08-25
Source file: overprep_pack/mock_exams/mock_exam_01_closed_format.md
Task type: MC
Topic: Fragment vs pixel
Wrong answer: final visible pixel
Correct answer: pixel candidate before final tests
Why I missed it: confused rasterization output with framebuffer output
Fix rule: fragment survives tests before becoming final pixel output
Review date 1:
Review date 2:
Review date 3:
"""


def oral_mode() -> str:
    return """Oral Exam Mode Without Open Essays
=================================

Use this with an AI examiner.

Prompt
------
Ask me one closed-format question at a time from CS8165. Use only:
- multiple choice,
- matching,
- fill-in-the-blank,
- ordering/sequencing,
- diagram labeling checklist,
- true/false with correction.

Do not ask broad essay questions. After I answer, grade strictly:
1. correct / partially correct / wrong,
2. one-sentence explanation,
3. the exact fact I must memorize,
4. next closed-format question.

Escalation
----------
If I answer three in a row correctly, make the next question a confusion pair or mixed-topic question.
If I answer wrong, ask a simpler fill-in or matching question on the same concept.
"""


def confusion_pairs() -> str:
    lines = [heading("Concept Confusion Pairs")]
    lines.append("For each row: choose left/right/both/neither, then explain with one sentence.")
    lines.append("")
    lines.append("Pair\tDecision Rule")
    for left, right, rule in CONFUSION_PAIRS:
        lines.append(f"{left} vs {right}\t{rule}")
    return "\n".join(lines)


def diagram_workbook() -> str:
    lines = [heading("Diagram Label Workbook")]
    lines.append("No artistic drawing required. You pass if all checklist labels are present and correctly connected.")
    for title, labels in DIAGRAM_LABELS:
        lines.append("")
        lines.append(heading(title, 2))
        lines.append("Required labels:")
        for label in labels:
            lines.append(f"- [ ] {label}")
        lines.append("Closed check: every label must be placed and connected with arrows where the process has direction.")
    return "\n".join(lines)


def code_drills() -> str:
    lines = [heading("Code Reading and Debugging Drills")]
    lines.append("These are closed-format OpenGL/software questions.")
    for qno, (question, answers, correct) in enumerate(CODE_MC, start=1):
        lines.append("")
        lines.append(f"{qno}. {question}")
        for label, answer in zip(["A", "B", "C", "D"], answers):
            lines.append(f"   {label}. {answer}")
        lines.append(f"   Answer: {correct}")
    return "\n".join(lines)


def one_pagers() -> str:
    lines = [heading("One-Pager Cheat Sheets")]
    for name, summary in ONE_PAGERS:
        lines.append("")
        lines.append(heading(name, 2))
        lines.append(summary)
        lines.append("Must be able to: define, place in pipeline, draw, name formula/algorithm, name pitfall.")
    return "\n".join(lines)


def spaced_repetition() -> str:
    return """Spaced Repetition Schedule
==========================

Use this with flashcards, matching, and cloze.

Cycle
-----
Day 0: Learn chapter.
Day 1: 10-minute recall.
Day 2: Matching + cloze.
Day 4: MC + sequencing.
Day 7: Diagram + math drill.
Day 14: Closed-format mock exam section.
Day 21: Final mixed review.

Rule
----
If you miss a concept, reset it to Day 0 in `mistake_log.md`.
"""


def readiness_checklist() -> str:
    lines = [heading("Final Readiness Checklist")]
    checks = [
        "I can order the full rendering pipeline.",
        "I can match every core term to its definition.",
        "I can fill cloze blanks for every chapter summary.",
        "I can distinguish every confusion pair.",
        "I can label the required diagrams.",
        "I can answer math/algorithm drills without notes.",
        "I can diagnose common OpenGL rendering failures.",
        "I can complete a closed-format mock exam under time pressure.",
        "I can cite which course chunk supports an answer.",
        "My mistake log has no repeated unfixed error.",
    ]
    for item in checks:
        lines.append(f"- [ ] {item}")
    return "\n".join(lines)


def readme() -> str:
    return """Overprep Pack
=============

This pack is for overpreparation using closed formats only. It avoids vague open-answer mock exams.

Use Order
---------
1. `one_pager_cheat_sheets.md`
2. `concept_confusion_pairs.md`
3. `closed_format_oral_exam_mode.md`
4. `mock_exams/`
5. `diagram_label_workbook.md`
6. `code_reading_debugging_drills.md`
7. `mistake_log.md`
8. `spaced_repetition_schedule.md`
9. `final_readiness_checklist.md`

Exam Style
----------
Use selecting, matching, filling blanks, ordering, labeling, and short correction. Avoid broad essay answers.
"""


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT / "README.md", readme())
    write(OUT / "mistake_log.md", mistake_log())
    write(OUT / "closed_format_oral_exam_mode.md", oral_mode())
    write(OUT / "concept_confusion_pairs.md", confusion_pairs())
    write(OUT / "diagram_label_workbook.md", diagram_workbook())
    write(OUT / "code_reading_debugging_drills.md", code_drills())
    write(OUT / "one_pager_cheat_sheets.md", one_pagers())
    write(OUT / "spaced_repetition_schedule.md", spaced_repetition())
    write(OUT / "final_readiness_checklist.md", readiness_checklist())
    for index in range(1, 4):
        write(OUT / "mock_exams" / f"mock_exam_{index:02d}_closed_format.md", mock_exam(index))
    print(f"Wrote {OUT.relative_to(ROOT).as_posix()}")
    print("Mock exams: 3")
    print(f"Confusion pairs: {len(CONFUSION_PAIRS)}")


if __name__ == "__main__":
    main()
