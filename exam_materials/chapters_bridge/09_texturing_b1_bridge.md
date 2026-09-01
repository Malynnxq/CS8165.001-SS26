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
