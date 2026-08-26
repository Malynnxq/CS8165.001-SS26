# Chapter 6 — Rasterization

> **Purpose.** This chapter reconstructs Lecture 6 as a self-contained explanation for a student who missed the lecture. Rather than commenting on slides one by one, it follows the conceptual problem: how do we turn continuous geometric primitives into discrete fragments efficiently and consistently?
>
> **Primary course source:** `course_text_parts/03_lectures/06_rasterization.txt` (Lecture 6 slides, 27 May 2026).

## 1. The problem rasterization solves

After transformation, projection, and clipping, the graphics pipeline knows where geometric primitives lie relative to the screen. But a triangle is still a mathematical object in continuous space, while a raster display is a finite grid of discrete sample locations.

That mismatch creates the central problem of this lecture:

> **Which discrete screen samples should represent a continuous line or triangle?**

The process that answers this question is **rasterization**.

Rasterization does not merely “turn a triangle into an image.” More precisely, it determines which sample locations are covered by a primitive and generates **fragments** for those locations. A fragment is a candidate contribution to a framebuffer sample; later operations such as depth testing can still reject it.

This distinction matters:

```text
continuous primitive
        ↓ rasterization
covered sample locations / fragments
        ↓ fragment processing
surviving contributions
        ↓
framebuffer pixels
```

The lecture emphasizes two competing requirements:

- **quality:** the discrete approximation should represent the intended geometry faithfully;
- **speed:** rasterization happens for enormous numbers of primitives and samples, so the inner operations must be extremely cheap and hardware-friendly.

Triangles dominate real-time graphics because general polygonal surfaces can be tessellated into triangles and triangle coverage is mathematically simple enough for highly parallel hardware.

---

# Part I — Rasterizing a line

## 2. Why a line is already nontrivial

Suppose the mathematical line segment joins integer endpoints `(x0,y0)` and `(x1,y1)`.

For a horizontal line, the answer is obvious: advance one pixel in `x` each step. Vertical and 45-degree diagonal lines are similarly simple.

For a general slope, however, the ideal line passes between pixel/sample locations. We must choose a sequence of discrete samples that approximates it.

A useful quality rule from the lecture is:

- if `|m| ≤ 1`, choose roughly one sample per **column**;
- if `|m| ≥ 1`, choose roughly one sample per **row**.

Why? If a shallow line advanced primarily in `y`, or a steep line advanced primarily in `x`, gaps could appear. The dominant axis should be the one along which we take one discrete step at a time.

---

## 3. The naïve equation-based algorithm

The familiar explicit line equation is

\[
y=mx+B.
\]

For each integer `x`, we can calculate the corresponding real-valued `y` and round it:

```text
for each x:
    y = round(m*x + B)
    draw(x,y)
```

This is conceptually straightforward, but it reveals several problems that motivate the rest of the section.

### Problem 1 — vertical lines

If `x0 = x1`, the slope requires division by zero.

### Problem 2 — steep lines

For `|m| > 1`, stepping once per column can skip rows and produce gaps. We can repair this by swapping the roles of `x` and `y`, but the simple formula is no longer universal.

### Problem 3 — repeated arithmetic

Recomputing `m*x+B` repeatedly performs more work than necessary.

### Problem 4 — floating point and rounding

Rasterization is a discrete decision problem. Floating-point arithmetic and repeated rounding add cost and can create consistency problems, including different results when the endpoints are traversed in the opposite order.

So the lecture progressively replaces expensive recomputation with **incremental decisions**.

---

## 4. DDA: reuse what you already know

The Digital Differential Analyzer observes that if

\[
y=mx+B,
\]

then moving from `x` to `x+1` changes `y` by exactly `m`:

\[
y_{new}=y_{old}+m.
\]

So calculate the slope once, then repeatedly add it:

```text
y = y0
for each x:
    draw(x, round(y))
    y += m
```

This is an important general optimization principle in graphics:

> **Neighboring pixels are geometrically related, so update values incrementally instead of recomputing them from scratch.**

This principle is called exploiting **spatial coherence**, and it will reappear in edge walking, scanline triangle filling, and attribute interpolation.

DDA is better than the naïve algorithm, but it still uses floating point and rounding. The next step is to turn the choice into an integer sign test.

---

# Part II — The midpoint line algorithm

## 5. Reduce each step to a two-way decision

Assume for the moment that

\[
0\le m\le1.
\]

Then after drawing a pixel `P=(xp,yp)`, the next pixel must be one of only two candidates:

- **E** = `(xp+1, yp)`;
- **NE** = `(xp+1, yp+1)`.

The ideal mathematical line passes somewhere relative to these candidates.

Instead of calculating the exact distance from both pixels to the line, inspect their midpoint:

\[
M=(x_p+1, y_p+\tfrac12).
\]

If the true line lies above this midpoint, choose `NE`; if it lies below, choose `E` (with a consistent convention in the exact tie case).

So rasterization becomes:

> **At each column, determine on which side of the ideal line the midpoint lies.**

That is much cheaper than solving the full line equation every time—if we choose the right representation.

---

## 6. Why an implicit line equation is useful

The explicit form `y=mx+B` tells us the line's `y` value for an `x` value. But the midpoint algorithm needs a different question:

> Is a test point above, below, or exactly on the line?

An **implicit equation** is perfect for this:

\[
F(x,y)=ax+by+c.
\]

The line itself satisfies

\[
F(x,y)=0.
\]

With a consistent orientation, the sign of `F` identifies the side of the line:

```text
F(x,y) > 0  → one side
F(x,y) = 0  → on the line
F(x,y) < 0  → the other side
```

For the orientation used in the lecture, the sign at the midpoint tells whether `E` or `NE` is the closer discrete choice.

Define the **decision variable**

\[
d=F(M).
\]

We no longer care about the exact geometric distance. We need only the sign of `d`.

This is a major conceptual simplification: a continuous geometric proximity problem has become an integer-like comparison.

---

## 7. The crucial optimization: update the decision variable incrementally

Suppose we already know the decision variable for the current step.

If we choose `E`, the next midpoint moves one unit in `x`. Because `F` is linear, its value changes by a constant amount.

If we choose `NE`, the midpoint moves one unit in both `x` and `y`, so `F` changes by another constant amount.

Using

\[
dx=x_1-x_0,\qquad dy=y_1-y_0,
\]

the lecture derives integer-scaled updates of the form

\[
d_{start}=2dy-dx,
\]

and then updates `d` by precomputed increments depending on whether `E` or `NE` was chosen.

The exact formulas matter for implementation, but the reason they exist matters even more:

> Because the line equation is linear and neighboring candidate points differ by fixed grid steps, the decision value changes by fixed increments.

Therefore the inner loop needs only additions, comparisons, and coordinate increments—no division and no general multiplication.

That is exactly the kind of computation hardware likes.

---

## 8. Worked midpoint example

The lecture uses the line from `(5,8)` to `(9,11)`.

Here

\[
dx=4,\qquad dy=3.
\]

The initial decision variable is

\[
d=2dy-dx=6-4=2.
\]

Since the initial sign chooses the diagonal candidate under the lecture's convention, the first move is `NE`.

The algorithm then updates `d` rather than recomputing the line equation. The lecture obtains the decision sequence

```text
2, 0, 6, 4
```

and corresponding choices

```text
NE, E, NE, NE.
```

The important point is not memorizing those four numbers. It is seeing that **one initial geometric calculation creates a recurrence that drives all later pixel choices**.

---

## 9. Reversibility and tie-breaking

Suppose a line is drawn from `P0` to `P1`, and later from `P1` to `P0`.

Ideally, the same sample set should be generated in reverse order. If ties are handled inconsistently, that need not happen.

The lecture therefore discusses a reversible version where the `d=0` case depends consistently on traversal direction.

This is not cosmetic. Shared edges between primitives must be rasterized consistently; otherwise cracks, double coverage, or leftover pixels can appear.

That leads directly to triangle edge rules.

---

# Part III — Triangle edges and ownership

## 10. Why triangle edges need a convention

Imagine two adjacent triangles forming a rectangle. They share one edge.

If both triangles include every sample exactly on the shared edge, those samples may be processed twice. If neither includes them, a visible crack can appear.

Therefore rasterization needs a deterministic **ownership rule** for samples lying exactly on triangle boundaries.

The lecture points toward the **top-left rule**: boundary samples are included for selected edge orientations (conceptually top/left edges) and excluded for the complementary orientations.

The exact convention is less important than its purpose:

> **Every shared boundary sample should belong to exactly one of two adjacent triangles.**

This is a consistency rule, not merely a line-drawing detail.

---

## 11. Edge coherence

When rasterizing a triangle scanline by scanline, its left and right boundaries move gradually.

If an edge intersects scanline `y` at `x`, then on scanline `y+1` the new intersection is

\[
x_{new}=x_{old}+\frac{dx}{dy}.
\]

Again, the lecture exploits coherence: calculate an edge slope once and update the intersection incrementally.

Even the fractional update can be represented using integer numerator/denominator bookkeeping, much like a discrete error accumulator.

So the midpoint-line algorithm is not an isolated trick. It introduces the broader theme of this entire chapter:

> **Replace repeated continuous calculations with incremental discrete state.**

---

# Part IV — Filling regions

## 12. Connectivity: what counts as the same region?

Before filling arbitrary raster regions, we must define when pixels are considered connected.

### 4-connected

A pixel can reach neighbors only by

- left,
- right,
- up,
- down.

### 8-connected

Diagonal moves are allowed too.

Every 4-connected region is also 8-connected, but not every 8-connected region is 4-connected. Two pixels touching only at a corner demonstrate the difference.

This choice changes what a fill algorithm considers one contiguous region.

---

## 13. Flood fill versus boundary fill

### Flood fill

Start from a seed pixel and replace the largest connected region having a specified **old color**.

Conceptually:

```text
if current pixel has target old color:
    recolor it
    visit its neighbors
```

### Boundary fill

Instead of identifying the interior by its original color, identify a **boundary color**. Starting from an interior seed, continue until the boundary is reached.

Conceptually:

```text
if pixel is boundary → stop
if pixel was already filled → stop
otherwise:
    fill it
    visit neighbors
```

The distinction is about how the region is specified:

- flood fill: “fill all connected pixels like this one”;
- boundary fill: “fill everything reachable before crossing this border.”

Naïve recursive implementations are easy to understand but can create very deep recursion and overflow the call stack. Explicit stacks or queues provide safer iterative implementations.

---

# Part V — Filled triangle rasterization with scanlines

## 14. What triangle rasterization must produce

A filled triangle rasterizer has three jobs:

1. determine which samples are covered;
2. generate fragments for those samples;
3. assign/interpolate per-fragment attributes such as depth, color, normals, or texture coordinates.

The third job is easy to overlook. Rasterization is not only coverage. A fragment in the middle of a triangle still needs values even though attributes were originally specified only at the vertices.

---

## 15. Scanline rasterization

A triangle is convex. Therefore, except at special boundary cases, a horizontal scanline intersects it in one continuous interval.

That suggests an efficient algorithm:

1. find the left boundary intersection;
2. find the right boundary intersection;
3. generate all fragments between them.

Because adjacent scanlines are similar, the boundary intersections can be updated incrementally.

### Split the triangle into two monotonic halves

Sort the vertices by `y`:

\[
y_0\le y_1\le y_2.
\]

Then think of the triangle as:

- a lower half from `y0` to `y1`;
- an upper half from `y1` to `y2`.

One long edge connects `V0` to `V2`; the other active edge changes from `V0→V1` to `V1→V2` at the middle vertex.

For each scanline, update the two edge `x` positions and process the interval between them.

This is a perfect use of coherence: neighboring scanline intervals differ only slightly.

---

## 16. From covered sample to fragment

The lecture's segment routine conceptually does:

```text
for x from x_left to x_right:
    processFragment(x,y)
```

Calling it `processFragment` rather than “paint pixel” is important. Rasterization creates candidate fragments. They still enter later pipeline operations such as depth testing and blending.

So by this point you should distinguish three objects clearly:

- **triangle:** continuous geometric primitive;
- **fragment:** rasterizer-generated candidate at a covered sample;
- **pixel/framebuffer value:** stored result after later fragment operations.

---

# Part VI — Interpolating vertex attributes

## 17. Why interpolation is necessary

Suppose the three vertices of a triangle have different colors. What color should a fragment in the center have?

Or suppose each vertex has a different depth `z`. The depth test needs a depth for every fragment, not just for the three vertices.

Rasterization therefore interpolates vertex attributes across the primitive.

Examples include:

- depth `z`;
- color `(r,g,b,a)`;
- normal components;
- texture coordinates `(u,v)`.

The lecture first presents interpolation along triangle edges and then across each scanline. Conceptually:

```text
vertex attributes
   ↓ interpolate along left/right edges
attributes at scanline endpoints
   ↓ interpolate across scanline
attribute at each fragment
```

This explains where fragment inputs come from.

---

## 18. Incremental interpolation

The same optimization pattern appears yet again.

If an attribute varies linearly over screen-space triangle coordinates, then moving one sample in `x` changes it by a constant increment

\[
\frac{d\theta}{dx},
\]

and moving one sample in `y` changes it by

\[
\frac{d\theta}{dy}.
\]

For depth, the lecture starts from the triangle plane

\[
Ax+By+Cz+D=0
\]

and solves for `z`:

\[
z=\frac{-Ax-By-D}{C}.
\]

Then increasing `x` by one changes depth by a constant proportional to `-A/C`, while increasing `y` by one changes it by a constant proportional to `-B/C`.

So instead of recomputing depth from the plane equation at every fragment:

```text
next fragment in x: z += dzdx
next scanline:       update using dzdy and horizontal correction
```

The same idea applies to other interpolated attributes.

> **Rasterization is full of recurrences because neighboring samples are coherent.**

A later texturing chapter will add an important qualification: after perspective projection, some attributes require perspective-correct interpolation rather than naïve screen-space linear interpolation. For this lecture, the essential point is how interpolation and incremental updates fit into rasterization.

---

# Part VII — Why modern GPUs prefer tiles

## 19. The parallelization problem

Scanline rasterization is naturally sequential: one edge position is updated from the previous scanline, and pixels along a segment are processed in order.

Modern GPUs, however, contain many processing units. We would like different screen regions to be handled independently.

This motivates **tile-based** or block-based triangle rasterization.

Divide the screen into small rectangular tiles. Different tiles can then be tested and rasterized in parallel.

The tradeoff is that some incremental information cannot be reused globally across tile boundaries, but the gain in parallelism fits GPU architecture much better.

---

## 20. Edge functions: represent a triangle as three inequalities

Here the implicit-function idea from line rasterization returns in a more powerful form.

Each directed triangle edge defines an implicit **edge function**

\[
E(x,y).
\]

Its sign tells which side of the edge a sample lies on.

For a triangle with consistently ordered vertices, a sample lies inside exactly when it lies on the interior side of **all three** edges:

\[
E_{01}(x,y)<0\;\land\;E_{12}(x,y)<0\;\land\;E_{20}(x,y)<0
\]

for the sign convention used in the lecture (with boundary tie rules handled consistently).

This is a beautiful result:

> **Triangle coverage becomes three sign tests.**

There is no need to walk from one scanline to the next to know whether an arbitrary sample is inside. That makes independent evaluation across many samples and tiles possible.

---

## 21. Tile-based rasterization procedure

A simplified procedure is:

1. determine which tiles might overlap the triangle, for example using its bounding box;
2. for each candidate tile, independently inspect its samples;
3. evaluate the three edge functions;
4. if a sample satisfies all interior tests, generate a fragment;
5. interpolate the fragment attributes.

A real GPU can optimize this much further—for example by rejecting whole tiles or groups of samples when coverage is obvious—but the lecture's conceptual point is the shift from **sequential scan conversion** to **parallel coverage tests**.

---

# Part VIII — The ideas that connect the whole lecture

## 22. Rasterization is discretization plus consistency

The first problem is approximation: continuous geometry must be represented on a discrete grid.

But a rasterizer cannot simply choose “nearby pixels.” It needs deterministic rules so neighboring primitives agree about shared boundaries.

Hence concepts such as:

- dominant-axis stepping;
- midpoint decisions;
- reversibility;
- top-left/shared-edge conventions.

These rules prevent gaps and unintended overlap.

---

## 23. Rasterization is also an optimization lesson

Watch how the lecture repeatedly transforms expensive formulas into cheap updates:

```text
Naïve line:
recompute y = mx+B
        ↓
DDA:
y += m
        ↓
Midpoint:
update an integer decision variable

Triangle edge:
recompute intersection
        ↓
edge walking:
x += dx/dy

Attribute:
recompute from geometry
        ↓
incremental interpolation:
θ += dθ/dx or dθ/dy
```

The mathematical theme is **linearity**. If a quantity changes predictably when coordinates move by one grid step, we can precompute the change and reuse it.

The computational theme is **coherence**. Nearby samples usually have nearby geometric values.

---

## 24. Scanline versus tile-based thinking

These two triangle approaches illustrate a hardware/software tradeoff.

### Scanline

Exploit sequential coherence aggressively.

**Strength:** excellent reuse of information from neighboring samples/rows.

**Weakness:** the sequential dependency makes massive parallelization awkward.

### Tile-based

Give up some cross-tile reuse to create independent blocks of work.

**Strength:** maps naturally onto parallel GPU hardware.

**Weakness:** information may need to be recomputed or initialized separately per tile.

Neither idea is “mathematically more correct.” They are different computational organizations of the same coverage problem.

---

# Part IX — Exam-oriented understanding

## 25. What you should be able to explain

You should be able to answer these without merely repeating definitions:

1. Why rasterization is necessary after geometric projection/clipping.
2. Why a fragment is not automatically the final pixel value.
3. Why shallow lines step primarily in `x` and steep lines primarily in `y`.
4. What is inefficient or inconsistent about the naïve `y=mx+B` algorithm.
5. What DDA improves and what limitations remain.
6. Why the midpoint algorithm considers only `E` and `NE` for `0≤m≤1`.
7. Why an implicit function is useful for deciding which candidate is closer.
8. What the decision variable `d` represents conceptually.
9. Why `d` can be updated using fixed increments.
10. Why integer arithmetic is valuable in rasterization.
11. Why reversibility and shared-edge conventions matter.
12. The difference between 4- and 8-connectivity.
13. The difference between flood fill and boundary fill.
14. Why a triangle can be rasterized scanline by scanline.
15. Why the triangle is split at its middle-`y` vertex in scanline rasterization.
16. Why vertex attributes must be interpolated.
17. How spatial coherence enables incremental interpolation.
18. Why scanline rasterization is difficult to parallelize extensively.
19. How three edge functions define triangle interior.
20. Why tile-based rasterization fits modern GPUs.

---

## 26. Check yourself

### Q1. Why isn't projection already rasterization?
Projection determines where continuous geometry maps relative to the image plane. Rasterization still has to decide which discrete sample locations that geometry covers.

### Q2. What did DDA gain over the naïve line equation?
It reuses the previous `y` and adds the slope rather than repeatedly evaluating `m*x+B`.

### Q3. Why is the midpoint algorithm faster still?
For the restricted slope case, each step is reduced to a sign test and fixed integer-like increments, avoiding repeated floating-point line evaluation and rounding.

### Q4. Why does an implicit line equation help?
Its sign classifies a point by side of the line. The midpoint algorithm needs exactly that classification, not the exact line height.

### Q5. Why must adjacent triangles agree on edge ownership?
Otherwise shared boundary samples can be generated twice or not at all, producing overlap or cracks.

### Q6. What is spatial coherence?
Nearby locations tend to have related geometry and attributes, allowing the next value to be updated cheaply from the current one.

### Q7. Why are triangle attributes interpolated?
Attributes are supplied at vertices, but fragment processing needs values at every generated fragment.

### Q8. Why are edge functions good for parallel rasterization?
A sample's coverage can be decided independently by evaluating three functions at that sample; no sequential scanline history is required.

---

# 27. Final mental model

Remember Lecture 6 as one continuous engineering story:

```text
Geometry is continuous, but the display is discrete.
        ↓
We need a rule for choosing samples.
        ↓
Naïve line equations work but are expensive/inconsistent.
        ↓
DDA exploits coherence.
        ↓
Midpoint rasterization turns geometry into incremental sign tests.
        ↓
Triangle edges require consistent ownership rules.
        ↓
Filled triangles can be processed scanline by scanline.
        ↓
Fragments need interpolated attributes.
        ↓
Those attributes can also be updated incrementally.
        ↓
Sequential coherence is efficient but limits parallelism.
        ↓
Edge functions make coverage independently testable.
        ↓
Tiles let modern GPUs rasterize many screen regions in parallel.
```

The deepest principle is not a particular formula. It is this:

> **Rasterization converts continuous geometry into discrete coverage decisions, and efficient rasterizers exploit linearity and spatial coherence so those decisions can be made with tiny, repeatable computations at enormous scale.**
