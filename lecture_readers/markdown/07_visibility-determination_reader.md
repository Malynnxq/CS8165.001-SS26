# Lecture 07 - Visibility Determination

Source chunk: `course_text_parts/03_lectures/07_visibility-determination.txt`
Extracted slide pages in source chunk: 69

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture asks which surfaces are visible from a viewpoint. Rasterization can generate many fragment candidates, but visibility decides which ones should affect the image.

## How To Read This Lecture

- First read the big picture and the mental models.
- Then open the source chunk and compare the slide bullets to the commentary.
- After each section, answer the check question without notes.
- If the check feels vague, revisit the source pages listed for that section.

## Per-Slide Commentary

Every extracted slide page gets its own reading note. This is the part to use when the original PDF is too terse or visually dense.

### Page 1 - Visual or title slide

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Visual or title slide' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Visual or title slide. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer links this visual or title page to the closest surrounding concept slide and names the topic transition it introduces.

Common trap: Do not invent details that are not visible in the extracted text; use this page as a boundary marker and rely on adjacent slides for technical content.

Check yourself: Can you turn 'Visual or title slide' into a causal sentence instead of repeating the slide title?

### Page 2 - Visibility Determination

Source cue: - Problem / - Given scene objects and virtual camera / - Determine visible parts of scene objects / - Not occluded by same scene object / - Not occluded by other scene objects

Professor-style explanation: The slide 'Visibility Determination' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Problem / - Given scene objects and virtual camera / - Determine visible parts of scene objects / - Not occluded by same scene object / - Not occluded by other scene objects. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Visibility Determination. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Problem / - Given scene objects and virtual camera / - Determine visible parts of scene objects / - Not occluded by same scene object / - Not occluded by other scene objects. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Visibility Determination' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Visibility Determination' works per object, per image region, per ray, or per fragment?

### Page 3 - Object-Based Algorithms

Source cue: - Geometry-based analysis of scene objects before rasterization / - Compare each scene object against all other scene objects / - Determine visible parts based on virtual camera / - Rasterize the visible scene parts / For each object in sceneObjects

Professor-style explanation: The slide 'Object-Based Algorithms' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Geometry-based analysis of scene objects before rasterization / - Compare each scene object against all other scene objects / - Determine visible parts based on virtual camera / - Rasterize the visible scene parts / For each object in sceneObjects. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Object-Based Algorithms. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Geometry-based analysis of scene objects before rasterization / - Compare each scene object against all other scene objects / - Determine visible parts based on virtual camera / - Rasterize the visible scene parts / For each object in sceneObjects. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Object-Based Algorithms' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Object-Based Algorithms'?

### Page 4 - Image-Based Algorithms

Source cue: - Pixel-based analysis of scene objects after rasterization / - Rasterize scene objects based on image resolution / - Investigate for each pixel which scene object is visible / For each pixel in outputRaster / // Determine which scene object is visible at this pixel

Professor-style explanation: The slide 'Image-Based Algorithms' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Pixel-based analysis of scene objects after rasterization / - Rasterize scene objects based on image resolution / - Investigate for each pixel which scene object is visible / For each pixel in outputRaster / // Determine which scene object is visible at this pixel. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Image-Based Algorithms. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Pixel-based analysis of scene objects after rasterization / - Rasterize scene objects based on image resolution / - Investigate for each pixel which scene object is visible / For each pixel in outputRaster / // Determine which scene object is visible at this pixel. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Image-Based Algorithms' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Image-Based Algorithms'?

### Page 5 - 7.1 Object-Based Algorithms

Source cue: 7.2 Binary Space Partitioning / 7.3 Warnock Algorithm / 7.4 Depth Buffer Algorithm / 7.5 Depth Buffer Extensions / 7.6 Ray Casting

Professor-style explanation: The slide '7.1 Object-Based Algorithms' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: 7.2 Binary Space Partitioning / 7.3 Warnock Algorithm / 7.4 Depth Buffer Algorithm / 7.5 Depth Buffer Extensions / 7.6 Ray Casting. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about 7.1 Object-Based Algorithms. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: 7.2 Binary Space Partitioning / 7.3 Warnock Algorithm / 7.4 Depth Buffer Algorithm / 7.5 Depth Buffer Extensions / 7.6 Ray Casting. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for '7.1 Object-Based Algorithms' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether '7.1 Object-Based Algorithms' works per object, per image region, per ray, or per fragment?

### Page 6 - 7.1 Object-Based Algorithms

Source cue: Exploiting sorting and clipping

Professor-style explanation: The slide '7.1 Object-Based Algorithms' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: Exploiting sorting and clipping. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion. For examination purposes, the important content is classification: inside, outside, crossing, intersection point, and the newly produced primitive segment or polygon.

Technical commentary: This slide is about 7.1 Object-Based Algorithms. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: Exploiting sorting and clipping. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Exam-grade answer: A strong answer for '7.1 Object-Based Algorithms' classifies geometry relative to the boundary, explains intersection creation, and names the geometry passed to rasterization.

Common trap: Do not describe clipping as only deletion; crossing primitives can be cut and replaced by new vertices or primitive pieces.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in '7.1 Object-Based Algorithms'?

### Page 7 - Painter‘s Algorithm 1/3

Source cue: Bob Ross - Grandeur of Summer

Professor-style explanation: The slide 'Painter‘s Algorithm 1/3' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: Bob Ross - Grandeur of Summer. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Painter‘s Algorithm 1/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: Bob Ross - Grandeur of Summer. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Painter‘s Algorithm 1/3' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Painter‘s Algorithm 1/3' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Painter‘s Algorithm 1/3' into a causal sentence instead of repeating the slide title?

### Page 8 - Painter‘s Algorithm 2/3

Source cue: - First algorithm for object-based visible polygon determination / - Input: set of polygons / - Output: rendering of visible polygons / - Procedure: simulate drawing process of a painting / 1. Sort polygons into list in back-to-front order

Professor-style explanation: The slide 'Painter‘s Algorithm 2/3' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - First algorithm for object-based visible polygon determination / - Input: set of polygons / - Output: rendering of visible polygons / - Procedure: simulate drawing process of a painting / 1. Sort polygons into list in back-to-front order. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Painter‘s Algorithm 2/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - First algorithm for object-based visible polygon determination / - Input: set of polygons / - Output: rendering of visible polygons / - Procedure: simulate drawing process of a painting / 1. Sort polygons into list in back-to-front order. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Painter‘s Algorithm 2/3' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Painter‘s Algorithm 2/3' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Painter‘s Algorithm 2/3' into a causal sentence instead of repeating the slide title?

### Page 9 - Painter‘s Algorithm 3/3

Source cue: - Advantages / - Simple implementation / - No special graphics hardware necessary / - Disadvantages / - Works for polygons only instead of 3D scene objects

Professor-style explanation: The slide 'Painter‘s Algorithm 3/3' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Advantages / - Simple implementation / - No special graphics hardware necessary / - Disadvantages / - Works for polygons only instead of 3D scene objects. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Painter‘s Algorithm 3/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Advantages / - Simple implementation / - No special graphics hardware necessary / - Disadvantages / - Works for polygons only instead of 3D scene objects. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Painter‘s Algorithm 3/3' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Painter‘s Algorithm 3/3' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Painter‘s Algorithm 3/3' into a causal sentence instead of repeating the slide title?

### Page 10 - Weiler-Atherton Algorithm 1/3

Source cue: - Clipping-based divide-and-conquer approach / - Input: set of polygons / - Output: set of visible polygon parts / - Procedure / 1. Sort polygons into list L in front-to-back order

Professor-style explanation: The slide 'Weiler-Atherton Algorithm 1/3' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Clipping-based divide-and-conquer approach / - Input: set of polygons / - Output: set of visible polygon parts / - Procedure / 1. Sort polygons into list L in front-to-back order. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion. For examination purposes, the important content is classification: inside, outside, crossing, intersection point, and the newly produced primitive segment or polygon.

Technical commentary: This slide is about Weiler-Atherton Algorithm 1/3. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Clipping-based divide-and-conquer approach / - Input: set of polygons / - Output: set of visible polygon parts / - Procedure / 1. Sort polygons into list L in front-to-back order. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Exam-grade answer: A strong answer for 'Weiler-Atherton Algorithm 1/3' classifies geometry relative to the boundary, explains intersection creation, and names the geometry passed to rasterization.

Common trap: Do not describe clipping as only deletion; crossing primitives can be cut and replaced by new vertices or primitive pieces.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Weiler-Atherton Algorithm 1/3'?

### Page 11 - Weiler-Atherton Algorithm 2/3

Source cue: - Example from original paper / - Z value order flipped / - Bold: clip polygon / - Gray: unoccluded parts

Professor-style explanation: The slide 'Weiler-Atherton Algorithm 2/3' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Example from original paper / - Z value order flipped / - Bold: clip polygon / - Gray: unoccluded parts. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion. For examination purposes, the important content is classification: inside, outside, crossing, intersection point, and the newly produced primitive segment or polygon.

Technical commentary: This slide is about Weiler-Atherton Algorithm 2/3. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Example from original paper / - Z value order flipped / - Bold: clip polygon / - Gray: unoccluded parts. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Exam-grade answer: A strong answer for 'Weiler-Atherton Algorithm 2/3' classifies geometry relative to the boundary, explains intersection creation, and names the geometry passed to rasterization.

Common trap: Do not describe clipping as only deletion; crossing primitives can be cut and replaced by new vertices or primitive pieces.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Weiler-Atherton Algorithm 2/3'?

### Page 12 - Weiler-Atherton Algorithm 3/3

Source cue: - Advantages / - Can handle lines and polygons / - Exact calculation of the visible polygons / - Can be used for wireframe rendering / with different edge s tyles

Professor-style explanation: The slide 'Weiler-Atherton Algorithm 3/3' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Advantages / - Can handle lines and polygons / - Exact calculation of the visible polygons / - Can be used for wireframe rendering / with different edge s tyles. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion. For examination purposes, the important content is classification: inside, outside, crossing, intersection point, and the newly produced primitive segment or polygon.

Technical commentary: This slide is about Weiler-Atherton Algorithm 3/3. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Advantages / - Can handle lines and polygons / - Exact calculation of the visible polygons / - Can be used for wireframe rendering / with different edge s tyles. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Exam-grade answer: A strong answer for 'Weiler-Atherton Algorithm 3/3' classifies geometry relative to the boundary, explains intersection creation, and names the geometry passed to rasterization.

Common trap: Do not describe clipping as only deletion; crossing primitives can be cut and replaced by new vertices or primitive pieces.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Weiler-Atherton Algorithm 3/3'?

### Page 13 - Back Face Culling 1/2

Source cue: - Solves visibility determination for one convex, opaque scene object, / as its back faces are not visible / - Algorithm culls away polygons facing away from virtual camera / - Input: convex, opaque 3D scene object / - Output: set of front-facing polygons of input scene object

Professor-style explanation: The slide 'Back Face Culling 1/2' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Solves visibility determination for one convex, opaque scene object, / as its back faces are not visible / - Algorithm culls away polygons facing away from virtual camera / - Input: convex, opaque 3D scene object / - Output: set of front-facing polygons of input scene object. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Back Face Culling 1/2. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Solves visibility determination for one convex, opaque scene object, / as its back faces are not visible / - Algorithm culls away polygons facing away from virtual camera / - Input: convex, opaque 3D scene object / - Output: set of front-facing polygons of input scene object. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Back Face Culling 1/2' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Back Face Culling 1/2' works per object, per image region, per ray, or per fragment?

### Page 14 - Back Face Culling 2/2

Source cue: - Advantages / - Simple implementation / - An average of 50% of the areas of a scene can be eliminated in this way / - Reduces number of polygons to be processed, / thus reduces GPU transfers and speeds up the rendering process

Professor-style explanation: The slide 'Back Face Culling 2/2' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. The terms are successive representations in object-based rendering: - Advantages / - Simple implementation / - An average of 50% of the areas of a scene can be eliminated in this way / - Reduces number of polygons to be processed, / thus reduces GPU transfers and speeds up the rendering process. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter. For examination purposes, the important content is the representation change at each stage: model data, vertices, primitives, fragments, fragment tests, and final framebuffer updates.

Technical commentary: This slide is about Back Face Culling 2/2. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. The terms are successive representations in object-based rendering: - Advantages / - Simple implementation / - An average of 50% of the areas of a scene can be eliminated in this way / - Reduces number of polygons to be processed, / thus reduces GPU transfers and speeds up the rendering process. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels.

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Exam-grade answer: A strong answer for 'Back Face Culling 2/2' states what representation enters the stage, what representation leaves it, and which later stage depends on that output.

Common trap: Do not collapse 'Back Face Culling 2/2' into 'the GPU draws it'; name the intermediate representations because that is where most errors and exam distinctions appear.

Check yourself: Can you name the input and output representation for 'Back Face Culling 2/2' in the rendering pipeline?

### Page 15 - Robert‘s Algorithm

Source cue: - First algorithm for object-based visible line determination / - Input: set of convex 3D scene objects / - Output: set of visible lines / - Procedure: perform for all scene objects the following steps / 1. Remove self-occluded surfaces through back-face culling

Professor-style explanation: The slide 'Robert‘s Algorithm' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - First algorithm for object-based visible line determination / - Input: set of convex 3D scene objects / - Output: set of visible lines / - Procedure: perform for all scene objects the following steps / 1. Remove self-occluded surfaces through back-face culling. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Robert‘s Algorithm. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - First algorithm for object-based visible line determination / - Input: set of convex 3D scene objects / - Output: set of visible lines / - Procedure: perform for all scene objects the following steps / 1. Remove self-occluded surfaces through back-face culling. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Robert‘s Algorithm' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Robert‘s Algorithm'?

### Page 16 - Assessment Robert‘s Algorithm

Source cue: - Advantages / - Determination of visible lines was particularly important / for presentation on vector screens / - Today used in non-photorealistic rendering / to generate line drawings

Professor-style explanation: The slide 'Assessment Robert‘s Algorithm' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Advantages / - Determination of visible lines was particularly important / for presentation on vector screens / - Today used in non-photorealistic rendering / to generate line drawings. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Assessment Robert‘s Algorithm. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Advantages / - Determination of visible lines was particularly important / for presentation on vector screens / - Today used in non-photorealistic rendering / to generate line drawings. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Assessment Robert‘s Algorithm' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Assessment Robert‘s Algorithm'?

### Page 17 - 7.2 Binary Space Partitioning

Source cue: Hierarchical scene bisection

Professor-style explanation: The slide '7.2 Binary Space Partitioning' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: Hierarchical scene bisection. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about 7.2 Binary Space Partitioning. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: Hierarchical scene bisection. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for '7.2 Binary Space Partitioning' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer '7.2 Binary Space Partitioning' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn '7.2 Binary Space Partitioning' into a causal sentence instead of repeating the slide title?

### Page 18 - Spatial Data Structures

Source cue: - Spatial data structures are specialized / for organizing and storing scene data / - Types of spatial data structures / - Quad Trees: Optimize 2D data retrieval by dividing space it into four nodes / - Octrees: Optimize 3D data retrieval by dividing space it into eight nodes

Professor-style explanation: The slide 'Spatial Data Structures' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Spatial data structures are specialized / for organizing and storing scene data / - Types of spatial data structures / - Quad Trees: Optimize 2D data retrieval by dividing space it into four nodes / - Octrees: Optimize 3D data retrieval by dividing space it into eight nodes. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Spatial Data Structures. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Spatial data structures are specialized / for organizing and storing scene data / - Types of spatial data structures / - Quad Trees: Optimize 2D data retrieval by dividing space it into four nodes / - Octrees: Optimize 3D data retrieval by dividing space it into eight nodes. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Spatial Data Structures' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Spatial Data Structures' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Spatial Data Structures' into a causal sentence instead of repeating the slide title?

### Page 19 - BSP Trees 1/2

Source cue: - BSP Trees are Binary Space Partitioning trees / that recursively subdivide space into convex subsets through hyperplanes / - Key functions / - Space organization: divide 3D space into subspace represented as nodes / - Query efficiency: facilitate rapid querying like determining object visibility

Professor-style explanation: The slide 'BSP Trees 1/2' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - BSP Trees are Binary Space Partitioning trees / that recursively subdivide space into convex subsets through hyperplanes / - Key functions / - Space organization: divide 3D space into subspace represented as nodes / - Query efficiency: facilitate rapid querying like determining object visibility. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about BSP Trees 1/2. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - BSP Trees are Binary Space Partitioning trees / that recursively subdivide space into convex subsets through hyperplanes / - Key functions / - Space organization: divide 3D space into subspace represented as nodes / - Query efficiency: facilitate rapid querying like determining object visibility. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'BSP Trees 1/2' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'BSP Trees 1/2' works per object, per image region, per ray, or per fragment?

### Page 20 - BSP Trees 2/2

Source cue: - Definition binary tree / - A binary tree is a tree with at most two child nodes per node / - Different traversal schemes for binary trees exist A X X / - In-order traversal: first left child, then root, then right child / B C Y C

Professor-style explanation: The slide 'BSP Trees 2/2' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Definition binary tree / - A binary tree is a tree with at most two child nodes per node / - Different traversal schemes for binary trees exist A X X / - In-order traversal: first left child, then root, then right child / B C Y C. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about BSP Trees 2/2. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Definition binary tree / - A binary tree is a tree with at most two child nodes per node / - Different traversal schemes for binary trees exist A X X / - In-order traversal: first left child, then root, then right child / B C Y C. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'BSP Trees 2/2' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'BSP Trees 2/2' works per object, per image region, per ray, or per fragment?

### Page 21 - Node Data Structure

Source cue: - Each node contains / - Hyperplane / - List of scene geometry associated with the node / Class BSPNode: / Declare plane as Plane

Professor-style explanation: The slide 'Node Data Structure' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Each node contains / - Hyperplane / - List of scene geometry associated with the node / Class BSPNode: / Declare plane as Plane. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Node Data Structure. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Each node contains / - Hyperplane / - List of scene geometry associated with the node / Class BSPNode: / Declare plane as Plane. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Node Data Structure' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Node Data Structure' works per object, per image region, per ray, or per fragment?

### Page 22 - BSP Tree Construction

Source cue: - Choose a hyperplane from scene geometry for root node / and associate that plane with root node, split remaining geometry at plane / - Proceed recursively with the two resulting sets of scene geometries / and check each polygon against hyperplane / - Coinciding: associate with node

Professor-style explanation: The slide 'BSP Tree Construction' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Choose a hyperplane from scene geometry for root node / and associate that plane with root node, split remaining geometry at plane / - Proceed recursively with the two resulting sets of scene geometries / and check each polygon against hyperplane / - Coinciding: associate with node. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about BSP Tree Construction. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Choose a hyperplane from scene geometry for root node / and associate that plane with root node, split remaining geometry at plane / - Proceed recursively with the two resulting sets of scene geometries / and check each polygon against hyperplane / - Coinciding: associate with node. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'BSP Tree Construction' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'BSP Tree Construction' works per object, per image region, per ray, or per fragment?

### Page 23 - BSP Tree Construction - Example

Source cue: 1 2 / 3 4 / A B E / 3 1

Professor-style explanation: The slide 'BSP Tree Construction - Example' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: 1 2 / 3 4 / A B E / 3 1. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about BSP Tree Construction - Example. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: 1 2 / 3 4 / A B E / 3 1. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'BSP Tree Construction - Example' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'BSP Tree Construction - Example' works per object, per image region, per ray, or per fragment?

### Page 24 - BSP Tree Construction - Pseudo Code

Source cue: Function buildBSPTree(BSPNode node, List of Polygons list) / // Select one polygon to use as a hyperplane / Polygon p = Get first polygon from list / Set node.plane to the plane of polygon p / Add polygon p to node.geometry

Professor-style explanation: The slide 'BSP Tree Construction - Pseudo Code' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: Function buildBSPTree(BSPNode node, List of Polygons list) / // Select one polygon to use as a hyperplane / Polygon p = Get first polygon from list / Set node.plane to the plane of polygon p / Add polygon p to node.geometry. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about BSP Tree Construction - Pseudo Code. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: Function buildBSPTree(BSPNode node, List of Polygons list) / // Select one polygon to use as a hyperplane / Polygon p = Get first polygon from list / Set node.plane to the plane of polygon p / Add polygon p to node.geometry. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'BSP Tree Construction - Pseudo Code' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'BSP Tree Construction - Pseudo Code' works per object, per image region, per ray, or per fragment?

### Page 25 - Visibility Determination

Source cue: - Visibility determination through modified depth-first traversal / respecting the current camera / - Tree traversal handles the entire scene geometry / - Drawing is done in analogy to painter's algorithm / - Traversing provides the necessary "strict back-to-front order"

Professor-style explanation: The slide 'Visibility Determination' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Visibility determination through modified depth-first traversal / respecting the current camera / - Tree traversal handles the entire scene geometry / - Drawing is done in analogy to painter's algorithm / - Traversing provides the necessary "strict back-to-front order". Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Visibility Determination. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Visibility determination through modified depth-first traversal / respecting the current camera / - Tree traversal handles the entire scene geometry / - Drawing is done in analogy to painter's algorithm / - Traversing provides the necessary "strict back-to-front order". Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Visibility Determination' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Visibility Determination' works per object, per image region, per ray, or per fragment?

### Page 26 - Visibility Determination - Pseudo Code

Source cue: Function BSPHiddenSurfaceTraversal(BSPNode node, Point eye) / // Calculate the signed distance from the eye point to the partition plane / float distance = classifyPoint(node.plane, eye) / If distance < 0 Then / // Eye-point is on the back side of the plane

Professor-style explanation: The slide 'Visibility Determination - Pseudo Code' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: Function BSPHiddenSurfaceTraversal(BSPNode node, Point eye) / // Calculate the signed distance from the eye point to the partition plane / float distance = classifyPoint(node.plane, eye) / If distance < 0 Then / // Eye-point is on the back side of the plane. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Visibility Determination - Pseudo Code. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: Function BSPHiddenSurfaceTraversal(BSPNode node, Point eye) / // Calculate the signed distance from the eye point to the partition plane / float distance = classifyPoint(node.plane, eye) / If distance < 0 Then / // Eye-point is on the back side of the plane. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Visibility Determination - Pseudo Code' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Visibility Determination - Pseudo Code' works per object, per image region, per ray, or per fragment?

### Page 27 - BSP Tree Traversal - Example

Source cue: B F / 4 1 2 / F B F B / 3 4 / F B F B

Professor-style explanation: The slide 'BSP Tree Traversal - Example' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: B F / 4 1 2 / F B F B / 3 4 / F B F B. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about BSP Tree Traversal - Example. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: B F / 4 1 2 / F B F B / 3 4 / F B F B. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'BSP Tree Traversal - Example' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'BSP Tree Traversal - Example' works per object, per image region, per ray, or per fragment?

### Page 28 - Splitting Planes Selection

Source cue: - Hyperplane selection influences tree balance and required geometry splits / - Two alternative approaches exist / - Planes can be derived from scene geometry / - Planes can be chosen freely / - Useful heuristics

Professor-style explanation: The slide 'Splitting Planes Selection' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Hyperplane selection influences tree balance and required geometry splits / - Two alternative approaches exist / - Planes can be derived from scene geometry / - Planes can be chosen freely / - Useful heuristics. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Splitting Planes Selection. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Hyperplane selection influences tree balance and required geometry splits / - Two alternative approaches exist / - Planes can be derived from scene geometry / - Planes can be chosen freely / - Useful heuristics. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Splitting Planes Selection' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Splitting Planes Selection' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Splitting Planes Selection' into a causal sentence instead of repeating the slide title?

### Page 29 - Traversal Optimization

Source cue: - Sub-trees can be skipped during traversal if content is outside view frustum / - Testing is done by checking 8 corner points of 3D view frustum / - If there are two points on different sides, then the subtree is traversed / - If all points are in one subspace, then the other subspace does not have / to be traversed (view-frustum culling)

Professor-style explanation: The slide 'Traversal Optimization' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Sub-trees can be skipped during traversal if content is outside view frustum / - Testing is done by checking 8 corner points of 3D view frustum / - If there are two points on different sides, then the subtree is traversed / - If all points are in one subspace, then the other subspace does not have / to be traversed (view-frustum culling). Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Traversal Optimization. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Sub-trees can be skipped during traversal if content is outside view frustum / - Testing is done by checking 8 corner points of 3D view frustum / - If there are two points on different sides, then the subtree is traversed / - If all points are in one subspace, then the other subspace does not have / to be traversed (view-frustum culling). Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Traversal Optimization' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Traversal Optimization' works per object, per image region, per ray, or per fragment?

### Page 30 - Assessment BSP Trees

Source cue: - Advantages / - Simple implementation / - Do not need a depth buffer / - Applicable to static and dynamic scenes / (static scene geometry precalculated, dynamic objects inserted)

Professor-style explanation: The slide 'Assessment BSP Trees' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Advantages / - Simple implementation / - Do not need a depth buffer / - Applicable to static and dynamic scenes / (static scene geometry precalculated, dynamic objects inserted). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Assessment BSP Trees. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Advantages / - Simple implementation / - Do not need a depth buffer / - Applicable to static and dynamic scenes / (static scene geometry precalculated, dynamic objects inserted). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Assessment BSP Trees' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Assessment BSP Trees'?

### Page 31 - 7.3 Warnock Algorithm

Source cue: Image-based divide-and-conquer strategy

Professor-style explanation: The slide '7.3 Warnock Algorithm' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: Image-based divide-and-conquer strategy. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about 7.3 Warnock Algorithm. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: Image-based divide-and-conquer strategy. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for '7.3 Warnock Algorithm' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether '7.3 Warnock Algorithm' works per object, per image region, per ray, or per fragment?

### Page 32 - Warnock Algorithm

Source cue: - Hybrid object- and image-based divide-and-conquer approach / - Input: set of polygons and viewport / - Output: set of visible polygon parts / - Procedure: exploit spatial coherence of projected polygons to divide viewport / - Divide viewport recursively into squared regions

Professor-style explanation: The slide 'Warnock Algorithm' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Hybrid object- and image-based divide-and-conquer approach / - Input: set of polygons and viewport / - Output: set of visible polygon parts / - Procedure: exploit spatial coherence of projected polygons to divide viewport / - Divide viewport recursively into squared regions. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Warnock Algorithm. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Hybrid object- and image-based divide-and-conquer approach / - Input: set of polygons and viewport / - Output: set of visible polygon parts / - Procedure: exploit spatial coherence of projected polygons to divide viewport / - Divide viewport recursively into squared regions. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Warnock Algorithm' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Warnock Algorithm' works per object, per image region, per ray, or per fragment?

### Page 33 - Region-Based Visibility Determination

Source cue: R P / Case 1 / - Given viewport region R and set of polygons P, for the following / cases visibility determination can be considered trivial / - Case 1: All polygons in P are outside of R R P i P i

Professor-style explanation: The slide 'Region-Based Visibility Determination' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: R P / Case 1 / - Given viewport region R and set of polygons P, for the following / cases visibility determination can be considered trivial / - Case 1: All polygons in P are outside of R R P i P i. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Region-Based Visibility Determination. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: R P / Case 1 / - Given viewport region R and set of polygons P, for the following / cases visibility determination can be considered trivial / - Case 1: All polygons in P are outside of R R P i P i. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Region-Based Visibility Determination' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Region-Based Visibility Determination' works per object, per image region, per ray, or per fragment?

### Page 34 - Procedure

Source cue: - Start with entire viewport region R / - Subdivide R into four equal subregions / - Terminate if subregion size matches pixel size / - Classify subregions based on trivial cases / - If subregion matches trivial cases: resolve

Professor-style explanation: The slide 'Procedure' explains how camera geometry turns a 3D scene into image coordinates. In view space, objects are described relative to the camera. The projection matrix then maps that camera-centered geometry into clip space, where the viewing volume and clipping boundaries can be handled consistently. Perspective projection uses the homogeneous coordinate so that the later divide by w creates foreshortening: farther objects occupy less image space. Orthographic projection removes that depth-based size change and keeps parallel structures visually parallel. The terms describe camera-to-screen mapping: - Start with entire viewport region R / - Subdivide R into four equal subregions / - Terminate if subregion size matches pixel size / - Classify subregions based on trivial cases / - If subregion matches trivial cases: resolve. View-space geometry is mapped by a projection matrix, clipped, divided into normalized coordinates, and finally mapped to a viewport. The object chain is view-space position, projection matrix, clip coordinate, normalized device coordinate, and viewport coordinate. The slide is therefore connecting camera setup, visual appearance, and the numeric coordinate pipeline that rasterization later consumes. For examination purposes, the important content is the camera-to-screen chain: view coordinates, projection matrix, clip coordinates, perspective divide, normalized device coordinates, and viewport mapping.

Technical commentary: This slide is about Procedure. The projection objects on the slide convert view-space geometry into clip coordinates, normalized coordinates, and finally screen-related positions. The terms describe camera-to-screen mapping: - Start with entire viewport region R / - Subdivide R into four equal subregions / - Terminate if subregion size matches pixel size / - Classify subregions based on trivial cases / - If subregion matches trivial cases: resolve. View-space geometry is mapped by a projection matrix, clipped, divided into normalized coordinates, and finally mapped to a viewport.

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Exam-grade answer: A strong answer for 'Procedure' explains the mapping from view space through clip space and perspective divide to normalized and viewport coordinates.

Common trap: Do not confuse projection with viewport mapping; projection creates clip coordinates and the perspective divide comes before final screen mapping.

Check yourself: Can you explain how 'Procedure' changes positions before rasterization?

### Page 35 - Pseudo Code

Source cue: Procedure warnockHSR(Polygons list, Viewport vp) / If isSimple(list, vp) Then / // Base case: Simple enough scenario to draw directly / drawPolygons(list) / Else

Professor-style explanation: The slide 'Pseudo Code' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: Procedure warnockHSR(Polygons list, Viewport vp) / If isSimple(list, vp) Then / // Base case: Simple enough scenario to draw directly / drawPolygons(list) / Else. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Pseudo Code. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: Procedure warnockHSR(Polygons list, Viewport vp) / If isSimple(list, vp) Then / // Base case: Simple enough scenario to draw directly / drawPolygons(list) / Else. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Pseudo Code' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Pseudo Code' works per object, per image region, per ray, or per fragment?

### Page 36 - Assessment Warnock Algorithm

Source cue: - Advantages / - Efficient for large polygons by exploiting spatial coherence / - Easy to implement through recursive programming / - Disadvantages / - Restriction to polygons as primitives

Professor-style explanation: The slide 'Assessment Warnock Algorithm' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Advantages / - Efficient for large polygons by exploiting spatial coherence / - Easy to implement through recursive programming / - Disadvantages / - Restriction to polygons as primitives. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Assessment Warnock Algorithm. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Advantages / - Efficient for large polygons by exploiting spatial coherence / - Easy to implement through recursive programming / - Disadvantages / - Restriction to polygons as primitives. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Assessment Warnock Algorithm' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Assessment Warnock Algorithm' works per object, per image region, per ray, or per fragment?

### Page 37 - 7.4 Depth Buffer Algorithm

Source cue: Exploiting image storage for visibility determination

Professor-style explanation: The slide '7.4 Depth Buffer Algorithm' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: Exploiting image storage for visibility determination. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about 7.4 Depth Buffer Algorithm. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: Exploiting image storage for visibility determination. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for '7.4 Depth Buffer Algorithm' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '7.4 Depth Buffer Algorithm'?

### Page 38 - Depth Buffer Algorithm 1/3

Source cue: - Image-based visibility determination algorithm / that exploits extra graphics memory called depth buffer (= z-buffer) / - Depth buffer / - Depth buffer is a 2D raster that contains depth values / - Depth value calculation h appens during rasterization

Professor-style explanation: The slide 'Depth Buffer Algorithm 1/3' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Image-based visibility determination algorithm / that exploits extra graphics memory called depth buffer (= z-buffer) / - Depth buffer / - Depth buffer is a 2D raster that contains depth values / - Depth value calculation h appens during rasterization. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Depth Buffer Algorithm 1/3. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Image-based visibility determination algorithm / that exploits extra graphics memory called depth buffer (= z-buffer) / - Depth buffer / - Depth buffer is a 2D raster that contains depth values / - Depth value calculation h appens during rasterization. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Depth Buffer Algorithm 1/3' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Depth Buffer Algorithm 1/3'?

### Page 39 - Depth Buffer Algorithm 2/3

Source cue: - Depth buffer algorithm follows occlusion culling principle / Function occlusionCulling(List of Polygons scene) / Initialize an OcclusionRepresentation OR / For each object obj in scene / If obj is occluded by OR Then

Professor-style explanation: The slide 'Depth Buffer Algorithm 2/3' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Depth buffer algorithm follows occlusion culling principle / Function occlusionCulling(List of Polygons scene) / Initialize an OcclusionRepresentation OR / For each object obj in scene / If obj is occluded by OR Then. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Depth Buffer Algorithm 2/3. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Depth buffer algorithm follows occlusion culling principle / Function occlusionCulling(List of Polygons scene) / Initialize an OcclusionRepresentation OR / For each object obj in scene / If obj is occluded by OR Then. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Depth Buffer Algorithm 2/3' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Depth Buffer Algorithm 2/3'?

### Page 40 - Depth Buffer Algorithm 3/3

Source cue: - Depth buffer algorithm performs depth testing for each fragment / - Depth buffer is initialized with background value (e.g., z = 1) / - For every scene object / - Rasterize scene object / - For each fragment

Professor-style explanation: The slide 'Depth Buffer Algorithm 3/3' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Depth buffer algorithm performs depth testing for each fragment / - Depth buffer is initialized with background value (e.g., z = 1) / - For every scene object / - Rasterize scene object / - For each fragment. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Depth Buffer Algorithm 3/3. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Depth buffer algorithm performs depth testing for each fragment / - Depth buffer is initialized with background value (e.g., z = 1) / - For every scene object / - Rasterize scene object / - For each fragment. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Depth Buffer Algorithm 3/3' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Depth Buffer Algorithm 3/3'?

### Page 41 - Pseudo Code - Depth Buffer Test

Source cue: Function zBufferHSR(List of Geometry list) / // Initialize z-buffer and color buffer for each pixel on the screen / For x from 0 to Width / For y from 0 to Height / Set depthbuffer[x][y] to 1.0 // Maximum depth value

Professor-style explanation: The slide 'Pseudo Code - Depth Buffer Test' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: Function zBufferHSR(List of Geometry list) / // Initialize z-buffer and color buffer for each pixel on the screen / For x from 0 to Width / For y from 0 to Height / Set depthbuffer[x][y] to 1.0 // Maximum depth value. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Pseudo Code - Depth Buffer Test. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: Function zBufferHSR(List of Geometry list) / // Initialize z-buffer and color buffer for each pixel on the screen / For x from 0 to Width / For y from 0 to Height / Set depthbuffer[x][y] to 1.0 // Maximum depth value. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Pseudo Code - Depth Buffer Test' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Pseudo Code - Depth Buffer Test'?

### Page 42 - OpenGL Depth Buffer

Source cue: - OpenGL depth buffer: initialization and activation / - Depth values a re limited to [0, 1] (0: near-plane, 1: far-plane) / - Depth test must be explicitly activated / - Depth test comparison function can be changed / Function init()

Professor-style explanation: The slide 'OpenGL Depth Buffer' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - OpenGL depth buffer: initialization and activation / - Depth values a re limited to [0, 1] (0: near-plane, 1: far-plane) / - Depth test must be explicitly activated / - Depth test comparison function can be changed / Function init(). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL Depth Buffer. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - OpenGL depth buffer: initialization and activation / - Depth values a re limited to [0, 1] (0: near-plane, 1: far-plane) / - Depth test must be explicitly activated / - Depth test comparison function can be changed / Function init(). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL Depth Buffer' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Depth Buffer'?

### Page 43 - Depth Buffer Precision

Source cue: - Depth buffer precision is limited by its bit-depth (e.g., 16-bit, 24-bit, 32-bit), / which determines how finely depth can be distinguished / - Depth buffer precision is not linear: denser at near- and sparser at far- / clipping plane ⇒ depth conflicts can occur especially at greater distances / Nvidia Blog

Professor-style explanation: The slide 'Depth Buffer Precision' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Depth buffer precision is limited by its bit-depth (e.g., 16-bit, 24-bit, 32-bit), / which determines how finely depth can be distinguished / - Depth buffer precision is not linear: denser at near- and sparser at far- / clipping plane ⇒ depth conflicts can occur especially at greater distances / Nvidia Blog. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Depth Buffer Precision. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Depth buffer precision is limited by its bit-depth (e.g., 16-bit, 24-bit, 32-bit), / which determines how finely depth can be distinguished / - Depth buffer precision is not linear: denser at near- and sparser at far- / clipping plane ⇒ depth conflicts can occur especially at greater distances / Nvidia Blog. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Depth Buffer Precision' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Depth Buffer Precision'?

### Page 44 - Z-Fighting 1/2

Source cue: - Z-fighting occurs when two or more objects are very close together in depth / - Depth buffer can't consistently resolve which one is closer / causing flickering or overlapping artifacts in the rendered scene

Professor-style explanation: The slide 'Z-Fighting 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Z-fighting occurs when two or more objects are very close together in depth / - Depth buffer can't consistently resolve which one is closer / causing flickering or overlapping artifacts in the rendered scene. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Z-Fighting 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Z-fighting occurs when two or more objects are very close together in depth / - Depth buffer can't consistently resolve which one is closer / causing flickering or overlapping artifacts in the rendered scene. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Z-Fighting 1/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Z-Fighting 1/2'?

### Page 45 - Z-Fighting 2/2

Source cue: - Mitigation through depth buffer properties / - Use higher precision buffers by switching from 24-bit to 32-bit depth / - Adjust near and far planes: bringing near plane out- and far plane inwards / reduces the depth range, improving effective depth buffer precision / - Mitigating through rendering properties

Professor-style explanation: The slide 'Z-Fighting 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Mitigation through depth buffer properties / - Use higher precision buffers by switching from 24-bit to 32-bit depth / - Adjust near and far planes: bringing near plane out- and far plane inwards / reduces the depth range, improving effective depth buffer precision / - Mitigating through rendering properties. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Z-Fighting 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Mitigation through depth buffer properties / - Use higher precision buffers by switching from 24-bit to 32-bit depth / - Adjust near and far planes: bringing near plane out- and far plane inwards / reduces the depth range, improving effective depth buffer precision / - Mitigating through rendering properties. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Z-Fighting 2/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Z-Fighting 2/2'?

### Page 46 - Assessment Depth Buffering

Source cue: - Advantages / - Easy implementation / - No presorting of scene objects required / ⇒ Object evaluation can be performed in any order / - Not limited to polygonal geometries

Professor-style explanation: The slide 'Assessment Depth Buffering' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Advantages / - Easy implementation / - No presorting of scene objects required / ⇒ Object evaluation can be performed in any order / - Not limited to polygonal geometries. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Assessment Depth Buffering. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Advantages / - Easy implementation / - No presorting of scene objects required / ⇒ Object evaluation can be performed in any order / - Not limited to polygonal geometries. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Assessment Depth Buffering' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Assessment Depth Buffering'?

### Page 47 - 7.5 Depth Buffer Extensions

Source cue: How to render semi-transparent scene objects, and how to generate halos

Professor-style explanation: The slide '7.5 Depth Buffer Extensions' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: How to render semi-transparent scene objects, and how to generate halos. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about 7.5 Depth Buffer Extensions. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: How to render semi-transparent scene objects, and how to generate halos. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for '7.5 Depth Buffer Extensions' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '7.5 Depth Buffer Extensions'?

### Page 48 - Semi-Transparent Objects 1/2

Source cue: - Rendering of semi-transparent objects requires special handling / - Opaque and semi-transparent geometry need to be separated / - Opaque geometry is rendered first, semi-transparent blended on top / Function draw(Vector scene) / // Clear the framebuffer to prepare for new drawing

Professor-style explanation: The slide 'Semi-Transparent Objects 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Rendering of semi-transparent objects requires special handling / - Opaque and semi-transparent geometry need to be separated / - Opaque geometry is rendered first, semi-transparent blended on top / Function draw(Vector scene) / // Clear the framebuffer to prepare for new drawing. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Semi-Transparent Objects 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Rendering of semi-transparent objects requires special handling / - Opaque and semi-transparent geometry need to be separated / - Opaque geometry is rendered first, semi-transparent blended on top / Function draw(Vector scene) / // Clear the framebuffer to prepare for new drawing. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Semi-Transparent Objects 1/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Semi-Transparent Objects 1/2'?

### Page 49 - Semi-Transparent Objects 2/2

Source cue: - Issue: correct transparency without presorting of scene objects not possible

Professor-style explanation: The slide 'Semi-Transparent Objects 2/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Issue: correct transparency without presorting of scene objects not possible. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Semi-Transparent Objects 2/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Issue: correct transparency without presorting of scene objects not possible. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Semi-Transparent Objects 2/2' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Semi-Transparent Objects 2/2' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Semi-Transparent Objects 2/2' into a causal sentence instead of repeating the slide title?

### Page 50 - Order-Independent Transparency 1/4

Source cue: - Order-independent transparency exploits depth peeling to avoid sorting / - Depth peeling peels away depth layers one-by-one in front-to-back order / - Extract nearest fragments with smallest z values in first rendering pass / - Extract next further fragments in each subsequent rendering pass / - The nth rendering pass delivers the fragments to the nth depth plane

Professor-style explanation: The slide 'Order-Independent Transparency 1/4' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Order-independent transparency exploits depth peeling to avoid sorting / - Depth peeling peels away depth layers one-by-one in front-to-back order / - Extract nearest fragments with smallest z values in first rendering pass / - Extract next further fragments in each subsequent rendering pass / - The nth rendering pass delivers the fragments to the nth depth plane. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Order-Independent Transparency 1/4. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Order-independent transparency exploits depth peeling to avoid sorting / - Depth peeling peels away depth layers one-by-one in front-to-back order / - Extract nearest fragments with smallest z values in first rendering pass / - Extract next further fragments in each subsequent rendering pass / - The nth rendering pass delivers the fragments to the nth depth plane. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Order-Independent Transparency 1/4' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Order-Independent Transparency 1/4' works per object, per image region, per ray, or per fragment?

### Page 51 - Order-Independent Transparency 2/4

Source cue: - Illustration of subsequent layers / Layer 0 Layer 1 Layer 2 / 0 depth 1 0 depth 1 0 depth 1

Professor-style explanation: The slide 'Order-Independent Transparency 2/4' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Illustration of subsequent layers / Layer 0 Layer 1 Layer 2 / 0 depth 1 0 depth 1 0 depth 1. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Order-Independent Transparency 2/4. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Illustration of subsequent layers / Layer 0 Layer 1 Layer 2 / 0 depth 1 0 depth 1 0 depth 1. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Order-Independent Transparency 2/4' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Order-Independent Transparency 2/4' works per object, per image region, per ray, or per fragment?

### Page 52 - Order-Independent Transparency 3/4

Source cue: - 1st pass / - Render scene with conventional depth test (GL_LESS) / - Store resulting depth layer in Z-Buffer A / - Store resulting color layer as Layer 0 / - 2nd pass

Professor-style explanation: The slide 'Order-Independent Transparency 3/4' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - 1st pass / - Render scene with conventional depth test (GL_LESS) / - Store resulting depth layer in Z-Buffer A / - Store resulting color layer as Layer 0 / - 2nd pass. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Order-Independent Transparency 3/4. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - 1st pass / - Render scene with conventional depth test (GL_LESS) / - Store resulting depth layer in Z-Buffer A / - Store resulting color layer as Layer 0 / - 2nd pass. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Order-Independent Transparency 3/4' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Order-Independent Transparency 3/4'?

### Page 53 - Order-Independent Transparency 4/4

Source cue: 1 layer 2 layers / 3 layers 4 layers

Professor-style explanation: The slide 'Order-Independent Transparency 4/4' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: 1 layer 2 layers / 3 layers 4 layers. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Order-Independent Transparency 4/4. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: 1 layer 2 layers / 3 layers 4 layers. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Order-Independent Transparency 4/4' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Order-Independent Transparency 4/4' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Order-Independent Transparency 4/4' into a causal sentence instead of repeating the slide title?

### Page 54 - Generating Haloes 1/2

Source cue: - Halo: circle of light around sun or moon caused by ice crystals in the air; [...]; / a distinguishing zone surrounding a central object / - Haloes as wireframe illustration tools result / in better spatial comprehension / - Add highlights to foreground lines

Professor-style explanation: The slide 'Generating Haloes 1/2' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Halo: circle of light around sun or moon caused by ice crystals in the air; [...]; / a distinguishing zone surrounding a central object / - Haloes as wireframe illustration tools result / in better spatial comprehension / - Add highlights to foreground lines. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Generating Haloes 1/2. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Halo: circle of light around sun or moon caused by ice crystals in the air; [...]; / a distinguishing zone surrounding a central object / - Haloes as wireframe illustration tools result / in better spatial comprehension / - Add highlights to foreground lines. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Generating Haloes 1/2' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Generating Haloes 1/2'?

### Page 55 - Generating Haloes 2/2

Source cue: - Proceeding / - Render wireframe model with thick lines into depth buffer / without writing to the color buffer ⇒ depth image contains thick lines / - Render wireframe model with thin lines into color buffer / ⇒ Lines of foreground surfaces have a "safety margin"

Professor-style explanation: The slide 'Generating Haloes 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Proceeding / - Render wireframe model with thick lines into depth buffer / without writing to the color buffer ⇒ depth image contains thick lines / - Render wireframe model with thin lines into color buffer / ⇒ Lines of foreground surfaces have a "safety margin". Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Generating Haloes 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Proceeding / - Render wireframe model with thick lines into depth buffer / without writing to the color buffer ⇒ depth image contains thick lines / - Render wireframe model with thin lines into color buffer / ⇒ Lines of foreground surfaces have a "safety margin". Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Generating Haloes 2/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Generating Haloes 2/2'?

### Page 56 - 7.6 Ray Casting

Source cue: Shooting rays to determine visibility

Professor-style explanation: The slide '7.6 Ray Casting' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: Shooting rays to determine visibility. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about 7.6 Ray Casting. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: Shooting rays to determine visibility. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for '7.6 Ray Casting' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether '7.6 Ray Casting' works per object, per image region, per ray, or per fragment?

### Page 57 - Ray Casting Principle

Source cue: - Image-based visibility determination algorithm exploiting ray intersections / - Ray initialization - initialize ray from viewpoint through each pixel / (ray generation) / - Intersection calculation - find object intersection closest to camera / (ray intersection)

Professor-style explanation: The slide 'Ray Casting Principle' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Image-based visibility determination algorithm exploiting ray intersections / - Ray initialization - initialize ray from viewpoint through each pixel / (ray generation) / - Intersection calculation - find object intersection closest to camera / (ray intersection). Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Ray Casting Principle. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Image-based visibility determination algorithm exploiting ray intersections / - Ray initialization - initialize ray from viewpoint through each pixel / (ray generation) / - Intersection calculation - find object intersection closest to camera / (ray intersection). Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Ray Casting Principle' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Ray Casting Principle' works per object, per image region, per ray, or per fragment?

### Page 58 - Ray Initialization 1/3

Source cue: - Ray is defined by origin and direction / - Mathematically parameterized as a 3D line via t / s−e / - p t = e + t s / s−e

Professor-style explanation: The slide 'Ray Initialization 1/3' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Ray is defined by origin and direction / - Mathematically parameterized as a 3D line via t / s−e / - p t = e + t s / s−e. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Ray Initialization 1/3. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Ray is defined by origin and direction / - Mathematically parameterized as a 3D line via t / s−e / - p t = e + t s / s−e. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Ray Initialization 1/3' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Ray Initialization 1/3'?

### Page 59 - Ray Initialization 2/3

Source cue: - How can we find s? / - Assumption: we have a simplified camera model / - Positioned in e / - Orthonormal base {u, v, w} / - Orthonormal: orthogonal + normalized

Professor-style explanation: The slide 'Ray Initialization 2/3' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - How can we find s? / - Assumption: we have a simplified camera model / - Positioned in e / - Orthonormal base {u, v, w} / - Orthonormal: orthogonal + normalized. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Ray Initialization 2/3. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - How can we find s? / - Assumption: we have a simplified camera model / - Positioned in e / - Orthonormal base {u, v, w} / - Orthonormal: orthogonal + normalized. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Ray Initialization 2/3' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Ray Initialization 2/3' works per object, per image region, per ray, or per fragment?

### Page 60 - Ray Initialization 3/3

Source cue: - Definition of the pixel grid with n × n pixels / x y / - Size of the pixel raster is r − l × t − b / - Pixel spacing is / - x-coordinate: (r − l)/n

Professor-style explanation: The slide 'Ray Initialization 3/3' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Definition of the pixel grid with n × n pixels / x y / - Size of the pixel raster is r − l × t − b / - Pixel spacing is / - x-coordinate: (r − l)/n. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Ray Initialization 3/3. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Definition of the pixel grid with n × n pixels / x y / - Size of the pixel raster is r − l × t − b / - Pixel spacing is / - x-coordinate: (r − l)/n. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Ray Initialization 3/3' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Ray Initialization 3/3' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Ray Initialization 3/3'?

### Page 61 - Intersection Calculation

Source cue: - Find smallest positive t for which p(t) is an intersection / - Simple procedure / - Iterate over all scene objects and calculate intersections / - Sort intersections / - Select intersection with smallest t

Professor-style explanation: The slide 'Intersection Calculation' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Find smallest positive t for which p(t) is an intersection / - Simple procedure / - Iterate over all scene objects and calculate intersections / - Sort intersections / - Select intersection with smallest t. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Intersection Calculation. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Find smallest positive t for which p(t) is an intersection / - Simple procedure / - Iterate over all scene objects and calculate intersections / - Sort intersections / - Select intersection with smallest t. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Intersection Calculation' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Intersection Calculation' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Intersection Calculation' into a causal sentence instead of repeating the slide title?

### Page 62 - Implicit Surface Intersection Calculation

Source cue: - Find set of all points with f x, y, z = 0 / - Examples: plane, sphere, quadrics, ... / n = (A, B, C) / c = (x , y , z ) / c c c

Professor-style explanation: The slide 'Implicit Surface Intersection Calculation' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Find set of all points with f x, y, z = 0 / - Examples: plane, sphere, quadrics, ... / n = (A, B, C) / c = (x , y , z ) / c c c. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Implicit Surface Intersection Calculation. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Find set of all points with f x, y, z = 0 / - Examples: plane, sphere, quadrics, ... / n = (A, B, C) / c = (x , y , z ) / c c c. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Implicit Surface Intersection Calculation' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Implicit Surface Intersection Calculation' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Implicit Surface Intersection Calculation' into a causal sentence instead of repeating the slide title?

### Page 63 - Intersection Calculation - Triangle

Source cue: - Idea: find intersection with plane which embeds triangle, / and test whether intersection lies inside triangle / 1. Calculate intersection with plane / through implicit surface intersection calculation / 2. Exploit barycentric coordinates

Professor-style explanation: The slide 'Intersection Calculation - Triangle' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Idea: find intersection with plane which embeds triangle, / and test whether intersection lies inside triangle / 1. Calculate intersection with plane / through implicit surface intersection calculation / 2. Exploit barycentric coordinates. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Intersection Calculation - Triangle. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Idea: find intersection with plane which embeds triangle, / and test whether intersection lies inside triangle / 1. Calculate intersection with plane / through implicit surface intersection calculation / 2. Exploit barycentric coordinates. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Intersection Calculation - Triangle' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Intersection Calculation - Triangle' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Intersection Calculation - Triangle'?

### Page 64 - Pseudo Code - Analytic Intersection Computation

Source cue: Function castRay(List sceneObjects, Window win, Camera cam) / // Iterate over each pixel on the window / For x from 0 to win.width / For y from 0 to win.height / Initialize ray r = calculateRay(x, y, win, cam) // Calculate ray from camera through pixel (x, y)

Professor-style explanation: The slide 'Pseudo Code - Analytic Intersection Computation' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: Function castRay(List sceneObjects, Window win, Camera cam) / // Iterate over each pixel on the window / For x from 0 to win.width / For y from 0 to win.height / Initialize ray r = calculateRay(x, y, win, cam) // Calculate ray from camera through pixel (x, y). Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Pseudo Code - Analytic Intersection Computation. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: Function castRay(List sceneObjects, Window win, Camera cam) / // Iterate over each pixel on the window / For x from 0 to win.width / For y from 0 to win.height / Initialize ray r = calculateRay(x, y, win, cam) // Calculate ray from camera through pixel (x, y). Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Pseudo Code - Analytic Intersection Computation' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Pseudo Code - Analytic Intersection Computation' works per object, per image region, per ray, or per fragment?

### Page 65 - Pseudo Code - Iterative Intersection Calculation (Ray Marching)

Source cue: - Ray march in ε steps and check all scene objects for intersection / Function intersect(const Ray& ray, const List of SceneObjects& sceneObjects) const / Initialize t as 0.0 // Starting point for ray parameter / Initialize epsilon as 0.01 // Small increment for ray parameter / // Loop to incrementally trace the ray through the scene

Professor-style explanation: The slide 'Pseudo Code - Iterative Intersection Calculation (Ray Marching)' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Ray march in ε steps and check all scene objects for intersection / Function intersect(const Ray& ray, const List of SceneObjects& sceneObjects) const / Initialize t as 0.0 // Starting point for ray parameter / Initialize epsilon as 0.01 // Small increment for ray parameter / // Loop to incrementally trace the ray through the scene. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Pseudo Code - Iterative Intersection Calculation (Ray Marching). The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Ray march in ε steps and check all scene objects for intersection / Function intersect(const Ray& ray, const List of SceneObjects& sceneObjects) const / Initialize t as 0.0 // Starting point for ray parameter / Initialize epsilon as 0.01 // Small increment for ray parameter / // Loop to incrementally trace the ray through the scene. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Pseudo Code - Iterative Intersection Calculation (Ray Marching)' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Pseudo Code - Iterative Intersection Calculation (Ray Marching)' works per object, per image region, per ray, or per fragment?

### Page 66 - Assessment Ray Casting

Source cue: - Advantages / - Image-precise algorithm that support all types of scene objects / - Analytic intersection calculation possible / - Can be parallelized and supported by graphics hardware / - Disadvantages

Professor-style explanation: The slide 'Assessment Ray Casting' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Advantages / - Image-precise algorithm that support all types of scene objects / - Analytic intersection calculation possible / - Can be parallelized and supported by graphics hardware / - Disadvantages. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Assessment Ray Casting. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Advantages / - Image-precise algorithm that support all types of scene objects / - Analytic intersection calculation possible / - Can be parallelized and supported by graphics hardware / - Disadvantages. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Assessment Ray Casting' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Assessment Ray Casting' works per object, per image region, per ray, or per fragment?

### Page 67 - but are crucial for accurate visibility determination

Source cue: - Visibility determination ensures only scene objects visible from camera are rendered / - Effective visibility determination is crucial for rendering efficiency and visual accuracy / - Object-based algorithms perform geometry-based analysis prior to rasterization / - Examples include the Painter's Algorithm, Weiler-Atherton, and Back Face Culling / - These methods often suffer from higher complexity and can be poorly parallelizable

Professor-style explanation: The slide 'but are crucial for accurate visibility determination' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Visibility determination ensures only scene objects visible from camera are rendered / - Effective visibility determination is crucial for rendering efficiency and visual accuracy / - Object-based algorithms perform geometry-based analysis prior to rasterization / - Examples include the Painter's Algorithm, Weiler-Atherton, and Back Face Culling / - These methods often suffer from higher complexity and can be poorly parallelizable. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion. For examination purposes, the important content is classification: inside, outside, crossing, intersection point, and the newly produced primitive segment or polygon.

Technical commentary: This slide is about but are crucial for accurate visibility determination. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Visibility determination ensures only scene objects visible from camera are rendered / - Effective visibility determination is crucial for rendering efficiency and visual accuracy / - Object-based algorithms perform geometry-based analysis prior to rasterization / - Examples include the Painter's Algorithm, Weiler-Atherton, and Back Face Culling / - These methods often suffer from higher complexity and can be poorly parallelizable. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Exam-grade answer: A strong answer for 'but are crucial for accurate visibility determination' classifies geometry relative to the boundary, explains intersection creation, and names the geometry passed to rasterization.

Common trap: Do not describe clipping as only deletion; crossing primitives can be cut and replaced by new vertices or primitive pieces.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'but are crucial for accurate visibility determination'?

### Page 68 - Literature and other sources used in this chapter

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Literature and other sources used in this chapter' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Literature and other sources used in this chapter. The slide lists source material or chapter references that support the technical content and give names for further reading. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Reference slides provide the source trail for definitions, algorithms, and deeper explanations.

Exam-grade answer: A strong answer for 'Literature and other sources used in this chapter' identifies what kind of source is listed and which course concept or algorithm that source supports.

Common trap: Do not skip 'Literature and other sources used in this chapter' if it names a standard algorithm or source that defines terminology used later in the chapter.

Check yourself: Can you identify which source or topic 'Literature and other sources used in this chapter' points to for deeper study?

### Page 69 - Practice, Addison-Wesley.

Source cue: - Text Books / - Foley J., van Dam, A., Feiner, S. (2013). Computer Graphics: Principles and / Practice, Addison-Wesley. / - Papers / - Everitt, C. (2001). Interactive order-independent transparency. White paper,

Professor-style explanation: The slide 'Practice, Addison-Wesley.' collects the source material behind the chapter. References are not rendering objects themselves, but they identify the books, papers, or external resources from which the lecture's terminology and algorithms are drawn. The listed sources support the chapter content: - Text Books / - Foley J., van Dam, A., Feiner, S. (2013). Computer Graphics: Principles and / Practice, Addison-Wesley. / - Papers / - Everitt, C. (2001). Interactive order-independent transparency. White paper,. They point to the books, papers, or resources behind the definitions and algorithms used in the lecture. In practical terms, a reference slide marks the boundary of the chapter and tells us where the formal definitions, derivations, or extended examples can be found if a topic needs more depth than the lecture slides provide. For examination purposes, the important content is source attribution and vocabulary: references tell where precise definitions and standard algorithms come from.

Technical commentary: This slide is about Practice, Addison-Wesley.. The slide lists source material or chapter references that support the technical content and give names for further reading. The listed sources support the chapter content: - Text Books / - Foley J., van Dam, A., Feiner, S. (2013). Computer Graphics: Principles and / Practice, Addison-Wesley. / - Papers / - Everitt, C. (2001). Interactive order-independent transparency. White paper,. They point to the books, papers, or resources behind the definitions and algorithms used in the lecture.

Why it matters: Reference slides provide the source trail for definitions, algorithms, and deeper explanations.

Exam-grade answer: A strong answer for 'Practice, Addison-Wesley.' identifies what kind of source is listed and which course concept or algorithm that source supports.

Common trap: Do not skip 'Practice, Addison-Wesley.' if it names a standard algorithm or source that defines terminology used later in the chapter.

Check yourself: Can you identify which source or topic 'Practice, Addison-Wesley.' points to for deeper study?

## 07.1 Object-Based Algorithms

Source location: Section 7.1

### Commentary

Object-based visibility algorithms reason about geometry before or while comparing surfaces. They can sort, split, or reject objects based on spatial relations. This is different from simply letting every fragment fight in the depth buffer.

The value of object-based reasoning is reducing work or establishing correct order. The difficulty is that geometry can overlap in complicated ways, so simple global ordering is not always possible.

### Mental Model

Object-based visibility tries to solve visibility with geometry before final pixels are written.

### Check Yourself

Why can intersecting polygons make simple depth sorting fail?

## 07.2 Binary Space Partitioning

Source location: Section 7.2

### Commentary

A BSP tree recursively divides space with planes. Once built, it can help traverse geometry in a view-dependent order. This is useful for visibility and ordering because the tree encodes spatial relationships.

The cost is preprocessing and possible splitting of geometry. BSP is a good example of trading memory and setup work for faster or more structured visibility decisions later.

### Mental Model

A BSP tree stores a recursive answer to 'which side of this plane is the geometry on?'

### Check Yourself

Why can building a BSP tree require splitting polygons?

## 07.3 Warnock Algorithm

Source location: Section 7.3

### Commentary

Warnock's algorithm works in image space by subdividing regions until visibility is simple enough to decide. If a region is ambiguous, split it. If it is simple, fill it.

This illustrates a general graphics strategy: recursively reduce a hard global problem into smaller local problems. The algorithm is less central in modern OpenGL practice than the depth buffer, but it helps contrast image-space and object-space approaches.

### Mental Model

When a region is too complicated, subdivide until the answer becomes simple.

### Check Yourself

What makes Warnock's algorithm image-space rather than object-space?

## 07.4 Depth Buffer Algorithm

Source location: Section 7.4

### Commentary

The depth buffer stores the closest accepted depth at each sample or pixel. For each fragment, compare its depth to the stored depth. If it passes, update the color and depth; otherwise discard it.

The strength of the depth buffer is simplicity and hardware efficiency. The weakness is precision: depth values are finite, and projection distributes precision unevenly. Bad near/far settings can create z-fighting.

### Mental Model

The depth buffer is a per-sample competition for closest visible fragment.

### Check Yourself

Why should the near plane not be unnecessarily close to the camera?

## 07.5 Depth Extensions and Ray Casting

Source location: Sections 7.5-7.6

### Commentary

Depth buffer extensions refine or adapt depth-based visibility, for example by handling precision, transparency, or multiple layers more carefully. Standard depth testing alone is not a complete solution for every visibility situation.

Ray casting takes the opposite direction from rasterization: for each image sample, cast a ray into the scene and find the closest intersection. This naturally solves primary visibility but requires intersection work instead of raster coverage work.

### Mental Model

Rasterization pushes primitives to pixels; ray casting pulls visibility from pixels into the scene.

### Check Yourself

Why is transparency harder than opaque nearest-surface visibility?

## End-of-Lecture Summary

If you remember only one thing from Lecture 07, remember this: This lecture asks which surfaces are visible from a viewpoint. Rasterization can generate many fragment candidates, but visibility decides which ones should affect the image.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
