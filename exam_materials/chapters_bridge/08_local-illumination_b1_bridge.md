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
