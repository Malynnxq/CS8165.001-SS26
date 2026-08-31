# Lecture 03 - Geometric Transformations B1 Bridge

Read this before the normal exam chapter if the English feels too dense. This version does not replace the main chapter. It prepares you for it.

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

When you read the main chapter, do not try to memorize the whole sentence first. Ask three smaller questions. What goes in? What changes? What comes out?

## 3. English Bridge

These phrases appear often in computer graphics texts. Learn them as small sentence patterns.

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

How to read it: if you see `to represent something`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: object/model coordinates, then model matrix, then world coordinates, then view matrix, then camera/view coordinates.

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

Course example: The later part of the chapter depends on the earlier part of this chain: object/model coordinates, then model matrix, then world coordinates, then view matrix, then camera/view coordinates.

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

Each part below connects a lecture section to easier English. Read the easy sentence first. Then read the explanation. Then read the same part in the normal chapter.

### 03.1 Mathematical Foundations

Easy sentence: this section explains one part of geometric transformations.

Main connection: A numeric vector is incomplete until you know what coordinate system it belongs to.

What this means in slower English:

The lecture uses vectors and matrices to express geometric operations. A vector can represent a point position, a direction, an offset, or an attribute depending on context. A matrix expresses a linear map or, with homogeneous coordinates, an affine transformation.

The central exam habit is to name the coordinate space. A point in model coordinates and a light direction in view coordinates cannot be mixed safely. Many visual bugs are coordinate space bugs.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why is a normal vector not transformed exactly like a point under all transformations?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 03.2 Affine Transformations

Easy sentence: this section explains one part of geometric transformations.

Main connection: Use 4D homogeneous coordinates so that a single matrix pipeline can move 3D points through the scene.

What this means in slower English:

Affine transformations include translation, rotation, scaling, shearing, and combinations of these. Homogeneous coordinates allow translation to be represented in matrix form together with other transformations.

Translation moves positions but not pure directions. Rotation changes orientation while preserving lengths if it is a proper rotation. Scaling can change lengths and can also affect normals. These distinctions matter later in lighting.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: What does the homogeneous w component let a transformation matrix express?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 03.3 Composition of Transformations

Easy sentence: this section explains one part of geometric transformations.

Main connection: Matrix chains are compressed stories of movement through coordinate spaces.

What this means in slower English:

Composition means applying several transformations in sequence. The order matters because matrix multiplication is generally not commutative. Rotating an object around its own origin and then translating it is different from translating it and then rotating around the world origin.

When you read a formula such as projection times view times model times position, read it from right to left for the point, first model, then view, then projection. The resulting matrix chain is compact, but the conceptual steps remain separate.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why can swapping model and view matrices destroy the intended camera/object relation?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 03.4 Coordinate System Change

Easy sentence: this section explains one part of geometric transformations.

Main connection: Moving the camera one way is equivalent to moving the world the opposite way for rendering.

What this means in slower English:

A transformation can be read actively as moving an object, or passively as changing the coordinate frame used to describe it. Both interpretations are valid, but mixing them carelessly causes sign and order errors.

The view matrix is a classic example, conceptually you position a camera, but the pipeline usually transforms the world by the inverse of the camera transform so that the camera becomes the origin of view space.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why is the view transform often related to the inverse camera transform?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 03.5 Transformations in OpenGL

Easy sentence: this section explains one part of geometric transformations.

Main connection: The shader is the place where abstract transformation math becomes GPU execution.

What this means in slower English:

Modern OpenGL does not automatically manage the old matrix stacks. You usually compute model, view, and projection matrices in application code and pass them to shaders as uniforms.

The vertex shader is where the final clip space position is normally computed. That means a wrong matrix uniform, wrong multiplication order, or wrong convention can make geometry vanish even though buffers and draw calls are correct.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Which matrix would you inspect first if an object follows the camera instead of staying in the world?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

## 6. Reading The Main Chapter After This

Now read the normal chapter for this lecture. When a sentence feels hard, do not translate every word first. First mark the verb. Then mark the technical noun. Then ask how the noun moves through the process.

The most dangerous misunderstanding in this lecture is: Do not multiply matrices without naming source space, target space, and order.

The compact rule is: p_world = M_model * p_model; p_view = V * p_world

You are ready for the main version when you can explain the process with simple English, recognize the important course words, and understand the verbs that connect the words.
