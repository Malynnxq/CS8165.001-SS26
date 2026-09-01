# Lecture 09 - Texturing Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/09_texturing.txt`
Extracted source pages: 133
Primary assignment connection: Rendering contest and texture/shader tasks

## 1. What Problem This Chapter Solves

Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `texture`: Sampled data array used for color, normals, material data, depth, or other shader inputs. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 09.1 Texture Objects, Texels, Formats, and Color Space

Source location: Section 9.1

A texture object stores sampled data on the GPU. A texel is one stored texture sample. The texture format decides what channels and numeric representation the samples use. Color space matters because color values may be stored nonlinearly, especially for sRGB images.

The key shift is to stop thinking of texture as only a picture. Textures can store color, normals, depth, lookup data, environment information, or volume data. The shader decides how the sampled values are interpreted.

Study meaning: A texture is a GPU-accessible sampled data field.

Closed check: Why can the same texture mechanism store both color maps and normal maps?

### 09.2 Texture Coordinates, UV Mapping, and Wrapping

Source location: Section 9.2

Texture coordinates map surface points to locations in texture space. UV coordinates are usually interpolated across primitives during rasterization and then used by the fragment shader to sample a texture.

Wrapping rules decide what happens outside the normal coordinate range. Repeat, clamp, mirrored repeat, and border behavior are not visual afterthoughts; they define the sampling function outside the base domain.

Study meaning: UVs are the address system that lets a fragment look up texture data.

Closed check: What artifact might appear if a wrapping mode is wrong at the edge of a surface?

### 09.3 Sampling, Filtering, Mipmaps, and Anisotropy

Source location: Section 9.3

Sampling turns continuous texture coordinates into values from discrete texels. Nearest filtering selects a nearby texel and can look blocky. Linear filtering blends nearby texels and looks smoother. Minification is harder because many texels may map to one pixel.

Mipmaps store prefiltered lower-resolution versions of a texture. They reduce aliasing and shimmer when textures are seen at small scale. Anisotropic filtering improves quality when a texture is viewed at a steep angle where footprint shape is elongated.

Study meaning: Filtering reconstructs values; mipmaps choose an appropriate scale before reconstruction.

Closed check: Why does a distant checkerboard shimmer without mipmapping?

### 09.4 Modern OpenGL Texture Pipeline

Source location: Section 9.4

In modern OpenGL, textures are represented by texture objects, bound to texture units, connected to sampler uniforms, and accessed in shaders. The shader does not sample a filename; it samples a bound texture through a sampler.

Texture bugs often come from state mismatches: wrong active texture unit, wrong sampler uniform, missing mipmaps for a mipmap filter, wrong wrap mode, or wrong internal format.

Study meaning: OpenGL texturing is a chain: object data -> texture unit -> sampler uniform -> shader lookup.

Closed check: Why can a texture appear black when the shader code is mathematically correct?

### 09.5 Normal Mapping

Source location: Section 9.5

Normal mapping stores normal directions in a texture so that lighting can vary at a finer scale than the geometry. The surface may have few triangles, but the shader receives detailed normals per fragment.

The hard part is coordinate space. Normal maps are often defined in tangent space, so the shader must transform or interpret them with the correct tangent, bitangent, and normal basis.

Study meaning: Normal mapping changes the lighting normal, not the actual mesh silhouette.

Closed check: Why does normal mapping not change the geometric outline of an object?

### 09.6 Environment Mapping and 3D Textures

Source location: Sections 9.6-9.7

Environment mapping uses textures to represent surrounding illumination or reflections. A direction, not a surface UV alone, can be used to sample an environment map. This is a texture lookup driven by view/reflection geometry.

3D textures and volume rendering extend the same sampled-data idea into three dimensions. Instead of sampling a 2D image, the shader samples a volume. This is useful for data such as medical scans, density fields, or procedural volumetric effects.

Study meaning: Textures are general sampled data; the coordinate dimensionality depends on the problem.

Closed check: What coordinate type would you use to sample a 3D texture?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### texture

Sampled data array used for color, normals, material data, depth, or other shader inputs. In an exam answer, connect `texture` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

### texel

A stored sample in texture memory. In an exam answer, connect `texel` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

### UV coordinates

Coordinates that map surface locations to texture space. In an exam answer, connect `UV coordinates` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

### filtering

Rule for reconstructing values between texels, such as nearest or linear filtering. In an exam answer, connect `filtering` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

### mipmap

Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling. In an exam answer, connect `mipmap` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

### environment mapping

Using texture lookup to approximate surrounding reflections or distant lighting. In an exam answer, connect `environment mapping` to the chapter chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`sampled value = texture(sampler, uv), then shader interprets the value`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `Rendering contest and texture/shader tasks`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not reduce texturing to pasting an image onto geometry.

The trap is dangerous because it usually sounds close to the truth. High exam performance depends on catching these near-misses quickly. When a multiple-choice option looks plausible, test it against the full chain: input, operation, output, next use. If one of those links is missing or wrong, the option is probably a distractor.

## 8. What A Strong Answer Must Contain

- The problem this chapter solves.
- The important data or object representation.
- The operation, algorithm, formula, or API mechanism.
- The output representation.
- The next pipeline stage or later use.
- One assignment or OpenGL/software connection.
- One typical mistake and the corrected distinction.

## 9. Closed-Format Self-Test

1. Complete the chain: `fragment coordinates -> ____ -> sampler/filter/wrap state -> texel fetch -> shader meaning`
2. Match `texel` to its role: A stored sample in texture memory.
3. Select the dangerous misconception: Do not reduce texturing to pasting an image onto geometry.
4. Explain in one sentence why `UV coordinates` belongs in this chapter.

## 10. End Condition

You are done with Lecture 09 only when you can read a new question, recognize that it belongs to `Texturing`, and reconstruct the relevant part of `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.
