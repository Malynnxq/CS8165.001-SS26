# Lecture 09 - Texturing

Source chunk: `course_text_parts/03_lectures/09_texturing.txt`
Extracted slide pages in source chunk: 133

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture treats textures as sampled data for shading, not merely images glued onto objects. It connects UV coordinates, sampling, filtering, mipmaps, OpenGL texture state, and advanced texture uses.

## How To Read This Lecture

- First read the big picture and the mental models.
- Then open the source chunk and compare the slide bullets to the commentary.
- After each section, answer the check question without notes.
- If the check feels vague, revisit the source pages listed for that section.

## Slide Walkthrough

This section adds a short reading comment for every extracted slide page. Use it when the original PDF page is too terse.

- Page 1: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 2: **Textures: Sampled Data for Shading**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 3: **Texturing Example**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 4: **Texture Mapping**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 5: **Why Textures Matter**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 6: **Textures Are More Than Color Images**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 7: **Texturing Demo**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 8: **Overview**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 9: **9.1 Texture Objects, Texels, Formats, and Color Space**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 10: **From Image File to GPU Texture Object**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 11: **Texels, Channels, and Meaning**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 12: **Texture Targets and Dimensionality**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 13: **Internal Texture Formats**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 14: **Numeric Texture Representations**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 15: **Color Textures vs. Data Textures**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 16: **2D Texture Access**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 17: **Bilinear Interpolation**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 18: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 19: **Texture Memory Footprint**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 20: **Texture Compression and Asset Pipelines**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 21: **Steps Involved in Texturing**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 22: **9.2 Texture Coordinates, UV Mapping, and Wrapping**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 23: **Texture Coordinate System 1/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 24: **Texture Coordinate System 2/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 25: **Texture Coordinate Specification**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 26: **Disc Parametrization**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 27: **Cylinder Parametrization**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 28: **Two-Part Mapping 1/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 29: **Two-Part Mapping 2/2**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 30: **Two-Part Mapping Example**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 31: **Projection Calculation Variations**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 32: **Texture Coordinate Transformation**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 33: **Demo - Texture Coordinate Transformation**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 34: **Height Field Texturing Example**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 35: **9.3 Sampling, Filtering, Mipmaps, and Anisotropy**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 36: **Forward vs. Inverse Mapping**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 37: **Forward Mapping**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 38: **Inverse Mapping 1/2**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 39: **Inverse Mapping 2/2**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 40: **Magnification vs. Minification**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 41: **Nearest vs. Linear Interpolation**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 42: **Minification Filtering Requirements**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 43: **Demo - Magnification Filtering: Nearest vs Linear**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 44: **MIP Mapping (multum in parvo = ‘much in little’)**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 45: **MIP Map Pyramid 1/2**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 46: **MIP Map Pyramid 2/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 47: **MIP Mapping Memory**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 48: **MIP Mapping Procedure**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 49: **LoD Calculation 1/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 50: **LoD Calculation 2/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 51: **Demo - Minification, Mipmaps, and Mipmap Level Visualization**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 52: **Anisotropic Filtering**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 53: **Demo - Anisotropic Filtering**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 54: **9.4 Modern OpenGL Texture Pipeline**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 55: **OpenGL Texturing**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 56: **OpenGL Minification & Magnification 1/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 57: **OpenGL Minification & Magnification 2/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 58: **OpenGL Minification & Magnification 3/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 59: **Demo - Texture Units and Sampler Uniforms**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 60: **Texture Wrapping 1/4**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 61: **Texture Wrapping 2/4**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 62: **Texture Wrapping 3/4**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 63: **Texture Wrapping 4/4**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 64: **Texel Value Usage**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 65: **Texturing in GLSL Shaders 1/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 66: **Texturing in GLSL Shaders 2/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 67: **Texturing in GLSL Shaders 3/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 68: **9.5 Normal Mapping**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 69: **Motivation**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 70: **Mesh Compression**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 71: **Normal Mapping 1/2**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 72: **Normal Mapping 2/2**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 73: **Normal Maps**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 74: **Tangent Space**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 75: **TBN Matrix**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 76: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 77: **Tangent Vector Derivation 1/2**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 78: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 79: **Tangent Vector Derivation 2/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 80: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 81: **Observations**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 82: **Variations**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 83: **9.6 Environment Mapping**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 84: **Environment Mapping Motivation**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 85: **Environment Mapping Process**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 86: **Environment Mapping Assumptions**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 87: **Environment Mapping 2/2**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 88: **Demo - Cube-map Reflection Vector**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 89: **Environment Mapping Types 1/2**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 90: **Environment Mapping Types 2/2**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 91: **Spherical Mapping 1/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 92: **Spherical Mapping 2/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 93: **Spherical Environment Mapping**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 94: **Sphere Map Distortion**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 95: **Demo - Environment Map Distortion**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 96: **Sphere Map Interpolation**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 97: **Sphere Map Coordinates**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 98: **Cube Environment Mapping**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 99: **Cube Mapping Example 1/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 100: **Cube Mapping Example 2/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 101: **Cube Mapping Distortion**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 102: **Cube Map Texture Coordinates**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 103: **Environment Mapping in OpenGL**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 104: **Cube Map Texture Object**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 105: **Sampling Direction**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 106: **Environment Mapping in GLSL 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 107: **Environment Mapping in GLSL 2/2**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 108: **Practical Cube-Map Issues**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 109: **1 glEnable(GL_TEXTURE_CUBE_MAP_SEAMLESS);**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 110: **Cube Mapping Pros and Cons**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 111: **Spherical Environment Mapping Assumptions**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 112: **Spherical Environment Mapping Conclusions**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 113: **9.7 3D Textures and Volume Rendering**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 114: **3D Texturing: Relevant Topics**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 115: **3D Texture as a Voxel Grid**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 116: **Object Space to Texture Space**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 117: **3D Texture Access**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 118: **Trilinear Interpolation**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 119: **f = (1 − α) ⋅ f + α ⋅ f**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 120: **3D Texture Memory Footprint**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 121: **3D Mipmaps and Filtering**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 122: **Solid Texturing**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 123: **Volumetric Data as Texture Data**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 124: **Transfer Functions**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 125: **Volume Rendering with 3D Textures**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 126: **Front-to-Back Alpha Compositing**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 127: **Ray Marching Volume Rendering**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 128: **Gradients and Volume Lighting**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 129: **Quality and Performance Trade-Offs**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 130: **3D Texturing Takeaways**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 131: **▪ Textures are sampled GPU data sources used by shaders**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 132: **Literature and other sources used in this chapter**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 133: **▪ Text Books**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?

## 09.1 Texture Objects, Texels, Formats, and Color Space

Source location: Section 9.1

### Commentary

A texture object stores sampled data on the GPU. A texel is one stored texture sample. The texture format decides what channels and numeric representation the samples use. Color space matters because color values may be stored nonlinearly, especially for sRGB images.

The key shift is to stop thinking of texture as only a picture. Textures can store color, normals, depth, lookup data, environment information, or volume data. The shader decides how the sampled values are interpreted.

### Mental Model

A texture is a GPU-accessible sampled data field.

### Check Yourself

Why can the same texture mechanism store both color maps and normal maps?

## 09.2 Texture Coordinates, UV Mapping, and Wrapping

Source location: Section 9.2

### Commentary

Texture coordinates map surface points to locations in texture space. UV coordinates are usually interpolated across primitives during rasterization and then used by the fragment shader to sample a texture.

Wrapping rules decide what happens outside the normal coordinate range. Repeat, clamp, mirrored repeat, and border behavior are not visual afterthoughts; they define the sampling function outside the base domain.

### Mental Model

UVs are the address system that lets a fragment look up texture data.

### Check Yourself

What artifact might appear if a wrapping mode is wrong at the edge of a surface?

## 09.3 Sampling, Filtering, Mipmaps, and Anisotropy

Source location: Section 9.3

### Commentary

Sampling turns continuous texture coordinates into values from discrete texels. Nearest filtering selects a nearby texel and can look blocky. Linear filtering blends nearby texels and looks smoother. Minification is harder because many texels may map to one pixel.

Mipmaps store prefiltered lower-resolution versions of a texture. They reduce aliasing and shimmer when textures are seen at small scale. Anisotropic filtering improves quality when a texture is viewed at a steep angle where footprint shape is elongated.

### Mental Model

Filtering reconstructs values; mipmaps choose an appropriate scale before reconstruction.

### Check Yourself

Why does a distant checkerboard shimmer without mipmapping?

## 09.4 Modern OpenGL Texture Pipeline

Source location: Section 9.4

### Commentary

In modern OpenGL, textures are represented by texture objects, bound to texture units, connected to sampler uniforms, and accessed in shaders. The shader does not sample a filename; it samples a bound texture through a sampler.

Texture bugs often come from state mismatches: wrong active texture unit, wrong sampler uniform, missing mipmaps for a mipmap filter, wrong wrap mode, or wrong internal format.

### Mental Model

OpenGL texturing is a chain: object data -> texture unit -> sampler uniform -> shader lookup.

### Check Yourself

Why can a texture appear black when the shader code is mathematically correct?

## 09.5 Normal Mapping

Source location: Section 9.5

### Commentary

Normal mapping stores normal directions in a texture so that lighting can vary at a finer scale than the geometry. The surface may have few triangles, but the shader receives detailed normals per fragment.

The hard part is coordinate space. Normal maps are often defined in tangent space, so the shader must transform or interpret them with the correct tangent, bitangent, and normal basis.

### Mental Model

Normal mapping changes the lighting normal, not the actual mesh silhouette.

### Check Yourself

Why does normal mapping not change the geometric outline of an object?

## 09.6 Environment Mapping and 3D Textures

Source location: Sections 9.6-9.7

### Commentary

Environment mapping uses textures to represent surrounding illumination or reflections. A direction, not a surface UV alone, can be used to sample an environment map. This is a texture lookup driven by view/reflection geometry.

3D textures and volume rendering extend the same sampled-data idea into three dimensions. Instead of sampling a 2D image, the shader samples a volume. This is useful for data such as medical scans, density fields, or procedural volumetric effects.

### Mental Model

Textures are general sampled data; the coordinate dimensionality depends on the problem.

### Check Yourself

What coordinate type would you use to sample a 3D texture?

## End-of-Lecture Summary

If you remember only one thing from Lecture 09, remember this: This lecture treats textures as sampled data for shading, not merely images glued onto objects. It connects UV coordinates, sampling, filtering, mipmaps, OpenGL texture state, and advanced texture uses.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
