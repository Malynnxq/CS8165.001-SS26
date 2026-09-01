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
