# 03 - Matching Tasks

Match each term to the correct role. Use the TSV file for import into tools; use this Markdown file for manual practice.

## Lecture 01 - Introduction

Terms:

1. raster image
2. pixel
3. color depth
4. 3D model
5. primitive
6. interactive graphics

Definitions:

A. A grid of stored pixel samples; it is already an image, not a 3D scene.
B. A discrete image sample containing color or channel values.
C. The number of bits used to represent color values, controlling precision and memory size.
D. A structured description of geometry and attributes that can generate many possible images.
E. A basic geometric object such as a point, line, or triangle used by the rendering pipeline.
F. Rendering where images must update quickly enough to respond to input or animation.

Trap check: Do not confuse an image representation with the geometric cause of the image.

## Lecture 02 - Rendering Pipeline

Terms:

1. application stage
2. geometry stage
3. rasterization
4. fragment
5. framebuffer
6. double buffering

Definitions:

A. CPU-side preparation of models, scene data, interaction, animation, and rendering state.
B. Pipeline stage that transforms vertices and prepares primitives.
C. Conversion of projected primitives into fragment candidates on a sample grid.
D. A candidate pixel contribution produced by rasterization before final tests and blending.
E. Memory target that stores color, depth, stencil, or related per-pixel results.
F. Using front and back buffers so drawing can happen off-screen before display swap.

Trap check: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.

## Lecture 03 - Geometric Transformations

Terms:

1. homogeneous coordinates
2. translation
3. rotation
4. scaling
5. matrix composition
6. normal transformation

Definitions:

A. Coordinates with an additional component that make translation and projection expressible by matrices.
B. A transformation that moves points by an offset; direction vectors are not shifted the same way.
C. A transformation that changes orientation while preserving distances.
D. A transformation that changes size and can distort normals if handled incorrectly.
E. Combining transformations by multiplication, where order matters.
F. Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling.

Trap check: Do not multiply matrices without naming source space, target space, and order.

## Lecture 04 - Geometric Projection

Terms:

1. view volume
2. orthographic projection
3. perspective projection
4. clip coordinates
5. perspective divide
6. viewport transformation

Definitions:

A. The 3D region visible to the camera before mapping to the screen.
B. Projection without perspective foreshortening; parallel lines stay parallel.
C. Projection where farther objects appear smaller after division by the homogeneous component.
D. Coordinates produced before clipping and perspective divide.
E. Division by w that produces normalized device coordinates.
F. Mapping normalized device coordinates to window or screen coordinates.

Trap check: Do not confuse projection with viewport mapping; the perspective divide sits between them.

## Lecture 05 - Clipping

Terms:

1. clipping
2. Cohen-Sutherland
3. Sutherland-Hodgman
4. Cyrus-Beck
5. outcode
6. intersection point

Definitions:

A. Removing or cutting geometry outside a valid window, plane, or volume.
B. Line clipping method using region/outcodes to reject, accept, or clip line segments.
C. Polygon clipping method that processes polygon vertices against clipping boundaries.
D. Parametric line clipping method using entering and leaving parameter intervals.
E. A compact code describing where a point lies relative to clipping boundaries.
F. New boundary point created when a primitive crosses a clipping edge or plane.

Trap check: Do not describe clipping as only deletion; crossing primitives can create new vertices.

## Lecture 06 - Rasterization

Terms:

1. scan conversion
2. triangle coverage
3. barycentric coordinates
4. interpolation
5. aliasing
6. fragment candidate

Definitions:

A. Determining which discrete samples are covered by an ideal geometric primitive.
B. Testing which pixel/sample positions lie inside a triangle.
C. Weights relative to triangle vertices used for inside tests and interpolation.
D. Computing per-fragment values from vertex attributes.
E. Artifacts caused when continuous signals are sampled too coarsely.
F. A potential contribution to the framebuffer, not yet a guaranteed visible pixel.

Trap check: Do not call every generated fragment a final pixel.

## Lecture 07 - Visibility Determination

Terms:

1. depth buffer
2. z-buffer algorithm
3. Painter's algorithm
4. BSP tree
5. Warnock algorithm
6. ray casting

Definitions:

A. Per-pixel storage of depth values used to keep the nearest visible fragment.
B. Image-space visibility method comparing fragment depths at each pixel.
C. Object-order visibility method based on drawing farther objects before nearer objects.
D. Space-partitioning structure that can support visibility ordering.
E. Image-space subdivision method for resolving visible surfaces in regions.
F. Finding visible surfaces by tracing rays from image samples into the scene.

Trap check: Do not confuse generating a fragment with proving that it is visible.

## Lecture 08 - Local Illumination

Terms:

1. surface normal
2. ambient term
3. diffuse reflection
4. specular reflection
5. Phong model
6. material coefficient

Definitions:

A. Vector describing surface orientation and controlling diffuse/specular response.
B. Approximate base illumination independent of direct light direction.
C. View-independent light response based on the angle between normal and light direction.
D. View-dependent highlight term based on reflection or half-vector alignment.
E. Local illumination model combining ambient, diffuse, and specular components.
F. Parameter controlling how strongly a surface responds to lighting terms.

Trap check: Do not mix up normal, light direction, and view direction; each changes a different lighting term.

## Lecture 09 - Texturing

Terms:

1. texture
2. texel
3. UV coordinates
4. filtering
5. mipmap
6. environment mapping

Definitions:

A. Sampled data array used for color, normals, material data, depth, or other shader inputs.
B. A stored sample in texture memory.
C. Coordinates that map surface locations to texture space.
D. Rule for reconstructing values between texels, such as nearest or linear filtering.
E. Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.
F. Using texture lookup to approximate surrounding reflections or distant lighting.

Trap check: Do not reduce texturing to pasting an image onto geometry.

## Lecture 10 - Shadows

Terms:

1. shadow
2. occluder
3. receiver
4. shadow map
5. shadow volume
6. projective shadow

Definitions:

A. Reduced direct illumination where an object blocks light from reaching a receiver.
B. Object that blocks light.
C. Surface where the shadow appears.
D. Depth image rendered from the light's point of view for later visibility comparison.
E. Volume of space hidden from a light by an occluder.
F. Shadow construction based on projecting geometry onto a receiver.

Trap check: Do not explain a shadow only from the camera view; the key test is light-space visibility.
