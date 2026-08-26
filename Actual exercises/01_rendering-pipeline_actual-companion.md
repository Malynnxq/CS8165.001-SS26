# Actual Exercise 1 — Rendering Pipeline

> **Grounding.** This companion is based on the **original Exercise 1 package now present in the repository**, especially `assignment_sources/exercise-01/Exercise1/glframework/src/main.cpp` and its shader/framework files. The original PDF is also present in the package, but GitHub exposes that file as binary; therefore I do **not** reproduce PDF wording I cannot verify character-for-character. Wherever I say “the task requires…”, I am referring to requirements that are directly visible in the supplied starter code/TODOs.
>
> **Do not confuse this with the reconstructed sheet.** The older `exercise_readers_v2/01_rendering-pipeline_exercise-companion.md` remains untouched. This file belongs to the separate **Actual exercises** directory and is tied to the real starter framework.

---

# 1. What the actual starter code asks you to do

The original `main.cpp` contains these explicit TODOs:

1. Replace the placeholder triangle in `createCubeVertices()` with a **cube**, including colors and correct face normals.
2. Correct the number of vertices passed to `glDrawArrays()` for the cube.
3. Create an initial **tetrahedron with four vertices**.
4. Subdivide each tetrahedron into **four smaller tetrahedra** recursively.
5. Compute correct normals for all four faces of each generated tetrahedron.
6. Correct the number of vertices passed to `glDrawArrays()` for the fractal tetrahedron.

The framework already gives you the rendering machinery:

```text
C++ vertex structures
↓
VBO / VAO creation
↓
vertex attributes
↓
MVP matrix
↓
vertex shader
↓
triangle primitive assembly
↓
rasterization
↓
fragment shader
↓
depth test + back-face culling
↓
framebuffer
```

So Exercise 1 is not asking you to write an OpenGL renderer from zero. It is asking you to understand enough of the rendering pipeline to **feed the pipeline correct geometry and attributes**.

---

# 2. Lecture map — what knowledge is already yours?

Before solving the code, map each requirement to the lecture material.

| Actual Exercise 1 requirement | Lecture knowledge |
|---|---|
| `vertex` contains position / texcoord / normal / color | Lecture 2: vertex attributes |
| VAO and VBO setup | Lecture 2 §5 |
| `glVertexAttribPointer` | Lecture 2 §5 |
| `GL_TRIANGLES` | Lecture 2 §6 |
| one cube face = two triangles | Lecture 2 primitive assembly + basic geometry |
| counter-clockwise vertex order | Lecture 2 primitive orientation; later Lecture 7 back-face culling |
| normals via cross product | developed fully in Lecture 3 |
| MVP matrix | Lecture 2 overview, Lecture 3 model/view, Lecture 4 projection |
| recursive tetrahedron subdivision | programming logic + geometric midpoint construction |
| `glEnable(GL_CULL_FACE)` | later explained fully in Lecture 7 |
| `glEnable(GL_DEPTH_TEST)` | later explained fully in Lecture 7 |

The useful mental distinction is:

```text
Lecture 2 tells you how vertex data reaches the GPU.
Lecture 3 gives you vector/cross-product tools.
Lecture 7 later explains why winding and depth state matter.
```

You do **not** need to have studied Lecture 7 first to complete the framework, because the relevant OpenGL state is already written for you. But later Lecture 7 explains the reason behind it.

---

# 3. Read the provided `vertex` structure first

The starter code defines

```cpp
struct vertex
{
    glm::vec3 position;
    glm::vec2 texcoord;
    glm::vec3 normal;
    glm::vec3 color;
};
```

This is one complete vertex record.

A vertex is therefore not “just xyz”. In this framework one vertex can carry:

```text
position → where the corner is
texcoord → where it would sample a texture
normal   → which direction the surface faces
color    → per-vertex color
```

The exercise does not use texture coordinates meaningfully yet, so `glm::vec2()` is acceptable for them in these tasks.

## Lecture connection

Go back to **Lecture 2 §5 — VBO / VAO / attributes** if this structure feels arbitrary.

The VBO stores a sequence like

```text
[position texcoord normal color]
[position texcoord normal color]
[position texcoord normal color]
...
```

The VAO tells OpenGL how to interpret that memory.

---

# 4. Understand the VAO setup before changing geometry

The framework already contains

```cpp
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE,
                      sizeof(vertex),
                      (void*)offsetof(vertex, position));

glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE,
                      sizeof(vertex),
                      (void*)offsetof(vertex, texcoord));

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE,
                      sizeof(vertex),
                      (void*)offsetof(vertex, normal));

glVertexAttribPointer(3, 3, GL_FLOAT, GL_FALSE,
                      sizeof(vertex),
                      (void*)offsetof(vertex, color));
```

You do **not** need to change this for the cube or tetrahedron.

Why?

Because every generated vertex uses the same `vertex` structure. Only the **values** inside each record change.

This separation is fundamental:

```text
VAO = format / interpretation
VBO = actual array of records
```

---

# 5. Actual Task A — Build the cube

The starter currently contains only three vertices:

```cpp
// TODO: create a cube here instead of a triangle and apply colors and correct normals
```

A cube has:

- 6 square faces;
- each square is represented as 2 triangles;
- each triangle needs 3 submitted vertices when using non-indexed `GL_TRIANGLES`.

Therefore

\[
6\cdot2\cdot3=36
\]

vertex records are needed in this framework.

## Why not only 8 vertices?

Geometrically a cube has eight corner positions.

But the framework stores the **normal as part of the vertex record**.

At a sharp cube corner, the same geometric position belongs to three different faces with three different face normals.

Therefore the corner cannot be represented by one single shared `(position, normal)` record if we want flat faces.

This is a very important graphics distinction:

```text
geometric point ≠ necessarily one GPU vertex record
```

A GPU “vertex” is a bundle of attributes.

---

# 6. Choose the eight cube corner positions

A convenient unit cube centered at the origin uses coordinates `±1`:

```cpp
glm::vec3 p000(-1,-1,-1);
glm::vec3 p001(-1,-1, 1);
glm::vec3 p010(-1, 1,-1);
glm::vec3 p011(-1, 1, 1);
glm::vec3 p100( 1,-1,-1);
glm::vec3 p101( 1,-1, 1);
glm::vec3 p110( 1, 1,-1);
glm::vec3 p111( 1, 1, 1);
```

The names are only mnemonic: each digit indicates which side of x/y/z the point belongs to.

---

# 7. Why winding order matters

The program enables

```cpp
glEnable(GL_CULL_FACE);
glCullFace(GL_BACK);
glFrontFace(GL_CCW);
```

This means front-facing triangles must appear **counter-clockwise** from their outward side.

So if one cube face is accidentally specified clockwise, OpenGL may classify it as a back face and discard it.

This is why you cannot list triangle corners in arbitrary order.

## Lecture connection

The full reason is in **Lecture 7 — back-face culling**.

For now remember:

```text
CCW order → determines front side
cross-product order → determines normal direction
```

These must agree.

---

# 8. Correct cube normals

A cube has constant face normals:

```text
right  : (+1, 0, 0)
left   : (-1, 0, 0)
top    : ( 0,+1, 0)
bottom : ( 0,-1, 0)
front  : ( 0, 0,+1)
back   : ( 0, 0,-1)
```

You can either assign these directly or calculate them with the provided helper:

```cpp
glm::vec3 calculateNormal(a,b,c)
{
    glm::vec3 ab = b - a;
    glm::vec3 ac = c - a;
    glm::vec3 n = glm::cross(ab, ac);
    return glm::normalize(n);
}
```

The cross product

\[
(b-a)\times(c-a)
\]

is perpendicular to the triangle.

Swapping two vertices reverses the normal.

---

# 9. A clean cube implementation

One readable solution is to use a helper that emits two triangles for one face.

```cpp
std::vector<vertex> createCubeVertices()
{
    std::vector<vertex> vertices;

    const glm::vec3 p000(-1,-1,-1);
    const glm::vec3 p001(-1,-1, 1);
    const glm::vec3 p010(-1, 1,-1);
    const glm::vec3 p011(-1, 1, 1);
    const glm::vec3 p100( 1,-1,-1);
    const glm::vec3 p101( 1,-1, 1);
    const glm::vec3 p110( 1, 1,-1);
    const glm::vec3 p111( 1, 1, 1);

    auto addFace = [&](glm::vec3 a,
                       glm::vec3 b,
                       glm::vec3 c,
                       glm::vec3 d,
                       glm::vec3 color)
    {
        // a,b,c,d must be ordered CCW as seen from outside.
        glm::vec3 n = calculateNormal(a,b,c);

        vertices.push_back({a, {}, n, color});
        vertices.push_back({b, {}, n, color});
        vertices.push_back({c, {}, n, color});

        vertices.push_back({a, {}, n, color});
        vertices.push_back({c, {}, n, color});
        vertices.push_back({d, {}, n, color});
    };

    // +Z front
    addFace(p001, p101, p111, p011, glm::vec3(1,0,0));

    // -Z back
    addFace(p100, p000, p010, p110, glm::vec3(0,1,0));

    // +X right
    addFace(p101, p100, p110, p111, glm::vec3(0,0,1));

    // -X left
    addFace(p000, p001, p011, p010, glm::vec3(1,1,0));

    // +Y top
    addFace(p011, p111, p110, p010, glm::vec3(1,0,1));

    // -Y bottom
    addFace(p000, p100, p101, p001, glm::vec3(0,1,1));

    return vertices;
}
```

## About the colors

The starter explicitly asks for colors, but the exact PDF color scheme is not text-accessible through the connector. The distinct face colors above are therefore a **valid explanatory example**, not a claim about a mandated color palette.

If the PDF illustration specifies particular colors, replace only the `color` arguments; the geometry reasoning stays the same.

---

# 10. Correct cube draw count

The starter says

```cpp
glDrawArrays(GL_TRIANGLES, 0, 3);
// TODO: Set the correct number of vertices to be rendered
```

For the cube implementation above:

\[
6\text{ faces}\times2\text{ triangles}\times3\text{ vertices}=36.
\]

So either write

```cpp
glDrawArrays(GL_TRIANGLES, 0, 36);
```

or, much better, use the count already stored in the VAO wrapper:

```cpp
glDrawArrays(GL_TRIANGLES, 0, cubaVAO.vertexCount);
```

The second solution cannot silently break if you later change the mesh size.

## Lecture connection

Lecture 2 §6: with `GL_TRIANGLES`, every consecutive group of three processed vertices forms one triangle.

---

# 11. What the cube task is really testing

It looks like a “make a cube” programming task, but conceptually it tests all of these:

```text
How is geometry represented as vertex records?
How do triangles form surfaces?
Why are sharp-edge normals duplicated?
Why does winding order matter?
How many vertices does a draw call consume?
How does the same generic pipeline render a new mesh?
```

That is exactly why it belongs to a rendering-pipeline exercise.

---

# 12. Actual Task B — Build the initial tetrahedron

The starter contains

```cpp
tetrahedron initialTetrahedron{};

// TODO: create a tetrahedron containing 4 vertices.
```

A tetrahedron is a polyhedron with:

- 4 vertices;
- 4 triangular faces.

A convenient regular tetrahedron centered around the origin can use

```cpp
initialTetrahedron[0] = {
    glm::vec3(-1,-1,-1), {}, {}, glm::vec3(1,0,0)
};
initialTetrahedron[1] = {
    glm::vec3( 1, 1,-1), {}, {}, glm::vec3(0,1,0)
};
initialTetrahedron[2] = {
    glm::vec3( 1,-1, 1), {}, {}, glm::vec3(0,0,1)
};
initialTetrahedron[3] = {
    glm::vec3(-1, 1, 1), {}, {}, glm::vec3(1,1,0)
};
```

These four points form a regular tetrahedral arrangement.

The starter later defines its faces as

```text
0,1,2
0,2,3
0,3,1
1,3,2
```

With the coordinate order above, these face orderings point outward consistently.

---

# 13. The recursive fractal idea

The function is

```cpp
splitFractalTetrahedron(std::vector<tetrahedron> tetrahedra,
                        int depth = 0)
```

For each tetrahedron, the TODO says:

```cpp
// TODO: Subdivide tetrahedron to create 4 new ones.
```

This is the tetrahedral analogue of a Sierpiński-style fractal subdivision.

Take one tetrahedron with vertices

```text
A, B, C, D
```

Calculate the six edge midpoints:

```text
AB, AC, AD, BC, BD, CD
```

Then keep four corner tetrahedra:

```text
at A: A, AB, AC, AD
at B: AB, B, BC, BD
at C: AC, BC, C, CD
at D: AD, BD, CD, D
```

The central tetrahedral region is omitted.

That omission creates the fractal holes.

---

# 14. Why `vertexLerp` works for the midpoint use case

The starter includes

```cpp
vertex vertexLerp(vertex a, vertex b, float t)
{
    vertex c{};
    c.position = (a.position + b.position) * t;
    c.texcoord = (a.texcoord + b.texcoord) * t;
    c.normal = (a.normal+ b.normal) * t;
    c.color = (a.color + b.color) * t;
    return c;
}
```

This is **not a general linear interpolation formula**.

The general formula should be

\[
(1-t)a+tb.
\]

However, if this exercise uses only

\[
t=0.5,
\]

then

\[
(a+b)\cdot0.5
\]

is exactly the midpoint.

So for subdivision you can safely call

```cpp
vertexLerp(a,b,0.5f)
```

for every edge.

If you wanted a generally correct helper, rewrite it as

```cpp
c.position = (1.0f - t) * a.position + t * b.position;
c.texcoord = (1.0f - t) * a.texcoord + t * b.texcoord;
c.normal   = (1.0f - t) * a.normal   + t * b.normal;
c.color    = (1.0f - t) * a.color    + t * b.color;
```

For this fractal, interpolating the endpoint colors also naturally gives midpoint colors.

---

# 15. Correct tetrahedron subdivision

Inside the loop, name the parent vertices:

```cpp
const vertex& A = th[0];
const vertex& B = th[1];
const vertex& C = th[2];
const vertex& D = th[3];
```

Create midpoints:

```cpp
vertex AB = vertexLerp(A, B, 0.5f);
vertex AC = vertexLerp(A, C, 0.5f);
vertex AD = vertexLerp(A, D, 0.5f);
vertex BC = vertexLerp(B, C, 0.5f);
vertex BD = vertexLerp(B, D, 0.5f);
vertex CD = vertexLerp(C, D, 0.5f);
```

Then the four new tetrahedra are

```cpp
splitTetrahedra[0] = { A,  AB, AC, AD };
splitTetrahedra[1] = { AB, B,  BC, BD };
splitTetrahedra[2] = { AC, BC, C,  CD };
splitTetrahedra[3] = { AD, BD, CD, D  };
```

## Why exactly four?

Each child occupies one corner of the parent tetrahedron.

The construction repeatedly shrinks the geometry while preserving the four corner regions.

---

# 16. Understand the recursion depth

The starter executes

```cpp
if (depth < 5)
    return splitFractalTetrahedron(result, depth + 1);
```

The initial call uses `depth = 0`.

At every level, one tetrahedron becomes four.

So after `k` subdivision rounds, the count is

\[
4^k.
\]

Because the code performs a split at depth 0 and continues while the previous depth is below 5, you should trace the exact calls rather than casually say “depth 5 means 4^5”.

Call sequence:

```text
depth 0 → split
call depth 1
↓
depth 1 → split
...
depth 5 → split
then stop
```

That means six subdivision rounds from the initial input, producing

\[
4^6=4096
\]

small tetrahedra.

Each tetrahedron contributes 4 faces × 3 vertices = 12 submitted triangle vertices, so the final vertex list has

\[
4096\cdot12=49152
\]

vertex records.

This is a good example of why recursion can generate geometry very rapidly.

---

# 17. Actual Task C — Compute face normals

The starter emits the tetrahedron faces in four groups:

```cpp
0,1,2
0,2,3
0,3,1
1,3,2
```

but currently sets

```cpp
glm::vec3 normal = glm::vec3();
```

which is the zero vector.

The TODO explicitly asks for correct normals.

Use the supplied helper for each face:

```cpp
glm::vec3 normal = calculateNormal(
    tetrahedron[0].position,
    tetrahedron[1].position,
    tetrahedron[2].position
);
```

Then assign that same face normal to all three submitted vertices of the triangle.

Repeat for the other three faces.

---

# 18. Full corrected face-normal section

```cpp
for (const auto& tetrahedron : FractalTetrahedra)
{
    glm::vec3 normal;

    normal = calculateNormal(
        tetrahedron[0].position,
        tetrahedron[1].position,
        tetrahedron[2].position
    );
    vertices.push_back(tetrahedron[0]); vertices.back().normal = normal;
    vertices.push_back(tetrahedron[1]); vertices.back().normal = normal;
    vertices.push_back(tetrahedron[2]); vertices.back().normal = normal;

    normal = calculateNormal(
        tetrahedron[0].position,
        tetrahedron[2].position,
        tetrahedron[3].position
    );
    vertices.push_back(tetrahedron[0]); vertices.back().normal = normal;
    vertices.push_back(tetrahedron[2]); vertices.back().normal = normal;
    vertices.push_back(tetrahedron[3]); vertices.back().normal = normal;

    normal = calculateNormal(
        tetrahedron[0].position,
        tetrahedron[3].position,
        tetrahedron[1].position
    );
    vertices.push_back(tetrahedron[0]); vertices.back().normal = normal;
    vertices.push_back(tetrahedron[3]); vertices.back().normal = normal;
    vertices.push_back(tetrahedron[1]); vertices.back().normal = normal;

    normal = calculateNormal(
        tetrahedron[1].position,
        tetrahedron[3].position,
        tetrahedron[2].position
    );
    vertices.push_back(tetrahedron[1]); vertices.back().normal = normal;
    vertices.push_back(tetrahedron[3]); vertices.back().normal = normal;
    vertices.push_back(tetrahedron[2]); vertices.back().normal = normal;
}
```

## Why one normal for all three vertices?

Because this exercise constructs a flat triangular face.

A constant face normal means the complete triangle represents one planar orientation.

Later in Lecture 8, you learn why smooth meshes may instead use averaged per-vertex normals.

---

# 19. Correct tetrahedron draw count

The starter currently says

```cpp
glDrawArrays(GL_TRIANGLES, 0, 0);
// TODO: Set the correct number of vertices to be rendered
```

Again, do not hard-code a number if you already stored the count:

```cpp
glDrawArrays(GL_TRIANGLES, 0, tetrahedronVAO.vertexCount);
```

This is safer and directly expresses the intent:

> Render every vertex record that was uploaded into this VAO/VBO mesh.

---

# 20. Why the shader and MVP code are already important

The framework computes

```cpp
glm::mat4 m = glm::mat4(1.0f);
glm::mat4 v = glframework::getCamera();
glm::mat4 p = glm::perspective(
    glm::radians(30.0f),
    (float)width / (float)height,
    0.1f,
    10.0f
);
glm::mat4 mvp = p * v * m;
```

and sends it to the shader:

```cpp
glUniformMatrix4fv(mvpLocation, 1, GL_FALSE,
                   glm::value_ptr(mvp));
```

You do not need to derive the perspective matrix for Exercise 1.

But you should understand the dependency chain:

```text
model coordinates
↓ M
world coordinates
↓ V
camera/view coordinates
↓ P
clip coordinates
```

The vertex shader then uses the matrix to produce `gl_Position`.

## Lecture connection

- Lecture 2: know that the vertex shader outputs `gl_Position`.
- Lecture 3: understand M and V transformations.
- Lecture 4: understand P and perspective projection.

Exercise 1 gives you the machinery before the later lectures derive all of it mathematically.

---

# 21. Why depth testing matters even in Exercise 1

The code enables

```cpp
glEnable(GL_DEPTH_TEST);
glDepthFunc(GL_LESS);
```

and clears

```cpp
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
```

every frame.

Without a depth test, the visible result could depend incorrectly on triangle draw order.

With depth testing, the closest fragment at each sample can win.

You do not have to implement depth testing; OpenGL does it.

## Lecture connection

This is fully explained in **Lecture 7 — Visibility Determination**.

For Exercise 1, it is enough to recognize that it lets the cube and tetrahedron behave as opaque 3D objects instead of a flat stack of triangles.

---

# 22. Why back-face culling matters

The code also enables

```cpp
glEnable(GL_CULL_FACE);
glCullFace(GL_BACK);
glFrontFace(GL_CCW);
```

For a closed opaque cube/tetrahedron, the back-facing triangles are normally unnecessary.

But this optimization only works if your winding is consistent.

This is why a “missing face” during debugging often means:

```text
wrong winding
not necessarily wrong coordinates
```

A quick diagnostic is temporarily disabling culling. If the face reappears, investigate triangle order.

---

# 23. Debugging checklist for the actual assignment

If the **cube is malformed**:

- verify all six faces exist;
- verify two triangles per face;
- check 36 total records;
- check CCW winding from outside;
- verify normals point outward;
- temporarily disable culling to isolate winding problems.

If the **tetrahedron is invisible**:

- check that the initial four vertices are non-degenerate;
- check face winding;
- check `glDrawArrays` count;
- check that recursive children are actually assigned;
- inspect whether positions remain inside the camera's view.

If the **fractal explodes or collapses**:

- verify every edge midpoint uses the intended two endpoints;
- verify every child tetrahedron uses one original corner plus its three adjacent midpoints;
- check recursion termination.

If **lighting/normals look wrong**:

- calculate face normals using positions in the same CCW order used for drawing;
- normalize the cross product;
- remember that the zero normal is invalid for meaningful directional lighting.

---

# 24. What C++ knowledge is actually required here?

This real Exercise 1 gives us much better evidence about the programming level expected by the practical course.

You need to be comfortable reading:

- `struct` definitions;
- `std::vector`;
- `std::array`;
- references and `const auto&`;
- loops;
- recursion;
- functions;
- basic lambda syntax if you use the optional cube helper;
- object/field access such as `.position`;
- OpenGL function calls.

But the **graphics reasoning** remains the difficult part:

```text
which vertices?
which triangles?
which winding?
which normals?
which vertex count?
which child tetrahedra?
```

You do not need advanced C++ template metaprogramming or sophisticated object-oriented design to understand this sheet.

---

# 25. Exam relevance: what this practical sheet reinforces

Even if the written exam never asks you to type a whole C++ program, this exercise trains concepts that can be asked theoretically.

You should be able to answer:

1. Why does a non-indexed cube with flat normals often require 36 vertex records instead of eight?
2. What does `GL_TRIANGLES` do with the vertex stream?
3. Why does vertex order affect culling and normals?
4. How is a face normal calculated from three positions?
5. Why must the normal be normalized?
6. What is the relationship between VBO data and VAO attribute layout?
7. Why can one geometric corner need multiple GPU vertices?
8. How many triangles does a tetrahedron contain?
9. How does midpoint subdivision create four child tetrahedra?
10. Why does fractal geometry grow exponentially?
11. What does the MVP matrix do conceptually?
12. Why are depth testing and culling separate operations?

---

# 26. Short derivation exercises from the actual code

## Q1 — Cube triangle count

Six square faces, two triangles each:

\[
6\cdot2=12\text{ triangles}.
\]

Non-indexed triangle list:

\[
12\cdot3=36\text{ vertex records}.
\]

## Q2 — Tetrahedron face count

A tetrahedron has four triangular faces:

\[
4\cdot3=12
\]

submitted records per generated tetrahedron in this framework.

## Q3 — Fractal growth

Each parent generates four children:

\[
N_{k+1}=4N_k.
\]

Thus

\[
N_k=4^kN_0.
\]

## Q4 — Face normal

For CCW triangle `(A,B,C)`,

\[
n=\frac{(B-A)\times(C-A)}{\|(B-A)\times(C-A)\|}.
\]

Swapping B and C gives

\[
-n.
\]

That is why cross-product order and winding are connected.

---

# 27. The complete actual Exercise 1 solution strategy

When solving from scratch, use this order:

```text
1. Read vertex structure.
2. Understand existing VAO/VBO configuration.
3. Construct cube positions.
4. Convert six faces into twelve CCW triangles.
5. Attach one correct outward normal to each face's vertices.
6. Upload and draw all cube vertices.
7. Define four initial tetrahedron vertices.
8. Compute six midpoints for each parent tetrahedron.
9. Assemble four corner tetrahedra.
10. Recurse until the provided depth condition stops.
11. Convert every final tetrahedron into four triangle faces.
12. Compute one face normal for each face.
13. Upload and draw every generated triangle vertex.
14. Use culling/depth-test behavior as debugging information.
```

This order mirrors the data flow of the program rather than the textual order of individual TODO comments.

---

# 28. Final conceptual map

The actual sheet is a compact demonstration of the whole early rendering pipeline:

```text
You create geometry on the CPU
        ↓
positions + colors + normals become vertex records
        ↓
VBO stores those records
        ↓
VAO explains their layout
        ↓
vertex shader transforms positions with MVP
        ↓
GL_TRIANGLES groups every three vertices
        ↓
front/back orientation is determined from winding
        ↓
rasterizer generates fragments
        ↓
depth test resolves visible surfaces
        ↓
fragment shader contributes final color
```

The cube teaches **mesh representation**.

The fractal tetrahedron teaches **procedural geometry generation**.

Normals teach **orientation encoded as an attribute**.

The draw calls teach **primitive assembly**.

Culling and depth state show that even a simple exercise already depends on later visibility concepts.

> **The deepest lesson is that OpenGL does not know what a “cube” or a “fractal tetrahedron” is. You supply a correctly structured stream of vertices and attributes; the rendering pipeline only knows how to transform, assemble, rasterize and process those primitives.**
