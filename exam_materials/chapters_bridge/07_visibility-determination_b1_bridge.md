# Lecture 07 - Visibility Determination B1 Bridge

Read this before the normal exam chapter if the English feels too dense. This version does not replace the main chapter. It prepares you for it.

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

When you read the main chapter, do not try to memorize the whole sentence first. Ask three smaller questions. What goes in? What changes? What comes out?

## 3. English Bridge

These phrases appear often in computer graphics texts. Learn them as small sentence patterns.

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

How to read it: if you see `to represent something`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: many projected or intersected candidates, then comparison rule, then visible surface or fragment, then final image contribution.

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

Course example: The later part of the chapter depends on the earlier part of this chain: many projected or intersected candidates, then comparison rule, then visible surface or fragment, then final image contribution.

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

Each part below connects a lecture section to easier English. Read the easy sentence first. Then read the explanation. Then read the same part in the normal chapter.

### 07.1 Object-Based Algorithms

Easy sentence: this section explains one part of visibility determination.

Main connection: Object-based visibility tries to solve visibility with geometry before final pixels are written.

What this means in slower English:

Object based visibility algorithms reason about geometry before or while comparing surfaces. They can sort, split, or reject objects based on spatial relations. This is different from simply letting every fragment fight in the depth buffer.

The value of object based reasoning is reducing work or establishing correct order. The difficulty is that geometry can overlap in complicated ways, so simple global ordering is not always possible.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why can intersecting polygons make simple depth sorting fail?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 07.2 Binary Space Partitioning

Easy sentence: this section explains one part of visibility determination.

Main connection: A BSP tree stores a recursive answer to 'which side of this plane is the geometry on?'

What this means in slower English:

A BSP tree recursively divides space with planes. Once built, it can help traverse geometry in a view dependent order. This is useful for visibility and ordering because the tree encodes spatial relationships.

The cost is preprocessing and possible splitting of geometry. BSP is a good example of trading memory and setup work for faster or more structured visibility decisions later.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why can building a BSP tree require splitting polygons?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 07.3 Warnock Algorithm

Easy sentence: this section explains one part of visibility determination.

Main connection: When a region is too complicated, subdivide until the answer becomes simple.

What this means in slower English:

Warnocks algorithm works in image space by subdividing regions until visibility is simple enough to decide. If a region is ambiguous, split it. If it is simple, fill it.

This illustrates a general graphics strategy, recursively reduce a hard global problem into smaller local problems. The algorithm is less central in modern OpenGL practice than the depth buffer, but it helps contrast image space and object space approaches.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: What makes Warnock's algorithm image-space rather than object-space?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 07.4 Depth Buffer Algorithm

Easy sentence: this section explains one part of visibility determination.

Main connection: The depth buffer is a per-sample competition for closest visible fragment.

What this means in slower English:

The depth buffer stores the closest accepted depth at each sample or pixel. For each fragment, compare its depth to the stored depth. If it passes, update the color and depth, otherwise discard it.

The strength of the depth buffer is simplicity and hardware efficiency. The weakness is precision, depth values are finite, and projection distributes precision unevenly. Bad near or far settings can create z fighting.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why should the near plane not be unnecessarily close to the camera?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 07.5 Depth Extensions and Ray Casting

Easy sentence: this section explains one part of visibility determination.

Main connection: Rasterization pushes primitives to pixels; ray casting pulls visibility from pixels into the scene.

What this means in slower English:

Depth buffer extensions refine or adapt depth based visibility, for example by handling precision, transparency, or multiple layers more carefully. Standard depth testing alone is not a complete solution for every visibility situation.

Ray casting takes the opposite direction from rasterization, for each image sample, cast a ray into the scene and find the closest intersection. This naturally solves primary visibility but requires intersection work instead of raster coverage work.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why is transparency harder than opaque nearest-surface visibility?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

## 6. Reading The Main Chapter After This

Now read the normal chapter for this lecture. When a sentence feels hard, do not translate every word first. First mark the verb. Then mark the technical noun. Then ask how the noun moves through the process.

The most dangerous misunderstanding in this lecture is: Do not confuse generating a fragment with proving that it is visible.

The compact rule is: visible fragment = candidate with passing depth/visibility test at the sample

You are ready for the main version when you can explain the process with simple English, recognize the important course words, and understand the verbs that connect the words.
