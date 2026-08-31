# Lecture 06 - Rasterization B1 Bridge

Read this before the normal exam chapter if the English feels too dense. This version does not replace the main chapter. It prepares you for it.

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

When you read the main chapter, do not try to memorize the whole sentence first. Ask three smaller questions. What goes in? What changes? What comes out?

## 3. English Bridge

These phrases appear often in computer graphics texts. Learn them as small sentence patterns.

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

How to read it: if you see `to represent something`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: projected primitive, then sample coverage, then fragment generation, then attribute interpolation, then fragment tests.

How to read it: if you see `to convert A into B`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

How to read it: if you see `to map A to B`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

How to read it: if you see `to determine whether`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

How to read it: if you see `to pass a test`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: projected primitive, then sample coverage, then fragment generation, then attribute interpolation, then fragment tests.

How to read it: if you see `to depend on`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

How to read it: if you see `to store a value`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

How to read it: if you see `at draw time`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

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

Each part below connects a lecture section to easier English. Read the easy sentence first. Then read the explanation. Then read the same part in the normal chapter.

### 06.1 Line Rasterization

Easy sentence: this section explains one part of rasterization.

Main connection: Rasterizing a line means approximating a continuous path by grid decisions.

What this means in slower English:

A mathematical line has infinitely many points, but a raster display has a finite grid. Line rasterization decides which grid cells or samples best approximate the ideal line. The algorithm must balance accuracy, speed, and consistency.

Incremental algorithms avoid recomputing expensive formulas for every pixel. The important idea is to step along one axis and update an error term that decides when to step along the other axis.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why are incremental error updates useful in line rasterization?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 06.2 Triangle Edge Rasterization

Easy sentence: this section explains one part of rasterization.

Main connection: Triangle rasterization answers the question: which samples are inside this projected triangle?

What this means in slower English:

Triangles are the core primitive in real time rendering. Edge functions or half space tests decide whether a sample lies inside the triangle. This allows the rasterizer to test coverage systematically.

Coverage is not final visibility. A covered sample becomes a fragment candidate. Depth testing, stencil testing, blending, and other operations still decide whether the framebuffer changes.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: What later stage can reject a fragment after triangle coverage succeeds?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 06.3 Region Filling

Easy sentence: this section explains one part of rasterization.

Main connection: Filling is about turning boundary descriptions into consistent interior samples.

What this means in slower English:

Region filling generalizes the idea of determining interior samples. The algorithm must identify connected areas or spans that should receive color. This connects rasterization to scan conversion and image space reasoning.

The practical issue is avoiding gaps, double fills, or inconsistent boundary handling. Small choices at edges can become visible artifacts when many primitives meet.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why can inconsistent edge rules create cracks between adjacent primitives?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 06.4 Scanline-Based Triangle Rasterization

Easy sentence: this section explains one part of rasterization.

Main connection: Each scanline asks: where does this triangle enter and leave this row?

What this means in slower English:

Scanline rasterization processes horizontal rows of the image. For each row that crosses a triangle, the algorithm finds the covered interval and fills the span. Attribute interpolation can be updated along edges and across each span.

The method is intuitive because it follows the memory layout of many images. It also demonstrates why interpolation is tied to rasterization, once you know a sample location inside the primitive, you can interpolate depth, color, normals, or texture coordinates.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Which attributes might be interpolated while filling triangle spans?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 06.5 Tile-Based Triangle Rasterization

Easy sentence: this section explains one part of rasterization.

Main connection: Block-based rasterization keeps the same coverage problem but changes the work organization.

What this means in slower English:

Tile or block based approaches group pixels into small regions. This can improve locality and parallel work distribution. Modern GPUs often reason in blocks or tiles internally because rendering is massively parallel.

For the exam, connect this to efficiency. The mathematical goal is still coverage, but the implementation is organized to use hardware resources well.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why is block organization attractive for parallel graphics hardware?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

## 6. Reading The Main Chapter After This

Now read the normal chapter for this lecture. When a sentence feels hard, do not translate every word first. First mark the verb. Then mark the technical noun. Then ask how the noun moves through the process.

The most dangerous misunderstanding in this lecture is: Do not call every generated fragment a final pixel.

The compact rule is: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1

You are ready for the main version when you can explain the process with simple English, recognize the important course words, and understand the verbs that connect the words.
