# Exercise Companion 4 — Projections and Clipping

> **Source status.** The repository preserves the Moodle assignment page **“Exercise 4: Projections and Clipping”**, but not the original task attachment. The exercises below are therefore **reconstructed study exercises**, not claimed to be the professor's original questions.
>
> **How to use this file.** For each problem, first read the **Lecture connection** and ask yourself whether you already understand that prerequisite. Then solve the task without looking at the worked solution. The purpose is to connect the mathematics directly to the concepts in your lecture readers.

---

# 0. The dependency chain for this sheet

Exercise 4 combines two consecutive lecture topics:

```text
3D point in view space
        ↓
projection matrix
        ↓
clip coordinates (x_c,y_c,z_c,w_c)
        ↓
CLIPPING in homogeneous clip space
        ↓
perspective division by w
        ↓
normalized device coordinates
        ↓
viewport transformation
        ↓
screen coordinates
```

The two main textbook chapters are:

- **Lecture 4 — Geometric Projection**
- **Lecture 5 — Clipping**

Earlier prerequisites:

- **Lecture 2:** rendering pipeline and `gl_Position`
- **Lecture 3:** matrices, homogeneous coordinates, transformation composition

Later connections:

- **Lecture 6:** rasterization starts after clipping/projection has produced screen-space primitives
- **Lecture 7:** depth values produced by projection are used for visibility determination

---

# Task 1 — Perspective versus orthographic projection

Two identical objects are placed on the viewing axis. Object A is twice as far from the camera as object B.

For each projection type, describe what happens to their apparent sizes:

1. perspective projection;
2. orthographic projection.

Explain the geometric reason using projection rays.

## Lecture connection

Lecture 4 §1–3.

## Solution

In **perspective projection**, projectors converge at the center of projection. Projected size depends on depth. Roughly,

\[
h_{image}\propto\frac{1}{z}.
\]

So an otherwise identical object twice as far away appears approximately half as large under the simplified geometry.

In **orthographic projection**, projection rays are parallel. Moving an object farther along the viewing direction does not create the same depth-dependent shrinking, so its projected size remains unchanged.

### Core recognition rule

```text
rays converge → perspective → depth changes apparent size
rays parallel → parallel projection → no perspective shrinking
```

---

# Task 2 — Similar-triangle projection

A vertical segment has height

\[
H=4.
\]

It is located at distance

\[
z=10
\]

from the center of projection. The image plane is at distance

\[
d=2.
\]

Using the simplified similar-triangle relation

\[
\frac{H'}{H}=\frac{d}{z},
\]

calculate the projected height.

What happens if the object is moved to `z=20`?

## Lecture connection

Lecture 4 §1 — similar triangles are the geometric origin of perspective shortening.

## Solution

Initially,

\[
H'=H\frac{d}{z}
=4\frac{2}{10}
=0.8.
\]

At `z=20`,

\[
H'=4\frac{2}{20}=0.4.
\]

Doubling the distance halves the projected height.

This is the geometric phenomenon that the perspective projection matrix plus homogeneous division later implements algebraically.

---

# Task 3 — Identify projection families

Classify each case:

A. Projection rays are parallel and perpendicular to the image plane.

B. Projection rays are parallel but not perpendicular to the image plane.

C. Projection rays converge at one eye point.

D. A technical drawing shows three principal axes with equal shortening.

## Lecture connection

Lecture 4 §2–4.

## Solution

A → **orthographic projection**.

B → **oblique projection**.

C → **perspective projection**.

D → **isometric projection**, an axonometric form of parallel/orthographic projection.

The important hierarchy is:

```text
planar projection
├── perspective
└── parallel
    ├── orthographic
    │   └── axonometric (isometric/dimetric/trimetric)
    └── oblique
```

---

# Task 4 — Build an orthographic mapping in one dimension

An orthographic view volume spans

\[
x\in[-4,12].
\]

Find the affine mapping that sends

\[
-4\mapsto-1,
\qquad
12\mapsto1.
\]

Then determine where `x=4` maps.

## Lecture connection

Lecture 4 §7–8, using translation/scaling from Lecture 3.

## Solution

The interval center is

\[
c=\frac{-4+12}{2}=4.
\]

The width is

\[
12-(-4)=16.
\]

To center the interval, subtract 4. To map half-width 8 to 1, scale by `1/8`.

Therefore

\[
x_{ndc}=\frac{x-4}{8}.
\]

Check:

\[
x=-4\Rightarrow\frac{-8}{8}=-1,
\]

\[
x=12\Rightarrow\frac8{8}=1.
\]

For `x=4`,

\[
x_{ndc}=0.
\]

### Why this matters

The full orthographic projection matrix does the same operation independently along x, y and depth: **translate the box to the origin, then scale it into the canonical volume**.

---

# Task 5 — Field of view and frustum height

A perspective camera has

\[
fovy=60^\circ
\]

and near distance

\[
n=2.
\]

For a symmetric frustum, calculate the near-plane half-height

\[
t=n\tan(fovy/2).
\]

Then calculate the full near-plane height.

## Lecture connection

Lecture 4 §5 and §11.

## Solution

Half-angle:

\[
30^\circ.
\]

Thus

\[
t=2\tan30^\circ
=2\frac1{\sqrt3}
\approx1.155.
\]

The full near-plane height is

\[
2t\approx2.309.
\]

### Interpretation

Increasing field of view increases the frustum width/height at the same near distance. More of the world fits into the image, so individual objects generally appear smaller.

---

# Task 6 — Aspect ratio

A window is `1920 × 1080` pixels.

1. Calculate its aspect ratio.
2. Why would using `aspect = 1.0` in the perspective matrix distort the image?

## Lecture connection

Lecture 4 §5–6 and §12.

## Solution

\[
aspect=\frac{1920}{1080}=\frac{16}{9}\approx1.7778.
\]

The projection matrix uses aspect ratio to make horizontal and vertical camera geometry consistent with the target image rectangle.

If the projection assumes a square image (`1:1`) but the viewport is wide (`16:9`), the normalized geometry is mapped into a differently shaped pixel rectangle. Circles can appear stretched into ellipses.

### Practical connection

On window resize, you commonly need to update both:

```text
glViewport(...)
projection aspect ratio
```

---

# Task 7 — Clip coordinates versus NDC

A perspective projection produces the clip-space point

\[
p_c=(2,1,3,4).
\]

Calculate its normalized device coordinates after perspective division.

## Lecture connection

Lecture 4 §9 and §13.

## Solution

Perspective division gives

\[
p_{ndc}=\left(
\frac{2}{4},
\frac{1}{4},
\frac{3}{4}
\right)
=(0.5,0.25,0.75).
\]

### Critical distinction

`gl_Position` is a **clip-space homogeneous coordinate**. It is not yet NDC.

The pipeline still performs

```text
clipping
→ divide by w
→ NDC
```

after the vertex shader.

---

# Task 8 — Why perspective needs w

Suppose two view-space points have the same x-coordinate but different depths. Why can an ordinary affine 3D transformation not produce perspective shrinking, while homogeneous projection can?

## Lecture connection

Lecture 4 §9, building on homogeneous coordinates from Lecture 3 §2.

## Solution

Perspective requires a relation of the form

\[
x_{projected}\propto\frac{x}{z}.
\]

Division by a coordinate is nonlinear in ordinary Cartesian 3D coordinates, so a standard affine matrix cannot directly express it.

A 4D homogeneous projection matrix instead prepares

\[
(x_c,y_c,z_c,w_c)
\]

with `w_c` related to depth. The later pipeline performs

\[
x_{ndc}=\frac{x_c}{w_c}.
\]

That division creates the required depth-dependent shrinking.

So the perspective effect is really a **two-step mechanism**:

```text
projection matrix creates depth-dependent w
        ↓
perspective division divides by w
```

---

# Task 9 — Viewport mapping

Use a viewport

```text
x0 = 0, y0 = 0
width = 800, height = 600
```

Map these NDC positions approximately to screen coordinates:

1. `(-1,-1)`
2. `(0,0)`
3. `(1,1)`
4. `(0.5,-0.5)`

Use

\[
x_s=x_0+\frac{x_{ndc}+1}{2}W,
\]

\[
y_s=y_0+\frac{y_{ndc}+1}{2}H.
\]

## Lecture connection

Lecture 4 §12.

## Solution

1. `(-1,-1)`:

\[
(0,0).
\]

2. `(0,0)`:

\[
(400,300).
\]

3. `(1,1)`:

\[
(800,600)
\]

as the continuous viewport boundary; actual discrete pixel-center conventions require care at the edge.

4. `(0.5,-0.5)`:

\[
x_s=\frac{1.5}{2}800=600,
\]

\[
y_s=\frac{0.5}{2}600=150.
\]

So approximately

\[
(600,150).
\]

### Conceptual distinction

Projection answers **where the point lies in normalized camera/image geometry**. The viewport transform answers **where that normalized position lies in the chosen pixel rectangle**.

---

# Task 10 — Is a clip-space point inside?

In the standard OpenGL-style homogeneous clipping test, x and y must satisfy

\[
-w\le x\le w,
\qquad
-w\le y\le w,
\]

with analogous depth bounds according to the course/API convention.

Classify the x/y status of:

A. `(x,y,w)=(1,2,3)`

B. `(4,0,3)`

C. `(-5,1,4)`

## Lecture connection

**Lecture 5 — Clipping**, with clip coordinates produced by Lecture 4.

## Solution

### A

For `w=3`, allowed x/y interval is `[-3,3]`.

`x=1`, `y=2` are both inside.

### B

`x=4 > 3`, so the point is outside the right clip boundary.

### C

`x=-5 < -4`, so the point is outside the left clip boundary.

### Why test before division?

The inequalities

\[
-w\le x\le w
\]

are the homogeneous equivalent of

\[
-1\le x/w\le1.
\]

This allows clipping to be handled robustly before perspective division.

---

# Task 11 — Trivial accept, trivial reject, or clipping required?

Consider a 2D rectangular clipping window and three line segments.

### Segment A

Both endpoints are inside.

### Segment B

Both endpoints lie to the left of the window.

### Segment C

One endpoint lies left of the window and the other lies inside.

Classify each as:

- trivially accept;
- trivially reject;
- clipping/intersection calculation required.

## Lecture connection

Lecture 5 — line clipping and region-code reasoning.

## Solution

A → **trivially accept**.

B → **trivially reject**, because both endpoints share an outside half-space (left).

C → **clipping required**, because the segment may enter the window at the left boundary.

This is the optimization principle behind algorithms such as Cohen–Sutherland: classify first, calculate intersections only when necessary.

---

# Task 12 — Cohen–Sutherland region codes

Use a rectangular window

\[
x\in[0,10],\qquad y\in[0,8].
\]

Use four conceptual bits:

```text
TOP    : y > 8
BOTTOM : y < 0
RIGHT  : x > 10
LEFT   : x < 0
```

Determine the outside regions for:

1. `P=(5,4)`
2. `Q=(-2,4)`
3. `R=(12,10)`
4. `S=(4,-3)`

Then explain how bitwise AND can trivially reject a segment.

## Lecture connection

Lecture 5 — Cohen–Sutherland line clipping.

## Solution

`P=(5,4)` is inside → code `0000`.

`Q=(-2,4)` is LEFT.

`R=(12,10)` is RIGHT + TOP.

`S=(4,-3)` is BOTTOM.

For two endpoints with codes `c1` and `c2`:

- if both codes are zero → trivially accept;
- if

\[
c_1\;\&\;c_2\neq0,
\]

then both endpoints share at least one outside half-space, so the segment cannot cross the window and is trivially rejected.

### Example

Two points both carrying LEFT have a nonzero AND in the LEFT bit. The entire segment lies on the outside side of the left boundary.

---

# Task 13 — Compute a line-window intersection

A segment runs from

\[
P_0=(-2,2)
\]

to

\[
P_1=(6,6).
\]

The clipping window has left boundary `x=0`.

Use the parametric line

\[
P(t)=P_0+t(P_1-P_0),\qquad0\le t\le1
\]

to find where the segment crosses `x=0`.

## Lecture connection

Lecture 5 line clipping. The vector/parametric representation also builds on earlier geometry knowledge.

## Solution

Direction:

\[
P_1-P_0=(8,4).
\]

Thus

\[
x(t)=-2+8t.
\]

At the left boundary,

\[
0=-2+8t
\Rightarrow t=\frac14.
\]

Then

\[
y(t)=2+4\left(\frac14\right)=3.
\]

Intersection:

\[
(0,3).
\]

If the other endpoint is inside the remaining boundaries, the clipped segment begins at `(0,3)` instead of `(-2,2)`.

---

# Task 14 — Polygon clipping can create new vertices

A triangle has one vertex outside the left clipping plane and two vertices inside.

What generally happens after clipping against that plane?

## Lecture connection

Lecture 5 — polygon clipping / Sutherland–Hodgman style reasoning.

## Solution

The two triangle edges connecting the outside vertex to the two inside vertices cross the clipping boundary.

Clipping computes two intersection points. The outside corner is removed, while the two original inside vertices remain.

The result is generally a **four-vertex polygon (quadrilateral)** rather than a triangle.

This is important:

> Clipping does not merely delete whole primitives. It can **modify topology and generate new vertices** where edges intersect clip planes.

The resulting polygon can later be triangulated/rasterized by the pipeline as required.

---

# Task 15 — Sutherland–Hodgman edge cases

When clipping a polygon against one clipping boundary, classify what should be emitted for an edge from previous vertex `S` to current vertex `P`:

1. inside → inside
2. inside → outside
3. outside → inside
4. outside → outside

## Lecture connection

Lecture 5 polygon clipping.

## Solution

### 1. inside → inside

Emit `P`.

### 2. inside → outside

Emit the intersection point only.

### 3. outside → inside

Emit the intersection point, then `P`.

### 4. outside → outside

Emit nothing.

This four-case rule is the heart of Sutherland–Hodgman polygon clipping.

Then repeat the process for each clipping boundary.

---

# Task 16 — Why clipping must happen before perspective division

A line segment crosses a frustum boundary. Why is the pipeline conceptually designed to clip in homogeneous clip space before dividing coordinates by `w`?

## Lecture connection

Lecture 4 §9 and Lecture 5.

## Solution

The projection matrix produces homogeneous coordinates. In that representation the canonical frustum boundaries can be expressed as linear inequalities such as

\[
-w\le x\le w.
\]

Clipping/intersection operations remain well behaved in homogeneous space.

Perspective division is nonlinear because each vertex is divided by its own `w`. Performing inappropriate linear interpolation after that divide can produce incorrect geometric/attribute behavior.

So the conceptual order is deliberately:

```text
projection
→ homogeneous clip coordinates
→ clip primitive
→ perspective divide
→ NDC
```

not

```text
projection
→ divide immediately
→ somehow clip later
```

This order also preserves the information needed for perspective-correct interpolation later in rasterization.

---

# Task 17 — Near and far planes are not optional decorations

Why does a perspective camera require a positive near distance instead of placing the near plane exactly at the center of projection? Give two conceptual reasons.

## Lecture connection

Lecture 4 §5, §9–10; later connection to Lecture 7 depth-buffer precision.

## Solution

First, the center of projection is where the perspective geometry becomes singular. Perspective involves division by a depth-related quantity; putting the projection plane/canonical mapping directly through the eye does not define a useful finite view boundary.

Second, the near plane defines the front boundary of the visible frustum and participates in the depth mapping. Its choice strongly affects depth-buffer precision later.

A very tiny near value combined with a very large far value can produce poor depth precision and contribute to z-fighting.

The full depth-buffer consequences are developed in Lecture 7.

---

# Task 18 — Full pipeline calculation

A vertex shader outputs

\[
p_c=(1,-1,1,2).
\]

Assume it survives clipping and the viewport is `800 × 600` beginning at `(0,0)`.

1. Calculate NDC x and y.
2. Calculate approximate viewport coordinates.
3. Name every major stage that happened before and after this point.

## Lecture connection

Lecture 2 pipeline + Lecture 3 transformations + Lecture 4 projection + Lecture 5 clipping + Lecture 6 rasterization.

## Solution

### Step 1 — perspective division

\[
x_{ndc}=\frac12=0.5,
\]

\[
y_{ndc}=\frac{-1}{2}=-0.5.
\]

### Step 2 — viewport

\[
x_s=\frac{0.5+1}{2}800=600,
\]

\[
y_s=\frac{-0.5+1}{2}600=150.
\]

So the projected location is approximately

\[
(600,150).
\]

### Complete conceptual chain

```text
local-space vertex
↓ model matrix              [Lecture 3]
world-space vertex
↓ view matrix               [Lecture 3]
view-space vertex
↓ projection matrix         [Lecture 4]
clip-space gl_Position
↓ clipping                  [Lecture 5]
clipped primitive
↓ perspective division      [Lecture 4]
NDC
↓ viewport transformation   [Lecture 4]
screen/window geometry
↓ rasterization             [Lecture 6]
fragments
↓ fragment processing
framebuffer
```

This chain is one of the most important things to be able to reconstruct for an exam.

---

# Task 19 — Diagnose a projection bug

A program uses

```cpp
glm::perspective(glm::radians(60.0f), 1.0f, 0.1f, 100.0f);
glViewport(0, 0, 1600, 900);
```

A sphere appears stretched horizontally.

What is the likely problem and how should it be corrected?

## Lecture connection

Lecture 4 §5–6 and §12.

## Solution

The projection matrix assumes aspect ratio

\[
1.0,
\]

but the viewport has

\[
\frac{1600}{900}\approx1.7778.
\]

Use the matching aspect ratio:

```cpp
glm::perspective(
    glm::radians(60.0f),
    1600.0f / 900.0f,
    0.1f,
    100.0f
);
```

The viewport and camera projection now describe compatible image shapes.

---

# Task 20 — Integrated clipping problem

A triangle has vertices A, B and C after projection into clip space. A and B lie inside the left clipping boundary; C lies outside it.

Explain, without doing numerical arithmetic:

1. which edges need intersections;
2. what new polygon results;
3. when perspective division happens;
4. why rasterization should receive the clipped result rather than the original triangle.

## Lecture connection

Lecture 4 + Lecture 5 + forward connection to Lecture 6.

## Solution

Edges `AC` and `BC` cross the left clipping plane, so each needs an intersection point.

Call the intersections `I_AC` and `I_BC`.

After removing outside vertex C, the surviving polygon is

```text
A → B → I_BC → I_AC
```

(up to traversal order), a four-vertex clipped polygon.

Perspective division happens **after clipping** for the surviving/generated clip-space vertices.

Rasterization must operate on the visible portion only. If the original uncut primitive were rasterized, it could generate fragments outside the valid view volume and behave incorrectly around the camera/frustum boundaries.

The pipeline therefore performs:

```text
primitive in clip space
→ geometrically restrict to view volume
→ divide/map surviving geometry
→ rasterize visible result
```

---

# 21. Cross-reference map — where each skill came from

| Exercise skill | Main lecture source |
|---|---|
| perspective shortening | Lecture 4 §1 |
| perspective vs parallel rays | Lecture 4 §2 |
| orthographic / axonometric / oblique | Lecture 4 §3 |
| vanishing points | Lecture 4 §4 |
| camera parameters | Lecture 4 §5 |
| `glm::perspective`, `frustum`, `ortho` | Lecture 4 §6 |
| canonical view volume | Lecture 4 §7 |
| orthographic matrix logic | Lecture 4 §8 + Lecture 3 |
| homogeneous perspective | Lecture 4 §9 |
| near/far depth mapping | Lecture 4 §10 |
| FOV scaling | Lecture 4 §11 |
| viewport mapping | Lecture 4 §12 |
| complete camera-to-screen chain | Lecture 4 §13 |
| homogeneous clip tests | Lecture 5 |
| trivial accept/reject | Lecture 5 |
| Cohen–Sutherland region codes | Lecture 5 |
| parametric line intersection | Lecture 5 |
| polygon clipping | Lecture 5 |
| Sutherland–Hodgman cases | Lecture 5 |
| rasterization after clipping | Lecture 6 |
| near/far and depth precision | Lecture 7 |

---

# 22. Exam-level traps

## Trap 1 — confusing clip space and NDC

Vertex shader output `gl_Position` is clip space:

\[
(x_c,y_c,z_c,w_c).
\]

Only after division by `w` do you get NDC.

## Trap 2 — thinking the projection matrix alone performs the whole perspective effect

The matrix prepares `w`; **perspective division** produces the depth-dependent shrinking.

## Trap 3 — clipping after dividing by w in your mental pipeline

The course pipeline is:

```text
clip coordinates → clipping → perspective division
```

## Trap 4 — confusing viewport with projection

Projection is camera geometry. Viewport maps normalized output to a pixel rectangle.

## Trap 5 — assuming clipping only deletes whole triangles

Clipping can create intersection vertices and turn one triangle into a polygon with more vertices.

## Trap 6 — forgetting aspect ratio

Projection and viewport must agree on image shape.

## Trap 7 — thinking orthographic projection means depth disappears

Depth is still retained for clipping and visibility testing.

---

# 23. What you should be able to do after this sheet

Without notes, you should be able to:

1. Explain perspective versus parallel projection geometrically.
2. Use similar triangles for a simple perspective calculation.
3. Distinguish orthographic, axonometric, oblique and perspective projection.
4. Derive a simple orthographic interval mapping from translate + scale.
5. Relate field of view to frustum size.
6. Calculate and interpret aspect ratio.
7. Distinguish view space, clip space, NDC and screen coordinates.
8. Perform perspective division.
9. Explain why homogeneous `w` enables perspective.
10. Map NDC coordinates into a viewport.
11. Apply simple homogeneous clip inequalities.
12. Recognize trivial line acceptance/rejection.
13. Understand Cohen–Sutherland region codes.
14. Compute a line-boundary intersection parametrically.
15. Explain how polygon clipping generates new vertices.
16. Reproduce the four Sutherland–Hodgman edge cases.
17. Explain why clipping precedes perspective division.
18. Connect near/far planes to later depth-buffer behavior.
19. Reconstruct the complete local → world → view → clip → NDC → screen chain.
20. Diagnose a projection/viewport aspect-ratio mismatch.

---

# 24. Final mental model

Do not study “projection” and “clipping” as unrelated chapters. They solve consecutive problems.

Projection asks:

> **How should camera-space geometry be represented so a 3D view can become an image?**

It produces homogeneous clip coordinates.

Clipping then asks:

> **Which portion of that projected primitive belongs to the camera's legal view volume?**

Only after that decision do we divide by `w` and map into the viewport.

So remember the causal chain:

```text
camera geometry
↓
projection matrix
↓
homogeneous clip coordinates
↓
clip against canonical boundaries
↓
perspective divide
↓
normalized device coordinates
↓
viewport
↓
rasterization
```

The deepest idea is:

> **Projection does not simply flatten 3D into 2D. It transforms camera geometry into a normalized homogeneous representation in which visibility against the view volume can be decided consistently. Clipping then restricts primitives to that volume before the nonlinear perspective divide and rasterization occur.**