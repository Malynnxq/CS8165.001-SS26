# Lecture 03 - Geometric Transformations Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/03_geometric-transformations.txt`
Extracted source pages: 54
Primary assignment connection: 03 Geometric Transformations

This is the chapter itself: a readable explanation for studying before you drill the material. Read it before using cloze, matching, MC, sequencing, or assignment practice.

## 1. What Problem This Chapter Solves

Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `homogeneous coordinates`: Coordinates with an additional component that make translation and projection expressible by matrices. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 03.1 Mathematical Foundations

Source location: Section 3.1

The lecture uses vectors and matrices to express geometric operations. A vector can represent a point position, a direction, an offset, or an attribute depending on context. A matrix expresses a linear map or, with homogeneous coordinates, an affine transformation.

The central exam habit is to name the coordinate space. A point in model coordinates and a light direction in view coordinates cannot be mixed safely. Many visual bugs are coordinate-space bugs.

Study meaning: A numeric vector is incomplete until you know what coordinate system it belongs to.

Closed check: Why is a normal vector not transformed exactly like a point under all transformations?

### 03.2 Affine Transformations

Source location: Section 3.2

Affine transformations include translation, rotation, scaling, shearing, and combinations of these. Homogeneous coordinates allow translation to be represented in matrix form together with other transformations.

Translation moves positions but not pure directions. Rotation changes orientation while preserving lengths if it is a proper rotation. Scaling can change lengths and can also affect normals. These distinctions matter later in lighting.

Study meaning: Use 4D homogeneous coordinates so that a single matrix pipeline can move 3D points through the scene.

Closed check: What does the homogeneous w component let a transformation matrix express?

### 03.3 Composition of Transformations

Source location: Section 3.3

Composition means applying several transformations in sequence. The order matters because matrix multiplication is generally not commutative. Rotating an object around its own origin and then translating it is different from translating it and then rotating around the world origin.

When you read a formula such as projection * view * model * position, read it from right to left for the point: first model, then view, then projection. The resulting matrix chain is compact, but the conceptual steps remain separate.

Study meaning: Matrix chains are compressed stories of movement through coordinate spaces.

Closed check: Why can swapping model and view matrices destroy the intended camera/object relation?

### 03.4 Coordinate System Change

Source location: Section 3.4

A transformation can be read actively as moving an object, or passively as changing the coordinate frame used to describe it. Both interpretations are valid, but mixing them carelessly causes sign and order errors.

The view matrix is a classic example: conceptually you position a camera, but the pipeline usually transforms the world by the inverse of the camera transform so that the camera becomes the origin of view space.

Study meaning: Moving the camera one way is equivalent to moving the world the opposite way for rendering.

Closed check: Why is the view transform often related to the inverse camera transform?

### 03.5 Transformations in OpenGL

Source location: Section 3.5

Modern OpenGL does not automatically manage the old matrix stacks. You usually compute model, view, and projection matrices in application code and pass them to shaders as uniforms.

The vertex shader is where the final clip-space position is normally computed. That means a wrong matrix uniform, wrong multiplication order, or wrong convention can make geometry vanish even though buffers and draw calls are correct.

Study meaning: The shader is the place where abstract transformation math becomes GPU execution.

Closed check: Which matrix would you inspect first if an object follows the camera instead of staying in the world?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### homogeneous coordinates

Coordinates with an additional component that make translation and projection expressible by matrices. In an exam answer, connect `homogeneous coordinates` to the chapter chain: `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

### translation

A transformation that moves points by an offset; direction vectors are not shifted the same way. In an exam answer, connect `translation` to the chapter chain: `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

### rotation

A transformation that changes orientation while preserving distances. In an exam answer, connect `rotation` to the chapter chain: `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

### scaling

A transformation that changes size and can distort normals if handled incorrectly. In an exam answer, connect `scaling` to the chapter chain: `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

### matrix composition

Combining transformations by multiplication, where order matters. In an exam answer, connect `matrix composition` to the chapter chain: `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

### normal transformation

Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling. In an exam answer, connect `normal transformation` to the chapter chain: `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`p_world = M_model * p_model; p_view = V * p_world`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `03 Geometric Transformations`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not multiply matrices without naming source space, target space, and order.

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

1. Complete the chain: `object/model coordinates -> ____ -> world coordinates -> view matrix -> camera/view coordinates`
2. Match `translation` to its role: A transformation that moves points by an offset; direction vectors are not shifted the same way.
3. Select the dangerous misconception: Do not multiply matrices without naming source space, target space, and order.
4. Explain in one sentence why `rotation` belongs in this chapter.

## 10. End Condition

You are done with Lecture 03 only when you can read a new question, recognize that it belongs to `Geometric Transformations`, and reconstruct the relevant part of `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.
