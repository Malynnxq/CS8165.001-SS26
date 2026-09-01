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
