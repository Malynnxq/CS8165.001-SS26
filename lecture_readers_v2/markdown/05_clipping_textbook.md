# Chapter 5 — Clipping

> **Purpose of this reader.** This chapter reconstructs the teaching behind Lecture 5 for a student who did not attend the lecture. It is organized by ideas rather than by individual slides. The goal is to understand *why* clipping is needed, *how* the major clipping algorithms reason about geometry, and *when* each approach is appropriate.
>
> **Primary course source:** `course_text_parts/03_lectures/05_clipping.txt` (Lecture 5 slides, 19 May 2026).

## 1. Why clipping exists

At the end of the previous chapters, we can transform a 3D model into camera space, project it, and map the result toward the screen. But projection does **not** guarantee that every resulting primitive lies inside the visible image.

Imagine a triangle whose left half is visible and whose right half lies outside the window. We should not spend time rasterizing and shading the invisible half. More importantly, later stages need geometry that correctly respects the boundaries of the view volume.

**Clipping** means cutting geometric primitives against a permitted region and discarding the portions outside that region.

The key distinction is:

- **culling/rejection:** discard an entire primitive because none of it matters;
- **clipping:** preserve the visible part of a primitive that crosses a boundary.

So a line from `(-2,0)` to `(0,0)` clipped against the square `[-1,1] × [-1,1]` does not disappear. It becomes the shorter line from `(-1,0)` to `(0,0)`.

This is why clipping belongs before expensive later work whenever possible: reducing geometry early means less rasterization and fragment processing later.

**Lecture connection:** slides 2–3 distinguish analytical clipping before raster conversion from pixel-based clipping during or after rasterization.

---

## 2. Analytical clipping versus pixel-based clipping

There are two broad places where clipping can happen.

### 2.1 Analytical clipping

Here we work with the **geometric primitive itself** before rasterization. A line is still a line segment; a polygon is still a sequence of vertices. We calculate intersections with the clip boundary and construct a new primitive containing only the allowed portion.

This is particularly useful when a large fraction of a primitive lies outside the visible region, because the invisible portion never becomes fragments.

OpenGL performs geometric clipping against its canonical view volume as part of the rendering pipeline.

### 2.2 Pixel/fragment-based clipping

Alternatively, rasterization may happen first and individual fragments can later be rejected. Mechanisms such as the scissor test, stencil operations, or fragment-shader logic can restrict where rendering takes effect.

This is more flexible for irregular screen-space regions, but it does not provide the same early reduction of geometric work.

The rest of this lecture is primarily about **analytical algorithms**.

---

# Part I — Clipping line segments

## 3. Start with the simplest possible approach

Suppose we want to clip a line segment against an axis-aligned rectangle.

A brute-force solution is:

1. test the segment against every rectangle edge;
2. calculate every intersection;
3. determine which intersections lie on both finite segments;
4. retain the part inside the rectangle.

This works, but it performs intersection calculations even in easy cases. If a line lies entirely inside the rectangle, we would prefer to accept it immediately. If it lies entirely to the left, we would prefer to reject it immediately.

This observation motivates **Cohen–Sutherland**.

---

## 4. Parametric representation of a line

Before the clipping algorithms, one representation is worth understanding because it returns repeatedly throughout the lecture.

For endpoints `p0` and `p1`, write the segment as

\[
p(t)=p_0+t(p_1-p_0),\qquad 0\le t\le1.
\]

Interpretation:

- `t = 0` gives `p0`;
- `t = 1` gives `p1`;
- `t = 0.5` gives the midpoint;
- values between 0 and 1 move continuously along the finite segment.

This converts a geometric question into a one-dimensional one: **which interval of `t` remains visible?**

Cyrus–Beck will exploit this idea directly. Cohen–Sutherland uses a different first strategy: classify endpoints cheaply before doing intersection arithmetic.

---

## 5. Cohen–Sutherland: classify first, calculate later

### 5.1 Divide the plane into nine regions

An axis-aligned clip rectangle is bounded by

\[
x_{min},\;x_{max},\;y_{min},\;y_{max}.
\]

Relative to that rectangle, a point can be:

- left of it,
- right of it,
- below it,
- above it,
- or inside it.

The four outside conditions are encoded as four bits, producing an **outcode**.

The lecture uses the convention:

- bit 0: `x < xmin`;
- bit 1: `x > xmax`;
- bit 2: `y < ymin`;
- bit 3: `y > ymax`.

Therefore the interior has outcode `0000`.

A point above and left of the rectangle has both the `above` and `left` bits set.

### 5.2 Why binary coding helps

Let the endpoint outcodes be `oc0` and `oc1`.

#### Trivial acceptance

If

```text
oc0 == 0 && oc1 == 0
```

both endpoints are inside. Because the rectangle is convex, the entire line segment between two interior points is also inside.

So we accept without calculating any intersections.

#### Trivial rejection

If

```text
(oc0 & oc1) != 0
```

there is at least one outside half-plane containing **both** endpoints.

For example, if both endpoints have the `left` bit set, the complete segment lies left of the rectangle and cannot enter it.

So we reject without calculating any intersections.

This is the clever core of Cohen–Sutherland: expensive geometry is replaced, whenever possible, by cheap comparisons and bitwise operations.

### 5.3 The ambiguous case

If neither test succeeds, the segment may cross the rectangle.

Choose an endpoint that is outside, select one boundary indicated by its outcode, intersect the line with that boundary, replace the old endpoint with the intersection, recompute its outcode, and repeat.

For example, for the top boundary `y = ymax`, the line equation gives

\[
x=x_0+(x_1-x_0)\frac{y_{max}-y_0}{y_1-y_0}.
\]

After replacement, the segment is shorter. Reclassification may now make it trivially acceptable, trivially rejectable, or require another clipping step.

### 5.4 A mental example

Suppose a line begins far above-left of the rectangle and ends inside it.

The inside endpoint has `0000`. The outside endpoint might have `1001` (depending on the lecture's bit ordering). Their bitwise AND is zero, so the line cannot be trivially rejected. We clip the outside endpoint against one violated boundary, classify the new point, and continue until the surviving endpoint reaches the rectangle.

### 5.5 Strength and weakness

Cohen–Sutherland is excellent when many segments are obviously inside or obviously outside. But for segments that genuinely cross several boundaries, its fixed iterative clipping order can perform unnecessary work.

That motivates the next algorithm.

**Lecture connection:** slides 5–15 develop brute force → endpoint analysis → four-bit outcodes → pseudo-code → evaluation.

---

## 6. Cyrus–Beck: solve the visible parameter interval

Cyrus–Beck approaches the same problem from a different direction.

Instead of repeatedly cutting an endpoint and reclassifying it, it asks:

> Along the parameter `t` from 0 to 1, when does the segment enter the clip region, and when does it leave?

This is naturally suited to **convex** clipping regions.

### 6.1 Why convexity matters

A set is convex if the straight segment between any two points inside it also stays inside it.

For a convex polygon, a line can enter the polygon at most once and leave at most once. Therefore its visible part can be represented by a single interval

\[
[t_{enter},t_{leave}].
\]

For a non-convex polygon, the same line might enter, leave, re-enter, and leave again. One interval would no longer be enough.

### 6.2 Describe each clip edge as a half-plane

For each boundary edge, choose:

- a point `PE` on the edge;
- an outward normal vector `N`.

The line is

\[
p(t)=p_0+tD,
\]

where

\[
D=p_1-p_0.
\]

An intersection with the infinite line supporting a clip edge occurs when the vector from `PE` to `p(t)` has zero component along the edge normal:

\[
N\cdot(p(t)-P_E)=0.
\]

Substitute the parametric line:

\[
N\cdot(p_0+tD-P_E)=0.
\]

Solving for `t` gives

\[
t=-\frac{N\cdot(p_0-P_E)}{N\cdot D}.
\]

The dot product therefore turns a 2D geometric intersection into a scalar parameter.

### 6.3 Entering versus leaving

The sign of

\[
N\cdot D
\]

tells us how the segment moves relative to the boundary's outward normal.

Conceptually:

- one sign means the line moves **into** the allowed half-plane;
- the other means it moves **out of** it;
- zero means the line is parallel to that boundary.

The algorithm gathers all constraints and tightens the initially allowed interval `[0,1]`.

A useful way to think about it is:

```text
t_enter = latest entry demanded by any boundary
t_leave = earliest exit demanded by any boundary
```

If eventually

\[
t_{enter}>t_{leave},
\]

there is no parameter value satisfying all half-plane constraints, so the segment is invisible.

Otherwise the clipped segment is simply

\[
p(t_{enter})\quad\text{to}\quad p(t_{leave}).
\]

### 6.4 Why this can be better

Notice the difference from Cohen–Sutherland. Cyrus–Beck can postpone calculating actual `(x,y)` intersection coordinates. It first works almost entirely with scalar `t` values and computes at most the final relevant endpoints.

That is advantageous when many lines truly require clipping.

### 6.5 Liang–Barsky

The lecture mentions Liang–Barsky as an optimization of the same parametric idea for an axis-aligned rectangular clipping region. The rectangle's simple normals and inequalities allow the calculations to be specialized.

**Lecture connection:** slides 16–24 introduce Cyrus–Beck, parametric line representation, edge normals, dot products, entering/leaving parameters, and compare it with Cohen–Sutherland.

---

# Part II — From lines to polygons

## 7. Why polygon clipping is harder

For a line clipped against a convex region, the result is at most one line segment.

For a polygon, new requirements appear:

1. the output must remain a **closed contour**;
2. clipping can introduce new vertices at boundary intersections;
3. a non-convex polygon can potentially produce multiple disconnected visible pieces.

So we need algorithms that operate on an ordered sequence of polygon vertices and preserve topology.

---

## 8. Sutherland–Hodgman: clip one half-plane at a time

Sutherland–Hodgman is conceptually elegant because it converts polygon clipping into a pipeline of simpler operations.

Suppose the clip region is a convex polygon. Every edge of that polygon defines an interior half-plane.

Instead of clipping against the whole polygon at once:

```text
input polygon
    ↓
clip against boundary 1
    ↓
clip against boundary 2
    ↓
...
    ↓
clip against final boundary
    ↓
output
```

The output vertex list of one stage becomes the input vertex list of the next.

### 8.1 Process one subject edge at a time

For one clip boundary, consider consecutive subject-polygon vertices:

- `s` = previous vertex;
- `p` = current vertex.

There are four possibilities.

### Case 1 — inside → inside

The entire end of the edge remains in the allowed half-plane.

**Output:** `p`.

### Case 2 — inside → outside

The edge leaves the allowed region.

**Output:** the intersection point only.

### Case 3 — outside → outside

No visible part of this edge reaches the interior.

**Output:** nothing.

### Case 4 — outside → inside

The edge enters the allowed region.

**Output:** the intersection point, then `p`.

These four rules are worth learning conceptually rather than memorizing. Ask: **what part of the directed edge should remain after crossing this boundary?** The output rules follow immediately.

### 8.2 Why the algorithm pipelines well

Each clipper receives a stream of vertices and emits another stream of vertices. As soon as a stage knows a new output vertex, it can forward it to the next stage. This makes the algorithm attractive for pipeline/hardware implementations.

### 8.3 Inside tests

For an axis-aligned rectangle, `inside` is just a coordinate comparison.

For a general directed convex boundary, use the orientation of the edge and a normal/cross-product-style test. With consistently counterclockwise clip vertices, all interior points lie on the same side of every directed edge.

### 8.4 Limitation

The clean half-plane pipeline relies on a **convex clip region**. Arbitrary polygon–polygon clipping introduces more complicated topology: the intersection can have multiple components and contours can switch between edges belonging to either polygon.

That is why the lecture next introduces Weiler–Atherton and Greiner–Hormann.

**Lecture connection:** slides 25–33 cover the four cases, sequential half-plane clipping, pipeline implementation, pseudo-code, inside tests, and intersection calculations.

---

# Part III — Arbitrary polygon clipping

## 9. Think of polygon clipping as a set operation

Let `A` be one polygon and `B` another.

The clipping result for intersection is simply

\[
A\cap B.
\]

But geometrically constructing the boundary of `A ∩ B` is harder than writing that notation.

The plane can be divided into four categories:

1. inside `A` only;
2. inside `B` only;
3. inside both `A` and `B`;
4. inside neither.

For an intersection operation, we want category 3.

The important insight is that the resulting boundary may alternate between pieces of the contour of `A` and pieces of the contour of `B`.

---

## 10. Weiler–Atherton: reconstruct the desired regions

The lecture presents Weiler–Atherton as an algorithm capable of clipping arbitrary polygons against arbitrary clip polygons.

Its conceptual workflow is:

1. find and insert intersections between the polygon boundaries;
2. subdivide the contours at those intersections;
3. determine which resulting edge segments border which regions;
4. traverse appropriate segments to construct closed output contours.

This is substantially more complex than Sutherland–Hodgman because the algorithm must handle **topology**, not merely inside/outside status relative to one convex half-plane.

### 10.1 Transversal versus overlapping intersections

Two boundary edges may cross at a single point. This is a **transversal intersection**, and the intersection point can be inserted into both vertex lists.

But edges can also overlap along a segment. Then there is no single crossing point, and the data structure must represent the overlap endpoints and decide how contours connect.

That special case illustrates why robust general polygon clipping is difficult.

### 10.2 What to remember

You do not need to mentally reduce Weiler–Atherton to a single formula. Its important role in the conceptual progression is:

> Once both polygons may be arbitrary, clipping becomes a problem of constructing the correct closed boundary graph from intersections and contour pieces.

**Lecture connection:** slides 34–39 introduce the region classification, intersection insertion, contour processing, and evaluation of Weiler–Atherton.

---

## 11. Greiner–Hormann: trace the boundary pieces that are inside

Greiner–Hormann offers a particularly intuitive idea for polygon intersection.

The lecture's **chalk wagon metaphor** is excellent:

- travel around polygon `A`, drawing only while you are inside `B`;
- travel around polygon `B`, drawing only while you are inside `A`;
- connect the drawn pieces into the resulting clipped contours.

This matches the set-theoretic fact that the boundary of `A ∩ B` consists of portions of `A` that lie inside `B` plus portions of `B` that lie inside `A`.

### 11.1 Intersection points become switching locations

First insert intersections into the contour representations. While traversing a polygon, crossing the other polygon's boundary changes whether the current contour segment is inside or outside. Under ordinary transversal crossings, this lets an inside/outside flag toggle at intersections.

The final contours are formed by following appropriate boundary pieces and switching between polygon contours at intersection nodes.

### 11.2 Winding number and inside tests

The lecture associates Greiner–Hormann with the **winding number**, a general way of deciding whether a point lies inside a polygon.

Intuitively, imagine walking around the polygon and asking how many times the closed contour winds around the test point. For ordinary simple polygons, a nonzero winding indicates an interior point under the winding-number rule.

This is more general than the simple half-plane test used for convex polygons.

### 11.3 Beyond intersection

Once contours and inside/outside transitions are represented correctly, closely related traversal rules can construct Boolean polygon operations such as intersection, union, and difference. The lecture uses set-operation examples to emphasize this connection.

**Lecture connection:** slides 40 onward introduce Greiner–Hormann, the chalk-wagon metaphor, contour detection, winding-number reasoning, and polygon set operations.

---

# Part IV — How the algorithms fit together

## 12. One problem, progressively harder geometry

The lecture is easier to remember if you see its algorithms as responses to increasingly general clipping problems.

| Problem | Core idea | Typical algorithm |
|---|---|---|
| Line vs axis-aligned rectangle, many easy accept/reject cases | classify endpoints with bit codes | Cohen–Sutherland |
| Line vs convex polygon | solve an allowed interval of line parameters | Cyrus–Beck |
| Polygon vs convex clip polygon | pass vertex lists through one half-plane clipper per boundary | Sutherland–Hodgman |
| Arbitrary polygon vs arbitrary polygon | reconstruct closed contours from intersections and boundary pieces | Weiler–Atherton / Greiner–Hormann |

This table is more important than memorizing five unrelated algorithm names. Each new method removes a restriction or changes the performance strategy.

---

## 13. A deeper unifying idea: clipping is constraint satisfaction

All of the early algorithms can be understood as asking whether geometry satisfies a set of inequalities.

For a rectangle:

\[
x\ge x_{min},\quad x\le x_{max},\quad y\ge y_{min},\quad y\le y_{max}.
\]

Cohen–Sutherland encodes violations of these inequalities as bits.

Cyrus–Beck substitutes `p(t)` into boundary constraints and asks which interval of `t` satisfies all of them.

Sutherland–Hodgman applies the constraints one at a time to a polygon vertex stream.

So although the algorithms look different, they share a common mathematical structure:

> **Keep the part of the primitive that satisfies all clip-region constraints.**

For arbitrary non-convex polygon intersections, a single conjunction of half-plane inequalities is no longer enough, so contour topology becomes central.

---

## 14. Where clipping sits in the graphics pipeline

Connect this chapter to the previous ones:

```text
model vertices
    ↓ model/view transformations
camera-space geometry
    ↓ projection
clip-space geometry
    ↓ clipping
visible portions of primitives
    ↓ perspective division / viewport stages as appropriate
screen-related geometry
    ↓ rasterization
fragments
    ↓ fragment operations
framebuffer
```

The exact implementation details of modern OpenGL matter, but the conceptual reason is simple: **do not rasterize geometry that lies outside the permitted viewing region.**

The lecture notes that OpenGL clips against the canonical view volume, while screen-space restrictions can also be implemented later with mechanisms such as scissoring, stencil operations, or fragment processing.

---

# Part V — Worked reasoning examples

## 15. Example: Cohen–Sutherland without arithmetic

Clip a line against a rectangle.

### Situation A

Both endpoint outcodes are `0000`.

**Reasoning:** both endpoints are inside a convex rectangle → the complete segment is inside → accept.

### Situation B

Both endpoint outcodes contain the `right` bit.

**Reasoning:** both endpoints lie in the right exterior half-plane → the whole segment is outside that boundary → reject.

### Situation C

One endpoint is above-left and the other is inside.

**Reasoning:** neither trivial test rejects it → select a violated boundary → compute one intersection → replace the outside endpoint → reclassify → repeat if needed.

Notice how arithmetic is the *last resort*, not the first step.

---

## 16. Example: Cyrus–Beck as interval narrowing

Start with the entire finite line segment:

\[
t\in[0,1].
\]

Suppose one clip boundary says the line does not enter the legal region until `t = 0.2`. Then

\[
t_{enter}=0.2.
\]

Another boundary says it leaves at `t = 0.8`, so

\[
t_{leave}=0.8.
\]

A third entry constraint at `t = 0.35` is stricter, so update

\[
t_{enter}=0.35.
\]

If no later constraint makes entry exceed exit, the visible segment is

\[
p(0.35)\text{ to }p(0.8).
\]

This is the conceptual heart of the algorithm.

---

## 17. Example: derive the four Sutherland–Hodgman cases yourself

Take one directed polygon edge from `s` to `p` and one clip boundary.

Ask only: **what portion of this edge lies inside?**

- inside → inside: the edge remains inside until `p`, so emit `p`;
- inside → outside: visibility ends at the crossing, so emit the intersection;
- outside → outside: no visible endpoint or crossing-to-interior exists, so emit nothing;
- outside → inside: visibility starts at the crossing and continues to `p`, so emit intersection + `p`.

If you understand this reasoning, there is almost nothing to memorize.

---

# Part VI — What you should know for the exam

## 18. Core knowledge checklist

You should be able to explain, without notes:

1. **Why clipping is performed before expensive later rendering stages.**
2. The difference between **analytical** and **pixel/fragment-based** clipping.
3. The parametric line representation `p(t)=p0+t(p1-p0)` and the meaning of `0≤t≤1`.
4. How a Cohen–Sutherland **outcode** represents violated rectangle boundaries.
5. Why `oc0 == 0 && oc1 == 0` gives trivial acceptance.
6. Why `(oc0 & oc1) != 0` gives trivial rejection.
7. Why Cohen–Sutherland can require repeated clipping.
8. Why Cyrus–Beck requires a **convex** clip region.
9. How Cyrus–Beck converts clipping into finding an entry/exit interval in `t`.
10. The role of **edge normals** and the **dot product** in Cyrus–Beck.
11. The four Sutherland–Hodgman inside/outside cases and their emitted vertices.
12. Why Sutherland–Hodgman naturally forms a pipeline.
13. Why arbitrary polygon clipping is topologically harder than clipping against a convex region.
14. The conceptual purpose of Weiler–Atherton.
15. The Greiner–Hormann/chalk-wagon idea and why output boundaries can alternate between the two input polygons.

---

## 19. Check yourself

### Q1. Why can Cohen–Sutherland accept a line when both endpoints are inside?
Because the rectangular clip region is convex: the complete segment joining two interior points remains inside.

### Q2. Why does a nonzero bitwise AND of the endpoint outcodes prove rejection?
Because the shared bit identifies one exterior half-plane containing both endpoints; the segment cannot cross into the rectangle across that boundary.

### Q3. Why is `t` useful in line clipping?
It orders every point of the segment with one scalar. Clipping can therefore become the problem of finding the allowed interval of `t`.

### Q4. What is the key difference between Cohen–Sutherland and Cyrus–Beck?
Cohen–Sutherland first uses endpoint region codes for cheap trivial decisions and may iteratively clip. Cyrus–Beck directly derives parameter constraints from convex clip boundaries and calculates the final relevant intersections after narrowing the parameter interval.

### Q5. In Sutherland–Hodgman, why do we emit both an intersection and `p` for outside → inside?
Because the visible part begins at the boundary intersection and continues to the interior endpoint `p`.

### Q6. Why is arbitrary polygon clipping harder?
The intersection can consist of multiple components, output contours may switch between edges of both polygons, and overlapping/non-transversal boundary cases must be represented correctly.

---

# 20. Final mental model

Do not remember Lecture 5 as five algorithm names. Remember the progression:

```text
We have geometry that may cross the visible boundary.
        ↓
Can we cheaply classify it?
        ↓
Cohen–Sutherland: encode endpoint regions.
        ↓
Can we solve visibility along a line more directly?
        ↓
Cyrus–Beck: find the legal interval of t.
        ↓
Now the primitive is a polygon.
        ↓
Sutherland–Hodgman: clip its vertex stream one half-plane at a time.
        ↓
Now both polygons may be arbitrary.
        ↓
Weiler–Atherton / Greiner–Hormann: intersections + contour topology.
```

The single idea underneath all of this is:

> **Clipping constructs exactly the portion of geometry satisfying the visible-region constraints, preferably before we spend computation on geometry that cannot contribute to the final image.**
