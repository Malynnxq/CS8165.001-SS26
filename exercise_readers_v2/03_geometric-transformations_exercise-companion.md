# Exercise Companion 3 — Geometric Transformations

> **Source status.** The repository preserves the Moodle assignment page titled **“Exercise 3: Geometric Transformations”**, but not the original task attachment. Therefore the exercises below are **reconstructed study exercises**, not the professor's original wording. They are derived from the official exercise topic and the corresponding lecture material.
>
> **Purpose.** This companion turns Lecture 3 from something you can recognize into something you can actually calculate with. Every task explicitly states where the required idea was taught, so you can distinguish **new problem-solving practice** from **knowledge you have already processed in the lecture reader**.

---

# 0. The central problem

A model is stored once in convenient local coordinates. Rendering requires us to place, orient and resize it in a scene.

The mathematical pattern is

\[
p' = M p.
\]

But most exam/exercise questions are really asking one of these deeper questions:

- Which transformation is needed?
- In which coordinate system?
- Around which reference point?
- In what order?
- Is the object being transformed, or are coordinates being changed between frames?
- How do we undo the transformation?
- How do we construct an orientation from directions?

## Main lecture connection

**Lecture 3 — Geometric Transformations** is the primary source:

- §2: vectors, matrices, homogeneous coordinates
- §3: translation
- §4: scaling
- §5: rotation
- §6: mirroring and shearing
- §7: composition/order
- §8: transformations around reference points
- §9–10: arbitrary axes, normalization, cross products, basis construction
- §11: coordinate-system changes
- §12: model/view/projection connection
- §13: modeling by transformation reuse

Supporting connections:

- **Lecture 2:** vertex shader and `gl_Position`
- **Lecture 4:** projection matrix after model/view transformations
- **Lecture 8:** normal vectors and why non-uniform scaling needs special treatment

---

# Task 1 — Translation by reasoning before matrices

A point is

\[
p=(2,-1,4).
\]

Translate it by

\[
t=(3,5,-2).
\]

1. Calculate the transformed point directly.
2. Write the corresponding homogeneous point and translation matrix.
3. Verify the same result by matrix multiplication.
4. Find the inverse transformation.

## Lecture connection

Lecture 3 §2–3.

## Solution

Directly,

\[
p'=p+t=(2+3,-1+5,4-2)=(5,4,2).
\]

In homogeneous coordinates,

\[
\tilde p=\begin{bmatrix}2\\-1\\4\\1\end{bmatrix}.
\]

Using column vectors,

\[
T=
\begin{bmatrix}
1&0&0&3\\
0&1&0&5\\
0&0&1&-2\\
0&0&0&1
\end{bmatrix}.
\]

Then

\[
T\tilde p=
\begin{bmatrix}
5\\4\\2\\1
\end{bmatrix}.
\]

The inverse translation negates the displacement:

\[
T^{-1}=T(-3,-5,2).
\]

### What the exercise is really testing

The fourth homogeneous component is not decorative. With `w=1`, the translation column contributes to the point coordinates.

---

# Task 2 — Why points and directions use different w values

Consider the translation matrix from Task 1. Apply it to

\[
\tilde p=(2,-1,4,1)^T
\]

and to the direction

\[
\tilde d=(2,-1,4,0)^T.
\]

Why does translation affect one but not the other?

## Lecture connection

Lecture 3 §2. This also connects to later normal/direction-vector calculations.

## Solution

For a homogeneous vector

\[
(x,y,z,w)^T,
\]

the translated x-coordinate is

\[
x'=x+t_xw.
\]

If `w=1`, translation contributes:

\[
x'=x+t_x.
\]

If `w=0`,

\[
x'=x.
\]

A point represents a **location**, so moving the coordinate-space contents should move it. A direction represents an orientation/displacement without a location, so translating the scene should not alter that direction.

This distinction becomes important later for normals, light directions and camera directions.

---

# Task 3 — Uniform versus non-uniform scaling

Let

\[
p=(2,3,-4).
\]

Calculate the result of scaling by

### A

\[
S=(2,2,2)
\]

### B

\[
S=(2,\tfrac12,-1).
\]

Then state which geometric properties are necessarily preserved.

## Lecture connection

Lecture 3 §4.

## Solution

### A

\[
p'=(4,6,-8).
\]

All dimensions are multiplied by the same magnitude. Shape angles are preserved; lengths are uniformly multiplied by 2.

### B

\[
p'=(4,1.5,4).
\]

Different axes use different scale factors, so this is non-uniform scaling. General lengths and angles are not preserved.

The negative z scale also reflects orientation along z.

### Important connection to Lecture 8

Non-uniform scaling creates a later problem for normal vectors. Simply applying the same model matrix to a normal generally does not preserve perpendicularity. This motivates the **inverse-transpose normal matrix** in illumination calculations.

---

# Task 4 — Standard-axis rotation

Rotate

\[
p=(1,0,0)
\]

by 90° around the z-axis in a right-handed coordinate system.

Use

\[
R_z(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta&0&0\\
\sin\theta&\cos\theta&0&0\\
0&0&1&0\\
0&0&0&1
\end{bmatrix}.
\]

## Lecture connection

Lecture 3 §5.

## Solution

For

\[
\theta=90^\circ,
\]

\[
\cos\theta=0,\qquad\sin\theta=1.
\]

Thus

\[
R_z(90^\circ)
\begin{bmatrix}1\\0\\0\\1\end{bmatrix}
=
\begin{bmatrix}0\\1\\0\\1\end{bmatrix}.
\]

So

\[
(1,0,0)\rightarrow(0,1,0).
\]

The length remains 1 because a pure rotation preserves distances.

---

# Task 5 — Transformation order

Let

\[
p=(1,0,0).
\]

Use:

- a scale by 2 in x;
- a translation by `(3,0,0)`.

Compare:

### A

scale first, then translate;

### B

translate first, then scale.

## Lecture connection

Lecture 3 §7 — one of the most important sections in the course.

## Solution

### A — scale, then translate

First:

\[
(1,0,0)\rightarrow(2,0,0).
\]

Then:

\[
(2,0,0)\rightarrow(5,0,0).
\]

So

\[
p_A=(5,0,0).
\]

With column vectors,

\[
p_A=TSp.
\]

### B — translate, then scale

First:

\[
(1,0,0)\rightarrow(4,0,0).
\]

Then scaling doubles the translated coordinate too:

\[
(4,0,0)\rightarrow(8,0,0).
\]

Thus

\[
p_B=(8,0,0).
\]

### Core lesson

\[
TS\neq ST.
\]

Matrix multiplication is generally **not commutative**.

For column-vector notation, read

\[
TRSp
\]

from right to left: scale first, then rotate, then translate.

---

# Task 6 — Rotate around a point that is not the origin

A point

\[
p=(3,1)
\]

must be rotated 90° counterclockwise around

\[
c=(2,1).
\]

Calculate the result and write the composite transformation conceptually.

## Lecture connection

Lecture 3 §8.

## Solution

The rotation matrix naturally rotates around the origin. Therefore:

### Step 1 — move the center to the origin

\[
p-c=(3,1)-(2,1)=(1,0).
\]

### Step 2 — rotate

A 90° counterclockwise rotation gives

\[
(1,0)\rightarrow(0,1).
\]

### Step 3 — move back

\[
(0,1)+(2,1)=(2,2).
\]

Therefore

\[
p'=(2,2).
\]

The composite matrix is

\[
M=T(c)R(90^\circ)T(-c).
\]

Read right-to-left:

```text
move pivot to origin
→ rotate
→ restore pivot
```

### Real graphics example

This is exactly the structure needed for a door rotating around its hinge or a planet orbiting around another point.

---

# Task 7 — Rotation order in 3D

Start with the direction

\[
d=(0,1,0).
\]

Compare:

1. rotate 90° around x, then 90° around z;
2. rotate 90° around z, then 90° around x.

Use the standard right-handed convention.

## Lecture connection

Lecture 3 §5 and §7.

## Solution

### Case 1 — x then z

Around x:

\[
(0,1,0)\rightarrow(0,0,1).
\]

A z rotation leaves the z-axis vector unchanged:

\[
(0,0,1)\rightarrow(0,0,1).
\]

### Case 2 — z then x

Around z:

\[
(0,1,0)\rightarrow(-1,0,0).
\]

An x rotation leaves an x-axis vector unchanged:

\[
(-1,0,0)\rightarrow(-1,0,0).
\]

The final directions differ.

Therefore

\[
R_zR_xd\neq R_xR_zd.
\]

The reason is geometric: after the first rotation, the second operation acts on a differently oriented vector/object.

---

# Task 8 — Inverse transformations

Suppose

\[
M=TRS
\]

where `S` scales, `R` rotates and `T` translates.

What is

\[
M^{-1}?
\]

## Lecture connection

Lecture 3 §2, §3–5 and §7.

## Solution

The inverse of a product reverses the order:

\[
(ABC)^{-1}=C^{-1}B^{-1}A^{-1}.
\]

Therefore

\[
M^{-1}=S^{-1}R^{-1}T^{-1}.
\]

Why reverse the order?

Suppose you:

```text
1. scale
2. rotate
3. translate
```

To undo the process, you must:

```text
1. undo translation
2. undo rotation
3. undo scaling
```

This is like removing clothing layers: the last operation applied must be undone first.

For common transforms:

- translation inverse → negate displacement;
- rotation inverse → negate angle (or transpose a pure rotation matrix);
- scaling inverse → reciprocal scale factors, assuming none is zero.

---

# Task 9 — Construct a perpendicular direction using the cross product

Let

\[
a=(1,0,0),\qquad b=(0,1,0).
\]

Calculate

\[
a\times b.
\]

Then calculate

\[
b\times a.
\]

What does this teach you?

## Lecture connection

Lecture 3 §9–10.

## Solution

Using the right-hand rule,

\[
a\times b=(0,0,1).
\]

But reversing the operands gives

\[
b\times a=(0,0,-1).
\]

Thus

\[
a\times b=-(b\times a).
\]

The cross product is not commutative.

It creates a vector perpendicular to both inputs, and operand order determines which of the two possible perpendicular directions is chosen.

This becomes important when constructing coordinate frames, camera bases, tangent spaces and surface normals.

---

# Task 10 — Normalize a direction

Given

\[
d=(3,4,0),
\]

find the unit direction.

Why should directions often be normalized before being used as basis vectors?

## Lecture connection

Lecture 3 §9–10.

## Solution

Magnitude:

\[
\|d\|=\sqrt{3^2+4^2}=5.
\]

Normalize:

\[
\hat d=\frac{d}{\|d\|}
=\left(\frac35,\frac45,0\right).
\]

Its length is 1.

An orthonormal coordinate basis needs unit axes. If basis vectors carry arbitrary magnitudes, the corresponding matrix may introduce unintended scaling in addition to orientation.

---

# Task 11 — Build an orientation basis

An aircraft should point in direction

\[
f=(0,0,-1).
\]

Use world-up

\[
u_0=(0,1,0).
\]

Construct a right vector and a corrected up vector using cross products.

## Lecture connection

Lecture 3 §9–10, especially the flight-direction/basis-construction example.

## Solution

The forward direction is already normalized:

\[
f=(0,0,-1).
\]

One consistent convention is

\[
r=f\times u_0.
\]

Then

\[
r=(1,0,0).
\]

Now construct an up vector perpendicular to both:

\[
u=r\times f=(0,1,0).
\]

We obtain an orthonormal frame consisting of right, up and forward directions.

### Degenerate case

If `f` is parallel to the chosen world-up direction, then

\[
f\times u_0=0.
\]

The zero vector cannot be normalized, so the algorithm needs another reference-up vector.

This is not merely theoretical; camera-orientation code must handle exactly this situation.

---

# Task 12 — Coordinate-system transformation

A point in object-local coordinates is

\[
p_{local}=(1,0,0,1)^T.
\]

The object is translated by `(5,2,0)` in world space.

1. Write `M_{world←local}`.
2. Find the world coordinates of the point.
3. What matrix converts the result back to local coordinates?

## Lecture connection

Lecture 3 §11.

## Solution

The local-to-world matrix is

\[
M_{world\leftarrow local}=
\begin{bmatrix}
1&0&0&5\\
0&1&0&2\\
0&0&1&0\\
0&0&0&1
\end{bmatrix}.
\]

Therefore

\[
p_{world}=M_{world\leftarrow local}p_{local}
=(6,2,0,1)^T.
\]

To go back,

\[
M_{local\leftarrow world}
=(M_{world\leftarrow local})^{-1}.
\]

Here that is translation by `(-5,-2,0)`.

### Key interpretation

The arrow notation tells you what coordinates are being produced:

\[
M_{A\leftarrow B}
\]

means **take coordinates expressed in B and express the same geometric entity in A**.

---

# Task 13 — Hierarchical transformation

A robot has a torso and an arm.

The torso's local-to-world transform is

\[
M_{world\leftarrow torso}.
\]

The arm is attached to the torso with

\[
M_{torso\leftarrow arm}.
\]

What is the arm's local-to-world matrix?

## Lecture connection

Lecture 3 §11 and §13.

## Solution

A point begins in arm coordinates:

\[
p_{arm}.
\]

First convert arm → torso:

\[
p_{torso}=M_{torso\leftarrow arm}p_{arm}.
\]

Then torso → world:

\[
p_{world}=M_{world\leftarrow torso}p_{torso}.
\]

Substitute:

\[
p_{world}
=M_{world\leftarrow torso}
M_{torso\leftarrow arm}
p_{arm}.
\]

Therefore

\[
M_{world\leftarrow arm}
=M_{world\leftarrow torso}
M_{torso\leftarrow arm}.
\]

This is the mathematical foundation of scene graphs and articulated models.

If the torso moves, the arm follows automatically because its world transformation contains the torso transformation.

---

# Task 14 — Model, view and projection order

A vertex begins in model-local coordinates as `p`.

You have:

- model matrix `M`;
- view matrix `V`;
- projection matrix `P`.

Which expression produces clip-space coordinates?

Explain the order.

## Lecture connection

Lecture 3 §12, with the rendering-pipeline context from Lecture 2 and projection details in Lecture 4.

## Solution

For column vectors,

\[
p_{clip}=PVMp.
\]

Read right-to-left:

```text
p
↓ M
local → world
↓ V
world → view/camera
↓ P
view → clip
```

In a vertex shader this often appears as

```glsl
gl_Position = projection * view * model * vec4(aPos, 1.0);
```

or as one precomputed MVP matrix:

```glsl
gl_Position = uMVP * vec4(aPos, 1.0);
```

### Why projection comes last

Projection expects geometry already expressed relative to the camera. It answers how camera/view-space geometry maps into the visible clip volume.

---

# Task 15 — Diagnose a transformation bug

A programmer wants an object to:

1. scale around its own center;
2. rotate around its own center;
3. move to world position `(5,0,0)`.

They construct

```cpp
model = scaleMatrix * rotationMatrix * translationMatrix;
```

assuming column-vector mathematics.

Why is this likely wrong, and what conceptual order should the matrix have?

## Lecture connection

Lecture 3 §7 and §12.

## Solution

With column vectors, the rightmost matrix acts first.

Their matrix

\[
SRT
\]

therefore means:

```text
translate first
→ rotate translated coordinates
→ scale everything including the translation
```

That is not the intended behavior.

For

```text
scale locally
→ rotate locally
→ translate into world
```

the conceptual matrix is

\[
M=TRS.
\]

Then

\[
p_{world}=TRSp_{local}.
\]

### Debugging habit

Never debug matrix order by staring at multiplication symbols alone. Write the intended geometric operations as a sequence, then remember that with column vectors the first operation appears nearest the vector.

---

# Task 16 — OpenGL/GLM connection

Suppose application code conceptually creates

```cpp
model = translate(I, position);
model = rotate(model, angle, axis);
model = scale(model, size);
```

and passes the resulting matrix as a uniform to the vertex shader.

Explain which parts happen on the CPU and which happen per vertex on the GPU.

## Lecture connection

Lecture 2 §8 and Lecture 3 §12–13.

## Solution

The application/CPU typically computes or updates the transformation matrix using GLM or equivalent mathematics.

It uploads the resulting matrix as a uniform:

```text
CPU
construct model matrix
↓
set shader uniform
```

The vertex shader then applies that same matrix to every relevant vertex:

```glsl
worldPos = model * vec4(aPos,1.0);
```

Thus:

- matrix construction/update → application side;
- matrix-vector multiplication for every vertex → vertex shader/GPU side.

This division is efficient because one matrix describes the transformation of an entire object while thousands of vertices can apply it in parallel.

---

# Task 17 — Full integration problem: model a column

You have a reusable unit cylinder centered around the origin. You want one copy to become a column that is:

- twice as tall;
- half as wide in x and z;
- rotated 30° around world y;
- placed at `(4,0,-3)`.

Construct the conceptual model matrix and explain the complete path to the screen.

## Lecture connection

Lecture 3 §4, §5, §7, §12–13; Lecture 2 for the pipeline; Lecture 4 for projection.

## Solution

### Step 1 — local scaling

Use

\[
S=S(0.5,2,0.5).
\]

This turns the unit cylinder into a tall narrow column.

### Step 2 — orientation

Use

\[
R=R_y(30^\circ).
\]

### Step 3 — world placement

Use

\[
T=T(4,0,-3).
\]

### Step 4 — model matrix

For column-vector convention,

\[
M=TRS.
\]

So every local vertex follows

\[
p_{world}=TRSp_{local}.
\]

### Step 5 — camera transformation

The view matrix gives

\[
p_{view}=Vp_{world}.
\]

### Step 6 — projection

Lecture 4's projection matrix produces

\[
p_{clip}=Pp_{view}.
\]

Combined:

\[
p_{clip}=PTRSp_{local}.
\]

### Step 7 — vertex shader

The GPU can receive the combined matrix as a uniform and execute

```glsl
gl_Position = uMVP * vec4(aPos,1.0);
```

for every cylinder vertex.

### Step 8 — rest of rendering pipeline

After the vertex shader:

```text
clip coordinates
→ clipping
→ perspective division
→ viewport transform
→ primitive rasterization
→ fragments
→ fragment shader
→ framebuffer
```

The important point is that the cylinder mesh itself never needed to be rewritten. A single stored primitive becomes many differently placed scene objects through transformation matrices.

---

# 18. Cross-reference map — “Where did I learn this?”

| Exercise skill | Main source |
|---|---|
| homogeneous point `(x,y,z,1)` | Lecture 3 §2 |
| direction `(x,y,z,0)` | Lecture 3 §2 |
| translation | Lecture 3 §3 |
| scaling | Lecture 3 §4 |
| standard-axis rotation | Lecture 3 §5 |
| reflection/shear | Lecture 3 §6 |
| matrix composition/order | Lecture 3 §7 |
| transform around pivot | Lecture 3 §8 |
| normalization | Lecture 3 §9–10 |
| cross product | Lecture 3 §9–10 |
| construct orthogonal basis | Lecture 3 §10 |
| coordinate-frame conversion | Lecture 3 §11 |
| inverse frame transformation | Lecture 3 §11 |
| hierarchical transformations | Lecture 3 §11, §13 |
| model matrix | Lecture 3 §12–13 |
| view matrix | Lecture 3 §12 |
| MVP chain | Lecture 3 §12 + Lecture 4 |
| matrix uniform in vertex shader | Lecture 2 §8 + Lecture 3 §12 |
| non-uniform scaling and normals | introduced here; deeper in Lecture 8 |

---

# 19. Exam-level traps to recognize

## Trap 1 — reading matrices left-to-right

For the course's common column-vector notation,

\[
TRSp
\]

means **S first, then R, then T**.

## Trap 2 — confusing a point with a direction

Point:

\[
w=1.
\]

Direction:

\[
w=0.
\]

Translation should affect the former but not the latter.

## Trap 3 — rotating around the wrong point

A standard rotation acts around the origin. For pivot `c`, use

\[
T(c)RT(-c).
\]

## Trap 4 — forgetting inverse order

\[
(ABC)^{-1}=C^{-1}B^{-1}A^{-1}.
\]

## Trap 5 — using an unnormalized basis

A supposed “rotation” matrix built from non-unit axes can introduce scaling.

## Trap 6 — cross product of parallel vectors

It produces zero and cannot be normalized into a basis axis.

## Trap 7 — losing track of coordinate systems

Always annotate mentally:

```text
local → world → view → clip
```

A matrix is not just “a transformation”; ask **from which coordinate system to which?**

---

# 20. What you should be able to do after Exercise 3

Without notes, you should be able to:

1. Apply translation, scaling and standard-axis rotation numerically.
2. Write their homogeneous 4×4 matrices.
3. Explain why homogeneous coordinates are used.
4. Distinguish points from direction vectors using `w`.
5. Predict the effect of transformation order.
6. Construct a transformation around an arbitrary pivot point.
7. Find inverses of common transformations and composite transformations.
8. Normalize vectors.
9. Compute and interpret cross products.
10. Construct a simple orthonormal basis from directions.
11. Recognize the parallel-vector degeneracy in basis construction.
12. Interpret `M_{A←B}` as a coordinate-system conversion.
13. Compose hierarchical local-to-world transformations.
14. Explain `PVMp` from local space all the way to clip space.
15. Connect CPU/GLM matrix construction to vertex-shader matrix multiplication.
16. Diagnose common matrix-order mistakes.

---

# 21. Final mental model

Exercise 3 should leave you with one coherent picture:

```text
stored model
(local coordinates)
        ↓ model matrix
world coordinates
        ↓ view matrix
camera coordinates
        ↓ projection matrix
clip coordinates
```

Inside the model matrix itself:

```text
scale / rotate / translate
        ↓
compose matrices in deliberate order
        ↓
one matrix applies to every model vertex
```

And for harder transformations:

```text
hard geometric operation
↓
move/change basis into a convenient coordinate system
↓
perform a simple standard operation
↓
transform back
```

The deepest idea is:

> **Transformation matrices are not formulas to memorize; they are mappings between geometric descriptions. Matrix composition lets you build complicated mappings from simple ones, and the order records the causal order of those geometric operations.**

If you can reason in terms of spaces, pivots and operation order, most transformation questions become derivable rather than memorization tasks.