# Lecture 07 - Visibility Determination Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/07_visibility-determination.txt`
Extracted source pages: 69
Primary assignment connection: Rasterization and integrated rendering tasks

## 1. What Problem This Chapter Solves

Visibility algorithms decide which candidate surface is actually seen from the current viewpoint. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `depth buffer`: Per-pixel storage of depth values used to keep the nearest visible fragment. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 07.1 Object-Based Algorithms

Source location: Section 7.1

Object-based visibility algorithms reason about geometry before or while comparing surfaces. They can sort, split, or reject objects based on spatial relations. This is different from simply letting every fragment fight in the depth buffer.

The value of object-based reasoning is reducing work or establishing correct order. The difficulty is that geometry can overlap in complicated ways, so simple global ordering is not always possible.

Study meaning: Object-based visibility tries to solve visibility with geometry before final pixels are written.

Closed check: Why can intersecting polygons make simple depth sorting fail?

### 07.2 Binary Space Partitioning

Source location: Section 7.2

A BSP tree recursively divides space with planes. Once built, it can help traverse geometry in a view-dependent order. This is useful for visibility and ordering because the tree encodes spatial relationships.

The cost is preprocessing and possible splitting of geometry. BSP is a good example of trading memory and setup work for faster or more structured visibility decisions later.

Study meaning: A BSP tree stores a recursive answer to 'which side of this plane is the geometry on?'

Closed check: Why can building a BSP tree require splitting polygons?

### 07.3 Warnock Algorithm

Source location: Section 7.3

Warnock's algorithm works in image space by subdividing regions until visibility is simple enough to decide. If a region is ambiguous, split it. If it is simple, fill it.

This illustrates a general graphics strategy: recursively reduce a hard global problem into smaller local problems. The algorithm is less central in modern OpenGL practice than the depth buffer, but it helps contrast image-space and object-space approaches.

Study meaning: When a region is too complicated, subdivide until the answer becomes simple.

Closed check: What makes Warnock's algorithm image-space rather than object-space?

### 07.4 Depth Buffer Algorithm

Source location: Section 7.4

The depth buffer stores the closest accepted depth at each sample or pixel. For each fragment, compare its depth to the stored depth. If it passes, update the color and depth; otherwise discard it.

The strength of the depth buffer is simplicity and hardware efficiency. The weakness is precision: depth values are finite, and projection distributes precision unevenly. Bad near/far settings can create z-fighting.

Study meaning: The depth buffer is a per-sample competition for closest visible fragment.

Closed check: Why should the near plane not be unnecessarily close to the camera?

### 07.5 Depth Extensions and Ray Casting

Source location: Sections 7.5-7.6

Depth buffer extensions refine or adapt depth-based visibility, for example by handling precision, transparency, or multiple layers more carefully. Standard depth testing alone is not a complete solution for every visibility situation.

Ray casting takes the opposite direction from rasterization: for each image sample, cast a ray into the scene and find the closest intersection. This naturally solves primary visibility but requires intersection work instead of raster coverage work.

Study meaning: Rasterization pushes primitives to pixels; ray casting pulls visibility from pixels into the scene.

Closed check: Why is transparency harder than opaque nearest-surface visibility?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### depth buffer

Per-pixel storage of depth values used to keep the nearest visible fragment. In an exam answer, connect `depth buffer` to the chapter chain: `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`. Say where it appears, what it affects, and what would break if you misunderstood it.

### z-buffer algorithm

Image-space visibility method comparing fragment depths at each pixel. In an exam answer, connect `z-buffer algorithm` to the chapter chain: `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`. Say where it appears, what it affects, and what would break if you misunderstood it.

### Painter's algorithm

Object-order visibility method based on drawing farther objects before nearer objects. In an exam answer, connect `Painter's algorithm` to the chapter chain: `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`. Say where it appears, what it affects, and what would break if you misunderstood it.

### BSP tree

Space-partitioning structure that can support visibility ordering. In an exam answer, connect `BSP tree` to the chapter chain: `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`. Say where it appears, what it affects, and what would break if you misunderstood it.

### Warnock algorithm

Image-space subdivision method for resolving visible surfaces in regions. In an exam answer, connect `Warnock algorithm` to the chapter chain: `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`. Say where it appears, what it affects, and what would break if you misunderstood it.

### ray casting

Finding visible surfaces by tracing rays from image samples into the scene. In an exam answer, connect `ray casting` to the chapter chain: `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`visible fragment = candidate with passing depth/visibility test at the sample`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `Rasterization and integrated rendering tasks`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not confuse generating a fragment with proving that it is visible.

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

1. Complete the chain: `many projected or intersected candidates -> comparison rule -> ____ -> final image contribution`
2. Match `z-buffer algorithm` to its role: Image-space visibility method comparing fragment depths at each pixel.
3. Select the dangerous misconception: Do not confuse generating a fragment with proving that it is visible.
4. Explain in one sentence why `Painter's algorithm` belongs in this chapter.

## 10. End Condition

You are done with Lecture 07 only when you can read a new question, recognize that it belongs to `Visibility Determination`, and reconstruct the relevant part of `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.
