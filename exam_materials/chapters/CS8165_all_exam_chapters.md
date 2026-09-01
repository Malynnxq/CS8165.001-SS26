# CS8165 Complete Exam Chapters

- Lecture 01 - Introduction: `chapters/01_introduction_exam_chapter.md`
- Lecture 02 - Rendering Pipeline: `chapters/02_rendering-pipeline_exam_chapter.md`
- Lecture 03 - Geometric Transformations: `chapters/03_geometric-transformations_exam_chapter.md`
- Lecture 04 - Geometric Projection: `chapters/04_geometric-projection_exam_chapter.md`
- Lecture 05 - Clipping: `chapters/05_clipping_exam_chapter.md`
- Lecture 06 - Rasterization: `chapters/06_rasterization_exam_chapter.md`
- Lecture 07 - Visibility Determination: `chapters/07_visibility-determination_exam_chapter.md`
- Lecture 08 - Local Illumination: `chapters/08_local-illumination_exam_chapter.md`
- Lecture 09 - Texturing: `chapters/09_texturing_exam_chapter.md`
- Lecture 10 - Shadows: `chapters/10_shadows_exam_chapter.md`

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

# Lecture 02 - Rendering Pipeline Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/02_rendering-pipeline.txt`
Extracted source pages: 94
Primary assignment connection: 01 Rendering Pipeline

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

# Lecture 03 - Geometric Transformations Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/03_geometric-transformations.txt`
Extracted source pages: 54
Primary assignment connection: 03 Geometric Transformations

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

# Lecture 04 - Geometric Projection Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/04_geometric-projection.txt`
Extracted source pages: 61
Primary assignment connection: 04 Projections and Clipping

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

# Lecture 05 - Clipping Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/05_clipping.txt`
Extracted source pages: 56
Primary assignment connection: 04 Projections and Clipping

## 1. What Problem This Chapter Solves

Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `clipping`: Removing or cutting geometry outside a valid window, plane, or volume. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 05.1 Cohen-Sutherland Line Clipping

Source location: Section 5.1

Cohen-Sutherland assigns outcodes to line endpoints based on which side of the clipping window they lie on. These codes allow quick accept, quick reject, or partial clipping. The algorithm is efficient because many cases are decided before computing intersections.

The exam-friendly idea is the logic of region codes: if both endpoints are inside, keep the segment. If the bitwise AND of the outcodes is nonzero, both endpoints share an outside region and the segment can be rejected. Otherwise, compute an intersection and continue.

Study meaning: Outcodes are a cheap classification before doing intersection math.

Closed check: What does a nonzero bitwise AND of two endpoint outcodes imply?

### 05.2 Cyrus-Beck Line Clipping

Source location: Section 5.2

Cyrus-Beck treats the line parametrically and clips against convex boundaries. Instead of repeatedly using region codes, it finds entering and leaving parameter values along the line.

The key is to reason about the line parameter t. A clipped line segment is not a new unrelated line; it is a restricted interval of the original parametric line. Boundary tests shrink that interval.

Study meaning: Clipping a parametric line means narrowing the valid t interval.

Closed check: Why does Cyrus-Beck naturally require convex clipping regions?

### 05.3 Sutherland-Hodgman Polygon Clipping

Source location: Section 5.3

Sutherland-Hodgman clips a polygon against one boundary at a time. For each edge of the polygon, it decides whether vertices are inside or outside and emits zero, one, or two vertices depending on transitions across the boundary.

This algorithm is easiest to understand as a stream processor. Feed in a polygon, clip it against the left boundary, feed the result into the right boundary, and so on. Each boundary can add intersection vertices.

Study meaning: Polygon clipping is repeated edge-by-edge filtering plus intersection insertion.

Closed check: When can polygon clipping increase the number of vertices?

### 05.4 Weiler-Atherton and Greiner-Hormann

Source location: Sections 5.4-5.5

These algorithms address more complex polygon clipping scenarios, especially when polygon relationships are not as simple as convex-window clipping. They organize intersections and traversal rules to produce correct output boundaries.

For preparation, focus on why simpler algorithms are not enough. Complex polygon intersection can require following alternating boundaries of subject and clipping polygons. That is a topology problem, not only a line-intersection problem.

Study meaning: Complex polygon clipping is about traversing boundary networks after intersections are known.

Closed check: Why are intersection ordering and traversal rules important for polygon clipping?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### clipping

Removing or cutting geometry outside a valid window, plane, or volume. In an exam answer, connect `clipping` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

### Cohen-Sutherland

Line clipping method using region/outcodes to reject, accept, or clip line segments. In an exam answer, connect `Cohen-Sutherland` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

### Sutherland-Hodgman

Polygon clipping method that processes polygon vertices against clipping boundaries. In an exam answer, connect `Sutherland-Hodgman` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

### Cyrus-Beck

Parametric line clipping method using entering and leaving parameter intervals. In an exam answer, connect `Cyrus-Beck` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

### outcode

A compact code describing where a point lies relative to clipping boundaries. In an exam answer, connect `outcode` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

### intersection point

New boundary point created when a primitive crosses a clipping edge or plane. In an exam answer, connect `intersection point` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `04 Projections and Clipping`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.

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

1. Complete the chain: `primitive -> boundary tests -> inside/outside classification -> ____ -> clipped primitive`
2. Match `Cohen-Sutherland` to its role: Line clipping method using region/outcodes to reject, accept, or clip line segments.
3. Select the dangerous misconception: Do not describe clipping as only deletion; crossing primitives can create new vertices.
4. Explain in one sentence why `Sutherland-Hodgman` belongs in this chapter.

## 10. End Condition

You are done with Lecture 05 only when you can read a new question, recognize that it belongs to `Clipping`, and reconstruct the relevant part of `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.

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

# Lecture 08 - Local Illumination Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/08_local-illumination.txt`
Extracted source pages: 62
Primary assignment connection: Rendering contest and shader-related tasks

## 1. What Problem This Chapter Solves

Local illumination computes color from surface orientation, light direction, view direction, and material response. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `surface point + normal + light + view + material -> lighting equation -> shaded color`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `surface normal`: Vector describing surface orientation and controlling diffuse/specular response. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 08.1 Physics of Light

Source location: Section 8.1

The physics slides provide intuition for light as energy interacting with surfaces. For this course, the goal is not full physical simulation but a usable model for real-time rendering.

Important terms are reflection, absorption, wavelength/color, intensity, and direction. These terms become shader inputs or material parameters later. The simplified model must still preserve the relation between light direction, surface orientation, and observed brightness.

Study meaning: Shading is an approximation of light-surface interaction that is cheap enough for rendering.

Closed check: Why does surface orientation affect diffuse brightness?

### 08.2 Light Sources

Source location: Section 8.2

Light source models define where light comes from and how its direction and intensity are computed. Directional lights approximate distant sources with parallel rays. Point lights emit from a position and often include attenuation. Spotlights add a directional cone.

In shader code, the type of light determines how you compute the light vector. A directional light can use a fixed direction; a point light requires subtracting the surface position from the light position.

Study meaning: Different light types mainly change how the light direction and intensity are computed at the surface point.

Closed check: What is the difference between a directional light vector and a point light vector?

### 08.3 Material Models

Source location: Section 8.3

A material model tells the shader how a surface responds to light. Diffuse material scatters light broadly; specular material creates view-dependent highlights; ambient terms approximate background illumination.

Material coefficients are not arbitrary decoration. They scale the contribution of each lighting term. If the specular coefficient is zero, the surface should not show a specular highlight under that model.

Study meaning: Light asks what arrives; material answers how the surface reacts.

Closed check: Which material parameter would you adjust to reduce shiny highlights?

### 08.4 Phong Illumination Model

Source location: Section 8.4

The Phong illumination model combines ambient, diffuse, and specular terms. Diffuse lighting uses the angle between normal and light direction. Specular lighting also depends on the viewer because highlights move with the view direction.

The formula is less important than the decomposition. Ambient is a rough constant approximation. Diffuse is orientation-dependent matte reflection. Specular is view-dependent shininess. A correct answer should name the vectors and normalize them.

Study meaning: Phong-style lighting is a sum of simple terms, each modeling a different visual effect.

Closed check: Why does the specular term depend on the view direction?

### 08.5 Shading

Source location: Section 8.5

Shading decides where the illumination calculation is evaluated and how results are interpolated. Flat shading uses one value per primitive. Gouraud shading evaluates at vertices and interpolates colors. Phong shading interpolates normals and evaluates lighting per fragment.

Per-fragment shading is more expensive but can represent highlights more accurately. This connects directly to the pipeline: interpolation during rasterization provides the data used by the fragment shader.

Study meaning: The shading method decides what is computed at vertices and what is computed at fragments.

Closed check: Why can Gouraud shading miss a small specular highlight?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### surface normal

Vector describing surface orientation and controlling diffuse/specular response. In an exam answer, connect `surface normal` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

### ambient term

Approximate base illumination independent of direct light direction. In an exam answer, connect `ambient term` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

### diffuse reflection

View-independent light response based on the angle between normal and light direction. In an exam answer, connect `diffuse reflection` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

### specular reflection

View-dependent highlight term based on reflection or half-vector alignment. In an exam answer, connect `specular reflection` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

### Phong model

Local illumination model combining ambient, diffuse, and specular components. In an exam answer, connect `Phong model` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

### material coefficient

Parameter controlling how strongly a surface responds to lighting terms. In an exam answer, connect `material coefficient` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`color = ambient + diffuse + specular`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `Rendering contest and shader-related tasks`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `surface point + normal + light + view + material -> lighting equation -> shaded color`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.

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

1. Complete the chain: `surface point + normal + light + view + material -> ____ -> shaded color`
2. Match `ambient term` to its role: Approximate base illumination independent of direct light direction.
3. Select the dangerous misconception: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
4. Explain in one sentence why `diffuse reflection` belongs in this chapter.

## 10. End Condition

You are done with Lecture 08 only when you can read a new question, recognize that it belongs to `Local Illumination`, and reconstruct the relevant part of `surface point + normal + light + view + material -> lighting equation -> shaded color` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.

# Lecture 09 - Texturing Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/09_texturing.txt`
Extracted source pages: 133
Primary assignment connection: Rendering contest and texture/shader tasks

## 1. What Problem This Chapter Solves

Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `texture`: Sampled data array used for color, normals, material data, depth, or other shader inputs. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 09.1 Texture Objects, Texels, Formats, and Color Space

Source location: Section 9.1

A texture object stores sampled data on the GPU. A texel is one stored texture sample. The texture format decides what channels and numeric representation the samples use. Color space matters because color values may be stored nonlinearly, especially for sRGB images.

The key shift is to stop thinking of texture as only a picture. Textures can store color, normals, depth, lookup data, environment information, or volume data. The shader decides how the sampled values are interpreted.

Study meaning: A texture is a GPU-accessible sampled data field.

Closed check: Why can the same texture mechanism store both color maps and normal maps?

### 09.2 Texture Coordinates, UV Mapping, and Wrapping

Source location: Section 9.2

Texture coordinates map surface points to locations in texture space. UV coordinates are usually interpolated across primitives during rasterization and then used by the fragment shader to sample a texture.

Wrapping rules decide what happens outside the normal coordinate range. Repeat, clamp, mirrored repeat, and border behavior are not visual afterthoughts; they define the sampling function outside the base domain.

Study meaning: UVs are the address system that lets a fragment look up texture data.

Closed check: What artifact might appear if a wrapping mode is wrong at the edge of a surface?

### 09.3 Sampling, Filtering, Mipmaps, and Anisotropy

Source location: Section 9.3

Sampling turns continuous texture coordinates into values from discrete texels. Nearest filtering selects a nearby texel and can look blocky. Linear filtering blends nearby texels and looks smoother. Minification is harder because many texels may map to one pixel.

Mipmaps store prefiltered lower-resolution versions of a texture. They reduce aliasing and shimmer when textures are seen at small scale. Anisotropic filtering improves quality when a texture is viewed at a steep angle where footprint shape is elongated.

Study meaning: Filtering reconstructs values; mipmaps choose an appropriate scale before reconstruction.

Closed check: Why does a distant checkerboard shimmer without mipmapping?

### 09.4 Modern OpenGL Texture Pipeline

Source location: Section 9.4

In modern OpenGL, textures are represented by texture objects, bound to texture units, connected to sampler uniforms, and accessed in shaders. The shader does not sample a filename; it samples a bound texture through a sampler.

Texture bugs often come from state mismatches: wrong active texture unit, wrong sampler uniform, missing mipmaps for a mipmap filter, wrong wrap mode, or wrong internal format.

Study meaning: OpenGL texturing is a chain: object data -> texture unit -> sampler uniform -> shader lookup.

Closed check: Why can a texture appear black when the shader code is mathematically correct?

### 09.5 Normal Mapping

Source location: Section 9.5

Normal mapping stores normal directions in a texture so that lighting can vary at a finer scale than the geometry. The surface may have few triangles, but the shader receives detailed normals per fragment.

The hard part is coordinate space. Normal maps are often defined in tangent space, so the shader must transform or interpret them with the correct tangent, bitangent, and normal basis.

Study meaning: Normal mapping changes the lighting normal, not the actual mesh silhouette.

Closed check: Why does normal mapping not change the geometric outline of an object?

### 09.6 Environment Mapping and 3D Textures

Source location: Sections 9.6-9.7

Environment mapping uses textures to represent surrounding illumination or reflections. A direction, not a surface UV alone, can be used to sample an environment map. This is a texture lookup driven by view/reflection geometry.

3D textures and volume rendering extend the same sampled-data idea into three dimensions. Instead of sampling a 2D image, the shader samples a volume. This is useful for data such as medical scans, density fields, or procedural volumetric effects.

Study meaning: Textures are general sampled data; the coordinate dimensionality depends on the problem.

Closed check: What coordinate type would you use to sample a 3D texture?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### texture

Sampled data array used for color, normals, material data, depth, or other shader inputs. In an exam answer, connect `texture` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

### texel

A stored sample in texture memory. In an exam answer, connect `texel` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

### UV coordinates

Coordinates that map surface locations to texture space. In an exam answer, connect `UV coordinates` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

### filtering

Rule for reconstructing values between texels, such as nearest or linear filtering. In an exam answer, connect `filtering` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

### mipmap

Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling. In an exam answer, connect `mipmap` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

### environment mapping

Using texture lookup to approximate surrounding reflections or distant lighting. In an exam answer, connect `environment mapping` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`sampled value = texture(sampler, uv), then shader interprets the value`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `Rendering contest and texture/shader tasks`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not reduce texturing to pasting an image onto geometry.

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

1. Complete the chain: `fragment coordinates -> ____ -> sampler/filter/wrap state -> texel fetch -> shader meaning`
2. Match `texel` to its role: A stored sample in texture memory.
3. Select the dangerous misconception: Do not reduce texturing to pasting an image onto geometry.
4. Explain in one sentence why `UV coordinates` belongs in this chapter.

## 10. End Condition

You are done with Lecture 09 only when you can read a new question, recognize that it belongs to `Texturing`, and reconstruct the relevant part of `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.

# Lecture 10 - Shadows Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/10_shadows.txt`
Extracted source pages: 60
Primary assignment connection: Rendering contest and integrated lighting tasks

## 1. What Problem This Chapter Solves

Shadows are visibility tests from the light source, not only dark shapes seen by the camera. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `shadow`: Reduced direct illumination where an object blocks light from reaching a receiver. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 10.1 Definitions

Source location: Section 10.1

A shadow is not simply a dark texture. It is evidence that light visibility is blocked. Important distinctions include hard versus soft shadows, umbra versus penumbra, and geometric versus precomputed approaches.

For real-time graphics, shadows are usually approximated. The approximation must answer a visibility question cheaply enough for interactive rendering.

Study meaning: Shadows are light-space visibility made visible in the camera image.

Closed check: Why is shadow computation related to visibility determination?

### 10.2 Ground Plane Shadows

Source location: Section 10.2

Ground plane shadows project an object onto a receiving plane. This is simple and can look convincing in restricted scenes, but it assumes a known planar receiver and does not handle general shadowing between arbitrary objects.

The method is useful pedagogically because it makes the geometric nature of shadows explicit: a light source, an occluder, and a receiver define where the shadow lands.

Study meaning: A planar shadow is projected geometry on a known receiver.

Closed check: What scene limitation makes ground plane shadows less general than shadow maps?

### 10.3 Light Maps

Source location: Section 10.3

Light maps store precomputed lighting or shadow information in textures. They can be efficient at runtime, but they are limited when lights, objects, or geometry move dynamically.

This is another example of a recurring graphics tradeoff: precompute for speed, but lose flexibility. Real-time rendering often mixes precomputed and dynamic techniques.

Study meaning: A light map spends storage and preprocessing to save runtime shading work.

Closed check: Why are light maps less suitable for fully dynamic moving lights?

### 10.4 Shadow Volumes

Source location: Section 10.4

Shadow volumes construct the volume of space blocked from a light by an occluder. The camera view can then determine whether visible points lie inside that volume. Stencil buffer techniques are often associated with this method.

The strength is geometric precision for hard shadows. The cost is handling silhouette edges, volume construction, and robust stencil operations. It is a good contrast to shadow maps, which are image-based from the light view.

Study meaning: A shadow volume is the 3D region where the light cannot reach.

Closed check: Why are silhouette edges important for constructing shadow volumes?

### 10.5 Shadow Maps

Source location: Section 10.5

Shadow mapping renders the scene from the light's point of view and stores depth. During the camera pass, a surface point is transformed into light space and compared against the stored depth. If it is farther than what the light saw, it is in shadow.

This method is practical and widely used, but it has artifacts. Shadow acne comes from precision/self-comparison issues. Bias can reduce acne but too much bias causes detached shadows. Resolution, filtering, and light projection strongly affect quality.

Study meaning: Shadow maps reuse the depth-buffer idea, but from the light's camera.

Closed check: What exactly is stored in a shadow map?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### shadow

Reduced direct illumination where an object blocks light from reaching a receiver. In an exam answer, connect `shadow` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

### occluder

Object that blocks light. In an exam answer, connect `occluder` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

### receiver

Surface where the shadow appears. In an exam answer, connect `receiver` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

### shadow map

Depth image rendered from the light's point of view for later visibility comparison. In an exam answer, connect `shadow map` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

### shadow volume

Volume of space hidden from a light by an occluder. In an exam answer, connect `shadow volume` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

### projective shadow

Shadow construction based on projecting geometry onto a receiver. In an exam answer, connect `projective shadow` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`point is shadowed if something is closer to the light along the same light ray`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `Rendering contest and integrated lighting tasks`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.

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

1. Complete the chain: `light -> possible blocker -> ____ -> light-space visibility test -> lit or shadowed result`
2. Match `occluder` to its role: Object that blocks light.
3. Select the dangerous misconception: Do not explain a shadow only from the camera view; the key test is light-space visibility.
4. Explain in one sentence why `receiver` belongs in this chapter.

## 10. End Condition

You are done with Lecture 10 only when you can read a new question, recognize that it belongs to `Shadows`, and reconstruct the relevant part of `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.
