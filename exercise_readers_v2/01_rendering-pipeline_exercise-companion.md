# Exercise Companion 01 — Rendering Pipeline

> **Important source note.** The repository contains the Moodle page for **Exercise 1: Rendering Pipeline**, but the original task sheet/attachment itself is missing. Therefore the exercises below are a **reconstructed study sheet**, not a transcription of the official Exercise 1. The reconstruction is grounded in the official Lecture 2 material and the course's OpenGL/C++ starter context. If the original sheet is later added to the repository, replace the reconstructed task statements while keeping this explanation/solution structure.
>
> **Primary lecture link:** `lecture_readers_v2/markdown/02_rendering-pipeline_textbook.md`
>
> **Official lecture source:** `course_text_parts/03_lectures/02_rendering-pipeline.txt`

---

# How to use this sheet

For every task, follow this order:

1. **Read the task without the solution.**
2. Look at **What you must already know**.
3. If one item is unclear, jump to the cited Lecture 2 section.
4. Try the task yourself.
5. Only then read **Solution and reasoning**.
6. Finish with **Can I now explain this without notes?**

The point is not to memorize answers. It is to make the exercise tell you **which lecture knowledge it is testing**.

---

# Task 1 — Reconstruct the rendering pipeline

## Reconstructed exercise text

Put the following concepts into a sensible rendering order and explain what representation enters and leaves each stage:

- framebuffer
- rasterization
- application stage
- fragment tests / operations
- geometry processing
- primitives
- fragments
- vertices

Then answer:

1. At which point does the pipeline stop working only with continuous geometry and begin producing discrete screen-related samples?
2. Why is a fragment not yet the same thing as a final pixel?
3. Why must fragment tests happen after rasterization?

## What you must already know

This is taught in **Lecture 2**:

- Section 1 — *The one problem behind the whole chapter*
- Section 2 — *Vocabulary you need before the pipeline details*
- Section 3 — *Application, geometry, rasterization, and why the order matters*
- Section 9 — *Rasterization and fragments without hand-waving*

Original slide anchors: Lecture 2 slides **2, 5–9, 35–36, 55–58, 68–85**.

## Solution and reasoning

A useful conceptual order is:

```text
application stage
    ↓
vertex data
    ↓
geometry processing
    ↓
primitives
    ↓
rasterization
    ↓
fragments
    ↓
fragment tests / operations
    ↓
framebuffer values / pixels
```

### Why this order exists

The **application stage** decides what scene objects exist and what should be submitted for rendering. It prepares data but does not yet turn geometry into image samples.

The **geometry stage** processes vertices and assembles them into primitives such as triangles. Transformations and projection place these primitives into the correct coordinate representation for the camera.

**Rasterization** is the crucial representation change. Before rasterization, a triangle is still a continuous mathematical primitive. After rasterization, the GPU has discrete candidate contributions associated with framebuffer sample locations.

Those candidates are **fragments**.

A fragment is not automatically a final pixel because it can still fail tests. For example, two triangles may produce fragments at the same screen location. The depth test can reject the farther fragment.

Therefore fragment tests must happen **after** rasterization: before rasterization there is no fragment at a particular sample location whose depth/stencil/scissor status could be tested.

## Compact exam answer

> Rasterization converts projected primitives into fragments. A fragment is a candidate framebuffer contribution, not yet a final pixel, because it still has to survive fragment tests such as depth and stencil. Surviving fragments may update framebuffer attachments such as color and depth.

## Can I now explain this without notes?

You should be able to explain the difference between:

```text
vertex → primitive → fragment → pixel/framebuffer value
```

without using any of those words as synonyms.

---

# Task 2 — VBO, VAO, stride, and offset

## Reconstructed exercise text

A program stores vertices in the following interleaved layout:

```text
[x, y, z, r, g, b]
```

Each component is a `float`.

Answer:

1. What should be stored in the VBO?
2. What should be remembered by the VAO?
3. What stride should be used for both attributes?
4. What offset should be used for position?
5. What offset should be used for color?
6. Explain in words what `glVertexAttribPointer` tells OpenGL.

Then write a plausible OpenGL setup for attribute location `0 = position` and `1 = color`.

## What you must already know

Lecture 2:

- Section 5 — *Why geometry is uploaded to the GPU*
- Section 6 — *Draw calls, primitive assembly, and the first pipeline handoff*

Original slide anchors: **22–33**.

## Solution and reasoning

### 1. What is in the VBO?

The VBO contains the raw vertex bytes:

```text
x y z r g b | x y z r g b | x y z r g b | ...
```

The VBO does not inherently know that the first three floats mean position and the next three mean color.

### 2. What does the VAO remember?

The VAO remembers the vertex input configuration: how the bytes from currently associated buffers should be interpreted as vertex attributes.

The useful mental distinction is:

```text
VBO = data
VAO = interpretation/setup of that data
```

### 3. Stride

One vertex contains six floats:

\[
\text{stride}=6\cdot sizeof(float).
\]

Both attributes use the same stride because the next position and the next color both begin one complete vertex record later.

### 4. Position offset

Position begins at the first byte of the vertex:

```text
offset = 0
```

### 5. Color offset

Color begins after three floats:

\[
\text{offset}=3\cdot sizeof(float).
\]

### 6. Meaning of `glVertexAttribPointer`

It tells OpenGL:

> When the vertex shader asks for this attribute location, interpret the bound vertex-buffer memory using this component count, type, stride, and offset.

A plausible setup is:

```cpp
glBindVertexArray(vao);
glBindBuffer(GL_ARRAY_BUFFER, vbo);

glBufferData(GL_ARRAY_BUFFER,
             sizeof(vertices),
             vertices,
             GL_STATIC_DRAW);

// location 0: vec3 position
glVertexAttribPointer(
    0,                      // attribute location
    3,                      // x, y, z
    GL_FLOAT,
    GL_FALSE,
    6 * sizeof(float),      // full vertex stride
    reinterpret_cast<void*>(0)
);
glEnableVertexAttribArray(0);

// location 1: vec3 color
glVertexAttribPointer(
    1,
    3,
    GL_FLOAT,
    GL_FALSE,
    6 * sizeof(float),
    reinterpret_cast<void*>(3 * sizeof(float))
);
glEnableVertexAttribArray(1);
```

## Why this connects to the lecture

Lecture 2 explains that the GPU receives **bytes**, not your C++ notion of a `Vertex` object. The VAO is what makes those bytes meaningful to the vertex shader.

## Common mistake

Thinking that the VAO stores the actual vertex data. In this mental model, it does not replace the VBO; it stores the vertex-input configuration.

---

# Task 3 — Primitive assembly and draw calls

## Reconstructed exercise text

Assume a VBO contains 12 sequential vertex records.

For each draw call below, explain how OpenGL interprets the vertex stream conceptually:

```cpp
glDrawArrays(GL_TRIANGLES, 0, 12);
glDrawArrays(GL_LINES,     0, 12);
```

Then answer:

1. How many independent triangles can `GL_TRIANGLES` form from 12 vertices?
2. How many independent lines can `GL_LINES` form from 12 vertices?
3. Why can the exact same vertex data produce a different geometric result merely by changing the primitive mode?
4. Why does primitive assembly logically happen after vertex processing but before rasterization?

## What you must already know

Lecture 2:

- Section 2 — vertex vs primitive
- Section 6 — draw calls and primitive assembly

Original slide anchors: **27–36**.

## Solution and reasoning

For `GL_TRIANGLES`, vertices are consumed in groups of three:

```text
(0,1,2)  → triangle 1
(3,4,5)  → triangle 2
(6,7,8)  → triangle 3
(9,10,11)→ triangle 4
```

So 12 vertices form **4 independent triangles**.

For `GL_LINES`, vertices are consumed in pairs:

```text
(0,1)   → line 1
(2,3)   → line 2
...
(10,11) → line 6
```

So 12 vertices form **6 independent lines**.

The same bytes can produce different geometry because the draw mode tells primitive assembly **how to group processed vertices**.

Primitive assembly must happen after vertex processing because each vertex first needs its processed position and outputs. It must happen before rasterization because rasterization needs complete primitives—e.g. a triangle—not unrelated isolated vertices.

## Core connection

```text
vertex shader invocations
        ↓
processed vertices
        ↓
primitive assembly
        ↓
triangles / lines / points
        ↓
rasterization
```

---

# Task 4 — Attribute, uniform, varying, and shader flow

## Reconstructed exercise text

Consider the following simplified shader pair:

```glsl
// vertex shader
layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aColor;

uniform mat4 uMVP;

out vec3 vColor;

void main() {
    gl_Position = uMVP * vec4(aPos, 1.0);
    vColor = aColor;
}
```

```glsl
// fragment shader
in vec3 vColor;
out vec4 FragColor;

void main() {
    FragColor = vec4(vColor, 1.0);
}
```

Explain the role of:

- `aPos`
- `aColor`
- `uMVP`
- `vColor`
- `gl_Position`
- `FragColor`

Then explain what happens to `vColor` for a fragment in the middle of a triangle whose vertices have different colors.

## What you must already know

Lecture 2:

- Section 7 — coordinate systems and clip space
- Section 8 — shaders, attributes, uniforms, varyings
- Section 9 — rasterization and interpolation

Original slide anchors: **46–64**.

## Solution and reasoning

### `aPos`

A **vertex attribute**. It changes from vertex to vertex and comes from the vertex input configuration/buffer data.

### `aColor`

Another vertex attribute. Each vertex may carry a different color.

### `uMVP`

A **uniform** matrix supplied by the application. During one draw it is typically shared by all relevant vertex shader invocations.

Its purpose is to transform local/object-space positions through the relevant model/view/projection chain into clip-space coordinates.

### `vColor`

A value passed from the vertex shader toward the fragment shader.

For a triangle, the rasterizer interpolates it between the vertex values.

### `gl_Position`

The required clip-space output position of a vertex shader.

It is consumed by later fixed-function geometry processing.

### `FragColor`

A fragment shader output that contributes to a framebuffer color attachment if the fragment survives the relevant operations/tests.

### What happens in the middle of the triangle?

Suppose the vertices are red, green, and blue. The fragment in the interior does not normally receive one of the original colors unchanged. Rasterization interpolates `vColor` according to the fragment's location in the triangle.

So conceptually:

```text
vertex colors
    ↓
interpolation across primitive
    ↓
per-fragment vColor
    ↓
fragment shader
    ↓
FragColor
```

## Important connection to Lecture 6

Lecture 2 introduces interpolation as part of the pipeline. Lecture 6 later explains rasterization and interpolation in much greater algorithmic detail.

If interpolation feels mysterious here, it is **not a new unrelated topic**; it is a preview of Lecture 6.

---

# Task 5 — Follow one vertex through coordinate systems

## Reconstructed exercise text

A vertex starts in a cube's local coordinate system at

\[
p_{local}=(0.5,0.5,0.5,1)^T.
\]

The application uses matrices `M`, `V`, and `P` for model, view, and projection transformations.

Answer:

1. Write the expression for the clip-space position.
2. Explain what each matrix conceptually changes.
3. What happens after the vertex shader has produced the clip-space coordinate?
4. What is the role of perspective division?
5. What is the role of `glViewport`?

You do **not** need to multiply concrete matrices for this task; explain the representation changes.

## What you must already know

Lecture 2:

- Section 7 — *Coordinate systems before projection and clip space*

Also connected to later chapters:

- Lecture 3 — geometric transformations
- Lecture 4 — geometric projection

This is an especially important example of how one exercise topic points forward into later lectures.

## Solution and reasoning

The standard conceptual chain is

\[
p_{clip}=PVMp_{local}.
\]

(Exact multiplication convention depends on the course's vector/matrix convention; here the column-vector convention is assumed.)

### Model matrix `M`

Transforms the vertex from the object's own local coordinates into world coordinates.

### View matrix `V`

Transforms world coordinates into the camera/view coordinate system.

### Projection matrix `P`

Transforms view-space coordinates into clip-space homogeneous coordinates.

After clipping, perspective division converts homogeneous clip coordinates to normalized device coordinates:

\[
(x_{ndc},y_{ndc},z_{ndc})
=
\left(\frac{x_c}{w_c},\frac{y_c}{w_c},\frac{z_c}{w_c}\right).
\]

The viewport transform then maps normalized coordinates into a screen/window region.

`glViewport(x,y,width,height)` specifies that target rectangle.

Conceptually:

```text
local
↓ M
world
↓ V
view/camera
↓ P
clip
↓ clipping + perspective division
NDC
↓ viewport transform
window/screen coordinates
```

## Where to look it up

If you understand the names but not **why** the matrices work, Lecture 3 is the place to revisit transformations and Lecture 4 is the place to revisit projection. Lecture 2 only establishes the pipeline location and dependency order.

---

# Task 6 — Fragment depth and the framebuffer

## Reconstructed exercise text

Two opaque triangles overlap at one framebuffer sample.

The first triangle produces a fragment with depth `0.65` and blue color.

The second triangle produces a fragment with depth `0.20` and red color.

Assume:

```cpp
glEnable(GL_DEPTH_TEST);
glDepthFunc(GL_LESS);
```

and the depth buffer has been cleared to `1.0`.

Answer:

1. What happens if the blue fragment is processed first?
2. What happens when the red fragment is processed afterward?
3. What final color/depth remains?
4. Why does this illustrate the statement that a fragment is not a pixel?
5. Which later lecture studies this idea in depth?

## What you must already know

Lecture 2:

- Sections on fragments, fragment tests, framebuffer, depth buffer
- Source anchors: **68–85**

Strong forward link:

- Lecture 7 — Visibility Determination

## Solution and reasoning

Initially:

```text
depth buffer = 1.0
```

Blue fragment:

```text
0.65 < 1.0 → pass
```

So the framebuffer becomes approximately:

```text
color = blue
depth = 0.65
```

Red fragment:

```text
0.20 < 0.65 → pass
```

So it replaces the previous contribution:

```text
color = red
depth = 0.20
```

Final result: **red**, depth **0.20**.

The blue fragment existed. It was a real fragment candidate and temporarily even updated the framebuffer. But it was not guaranteed to be the final visible pixel value.

This is exactly why the vocabulary matters:

```text
fragment = candidate contribution
pixel/framebuffer value = stored result after pipeline operations
```

Lecture 7 later turns this into a complete visibility topic through z-buffering and other hidden-surface algorithms.

---

# Task 7 — Debug a broken draw call conceptually

## Reconstructed exercise text

A program executes:

```cpp
glUseProgram(program);
glBindVertexArray(vao);
glDrawArrays(GL_TRIANGLES, 0, 3);
```

but nothing appears.

List at least **six conceptually different causes** from the rendering pipeline. For each one, say which stage/resource you would inspect.

## What you must already know

Lecture 2 as a whole, especially Sections 4–9.

This task is important because it tests whether you understand OpenGL as a **stateful pipeline**, rather than as a collection of commands to memorize.

## Solution and reasoning

Possible causes include:

### 1. Vertex data was never uploaded correctly

Inspect VBO contents / `glBufferData`.

Pipeline location: **vertex input preparation**.

### 2. VAO attribute layout is wrong

Wrong stride, offset, type, or disabled attribute.

Pipeline location: **vertex input interpretation**.

### 3. Shader input locations do not match the VAO

For example, the VAO supplies position at location 0 but the shader expects another location.

Pipeline location: **vertex input → vertex shader interface**.

### 4. Vertex shader transforms geometry outside the clip volume

For example, a bad `uMVP` matrix.

Pipeline location: **vertex shader / coordinate transformations**.

### 5. Triangle is clipped or culled

Its geometry may not survive the geometric stages.

Pipeline location: **clipping / culling**.

### 6. Fragment shader output is invisible

Perhaps alpha/color is wrong or shader logic discards fragments.

Pipeline location: **fragment shader**.

### 7. Depth testing rejects the fragments

Stale depth buffer, wrong comparison, or unexpected depth values.

Pipeline location: **fragment tests**.

### 8. Viewport is wrong

For example, width/height were never updated after framebuffer resize.

Pipeline location: **viewport transform**.

### 9. Wrong framebuffer is bound

Rendering may be going somewhere other than the visible default framebuffer.

Pipeline location: **framebuffer/output**.

### 10. Wrong primitive/count

The draw call may not supply enough vertices or may use an unintended primitive mode.

Pipeline location: **primitive assembly**.

## The real lesson

A draw call is not “draw this triangle.” It means:

> Run the current vertex range through the current OpenGL state and current pipeline configuration.

That is why debugging should follow the pipeline in order.

---

# Task 8 — Build the complete explanation from CPU to screen

## Reconstructed exercise text

Explain what happens after a C++ application decides to render one colored triangle. Your answer must correctly use all of the following terms:

- CPU application
- VBO
- VAO
- vertex attribute
- draw call
- vertex shader
- `gl_Position`
- primitive assembly
- clipping
- perspective division
- viewport
- rasterization
- interpolation
- fragment
- fragment shader
- depth test
- framebuffer

## What you must already know

This is the **integration task** for the whole Lecture 2 reader.

If you cannot answer one segment, use the mapping below:

```text
CPU/OpenGL state            → Lecture 2 §4
VBO/VAO/attributes          → Lecture 2 §5
Draw call/primitive assembly→ Lecture 2 §6
Coordinate systems          → Lecture 2 §7
Shaders/uniforms/varyings   → Lecture 2 §8
Rasterization/fragments     → Lecture 2 §9
Depth/framebuffer           → Lecture 2 later fragment-test/framebuffer sections
```

## Model solution

The CPU application prepares scene state and vertex data. The triangle's vertex records are uploaded into a VBO. A VAO describes how the bytes in that buffer map to vertex attributes such as position and color.

The application activates the desired shader program, binds the VAO, sets uniforms such as transformation matrices, and issues a draw call.

For every input vertex, the vertex shader reads the configured attributes. It transforms the position and writes the clip-space result to `gl_Position`; it may also output values such as color to be interpolated later.

Primitive assembly groups the processed vertices according to the selected draw mode, for example three vertices into one triangle.

The primitive is clipped against the viewable region. After the relevant homogeneous processing, perspective division converts clip coordinates into normalized device coordinates. The viewport transform maps them into the configured window region.

Rasterization determines which discrete framebuffer samples are covered by the triangle and generates fragments. Varying vertex outputs are interpolated across the triangle so every fragment receives appropriate intermediate values.

The fragment shader computes outputs such as color for each fragment. Fragment tests such as the depth test determine whether the candidate is allowed to update the framebuffer. Surviving fragments modify framebuffer attachments such as color and depth.

That stored framebuffer color can ultimately become the image displayed on screen.

---

# Knowledge map — where each Exercise 1 idea comes from

| Exercise idea | Main Lecture 2 source | Later lecture that deepens it |
|---|---|---|
| vertex → primitive → fragment → pixel | §§1–3, 9 | Lecture 6 Rasterization |
| VBO / VAO | §5 | mostly implementation context |
| draw calls / primitive modes | §6 | Lecture 6 for rasterization behavior |
| local/world/view/clip coordinates | §7 | Lecture 3 + Lecture 4 |
| model/view/projection matrices | §7 | Lecture 3 + Lecture 4 |
| vertex shader | §8 | used throughout later OpenGL topics |
| attributes / uniforms / varyings | §8 | Lectures 8–10 use them heavily |
| interpolation | §§8–9 | Lecture 6 |
| fragments | §§2, 9 | Lectures 6–10 |
| depth test | fragment-test section | Lecture 7 Visibility |
| framebuffer | framebuffer section | Lecture 7 + shadow mapping in Lecture 10 |

---

# What this sheet cannot claim

Because the original Exercise 1 attachment is absent from the repository, I cannot reliably claim that the official sheet asked exactly these questions, used these numbers, or expected these code fragments.

What **is** reliable is that every concept and solution above is grounded in the official Rendering Pipeline lecture and the course's stated C/C++/OpenGL practical context.

If the original sheet becomes available, the next version should have the following structure for each official subtask:

```text
ORIGINAL TASK TEXT
↓
WHAT THE TASK IS TESTING
↓
LECTURE LINK / SECTION / SLIDE ANCHOR
↓
PREREQUISITES
↓
SOLUTION STRATEGY
↓
FULL SOLUTION
↓
WHY IT WORKS
↓
COMMON MISTAKES
↓
A VARIANT TO SOLVE YOURSELF
```
