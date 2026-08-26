# Chapter 9 — Texturing

> **Purpose.** Lecture 8 explained how a light/material model computes the appearance of a surface point. But its material coefficients were effectively constant over a surface. Real objects contain writing, scratches, bricks, pores, varying roughness, small bumps, and many other spatial variations. This chapter explains how **textures turn those spatially varying properties into sampled data that shaders can efficiently look up**.
>
> **Primary course source:** `course_text_parts/03_lectures/09_texturing.txt` (Lecture 9 slides, 19 July 2026).

## 1. The problem left by local illumination

In Lecture 8, a diffuse term looked like

\[
I_d=k_dL_d\max(0,n\cdot l).
\]

But where does `k_d` come from?

If one constant `k_d` is stored for an entire object, every point has essentially the same base material color. To represent a brick wall faithfully with geometry alone, we might need to model every brick, crack, scratch, and bump.

That would be wasteful because many visible details affect **appearance** much more than the object's large-scale silhouette.

A texture provides another source of information:

```text
fragment position on object
        ↓
texture coordinate
        ↓
texture lookup
        ↓
material/shading data
        ↓
fragment shader
```

The most familiar texture stores color, but a texture can store almost any sampled field.

---

# Part I — What a texture actually is

## 2. A texture is sampled data, not necessarily an image

A useful definition is:

> A **texture** is a sampled data field that a rendering program can access using coordinates.

Examples of stored values include:

- base color/albedo;
- opacity;
- normal vectors;
- roughness;
- metallic values;
- ambient-occlusion factors;
- heights;
- masks;
- density;
- arbitrary numerical lookup data.

This explains why “texture = picture glued onto an object” is too narrow. A color photograph is merely one common case.

---

## 3. Texels

A **texel** (texture element) is one stored sample in a texture.

For a 2D image texture it is analogous to a pixel, but the terminology reminds us that texture samples do not have to correspond one-to-one with screen pixels.

A texel can have layouts such as

```text
R
RG
RGB
RGBA
```

or specialized depth/integer/floating-point formats.

Channel count does **not** determine meaning. Three channels might encode RGB color or the three components of a normal vector. One channel might mean roughness, opacity, height, density, or an object ID.

The shader defines the semantics.

---

## 4. Texture dimensionality

A texture has a domain.

A 1D texture is sampled with

\[
s.
\]

A 2D texture is sampled with

\[
(s,t).
\]

A 3D texture is sampled with

\[
(s,t,r).
\]

Typical uses are:

- 1D: lookup tables and transfer functions;
- 2D: images and material maps;
- 3D: volume data and solid textures.

Texture coordinates are usually normalized so each dimension conceptually occupies `[0,1]`.

---

# Part II — From a file to something a shader can sample

## 5. Do not confuse file, texture object, and sampler

Suppose you load `brick.png`.

There are several distinct concepts:

```text
PNG/JPEG/EXR file
        ↓ decode
CPU-side array
        ↓ upload
GPU texture object
        ↓ accessed through
shader sampler
        ↓
texture lookup result
```

A PNG file is a storage/asset format. `GL_RGBA8` is a GPU texture format. A `sampler2D` is a shader interface for sampling a compatible texture.

These are related, but they are not the same thing.

---

## 6. Internal formats and memory

The GPU needs to know how each texel is represented.

Examples include:

- `GL_R8` — one normalized 8-bit channel;
- `GL_RGBA8` — four normalized 8-bit channels;
- `GL_RGBA16F` — four 16-bit floating-point channels;
- `GL_R32F` — one 32-bit float;
- depth formats such as `GL_DEPTH_COMPONENT24`.

For a 2D texture,

\[
\text{memory}=w\,h\,(\text{bytes per texel}).
\]

So a 4096×4096 RGBA8 texture needs

\[
4096^2\cdot4=67,108,864\text{ bytes}\approx64\text{ MiB}.
\]

Higher precision and more channels cost memory and bandwidth.

This is why texture format is an engineering decision, not cosmetic metadata.

---

## 7. Normalized integers, integers, and floating point

A stored byte value `255` can be interpreted as normalized `1.0`, or it can remain integer `255`, depending on the texture representation and sampler.

Broadly:

- normalized formats store integers but return normalized floating-point values;
- integer formats preserve integer values;
- floating-point formats store floating-point values directly.

Use integer representations for discrete labels/IDs and floating point when values need larger range or precision, such as HDR data and simulation fields.

---

## 8. Color textures versus data textures

This is one of the easiest practical mistakes to make.

A base-color texture represents perceptual color and is commonly encoded in **sRGB**. Before physically meaningful arithmetic, it should be decoded to a linear representation.

But a normal map or roughness map already stores numerical data. Applying sRGB decoding to it would alter those numbers and therefore corrupt the meaning.

Rule:

```text
perceptual color texture → sRGB decoding
numeric/data texture     → keep linear
```

---

# Part III — How a point on a triangle knows where to look in a texture

## 9. We need a mapping between spaces

A mesh vertex lives in 3D object space:

\[
p=(x,y,z).
\]

A 2D texture lookup needs

\[
(s,t).
\]

Therefore we need a mapping

\[
(x,y,z)\longrightarrow(s,t).
\]

This is **texture mapping / parameterization**.

Usually each mesh vertex stores texture coordinates alongside its position, normal, and other attributes.

During rasterization, the texture coordinates are interpolated across the triangle, exactly like other varying vertex attributes.

Thus Lecture 6's interpolation machinery becomes central again.

---

## 10. Simple parameterizations

Some shapes have natural parameters.

For a cylinder of radius `r` and height `h`, a surface point can be written as

\[
p(\theta,z)=(r\cos\theta,r\sin\theta,z).
\]

A natural texture mapping is

\[
s=\frac{\theta}{2\pi},\qquad t=\frac{z}{h}.
\]

Walking once around the cylinder traverses the horizontal texture dimension once; moving from bottom to top traverses the vertical dimension.

A disc similarly uses angle and radial distance.

The key insight is:

> UV coordinates are coordinates on a parameter domain for the surface.

---

## 11. Why arbitrary meshes need UV unwrapping

A complicated 3D surface usually has no single distortion-free flattening onto a rectangle.

Imagine cutting the surface of a cardboard globe so it can lie flat. You need seams, and some regions stretch.

UV unwrapping performs the analogous operation for a mesh.

This produces two unavoidable issues:

- **seams** — discontinuities where the surface is cut;
- **distortion** — unequal stretching/compression of texture area.

So UV mapping is not simply assigning random `(s,t)` values. It is a geometric parameterization problem.

---

## 12. Two-part mappings

For complicated geometry, coordinates can be derived using an intermediate parameterizable shape such as a plane, cylinder, sphere, or box.

Conceptually:

```text
complex object
   ↓ project/map
intermediate simple geometry
   ↓ parameterize
texture coordinates
```

Different projection strategies trade distortion against seams and suitability for particular object shapes.

---

# Part IV — A texture lookup usually lands between texels

## 13. Why filtering is necessary

Suppose a fragment has texture coordinate `(0.413,0.726)`. There is generally no texel center exactly at that continuous coordinate.

The renderer therefore needs a **reconstruction/filtering rule**.

Two basic choices are nearest-neighbor and linear filtering.

---

## 14. Nearest-neighbor filtering

Nearest filtering chooses the closest texel.

It is simple and preserves hard texel boundaries, but magnified textures look blocky.

It is appropriate when discrete labels or deliberately pixelated appearance should not be blended.

---

## 15. Bilinear interpolation

For a 2D texture, linear filtering combines the four neighboring texels.

Let the surrounding samples be

\[
f_{00},f_{10},f_{01},f_{11}.
\]

Interpolate horizontally:

\[
f_0=(1-\alpha)f_{00}+\alpha f_{10},
\]

\[
f_1=(1-\alpha)f_{01}+\alpha f_{11}.
\]

Then vertically:

\[
f(s,t)=(1-\beta)f_0+\beta f_1.
\]

This is **bilinear interpolation**.

Notice the recurring principle from earlier lectures: continuous values are reconstructed from discrete samples by interpolation.

---

# Part V — Magnification and minification are different problems

## 16. Magnification

A texture is magnified when a texel covers multiple screen pixels.

The problem is:

> We have too few texture samples for the displayed area. How do we reconstruct values between them?

Nearest gives blockiness. Bilinear filtering smooths transitions.

---

## 17. Minification

A texture is minified when many texels project into one screen pixel.

This is harder.

Suppose a checkerboard contains hundreds of black/white texels inside one pixel footprint. Choosing one texel is not a faithful representation of the average contribution of that whole region.

As the camera moves, the chosen samples change rapidly, producing aliasing, flickering, and moiré patterns.

This is a sampling-theory problem: high-frequency texture detail is being sampled below a sufficient rate.

---

# Part VI — Mipmaps

## 18. Pre-filter the texture at several scales

A **mipmap pyramid** stores successively lower-resolution versions of a texture:

```text
level 0: 1024 × 1024
level 1:  512 × 512
level 2:  256 × 256
...
level 10:   1 × 1
```

When an object becomes small on screen, the GPU samples a smaller mip level whose texels already summarize larger regions of the original texture.

This approximates the filtering that minification actually requires.

---

## 19. Why the full mip chain costs only about one third extra

For a 2D texture, each level has one quarter as many texels as the previous level:

\[
1+\frac14+\frac1{16}+\frac1{64}+\cdots
\]

This geometric series converges to

\[
\frac{1}{1-1/4}=\frac43.
\]

Therefore the complete mip chain uses approximately

\[
\frac43
\]

times the base-level memory—about **33% extra**, not twice the memory.

---

## 20. Trilinear mipmap filtering

Bilinear filtering interpolates within one mip level.

For smoother transitions between levels, the GPU can:

1. bilinearly sample mip level `k`;
2. bilinearly sample mip level `k+1`;
3. linearly interpolate between those two results.

This is commonly called **trilinear filtering** in the mipmapping context.

Do not confuse it with trilinear interpolation of a 3D texture, which also uses the word “trilinear” but refers to interpolation across three spatial texture dimensions.

---

# Part VII — Why anisotropic filtering exists

## 21. A pixel footprint need not be square in texture space

When a textured surface is viewed obliquely, one screen pixel can correspond to a long, thin region in texture space.

Ordinary mipmapping chooses a roughly isotropic scale. It may therefore blur too much in one direction or undersample another.

**Anisotropic filtering** takes the directional shape of the footprint into account and uses multiple appropriately distributed samples.

Result: textures viewed at grazing angles—roads, floors, walls receding into the distance—retain more detail with less aliasing.

---

# Part VIII — What happens outside [0,1]?

## 22. Texture wrapping

Texture coordinates are not necessarily restricted before sampling. A coordinate might be `(2.3,-0.2)`.

The wrapping mode defines what this means.

### Clamp to edge

Coordinates outside the domain use the nearest edge value.

### Clamp to border

Outside coordinates produce a configurable border color.

### Repeat

The fractional part repeats the texture periodically. For example,

\[
s=2.3\rightarrow0.3.
\]

### Mirrored repeat

Alternating repetitions are reflected, which can make repeated patterns less visibly discontinuous at boundaries.

Wrapping is configured independently for texture dimensions such as `S` and `T`.

---

# Part IX — Modern OpenGL mental model

## 23. Texture object, texture unit, and sampler uniform

These names are easy to mix up.

A **texture object** stores texture data/configuration.

A **texture unit** is a binding slot through which shaders can access a bound texture.

A **sampler uniform** in GLSL identifies which texture unit a shader lookup should use.

Conceptually:

```text
texture object A ──bind──> texture unit 0 ←── sampler uniform baseTex
texture object B ──bind──> texture unit 1 ←── sampler uniform normalTex
```

Then the shader can execute a lookup such as

```glsl
vec4 c = texture(baseTex, uv);
```

where `uv` is an interpolated texture coordinate.

---

## 24. Where texture coordinates travel

At a vertex, texture coordinates are vertex attributes.

The vertex shader passes them as varying output. Rasterization interpolates them. The fragment shader receives the interpolated value and samples the texture.

```text
vertex buffer
(position, normal, uv)
        ↓
vertex shader
        ↓ uv
rasterizer/interpolator
        ↓ interpolated uv
fragment shader
        ↓
texture(sampler, uv)
        ↓
texel/filter result
```

This connects texturing directly to the programmable rendering pipeline.

---

# Part X — Textures and illumination meet

## 25. A texture can provide material coefficients

Lecture 8 used constants such as `k_d`, `k_s`, etc.

Now these can vary spatially:

\[
k_d=k_d(s,t).
\]

At each fragment:

1. obtain interpolated `(s,t)`;
2. sample the albedo/diffuse texture;
3. use that value in the illumination equation.

So instead of one material color per mesh, every surface location can have its own.

Modern materials commonly use a **stack** of maps:

```text
base color map
normal map
roughness map
metallic map
AO map
emissive map
opacity map
```

All can be sampled using the same or related UV coordinates.

---

# Part XI — Normal mapping

## 26. Geometry is expensive; normals are powerful

Lecture 8 showed that the normal strongly affects lighting. A tiny change in normal direction can create the appearance of a bump even when the actual surface position has not changed.

This suggests a trick:

> Instead of adding triangles for every small bump, store small-scale normal variations in a texture.

That is **normal mapping**.

The object's silhouette remains unchanged, because geometry has not changed. But illumination reacts as if the surface orientation contained fine detail.

---

## 27. Encoding a normal in a texture

A normalized normal has components in

\[
[-1,1].
\]

Ordinary normalized texture channels commonly store

\[
[0,1].
\]

So encode a component approximately as

\[
n'=\frac{n+1}{2}=0.5n+0.5.
\]

After sampling, decode:

\[
n=2n'-1,
\]

then normalize:

\[
n\leftarrow\frac{n}{\|n\|}.
\]

The normalization is important because filtering/interpolation can change vector length.

---

# Part XII — Tangent space

## 28. Why normal-map vectors need their own coordinate system

Suppose a normal map stores `(0,0,1)` as “no perturbation.” What direction should `+z` mean?

It cannot mean world `+z`, because the same texture may be applied to a wall, floor, curved character, etc.

Instead normal maps are commonly expressed in **tangent space**, a local coordinate system attached to the surface.

Its basis is:

- `T` — tangent, approximately the direction of increasing texture coordinate `s/u`;
- `B` — bitangent, approximately increasing `t/v`;
- `N` — geometric/interpolated surface normal.

A flat tangent-space normal `(0,0,1)` therefore means “point along the underlying surface normal,” regardless of how the object is oriented globally.

---

## 29. The TBN matrix

Arrange the basis vectors into a matrix

\[
TBN=[\,T\;B\;N\,].
\]

Then a tangent-space normal can be transformed into the coordinate system used for lighting:

\[
n_{view/world}=TBN\,n_{tangent}
\]

provided all basis vectors have been expressed in the intended target coordinate system and conventions are consistent.

This is analogous to the coordinate-system changes from earlier transformation lectures: a vector's numerical components only make sense relative to a basis.

---

## 30. Where tangent and bitangent come from

For a triangle, geometric edge vectors can be related to changes in UV coordinates.

Let

\[
e_0=p_1-p_0,\qquad e_1=p_2-p_0,
\]

and UV differences

\[
(\Delta u_0,\Delta v_0),\qquad(\Delta u_1,\Delta v_1).
\]

Assume

\[
e_0=\Delta u_0T+\Delta v_0B,
\]

\[
e_1=\Delta u_1T+\Delta v_1B.
\]

In matrix form,

\[
\begin{bmatrix}e_0\\e_1\end{bmatrix}
=
\begin{bmatrix}
\Delta u_0&\Delta v_0\\
\Delta u_1&\Delta v_1
\end{bmatrix}
\begin{bmatrix}T\\B\end{bmatrix}.
\]

Invert the 2×2 UV-difference matrix to solve for `T` and `B`.

The important conceptual meaning is more useful than memorizing the expanded formula:

> `T` and `B` tell us which 3D directions correspond to moving horizontally and vertically in the texture.

---

# Part XIII — Environment mapping

## 31. Approximate reflections with a texture lookup

A shiny object should reflect its surroundings. Fully tracing reflected rays through the scene is expensive.

Environment mapping replaces much of that computation with a lookup.

At a surface point:

1. compute the viewing/incident direction;
2. reflect it around the normal to obtain `r`;
3. use `r` as a direction into an environment representation;
4. fetch the corresponding environment color.

So the texture is no longer primarily indexed by UV coordinates painted onto the object. It is indexed by a **direction**.

---

## 32. Cube maps

A cube map stores the environment in six square images corresponding to the faces of a cube.

Given a direction vector

\[
d=(d_x,d_y,d_z),
\]

the largest-magnitude component determines which cube face is hit, and the other components determine coordinates on that face.

Advantages include:

- natural representation of directional data;
- no spherical pole singularity;
- strong GPU support;
- useful for skyboxes, reflections, and image-based lighting.

Potential issues include face seams, inconsistent orientation, and filtering/compression artifacts.

---

## 33. Why environment reflections are only approximate

A simple environment map effectively assumes the surrounding environment is far away.

The same direction is therefore treated as seeing roughly the same environmental color regardless of the exact point on the object.

It usually does not correctly model:

- self-reflection;
- nearby moving objects;
- parallax from local surroundings;
- multiple interreflections.

So it creates a convincing visual cue, not a complete solution to global illumination.

---

# Part XIV — 3D textures

## 34. From texels to voxels

A 3D texture stores a regular grid of samples. A sample is often called a **voxel**.

Coordinates are

\[
(s,t,r)\in[0,1]^3.
\]

Voxel values might represent:

- density;
- temperature;
- CT/MRI intensity;
- color and opacity;
- material IDs;
- vector fields.

A 3D texture is therefore a sampled function

\[
f(s,t,r).
\]

---

## 35. Trilinear interpolation in a 3D texture

A continuous lookup position usually lies between eight neighboring voxels.

Linear filtering blends them by interpolating successively along the three axes.

Conceptually:

```text
8 corner voxels
→ 4 interpolations along s
→ 2 interpolations along t
→ 1 interpolation along r
→ final value
```

This is spatial **trilinear interpolation**.

Again, distinguish it from “trilinear mipmap filtering” for a 2D texture.

---

## 36. Why 3D textures become huge quickly

Memory is

\[
\text{memory}=w\,h\,d\,(\text{bytes per voxel}).
\]

If every dimension doubles, voxel count increases by

\[
2^3=8.
\]

Thus volume resolution is much more expensive than 2D image resolution.

For a cubic texture with side length `N`, storage grows as

\[
O(N^3).
\]

---

## 37. 3D mipmap overhead

Each next 3D mip level has half the resolution in every dimension, therefore only one eighth as many voxels:

\[
1+\frac18+\frac1{64}+\cdots
=
\frac{1}{1-1/8}
=
\frac87.
\]

So a full 3D mip chain adds roughly **1/7 ≈ 14.3%** over the base volume.

However, averaging voxel data is not always semantically meaningful—for example, averaging categorical material IDs can create nonsense.

---

# Part XV — Solid texturing

## 38. A material can exist throughout 3D space

A 2D texture is like a patterned sheet wrapped around a surface.

A 3D solid texture is more like a block of patterned material from which the object has been carved.

At a surface point, use its 3D position to sample the texture volume.

This is useful for materials such as marble, wood, stone, or procedural noise and avoids many UV seams.

---

# Part XVI — Volume rendering

## 39. A volume is not just a surface

Medical and scientific data often gives a scalar field

\[
\rho=f(x,y,z).
\]

For example, `ρ` may be CT intensity or smoke density.

There may be no explicit triangle surface to render. Instead we want to visualize values throughout the volume.

Store `ρ` in a 3D texture, then determine how sampled values should appear.

---

## 40. Transfer functions

A **transfer function** maps a scalar data value to optical properties:

\[
T(\rho)=(c,\alpha).
\]

Here

- `c` = displayed/emitted color;
- `α` = opacity.

This allows different value ranges to be emphasized or hidden.

For example, a CT visualization might make one tissue range nearly transparent and bone-like values opaque and bright.

The transfer function therefore answers:

> What should this numerical data value look like?

---

## 41. Ray marching

One common volume-rendering method sends one ray through the volume for each relevant image fragment/pixel.

For a ray

\[
p(t)=o+td,
\]

sample repeatedly:

```text
enter volume
↓
sample density
↓
apply transfer function
↓
accumulate color/opacity
↓
advance along ray
↓
repeat until exit or opaque
```

This connects directly to the ray-casting ideas from Lecture 7, except now we do not stop at the first surface intersection. We integrate/composite many samples along the ray.

---

## 42. Front-to-back alpha compositing

Suppose accumulated color/opacity are `C` and `α`, and a new sample has color `c_i` and opacity `α_i`.

Front-to-back compositing can be written

\[
C_{new}=C+(1-\alpha)\alpha_i c_i,
\]

\[
\alpha_{new}=\alpha+(1-\alpha)\alpha_i.
\]

Why the factor `(1-α)`?

Because only the fraction of light not already blocked by accumulated opacity can contribute from deeper samples.

Once `α` is near `1`, deeper samples have almost no visible influence. We can stop early—**early ray termination**.

---

## 43. Step size: quality versus cost

Ray marching samples a continuous volume at discrete positions.

Small step size:

- more samples;
- better chance of detecting thin structures;
- higher cost.

Large step size:

- fewer samples;
- faster;
- can miss features and create artifacts.

Thus volume rendering is another sampling problem.

Acceleration techniques include empty-space skipping, early termination, bricking/paging, and lower-resolution representations.

---

## 44. Gradients as normals inside a volume

For a scalar field `ρ(x,y,z)`, the gradient

\[
\nabla\rho=
\begin{bmatrix}
\partial\rho/\partial x\\
\partial\rho/\partial y\\
\partial\rho/\partial z
\end{bmatrix}
\]

points toward greatest increase.

On a constant-value surface inside the field, the gradient is perpendicular to that surface. Therefore a normalized gradient can act like a surface normal for illumination.

With sampled data, derivatives can be approximated by central differences, e.g.

\[
\frac{\partial\rho}{\partial x}
\approx
\frac{\rho(x+\Delta,y,z)-\rho(x-\Delta,y,z)}{2\Delta}.
\]

The lecture's proportional gradient expression may omit the common denominator when only direction matters, because normalization removes a shared scale factor.

This lets Phong-like lighting from Lecture 8 be reused inside volume rendering.

---

# Part XVII — The whole chapter as one pipeline

## 45. Surface texturing

```text
mesh vertex
(position, normal, UV)
        ↓
vertex shader
        ↓
rasterization + interpolation
        ↓
fragment UV
        ↓
wrapping + filtering + mip selection
        ↓
texture lookup(s)
        ↓
albedo / normal / roughness / etc.
        ↓
illumination model
        ↓
fragment color
```

## 46. Volume texturing

```text
3D sampled field
        ↓
GPU 3D texture
        ↓
viewing ray
        ↓
repeated trilinear samples
        ↓
transfer function
        ↓
front-to-back compositing
        ↓
final pixel color
```

These are not unrelated topics. Both are manifestations of the same core idea:

> **Store a sampled function in GPU memory, construct coordinates into that function, reconstruct values between stored samples, and use those values during rendering.**

---

# Part XVIII — Common confusions

## 47. Pixel versus texel

A **pixel** belongs to an image/framebuffer/display grid.

A **texel** belongs to a texture.

One pixel may depend on many texels during minification; one texel may affect many pixels during magnification.

---

## 48. UV interpolation versus texture filtering

These are two different interpolations.

First, rasterization interpolates **UV coordinates across the triangle**.

Then, the texture unit uses the resulting UV coordinate to interpolate **texel values inside the texture**.

```text
vertex UVs
→ interpolate across triangle
→ fragment UV
→ filter neighboring texels
→ sampled value
```

Do not merge these into one operation.

---

## 49. Texture mapping versus normal mapping

Texture mapping is the general mechanism of sampling texture data using coordinates.

Normal mapping is one particular use: the sampled data represents local normal directions.

---

## 50. Normal mapping versus actual geometry

Normal mapping changes lighting, not the true mesh surface.

Therefore it generally does not change:

- silhouette;
- actual intersections;
- true geometric depth;
- shadows unless the shadow method specifically accounts for the detail.

It creates the appearance of small-scale geometric detail through illumination.

---

## 51. Mipmapping does not add detail

Mipmaps contain increasingly **less** high-frequency information. Their purpose is to correctly represent a texture when it projects to fewer pixels and thereby reduce aliasing.

---

## 52. Environment mapping is not exact ray tracing

It uses a precomputed/captured environment representation and simplifying assumptions. It can look reflective without solving all scene-dependent reflection paths.

---

# Part XIX — Exam-oriented mastery

## 53. Questions you should be able to answer from reasoning

You should be able to explain:

1. Why textures separate appearance complexity from geometric complexity.
2. Why a texture is more general than a color image.
3. Pixel versus texel versus voxel.
4. Texture file versus GPU texture object versus sampler.
5. What internal formats determine.
6. Why color textures and data textures require different color-space handling.
7. How UV coordinates map a 3D surface to a 2D texture domain.
8. Why seams and distortion arise in UV unwrapping.
9. Why texture coordinates are interpolated across triangles.
10. Nearest versus bilinear filtering.
11. Magnification versus minification.
12. Why minification creates aliasing.
13. How mipmaps reduce minification aliasing.
14. Why a 2D mip chain costs approximately `4/3` of base memory.
15. What trilinear mipmap filtering does.
16. Why anisotropic filtering helps at oblique viewing angles.
17. Clamp, border, repeat, and mirrored-repeat wrapping.
18. Texture objects, units, and sampler uniforms in OpenGL.
19. How textures provide spatially varying material coefficients.
20. How normal mapping creates apparent geometric detail.
21. Why normal-map values must be decoded from `[0,1]` to `[-1,1]`.
22. What tangent space is and why it is useful.
23. What the TBN matrix does.
24. How tangent/bitangent directions follow from triangle edges and UV differences.
25. How environment mapping converts a reflection direction into a lookup.
26. Cube-map advantages and limitations.
27. How 3D textures generalize 2D textures.
28. Why 3D texture memory grows cubically.
29. How trilinear interpolation reconstructs a value from eight voxels.
30. What a transfer function does in volume rendering.
31. How ray marching samples a volume.
32. Why front-to-back compositing contains `(1-α)`.
33. Why early ray termination works.
34. Why the gradient of a scalar field can act as a normal.

---

# 54. Final mental model

Remember Lecture 9 as a progression:

```text
Lecture 8:
a surface point needs material properties
        ↓
but real material properties vary over space
        ↓
store those variations as sampled texture data
        ↓
assign coordinates from geometry into texture space
        ↓
rasterization interpolates those coordinates
        ↓
texture filtering reconstructs values between texels
        ↓
mipmaps / anisotropy handle difficult sampling scales
        ↓
shader uses samples as color, normal, roughness, etc.
        ↓
normal maps even encode apparent geometric detail
        ↓
environment maps turn directions into sampled surroundings
        ↓
3D textures extend the same idea from surfaces to volumes
        ↓
ray marching repeatedly samples and composites a volume
```

The deepest idea of the chapter is:

> **A texture is a sampled function. Texturing is the process of constructing coordinates into that function, reconstructing a value from discrete samples, and using the result to control rendering.**

Once you see textures this way, UV maps, normal maps, cube maps, mipmaps, and volume textures stop looking like separate tricks. They are different applications of the same sampling-and-lookup mechanism.
