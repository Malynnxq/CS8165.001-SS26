# Lecture 01 - Introduction Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/01_introduction.txt`
Extracted source pages: 51
Primary assignment connection: 00 Introduction to C++

## 1. What Problem This Chapter Solves

Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `raster image`: A grid of stored pixel samples; it is already an image, not a 3D scene. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 01.1 Course Organization

Source location: Slides around 6-15

The organizational slides matter because they explain how the theory and programming parts fit together. The exercises are not separate from the lecture; they are the practical version of the same pipeline ideas. When the course says that slides are generally not self-explanatory, that is a warning: the bullet points are anchors, not a textbook.

Treat every exercise sheet as an applied checkpoint. Rendering pipeline, primitive types, shaders, transformations, projection, clipping, and rasterization are introduced in the lectures and then turned into OpenGL tasks. If a topic appears both in a lecture and an exercise, it is more likely to be exam relevant.

Study meaning: Lecture slides give the vocabulary; exercises force you to connect that vocabulary to code and visible output.

Closed check: Can you list the five exercise themes and connect each one to a later lecture chapter?

### 01.2 Computer Graphics Overview

Source location: Section 1.2

Computer graphics is about generating images from descriptions. The description can be pixel-based, object-based, physically motivated, artistic, or algorithmic. The common thread is that the computer must decide what color belongs at image samples.

Interactive graphics adds a time constraint. The image is not computed once and admired; it must respond to camera motion, user input, animation, and changing state. That is why real-time rendering often uses approximations and specialized GPU stages.

Study meaning: Graphics is controlled image generation. Interactive graphics is controlled image generation under a strict time budget.

Closed check: What changes when a renderer must be interactive rather than offline?

### 01.3 Pixel-Based Representations

Source location: Section 1.3

A pixel-based representation stores an image directly as samples on a grid. It is easy to display and edit locally, but it does not know the underlying 3D scene. If you zoom into a raster image, you reveal the sampling grid, not more geometry.

This is the first place where sampling becomes important. Resolution, color depth, aliasing, and frame time are not cosmetic details. They decide what information can be represented and how much data must be processed per second.

Study meaning: A raster image is already the answer. It contains color samples, not the geometric reasons behind them.

Closed check: Why can a pixel image be easy to display but hard to reinterpret as a 3D scene?

### 01.4 3D Models

Source location: Section 1.4

A 3D model is a structured description of objects before they become pixels. It may contain vertices, primitives, topology, normals, materials, textures, and transformations. Unlike a pixel image, it can be viewed from different camera positions.

The course mostly follows object-based rendering: start from model data, transform it, project it, rasterize it, shade it, test visibility, and finally update pixels. Later chapters explain these steps one by one.

Study meaning: A model is not an image. It is a cause from which many possible images can be generated.

Closed check: Which model attributes can influence final color besides vertex positions?

### 01.5 Algorithmic Paradigms

Source location: Section 1.5

The lecture contrasts ways to generate images. Rasterization works from objects toward pixels and is the dominant real-time pipeline. Ray-based methods work from image samples into the scene and are powerful for visibility and lighting but can be more expensive.

Do not memorize these paradigms as names only. Ask what direction information flows. Does the algorithm start from geometry and find covered pixels, or from pixels/rays and find visible geometry? That direction explains the strengths and weaknesses.

Study meaning: Rasterization asks, 'Which samples does this primitive cover?' Ray casting asks, 'What does this sample see?'

Closed check: Which paradigm fits OpenGL's standard real-time pipeline most directly?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### raster image

A grid of stored pixel samples; it is already an image, not a 3D scene. In an exam answer, connect `raster image` to the chapter chain: `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`. Say where it appears, what it affects, and what would break if you misunderstood it.

### pixel

A discrete image sample containing color or channel values. In an exam answer, connect `pixel` to the chapter chain: `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`. Say where it appears, what it affects, and what would break if you misunderstood it.

### color depth

The number of bits used to represent color values, controlling precision and memory size. In an exam answer, connect `color depth` to the chapter chain: `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`. Say where it appears, what it affects, and what would break if you misunderstood it.

### 3D model

A structured description of geometry and attributes that can generate many possible images. In an exam answer, connect `3D model` to the chapter chain: `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`. Say where it appears, what it affects, and what would break if you misunderstood it.

### primitive

A basic geometric object such as a point, line, or triangle used by the rendering pipeline. In an exam answer, connect `primitive` to the chapter chain: `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`. Say where it appears, what it affects, and what would break if you misunderstood it.

### interactive graphics

Rendering where images must update quickly enough to respond to input or animation. In an exam answer, connect `interactive graphics` to the chapter chain: `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`image memory = width x height x bits per pixel, then divide by 8 for bytes`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `00 Introduction to C++`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not confuse an image representation with the geometric cause of the image.

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

1. Complete the chain: `scene or image description -> representation choice -> ____ -> visible image -> interaction or analysis`
2. Match `pixel` to its role: A discrete image sample containing color or channel values.
3. Select the dangerous misconception: Do not confuse an image representation with the geometric cause of the image.
4. Explain in one sentence why `color depth` belongs in this chapter.

## 10. End Condition

You are done with Lecture 01 only when you can read a new question, recognize that it belongs to `Introduction`, and reconstruct the relevant part of `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.
