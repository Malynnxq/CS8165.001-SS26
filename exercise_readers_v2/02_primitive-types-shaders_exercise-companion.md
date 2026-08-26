# Exercise Companion 2 — Primitive Types / Shaders

> **Status of the source.** The repository contains the Moodle assignment page titled **“Exercise 2: Primitive Types / Shaders”**, but the actual exercise attachment/question text was not preserved in the export. Therefore the tasks below are **reconstructed study exercises**, not claimed to be the professor's original wording. They are designed from the official assignment topic and the corresponding course lecture material.
>
> **How to use this companion.** Try each task before opening its solution. Every task contains a **Lecture connection** so you can immediately identify whether the required knowledge has already appeared in your textbook reader and where to review it.

---

# 0. What Exercise 2 is trying to make operational

Exercise 1 was about the overall rendering pipeline. Exercise 2 narrows the focus to two things that sit near the beginning and end of that pipeline:

1. **Primitive types:** how a stream of vertices is interpreted as points, lines, triangles, strips, etc.
2. **Shaders:** how per-vertex and per-fragment programs exchange data with the application and with each other.

The conceptual chain is

```text
CPU vertex data
    ↓
VBO + VAO interpretation
    ↓
vertex shader invocations
    ↓
primitive assembly
    ↓
points / lines / triangles
    ↓
rasterization + interpolation
    ↓
fragment shader invocations
    ↓
fragment outputs
```

The goal is not to memorize OpenGL function names in isolation. You should be able to look at data, a primitive mode, and shader code and predict what the GPU does.

## Main lecture source

This sheet is primarily connected to **Lecture 2 — The Rendering Pipeline**:

- Lecture 2 §2 — vertices, primitives, fragments
- Lecture 2 §5 — VBOs, VAOs and vertex attributes
- Lecture 2 §6 — draw calls and primitive assembly
- Lecture 2 §8 — vertex/fragment shaders, attributes, uniforms and varyings
- Lecture 2 §9 — rasterization and interpolation

Later connections:

- **Lecture 3 — Geometric Transformations:** transformations performed in vertex shaders
- **Lecture 6 — Rasterization:** detailed interpolation and fragment generation
- **Lecture 8 — Local Illumination:** per-vertex versus per-fragment lighting
- **Lecture 9 — Texturing:** interpolated texture coordinates and texture sampling in fragment shaders

---

# Task 1 — From vertices to primitives

Consider six vertices in a vertex buffer:

```text
v0  v1  v2  v3  v4  v5
```

For each primitive mode below, state which primitives are assembled:

1. `GL_POINTS`
2. `GL_LINES`
3. `GL_LINE_STRIP`
4. `GL_TRIANGLES`
5. `GL_TRIANGLE_STRIP`

Then answer: why does changing only the primitive mode change the rendered geometry even though the VBO contains exactly the same bytes?

## Lecture connection

**Already discussed:** Lecture 2 §2 and §6.

Review especially the idea that the VBO stores **vertices**, while the draw-call mode tells **primitive assembly** how those vertex shader outputs should be grouped.

## Solution

### 1. `GL_POINTS`

Each vertex is an independent point:

```text
(v0) (v1) (v2) (v3) (v4) (v5)
```

Six vertices → six point primitives.

### 2. `GL_LINES`

Vertices are consumed in independent pairs:

```text
(v0,v1)
(v2,v3)
(v4,v5)
```

Six vertices → three independent line segments.

### 3. `GL_LINE_STRIP`

Each new vertex continues the previous line:

```text
(v0,v1)
(v1,v2)
(v2,v3)
(v3,v4)
(v4,v5)
```

Six vertices → five connected line segments.

### 4. `GL_TRIANGLES`

Vertices are consumed in independent groups of three:

```text
(v0,v1,v2)
(v3,v4,v5)
```

Six vertices → two independent triangles.

### 5. `GL_TRIANGLE_STRIP`

After the first two vertices, every new vertex completes another triangle:

```text
(v0,v1,v2)
(v1,v2,v3)
(v2,v3,v4)
(v3,v4,v5)
```

The winding convention alternates internally so that consistently oriented strip triangles can be rasterized correctly.

### Why the bytes can stay identical

The VBO does not say “I am a triangle.” It contains vertex records. The primitive mode supplies an **interpretation rule** for the sequence of processed vertices.

So:

```text
same vertex stream + different assembly rule = different primitives
```

This is a recurring graphics idea: stored data and the rule used to interpret that data are separate.

### Common mistake

Do not say that `GL_TRIANGLES` somehow converts points into triangles geometrically. The vertices were always geometric positions; primitive assembly simply groups them into triangle primitives.

---

# Task 2 — How many vertices do we need?

You want to render a rectangle using two triangles.

### A

If you use `GL_TRIANGLES` with no index buffer and duplicate shared vertices, how many vertex records are required?

### B

If you use a triangle strip, how many vertex records can represent the rectangle?

### C

Why can indexed rendering reduce duplicated vertex data even when using ordinary triangles?

## Lecture connection

Lecture 2 §5–6: vertex buffers and primitive assembly.

The deeper idea is that **geometric vertices can be shared by multiple primitives**, while a simple non-indexed triangle list may repeat their records.

## Solution

### A — independent triangles

Two triangles × three vertices each:

\[
2\cdot3=6
\]

vertex records.

For a rectangle with corners `A,B,C,D`, we might store

```text
A B C   C B D
```

`B` and `C` appear twice.

### B — triangle strip

A rectangle can be represented with four vertices arranged appropriately:

```text
A B C D
```

The strip produces two triangles from those four processed vertices.

### C — indexed rendering

Instead of duplicating full vertex records, store the four unique vertices once and provide an index sequence such as

```text
0 1 2   2 1 3
```

The indices say which stored vertex to reuse.

This matters especially when a vertex record contains more than position—for example normal, color and texture coordinates. Repeating a large record wastes memory and bandwidth.

### Important nuance

Vertex sharing is only possible when all attributes that define the vertex can truly be shared. At a hard normal discontinuity or UV seam, the same geometric position may need multiple distinct vertex records.

You will understand that issue much better in Lectures 8 and 9.

---

# Task 3 — Read a vertex shader

Consider:

```glsl
#version 330 core

layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aColor;

uniform mat4 uMVP;

out vec3 vColor;

void main()
{
    gl_Position = uMVP * vec4(aPos, 1.0);
    vColor = aColor;
}
```

Explain every declared variable and answer:

1. Which values differ from vertex to vertex?
2. Which value is normally shared by all vertices of one draw call?
3. What is the mandatory geometric output?
4. Where does `vColor` go next?
5. Why is `vec4(aPos,1.0)` used instead of simply multiplying a `mat4` by `vec3`?

## Lecture connection

Lecture 2 §8: shaders, attributes, uniforms, varyings.

For question 5, Lecture 2 introduces the MVP usage; **Lecture 3** explains homogeneous coordinates and transformation matrices in depth.

## Solution

### `aPos`

```glsl
layout(location = 0) in vec3 aPos;
```

This is a **vertex attribute**. Every vertex shader invocation receives the position associated with its current vertex.

### `aColor`

Another per-vertex attribute. Different vertices may carry different colors.

### `uMVP`

```glsl
uniform mat4 uMVP;
```

A **uniform** is supplied by the application and remains constant across shader invocations until the application changes it. For one object draw call, all its vertices commonly use the same MVP matrix.

### `vColor`

```glsl
out vec3 vColor;
```

This is output from the vertex shader. For a triangle, each vertex invocation produces one value. Rasterization interpolates those values across the triangle and makes the resulting per-fragment value available to the matching fragment-shader input.

### `gl_Position`

This built-in output is the transformed **clip-space position** of the current vertex. The later fixed-function pipeline needs it for clipping, perspective division, viewport mapping and rasterization.

### Why homogeneous `vec4`

A 4×4 transformation matrix operates on homogeneous 4-component coordinates. A point is represented as

\[
(x,y,z,1).
\]

The `1` is what allows translation to be represented by matrix multiplication.

Lecture 3 explains why vectors representing directions often use `w=0` while positions use `w=1`.

---

# Task 4 — Match the fragment shader to the vertex shader

Given the vertex shader from Task 3, consider:

```glsl
#version 330 core

in vec3 vColor;
out vec4 FragColor;

void main()
{
    FragColor = vec4(vColor, 1.0);
}
```

Suppose the triangle vertices have colors

```text
v0 = red   = (1,0,0)
v1 = green = (0,1,0)
v2 = blue  = (0,0,1)
```

What color should you expect approximately near the center of the triangle, and why?

## Lecture connection

Lecture 2 §8–9 introduces varyings and interpolation.

**Lecture 6 — Rasterization** develops barycentric interpolation rigorously.

## Solution

The fragment shader does not receive one of the three vertex colors unchanged. The rasterizer interpolates `vColor` across the primitive.

Near the triangle centroid, the barycentric weights are approximately

\[
\alpha=\beta=\gamma=\frac13.
\]

Therefore

\[
C
=\frac13(1,0,0)
+\frac13(0,1,0)
+\frac13(0,0,1)
=\left(\frac13,\frac13,\frac13\right).
\]

So the center is approximately gray.

The causal chain is

```text
vertex colors
↓
vertex shader outputs vColor
↓
rasterizer interpolates vColor
↓
fragment shader receives interpolated value
↓
FragColor
```

### Important connection to later lectures

Exactly the same mechanism later transports:

- normals for Phong shading — Lecture 8;
- texture coordinates — Lecture 9;
- depth and other attributes — Lecture 6/7.

---

# Task 5 — Attribute, uniform, varying, or fragment output?

Classify each quantity according to its most natural role in a simple rendering program:

- vertex position
- vertex color
- one object's model matrix
- camera projection matrix
- texture coordinate at a mesh vertex
- interpolated texture coordinate at a fragment
- final fragment color
- time value used to animate every vertex

## Lecture connection

Lecture 2 §8.

## Solution

| Quantity | Natural role | Why |
|---|---|---|
| vertex position | vertex attribute | differs by vertex |
| vertex color | vertex attribute | can differ by vertex |
| model matrix | uniform | normally shared by the object's vertices |
| projection matrix | uniform | normally shared across many vertices/draws |
| vertex texture coordinate | vertex attribute | stored per mesh vertex |
| fragment texture coordinate | interpolated varying | derived between vertex values |
| final fragment color | fragment shader output | written by fragment processing |
| animation time | uniform | one current time can affect all invocations |

The classification follows one question:

> **At what frequency does this value conceptually change?**

Per vertex → attribute.

Shared across many invocations → uniform.

Passed/interpolated between shader stages → varying/interface value.

Produced as a fragment result → fragment output.

---

# Task 6 — Connect C++ attribute setup to GLSL

Suppose the CPU stores each vertex as

```text
x y z   r g b
```

using six `float`s.

The vertex shader expects

```glsl
layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aColor;
```

Write the essential `glVertexAttribPointer` setup and explain every numerical argument.

## Lecture connection

Lecture 2 §5: VBO, VAO, stride and offset.

This is the point where C++ memory layout meets shader input declarations.

## Solution

```cpp
glVertexAttribPointer(
    0,                      // attribute location
    3,                      // x,y,z
    GL_FLOAT,               // component type
    GL_FALSE,               // do not normalize float data
    6 * sizeof(float),      // bytes from one vertex to the next
    (void*)0                // position begins at byte 0
);
glEnableVertexAttribArray(0);

glVertexAttribPointer(
    1,
    3,                      // r,g,b
    GL_FLOAT,
    GL_FALSE,
    6 * sizeof(float),
    (void*)(3 * sizeof(float)) // skip x,y,z
);
glEnableVertexAttribArray(1);
```

### Why stride is six floats

To get from the position of vertex `i` to the position of vertex `i+1`, the GPU must skip the entire record:

```text
x y z r g b
```

which is six floats.

### Why color offset is three floats

The color begins after

```text
x y z
```

so the starting byte offset is

\[
3\cdot\text{sizeof(float)}.
\]

### What happens if the stride is wrong?

The GPU will read the wrong bytes for later vertices. This can produce distorted geometry, bizarre colors, or apparently random behavior.

The shader declaration itself cannot infer the layout of your C++ array. The VAO configuration establishes that correspondence.

---

# Task 7 — Debug a shader interface

Consider this vertex shader:

```glsl
layout(location = 0) in vec3 aPos;
out vec3 color;

void main()
{
    gl_Position = vec4(aPos, 1.0);
    color = vec3(1.0, 0.0, 0.0);
}
```

and this fragment shader:

```glsl
in vec2 color;
out vec4 FragColor;

void main()
{
    FragColor = vec4(color, 0.0, 1.0);
}
```

What is wrong conceptually?

## Lecture connection

Lecture 2 §8: shader compilation/linking and stage interfaces.

## Solution

The vertex shader produces

```glsl
out vec3 color;
```

but the fragment shader expects

```glsl
in vec2 color;
```

The interface does not agree on the type.

The shader stages are not isolated programs that can arbitrarily reinterpret each other's outputs. During program linking, their interfaces must be compatible.

A corrected fragment input is

```glsl
in vec3 color;
```

and then

```glsl
FragColor = vec4(color, 1.0);
```

works naturally.

### General debugging rule

Whenever data crosses a shader-stage boundary, check:

```text
producer name/location/type
        ↕ compatible with
consumer name/location/type
```

This same idea becomes important for texture coordinates, normals and other interpolated data later in the course.

---

# Task 8 — Why does one draw call invoke the vertex shader many times?

Assume:

```cpp
glDrawArrays(GL_TRIANGLES, 0, 6);
```

### A

How many vertex records are requested?

### B

How many independent triangles are assembled?

### C

Is the fragment shader also executed exactly six times?

Explain.

## Lecture connection

Lecture 2 §6, §8 and §9.

This task tests whether you understand the different **invocation frequencies** of pipeline stages.

## Solution

### A

Six vertex records are submitted for processing.

At the conceptual course level, think of this as six vertex shader invocations.

### B

With `GL_TRIANGLES`, each three processed vertices form one triangle:

\[
6/3=2.
\]

### C

No.

Fragment shader invocation count depends on how many framebuffer samples the rasterized triangles cover, clipping, multisampling and implementation details.

A tiny triangle may produce very few fragments. A large full-screen triangle may produce millions.

This exposes a fundamental distinction:

```text
vertex shader frequency ≈ submitted vertices
fragment shader frequency ≈ covered raster samples/fragments
```

That difference becomes important when comparing Gouraud and Phong shading in Lecture 8: lighting at vertices can be much cheaper than lighting at every fragment.

---

# Task 9 — Predict what a shader does geometrically

Consider:

```glsl
layout(location = 0) in vec3 aPos;
uniform float scale;

void main()
{
    gl_Position = vec4(scale * aPos.xy, aPos.z, 1.0);
}
```

What happens visually when:

1. `scale = 1.0`
2. `scale = 0.5`
3. `scale = 2.0`
4. `scale = -1.0`

Assume the input positions already make sense directly as clip-space coordinates.

## Lecture connection

Lecture 2 §7–8 introduces clip-space output and vertex shaders.

**Lecture 3** is the main reference for scaling transformations.

## Solution

The shader multiplies only the `x` and `y` components by `scale`.

### `scale = 1`

No change.

### `scale = 0.5`

All x/y distances from the origin are halved. The geometry appears half as large in each screen direction.

### `scale = 2`

Coordinates double. The geometry expands around the origin. Parts may move outside the clip volume and be clipped.

### `scale = -1`

Both x and y change sign:

\[
(x,y)\mapsto(-x,-y).
\]

This is equivalent in 2D to a 180° rotation around the origin, not merely “negative size.”

### Why this task matters

Shader code is mathematics executed per vertex. You should train yourself to translate

```glsl
scale * aPos.xy
```

into a geometric operation rather than treating it as programming syntax to memorize.

---

# Task 10 — Why can a fragment shader make a triangle look non-uniform?

Suppose a triangle has no per-vertex color at all. The fragment shader is

```glsl
out vec4 FragColor;

void main()
{
    FragColor = vec4(gl_FragCoord.x / 800.0,
                     gl_FragCoord.y / 600.0,
                     0.0,
                     1.0);
}
```

Assume an 800×600 viewport.

Why can the triangle contain a color gradient even though the vertices carry no colors?

## Lecture connection

Lecture 2 §8–9: fragment shader and rasterization.

## Solution

A fragment shader executes for individual fragment candidates. It can compute output from information available at that fragment; it does not require the color to have originated at vertices.

`gl_FragCoord.x` and `.y` vary with screen position, so the shader computes different RGB values at different fragments.

Approximately:

- left side → small red component;
- right side → large red component;
- bottom → small green component;
- top → large green component.

This distinguishes two mechanisms:

```text
Mechanism A:
vertex data → interpolation → fragment shader

Mechanism B:
fragment shader computes value directly per fragment
```

Later, illumination and texturing combine both mechanisms extensively.

---

# Task 11 — Primitive topology and shared interpolation

Imagine a triangle with scalar vertex values

\[
f_0=0,\qquad f_1=6,\qquad f_2=3.
\]

At a fragment with barycentric weights

\[
\alpha=0.2,\qquad\beta=0.5,\qquad\gamma=0.3,
\]

calculate the interpolated value.

Then explain what this has to do with shaders.

## Lecture connection

Lecture 2 introduces varying interpolation.

For the full mathematics, see **Lecture 6 — Rasterization**.

## Solution

Linear barycentric interpolation gives

\[
f=\alpha f_0+\beta f_1+\gamma f_2.
\]

Therefore

\[
f=0.2(0)+0.5(6)+0.3(3)
=0+3+0.9
=3.9.
\]

If the vertex shader outputs these values as a varying/interface variable, the rasterizer produces approximately this interpolated value for the fragment shader.

The important relationship is

```text
primitive topology
→ determines which vertices belong to the triangle
→ those vertices provide endpoint/corner values
→ rasterization interpolates between those values
→ fragment shader receives local value
```

Primitive assembly and shaders are therefore not independent topics. The primitive determines **which shader outputs are interpolated together**.

---

# Task 12 — Full integration problem

You are given this application-side data:

```cpp
float vertices[] = {
    // position          // color
    -0.5f, -0.5f, 0.0f, 1.0f, 0.0f, 0.0f,
     0.5f, -0.5f, 0.0f, 0.0f, 1.0f, 0.0f,
     0.0f,  0.5f, 0.0f, 0.0f, 0.0f, 1.0f
};
```

with a correctly configured VBO/VAO, followed by

```cpp
glDrawArrays(GL_TRIANGLES, 0, 3);
```

Vertex shader:

```glsl
layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aColor;

out vec3 vColor;

void main()
{
    gl_Position = vec4(aPos, 1.0);
    vColor = aColor;
}
```

Fragment shader:

```glsl
in vec3 vColor;
out vec4 FragColor;

void main()
{
    FragColor = vec4(vColor, 1.0);
}
```

Explain the complete journey from the C++ array to the final colored triangle.

## Lecture connection

This is essentially a mastery test for Lecture 2 §§5–9 and Exercise Companions 1–2.

## Solution

### Step 1 — CPU representation

The application stores three vertex records. Each record contains six floats:

```text
position xyz + color rgb
```

### Step 2 — VBO

The bytes are uploaded to a buffer object accessible to OpenGL.

The VBO itself does not intrinsically know that the first three floats mean position and the next three mean color.

### Step 3 — VAO / attribute layout

The attribute setup tells OpenGL:

```text
location 0 → read three floats at offset 0
location 1 → read three floats after the position
stride     → six floats per vertex
```

This matches the shader's `aPos` and `aColor` declarations.

### Step 4 — draw call

```cpp
glDrawArrays(GL_TRIANGLES, 0, 3)
```

requests three vertices and specifies triangle-list primitive assembly.

### Step 5 — vertex shader

For each vertex, the shader receives one `aPos` and `aColor`.

Because the positions are already suitable as clip coordinates in this simplified example,

```glsl
gl_Position = vec4(aPos,1.0);
```

passes them directly into clip-space output.

The shader also copies each vertex color to `vColor`.

### Step 6 — primitive assembly

The three processed vertices are grouped into one triangle.

### Step 7 — clipping/postprocessing

The GPU determines whether the primitive lies in the visible clip volume, performs the required post-vertex transformations, and maps it toward screen space.

### Step 8 — rasterization

The projected triangle covers many sample positions. Rasterization generates fragment candidates there.

### Step 9 — interpolation

For every fragment, the three vertex `vColor` values are interpolated according to the fragment's location within the triangle.

So the triangle transitions smoothly between red, green and blue.

### Step 10 — fragment shader

Each fragment shader invocation receives its interpolated `vColor` and writes

```glsl
FragColor = vec4(vColor,1.0);
```

### Step 11 — fragment operations/framebuffer

After relevant fragment tests and operations, surviving results update the framebuffer's color attachment.

### Step 12 — display

The rendered framebuffer is eventually presented in the window.

The complete causal chain is

```text
C++ vertex records
↓
VBO stores bytes
↓
VAO explains bytes
↓
vertex shader reads attributes
↓
vertex shader produces clip position + varying color
↓
primitive assembly creates triangle
↓
rasterization creates fragments
↓
colors are interpolated
↓
fragment shader writes color
↓
fragment tests/operations
↓
framebuffer
↓
screen
```

If you can explain this chain without looking it up, you have understood the central purpose of Exercises 1 and 2.

---

# 13. Cross-reference map: “Where did I learn this?”

| Exercise concept | First/main lecture source | Later deeper treatment |
|---|---|---|
| vertex / primitive / fragment | Lecture 2 §2 | Lecture 6 |
| VBO / VAO | Lecture 2 §5 | practical OpenGL throughout course |
| primitive assembly | Lecture 2 §6 | Lecture 6 rasterization context |
| `GL_TRIANGLES`, strips, lines | Lecture 2 §6 | — |
| vertex shader | Lecture 2 §8 | Lectures 3–5 use transformations/projection |
| fragment shader | Lecture 2 §8 | Lectures 8–10 |
| attributes | Lecture 2 §5, §8 | Lecture 9 texture coordinates/normals |
| uniforms | Lecture 2 §8 | transformations, lighting, textures |
| shader stage outputs/varyings | Lecture 2 §8 | Lecture 6 interpolation |
| `gl_Position` / clip space | Lecture 2 §7–8 | Lecture 4 projections/clipping |
| interpolation | Lecture 2 §8–9 | Lecture 6 |
| barycentric interpolation | introduced conceptually in Lecture 2 | Lecture 6 |
| per-vertex vs per-fragment work | Lecture 2 | Lecture 8 Gouraud vs Phong shading |
| texture-coordinate varying | same shader mechanism | Lecture 9 |

---

# 14. What you should be able to do after this sheet

Without notes, you should be able to:

1. Take a sequence of vertices and determine the primitives produced by common primitive modes.
2. Explain why primitive topology is separate from the bytes in a VBO.
3. Explain why triangle strips can reuse processed vertices.
4. Distinguish VBO data from VAO interpretation.
5. Connect `glVertexAttribPointer` to `layout(location=...)` shader inputs.
6. Distinguish attributes, uniforms, shader outputs/varyings, and fragment outputs.
7. Read a simple GLSL vertex shader and explain its geometry mathematically.
8. Explain what `gl_Position` represents.
9. Explain how vertex-shader outputs become fragment-shader inputs.
10. Calculate a simple interpolated varying value.
11. Explain why fragment shader invocation count is unrelated to the raw number of submitted vertices.
12. Diagnose a simple mismatch between shader stages.
13. Explain the complete CPU → GPU → primitive → fragment → framebuffer journey for a triangle.

---

# 15. Final mental model

Do not memorize Exercise 2 as two disconnected subjects called “primitive types” and “shaders.”

They are consecutive pieces of one pipeline:

```text
vertex records
↓
vertex shader computes one result per vertex
↓
primitive mode says which results belong together
↓
assembled primitive
↓
rasterization fills the primitive with fragments
↓
vertex outputs are interpolated across it
↓
fragment shader computes one result per fragment
```

The deepest idea is:

> **A vertex shader transforms and annotates individual vertices; primitive assembly gives those vertices geometric relationships; rasterization turns those relationships into fragment locations; and the fragment shader computes the local result at those locations.**

That relationship is the foundation for nearly everything that follows in the course—transformations, clipping, rasterization, illumination, texturing and shadows.