# Lecture 04 - Geometric Projection B1 Bridge

Read this before the normal exam chapter if the English feels too dense. This version does not replace the main chapter. It prepares you for it.

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

When you read the main chapter, do not try to memorize the whole sentence first. Ask three smaller questions. What goes in? What changes? What comes out?

## 3. English Bridge

These phrases appear often in computer graphics texts. Learn them as small sentence patterns.

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

How to read it: if you see `to represent something`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: view-space position, then projection matrix, then clip coordinates, then perspective divide, then NDC, then viewport coordinates.

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

Course example: The later part of the chapter depends on the earlier part of this chain: view-space position, then projection matrix, then clip coordinates, then perspective divide, then NDC, then viewport coordinates.

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

Each part below connects a lecture section to easier English. Read the easy sentence first. Then read the explanation. Then read the same part in the normal chapter.

### 04.1 Linear Perspective and Planar Projections

Easy sentence: this section explains one part of geometric projection.

Main connection: Projection is the rule that turns 3D positions into image-plane positions.

What this means in slower English:

Perspective projection models the visual effect that farther objects appear smaller. Orthographic projection removes this distance based size change and keeps parallel lines parallel. Both are useful, but they communicate different spatial relationships.

Planar projection means mapping points onto an image plane. The lectures art examples are not decoration, they show that projection is a geometric rule for constructing an image from a viewpoint.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: What visual cue does perspective projection add that orthographic projection lacks?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 04.2 Camera Modeling

Easy sentence: this section explains one part of geometric projection.

Main connection: A camera is not only an eye position; it is also a volume and a mapping rule.

What this means in slower English:

A virtual camera is defined by position, orientation, projection type, viewing volume, and image or viewport settings. The view transform places the world relative to the camera. The projection transform maps that view into clip coordinates.

Near and far clipping planes are part of the camera model. They decide what range of depths is represented and strongly affect depth buffer precision. A careless near or far setup can create z fighting even if the scene geometry is correct.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why can changing the near plane affect depth artifacts?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 04.3 Specifying Projections in OpenGL

Easy sentence: this section explains one part of geometric projection.

Main connection: The projection matrix is the camera lens encoded as linear algebra in homogeneous coordinates.

What this means in slower English:

In OpenGL, projection is usually encoded in a projection matrix sent to a shader. The matrix maps view space coordinates to clip space. Clipping and the perspective divide then lead toward normalized device coordinates.

Aspect ratio and field of view must match the intended viewport. If the aspect ratio is wrong, objects appear stretched. If the field of view is extreme, the image can look distorted even though the math is functioning.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: What symptom suggests that the projection aspect ratio does not match the window?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 04.4 Orthographic and Perspective Derivations

Easy sentence: this section explains one part of geometric projection.

Main connection: Projection matrices normalize a viewing volume; perspective also prepares the divide by w.

What this means in slower English:

The derivations are there to explain where the matrix entries come from. Orthographic projection maps a box shaped view volume into normalized coordinates. Perspective projection maps a frustum and uses the homogeneous component for the later divide.

You do not need to treat these matrices as random formulas. Each part maps a coordinate range into a standard range. The perspective matrix additionally arranges w so that the perspective divide creates foreshortening.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: What does the perspective divide do to x and y coordinates?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 04.5 Viewport Transformation

Easy sentence: this section explains one part of geometric projection.

Main connection: Projection decides normalized position; viewport decides where that position lands on the screen.

What this means in slower English:

After normalized device coordinates, the viewport transform maps the normalized range to actual window coordinates. This is the last geometric mapping before rasterization uses the target grid.

Separating projection from viewport mapping helps debugging. A wrong projection can produce wrong normalized coordinates, a wrong viewport can map otherwise valid coordinates into the wrong part of the window.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why is resizing a window related to both viewport and projection settings?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

## 6. Reading The Main Chapter After This

Now read the normal chapter for this lecture. When a sentence feels hard, do not translate every word first. First mark the verb. Then mark the technical noun. Then ask how the noun moves through the process.

The most dangerous misunderstanding in this lecture is: Do not confuse projection with viewport mapping; the perspective divide sits between them.

The compact rule is: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w

You are ready for the main version when you can explain the process with simple English, recognize the important course words, and understand the verbs that connect the words.
