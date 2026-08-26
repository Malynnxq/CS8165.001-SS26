# Lecture 04 - Geometric Projection

Primary source: `course_text_parts/03_lectures/04_geometric-projection.txt`

A beginner-friendly textbook chapter for a student who missed the lecture. It explains projection as a chain from camera geometry to screen coordinates, introduces the required vocabulary before the matrix derivations, and uses the lecture's own examples and OpenGL functions as anchors.

## How to use this chapter

Read it in order. The central dependency chain is:

`3D point in view space -> projection -> clip coordinates -> perspective division -> normalized device coordinates -> viewport transform -> screen coordinates`

If one arrow is unclear, do not memorize the formulas yet. First make sure you understand what representation enters the step, what leaves it, and why the step is needed.

## Source anchors

- Slides 2 and 4-18: why projection is needed, linear perspective, similar triangles, and the historical development of perspective construction.
- Slides 19-31: planar projection families, orthographic/axonometric/oblique projection, perspective projection, vanishing points.
- Slides 32-37: camera modeling, view volume, field of view, aspect ratio, near/far clipping planes.
- Slides 39-42: `glm::perspective`, `glm::frustum`, `glm::ortho`.
- Slides 43-48: orthographic projection as translation + scaling + handedness change into a canonical view volume.
- Slides 49-54: perspective projection derivation, depth mapping, homogeneous `w`, and perspective division.
- Slides 55-57 and following: viewport transformation and mapping normalized coordinates to a pixel rectangle.

## 1. Why projection exists at all

Source focus: 2, 6, 16

A 3D model contains points with three spatial coordinates. A screen, however, is a two-dimensional surface. Before rasterization can decide which pixels a triangle covers, the renderer must answer a more basic question: where does each 3D point appear in the image?

Projection is the rule that maps 3D positions to a 2D image representation. In the lecture, this is described geometrically using projectors: straight lines running from the object toward the image plane. Depending on the projection type, these lines are either parallel or converge toward a common center of projection.

The key visual phenomenon of perspective is depth-dependent size. If an object moves farther away from the eye, its image becomes smaller. The Renaissance perspective slides are therefore not decorative history. They motivate the exact geometric rule computer graphics later expresses with matrices.

### Similar triangles are the core geometric idea

The lecture's Alberti construction uses similar triangles. If an object of height `H` is at distance `z` from the eye and the image plane is at distance `d`, the projected height is proportional to

`H_projected / H = d / z`.

The exact sign convention depends on the coordinate system, but the important relation is this: projected size is inversely proportional to distance. That single fact explains perspective shortening.

### Concrete example

If two identical poles are viewed with perspective projection and one is twice as far from the camera, its projected height is roughly half as large, assuming both are measured along the same viewing geometry.

### Check yourself

Why does perspective projection make distant objects smaller, while a parallel projection does not?

## 2. Projection rays, projection plane, and the two major families

Source focus: 20-22

A planar geometric projection has two ingredients: straight projection rays and a flat projection plane. To project a point, follow its projection ray until it intersects the projection plane. That intersection is the point's image.

There are two major families.

In **perspective projection**, all projectors meet at one center of projection, usually interpreted as the eye or camera center. Distance from that center changes the projected size of an object.

In **parallel projection**, all projectors have the same direction. They do not converge. Because the projection direction does not depend on how far the object is from the camera, objects do not shrink with distance in the same way.

This distinction is more fundamental than the names of the subtypes. Whenever you encounter a projection method, first ask: do the rays converge at one point or remain parallel?

### Concrete example

Architectural renderings often use perspective because they should resemble human vision. Engineering drawings often use orthographic projection because measurements and scale matter more than realism.

### Check yourself

What property of the projection rays distinguishes perspective from parallel projection?

## 3. Parallel projections: orthographic, axonometric, and oblique

Source focus: 23-28

Parallel projection contains several useful subtypes. They differ mainly in the relation between the projection direction and the projection plane.

In **orthographic projection**, the projectors are perpendicular to the projection plane. Front, top, and side views are the simplest examples. Because the mapping does not introduce perspective shortening, dimensions parallel to the image plane can be measured directly. The tradeoff is that the result looks less like normal vision and may require several views to communicate 3D structure.

An **axonometric projection** is still orthographic in the sense that projection rays are perpendicular to the image plane, but the object or plane orientation is chosen so that several faces are visible at once. Isometric projection is the special case where the three principal axes are shortened equally. Dimetric and trimetric projections use two or three different shortening factors.

In an **oblique projection**, projection rays are not perpendicular to the image plane. One main face can remain undistorted while depth is shown along a slanted direction. Cavalier projection keeps full depth scale; cabinet projection reduces the depth contribution, making the drawing look less stretched.

### Why these exist

The projection family is chosen according to what information should be preserved. Orthographic views preserve measurement. Axonometric views preserve a useful technical impression of several faces. Oblique views can preserve one important face exactly while still showing depth.

### Check yourself

Why can an orthographic engineering drawing be better for measurement than a perspective rendering?

## 4. Perspective projection and vanishing points

Source focus: 29-31

Perspective projection produces the visual cues we associate with photographs and human vision. Parallel world-space lines that recede away from the camera may meet at a vanishing point in the image. Object scale depends on depth, so exact length measurements are generally lost.

One-, two-, and three-point perspective are not separate projection algorithms. They describe how many principal directions of a box produce finite vanishing points under a particular camera/object orientation. Rotate the box and the apparent number of vanishing points can change even though the underlying projection remains the same perspective projection.

This is an important conceptual distinction: vanishing points are a consequence of geometry and orientation, not a different GPU pipeline stage.

### Concrete example

A road viewed straight ahead often gives a strong one-point perspective: road edges converge toward one distant point. Turn the camera relative to a building, and two horizontal principal directions can converge toward different vanishing points.

### Check yourself

Why can rotating a cube change the number of visible vanishing points without changing the projection type?

## 5. A virtual camera is more than a position

Source focus: 32-37

To project a scene, the renderer needs a camera model. The lecture lists several camera parameters: position, orientation, projection type, field of view, aspect ratio, and near/far distances.

Position and orientation determine **view space**: coordinates relative to the camera. Projection then acts on those view-space coordinates.

The **field of view** controls how much of the scene fits into the image. A larger field of view shows more of the scene but increases perspective distortion, similar to a wide-angle lens.

The **aspect ratio** is image width divided by image height. It links the horizontal and vertical extent of the viewing volume. If the projection matrix assumes one aspect ratio while the output window uses another, shapes become stretched.

The **near** and **far clipping planes** limit the depth range that belongs to the camera's view volume. Geometry before the near plane or beyond the far plane is outside the allowed volume. These limits are also important later for depth-buffer precision.

### The frustum

For perspective projection, the natural viewing region is pyramid-like. Computer graphics commonly uses a truncated rectangular pyramid called a **view frustum** because it matches a rectangular screen and is easy to clip against using planes.

For orthographic projection, the view volume is a rectangular box rather than a frustum, because the projection rays stay parallel.

### Check yourself

What four parameters besides camera position/orientation strongly determine a perspective view volume?

## 6. OpenGL/GLM projection specification

Source focus: 39-42

The course uses GLM to construct projection matrices.

`glm::perspective(fovy, aspect, near, far)` creates a symmetric perspective frustum from a vertical field of view, image aspect ratio, and near/far distances.

`glm::frustum(left, right, bottom, top, near, far)` specifies the frustum directly and can create asymmetric perspective views.

`glm::ortho(left, right, bottom, top, near, far)` creates an orthographic view volume.

These functions do not directly produce pixels. They produce a **projection matrix** that transforms view-space coordinates into clip coordinates. Later fixed-function stages perform clipping, perspective division, and viewport mapping.

### Concrete example

If a window is 1600x900, its aspect ratio is 1600/900. Using an aspect ratio of 1.0 in the projection matrix while rendering into that wide window causes the image geometry to appear horizontally distorted.

### Check yourself

What is the conceptual difference between `glm::perspective` and `glm::ortho`, even though both return 4x4 matrices?

## 7. The canonical view volume: why projection matrices normalize geometry

Source focus: 43-45, 49-50

The GPU would be harder to design if every camera produced a completely different clipping volume. Instead, projection transforms the user-defined view volume into a standard, **canonical view volume**.

The lecture represents this canonical volume as a cube with normalized bounds around `[-1, 1]`. The exact handedness conventions shown in the slides are part of the course's derivation, but the general idea is more important: arbitrary camera geometry is converted into one standard coordinate region so later clipping and rasterization can use uniform rules.

So projection has two jobs at once:

1. create the desired visual mapping from 3D toward 2D, and
2. normalize the chosen camera volume into a standard form for the GPU.

That is why projection matrices contain more structure than simply 'delete z'.

### Check yourself

Why is converting every camera's view volume into one canonical volume useful for the later pipeline?

## 8. Orthographic projection derivation: translate, scale, flip

Source focus: 45-48

Orthographic projection is the easier derivation because there is no depth-dependent shrinking. The source view volume is a rectangular cuboid described by left/right, bottom/top, and near/far limits. The goal is to map that cuboid into the canonical cube.

The lecture decomposes this into familiar transformations from Lecture 3.

First, **translate** the cuboid so its center moves to the origin. If the x-range is `[l, r]`, its center is `(l+r)/2`, so the x translation is the negative of that value. The same logic applies to y and z.

Second, **scale** the centered cuboid so each half-extent becomes 1. Along x, the full width is `r-l`, so the scale factor is `2/(r-l)`. The same pattern gives `2/(t-b)` and `2/(f-n)` for the other dimensions.

Third, the lecture applies a z-axis sign change to match its chosen handedness/canonical-depth convention.

The resulting matrix is therefore not mysterious. It is just a compact composition of translate + scale + depth-orientation adjustment.

### Why z is still kept

Even though the final image is 2D, the pipeline does not immediately throw away depth. Depth is still needed for clipping and visibility tests. Orthographic projection changes the coordinate system while preserving useful depth information for later stages.

### Concrete example

If an orthographic camera views x from -10 to 10, the projection must map -10 to -1, 0 to 0, and 10 to 1. That mapping is exactly a scale by 1/10 along x when the range is already centered.

### Check yourself

Why can orthographic projection be built from ordinary affine transformations, while perspective projection needs something extra?

## 9. Perspective projection: the extra ingredient is homogeneous division

Source focus: 49-54

Perspective cannot be represented as an ordinary 3D affine transformation because the projected x and y coordinates must depend on depth. A distant point must be divided by a larger depth-related value than a near point.

Homogeneous coordinates solve this. A 4D clip-space point contains `(x_c, y_c, z_c, w_c)`. After clipping, the GPU performs **perspective division**:

`x_ndc = x_c / w_c`

`y_ndc = y_c / w_c`

`z_ndc = z_c / w_c`

The perspective matrix is constructed so that `w_c` is related to the original view-space depth. Therefore the divide automatically creates perspective shortening.

This is the central conceptual point of the perspective derivation. The matrix itself does not finish the perspective effect; the matrix prepares a meaningful `w`, and the later divide by `w` creates the nonlinear depth-dependent scaling.

### Why the bottom row matters

The lecture's perspective matrix contains a row that makes `w` depend on `-z`. That is exactly what an ordinary affine matrix does not do. After multiplication, x and y are still homogeneous quantities. Only after division by w do they become normalized Cartesian coordinates.

### Concrete example

Suppose two points have the same view-space x but different depths. After projection, their clip-space x values may be similar in form, but the farther point receives a larger magnitude of `w`. Dividing by that larger `w` produces a smaller normalized x, moving the point closer to the image center.

### Check yourself

Why is perspective division essential to perspective projection rather than just an implementation detail?

## 10. Mapping near and far depth into normalized depth

Source focus: 51-52

Perspective projection must also transform depth. The lecture chooses coefficients so that the near plane maps to one normalized depth boundary and the far plane maps to the other.

This is done by solving for two constants in the depth part of the projection matrix. The important reasoning is boundary matching: choose the matrix so that the known input depths `z=-n` and `z=-f` become the desired normalized values after division by `w`.

You do not need to treat the constants as magic. They are the unique coefficients that satisfy the chosen near/far mapping under the perspective-divide rule.

A consequence is that perspective depth is **nonlinear** with respect to view-space distance. Equal world-space depth intervals do not receive equal normalized-depth intervals. This becomes important when you study depth-buffer precision and z-fighting.

### Check yourself

Why is it useful to derive the depth coefficients by forcing the near and far planes to map to chosen boundary values?

## 11. Field of view determines the x/y scaling terms

Source focus: 53-54

The x and y terms of the perspective matrix are derived from the frustum geometry. At the near plane, the half-height is connected to the vertical field of view by a tangent relation.

If `fovy` is the vertical field of view and `n` is the near distance, then approximately

`top = n * tan(fovy/2)`.

To normalize that top boundary to y=1, the projection must scale by the reciprocal of the tangent. That is why `cot(fovy/2)` appears in the perspective matrix.

The horizontal scale is additionally adjusted by the aspect ratio. A wider image needs a wider horizontal field for the same vertical field of view.

So the matrix entries are not arbitrary constants: they directly encode camera geometry.

### Check yourself

Why does increasing `fovy` make objects appear smaller on screen, all else equal?

## 12. Viewport transformation: normalized coordinates become pixels

Source focus: 55-57 and following

After projection and perspective division, positions are expressed in **normalized device coordinates** (NDC). Their x and y values lie in a standardized interval such as `[-1, 1]` for the canonical view.

But a real window is measured in pixels, for example 800x600. The **viewport transformation** maps normalized coordinates into a chosen pixel rectangle.

`glViewport(x, y, width, height)` defines that rectangle. Conceptually, the mapping performs a scale and translation:

- NDC x=-1 maps to the left edge of the viewport,
- NDC x=1 maps to the right edge,
- NDC y=-1 maps to the bottom edge,
- NDC y=1 maps to the top edge.

If the window is resized, the viewport should be updated. Usually the projection aspect ratio must also be updated, otherwise a circle can become an ellipse because the camera mapping and pixel rectangle disagree.

### Concrete example

For `glViewport(0, 0, 800, 600)`, NDC x=0 lies halfway across the viewport at roughly x=400. NDC y=0 lies halfway up at roughly y=300.

### Check yourself

What is the difference between projection and viewport transformation?

## 13. Put the complete camera-to-screen chain together

Source focus: chapter as a whole

Start with a point in world space. The view transformation rewrites it relative to the camera, producing view-space coordinates. The projection matrix maps that point into clip coordinates. Clipping decides whether the point or its primitive lies inside the allowed view volume. Perspective division converts clip coordinates into normalized device coordinates. The viewport transformation maps those normalized coordinates into screen coordinates used for rasterization.

The complete chain is:

`world space -> view space -> clip space -> NDC -> screen coordinates -> rasterization`

For perspective projection, the crucial nonlinear step is the division by `w`. For orthographic projection, `w` does not create depth-dependent shrinking, so objects retain their scale with distance.

Later lectures fit directly after this chapter. Clipping operates on the projected viewing volume. Rasterization consumes screen-space primitives. Visibility uses depth values preserved through projection. Therefore projection is the bridge between 3D camera geometry and the discrete 2D image pipeline.

### Concrete example

A cube corner might begin as a world-space point `(2, 1, -8)`. The view matrix expresses it relative to the camera. The perspective matrix creates clip coordinates with a depth-dependent `w`. Dividing by `w` gives normalized coordinates. The viewport maps them into a pixel position. Only then can rasterization decide which fragments the cube's triangles generate around that position.

### Check yourself

Explain the entire path from a 3D point in view space to a 2D screen coordinate, naming every representation change.

## Minimum concept map

`camera parameters -> view volume -> projection matrix -> clip coordinates -> clipping -> perspective division -> normalized device coordinates -> viewport transform -> screen coordinates`

Key contrast:

`orthographic: parallel rays, no depth-dependent shrinking`

`perspective: rays meet at camera center, divide by w creates depth-dependent shrinking`

If you can explain those two lines and the full coordinate chain without looking at the slides, you understand the backbone of Lecture 4.