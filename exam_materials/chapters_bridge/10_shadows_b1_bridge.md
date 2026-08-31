# Lecture 10 - Shadows B1 Bridge

Read this before the normal exam chapter if the English feels too dense. This version does not replace the main chapter. It prepares you for it.

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

When you read the main chapter, do not try to memorize the whole sentence first. Ask three smaller questions. What goes in? What changes? What comes out?

## 3. English Bridge

These phrases appear often in computer graphics texts. Learn them as small sentence patterns.

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

How to read it: if you see `to represent something`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: light, then possible blocker, then receiver point, then light-space visibility test, then lit or shadowed result.

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

Course example: The later part of the chapter depends on the earlier part of this chain: light, then possible blocker, then receiver point, then light-space visibility test, then lit or shadowed result.

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

Each part below connects a lecture section to easier English. Read the easy sentence first. Then read the explanation. Then read the same part in the normal chapter.

### 10.1 Definitions

Easy sentence: this section explains one part of shadows.

Main connection: Shadows are light-space visibility made visible in the camera image.

What this means in slower English:

A shadow is not simply a dark texture. It is evidence that light visibility is blocked. Important distinctions include hard versus soft shadows, umbra versus penumbra, and geometric versus precomputed approaches.

For real time graphics, shadows are usually approximated. The approximation must answer a visibility question cheaply enough for interactive rendering.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why is shadow computation related to visibility determination?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 10.2 Ground Plane Shadows

Easy sentence: this section explains one part of shadows.

Main connection: A planar shadow is projected geometry on a known receiver.

What this means in slower English:

Ground plane shadows project an object onto a receiving plane. This is simple and can look convincing in restricted scenes, but it assumes a known planar receiver and does not handle general shadowing between arbitrary objects.

The method is useful pedagogically because it makes the geometric nature of shadows explicit, a light source, an occluder, and a receiver define where the shadow lands.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: What scene limitation makes ground plane shadows less general than shadow maps?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 10.3 Light Maps

Easy sentence: this section explains one part of shadows.

Main connection: A light map spends storage and preprocessing to save runtime shading work.

What this means in slower English:

Light maps store precomputed lighting or shadow information in textures. They can be efficient at runtime, but they are limited when lights, objects, or geometry move dynamically.

This is another example of a recurring graphics tradeoff, precompute for speed, but lose flexibility. Real time rendering often mixes precomputed and dynamic techniques.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why are light maps less suitable for fully dynamic moving lights?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 10.4 Shadow Volumes

Easy sentence: this section explains one part of shadows.

Main connection: A shadow volume is the 3D region where the light cannot reach.

What this means in slower English:

Shadow volumes construct the volume of space blocked from a light by an occluder. The camera view can then determine whether visible points lie inside that volume. Stencil buffer techniques are often associated with this method.

The strength is geometric precision for hard shadows. The cost is handling silhouette edges, volume construction, and robust stencil operations. It is a good contrast to shadow maps, which are image based from the light view.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why are silhouette edges important for constructing shadow volumes?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 10.5 Shadow Maps

Easy sentence: this section explains one part of shadows.

Main connection: Shadow maps reuse the depth-buffer idea, but from the light's camera.

What this means in slower English:

Shadow mapping renders the scene from the lights point of view and stores depth. During the camera pass, a surface point is transformed into light space and compared against the stored depth. If it is farther than what the light saw, it is in shadow.

This method is practical and widely used, but it has artifacts. Shadow acne comes from precision or self comparison issues. Bias can reduce acne but too much bias causes detached shadows. Resolution, filtering, and light projection strongly affect quality.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: What exactly is stored in a shadow map?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

## 6. Reading The Main Chapter After This

Now read the normal chapter for this lecture. When a sentence feels hard, do not translate every word first. First mark the verb. Then mark the technical noun. Then ask how the noun moves through the process.

The most dangerous misunderstanding in this lecture is: Do not explain a shadow only from the camera view; the key test is light-space visibility.

The compact rule is: point is shadowed if something is closer to the light along the same light ray

You are ready for the main version when you can explain the process with simple English, recognize the important course words, and understand the verbs that connect the words.
