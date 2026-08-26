# Chapter 10 — Shadows

> **Purpose.** This chapter reconstructs Lecture 10 as a coherent lesson. Rather than memorizing several shadow algorithms, we will ask one question repeatedly: **how can the renderer decide whether a surface point can see the light source?** Different shadow techniques answer that question using projected geometry, precomputed textures, explicit shadow volumes, or depth maps rendered from the light.
>
> **Primary course source:** `course_text_parts/03_lectures/10_shadows.txt` (Lecture 10 slides, July 2026).

## 1. Why shadows matter

A shadow is not just a dark decoration. It provides strong information about spatial relationships.

From a shadow we can infer:

- whether an object touches the ground or floats above it;
- which object lies between a light and another object;
- approximate relative positions and distances;
- shape and orientation of surfaces;
- mood and visual atmosphere.

This is why scenes with correct geometry but no shadows can still look strangely flat.

The essential physical condition is simple:

> A point is shadowed with respect to a light if another object blocks the path from that point to the light.

Everything in this chapter is an approximation or computational reformulation of that condition.

---

# Part I — Basic vocabulary

## 2. Occluder and receiver

A **shadow caster** or **occluder** is an object that blocks light.

A **shadow receiver** is a surface on which the reduced illumination becomes visible.

The same object can be both. That produces **self-shadowing**.

For example, on a bent arm, one part of the arm may block light from reaching another part of the same arm.

This distinction becomes important because some simple algorithms work only when caster and receiver are treated as separate objects.

---

## 3. Hard shadows, umbra, and penumbra

A point light is modeled as one infinitesimal position. A receiver point either has an unobstructed path to that point or it does not.

That produces an idealized **hard shadow** with a sharp boundary.

An area light occupies a finite region. From a receiver point, the occluder may block:

- all of the light source → **umbra**;
- only part of the light source → **penumbra**;
- none of it → fully illuminated region.

So soft shadows are fundamentally about **partial visibility of an extended light source**.

The size and softness depend on geometry: light size and relative distances between light, caster, and receiver.

---

## 4. Shadows belong to global light transport

Lecture 8 used a local illumination model such as Phong. It essentially assumed that if a light direction exists, the light reaches the point.

But in reality we need a visibility term:

\[
V(P,L)=
\begin{cases}
1,&\text{light visible from }P\\
0,&\text{light blocked}
\end{cases}
\]

Then a direct-light term becomes conceptually

\[
I_{direct}=V(P,L)\,I_{local}.
\]

For an area light, `V` can be fractional after sampling multiple points on the light.

Thus shadows are the missing **light-visibility test** between geometry and illumination.

---

# Part II — The simplest approximation: ground-plane shadows

## 5. Static shadow polygons

The crudest approach is to represent a shadow as an ordinary dark polygon placed on a receiver such as the ground.

For a game car, for example, one might place a dark flattened shape below the car.

This can be convincing when:

- the receiver is approximately planar;
- the caster stays close to it;
- motion is fast enough that inaccuracies are not noticed;
- realism is not critical.

But it is not a true geometric shadow computation. The dark polygon may extend into places where no actual shadow should exist.

---

## 6. Why z-fighting appears

If the shadow polygon lies exactly on the receiving ground polygon, both can map to nearly identical depth values.

The depth buffer may alternate between them, creating **z-fighting**.

This connects directly to Lecture 7.

A common workaround is to offset the shadow slightly. But too much offset causes the shadow to appear detached or leak over unrelated geometry.

This is already a recurring shadow-rendering theme:

> Small numerical biases solve one artifact but can create another.

---

# Part III — Projected shadow geometry

## 7. Project the caster onto a plane from the light

A more accurate ground-plane technique projects each caster vertex along the line from the light onto the receiver plane.

Suppose the receiver is the plane

\[
z=0.
\]

Let the light position be `L` and a caster point be `P`.

The shadow point `S` lies on the line through the light and the caster point.

One parameterization is

\[
S=P-\alpha L
\]

under the lecture's coordinate setup. Choose `α` so that the resulting shadow point satisfies

\[
S_z=0.
\]

This converts each object vertex into a projected shadow vertex.

The operation can be represented by a matrix, which means the whole caster can be rendered again with a **shadow projection matrix**.

---

## 8. Why this is useful

The algorithm can be implemented as:

```text
render object normally
↓
modify transformation with shadow-projection matrix
↓
render object again in dark/blended shadow color
```

This gives a shadow whose shape follows the caster much better than a fixed blob.

But it has important restrictions:

- receiver must typically be planar;
- self-shadowing is not handled;
- multiple receiver surfaces are difficult;
- projected geometry may overlap in problematic ways;
- soft shadows are not naturally produced.

So the method is best understood as a special-case geometric trick.

---

# Part IV — Precompute static lighting: light maps

## 9. When nothing moves, do the expensive work beforehand

If lights and scene geometry are static, shadows do not need to be recomputed every frame.

We can run an expensive offline algorithm—possibly ray tracing—to determine illumination and shadowing, then store the result in a **light map**.

At runtime:

```text
surface UV
→ light-map lookup
→ precomputed lighting/shadow factor
```

This is a classic time–memory tradeoff:

> Spend computation during preprocessing and memory at runtime to avoid expensive per-frame shadow calculations.

---

## 10. Why light maps can contain soft shadows

For an area light, cast multiple rays from a receiver point to different positions on the light.

If, for example, 75% of those rays are blocked, the point receives roughly 25% of the unoccluded direct contribution in this simplified sampling model.

Store that result in the light map.

Filtering the map can further smooth the appearance.

The disadvantage is obvious: move the light or important geometry, and the precomputed shadow no longer matches the scene.

---

# Part V — Shadow volumes

## 11. Think of a shadow as a region in 3D space

Instead of projecting a shadow onto one specific receiver, imagine the entire region behind an occluder that is hidden from the light.

That region is the **shadow volume**.

Any visible scene point inside it should be treated as shadowed.

This representation is much more general than a ground-plane polygon because the shadow is defined in space, not on one receiving plane.

---

## 12. Constructing the volume from silhouette edges

Consider the object from the **light's** point of view.

A silhouette edge lies between:

- a face oriented toward the light;
- a face oriented away from the light.

These edges form the boundary of the caster as seen by the light.

Extrude each silhouette edge away from the light. The extruded quads form the side walls of a shadow volume.

Conceptually:

```text
light
  ↓
shadow caster silhouette
  ↓ extrude away from light
3D shadow volume
```

This is closely related to the back-face and silhouette reasoning from Lecture 7.

---

## 13. How do we know whether a visible point lies inside?

Imagine the camera ray from the eye to a visible surface point.

As the ray crosses shadow-volume boundaries, it enters and leaves shadowed regions.

Under a suitable convention, we can maintain a counter:

- crossing one orientation of shadow-volume face increments it;
- crossing the opposite orientation decrements it.

If the counter at the visible point is nonzero, the point lies inside a shadow volume.

This is analogous to point-inside tests based on boundary crossings.

---

# Part VI — The stencil buffer makes shadow volumes practical

## 14. What is the stencil buffer doing here?

The stencil buffer is another per-pixel framebuffer attachment, similar conceptually to color and depth, but it stores small integer values used for masking/counting operations.

Shadow volumes use it to store how many relevant volume-boundary crossings occur before the visible surface.

A simplified multi-pass procedure is:

1. render scene with ambient contribution;
2. render shadow-volume faces while updating stencil values;
3. render direct light only where the stencil says the visible point is outside shadow.

The lecture describes incrementing/decrementing stencil values for front/back shadow-volume faces.

---

## 15. Why depth testing matters during stencil construction

We care only about volume intersections between the camera and the visible scene surface.

Depth testing lets stencil updates correspond to relevant shadow-volume surfaces relative to the already-known scene depth.

This is an elegant reuse of the visibility infrastructure from Lecture 7:

```text
scene depth
+ shadow-volume geometry
+ stencil counting
→ light visibility mask
```

---

## 16. Strengths and weaknesses of shadow volumes

Strengths:

- geometrically sharp, accurate hard-shadow boundaries;
- receiver geometry can be complex;
- dynamic shadows are possible;
- resolution is not limited by a shadow texture.

Weaknesses:

- silhouette extraction and volume construction cost work;
- geometry count can become large;
- robust handling of near/far clipping and camera-inside-volume cases is subtle;
- stencil range is finite;
- caster geometry generally needs to form suitable closed volumes.

So shadow volumes trade image-resolution artifacts for geometric complexity.

---

# Part VII — Shadow maps

## 17. The central insight: render the scene from the light

Shadow mapping gives perhaps the cleanest conceptual answer to the shadow question.

Recall the z-buffer:

> From the camera, which surface is closest at each pixel?

Now ask the same question from the light:

> From the light, which surface is closest in each light-image direction?

Render the scene from the light's viewpoint, but store only depth.

The resulting depth texture is the **shadow map**.

It records the nearest surface visible to the light.

---

## 18. Two-pass shadow mapping

### Pass 1 — light pass

Use the light as the camera.

For every visible direction, store nearest depth:

```text
light view + projection
→ rasterize scene
→ depth buffer
→ shadow map
```

### Pass 2 — camera pass

Render normally from the camera.

For each fragment `P`:

1. transform `P` into the light's coordinate/clip space;
2. project it into shadow-map coordinates `(x',y')`;
3. compute its light-space depth `z'`;
4. fetch the stored shadow-map depth at `(x',y')`;
5. compare them.

If

\[
z' > z_{shadowmap}
\]

by more than an allowed tolerance, another surface was closer to the light, so the fragment is shadowed.

If the depths match, the fragment is the surface the light “saw,” so it is illuminated.

---

## 19. The deepest connection to Lecture 7

A shadow map is essentially a **z-buffer from the light source**.

Camera visibility asks:

\[
\text{What is nearest to the camera?}
\]

Shadow visibility asks:

\[
\text{What is nearest to the light?}
\]

That means the same depth-buffer machinery solves two related visibility problems.

This is why shadow mapping maps so naturally onto rasterization hardware.

---

# Part VIII — Coordinate transformations in shadow mapping

## 20. A camera fragment must be re-expressed in light space

A fragment is being rendered from the camera's perspective, but the shadow map uses the light's perspective.

Therefore world-space point `P` must undergo the light's transformation:

\[
P_{lightClip}=M_{lightProj}M_{lightView}P_{world}.
\]

After perspective division and mapping to texture coordinates, we get something like

\[
(s,t,z_{light}).
\]

Then `(s,t)` indexes the shadow map and `z_light` is compared to the stored depth.

This is a direct application of Lectures 3, 4, and 9:

- coordinate transformations;
- projection;
- texture lookup.

Shadow mapping is therefore not a new isolated mechanism—it combines previously learned pieces.

---

# Part IX — Shadow acne and depth bias

## 21. Why a surface can incorrectly shadow itself

Ideally, when rendering a surface point that generated the shadow-map depth, the two depths should be identical.

In practice they may differ slightly because of:

- finite depth precision;
- rasterization/sample differences;
- different projections/resolutions;
- numerical rounding.

Then the camera-pass fragment can appear microscopically behind the stored depth and fail the comparison.

The result is false self-shadowing, often called **shadow acne**.

The lecture describes this as the bias problem. fileciteturn43file0

---

## 22. Add a depth bias

Instead of testing simply

\[
z' > z_{map},
\]

allow a tolerance:

\[
z' > z_{map}+\text{bias}.
\]

A small bias suppresses self-shadowing caused by numerical error.

But there is no universally perfect value.

Too small:

- acne remains.

Too large:

- the shadow appears detached from the caster;
- contact regions become incorrectly illuminated.

This artifact is often called **peter-panning**.

Thus bias selection is a precision tradeoff, not a magic fix.

---

# Part X — Shadow-map aliasing

## 23. One shadow texel can represent a large visible area

The shadow map has finite resolution.

A region seen by the camera may correspond to only a few shadow-map texels. Then the shadow boundary becomes blocky or unstable.

This is conceptually similar to texture minification from Lecture 9.

But ordinary texture filtering cannot simply average depth values and expect a correct visibility result.

Why?

A depth value is not a color. Averaging two blocker depths creates a synthetic depth that may correspond to no actual surface.

---

## 24. Percentage-Closer Filtering (PCF)

Instead of averaging **depths**, perform several depth comparisons and average the **binary visibility results**.

For neighboring shadow-map samples:

\[
V_i=
\begin{cases}
1,& z'\le z_i+\text{bias}\\
0,& z'>z_i+\text{bias}
\end{cases}
\]

Then

\[
V_{PCF}=\frac{1}{N}\sum_iV_i.
\]

A value near `1` means mostly illuminated; near `0` means mostly shadowed.

This softens jagged boundaries and approximates a penumbra-like transition.

The lecture explicitly emphasizes that PCF filters the **results of shadow tests**, because filtering raw depth values is not meaningful for this purpose. fileciteturn43file0

---

## 25. Why a larger PCF kernel looks softer

A 1-sample comparison gives a hard binary boundary.

A 5×5 kernel compares 25 neighboring shadow texels. Near an edge, some samples say illuminated and some shadowed, producing an intermediate value.

A larger kernel blends over a broader region and can imitate softer shadows.

But this is only an approximation to true area-light visibility: physically correct penumbra size depends on light size and scene geometry, not just a fixed image-space kernel.

---

# Part XI — Compare the methods by representation

## 26. One physical problem, several computational representations

| Method | Representation of shadow | Best intuition |
|---|---|---|
| Static blob/polygon | dark receiver geometry | fake the visible dark region |
| Projected shadow | transformed caster geometry | project caster onto receiver |
| Light map | precomputed texture | store shadow/lighting offline |
| Shadow volume | 3D occluded region | test whether point lies inside light-blocked volume |
| Shadow map | light-space depth texture | test whether light can see the point |

This is the most useful way to remember the lecture.

---

## 27. Static versus dynamic scenes

Another organizing axis is **when** the calculation happens.

### Static

If geometry and lights do not move, expensive work can be precomputed.

Examples:

- light maps;
- fixed shadow polygons.

### Dynamic

If objects or lights move, the shadow representation must be updated.

Examples:

- dynamic projected shadows;
- shadow volumes generated per frame;
- shadow maps rendered per frame.

The more dynamic the scene, the more attractive GPU-friendly image-space techniques become.

---

# Part XII — Connections to earlier lectures

## 28. Lecture 3/4: transformations and projection

Projected ground shadows and shadow maps both depend on transforming points into another coordinate system.

Shadow maps require a full light view/projection transform.

---

## 29. Lecture 7: visibility and depth buffers

Shadow maps are depth buffers from the light.

Shadow volumes also rely on depth and visibility of the camera-rendered scene.

---

## 30. Lecture 8: illumination

A shadow is not primarily “paint black.” It modulates the direct-light contribution.

Conceptually:

\[
I=I_{ambient}+V(P,L)(I_{diffuse}+I_{specular}).
\]

This explains why shadowed surfaces may still receive ambient/indirect approximation rather than becoming perfectly black.

---

## 31. Lecture 9: textures and filtering

A shadow map is a texture containing depth data.

The camera pass computes texture coordinates in light space and samples it.

PCF is a specialized filtering strategy applied to comparison results.

---

# Part XIII — Worked examples

## 32. Shadow-map test

Suppose a fragment transformed into light space has depth

\[
z'=0.65.
\]

The shadow map stores

\[
z_{map}=0.40.
\]

This means the light first encountered some surface at depth `0.40`. The current fragment is farther away at `0.65`.

Therefore another object blocks the light, so the fragment is shadowed.

If instead

\[
z'=0.40001
\]

while the stored depth is `0.40`, that tiny difference may be mere numerical error. A bias can prevent false self-shadowing.

---

## 33. PCF example

Suppose a 3×3 PCF kernel gives comparison results

```text
1 1 1
1 1 0
0 0 0
```

Five of nine samples say illuminated.

Then

\[
V\approx\frac59\approx0.56.
\]

The fragment receives roughly 56% of the direct-light contribution in this simple filtering interpretation.

This is how a binary shadow map can produce a visually smooth edge.

---

# Part XIV — Common confusions

## 34. “A shadow map stores shadows”

More precisely, it stores **depth from the light**.

The shadow status is computed later by comparing a camera fragment's light-space depth to that stored depth.

---

## 35. “PCF averages depth”

No. For this method, averaging raw depth is not the intended operation.

PCF performs several **depth comparisons** and filters the resulting visibility values.

---

## 36. “A larger PCF kernel gives physically correct soft shadows”

Not necessarily. It gives a softer-looking boundary. True soft-shadow width depends on extended-light visibility and scene geometry.

---

## 37. “Ambient light should also disappear in shadow”

In the simplified Phong-style interpretation, a shadow commonly removes/reduces the direct light from a particular light source while an ambient approximation can remain.

---

## 38. “Shadow volume and shadow map are two versions of the same representation”

No.

A shadow volume represents an occluded **3D region geometrically**.

A shadow map represents the nearest surfaces visible from the light as an **image/depth texture**.

---

# Part XV — Exam-oriented mastery

## 39. What you should be able to explain

You should be able to answer from understanding:

1. Why shadows improve depth and spatial perception.
2. Occluder versus receiver and the meaning of self-shadowing.
3. Hard shadow, umbra, and penumbra.
4. Why area lights naturally produce soft shadows.
5. Why shadows can be interpreted as light visibility.
6. How static shadow polygons approximate a shadow and their limitations.
7. Why projected planar shadows can be represented by a transformation matrix.
8. Why projected-shadow techniques struggle with arbitrary receivers and self-shadowing.
9. Why light maps are useful for static scenes.
10. How area-light sampling can be baked into light maps.
11. What a shadow volume represents.
12. How silhouette edges from the light define shadow-volume side walls.
13. How stencil counting determines whether a visible point lies inside a shadow volume.
14. Why shadow volumes can produce resolution-independent hard boundaries.
15. Why shadow volumes are geometrically expensive.
16. What a shadow map stores.
17. Why rendering from the light produces exactly the information needed for shadow testing.
18. The two passes of shadow mapping.
19. Why a camera fragment must be transformed into light space.
20. Why shadow mapping is closely related to the z-buffer algorithm.
21. What causes shadow acne.
22. Why depth bias helps and why too much bias is harmful.
23. Why finite shadow-map resolution causes aliasing.
24. Why filtering depth values directly is problematic.
25. How percentage-closer filtering works.
26. The differences between projected shadows, light maps, shadow volumes, and shadow maps.

---

# 40. Final mental model

Remember Lecture 10 as a sequence of increasingly general answers to one question:

```text
Can this surface point see the light?
        ↓
Cheapest fake:
place a dark polygon
        ↓
Planar geometry:
project the caster onto the receiver
        ↓
Static scene:
precompute lighting into a light map
        ↓
Geometric dynamic solution:
build the full shadowed volume
        ↓
GPU-friendly image-space solution:
render depth from the light
        ↓
transform camera fragment into light space
        ↓
compare its depth with the shadow map
        ↓
blocked → suppress direct light
visible → apply direct light
        ↓
finite precision → bias problem
finite resolution → aliasing
        ↓
PCF filters multiple visibility tests
```

The deepest idea of the chapter is:

> **A shadow is a visibility problem between a surface point and a light source. Every shadow algorithm differs mainly in how it represents and evaluates that visibility.**
