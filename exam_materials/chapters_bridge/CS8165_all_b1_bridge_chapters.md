# CS8165 B1 Bridge Chapters

- Lecture 01 - Introduction: `chapters_bridge/01_introduction_b1_bridge.md`
- Lecture 02 - Rendering Pipeline: `chapters_bridge/02_rendering-pipeline_b1_bridge.md`
- Lecture 03 - Geometric Transformations: `chapters_bridge/03_geometric-transformations_b1_bridge.md`
- Lecture 04 - Geometric Projection: `chapters_bridge/04_geometric-projection_b1_bridge.md`
- Lecture 05 - Clipping: `chapters_bridge/05_clipping_b1_bridge.md`
- Lecture 06 - Rasterization: `chapters_bridge/06_rasterization_b1_bridge.md`
- Lecture 07 - Visibility Determination: `chapters_bridge/07_visibility-determination_b1_bridge.md`
- Lecture 08 - Local Illumination: `chapters_bridge/08_local-illumination_b1_bridge.md`
- Lecture 09 - Texturing: `chapters_bridge/09_texturing_b1_bridge.md`
- Lecture 10 - Shadows: `chapters_bridge/10_shadows_b1_bridge.md`

# Lecture 01 - Introduction B1 Bridge

## 1. Starting Point

This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called Introduction works in a rendering system?

## 2. Everyday Bridge

You already know that a phone or laptop screen is made of many small picture points. This lecture connects that everyday idea to the more technical idea of computer graphics.

The main idea in easier English is this: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.

A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.

For this lecture, the process is:

1. scene or image description. This is the start.

2. representation choice. This comes after the previous step.

3. sampling or rendering process. This comes after the previous step.

4. visible image. This comes after the previous step.

5. interaction or analysis. This comes after the previous step.

## 3. English Bridge

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

Pattern: subject, verb, object, result.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: scene or image description, then representation choice, then sampling or rendering process, then visible image, then interaction or analysis.

Pattern: input, conversion, output.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

Pattern: source space, mapping rule, target space.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

Pattern: object, test, true or false result.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

Pattern: candidate, test rule, accepted or rejected result.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: scene or image description, then representation choice, then sampling or rendering process, then visible image, then interaction or analysis.

Pattern: later step, required earlier step.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

Pattern: storage object, stored value, later access.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

Pattern: current state, draw command, GPU result.

## 4. Terminology Bridge

The important words are not random vocabulary. Each word has a job in the rendering story.

### raster image

Simple meaning: A grid of stored pixel samples; it is already an image, not a 3D scene.

Why it is here: this word helps explain introduction. It connects to this process: `scene or image description, then representation choice, then sampling or rendering process, then visible image, then interaction or analysis`.

Good sentence pattern: `raster image` is used when the system needs to describe, change, test, store, or use this kind of information.

### pixel

Simple meaning: A discrete image sample containing color or channel values.

Why it is here: this word helps explain introduction. It connects to this process: `scene or image description, then representation choice, then sampling or rendering process, then visible image, then interaction or analysis`.

Good sentence pattern: `pixel` is used when the system needs to describe, change, test, store, or use this kind of information.

### color depth

Simple meaning: The number of bits used to represent color values, controlling precision and memory size.

Why it is here: this word helps explain introduction. It connects to this process: `scene or image description, then representation choice, then sampling or rendering process, then visible image, then interaction or analysis`.

Good sentence pattern: `color depth` is used when the system needs to describe, change, test, store, or use this kind of information.

### 3D model

Simple meaning: A structured description of geometry and attributes that can generate many possible images.

Why it is here: this word helps explain introduction. It connects to this process: `scene or image description, then representation choice, then sampling or rendering process, then visible image, then interaction or analysis`.

Good sentence pattern: `3D model` is used when the system needs to describe, change, test, store, or use this kind of information.

### primitive

Simple meaning: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.

Why it is here: this word helps explain introduction. It connects to this process: `scene or image description, then representation choice, then sampling or rendering process, then visible image, then interaction or analysis`.

Good sentence pattern: `primitive` is used when the system needs to describe, change, test, store, or use this kind of information.

### interactive graphics

Simple meaning: Rendering where images must update quickly enough to respond to input or animation.

Why it is here: this word helps explain introduction. It connects to this process: `scene or image description, then representation choice, then sampling or rendering process, then visible image, then interaction or analysis`.

Good sentence pattern: `interactive graphics` is used when the system needs to describe, change, test, store, or use this kind of information.

## 5. Step By Step Bridge

### 01.1 Course Organization

Core sentence: this section explains one part of the introduction.

Main connection: Lecture slides give the vocabulary; exercises force you to connect that vocabulary to code and visible output.

Slower English:

The organizational slides matter because they explain how the theory and programming parts fit together. The exercises are not separate from the lecture, they are the practical version of the same pipeline ideas. When the course says that slides are generally not self explanatory, that is a warning, the bullet points are anchors, not a textbook.

Treat every exercise sheet as an applied checkpoint. Rendering pipeline, primitive types, shaders, transformations, projection, clipping, and rasterization are introduced in the lectures and then turned into OpenGL tasks. If a topic appears both in a lecture and an exercise, it is more likely to be exam relevant.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Can you list the five exercise themes and connect each one to a later lecture chapter?

### 01.2 Computer Graphics Overview

Core sentence: this section explains one part of the introduction.

Main connection: Graphics is controlled image generation. Interactive graphics is controlled image generation under a strict time budget.

Slower English:

Computer graphics is about generating images from descriptions. The description can be pixel based, object based, physically motivated, artistic, or algorithmic. The common thread is that the computer must decide what color belongs at image samples.

Interactive graphics adds a time constraint. The image is not computed once and admired, it must respond to camera motion, user input, animation, and changing state. That is why real time rendering often uses approximations and specialized GPU stages.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What changes when a renderer must be interactive rather than offline?

### 01.3 Pixel-Based Representations

Core sentence: this section explains one part of the introduction.

Main connection: A raster image is already the answer. It contains color samples, not the geometric reasons behind them.

Slower English:

A pixel based representation stores an image directly as samples on a grid. It is easy to display and edit locally, but it does not know the underlying D scene. If you zoom into a raster image, you reveal the sampling grid, not more geometry.

This is the first place where sampling becomes important. Resolution, color depth, aliasing, and frame time are not cosmetic details. They decide what information can be represented and how much data must be processed per second.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why can a pixel image be easy to display but hard to reinterpret as a 3D scene?

### 01.4 3D Models

Core sentence: this section explains one part of the introduction.

Main connection: A model is not an image. It is a cause from which many possible images can be generated.

Slower English:

A D model is a structured description of objects before they become pixels. It may contain vertices, primitives, topology, normals, materials, textures, and transformations. Unlike a pixel image, it can be viewed from different camera positions.

The course mostly follows object based rendering, start from model data, transform it, project it, rasterize it, shade it, test visibility, and finally update pixels. Later chapters explain these steps one by one.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Which model attributes can influence final color besides vertex positions?

### 01.5 Algorithmic Paradigms

Core sentence: this section explains one part of the introduction.

Main connection: Rasterization asks, 'Which samples does this primitive cover?' Ray casting asks, 'What does this sample see?'

Slower English:

The lecture contrasts ways to generate images. Rasterization works from objects toward pixels and is the dominant real time pipeline. Ray based methods work from image samples into the scene and are powerful for visibility and lighting but can be more expensive.

Do not memorize these paradigms as names only. Ask what direction information flows. Does the algorithm start from geometry and find covered pixels, or from pixels or rays and find visible geometry? That direction explains the strengths and weaknesses.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Which paradigm fits OpenGL's standard real-time pipeline most directly?

## 6. Reading The Main Chapter After This

The most dangerous misunderstanding in this lecture is: Do not confuse an image representation with the geometric cause of the image.

The compact rule is: image memory = width x height x bits per pixel, then divide by 8 for bytes

# Lecture 02 - Rendering Pipeline B1 Bridge

## 1. Starting Point

This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called Rendering Pipeline works in a rendering system?

## 2. Everyday Bridge

You already know a factory line, where one station does one job and gives the result to the next station. The rendering pipeline works in a similar way.

The main idea in easier English is this: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.

A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.

For this lecture, the process is:

1. application data. This is the start.

2. geometry stage. This comes after the previous step.

3. primitive assembly. This comes after the previous step.

4. rasterization. This comes after the previous step.

5. fragment operations. This comes after the previous step.

6. framebuffer. This comes after the previous step.

## 3. English Bridge

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

Pattern: subject, verb, object, result.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: application data, then geometry stage, then primitive assembly, then rasterization, then fragment operations, then framebuffer.

Pattern: input, conversion, output.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

Pattern: source space, mapping rule, target space.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

Pattern: object, test, true or false result.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

Pattern: candidate, test rule, accepted or rejected result.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: application data, then geometry stage, then primitive assembly, then rasterization, then fragment operations, then framebuffer.

Pattern: later step, required earlier step.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

Pattern: storage object, stored value, later access.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

Pattern: current state, draw command, GPU result.

## 4. Terminology Bridge

The important words are not random vocabulary. Each word has a job in the rendering story.

### application stage

Simple meaning: CPU-side preparation of models, scene data, interaction, animation, and rendering state.

Why it is here: this word helps explain rendering pipeline. It connects to this process: `application data, then geometry stage, then primitive assembly, then rasterization, then fragment operations, then framebuffer`.

Good sentence pattern: `application stage` is used when the system needs to describe, change, test, store, or use this kind of information.

### geometry stage

Simple meaning: Pipeline stage that transforms vertices and prepares primitives.

Why it is here: this word helps explain rendering pipeline. It connects to this process: `application data, then geometry stage, then primitive assembly, then rasterization, then fragment operations, then framebuffer`.

Good sentence pattern: `geometry stage` is used when the system needs to describe, change, test, store, or use this kind of information.

### rasterization

Simple meaning: Conversion of projected primitives into fragment candidates on a sample grid.

Why it is here: this word helps explain rendering pipeline. It connects to this process: `application data, then geometry stage, then primitive assembly, then rasterization, then fragment operations, then framebuffer`.

Good sentence pattern: `rasterization` is used when the system needs to describe, change, test, store, or use this kind of information.

### fragment

Simple meaning: A candidate pixel contribution produced by rasterization before final tests and blending.

Why it is here: this word helps explain rendering pipeline. It connects to this process: `application data, then geometry stage, then primitive assembly, then rasterization, then fragment operations, then framebuffer`.

Good sentence pattern: `fragment` is used when the system needs to describe, change, test, store, or use this kind of information.

### framebuffer

Simple meaning: Memory target that stores color, depth, stencil, or related per-pixel results.

Why it is here: this word helps explain rendering pipeline. It connects to this process: `application data, then geometry stage, then primitive assembly, then rasterization, then fragment operations, then framebuffer`.

Good sentence pattern: `framebuffer` is used when the system needs to describe, change, test, store, or use this kind of information.

### double buffering

Simple meaning: Using front and back buffers so drawing can happen off-screen before display swap.

Why it is here: this word helps explain rendering pipeline. It connects to this process: `application data, then geometry stage, then primitive assembly, then rasterization, then fragment operations, then framebuffer`.

Good sentence pattern: `double buffering` is used when the system needs to describe, change, test, store, or use this kind of information.

## 5. Step By Step Bridge

### 02.1 Rendering Process

Core sentence: this section explains one part of the rendering pipeline.

Main connection: Vertices become primitives, primitives become fragments, and fragments compete to become pixel updates.

Slower English:

Object based rendering starts with scene objects represented as primitives. The pipeline transforms vertices, assembles primitives, rasterizes them into fragments, and lets only some fragments become pixels. The important detail is that the representation changes at every stage.

The application stage prepares data and state. The geometry stage handles positions and primitives. The rasterization stage creates fragments and applies fragment operations. This separation helps you explain both theory questions and black screen OpenGL bugs.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What is the difference between a fragment and a final pixel?

### 02.2 OpenGL Overview

Core sentence: this section explains one part of the rendering pipeline.

Main connection: OpenGL draw calls consume the state machine as it exists right now.

Slower English:

OpenGL is an API for controlling a graphics pipeline. It is not a renderer by itself in the sense of a single command that understands your scene. You create a context, provide buffers, set state, compile shaders, bind objects, and issue draw calls.

Modern OpenGL is stateful and shader based. Many errors happen because the programmer assumes that a later call carries more information than it really does. The GPU uses the currently bound objects and current state at draw time.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why can binding the wrong vertex array or shader program produce a valid draw call with wrong output?

### 02.3 OpenGL Rendering

Core sentence: this section explains one part of the rendering pipeline.

Main connection: Modern OpenGL makes the data path explicit; that gives control but also creates responsibility.

Slower English:

Older OpenGL exposed a fixed function style where many transformations and lighting choices were configured through predefined calls. Modern OpenGL expects you to write shader programs and explicitly manage data flow.

This is not just historical trivia. It explains why shader code, vertex attributes, uniforms, and buffer objects are central in the exercises. If the shader expects an attribute and the vertex layout does not provide it, the pipeline has no magic fallback.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Which data usually goes into vertex attributes, and which data usually goes into uniforms?

### 02.4 OpenGL Rendering Pipeline

Core sentence: this section explains one part of the rendering pipeline.

Main connection: Programmable shaders compute values; fixed pipeline stages decide coverage, interpolation, tests, and output rules.

Slower English:

The vertex shader runs per vertex and usually outputs clip space position plus attributes for later interpolation. Primitive assembly groups vertices into points, lines, or triangles. Clipping handles geometry outside the view volume. Rasterization creates fragments.

The fragment shader computes candidate fragment output, often using interpolated attributes, uniforms, and textures. After that, tests and operations such as depth testing, stencil testing, blending, and masking decide what reaches the framebuffer.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: If your geometry appears in wireframe but colors are wrong, which stages become suspicious?

### 02.5 Fragment Tests, Framebuffer, and Pixel-Based Rendering

Core sentence: this section explains one part of the rendering pipeline.

Main connection: The framebuffer is the destination; fragment operations are the rules for writing into it.

Slower English:

Fragment tests are the gatekeepers after shading. A fragment can have a perfectly valid color and still fail because depth, stencil, scissor, masking, or blending state prevents a visible update. This is why final pixels are a subset of generated fragments.

The framebuffer stores the final render targets, color buffers, depth buffers, stencil buffers, or custom attachments. Pixel based rendering starts from image data instead of geometric primitives, which is useful for image processing but conceptually different from the object to pixel pipeline.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why can two fragments with different colors produce only one visible pixel color?

## 6. Reading The Main Chapter After This

The most dangerous misunderstanding in this lecture is: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.

The compact rule is: vertices -> primitives -> fragments -> tests -> pixels

# Lecture 03 - Geometric Transformations B1 Bridge

## 1. Starting Point

This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called Geometric Transformations works in a rendering system?

## 2. Everyday Bridge

You already know moving, turning, and resizing objects from normal software. This lecture explains the mathematical version of those actions.

The main idea in easier English is this: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.

A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.

For this lecture, the process is:

1. object/model coordinates. This is the start.

2. model matrix. This comes after the previous step.

3. world coordinates. This comes after the previous step.

4. view matrix. This comes after the previous step.

5. camera/view coordinates. This comes after the previous step.

## 3. English Bridge

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

Pattern: subject, verb, object, result.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: object/model coordinates, then model matrix, then world coordinates, then view matrix, then camera/view coordinates.

Pattern: input, conversion, output.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

Pattern: source space, mapping rule, target space.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

Pattern: object, test, true or false result.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

Pattern: candidate, test rule, accepted or rejected result.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: object/model coordinates, then model matrix, then world coordinates, then view matrix, then camera/view coordinates.

Pattern: later step, required earlier step.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

Pattern: storage object, stored value, later access.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

Pattern: current state, draw command, GPU result.

## 4. Terminology Bridge

The important words are not random vocabulary. Each word has a job in the rendering story.

### homogeneous coordinates

Simple meaning: Coordinates with an additional component that make translation and projection expressible by matrices.

Why it is here: this word helps explain geometric transformations. It connects to this process: `object/model coordinates, then model matrix, then world coordinates, then view matrix, then camera/view coordinates`.

Good sentence pattern: `homogeneous coordinates` is used when the system needs to describe, change, test, store, or use this kind of information.

### translation

Simple meaning: A transformation that moves points by an offset; direction vectors are not shifted the same way.

Why it is here: this word helps explain geometric transformations. It connects to this process: `object/model coordinates, then model matrix, then world coordinates, then view matrix, then camera/view coordinates`.

Good sentence pattern: `translation` is used when the system needs to describe, change, test, store, or use this kind of information.

### rotation

Simple meaning: A transformation that changes orientation while preserving distances.

Why it is here: this word helps explain geometric transformations. It connects to this process: `object/model coordinates, then model matrix, then world coordinates, then view matrix, then camera/view coordinates`.

Good sentence pattern: `rotation` is used when the system needs to describe, change, test, store, or use this kind of information.

### scaling

Simple meaning: A transformation that changes size and can distort normals if handled incorrectly.

Why it is here: this word helps explain geometric transformations. It connects to this process: `object/model coordinates, then model matrix, then world coordinates, then view matrix, then camera/view coordinates`.

Good sentence pattern: `scaling` is used when the system needs to describe, change, test, store, or use this kind of information.

### matrix composition

Simple meaning: Combining transformations by multiplication, where order matters.

Why it is here: this word helps explain geometric transformations. It connects to this process: `object/model coordinates, then model matrix, then world coordinates, then view matrix, then camera/view coordinates`.

Good sentence pattern: `matrix composition` is used when the system needs to describe, change, test, store, or use this kind of information.

### normal transformation

Simple meaning: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling.

Why it is here: this word helps explain geometric transformations. It connects to this process: `object/model coordinates, then model matrix, then world coordinates, then view matrix, then camera/view coordinates`.

Good sentence pattern: `normal transformation` is used when the system needs to describe, change, test, store, or use this kind of information.

## 5. Step By Step Bridge

### 03.1 Mathematical Foundations

Core sentence: this section explains one part of geometric transformations.

Main connection: A numeric vector is incomplete until you know what coordinate system it belongs to.

Slower English:

The lecture uses vectors and matrices to express geometric operations. A vector can represent a point position, a direction, an offset, or an attribute depending on context. A matrix expresses a linear map or, with homogeneous coordinates, an affine transformation.

The central exam habit is to name the coordinate space. A point in model coordinates and a light direction in view coordinates cannot be mixed safely. Many visual bugs are coordinate space bugs.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why is a normal vector not transformed exactly like a point under all transformations?

### 03.2 Affine Transformations

Core sentence: this section explains one part of geometric transformations.

Main connection: Use 4D homogeneous coordinates so that a single matrix pipeline can move 3D points through the scene.

Slower English:

Affine transformations include translation, rotation, scaling, shearing, and combinations of these. Homogeneous coordinates allow translation to be represented in matrix form together with other transformations.

Translation moves positions but not pure directions. Rotation changes orientation while preserving lengths if it is a proper rotation. Scaling can change lengths and can also affect normals. These distinctions matter later in lighting.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What does the homogeneous w component let a transformation matrix express?

### 03.3 Composition of Transformations

Core sentence: this section explains one part of geometric transformations.

Main connection: Matrix chains are compressed stories of movement through coordinate spaces.

Slower English:

Composition means applying several transformations in sequence. The order matters because matrix multiplication is generally not commutative. Rotating an object around its own origin and then translating it is different from translating it and then rotating around the world origin.

When you read a formula such as projection times view times model times position, read it from right to left for the point, first model, then view, then projection. The resulting matrix chain is compact, but the conceptual steps remain separate.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why can swapping model and view matrices destroy the intended camera/object relation?

### 03.4 Coordinate System Change

Core sentence: this section explains one part of geometric transformations.

Main connection: Moving the camera one way is equivalent to moving the world the opposite way for rendering.

Slower English:

A transformation can be read actively as moving an object, or passively as changing the coordinate frame used to describe it. Both interpretations are valid, but mixing them carelessly causes sign and order errors.

The view matrix is a classic example, conceptually you position a camera, but the pipeline usually transforms the world by the inverse of the camera transform so that the camera becomes the origin of view space.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why is the view transform often related to the inverse camera transform?

### 03.5 Transformations in OpenGL

Core sentence: this section explains one part of geometric transformations.

Main connection: The shader is the place where abstract transformation math becomes GPU execution.

Slower English:

Modern OpenGL does not automatically manage the old matrix stacks. You usually compute model, view, and projection matrices in application code and pass them to shaders as uniforms.

The vertex shader is where the final clip space position is normally computed. That means a wrong matrix uniform, wrong multiplication order, or wrong convention can make geometry vanish even though buffers and draw calls are correct.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Which matrix would you inspect first if an object follows the camera instead of staying in the world?

## 6. Reading The Main Chapter After This

The most dangerous misunderstanding in this lecture is: Do not multiply matrices without naming source space, target space, and order.

The compact rule is: p_world = M_model * p_model; p_view = V * p_world

# Lecture 04 - Geometric Projection B1 Bridge

## 1. Starting Point

This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called Geometric Projection works in a rendering system?

## 2. Everyday Bridge

You already know that a camera turns a three dimensional scene into a flat picture. Projection is the graphics version of that idea.

The main idea in easier English is this: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.

A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.

For this lecture, the process is:

1. view-space position. This is the start.

2. projection matrix. This comes after the previous step.

3. clip coordinates. This comes after the previous step.

4. perspective divide. This comes after the previous step.

5. NDC. This comes after the previous step.

6. viewport coordinates. This comes after the previous step.

## 3. English Bridge

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

Pattern: subject, verb, object, result.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: view-space position, then projection matrix, then clip coordinates, then perspective divide, then NDC, then viewport coordinates.

Pattern: input, conversion, output.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

Pattern: source space, mapping rule, target space.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

Pattern: object, test, true or false result.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

Pattern: candidate, test rule, accepted or rejected result.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: view-space position, then projection matrix, then clip coordinates, then perspective divide, then NDC, then viewport coordinates.

Pattern: later step, required earlier step.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

Pattern: storage object, stored value, later access.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

Pattern: current state, draw command, GPU result.

## 4. Terminology Bridge

The important words are not random vocabulary. Each word has a job in the rendering story.

### view volume

Simple meaning: The 3D region visible to the camera before mapping to the screen.

Why it is here: this word helps explain geometric projection. It connects to this process: `view-space position, then projection matrix, then clip coordinates, then perspective divide, then NDC, then viewport coordinates`.

Good sentence pattern: `view volume` is used when the system needs to describe, change, test, store, or use this kind of information.

### orthographic projection

Simple meaning: Projection without perspective foreshortening; parallel lines stay parallel.

Why it is here: this word helps explain geometric projection. It connects to this process: `view-space position, then projection matrix, then clip coordinates, then perspective divide, then NDC, then viewport coordinates`.

Good sentence pattern: `orthographic projection` is used when the system needs to describe, change, test, store, or use this kind of information.

### perspective projection

Simple meaning: Projection where farther objects appear smaller after division by the homogeneous component.

Why it is here: this word helps explain geometric projection. It connects to this process: `view-space position, then projection matrix, then clip coordinates, then perspective divide, then NDC, then viewport coordinates`.

Good sentence pattern: `perspective projection` is used when the system needs to describe, change, test, store, or use this kind of information.

### clip coordinates

Simple meaning: Coordinates produced before clipping and perspective divide.

Why it is here: this word helps explain geometric projection. It connects to this process: `view-space position, then projection matrix, then clip coordinates, then perspective divide, then NDC, then viewport coordinates`.

Good sentence pattern: `clip coordinates` is used when the system needs to describe, change, test, store, or use this kind of information.

### perspective divide

Simple meaning: Division by w that produces normalized device coordinates.

Why it is here: this word helps explain geometric projection. It connects to this process: `view-space position, then projection matrix, then clip coordinates, then perspective divide, then NDC, then viewport coordinates`.

Good sentence pattern: `perspective divide` is used when the system needs to describe, change, test, store, or use this kind of information.

### viewport transformation

Simple meaning: Mapping normalized device coordinates to window or screen coordinates.

Why it is here: this word helps explain geometric projection. It connects to this process: `view-space position, then projection matrix, then clip coordinates, then perspective divide, then NDC, then viewport coordinates`.

Good sentence pattern: `viewport transformation` is used when the system needs to describe, change, test, store, or use this kind of information.

## 5. Step By Step Bridge

### 04.1 Linear Perspective and Planar Projections

Core sentence: this section explains one part of geometric projection.

Main connection: Projection is the rule that turns 3D positions into image-plane positions.

Slower English:

Perspective projection models the visual effect that farther objects appear smaller. Orthographic projection removes this distance based size change and keeps parallel lines parallel. Both are useful, but they communicate different spatial relationships.

Planar projection means mapping points onto an image plane. The lectures art examples are not decoration, they show that projection is a geometric rule for constructing an image from a viewpoint.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What visual cue does perspective projection add that orthographic projection lacks?

### 04.2 Camera Modeling

Core sentence: this section explains one part of geometric projection.

Main connection: A camera is not only an eye position; it is also a volume and a mapping rule.

Slower English:

A virtual camera is defined by position, orientation, projection type, viewing volume, and image or viewport settings. The view transform places the world relative to the camera. The projection transform maps that view into clip coordinates.

Near and far clipping planes are part of the camera model. They decide what range of depths is represented and strongly affect depth buffer precision. A careless near or far setup can create z fighting even if the scene geometry is correct.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why can changing the near plane affect depth artifacts?

### 04.3 Specifying Projections in OpenGL

Core sentence: this section explains one part of geometric projection.

Main connection: The projection matrix is the camera lens encoded as linear algebra in homogeneous coordinates.

Slower English:

In OpenGL, projection is usually encoded in a projection matrix sent to a shader. The matrix maps view space coordinates to clip space. Clipping and the perspective divide then lead toward normalized device coordinates.

Aspect ratio and field of view must match the intended viewport. If the aspect ratio is wrong, objects appear stretched. If the field of view is extreme, the image can look distorted even though the math is functioning.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What symptom suggests that the projection aspect ratio does not match the window?

### 04.4 Orthographic and Perspective Derivations

Core sentence: this section explains one part of geometric projection.

Main connection: Projection matrices normalize a viewing volume; perspective also prepares the divide by w.

Slower English:

The derivations are there to explain where the matrix entries come from. Orthographic projection maps a box shaped view volume into normalized coordinates. Perspective projection maps a frustum and uses the homogeneous component for the later divide.

You do not need to treat these matrices as random formulas. Each part maps a coordinate range into a standard range. The perspective matrix additionally arranges w so that the perspective divide creates foreshortening.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What does the perspective divide do to x and y coordinates?

### 04.5 Viewport Transformation

Core sentence: this section explains one part of geometric projection.

Main connection: Projection decides normalized position; viewport decides where that position lands on the screen.

Slower English:

After normalized device coordinates, the viewport transform maps the normalized range to actual window coordinates. This is the last geometric mapping before rasterization uses the target grid.

Separating projection from viewport mapping helps debugging. A wrong projection can produce wrong normalized coordinates, a wrong viewport can map otherwise valid coordinates into the wrong part of the window.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why is resizing a window related to both viewport and projection settings?

## 6. Reading The Main Chapter After This

The most dangerous misunderstanding in this lecture is: Do not confuse projection with viewport mapping; the perspective divide sits between them.

The compact rule is: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w

# Lecture 05 - Clipping B1 Bridge

## 1. Starting Point

This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called Clipping works in a rendering system?

## 2. Everyday Bridge

You already know cropping a photo or cutting away the part of a picture that is outside a window. Clipping is the geometric version of that idea.

The main idea in easier English is this: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.

A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.

For this lecture, the process is:

1. primitive. This is the start.

2. boundary tests. This comes after the previous step.

3. inside/outside classification. This comes after the previous step.

4. intersections. This comes after the previous step.

5. clipped primitive. This comes after the previous step.

## 3. English Bridge

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

Pattern: subject, verb, object, result.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive.

Pattern: input, conversion, output.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

Pattern: source space, mapping rule, target space.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

Pattern: object, test, true or false result.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

Pattern: candidate, test rule, accepted or rejected result.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive.

Pattern: later step, required earlier step.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

Pattern: storage object, stored value, later access.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

Pattern: current state, draw command, GPU result.

## 4. Terminology Bridge

The important words are not random vocabulary. Each word has a job in the rendering story.

### clipping

Simple meaning: Removing or cutting geometry outside a valid window, plane, or volume.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `clipping` is used when the system needs to describe, change, test, store, or use this kind of information.

### Cohen-Sutherland

Simple meaning: Line clipping method using region/outcodes to reject, accept, or clip line segments.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `Cohen-Sutherland` is used when the system needs to describe, change, test, store, or use this kind of information.

### Sutherland-Hodgman

Simple meaning: Polygon clipping method that processes polygon vertices against clipping boundaries.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `Sutherland-Hodgman` is used when the system needs to describe, change, test, store, or use this kind of information.

### Cyrus-Beck

Simple meaning: Parametric line clipping method using entering and leaving parameter intervals.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `Cyrus-Beck` is used when the system needs to describe, change, test, store, or use this kind of information.

### outcode

Simple meaning: A compact code describing where a point lies relative to clipping boundaries.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `outcode` is used when the system needs to describe, change, test, store, or use this kind of information.

### intersection point

Simple meaning: New boundary point created when a primitive crosses a clipping edge or plane.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `intersection point` is used when the system needs to describe, change, test, store, or use this kind of information.

## 5. Step By Step Bridge

### 05.1 Cohen-Sutherland Line Clipping

Core sentence: this section explains one part of clipping.

Main connection: Outcodes are a cheap classification before doing intersection math.

Slower English:

Cohen Sutherland assigns outcodes to line endpoints based on which side of the clipping window they lie on. These codes allow quick accept, quick reject, or partial clipping. The algorithm is efficient because many cases are decided before computing intersections.

The exam friendly idea is the logic of region codes, if both endpoints are inside, keep the segment. If the bitwise AND of the outcodes is nonzero, both endpoints share an outside region and the segment can be rejected. Otherwise, compute an intersection and continue.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What does a nonzero bitwise AND of two endpoint outcodes imply?

### 05.2 Cyrus-Beck Line Clipping

Core sentence: this section explains one part of clipping.

Main connection: Clipping a parametric line means narrowing the valid t interval.

Slower English:

Cyrus Beck treats the line parametrically and clips against convex boundaries. Instead of repeatedly using region codes, it finds entering and leaving parameter values along the line.

The key is to reason about the line parameter t. A clipped line segment is not a new unrelated line, it is a restricted interval of the original parametric line. Boundary tests shrink that interval.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why does Cyrus-Beck naturally require convex clipping regions?

### 05.3 Sutherland-Hodgman Polygon Clipping

Core sentence: this section explains one part of clipping.

Main connection: Polygon clipping is repeated edge-by-edge filtering plus intersection insertion.

Slower English:

Sutherland Hodgman clips a polygon against one boundary at a time. For each edge of the polygon, it decides whether vertices are inside or outside and emits zero, one, or two vertices depending on transitions across the boundary.

This algorithm is easiest to understand as a stream processor. Feed in a polygon, clip it against the left boundary, feed the result into the right boundary, and so on. Each boundary can add intersection vertices.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: When can polygon clipping increase the number of vertices?

### 05.4 Weiler-Atherton and Greiner-Hormann

Core sentence: this section explains one part of clipping.

Main connection: Complex polygon clipping is about traversing boundary networks after intersections are known.

Slower English:

These algorithms address more complex polygon clipping scenarios, especially when polygon relationships are not as simple as convex window clipping. They organize intersections and traversal rules to produce correct output boundaries.

For preparation, focus on why simpler algorithms are not enough. Complex polygon intersection can require following alternating boundaries of subject and clipping polygons. That is a topology problem, not only a line intersection problem.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why are intersection ordering and traversal rules important for polygon clipping?

## 6. Reading The Main Chapter After This

The most dangerous misunderstanding in this lecture is: Do not describe clipping as only deletion; crossing primitives can create new vertices.

The compact rule is: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval

# Lecture 06 - Rasterization B1 Bridge

## 1. Starting Point

This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called Rasterization works in a rendering system?

## 2. Everyday Bridge

You already know that a screen is a grid. Rasterization explains how smooth geometric shapes become decisions on that grid.

The main idea in easier English is this: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.

A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.

For this lecture, the process is:

1. projected primitive. This is the start.

2. sample coverage. This comes after the previous step.

3. fragment generation. This comes after the previous step.

4. attribute interpolation. This comes after the previous step.

5. fragment tests. This comes after the previous step.

## 3. English Bridge

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

Pattern: subject, verb, object, result.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: projected primitive, then sample coverage, then fragment generation, then attribute interpolation, then fragment tests.

Pattern: input, conversion, output.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

Pattern: source space, mapping rule, target space.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

Pattern: object, test, true or false result.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

Pattern: candidate, test rule, accepted or rejected result.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: projected primitive, then sample coverage, then fragment generation, then attribute interpolation, then fragment tests.

Pattern: later step, required earlier step.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

Pattern: storage object, stored value, later access.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

Pattern: current state, draw command, GPU result.

## 4. Terminology Bridge

The important words are not random vocabulary. Each word has a job in the rendering story.

### scan conversion

Simple meaning: Determining which discrete samples are covered by an ideal geometric primitive.

Why it is here: this word helps explain rasterization. It connects to this process: `projected primitive, then sample coverage, then fragment generation, then attribute interpolation, then fragment tests`.

Good sentence pattern: `scan conversion` is used when the system needs to describe, change, test, store, or use this kind of information.

### triangle coverage

Simple meaning: Testing which pixel/sample positions lie inside a triangle.

Why it is here: this word helps explain rasterization. It connects to this process: `projected primitive, then sample coverage, then fragment generation, then attribute interpolation, then fragment tests`.

Good sentence pattern: `triangle coverage` is used when the system needs to describe, change, test, store, or use this kind of information.

### barycentric coordinates

Simple meaning: Weights relative to triangle vertices used for inside tests and interpolation.

Why it is here: this word helps explain rasterization. It connects to this process: `projected primitive, then sample coverage, then fragment generation, then attribute interpolation, then fragment tests`.

Good sentence pattern: `barycentric coordinates` is used when the system needs to describe, change, test, store, or use this kind of information.

### interpolation

Simple meaning: Computing per-fragment values from vertex attributes.

Why it is here: this word helps explain rasterization. It connects to this process: `projected primitive, then sample coverage, then fragment generation, then attribute interpolation, then fragment tests`.

Good sentence pattern: `interpolation` is used when the system needs to describe, change, test, store, or use this kind of information.

### aliasing

Simple meaning: Artifacts caused when continuous signals are sampled too coarsely.

Why it is here: this word helps explain rasterization. It connects to this process: `projected primitive, then sample coverage, then fragment generation, then attribute interpolation, then fragment tests`.

Good sentence pattern: `aliasing` is used when the system needs to describe, change, test, store, or use this kind of information.

### fragment candidate

Simple meaning: A potential contribution to the framebuffer, not yet a guaranteed visible pixel.

Why it is here: this word helps explain rasterization. It connects to this process: `projected primitive, then sample coverage, then fragment generation, then attribute interpolation, then fragment tests`.

Good sentence pattern: `fragment candidate` is used when the system needs to describe, change, test, store, or use this kind of information.

## 5. Step By Step Bridge

### 06.1 Line Rasterization

Core sentence: this section explains one part of rasterization.

Main connection: Rasterizing a line means approximating a continuous path by grid decisions.

Slower English:

A mathematical line has infinitely many points, but a raster display has a finite grid. Line rasterization decides which grid cells or samples best approximate the ideal line. The algorithm must balance accuracy, speed, and consistency.

Incremental algorithms avoid recomputing expensive formulas for every pixel. The important idea is to step along one axis and update an error term that decides when to step along the other axis.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why are incremental error updates useful in line rasterization?

### 06.2 Triangle Edge Rasterization

Core sentence: this section explains one part of rasterization.

Main connection: Triangle rasterization answers the question: which samples are inside this projected triangle?

Slower English:

Triangles are the core primitive in real time rendering. Edge functions or half space tests decide whether a sample lies inside the triangle. This allows the rasterizer to test coverage systematically.

Coverage is not final visibility. A covered sample becomes a fragment candidate. Depth testing, stencil testing, blending, and other operations still decide whether the framebuffer changes.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What later stage can reject a fragment after triangle coverage succeeds?

### 06.3 Region Filling

Core sentence: this section explains one part of rasterization.

Main connection: Filling is about turning boundary descriptions into consistent interior samples.

Slower English:

Region filling generalizes the idea of determining interior samples. The algorithm must identify connected areas or spans that should receive color. This connects rasterization to scan conversion and image space reasoning.

The practical issue is avoiding gaps, double fills, or inconsistent boundary handling. Small choices at edges can become visible artifacts when many primitives meet.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why can inconsistent edge rules create cracks between adjacent primitives?

### 06.4 Scanline-Based Triangle Rasterization

Core sentence: this section explains one part of rasterization.

Main connection: Each scanline asks: where does this triangle enter and leave this row?

Slower English:

Scanline rasterization processes horizontal rows of the image. For each row that crosses a triangle, the algorithm finds the covered interval and fills the span. Attribute interpolation can be updated along edges and across each span.

The method is intuitive because it follows the memory layout of many images. It also demonstrates why interpolation is tied to rasterization, once you know a sample location inside the primitive, you can interpolate depth, color, normals, or texture coordinates.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Which attributes might be interpolated while filling triangle spans?

### 06.5 Tile-Based Triangle Rasterization

Core sentence: this section explains one part of rasterization.

Main connection: Block-based rasterization keeps the same coverage problem but changes the work organization.

Slower English:

Tile or block based approaches group pixels into small regions. This can improve locality and parallel work distribution. Modern GPUs often reason in blocks or tiles internally because rendering is massively parallel.

For the exam, connect this to efficiency. The mathematical goal is still coverage, but the implementation is organized to use hardware resources well.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why is block organization attractive for parallel graphics hardware?

## 6. Reading The Main Chapter After This

The most dangerous misunderstanding in this lecture is: Do not call every generated fragment a final pixel.

The compact rule is: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1

# Lecture 07 - Visibility Determination B1 Bridge

## 1. Starting Point

This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called Visibility Determination works in a rendering system?

## 2. Everyday Bridge

You already know that a nearer object can hide a farther object. Visibility determination is the formal version of that simple fact.

The main idea in easier English is this: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.

A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.

For this lecture, the process is:

1. many projected or intersected candidates. This is the start.

2. comparison rule. This comes after the previous step.

3. visible surface or fragment. This comes after the previous step.

4. final image contribution. This comes after the previous step.

## 3. English Bridge

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

Pattern: subject, verb, object, result.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: many projected or intersected candidates, then comparison rule, then visible surface or fragment, then final image contribution.

Pattern: input, conversion, output.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

Pattern: source space, mapping rule, target space.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

Pattern: object, test, true or false result.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

Pattern: candidate, test rule, accepted or rejected result.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: many projected or intersected candidates, then comparison rule, then visible surface or fragment, then final image contribution.

Pattern: later step, required earlier step.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

Pattern: storage object, stored value, later access.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

Pattern: current state, draw command, GPU result.

## 4. Terminology Bridge

The important words are not random vocabulary. Each word has a job in the rendering story.

### depth buffer

Simple meaning: Per-pixel storage of depth values used to keep the nearest visible fragment.

Why it is here: this word helps explain visibility determination. It connects to this process: `many projected or intersected candidates, then comparison rule, then visible surface or fragment, then final image contribution`.

Good sentence pattern: `depth buffer` is used when the system needs to describe, change, test, store, or use this kind of information.

### z-buffer algorithm

Simple meaning: Image-space visibility method comparing fragment depths at each pixel.

Why it is here: this word helps explain visibility determination. It connects to this process: `many projected or intersected candidates, then comparison rule, then visible surface or fragment, then final image contribution`.

Good sentence pattern: `z-buffer algorithm` is used when the system needs to describe, change, test, store, or use this kind of information.

### Painter's algorithm

Simple meaning: Object-order visibility method based on drawing farther objects before nearer objects.

Why it is here: this word helps explain visibility determination. It connects to this process: `many projected or intersected candidates, then comparison rule, then visible surface or fragment, then final image contribution`.

Good sentence pattern: `Painter's algorithm` is used when the system needs to describe, change, test, store, or use this kind of information.

### BSP tree

Simple meaning: Space-partitioning structure that can support visibility ordering.

Why it is here: this word helps explain visibility determination. It connects to this process: `many projected or intersected candidates, then comparison rule, then visible surface or fragment, then final image contribution`.

Good sentence pattern: `BSP tree` is used when the system needs to describe, change, test, store, or use this kind of information.

### Warnock algorithm

Simple meaning: Image-space subdivision method for resolving visible surfaces in regions.

Why it is here: this word helps explain visibility determination. It connects to this process: `many projected or intersected candidates, then comparison rule, then visible surface or fragment, then final image contribution`.

Good sentence pattern: `Warnock algorithm` is used when the system needs to describe, change, test, store, or use this kind of information.

### ray casting

Simple meaning: Finding visible surfaces by tracing rays from image samples into the scene.

Why it is here: this word helps explain visibility determination. It connects to this process: `many projected or intersected candidates, then comparison rule, then visible surface or fragment, then final image contribution`.

Good sentence pattern: `ray casting` is used when the system needs to describe, change, test, store, or use this kind of information.

## 5. Step By Step Bridge

### 07.1 Object-Based Algorithms

Core sentence: this section explains one part of visibility determination.

Main connection: Object-based visibility tries to solve visibility with geometry before final pixels are written.

Slower English:

Object based visibility algorithms reason about geometry before or while comparing surfaces. They can sort, split, or reject objects based on spatial relations. This is different from simply letting every fragment fight in the depth buffer.

The value of object based reasoning is reducing work or establishing correct order. The difficulty is that geometry can overlap in complicated ways, so simple global ordering is not always possible.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why can intersecting polygons make simple depth sorting fail?

### 07.2 Binary Space Partitioning

Core sentence: this section explains one part of visibility determination.

Main connection: A BSP tree stores a recursive answer to 'which side of this plane is the geometry on?'

Slower English:

A BSP tree recursively divides space with planes. Once built, it can help traverse geometry in a view dependent order. This is useful for visibility and ordering because the tree encodes spatial relationships.

The cost is preprocessing and possible splitting of geometry. BSP is a good example of trading memory and setup work for faster or more structured visibility decisions later.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why can building a BSP tree require splitting polygons?

### 07.3 Warnock Algorithm

Core sentence: this section explains one part of visibility determination.

Main connection: When a region is too complicated, subdivide until the answer becomes simple.

Slower English:

Warnocks algorithm works in image space by subdividing regions until visibility is simple enough to decide. If a region is ambiguous, split it. If it is simple, fill it.

This illustrates a general graphics strategy, recursively reduce a hard global problem into smaller local problems. The algorithm is less central in modern OpenGL practice than the depth buffer, but it helps contrast image space and object space approaches.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What makes Warnock's algorithm image-space rather than object-space?

### 07.4 Depth Buffer Algorithm

Core sentence: this section explains one part of visibility determination.

Main connection: The depth buffer is a per-sample competition for closest visible fragment.

Slower English:

The depth buffer stores the closest accepted depth at each sample or pixel. For each fragment, compare its depth to the stored depth. If it passes, update the color and depth, otherwise discard it.

The strength of the depth buffer is simplicity and hardware efficiency. The weakness is precision, depth values are finite, and projection distributes precision unevenly. Bad near or far settings can create z fighting.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why should the near plane not be unnecessarily close to the camera?

### 07.5 Depth Extensions and Ray Casting

Core sentence: this section explains one part of visibility determination.

Main connection: Rasterization pushes primitives to pixels; ray casting pulls visibility from pixels into the scene.

Slower English:

Depth buffer extensions refine or adapt depth based visibility, for example by handling precision, transparency, or multiple layers more carefully. Standard depth testing alone is not a complete solution for every visibility situation.

Ray casting takes the opposite direction from rasterization, for each image sample, cast a ray into the scene and find the closest intersection. This naturally solves primary visibility but requires intersection work instead of raster coverage work.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why is transparency harder than opaque nearest-surface visibility?

## 6. Reading The Main Chapter After This

The most dangerous misunderstanding in this lecture is: Do not confuse generating a fragment with proving that it is visible.

The compact rule is: visible fragment = candidate with passing depth/visibility test at the sample

# Lecture 08 - Local Illumination B1 Bridge

## 1. Starting Point

This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called Local Illumination works in a rendering system?

## 2. Everyday Bridge

You already know that a surface looks brighter when it faces a lamp and darker when it turns away. Local illumination explains this with vectors and material values.

The main idea in easier English is this: Local illumination computes color from surface orientation, light direction, view direction, and material response.

A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.

For this lecture, the process is:

1. surface point + normal + light + view + material. This is the start.

2. lighting equation. This comes after the previous step.

3. shaded color. This comes after the previous step.

## 3. English Bridge

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

Pattern: subject, verb, object, result.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: surface point + normal + light + view + material, then lighting equation, then shaded color.

Pattern: input, conversion, output.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

Pattern: source space, mapping rule, target space.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

Pattern: object, test, true or false result.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

Pattern: candidate, test rule, accepted or rejected result.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: surface point + normal + light + view + material, then lighting equation, then shaded color.

Pattern: later step, required earlier step.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

Pattern: storage object, stored value, later access.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

Pattern: current state, draw command, GPU result.

## 4. Terminology Bridge

The important words are not random vocabulary. Each word has a job in the rendering story.

### surface normal

Simple meaning: Vector describing surface orientation and controlling diffuse/specular response.

Why it is here: this word helps explain local illumination. It connects to this process: `surface point + normal + light + view + material, then lighting equation, then shaded color`.

Good sentence pattern: `surface normal` is used when the system needs to describe, change, test, store, or use this kind of information.

### ambient term

Simple meaning: Approximate base illumination independent of direct light direction.

Why it is here: this word helps explain local illumination. It connects to this process: `surface point + normal + light + view + material, then lighting equation, then shaded color`.

Good sentence pattern: `ambient term` is used when the system needs to describe, change, test, store, or use this kind of information.

### diffuse reflection

Simple meaning: View-independent light response based on the angle between normal and light direction.

Why it is here: this word helps explain local illumination. It connects to this process: `surface point + normal + light + view + material, then lighting equation, then shaded color`.

Good sentence pattern: `diffuse reflection` is used when the system needs to describe, change, test, store, or use this kind of information.

### specular reflection

Simple meaning: View-dependent highlight term based on reflection or half-vector alignment.

Why it is here: this word helps explain local illumination. It connects to this process: `surface point + normal + light + view + material, then lighting equation, then shaded color`.

Good sentence pattern: `specular reflection` is used when the system needs to describe, change, test, store, or use this kind of information.

### Phong model

Simple meaning: Local illumination model combining ambient, diffuse, and specular components.

Why it is here: this word helps explain local illumination. It connects to this process: `surface point + normal + light + view + material, then lighting equation, then shaded color`.

Good sentence pattern: `Phong model` is used when the system needs to describe, change, test, store, or use this kind of information.

### material coefficient

Simple meaning: Parameter controlling how strongly a surface responds to lighting terms.

Why it is here: this word helps explain local illumination. It connects to this process: `surface point + normal + light + view + material, then lighting equation, then shaded color`.

Good sentence pattern: `material coefficient` is used when the system needs to describe, change, test, store, or use this kind of information.

## 5. Step By Step Bridge

### 08.1 Physics of Light

Core sentence: this section explains one part of local illumination.

Main connection: Shading is an approximation of light-surface interaction that is cheap enough for rendering.

Slower English:

The physics slides provide intuition for light as energy interacting with surfaces. For this course, the goal is not full physical simulation but a usable model for real time rendering.

Important terms are reflection, absorption, wavelength or color, intensity, and direction. These terms become shader inputs or material parameters later. The simplified model must still preserve the relation between light direction, surface orientation, and observed brightness.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why does surface orientation affect diffuse brightness?

### 08.2 Light Sources

Core sentence: this section explains one part of local illumination.

Main connection: Different light types mainly change how the light direction and intensity are computed at the surface point.

Slower English:

Light source models define where light comes from and how its direction and intensity are computed. Directional lights approximate distant sources with parallel rays. Point lights emit from a position and often include attenuation. Spotlights add a directional cone.

In shader code, the type of light determines how you compute the light vector. A directional light can use a fixed direction, a point light requires subtracting the surface position from the light position.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What is the difference between a directional light vector and a point light vector?

### 08.3 Material Models

Core sentence: this section explains one part of local illumination.

Main connection: Light asks what arrives; material answers how the surface reacts.

Slower English:

A material model tells the shader how a surface responds to light. Diffuse material scatters light broadly, specular material creates view dependent highlights, ambient terms approximate background illumination.

Material coefficients are not arbitrary decoration. They scale the contribution of each lighting term. If the specular coefficient is zero, the surface should not show a specular highlight under that model.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Which material parameter would you adjust to reduce shiny highlights?

### 08.4 Phong Illumination Model

Core sentence: this section explains one part of local illumination.

Main connection: Phong-style lighting is a sum of simple terms, each modeling a different visual effect.

Slower English:

The Phong illumination model combines ambient, diffuse, and specular terms. Diffuse lighting uses the angle between normal and light direction. Specular lighting also depends on the viewer because highlights move with the view direction.

The formula is less important than the decomposition. Ambient is a rough constant approximation. Diffuse is orientation dependent matte reflection. Specular is view dependent shininess. A correct answer should name the vectors and normalize them.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why does the specular term depend on the view direction?

### 08.5 Shading

Core sentence: this section explains one part of local illumination.

Main connection: The shading method decides what is computed at vertices and what is computed at fragments.

Slower English:

Shading decides where the illumination calculation is evaluated and how results are interpolated. Flat shading uses one value per primitive. Gouraud shading evaluates at vertices and interpolates colors. Phong shading interpolates normals and evaluates lighting per fragment.

Per fragment shading is more expensive but can represent highlights more accurately. This connects directly to the pipeline, interpolation during rasterization provides the data used by the fragment shader.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why can Gouraud shading miss a small specular highlight?

## 6. Reading The Main Chapter After This

The most dangerous misunderstanding in this lecture is: Do not mix up normal, light direction, and view direction; each changes a different lighting term.

The compact rule is: color = ambient + diffuse + specular

# Lecture 09 - Texturing B1 Bridge

## 1. Starting Point

This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called Texturing works in a rendering system?

## 2. Everyday Bridge

You already know that an image can be placed on a surface, like a label on a bottle. Texturing is the graphics version, but it is more general than a simple sticker.

The main idea in easier English is this: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.

A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.

For this lecture, the process is:

1. fragment coordinates. This is the start.

2. texture coordinates. This comes after the previous step.

3. sampler/filter/wrap state. This comes after the previous step.

4. texel fetch. This comes after the previous step.

5. shader meaning. This comes after the previous step.

## 3. English Bridge

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

Pattern: subject, verb, object, result.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: fragment coordinates, then texture coordinates, then sampler/filter/wrap state, then texel fetch, then shader meaning.

Pattern: input, conversion, output.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

Pattern: source space, mapping rule, target space.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

Pattern: object, test, true or false result.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

Pattern: candidate, test rule, accepted or rejected result.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: fragment coordinates, then texture coordinates, then sampler/filter/wrap state, then texel fetch, then shader meaning.

Pattern: later step, required earlier step.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

Pattern: storage object, stored value, later access.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

Pattern: current state, draw command, GPU result.

## 4. Terminology Bridge

The important words are not random vocabulary. Each word has a job in the rendering story.

### texture

Simple meaning: Sampled data array used for color, normals, material data, depth, or other shader inputs.

Why it is here: this word helps explain texturing. It connects to this process: `fragment coordinates, then texture coordinates, then sampler/filter/wrap state, then texel fetch, then shader meaning`.

Good sentence pattern: `texture` is used when the system needs to describe, change, test, store, or use this kind of information.

### texel

Simple meaning: A stored sample in texture memory.

Why it is here: this word helps explain texturing. It connects to this process: `fragment coordinates, then texture coordinates, then sampler/filter/wrap state, then texel fetch, then shader meaning`.

Good sentence pattern: `texel` is used when the system needs to describe, change, test, store, or use this kind of information.

### UV coordinates

Simple meaning: Coordinates that map surface locations to texture space.

Why it is here: this word helps explain texturing. It connects to this process: `fragment coordinates, then texture coordinates, then sampler/filter/wrap state, then texel fetch, then shader meaning`.

Good sentence pattern: `UV coordinates` is used when the system needs to describe, change, test, store, or use this kind of information.

### filtering

Simple meaning: Rule for reconstructing values between texels, such as nearest or linear filtering.

Why it is here: this word helps explain texturing. It connects to this process: `fragment coordinates, then texture coordinates, then sampler/filter/wrap state, then texel fetch, then shader meaning`.

Good sentence pattern: `filtering` is used when the system needs to describe, change, test, store, or use this kind of information.

### mipmap

Simple meaning: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.

Why it is here: this word helps explain texturing. It connects to this process: `fragment coordinates, then texture coordinates, then sampler/filter/wrap state, then texel fetch, then shader meaning`.

Good sentence pattern: `mipmap` is used when the system needs to describe, change, test, store, or use this kind of information.

### environment mapping

Simple meaning: Using texture lookup to approximate surrounding reflections or distant lighting.

Why it is here: this word helps explain texturing. It connects to this process: `fragment coordinates, then texture coordinates, then sampler/filter/wrap state, then texel fetch, then shader meaning`.

Good sentence pattern: `environment mapping` is used when the system needs to describe, change, test, store, or use this kind of information.

## 5. Step By Step Bridge

### 09.1 Texture Objects, Texels, Formats, and Color Space

Core sentence: this section explains one part of texturing.

Main connection: A texture is a GPU-accessible sampled data field.

Slower English:

A texture object stores sampled data on the GPU. A texel is one stored texture sample. The texture format decides what channels and numeric representation the samples use. Color space matters because color values may be stored nonlinearly, especially for sRGB images.

The key shift is to stop thinking of texture as only a picture. Textures can store color, normals, depth, lookup data, environment information, or volume data. The shader decides how the sampled values are interpreted.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why can the same texture mechanism store both color maps and normal maps?

### 09.2 Texture Coordinates, UV Mapping, and Wrapping

Core sentence: this section explains one part of texturing.

Main connection: UVs are the address system that lets a fragment look up texture data.

Slower English:

Texture coordinates map surface points to locations in texture space. UV coordinates are usually interpolated across primitives during rasterization and then used by the fragment shader to sample a texture.

Wrapping rules decide what happens outside the normal coordinate range. Repeat, clamp, mirrored repeat, and border behavior are not visual afterthoughts, they define the sampling function outside the base domain.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What artifact might appear if a wrapping mode is wrong at the edge of a surface?

### 09.3 Sampling, Filtering, Mipmaps, and Anisotropy

Core sentence: this section explains one part of texturing.

Main connection: Filtering reconstructs values; mipmaps choose an appropriate scale before reconstruction.

Slower English:

Sampling turns continuous texture coordinates into values from discrete texels. Nearest filtering selects a nearby texel and can look blocky. Linear filtering blends nearby texels and looks smoother. Minification is harder because many texels may map to one pixel.

Mipmaps store prefiltered lower resolution versions of a texture. They reduce aliasing and shimmer when textures are seen at small scale. Anisotropic filtering improves quality when a texture is viewed at a steep angle where footprint shape is elongated.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why does a distant checkerboard shimmer without mipmapping?

### 09.4 Modern OpenGL Texture Pipeline

Core sentence: this section explains one part of texturing.

Main connection: OpenGL texturing is a chain: object data -> texture unit -> sampler uniform -> shader lookup.

Slower English:

In modern OpenGL, textures are represented by texture objects, bound to texture units, connected to sampler uniforms, and accessed in shaders. The shader does not sample a filename, it samples a bound texture through a sampler.

Texture bugs often come from state mismatches, wrong active texture unit, wrong sampler uniform, missing mipmaps for a mipmap filter, wrong wrap mode, or wrong internal format.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why can a texture appear black when the shader code is mathematically correct?

### 09.5 Normal Mapping

Core sentence: this section explains one part of texturing.

Main connection: Normal mapping changes the lighting normal, not the actual mesh silhouette.

Slower English:

Normal mapping stores normal directions in a texture so that lighting can vary at a finer scale than the geometry. The surface may have few triangles, but the shader receives detailed normals per fragment.

The hard part is coordinate space. Normal maps are often defined in tangent space, so the shader must transform or interpret them with the correct tangent, bitangent, and normal basis.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why does normal mapping not change the geometric outline of an object?

### 09.6 Environment Mapping and 3D Textures

Core sentence: this section explains one part of texturing.

Main connection: Textures are general sampled data; the coordinate dimensionality depends on the problem.

Slower English:

Environment mapping uses textures to represent surrounding illumination or reflections. A direction, not a surface UV alone, can be used to sample an environment map. This is a texture lookup driven by view or reflection geometry.

D textures and volume rendering extend the same sampled data idea into three dimensions. Instead of sampling a D image, the shader samples a volume. This is useful for data such as medical scans, density fields, or procedural volumetric effects.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What coordinate type would you use to sample a 3D texture?

## 6. Reading The Main Chapter After This

The most dangerous misunderstanding in this lecture is: Do not reduce texturing to pasting an image onto geometry.

The compact rule is: sampled value = texture(sampler, uv), then shader interprets the value

# Lecture 10 - Shadows B1 Bridge

## 1. Starting Point

This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called Shadows works in a rendering system?

## 2. Everyday Bridge

You already know that a shadow appears when something blocks light. The important course idea is that this is a visibility question from the light, not only from the camera.

The main idea in easier English is this: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.

A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.

For this lecture, the process is:

1. light. This is the start.

2. possible blocker. This comes after the previous step.

3. receiver point. This comes after the previous step.

4. light-space visibility test. This comes after the previous step.

5. lit or shadowed result. This comes after the previous step.

## 3. English Bridge

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

Pattern: subject, verb, object, result.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: light, then possible blocker, then receiver point, then light-space visibility test, then lit or shadowed result.

Pattern: input, conversion, output.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

Pattern: source space, mapping rule, target space.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

Pattern: object, test, true or false result.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

Pattern: candidate, test rule, accepted or rejected result.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: light, then possible blocker, then receiver point, then light-space visibility test, then lit or shadowed result.

Pattern: later step, required earlier step.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

Pattern: storage object, stored value, later access.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

Pattern: current state, draw command, GPU result.

## 4. Terminology Bridge

The important words are not random vocabulary. Each word has a job in the rendering story.

### shadow

Simple meaning: Reduced direct illumination where an object blocks light from reaching a receiver.

Why it is here: this word helps explain shadows. It connects to this process: `light, then possible blocker, then receiver point, then light-space visibility test, then lit or shadowed result`.

Good sentence pattern: `shadow` is used when the system needs to describe, change, test, store, or use this kind of information.

### occluder

Simple meaning: Object that blocks light.

Why it is here: this word helps explain shadows. It connects to this process: `light, then possible blocker, then receiver point, then light-space visibility test, then lit or shadowed result`.

Good sentence pattern: `occluder` is used when the system needs to describe, change, test, store, or use this kind of information.

### receiver

Simple meaning: Surface where the shadow appears.

Why it is here: this word helps explain shadows. It connects to this process: `light, then possible blocker, then receiver point, then light-space visibility test, then lit or shadowed result`.

Good sentence pattern: `receiver` is used when the system needs to describe, change, test, store, or use this kind of information.

### shadow map

Simple meaning: Depth image rendered from the light's point of view for later visibility comparison.

Why it is here: this word helps explain shadows. It connects to this process: `light, then possible blocker, then receiver point, then light-space visibility test, then lit or shadowed result`.

Good sentence pattern: `shadow map` is used when the system needs to describe, change, test, store, or use this kind of information.

### shadow volume

Simple meaning: Volume of space hidden from a light by an occluder.

Why it is here: this word helps explain shadows. It connects to this process: `light, then possible blocker, then receiver point, then light-space visibility test, then lit or shadowed result`.

Good sentence pattern: `shadow volume` is used when the system needs to describe, change, test, store, or use this kind of information.

### projective shadow

Simple meaning: Shadow construction based on projecting geometry onto a receiver.

Why it is here: this word helps explain shadows. It connects to this process: `light, then possible blocker, then receiver point, then light-space visibility test, then lit or shadowed result`.

Good sentence pattern: `projective shadow` is used when the system needs to describe, change, test, store, or use this kind of information.

## 5. Step By Step Bridge

### 10.1 Definitions

Core sentence: this section explains one part of shadows.

Main connection: Shadows are light-space visibility made visible in the camera image.

Slower English:

A shadow is not simply a dark texture. It is evidence that light visibility is blocked. Important distinctions include hard versus soft shadows, umbra versus penumbra, and geometric versus precomputed approaches.

For real time graphics, shadows are usually approximated. The approximation must answer a visibility question cheaply enough for interactive rendering.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why is shadow computation related to visibility determination?

### 10.2 Ground Plane Shadows

Core sentence: this section explains one part of shadows.

Main connection: A planar shadow is projected geometry on a known receiver.

Slower English:

Ground plane shadows project an object onto a receiving plane. This is simple and can look convincing in restricted scenes, but it assumes a known planar receiver and does not handle general shadowing between arbitrary objects.

The method is useful pedagogically because it makes the geometric nature of shadows explicit, a light source, an occluder, and a receiver define where the shadow lands.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What scene limitation makes ground plane shadows less general than shadow maps?

### 10.3 Light Maps

Core sentence: this section explains one part of shadows.

Main connection: A light map spends storage and preprocessing to save runtime shading work.

Slower English:

Light maps store precomputed lighting or shadow information in textures. They can be efficient at runtime, but they are limited when lights, objects, or geometry move dynamically.

This is another example of a recurring graphics tradeoff, precompute for speed, but lose flexibility. Real time rendering often mixes precomputed and dynamic techniques.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why are light maps less suitable for fully dynamic moving lights?

### 10.4 Shadow Volumes

Core sentence: this section explains one part of shadows.

Main connection: A shadow volume is the 3D region where the light cannot reach.

Slower English:

Shadow volumes construct the volume of space blocked from a light by an occluder. The camera view can then determine whether visible points lie inside that volume. Stencil buffer techniques are often associated with this method.

The strength is geometric precision for hard shadows. The cost is handling silhouette edges, volume construction, and robust stencil operations. It is a good contrast to shadow maps, which are image based from the light view.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: Why are silhouette edges important for constructing shadow volumes?

### 10.5 Shadow Maps

Core sentence: this section explains one part of shadows.

Main connection: Shadow maps reuse the depth-buffer idea, but from the light's camera.

Slower English:

Shadow mapping renders the scene from the lights point of view and stores depth. During the camera pass, a surface point is transformed into light space and compared against the stored depth. If it is farther than what the light saw, it is in shadow.

This method is practical and widely used, but it has artifacts. Shadow acne comes from precision or self comparison issues. Bias can reduce acne but too much bias causes detached shadows. Resolution, filtering, and light projection strongly affect quality.

Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.

Check: What exactly is stored in a shadow map?

## 6. Reading The Main Chapter After This

The most dangerous misunderstanding in this lecture is: Do not explain a shadow only from the camera view; the key test is light-space visibility.

The compact rule is: point is shadowed if something is closer to the light along the same light ray
