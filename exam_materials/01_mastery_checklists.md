# 01 - Mastery Checklists By Lecture

Use these checklists after reading a chapter and before doing mixed exam simulation.

## Lecture 01 - Introduction

- [ ] I can state the core problem this lecture solves.
- [ ] I can explain the data entering the topic.
- [ ] I can explain the operation, algorithm, or transformation.
- [ ] I can name the output representation.
- [ ] I can place the topic in the rendering pipeline.
- [ ] I can connect it to the listed assignment.
- [ ] I can solve a closed-format question about it.
- [ ] I can identify the common trap.

Core chain to recite: `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`

Trap to avoid: Do not confuse an image representation with the geometric cause of the image.

Terms to know:

- [ ] `raster image` - A grid of stored pixel samples; it is already an image, not a 3D scene.
- [ ] `pixel` - A discrete image sample containing color or channel values.
- [ ] `color depth` - The number of bits used to represent color values, controlling precision and memory size.
- [ ] `3D model` - A structured description of geometry and attributes that can generate many possible images.
- [ ] `primitive` - A basic geometric object such as a point, line, or triangle used by the rendering pipeline.
- [ ] `interactive graphics` - Rendering where images must update quickly enough to respond to input or animation.

## Lecture 02 - Rendering Pipeline

- [ ] I can state the core problem this lecture solves.
- [ ] I can explain the data entering the topic.
- [ ] I can explain the operation, algorithm, or transformation.
- [ ] I can name the output representation.
- [ ] I can place the topic in the rendering pipeline.
- [ ] I can connect it to the listed assignment.
- [ ] I can solve a closed-format question about it.
- [ ] I can identify the common trap.

Core chain to recite: `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`

Trap to avoid: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.

Terms to know:

- [ ] `application stage` - CPU-side preparation of models, scene data, interaction, animation, and rendering state.
- [ ] `geometry stage` - Pipeline stage that transforms vertices and prepares primitives.
- [ ] `rasterization` - Conversion of projected primitives into fragment candidates on a sample grid.
- [ ] `fragment` - A candidate pixel contribution produced by rasterization before final tests and blending.
- [ ] `framebuffer` - Memory target that stores color, depth, stencil, or related per-pixel results.
- [ ] `double buffering` - Using front and back buffers so drawing can happen off-screen before display swap.

## Lecture 03 - Geometric Transformations

- [ ] I can state the core problem this lecture solves.
- [ ] I can explain the data entering the topic.
- [ ] I can explain the operation, algorithm, or transformation.
- [ ] I can name the output representation.
- [ ] I can place the topic in the rendering pipeline.
- [ ] I can connect it to the listed assignment.
- [ ] I can solve a closed-format question about it.
- [ ] I can identify the common trap.

Core chain to recite: `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`

Trap to avoid: Do not multiply matrices without naming source space, target space, and order.

Terms to know:

- [ ] `homogeneous coordinates` - Coordinates with an additional component that make translation and projection expressible by matrices.
- [ ] `translation` - A transformation that moves points by an offset; direction vectors are not shifted the same way.
- [ ] `rotation` - A transformation that changes orientation while preserving distances.
- [ ] `scaling` - A transformation that changes size and can distort normals if handled incorrectly.
- [ ] `matrix composition` - Combining transformations by multiplication, where order matters.
- [ ] `normal transformation` - Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling.

## Lecture 04 - Geometric Projection

- [ ] I can state the core problem this lecture solves.
- [ ] I can explain the data entering the topic.
- [ ] I can explain the operation, algorithm, or transformation.
- [ ] I can name the output representation.
- [ ] I can place the topic in the rendering pipeline.
- [ ] I can connect it to the listed assignment.
- [ ] I can solve a closed-format question about it.
- [ ] I can identify the common trap.

Core chain to recite: `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`

Trap to avoid: Do not confuse projection with viewport mapping; the perspective divide sits between them.

Terms to know:

- [ ] `view volume` - The 3D region visible to the camera before mapping to the screen.
- [ ] `orthographic projection` - Projection without perspective foreshortening; parallel lines stay parallel.
- [ ] `perspective projection` - Projection where farther objects appear smaller after division by the homogeneous component.
- [ ] `clip coordinates` - Coordinates produced before clipping and perspective divide.
- [ ] `perspective divide` - Division by w that produces normalized device coordinates.
- [ ] `viewport transformation` - Mapping normalized device coordinates to window or screen coordinates.

## Lecture 05 - Clipping

- [ ] I can state the core problem this lecture solves.
- [ ] I can explain the data entering the topic.
- [ ] I can explain the operation, algorithm, or transformation.
- [ ] I can name the output representation.
- [ ] I can place the topic in the rendering pipeline.
- [ ] I can connect it to the listed assignment.
- [ ] I can solve a closed-format question about it.
- [ ] I can identify the common trap.

Core chain to recite: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`

Trap to avoid: Do not describe clipping as only deletion; crossing primitives can create new vertices.

Terms to know:

- [ ] `clipping` - Removing or cutting geometry outside a valid window, plane, or volume.
- [ ] `Cohen-Sutherland` - Line clipping method using region/outcodes to reject, accept, or clip line segments.
- [ ] `Sutherland-Hodgman` - Polygon clipping method that processes polygon vertices against clipping boundaries.
- [ ] `Cyrus-Beck` - Parametric line clipping method using entering and leaving parameter intervals.
- [ ] `outcode` - A compact code describing where a point lies relative to clipping boundaries.
- [ ] `intersection point` - New boundary point created when a primitive crosses a clipping edge or plane.

## Lecture 06 - Rasterization

- [ ] I can state the core problem this lecture solves.
- [ ] I can explain the data entering the topic.
- [ ] I can explain the operation, algorithm, or transformation.
- [ ] I can name the output representation.
- [ ] I can place the topic in the rendering pipeline.
- [ ] I can connect it to the listed assignment.
- [ ] I can solve a closed-format question about it.
- [ ] I can identify the common trap.

Core chain to recite: `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`

Trap to avoid: Do not call every generated fragment a final pixel.

Terms to know:

- [ ] `scan conversion` - Determining which discrete samples are covered by an ideal geometric primitive.
- [ ] `triangle coverage` - Testing which pixel/sample positions lie inside a triangle.
- [ ] `barycentric coordinates` - Weights relative to triangle vertices used for inside tests and interpolation.
- [ ] `interpolation` - Computing per-fragment values from vertex attributes.
- [ ] `aliasing` - Artifacts caused when continuous signals are sampled too coarsely.
- [ ] `fragment candidate` - A potential contribution to the framebuffer, not yet a guaranteed visible pixel.

## Lecture 07 - Visibility Determination

- [ ] I can state the core problem this lecture solves.
- [ ] I can explain the data entering the topic.
- [ ] I can explain the operation, algorithm, or transformation.
- [ ] I can name the output representation.
- [ ] I can place the topic in the rendering pipeline.
- [ ] I can connect it to the listed assignment.
- [ ] I can solve a closed-format question about it.
- [ ] I can identify the common trap.

Core chain to recite: `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`

Trap to avoid: Do not confuse generating a fragment with proving that it is visible.

Terms to know:

- [ ] `depth buffer` - Per-pixel storage of depth values used to keep the nearest visible fragment.
- [ ] `z-buffer algorithm` - Image-space visibility method comparing fragment depths at each pixel.
- [ ] `Painter's algorithm` - Object-order visibility method based on drawing farther objects before nearer objects.
- [ ] `BSP tree` - Space-partitioning structure that can support visibility ordering.
- [ ] `Warnock algorithm` - Image-space subdivision method for resolving visible surfaces in regions.
- [ ] `ray casting` - Finding visible surfaces by tracing rays from image samples into the scene.

## Lecture 08 - Local Illumination

- [ ] I can state the core problem this lecture solves.
- [ ] I can explain the data entering the topic.
- [ ] I can explain the operation, algorithm, or transformation.
- [ ] I can name the output representation.
- [ ] I can place the topic in the rendering pipeline.
- [ ] I can connect it to the listed assignment.
- [ ] I can solve a closed-format question about it.
- [ ] I can identify the common trap.

Core chain to recite: `surface point + normal + light + view + material -> lighting equation -> shaded color`

Trap to avoid: Do not mix up normal, light direction, and view direction; each changes a different lighting term.

Terms to know:

- [ ] `surface normal` - Vector describing surface orientation and controlling diffuse/specular response.
- [ ] `ambient term` - Approximate base illumination independent of direct light direction.
- [ ] `diffuse reflection` - View-independent light response based on the angle between normal and light direction.
- [ ] `specular reflection` - View-dependent highlight term based on reflection or half-vector alignment.
- [ ] `Phong model` - Local illumination model combining ambient, diffuse, and specular components.
- [ ] `material coefficient` - Parameter controlling how strongly a surface responds to lighting terms.

## Lecture 09 - Texturing

- [ ] I can state the core problem this lecture solves.
- [ ] I can explain the data entering the topic.
- [ ] I can explain the operation, algorithm, or transformation.
- [ ] I can name the output representation.
- [ ] I can place the topic in the rendering pipeline.
- [ ] I can connect it to the listed assignment.
- [ ] I can solve a closed-format question about it.
- [ ] I can identify the common trap.

Core chain to recite: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`

Trap to avoid: Do not reduce texturing to pasting an image onto geometry.

Terms to know:

- [ ] `texture` - Sampled data array used for color, normals, material data, depth, or other shader inputs.
- [ ] `texel` - A stored sample in texture memory.
- [ ] `UV coordinates` - Coordinates that map surface locations to texture space.
- [ ] `filtering` - Rule for reconstructing values between texels, such as nearest or linear filtering.
- [ ] `mipmap` - Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.
- [ ] `environment mapping` - Using texture lookup to approximate surrounding reflections or distant lighting.

## Lecture 10 - Shadows

- [ ] I can state the core problem this lecture solves.
- [ ] I can explain the data entering the topic.
- [ ] I can explain the operation, algorithm, or transformation.
- [ ] I can name the output representation.
- [ ] I can place the topic in the rendering pipeline.
- [ ] I can connect it to the listed assignment.
- [ ] I can solve a closed-format question about it.
- [ ] I can identify the common trap.

Core chain to recite: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`

Trap to avoid: Do not explain a shadow only from the camera view; the key test is light-space visibility.

Terms to know:

- [ ] `shadow` - Reduced direct illumination where an object blocks light from reaching a receiver.
- [ ] `occluder` - Object that blocks light.
- [ ] `receiver` - Surface where the shadow appears.
- [ ] `shadow map` - Depth image rendered from the light's point of view for later visibility comparison.
- [ ] `shadow volume` - Volume of space hidden from a light by an occluder.
- [ ] `projective shadow` - Shadow construction based on projecting geometry onto a receiver.
