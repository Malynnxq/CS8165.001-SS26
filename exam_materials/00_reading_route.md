# 00 - Reading Route

Use this route when you want a strict, reading-first path from raw course files to exam-level performance.

## The Order

1. Read one lecture in `lecture_readers/markdown/` or the combined PDF.
2. Open the matching raw source chunk in `course_text_parts/03_lectures/`.
3. Check every slide cue against the Professor-style explanation.
4. Open the matching assignment text and extracted source package.
5. Do closed-format practice: cloze, matching, sequencing, MC, diagram labels, OpenGL debugging.
6. Log every wrong answer in the mistake log.
7. Repeat with changed wording from the repetition variants.

## Completion Rule

A topic is not finished when it feels familiar. It is finished when you can identify it under new wording, connect it to the pipeline, solve a closed-format task, and explain the common trap.

## Lecture 01 - Introduction

Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.

Concept chain: `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`

Assignment connection: 00 Introduction to C++

Formula or compact rule: `image memory = width x height x bits per pixel, then divide by 8 for bytes`

High-risk trap: Do not confuse an image representation with the geometric cause of the image.

Before moving on, you must be able to match each term to its role:

- `raster image` - A grid of stored pixel samples; it is already an image, not a 3D scene.
- `pixel` - A discrete image sample containing color or channel values.
- `color depth` - The number of bits used to represent color values, controlling precision and memory size.
- `3D model` - A structured description of geometry and attributes that can generate many possible images.
- `primitive` - A basic geometric object such as a point, line, or triangle used by the rendering pipeline.
- `interactive graphics` - Rendering where images must update quickly enough to respond to input or animation.

## Lecture 02 - Rendering Pipeline

Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.

Concept chain: `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`

Assignment connection: 01 Rendering Pipeline

Formula or compact rule: `vertices -> primitives -> fragments -> tests -> pixels`

High-risk trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.

Before moving on, you must be able to match each term to its role:

- `application stage` - CPU-side preparation of models, scene data, interaction, animation, and rendering state.
- `geometry stage` - Pipeline stage that transforms vertices and prepares primitives.
- `rasterization` - Conversion of projected primitives into fragment candidates on a sample grid.
- `fragment` - A candidate pixel contribution produced by rasterization before final tests and blending.
- `framebuffer` - Memory target that stores color, depth, stencil, or related per-pixel results.
- `double buffering` - Using front and back buffers so drawing can happen off-screen before display swap.

## Lecture 03 - Geometric Transformations

Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.

Concept chain: `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`

Assignment connection: 03 Geometric Transformations

Formula or compact rule: `p_world = M_model * p_model; p_view = V * p_world`

High-risk trap: Do not multiply matrices without naming source space, target space, and order.

Before moving on, you must be able to match each term to its role:

- `homogeneous coordinates` - Coordinates with an additional component that make translation and projection expressible by matrices.
- `translation` - A transformation that moves points by an offset; direction vectors are not shifted the same way.
- `rotation` - A transformation that changes orientation while preserving distances.
- `scaling` - A transformation that changes size and can distort normals if handled incorrectly.
- `matrix composition` - Combining transformations by multiplication, where order matters.
- `normal transformation` - Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling.

## Lecture 04 - Geometric Projection

Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.

Concept chain: `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`

Assignment connection: 04 Projections and Clipping

Formula or compact rule: `p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w`

High-risk trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.

Before moving on, you must be able to match each term to its role:

- `view volume` - The 3D region visible to the camera before mapping to the screen.
- `orthographic projection` - Projection without perspective foreshortening; parallel lines stay parallel.
- `perspective projection` - Projection where farther objects appear smaller after division by the homogeneous component.
- `clip coordinates` - Coordinates produced before clipping and perspective divide.
- `perspective divide` - Division by w that produces normalized device coordinates.
- `viewport transformation` - Mapping normalized device coordinates to window or screen coordinates.

## Lecture 05 - Clipping

Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.

Concept chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`

Assignment connection: 04 Projections and Clipping

Formula or compact rule: `line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval`

High-risk trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.

Before moving on, you must be able to match each term to its role:

- `clipping` - Removing or cutting geometry outside a valid window, plane, or volume.
- `Cohen-Sutherland` - Line clipping method using region/outcodes to reject, accept, or clip line segments.
- `Sutherland-Hodgman` - Polygon clipping method that processes polygon vertices against clipping boundaries.
- `Cyrus-Beck` - Parametric line clipping method using entering and leaving parameter intervals.
- `outcode` - A compact code describing where a point lies relative to clipping boundaries.
- `intersection point` - New boundary point created when a primitive crosses a clipping edge or plane.

## Lecture 06 - Rasterization

Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.

Concept chain: `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`

Assignment connection: 05 Rasterization

Formula or compact rule: `attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1`

High-risk trap: Do not call every generated fragment a final pixel.

Before moving on, you must be able to match each term to its role:

- `scan conversion` - Determining which discrete samples are covered by an ideal geometric primitive.
- `triangle coverage` - Testing which pixel/sample positions lie inside a triangle.
- `barycentric coordinates` - Weights relative to triangle vertices used for inside tests and interpolation.
- `interpolation` - Computing per-fragment values from vertex attributes.
- `aliasing` - Artifacts caused when continuous signals are sampled too coarsely.
- `fragment candidate` - A potential contribution to the framebuffer, not yet a guaranteed visible pixel.

## Lecture 07 - Visibility Determination

Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.

Concept chain: `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`

Assignment connection: Rasterization and integrated rendering tasks

Formula or compact rule: `visible fragment = candidate with passing depth/visibility test at the sample`

High-risk trap: Do not confuse generating a fragment with proving that it is visible.

Before moving on, you must be able to match each term to its role:

- `depth buffer` - Per-pixel storage of depth values used to keep the nearest visible fragment.
- `z-buffer algorithm` - Image-space visibility method comparing fragment depths at each pixel.
- `Painter's algorithm` - Object-order visibility method based on drawing farther objects before nearer objects.
- `BSP tree` - Space-partitioning structure that can support visibility ordering.
- `Warnock algorithm` - Image-space subdivision method for resolving visible surfaces in regions.
- `ray casting` - Finding visible surfaces by tracing rays from image samples into the scene.

## Lecture 08 - Local Illumination

Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.

Concept chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`

Assignment connection: Rendering contest and shader-related tasks

Formula or compact rule: `color = ambient + diffuse + specular`

High-risk trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.

Before moving on, you must be able to match each term to its role:

- `surface normal` - Vector describing surface orientation and controlling diffuse/specular response.
- `ambient term` - Approximate base illumination independent of direct light direction.
- `diffuse reflection` - View-independent light response based on the angle between normal and light direction.
- `specular reflection` - View-dependent highlight term based on reflection or half-vector alignment.
- `Phong model` - Local illumination model combining ambient, diffuse, and specular components.
- `material coefficient` - Parameter controlling how strongly a surface responds to lighting terms.

## Lecture 09 - Texturing

Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.

Concept chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`

Assignment connection: Rendering contest and texture/shader tasks

Formula or compact rule: `sampled value = texture(sampler, uv), then shader interprets the value`

High-risk trap: Do not reduce texturing to pasting an image onto geometry.

Before moving on, you must be able to match each term to its role:

- `texture` - Sampled data array used for color, normals, material data, depth, or other shader inputs.
- `texel` - A stored sample in texture memory.
- `UV coordinates` - Coordinates that map surface locations to texture space.
- `filtering` - Rule for reconstructing values between texels, such as nearest or linear filtering.
- `mipmap` - Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.
- `environment mapping` - Using texture lookup to approximate surrounding reflections or distant lighting.

## Lecture 10 - Shadows

Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.

Concept chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`

Assignment connection: Rendering contest and integrated lighting tasks

Formula or compact rule: `point is shadowed if something is closer to the light along the same light ray`

High-risk trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.

Before moving on, you must be able to match each term to its role:

- `shadow` - Reduced direct illumination where an object blocks light from reaching a receiver.
- `occluder` - Object that blocks light.
- `receiver` - Surface where the shadow appears.
- `shadow map` - Depth image rendered from the light's point of view for later visibility comparison.
- `shadow volume` - Volume of space hidden from a light by an occluder.
- `projective shadow` - Shadow construction based on projecting geometry onto a receiver.
