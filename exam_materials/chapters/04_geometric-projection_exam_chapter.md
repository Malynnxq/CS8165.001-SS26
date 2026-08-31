# Lecture 04 - Geometric Projection Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/04_geometric-projection.txt`
Extracted source pages: 61
Primary assignment connection: 04 Projections and Clipping

This is the chapter itself: a readable explanation for studying before you drill the material. Read it before using cloze, matching, MC, sequencing, or assignment practice.

## 1. What Problem This Chapter Solves

Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `view volume`: The 3D region visible to the camera before mapping to the screen. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 04.1 Linear Perspective and Planar Projections

Source location: Sections 4.1-4.2

Perspective projection models the visual effect that farther objects appear smaller. Orthographic projection removes this distance-based size change and keeps parallel lines parallel. Both are useful, but they communicate different spatial relationships.

Planar projection means mapping points onto an image plane. The lecture's art examples are not decoration; they show that projection is a geometric rule for constructing an image from a viewpoint.

Study meaning: Projection is the rule that turns 3D positions into image-plane positions.

Closed check: What visual cue does perspective projection add that orthographic projection lacks?

### 04.2 Camera Modeling

Source location: Section 4.3

A virtual camera is defined by position, orientation, projection type, viewing volume, and image/viewport settings. The view transform places the world relative to the camera. The projection transform maps that view into clip coordinates.

Near and far clipping planes are part of the camera model. They decide what range of depths is represented and strongly affect depth buffer precision. A careless near/far setup can create z-fighting even if the scene geometry is correct.

Study meaning: A camera is not only an eye position; it is also a volume and a mapping rule.

Closed check: Why can changing the near plane affect depth artifacts?

### 04.3 Specifying Projections in OpenGL

Source location: Section 4.4

In OpenGL, projection is usually encoded in a projection matrix sent to a shader. The matrix maps view-space coordinates to clip space. Clipping and the perspective divide then lead toward normalized device coordinates.

Aspect ratio and field of view must match the intended viewport. If the aspect ratio is wrong, objects appear stretched. If the field of view is extreme, the image can look distorted even though the math is functioning.

Study meaning: The projection matrix is the camera lens encoded as linear algebra in homogeneous coordinates.

Closed check: What symptom suggests that the projection aspect ratio does not match the window?

### 04.4 Orthographic and Perspective Derivations

Source location: Sections 4.5-4.6

The derivations are there to explain where the matrix entries come from. Orthographic projection maps a box-shaped view volume into normalized coordinates. Perspective projection maps a frustum and uses the homogeneous component for the later divide.

You do not need to treat these matrices as random formulas. Each part maps a coordinate range into a standard range. The perspective matrix additionally arranges w so that the perspective divide creates foreshortening.

Study meaning: Projection matrices normalize a viewing volume; perspective also prepares the divide by w.

Closed check: What does the perspective divide do to x and y coordinates?

### 04.5 Viewport Transformation

Source location: Section 4.7

After normalized device coordinates, the viewport transform maps the normalized range to actual window coordinates. This is the last geometric mapping before rasterization uses the target grid.

Separating projection from viewport mapping helps debugging. A wrong projection can produce wrong normalized coordinates; a wrong viewport can map otherwise valid coordinates into the wrong part of the window.

Study meaning: Projection decides normalized position; viewport decides where that position lands on the screen.

Closed check: Why is resizing a window related to both viewport and projection settings?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### view volume

The 3D region visible to the camera before mapping to the screen. In an exam answer, connect `view volume` to the chapter chain: `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

### orthographic projection

Projection without perspective foreshortening; parallel lines stay parallel. In an exam answer, connect `orthographic projection` to the chapter chain: `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

### perspective projection

Projection where farther objects appear smaller after division by the homogeneous component. In an exam answer, connect `perspective projection` to the chapter chain: `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

### clip coordinates

Coordinates produced before clipping and perspective divide. In an exam answer, connect `clip coordinates` to the chapter chain: `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

### perspective divide

Division by w that produces normalized device coordinates. In an exam answer, connect `perspective divide` to the chapter chain: `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

### viewport transformation

Mapping normalized device coordinates to window or screen coordinates. In an exam answer, connect `viewport transformation` to the chapter chain: `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `04 Projections and Clipping`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.

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

1. Complete the chain: `view-space position -> ____ -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`
2. Match `orthographic projection` to its role: Projection without perspective foreshortening; parallel lines stay parallel.
3. Select the dangerous misconception: Do not confuse projection with viewport mapping; the perspective divide sits between them.
4. Explain in one sentence why `perspective projection` belongs in this chapter.

## 10. End Condition

You are done with Lecture 04 only when you can read a new question, recognize that it belongs to `Geometric Projection`, and reconstruct the relevant part of `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.
