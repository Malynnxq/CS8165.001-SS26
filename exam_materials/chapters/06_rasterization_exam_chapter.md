# Lecture 06 - Rasterization Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/06_rasterization.txt`
Extracted source pages: 61
Primary assignment connection: 05 Rasterization

## 1. What Problem This Chapter Solves

Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `scan conversion`: Determining which discrete samples are covered by an ideal geometric primitive. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 06.1 Line Rasterization

Source location: Section 6.1

A mathematical line has infinitely many points, but a raster display has a finite grid. Line rasterization decides which grid cells or samples best approximate the ideal line. The algorithm must balance accuracy, speed, and consistency.

Incremental algorithms avoid recomputing expensive formulas for every pixel. The important idea is to step along one axis and update an error term that decides when to step along the other axis.

Study meaning: Rasterizing a line means approximating a continuous path by grid decisions.

Closed check: Why are incremental error updates useful in line rasterization?

### 06.2 Triangle Edge Rasterization

Source location: Section 6.2

Triangles are the core primitive in real-time rendering. Edge functions or half-space tests decide whether a sample lies inside the triangle. This allows the rasterizer to test coverage systematically.

Coverage is not final visibility. A covered sample becomes a fragment candidate. Depth testing, stencil testing, blending, and other operations still decide whether the framebuffer changes.

Study meaning: Triangle rasterization answers the question: which samples are inside this projected triangle?

Closed check: What later stage can reject a fragment after triangle coverage succeeds?

### 06.3 Region Filling

Source location: Section 6.3

Region filling generalizes the idea of determining interior samples. The algorithm must identify connected areas or spans that should receive color. This connects rasterization to scan conversion and image-space reasoning.

The practical issue is avoiding gaps, double fills, or inconsistent boundary handling. Small choices at edges can become visible artifacts when many primitives meet.

Study meaning: Filling is about turning boundary descriptions into consistent interior samples.

Closed check: Why can inconsistent edge rules create cracks between adjacent primitives?

### 06.4 Scanline-Based Triangle Rasterization

Source location: Section 6.4

Scanline rasterization processes horizontal rows of the image. For each row that crosses a triangle, the algorithm finds the covered interval and fills the span. Attribute interpolation can be updated along edges and across each span.

The method is intuitive because it follows the memory layout of many images. It also demonstrates why interpolation is tied to rasterization: once you know a sample location inside the primitive, you can interpolate depth, color, normals, or texture coordinates.

Study meaning: Each scanline asks: where does this triangle enter and leave this row?

Closed check: Which attributes might be interpolated while filling triangle spans?

### 06.5 Tile-Based Triangle Rasterization

Source location: Section 6.5

Tile- or block-based approaches group pixels into small regions. This can improve locality and parallel work distribution. Modern GPUs often reason in blocks or tiles internally because rendering is massively parallel.

For the exam, connect this to efficiency. The mathematical goal is still coverage, but the implementation is organized to use hardware resources well.

Study meaning: Block-based rasterization keeps the same coverage problem but changes the work organization.

Closed check: Why is block organization attractive for parallel graphics hardware?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### scan conversion

Determining which discrete samples are covered by an ideal geometric primitive. In an exam answer, connect `scan conversion` to the chapter chain: `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`. Say where it appears, what it affects, and what would break if you misunderstood it.

### triangle coverage

Testing which pixel/sample positions lie inside a triangle. In an exam answer, connect `triangle coverage` to the chapter chain: `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`. Say where it appears, what it affects, and what would break if you misunderstood it.

### barycentric coordinates

Weights relative to triangle vertices used for inside tests and interpolation. In an exam answer, connect `barycentric coordinates` to the chapter chain: `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`. Say where it appears, what it affects, and what would break if you misunderstood it.

### interpolation

Computing per-fragment values from vertex attributes. In an exam answer, connect `interpolation` to the chapter chain: `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`. Say where it appears, what it affects, and what would break if you misunderstood it.

### aliasing

Artifacts caused when continuous signals are sampled too coarsely. In an exam answer, connect `aliasing` to the chapter chain: `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`. Say where it appears, what it affects, and what would break if you misunderstood it.

### fragment candidate

A potential contribution to the framebuffer, not yet a guaranteed visible pixel. In an exam answer, connect `fragment candidate` to the chapter chain: `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `05 Rasterization`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not call every generated fragment a final pixel.

The trap is dangerous because it usually sounds close to the truth. High exam performance depends on catching these near-misses quickly. When a multiple-choice option looks plausible, test it against the full chain: input, operation, output, next use. If one of those links is missing or wrong, the option is probably a distractor.

## 8. What A Strong Answer Must Contain

- The problem this chapter solves.
- The important data or object representation.
- The operation, algorithm, formula, or API mechanism.
- The output representation.
- The next pipeline stage or later use.
- One assignment or OpenGL/software connection.
- One typical mistake and the corrected distinction.

## 9. Closed-Format Self-Test

1. Complete the chain: `projected primitive -> ____ -> fragment generation -> attribute interpolation -> fragment tests`
2. Match `triangle coverage` to its role: Testing which pixel/sample positions lie inside a triangle.
3. Select the dangerous misconception: Do not call every generated fragment a final pixel.
4. Explain in one sentence why `barycentric coordinates` belongs in this chapter.

## 10. End Condition

You are done with Lecture 06 only when you can read a new question, recognize that it belongs to `Rasterization`, and reconstruct the relevant part of `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.
