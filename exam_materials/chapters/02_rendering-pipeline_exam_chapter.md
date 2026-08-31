# Lecture 02 - Rendering Pipeline Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/02_rendering-pipeline.txt`
Extracted source pages: 94
Primary assignment connection: 01 Rendering Pipeline

This is the chapter itself: a readable explanation for studying before you drill the material. Read it before using cloze, matching, MC, sequencing, or assignment practice.

## 1. What Problem This Chapter Solves

Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `application stage`: CPU-side preparation of models, scene data, interaction, animation, and rendering state. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 02.1 Rendering Process

Source location: Section 2.1

Object-based rendering starts with scene objects represented as primitives. The pipeline transforms vertices, assembles primitives, rasterizes them into fragments, and lets only some fragments become pixels. The important detail is that the representation changes at every stage.

The application stage prepares data and state. The geometry stage handles positions and primitives. The rasterization stage creates fragments and applies fragment operations. This separation helps you explain both theory questions and black-screen OpenGL bugs.

Study meaning: Vertices become primitives, primitives become fragments, and fragments compete to become pixel updates.

Closed check: What is the difference between a fragment and a final pixel?

### 02.2 OpenGL Overview

Source location: Section 2.2

OpenGL is an API for controlling a graphics pipeline. It is not a renderer by itself in the sense of a single command that understands your scene. You create a context, provide buffers, set state, compile shaders, bind objects, and issue draw calls.

Modern OpenGL is stateful and shader-based. Many errors happen because the programmer assumes that a later call carries more information than it really does. The GPU uses the currently bound objects and current state at draw time.

Study meaning: OpenGL draw calls consume the state machine as it exists right now.

Closed check: Why can binding the wrong vertex array or shader program produce a valid draw call with wrong output?

### 02.3 OpenGL Rendering

Source location: Section 2.3

Older OpenGL exposed a fixed-function style where many transformations and lighting choices were configured through predefined calls. Modern OpenGL expects you to write shader programs and explicitly manage data flow.

This is not just historical trivia. It explains why shader code, vertex attributes, uniforms, and buffer objects are central in the exercises. If the shader expects an attribute and the vertex layout does not provide it, the pipeline has no magic fallback.

Study meaning: Modern OpenGL makes the data path explicit; that gives control but also creates responsibility.

Closed check: Which data usually goes into vertex attributes, and which data usually goes into uniforms?

### 02.4 OpenGL Rendering Pipeline

Source location: Section 2.4

The vertex shader runs per vertex and usually outputs clip-space position plus attributes for later interpolation. Primitive assembly groups vertices into points, lines, or triangles. Clipping handles geometry outside the view volume. Rasterization creates fragments.

The fragment shader computes candidate fragment output, often using interpolated attributes, uniforms, and textures. After that, tests and operations such as depth testing, stencil testing, blending, and masking decide what reaches the framebuffer.

Study meaning: Programmable shaders compute values; fixed pipeline stages decide coverage, interpolation, tests, and output rules.

Closed check: If your geometry appears in wireframe but colors are wrong, which stages become suspicious?

### 02.5 Fragment Tests, Framebuffer, and Pixel-Based Rendering

Source location: Sections 2.5-2.7

Fragment tests are the gatekeepers after shading. A fragment can have a perfectly valid color and still fail because depth, stencil, scissor, masking, or blending state prevents a visible update. This is why final pixels are a subset of generated fragments.

The framebuffer stores the final render targets: color buffers, depth buffers, stencil buffers, or custom attachments. Pixel-based rendering starts from image data instead of geometric primitives, which is useful for image processing but conceptually different from the object-to-pixel pipeline.

Study meaning: The framebuffer is the destination; fragment operations are the rules for writing into it.

Closed check: Why can two fragments with different colors produce only one visible pixel color?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### application stage

CPU-side preparation of models, scene data, interaction, animation, and rendering state. In an exam answer, connect `application stage` to the chapter chain: `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`. Say where it appears, what it affects, and what would break if you misunderstood it.

### geometry stage

Pipeline stage that transforms vertices and prepares primitives. In an exam answer, connect `geometry stage` to the chapter chain: `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`. Say where it appears, what it affects, and what would break if you misunderstood it.

### rasterization

Conversion of projected primitives into fragment candidates on a sample grid. In an exam answer, connect `rasterization` to the chapter chain: `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`. Say where it appears, what it affects, and what would break if you misunderstood it.

### fragment

A candidate pixel contribution produced by rasterization before final tests and blending. In an exam answer, connect `fragment` to the chapter chain: `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`. Say where it appears, what it affects, and what would break if you misunderstood it.

### framebuffer

Memory target that stores color, depth, stencil, or related per-pixel results. In an exam answer, connect `framebuffer` to the chapter chain: `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`. Say where it appears, what it affects, and what would break if you misunderstood it.

### double buffering

Using front and back buffers so drawing can happen off-screen before display swap. In an exam answer, connect `double buffering` to the chapter chain: `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`vertices -> primitives -> fragments -> tests -> pixels`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `01 Rendering Pipeline`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.

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

1. Complete the chain: `application data -> geometry stage -> primitive assembly -> ____ -> fragment operations -> framebuffer`
2. Match `geometry stage` to its role: Pipeline stage that transforms vertices and prepares primitives.
3. Select the dangerous misconception: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
4. Explain in one sentence why `rasterization` belongs in this chapter.

## 10. End Condition

You are done with Lecture 02 only when you can read a new question, recognize that it belongs to `Rendering Pipeline`, and reconstruct the relevant part of `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.
