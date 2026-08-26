# Chapter 7 — Visibility Determination

> **Purpose.** This chapter reconstructs Lecture 7 for a student who missed the lecture. The algorithms are not presented as an isolated list. Instead, we begin with the visibility problem and progressively ask *where* visibility can be solved: on geometry, on regions of space, on image regions, per fragment, or by tracing rays.
>
> **Primary course source:** `course_text_parts/03_lectures/07_visibility-determination.txt` (Lecture 7 slides, 9 June 2026).

## 1. The problem: projection does not tell us what is visible

Suppose two triangles project onto the same screen position. Projection tells us where both triangles appear, and rasterization can generate fragments for both. But the final image should normally show only the surface closest to the camera at that position.

This is the **visibility determination** problem:

> Given a camera and a scene, determine which parts of the scene are actually visible from that camera.

A surface can fail to contribute because:

- another object lies in front of it;
- another part of the same object lies in front of it;
- for a closed opaque object, the surface faces away from the camera;
- it lies outside the relevant viewing region.

The literature therefore uses two complementary descriptions:

- **visible-surface determination:** find what can be seen;
- **hidden-surface removal:** remove what cannot be seen.

They describe the same underlying problem from opposite directions.

A good visibility algorithm should be general, fast enough that the visibility test is cheaper than rendering everything unnecessarily, and robust against numerical error.

---

## 2. The first major distinction: object space or image space?

There are two broad strategies.

### Object-based visibility

Analyze geometry before or independently of rasterization. Compare surfaces, sort them, split them, or classify their orientation.

Conceptually:

```text
scene geometry
    ↓ geometric visibility reasoning
visible geometry
    ↓ rasterization
image
```

The advantage is that invisible geometry can sometimes be eliminated before expensive rasterization. The difficulty is that geometric relationships between many objects can become complicated and expensive.

### Image-based visibility

Rasterize candidate geometry and decide visibility at image/sample locations.

Conceptually:

```text
scene geometry
    ↓ rasterization
candidate fragments
    ↓ per-sample visibility test
visible fragments
```

The depth buffer is the canonical example.

This distinction organizes much of the lecture. The later algorithms differ mainly in **where they store and resolve visibility information**.

---

# Part I — Object-based algorithms

## 3. Painter's algorithm: draw from back to front

Imagine painting a landscape. You first paint the distant sky and mountains, then nearer trees, then a person in the foreground. Later paint naturally covers earlier paint.

The Painter's algorithm applies exactly this idea:

1. assign/sort polygons by depth;
2. render the farthest first;
3. render progressively nearer polygons on top.

If the ordering is correct, ordinary overwriting of the color buffer solves visibility.

### Why this is attractive

It is simple and needs no dedicated depth buffer.

### Why it is not generally sufficient

A polygon does not necessarily have one depth. One end may be nearer than another. Worse, polygons can overlap cyclically:

```text
A is in front of B somewhere,
B is in front of C somewhere,
C is in front of A somewhere.
```

Then no single global ordering `A,B,C` can be correct everywhere.

The cure is to split polygons until a valid order exists, but that makes the method substantially more complicated.

**Core lesson:** visibility cannot always be reduced to assigning one scalar depth to an entire polygon.

---

## 4. Weiler–Atherton as visibility by clipping

You met Weiler–Atherton in the clipping lecture. Here the same geometric machinery is used for visibility.

The idea is roughly:

1. sort polygons front-to-back;
2. choose the foremost polygon;
3. use its projected region as a clip/occlusion region for polygons behind it;
4. keep the unoccluded pieces;
5. continue recursively/iteratively.

Unlike a simple Painter's ordering, this can calculate exact visible polygon pieces.

That is powerful for line/wireframe rendering because hidden portions can be removed geometrically before drawing.

The cost is complexity: polygon splitting, clipping, numerical robustness, and poor parallelization make this unattractive for the massively parallel real-time GPU pipeline.

---

## 5. Back-face culling: remove surfaces that cannot face the camera

Before solving object-versus-object occlusion, we can often eliminate some surfaces for free.

For a closed opaque object, a polygon whose outward-facing normal points away from the camera cannot be directly visible.

Let

- `n` = face normal;
- `v` = consistently defined viewing direction.

The dot product

\[
s=v\cdot n
\]

indicates their relative orientation. Under the sign convention used in the lecture, one sign denotes front-facing and the opposite sign back-facing.

### Why the dot product works

Recall

\[
v\cdot n=\|v\|\|n\|\cos\theta.
\]

Its sign tells whether the angle is acute or obtuse. Therefore it tells which side of the surface the camera direction lies on.

A polygon normal can be obtained from two consistently ordered edge vectors:

\[
n=e_0\times e_1.
\]

This also explains why **vertex winding order matters**: reversing the order reverses the cross product and therefore the normal.

### What back-face culling does *not* solve

It does not determine whether a front-facing surface is hidden behind another object. It only removes surfaces that are impossible to see because of their own orientation.

So think of it as an inexpensive early filter, not a complete visibility algorithm.

---

## 6. Roberts' algorithm: visible lines as a geometric problem

Roberts' algorithm historically targeted visible-line determination for convex 3D objects.

Its conceptual sequence is:

1. remove self-hidden faces with back-face culling;
2. construct occluding/shadow volumes from silhouettes;
3. clip candidate edges against those volumes;
4. reconnect the surviving visible edge pieces.

This made sense for vector displays and remains conceptually relevant to non-photorealistic line rendering.

Its weakness is again geometric complexity: arbitrary non-convex scenes need decomposition or more elaborate handling.

---

# Part II — Organizing space before asking visibility questions

## 7. Why spatial data structures appear here

If every object is compared with every other object, the work can approach quadratic growth.

A different strategy is to organize space so that large irrelevant groups can be ignored together.

Examples introduced by the lecture include:

- quadtrees for recursive 2D subdivision;
- octrees for recursive 3D subdivision;
- kd-trees for binary spatial partitioning;
- BSP trees for recursive partitioning by planes.

The important idea is not the names. It is this:

> **Spend preprocessing/storage to make later spatial queries cheaper.**

That idea is fundamental not only for visibility but also collision detection and ray tracing.

---

## 8. BSP trees: recursively divide space with planes

**BSP** means **Binary Space Partitioning**.

In 3D, choose a plane. It divides space into two half-spaces:

```text
             splitting plane
          /                 \
     front space         back space
```

Each side can then be subdivided recursively by another plane, producing a binary tree.

A node conceptually stores:

- a splitting plane;
- geometry lying on/associated with that plane;
- a front subtree;
- a back subtree.

### What happens to a polygon during construction?

Relative to a splitting plane, a polygon can be:

- entirely in front;
- entirely behind;
- coincident with the plane;
- intersecting the plane.

An intersecting polygon may have to be split into front and back pieces.

This is the price of creating a spatial ordering structure.

---

## 9. How BSP traversal creates a depth order

Suppose the camera lies on the front side of a node's splitting plane.

For back-to-front rendering, geometry behind the plane should be processed first, then geometry on the plane, then geometry on the camera side.

If the camera lies on the opposite side, reverse the traversal.

Thus the tree can produce a view-dependent Painter-like ordering without sorting every polygon from scratch each frame.

This is particularly attractive for mostly static scenes because tree construction can be precomputed.

### Splitting-plane choice matters

A poor plane can create many polygon splits or a badly unbalanced tree. A useful heuristic tries to balance competing goals:

- split few polygons;
- divide geometry reasonably evenly;
- often reuse existing polygon planes.

There is no universally perfect local choice.

### View-frustum pruning

A spatial hierarchy gives another benefit: if an entire subtree lies outside the camera's view frustum, the subtree can be skipped. One test can therefore eliminate many objects.

This is the recurring hierarchy principle:

> **Reject groups, not individual primitives, whenever possible.**

---

# Part III — Divide the image instead: Warnock

## 10. The spatial-coherence insight

Nearby image samples often see the same surface. Instead of resolving visibility independently at every pixel immediately, Warnock's algorithm asks whether a larger image region is already simple enough to solve.

Start with the whole viewport.

If visibility is ambiguous, split it into four smaller rectangles. Continue recursively only where necessary.

This is an image-space divide-and-conquer algorithm.

---

## 11. What counts as a simple Warnock region?

For a viewport region `R`, visibility is trivial in cases such as:

- no polygon affects `R` → draw background;
- only one polygon affects `R` → draw that polygon where relevant;
- one polygon completely covers `R` → fill with that polygon if it is the visible one;
- multiple polygons affect `R`, but one covering polygon is definitely in front of all others → use it.

If none of these conditions can be established, subdivide `R` into four regions and repeat.

Eventually a region can become as small as a pixel, where the ambiguity must be resolved at the finest image scale.

### Why this can save work

Large simple image areas are resolved with one decision instead of many pixel-level decisions.

### Why it lost importance for mainstream GPU rendering

Its recursive irregular workload is less natural for conventional graphics hardware than the highly regular depth-buffer test.

---

# Part IV — The depth buffer

## 12. The key idea: remember the nearest depth seen so far

The depth-buffer algorithm solves visibility independently at each framebuffer location.

In addition to color, maintain a 2D array of depth values—the **depth buffer** or **z-buffer**.

At each sample location, it stores the depth of the currently closest accepted fragment.

Initialize it to the far/background depth. Then for every generated fragment:

```text
if fragment is closer than stored depth:
    replace stored depth
    replace stored color
else:
    discard fragment
```

For the common OpenGL convention described in the lecture, normalized depth lies in `[0,1]`, with values nearer `0` closer to the near plane and values nearer `1` toward the far plane. With `GL_LESS`, a fragment passes when its depth is smaller than the stored value.

---

## 13. Why the depth buffer is so powerful

The crucial property is **order independence for opaque surfaces**.

Suppose three opaque fragments at the same sample have depths

```text
0.8, 0.2, 0.5
```

No matter which order they arrive, the final stored depth is `0.2`.

The algorithm does not need a global polygon sort. It reduces visibility to many independent local minimum operations.

That maps extremely well to raster hardware.

It also works for anything that can generate fragments, not only polygons.

---

## 14. Connect Lecture 6 to Lecture 7

Lecture 6 explained that rasterization interpolates depth across a triangle and generates fragments.

Now you can see **why that interpolated depth was necessary**:

```text
triangle vertices have z/depth
        ↓ rasterization interpolates depth
fragment gets depth value
        ↓ depth test
compare against depth buffer
        ↓
keep nearest visible fragment
```

This is an important conceptual bridge between the two lectures. Rasterization determines *coverage*; the depth test resolves *occlusion* among covered fragments.

---

## 15. OpenGL depth testing

The lecture's OpenGL setup corresponds conceptually to:

```cpp
glClearDepth(1.0);
glEnable(GL_DEPTH_TEST);
glDepthFunc(GL_LESS);
```

Before drawing a new frame, the depth buffer must be cleared:

```cpp
glClear(GL_DEPTH_BUFFER_BIT);
```

If you forget this, depths from a previous frame can incorrectly occlude new geometry.

The comparison function is configurable because some rendering techniques need relationships other than “strictly smaller.”

---

# Part V — Finite depth precision and z-fighting

## 16. A depth buffer stores finite numbers

A mathematical depth is continuous, but a depth buffer has finite precision—commonly represented with a fixed number of bits or a floating format.

Therefore sufficiently close depths can become indistinguishable after quantization.

If two surfaces repeatedly map to the same or nearly the same representable depth, tiny numerical differences can cause one to win at some samples/frames and the other elsewhere.

The visible result flickers or forms interference-like patterns. This is **z-fighting**.

---

## 17. Why perspective makes depth precision nonuniform

Under perspective projection, the mapping from view-space distance to stored depth is nonlinear. The lecture emphasizes that precision is denser near the near clipping plane and sparser toward the far plane.

So the choice of near/far planes affects numerical robustness.

A particularly useful practical rule is:

> Do not choose an unnecessarily tiny near-plane distance or unnecessarily huge depth range.

Moving the near plane farther from the camera and/or bringing the far plane closer can improve effective precision.

Other mitigations include:

- higher-precision depth formats;
- polygon offset for nearly coplanar surfaces such as decals;
- multiple rendering ranges/passes in specialized cases.

---

# Part VI — Why transparency breaks the simple z-buffer story

## 18. Opaque visibility asks “which is nearest?”

For opaque objects, once the nearest surface is known, farther surfaces at that sample do not contribute to the final color.

Transparency is different. A transparent foreground surface and a background surface can **both** contribute.

Therefore one nearest-depth value is not enough to describe all color contributions.

This is why ordinary alpha blending generally requires special ordering.

---

## 19. Standard transparent rendering

A common strategy in the lecture is:

1. render opaque geometry first with normal depth testing/writing;
2. enable blending;
3. render transparent geometry afterward;
4. keep depth testing so transparent fragments hidden behind opaque geometry can be rejected;
5. avoid letting ordinary transparent layers destroy the depth information needed for subsequent layers, depending on the chosen method.

With standard source-alpha blending, the familiar conceptual form is

\[
C_{out}=\alpha C_{src}+(1-\alpha)C_{dst}.
\]

Because this operation is generally order-dependent, transparent surfaces normally need an appropriate back-to-front ordering.

So the depth buffer solved opaque visibility elegantly, but transparency reintroduces an ordering problem.

---

## 20. Depth peeling: recover multiple depth layers

**Order-independent transparency** techniques try to avoid explicitly sorting transparent objects.

The lecture introduces **depth peeling**.

Think of the scene along one pixel ray as layers:

```text
camera
  ↓
layer 0: nearest transparent fragment
layer 1: next fragment
layer 2: next fragment
...
```

First render the nearest layer. In the next pass, reject that already extracted layer and find the nearest fragment *behind* it. Repeat.

The passes therefore “peel” the scene front-to-back one depth layer at a time.

After collecting the layers, combine their colors in the correct compositing order.

The advantage is that object submission order no longer has to provide the correct transparency order. The disadvantage is multiple rendering passes and extra storage/work.

---

## 21. Haloes: reuse depth information for illustration

The lecture also shows a nonstandard use of the depth buffer: creating **haloes** around foreground wireframe lines to improve spatial understanding.

Conceptually:

1. render thick wireframe lines into depth only;
2. render thinner visible lines into color;
3. the thick depth footprint creates a safety margin that suppresses background lines near foreground lines.

This is a useful lesson beyond the specific effect:

> A depth buffer is not merely an automatic hidden-surface mechanism; it is a general image-space representation of scene depth that can be exploited creatively.

---

# Part VII — Ray casting: reverse the question

## 22. Rasterization asks primitive → samples

The rasterization pipeline essentially asks:

> For this primitive, which image samples does it cover?

Ray casting reverses the direction:

> For this image sample, which scene surface is encountered first?

For every pixel/sample:

1. generate a ray from the camera through the image plane;
2. intersect it with scene objects;
3. select the closest valid intersection;
4. shade that intersection;
5. store the resulting color.

Visibility is therefore built directly into the nearest-intersection query.

---

## 23. Parameterizing a ray

A ray can be written as

\[
p(t)=e+t\,d,
\]

where

- `e` is the eye/ray origin;
- `d` is the direction;
- `t` tells how far along the ray we travel.

The lecture expresses the direction using a point `s` on the image plane:

\[
d=s-e.
\]

Then

\[
p(t)=e+t(s-e).
\]

For positive `t`, smaller valid values correspond to intersections closer to the ray origin.

Therefore visibility becomes:

> **Find the smallest positive intersection parameter `t`.**

This is the ray-casting analogue of the z-buffer's “keep the smallest depth.” Both solve the same physical question using different representations.

---

## 24. Generating a ray through a pixel

Assume a camera with an orthonormal basis

\[
\{u,v,w\},
\]

where `u` and `v` span the image plane and `w` describes the camera's third axis.

The image plane has left/right limits `l,r`, bottom/top limits `b,t`, and a distance `d` from the eye.

For pixel indices `(x,y)`, first find the corresponding sample position on the image plane. The lecture centers the ray through the pixel/sample rather than simply using a corner.

Then express that image-plane point in the camera basis and subtract the eye position to obtain the ray direction.

Conceptually:

```text
pixel index
   ↓ map to position on image plane
image-plane sample s
   ↓
direction = s - eye
   ↓
ray p(t) = eye + t*direction
```

This connects directly back to the camera coordinate systems and projection concepts from Lectures 3 and 4.

---

## 25. Ray–object intersections

For every ray, we need the nearest surface intersection.

### Implicit surfaces

If a surface is described by

\[
f(x,y,z)=0,
\]

substitute the ray:

\[
f(e+t d)=0.
\]

This produces an equation in `t`.

For example:

- a plane gives a linear equation;
- a sphere gives a quadratic equation.

Solve for valid `t` values and retain the smallest positive one.

### Triangles

One conceptual approach from the lecture is:

1. intersect the ray with the plane containing the triangle;
2. test whether the intersection lies inside the triangle, for example with barycentric coordinates.

The expensive part is scale: naïvely testing every pixel ray against every scene object performs enormous numbers of intersection tests.

This is why the spatial data structures introduced earlier become relevant again. A BVH, kd-tree, BSP tree, or related hierarchy can reject large groups of objects before detailed intersection testing.

---

## 26. Ray marching versus analytic intersection

The lecture contrasts analytic intersection with an iterative approach that advances along the ray in small steps.

A naïve ray marcher does roughly:

```text
t = 0
repeat:
    p = origin + t*direction
    test whether p intersects/is inside something
    t += epsilon
```

This is conceptually simple but accuracy and performance depend strongly on step size and the type of scene representation.

Analytic intersection, when available, can directly solve for the exact candidate `t` values instead of sampling many positions along the ray.

Do not confuse **ray casting** (the visibility/rendering framework) with **ray marching** (one possible numerical strategy for progressing along a ray).

---

# Part VIII — One visibility problem, several representations

## 27. Compare the major algorithms by what they store

| Method | Main representation | Central question |
|---|---|---|
| Painter's algorithm | ordered polygons | Which polygon should be drawn later? |
| Weiler–Atherton visibility | clipped polygon pieces | Which geometric pieces remain unoccluded? |
| Back-face culling | face normals/orientation | Can this face possibly point toward the camera? |
| BSP tree | hierarchical spatial half-spaces | Which regions/geometry should be traversed and in what order? |
| Warnock | recursively subdivided image regions | Is visibility already simple in this region? |
| Z-buffer | nearest depth per sample | Is this fragment closer than the stored one? |
| Depth peeling | multiple ordered depth layers | What is the next visible layer behind the previous one? |
| Ray casting | nearest positive ray intersection | What surface does this viewing ray hit first? |

This table is the conceptual core of the lecture. The algorithms are not arbitrary inventions; each chooses a different domain in which visibility becomes easier to decide.

---

## 28. The recurring optimization principle: reject work early or locally

Visibility algorithms improve rendering by avoiding or resolving unnecessary work at different scales:

```text
face orientation
→ reject a polygon with back-face culling

spatial hierarchy
→ reject an entire subtree

Warnock region
→ resolve many pixels with one region decision

z-buffer
→ reject a hidden fragment locally

ray hierarchy
→ reject many objects before intersection tests
```

The best location for a visibility decision depends on the representation, hardware, scene dynamics, and rendering technique.

---

# Part IX — Exam-oriented understanding

## 29. What you should be able to explain

You should be able to answer these from understanding rather than memorization:

1. What visibility determination solves and why projection/rasterization alone are insufficient.
2. The difference between object-based and image-based visibility algorithms.
3. Why Painter's algorithm needs back-to-front ordering.
4. Why a single depth value per polygon is not generally sufficient.
5. How clipping can be used for exact geometric visibility.
6. What back-face culling removes and what it does not remove.
7. Why vertex order affects face normals and culling.
8. Why spatial data structures help visibility queries.
9. How a BSP plane divides space and how polygons are classified during construction.
10. How camera position changes BSP traversal order.
11. Why splitting-plane selection affects BSP performance.
12. How Warnock exploits image-space coherence.
13. The meaning of the depth buffer and the fragment depth test.
14. Why opaque depth buffering does not require object sorting.
15. Why finite/nonuniform depth precision produces z-fighting.
16. Why near/far plane selection affects depth precision.
17. Why ordinary transparency is order-dependent.
18. What depth peeling means conceptually.
19. How the halo technique exploits depth information.
20. How ray casting turns visibility into the smallest-positive-`t` problem.
21. How a camera ray is generated through an image sample.
22. How implicit-surface intersection reduces to solving `f(e+td)=0`.
23. Why spatial acceleration is crucial for ray casting.

---

## 30. Check yourself

### Q1. Why isn't back-face culling a complete hidden-surface algorithm?
A front-facing polygon can still be hidden by another object or another part of the scene.

### Q2. Why does the z-buffer work regardless of opaque object submission order?
At each sample it retains the nearest passing depth. Taking the minimum depth produces the same final nearest surface regardless of arrival order, assuming the same depth convention/test and ordinary opaque rendering.

### Q3. Why can transparent objects not be handled by simply keeping the nearest fragment?
Because farther transparent/background surfaces may still contribute to the final color through blending.

### Q4. What problem does a BSP tree solve that a flat object list does not?
It organizes geometry hierarchically in space, allowing view-dependent ordering and rejection of whole spatial subtrees.

### Q5. What is Warnock's key question?
Whether visibility within the current image region is simple enough to resolve directly; if not, subdivide the region.

### Q6. What do z-buffering and ray casting have in common?
Both ultimately seek the nearest visible surface at each image sample. Z-buffering discovers candidates by rasterizing primitives; ray casting discovers them by intersecting a viewing ray with scene geometry.

### Q7. Why is the smallest positive ray parameter important?
Positive `t` lies in front of the ray origin, and the smallest positive valid `t` is the first surface encountered from the camera.

---

# 31. Final mental model

Remember Lecture 7 as a sequence of increasingly different answers to one question:

```text
Which surface can the camera actually see?
        ↓
Can geometry be ordered?
→ Painter's algorithm
        ↓
Can hidden pieces be cut away geometrically?
→ clipping / Weiler–Atherton
        ↓
Can impossible faces be rejected immediately?
→ back-face culling
        ↓
Can space itself be organized hierarchically?
→ BSP trees
        ↓
Can large image regions be solved together?
→ Warnock
        ↓
Can visibility be reduced to one local value per sample?
→ depth buffer
        ↓
What if several depth layers contribute?
→ transparency / depth peeling
        ↓
Can we ask directly what each viewing ray hits first?
→ ray casting
```

The deepest connection is this:

> **Visibility determination is the problem of choosing the camera-relevant subset of scene information. Different algorithms become efficient by representing that choice at different levels: faces, polygon pieces, spatial regions, image regions, depth samples, or rays.**
