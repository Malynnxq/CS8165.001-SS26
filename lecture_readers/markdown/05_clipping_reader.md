# Lecture 05 - Clipping

Source chunk: `course_text_parts/03_lectures/05_clipping.txt`
Extracted slide pages in source chunk: 56

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture focuses on algorithms that remove or trim geometry against boundaries. Clipping is a geometric operation before rasterization, not a visibility test between overlapping objects.

## How To Read This Lecture

- First read the big picture and the mental models.
- Then open the source chunk and compare the slide bullets to the commentary.
- After each section, answer the check question without notes.
- If the check feels vague, revisit the source pages listed for that section.

## Per-Slide Commentary

Every extracted slide page gets its own reading note. This is the part to use when the original PDF is too terse or visually dense.

### Page 1 - Visual or title slide

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Visual or title slide' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail.

Technical commentary: This slide is about Visual or title slide. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Visual or title slide' into a causal sentence instead of repeating the slide title?

### Page 2 - Clipping Projected Geometry 1/2

Source cue: - Now that the geometry has been transformed to its representation on the / screen, parts outside screen must be clipped away / - Clipping ensures that following costly computations / (e.g., rasterization, illumination, shading) are only applied to visible parts / - Since clipping is performed for all geometry, algorithms are highly optimized

Professor-style explanation: The slide 'Clipping Projected Geometry 1/2' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Now that the geometry has been transformed to its representation on the / screen, parts outside screen must be clipped away / - Clipping ensures that following costly computations / (e.g., rasterization, illumination, shading) are only applied to visible parts / - Since clipping is performed for all geometry, algorithms are highly optimized. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear.

Technical commentary: This slide is about Clipping Projected Geometry 1/2. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Now that the geometry has been transformed to its representation on the / screen, parts outside screen must be clipped away / - Clipping ensures that following costly computations / (e.g., rasterization, illumination, shading) are only applied to visible parts / - Since clipping is performed for all geometry, algorithms are highly optimized. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Clipping Projected Geometry 1/2'?

### Page 3 - Clipping Projected Geometry 2/2

Source cue: - Analytical clipping / - Clipping before raster conversion, clipped primitives are raster-converted / - Compute time savings if clipped primitive is much smaller than unclipped / - OpenGL: clipping against canonical view volume / - Pixel-based clipping

Professor-style explanation: The slide 'Clipping Projected Geometry 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Analytical clipping / - Clipping before raster conversion, clipped primitives are raster-converted / - Compute time savings if clipped primitive is much smaller than unclipped / - OpenGL: clipping against canonical view volume / - Pixel-based clipping. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Clipping Projected Geometry 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Analytical clipping / - Clipping before raster conversion, clipped primitives are raster-converted / - Compute time savings if clipped primitive is much smaller than unclipped / - OpenGL: clipping against canonical view volume / - Pixel-based clipping. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Clipping Projected Geometry 2/2'?

### Page 4 - 5.1 Cohen-Sutherland Line Clipping

Source cue: 5.2 Cyrus-Beck Line Clipping / 5.3 Sutherland-Hodgman Polygon Clipping / 5.4 Weiler-Atherton Polygon Clipping / 5.5 Greiner-Hormann Polygon Clipping

Professor-style explanation: The slide '5.1 Cohen-Sutherland Line Clipping' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: 5.2 Cyrus-Beck Line Clipping / 5.3 Sutherland-Hodgman Polygon Clipping / 5.4 Weiler-Atherton Polygon Clipping / 5.5 Greiner-Hormann Polygon Clipping. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about 5.1 Cohen-Sutherland Line Clipping. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: 5.2 Cyrus-Beck Line Clipping / 5.3 Sutherland-Hodgman Polygon Clipping / 5.4 Weiler-Atherton Polygon Clipping / 5.5 Greiner-Hormann Polygon Clipping. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in '5.1 Cohen-Sutherland Line Clipping'?

### Page 5 - 5.1 Cohen-Sutherland Line Clipping

Source cue: Clip lines against rectangle

Professor-style explanation: The slide '5.1 Cohen-Sutherland Line Clipping' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: Clip lines against rectangle. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about 5.1 Cohen-Sutherland Line Clipping. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: Clip lines against rectangle. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in '5.1 Cohen-Sutherland Line Clipping'?

### Page 6 - Brute-Force Line Clipping 1/2

Source cue: - Check each edge of the rectangle for intersection with line / - Intersection calculation for the line defined by the edge, and the line / - If intersection lies within edge and within line, clipping necessary

Professor-style explanation: The slide 'Brute-Force Line Clipping 1/2' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Check each edge of the rectangle for intersection with line / - Intersection calculation for the line defined by the edge, and the line / - If intersection lies within edge and within line, clipping necessary. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Brute-Force Line Clipping 1/2. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Check each edge of the rectangle for intersection with line / - Intersection calculation for the line defined by the edge, and the line / - If intersection lies within edge and within line, clipping necessary. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Brute-Force Line Clipping 1/2'?

### Page 7 - Brute-Force Line Clipping 2/2

Source cue: - Using the parameter representation for lines / x x − x / 0 1 0 / p t = p + t ⋅ p − p = + t ⋅ , p / 0 1 0 y y − y 1

Professor-style explanation: The slide 'Brute-Force Line Clipping 2/2' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Using the parameter representation for lines / x x − x / 0 1 0 / p t = p + t ⋅ p − p = + t ⋅ , p / 0 1 0 y y − y 1. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Brute-Force Line Clipping 2/2. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Using the parameter representation for lines / x x − x / 0 1 0 / p t = p + t ⋅ p − p = + t ⋅ , p / 0 1 0 y y − y 1. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Brute-Force Line Clipping 2/2'?

### Page 8 - Endpoint Analysis 1/2

Source cue: - Idea: Use end point analysis to create new lines / - Clipping against a rectangle yields a line / - Clipping against a convex polygon results in a line / - Endpoint analysis / - Line segment s = (p , p ), p = (x , y ) and p = (x , y )

Professor-style explanation: The slide 'Endpoint Analysis 1/2' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Idea: Use end point analysis to create new lines / - Clipping against a rectangle yields a line / - Clipping against a convex polygon results in a line / - Endpoint analysis / - Line segment s = (p , p ), p = (x , y ) and p = (x , y ). A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Endpoint Analysis 1/2. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Idea: Use end point analysis to create new lines / - Clipping against a rectangle yields a line / - Clipping against a convex polygon results in a line / - Endpoint analysis / - Line segment s = (p , p ), p = (x , y ) and p = (x , y ). A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Endpoint Analysis 1/2'?

### Page 9 - Endpoint Analysis 2/2

Source cue: - Clipping lines against a clip rectangle by reduction to endpoint analysis / - If both endpoints are to the right of x and to the left of x / min max / and above y and below y , they are inside / min max

Professor-style explanation: The slide 'Endpoint Analysis 2/2' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Clipping lines against a clip rectangle by reduction to endpoint analysis / - If both endpoints are to the right of x and to the left of x / min max / and above y and below y , they are inside / min max. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Endpoint Analysis 2/2. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Clipping lines against a clip rectangle by reduction to endpoint analysis / - If both endpoints are to the right of x and to the left of x / min max / and above y and below y , they are inside / min max. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Endpoint Analysis 2/2'?

### Page 10 - Binary Coding of Half-Planes 1/3

Source cue: - Classification of the plane in nine regions / - Classify a point by one bit each / for belonging to each of the 4 half-planes / 1001 1000 1010 / - 4-bit outcode

Professor-style explanation: The slide 'Binary Coding of Half-Planes 1/3' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Classification of the plane in nine regions / - Classify a point by one bit each / for belonging to each of the 4 half-planes / 1001 1000 1010 / - 4-bit outcode. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Binary Coding of Half-Planes 1/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Classification of the plane in nine regions / - Classify a point by one bit each / for belonging to each of the 4 half-planes / 1001 1000 1010 / - 4-bit outcode. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Binary Coding of Half-Planes 1/3' into a causal sentence instead of repeating the slide title?

### Page 11 - Binary Coding of Half-Planes 2/3

Source cue: - Endpoint classification / - Line segment s = (p , p ) / 0 1 / - Outcodes: / 1001 1000 1010

Professor-style explanation: The slide 'Binary Coding of Half-Planes 2/3' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Endpoint classification / - Line segment s = (p , p ) / 0 1 / - Outcodes: / 1001 1000 1010. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations.

Technical commentary: This slide is about Binary Coding of Half-Planes 2/3. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Endpoint classification / - Line segment s = (p , p ) / 0 1 / - Outcodes: / 1001 1000 1010. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Binary Coding of Half-Planes 2/3'?

### Page 12 - Binary Coding of Half-Planes 3/3

Source cue: - Clipping, if (oc0 & oc1) = 0: / - Choose an order for clipping (e.g., top, bottom, right, left) / - Select clip edge that is crossed by the line / - Check done on basis of bit codes, which differ in at least 1 bit / - Clip s at this clip edge

Professor-style explanation: The slide 'Binary Coding of Half-Planes 3/3' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Clipping, if (oc0 & oc1) = 0: / - Choose an order for clipping (e.g., top, bottom, right, left) / - Select clip edge that is crossed by the line / - Check done on basis of bit codes, which differ in at least 1 bit / - Clip s at this clip edge. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Binary Coding of Half-Planes 3/3. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Clipping, if (oc0 & oc1) = 0: / - Choose an order for clipping (e.g., top, bottom, right, left) / - Select clip edge that is crossed by the line / - Check done on basis of bit codes, which differ in at least 1 bit / - Clip s at this clip edge. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Binary Coding of Half-Planes 3/3'?

### Page 13 - Pseudo Code

Source cue: void cohensutherlandLineClipper(Line s, Rectangle r) { / int oc0 = outcode(s.p0, r); / int oc1 = outcode(s.p1, r); / bool done = false; / while (!done) { int outcode(Point p, Rectangle r) {

Professor-style explanation: The slide 'Pseudo Code' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: void cohensutherlandLineClipper(Line s, Rectangle r) { / int oc0 = outcode(s.p0, r); / int oc1 = outcode(s.p1, r); / bool done = false; / while (!done) { int outcode(Point p, Rectangle r) {. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Pseudo Code. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: void cohensutherlandLineClipper(Line s, Rectangle r) { / int oc0 = outcode(s.p0, r); / int oc1 = outcode(s.p1, r); / bool done = false; / while (!done) { int outcode(Point p, Rectangle r) {. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Pseudo Code'?

### Page 14 - Example

Source cue: 1001 1000 1010 / 0001 0000 0010 / 0101 0100 0110

Professor-style explanation: The slide 'Example' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: 1001 1000 1010 / 0001 0000 0010 / 0101 0100 0110. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Example. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: 1001 1000 1010 / 0001 0000 0010 / 0101 0100 0110. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Example' into a causal sentence instead of repeating the slide title?

### Page 15 - Evaluation

Source cue: - Occasionally performs several (unnecessary) clip operations on a line as test / and clippings are done in a fixed edge order / - Especially efficient when / - almost all lines are outside / - almost all lines are inside

Professor-style explanation: The slide 'Evaluation' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Occasionally performs several (unnecessary) clip operations on a line as test / and clippings are done in a fixed edge order / - Especially efficient when / - almost all lines are outside / - almost all lines are inside. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Evaluation. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Occasionally performs several (unnecessary) clip operations on a line as test / and clippings are done in a fixed edge order / - Especially efficient when / - almost all lines are outside / - almost all lines are inside. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Evaluation'?

### Page 16 - 5.2 Cyrus-Beck Line Clipping

Source cue: Clip lines against convex polygon

Professor-style explanation: The slide '5.2 Cyrus-Beck Line Clipping' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: Clip lines against convex polygon. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about 5.2 Cyrus-Beck Line Clipping. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: Clip lines against convex polygon. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in '5.2 Cyrus-Beck Line Clipping'?

### Page 17 - Cyrus-Beck Line Clipping

Source cue: - Introduced in 1978 by Cyrus and Beck / - Algorithm for clipping lines against a convex polygon in the plane / - Expandable to clipping lines against a convex polyhedron in space / - Fundamentally different approach than Cohen-Sutherland / - Further development in 1984 by Liang and Barsky

Professor-style explanation: The slide 'Cyrus-Beck Line Clipping' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Introduced in 1978 by Cyrus and Beck / - Algorithm for clipping lines against a convex polygon in the plane / - Expandable to clipping lines against a convex polyhedron in space / - Fundamentally different approach than Cohen-Sutherland / - Further development in 1984 by Liang and Barsky. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Cyrus-Beck Line Clipping. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Introduced in 1978 by Cyrus and Beck / - Algorithm for clipping lines against a convex polygon in the plane / - Expandable to clipping lines against a convex polyhedron in space / - Fundamentally different approach than Cohen-Sutherland / - Further development in 1984 by Liang and Barsky. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Cyrus-Beck Line Clipping'?

### Page 18 - Parametric Line Representation

Source cue: - Parametric line representation written as follows / p t = p + t ⋅ p − p , 0 ≤ t ≤ 1 / 0 1 0 / - Proceeding / - Find the 4 t's for the 4 clip edges

Professor-style explanation: The slide 'Parametric Line Representation' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Parametric line representation written as follows / p t = p + t ⋅ p − p , 0 ≤ t ≤ 1 / 0 1 0 / - Proceeding / - Find the 4 t's for the 4 clip edges. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations.

Technical commentary: This slide is about Parametric Line Representation. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Parametric line representation written as follows / p t = p + t ⋅ p − p , 0 ≤ t ≤ 1 / 0 1 0 / - Proceeding / - Find the 4 t's for the 4 clip edges. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Parametric Line Representation'?

### Page 19 - Intersection Point Calculation 1/2

Source cue: - Consider edge E and its outward pointing edge normal N / - Through dot product N ⋅ (p(t) − p ) it can be decided / in which half-space a line point p(t) lies / p N  (p(t) - p ) < 0 / E E

Professor-style explanation: The slide 'Intersection Point Calculation 1/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Consider edge E and its outward pointing edge normal N / - Through dot product N ⋅ (p(t) − p ) it can be decided / in which half-space a line point p(t) lies / p N  (p(t) - p ) < 0 / E E. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations.

Technical commentary: This slide is about Intersection Point Calculation 1/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Consider edge E and its outward pointing edge normal N / - Through dot product N ⋅ (p(t) − p ) it can be decided / in which half-space a line point p(t) lies / p N  (p(t) - p ) < 0 / E E. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Intersection Point Calculation 1/2'?

### Page 20 - Intersection Point Calculation 2/2

Source cue: - Determine intersection by calculating t for / N ⋅ p t − p = 0 / - Substitution of p t and regrouping gives / N ⋅ p − p / 0 E

Professor-style explanation: The slide 'Intersection Point Calculation 2/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Determine intersection by calculating t for / N ⋅ p t − p = 0 / - Substitution of p t and regrouping gives / N ⋅ p − p / 0 E. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Intersection Point Calculation 2/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Determine intersection by calculating t for / N ⋅ p t − p = 0 / - Substitution of p t and regrouping gives / N ⋅ p − p / 0 E. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Intersection Point Calculation 2/2' into a causal sentence instead of repeating the slide title?

### Page 21 - Determine Relevant t-Values

Source cue: - Classification of intersection points as potentially entering (PE) / or potentially leaving (PL) with respect to interior of half-plane edge / s PE / PL PL PL / p s

Professor-style explanation: The slide 'Determine Relevant t-Values' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Classification of intersection points as potentially entering (PE) / or potentially leaving (PL) with respect to interior of half-plane edge / s PE / PL PL PL / p s. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Determine Relevant t-Values. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Classification of intersection points as potentially entering (PE) / or potentially leaving (PL) with respect to interior of half-plane edge / s PE / PL PL PL / p s. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Determine Relevant t-Values' into a causal sentence instead of repeating the slide title?

### Page 22 - Pseudo Code

Source cue: void cyrusBeckLineClipper(Line s, Rectangle r) { / precalculate N for edges of r and select P / i E / D = s.p1 - s.p0 / if (s.p0 == s.p1) {

Professor-style explanation: The slide 'Pseudo Code' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: void cyrusBeckLineClipper(Line s, Rectangle r) { / precalculate N for edges of r and select P / i E / D = s.p1 - s.p0 / if (s.p0 == s.p1) {. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Pseudo Code. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: void cyrusBeckLineClipper(Line s, Rectangle r) { / precalculate N for edges of r and select P / i E / D = s.p1 - s.p0 / if (s.p0 == s.p1) {. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Pseudo Code'?

### Page 23 - Axis-Parallel Clipping Region

Source cue: - When clipping region is axis parallel and given by [x , x ] × [y , y ], / min max min max / following values occur / N ⋅ p − p / 0 E

Professor-style explanation: The slide 'Axis-Parallel Clipping Region' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - When clipping region is axis parallel and given by [x , x ] × [y , y ], / min max min max / following values occur / N ⋅ p − p / 0 E. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Axis-Parallel Clipping Region. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - When clipping region is axis parallel and given by [x , x ] × [y , y ], / min max min max / following values occur / N ⋅ p − p / 0 E. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Axis-Parallel Clipping Region'?

### Page 24 - Comparison with Cohen-Sutherland

Source cue: - Algorithm of Cohen-Sutherland / - Sometimes performs useless clip operations, / as clipping and testing are done in a fixed order / - Efficient when outcode tests can be performed inexpensively (e.g., by bitwise / operations) and the majority of line segments are trivially accepted or rejected

Professor-style explanation: The slide 'Comparison with Cohen-Sutherland' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Algorithm of Cohen-Sutherland / - Sometimes performs useless clip operations, / as clipping and testing are done in a fixed order / - Efficient when outcode tests can be performed inexpensively (e.g., by bitwise / operations) and the majority of line segments are trivially accepted or rejected. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Comparison with Cohen-Sutherland. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Algorithm of Cohen-Sutherland / - Sometimes performs useless clip operations, / as clipping and testing are done in a fixed order / - Efficient when outcode tests can be performed inexpensively (e.g., by bitwise / operations) and the majority of line segments are trivially accepted or rejected. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Comparison with Cohen-Sutherland'?

### Page 25 - 5.3 Sutherland-Hodgman Polygon Clipping

Source cue: A pipelined version of the scalar product algorithm extended to clip polygons

Professor-style explanation: The slide '5.3 Sutherland-Hodgman Polygon Clipping' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: A pipelined version of the scalar product algorithm extended to clip polygons. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about 5.3 Sutherland-Hodgman Polygon Clipping. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: A pipelined version of the scalar product algorithm extended to clip polygons. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in '5.3 Sutherland-Hodgman Polygon Clipping'?

### Page 26 - Sutherland-Hodgman Polygon Clipping 1/2

Source cue: - Background / - General polygon clipping (arbitrary polygon against convex polygon) / - Originally developed for visibility detection / (apply before rasterization to eliminate non-visible polygon pieces) / - Polygon clipping is more complex than line clipping

Professor-style explanation: The slide 'Sutherland-Hodgman Polygon Clipping 1/2' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Background / - General polygon clipping (arbitrary polygon against convex polygon) / - Originally developed for visibility detection / (apply before rasterization to eliminate non-visible polygon pieces) / - Polygon clipping is more complex than line clipping. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Sutherland-Hodgman Polygon Clipping 1/2. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Background / - General polygon clipping (arbitrary polygon against convex polygon) / - Originally developed for visibility detection / (apply before rasterization to eliminate non-visible polygon pieces) / - Polygon clipping is more complex than line clipping. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Sutherland-Hodgman Polygon Clipping 1/2'?

### Page 27 - Sutherland-Hodgman Polygon Clipping 2/2

Source cue: - Iterative algorithm paradigm / - Clipping a polygon takes place against a half-plane / - Clipping is performed sequentially for each edge of the clipping region / - Input / - Convex clipping region

Professor-style explanation: The slide 'Sutherland-Hodgman Polygon Clipping 2/2' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Iterative algorithm paradigm / - Clipping a polygon takes place against a half-plane / - Clipping is performed sequentially for each edge of the clipping region / - Input / - Convex clipping region. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Sutherland-Hodgman Polygon Clipping 2/2. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Iterative algorithm paradigm / - Clipping a polygon takes place against a half-plane / - Clipping is performed sequentially for each edge of the clipping region / - Input / - Convex clipping region. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Sutherland-Hodgman Polygon Clipping 2/2'?

### Page 28 - Four Cases

Source cue: - Depending on which case occurs, following points added to output list / - Case 1: p / - Case 2: Intersection point i / - Case 3: -- / - Case 4: Intersection point i and p

Professor-style explanation: The slide 'Four Cases' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Depending on which case occurs, following points added to output list / - Case 1: p / - Case 2: Intersection point i / - Case 3: -- / - Case 4: Intersection point i and p. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Four Cases. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Depending on which case occurs, following points added to output list / - Case 1: p / - Case 2: Intersection point i / - Case 3: -- / - Case 4: Intersection point i and p. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Four Cases' into a causal sentence instead of repeating the slide title?

### Page 29 - Proceeding

Source cue: - Polygon to be clipped is defined by / - Vertices: [v , v , ... , v ] / 1 2 n / - Contour: [v , v , ... , v , v ] / 1 2 n 1

Professor-style explanation: The slide 'Proceeding' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Polygon to be clipped is defined by / - Vertices: [v , v , ... , v ] / 1 2 n / - Contour: [v , v , ... , v , v ] / 1 2 n 1. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Proceeding. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Polygon to be clipped is defined by / - Vertices: [v , v , ... , v ] / 1 2 n / - Contour: [v , v , ... , v , v ] / 1 2 n 1. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Proceeding' into a causal sentence instead of repeating the slide title?

### Page 30 - Pipeline Version

Source cue: - Speed c an be optimized through pipeline version / - Input: sequence of polygon vertices processed by "Pipeline of Clippers" / - Passing on to the next level once a new vertex has been identified / - No cache is needed during clipping / - Suitable for implementation by hardware

Professor-style explanation: The slide 'Pipeline Version' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Speed c an be optimized through pipeline version / - Input: sequence of polygon vertices processed by "Pipeline of Clippers" / - Passing on to the next level once a new vertex has been identified / - No cache is needed during clipping / - Suitable for implementation by hardware. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Pipeline Version. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Speed c an be optimized through pipeline version / - Input: sequence of polygon vertices processed by "Pipeline of Clippers" / - Passing on to the next level once a new vertex has been identified / - No cache is needed during clipping / - Suitable for implementation by hardware. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Pipeline Version'?

### Page 31 - Pseudo Code

Source cue: public VertexList shClipper(VertexList inputVertices, Edge clipE) { / VertexList outputVertices; // output list of vertices / int N = inputVertices.size(); // number of vertices to be processed / Vertex s = inputVertices.get(N-1); // get last vertex / for (int j = 0; j < N; j++) {

Professor-style explanation: The slide 'Pseudo Code' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: public VertexList shClipper(VertexList inputVertices, Edge clipE) { / VertexList outputVertices; // output list of vertices / int N = inputVertices.size(); // number of vertices to be processed / Vertex s = inputVertices.get(N-1); // get last vertex / for (int j = 0; j < N; j++) {. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Pseudo Code. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: public VertexList shClipper(VertexList inputVertices, Edge clipE) { / VertexList outputVertices; // output list of vertices / int N = inputVertices.size(); // number of vertices to be processed / Vertex s = inputVertices.get(N-1); // get last vertex / for (int j = 0; j < N; j++) {. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Pseudo Code' into a causal sentence instead of repeating the slide title?

### Page 32 - Inside Test

Source cue: - Inside test for rectangular clip regions / boolean inside(Vertex v, Edge e) { // e is edge of a clip rectangle / if (e.v1.x > e.v0.x) // bottom / if (v.y >= e.v0.y) return true; / else if (e.v1.x < e.v0.x) // top

Professor-style explanation: The slide 'Inside Test' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Inside test for rectangular clip regions / boolean inside(Vertex v, Edge e) { // e is edge of a clip rectangle / if (e.v1.x > e.v0.x) // bottom / if (v.y >= e.v0.y) return true; / else if (e.v1.x < e.v0.x) // top. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Inside Test. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Inside test for rectangular clip regions / boolean inside(Vertex v, Edge e) { // e is edge of a clip rectangle / if (e.v1.x > e.v0.x) // bottom / if (v.y >= e.v0.y) return true; / else if (e.v1.x < e.v0.x) // top. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Inside Test' into a causal sentence instead of repeating the slide title?

### Page 33 - Intersection Computation

Source cue: - For rectangular clip regions / Vertex intersect(Vertex p, Vertex s, Edge e) { / Vertex i; / if (e.v0.y == e.v1.y) { // horizontal edge / i.y = e.v0.y;

Professor-style explanation: The slide 'Intersection Computation' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - For rectangular clip regions / Vertex intersect(Vertex p, Vertex s, Edge e) { / Vertex i; / if (e.v0.y == e.v1.y) { // horizontal edge / i.y = e.v0.y. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Intersection Computation. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - For rectangular clip regions / Vertex intersect(Vertex p, Vertex s, Edge e) { / Vertex i; / if (e.v0.y == e.v1.y) { // horizontal edge / i.y = e.v0.y. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Intersection Computation' into a causal sentence instead of repeating the slide title?

### Page 34 - 5.4 Weiler-Atherton Polygon Clipping

Source cue: Clip arbitrary polygons against arbitrary clip polygons

Professor-style explanation: The slide '5.4 Weiler-Atherton Polygon Clipping' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: Clip arbitrary polygons against arbitrary clip polygons. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about 5.4 Weiler-Atherton Polygon Clipping. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: Clip arbitrary polygons against arbitrary clip polygons. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in '5.4 Weiler-Atherton Polygon Clipping'?

### Page 35 - Weiler-Atherton Polygon Clipping

Source cue: - Basic idea: edges of the clip polygon A and the polygon B to be clipped / divide the plane into disjoint regions / - Following four region types are distinguished / 1. Only-in-A (light blue) / 2. Only-in-B (gray)

Professor-style explanation: The slide 'Weiler-Atherton Polygon Clipping' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Basic idea: edges of the clip polygon A and the polygon B to be clipped / divide the plane into disjoint regions / - Following four region types are distinguished / 1. Only-in-A (light blue) / 2. Only-in-B (gray). A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Weiler-Atherton Polygon Clipping. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Basic idea: edges of the clip polygon A and the polygon B to be clipped / divide the plane into disjoint regions / - Following four region types are distinguished / 1. Only-in-A (light blue) / 2. Only-in-B (gray). A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Weiler-Atherton Polygon Clipping'?

### Page 36 - Example Run

Source cue: - Proceeding best illustrated by example run / - Given case: two partially overlapping polygons / - Insert all intersections of A and B / - Double all edge segments, and label each segment / according to the adjacent region

Professor-style explanation: The slide 'Example Run' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Proceeding best illustrated by example run / - Given case: two partially overlapping polygons / - Insert all intersections of A and B / - Double all edge segments, and label each segment / according to the adjacent region. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Example Run. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Proceeding best illustrated by example run / - Given case: two partially overlapping polygons / - Insert all intersections of A and B / - Double all edge segments, and label each segment / according to the adjacent region. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Example Run' into a causal sentence instead of repeating the slide title?

### Page 37 - Intersection Types

Source cue: - There are two intersection types that are distinguished / - Transversal intersections / - Two edges of the two polygons intersect at one point / - Procedure: intersection is inserted in vertex list of both polygons / - Segment overlaps (non-transversal)

Professor-style explanation: The slide 'Intersection Types' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - There are two intersection types that are distinguished / - Transversal intersections / - Two edges of the two polygons intersect at one point / - Procedure: intersection is inserted in vertex list of both polygons / - Segment overlaps (non-transversal). The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Intersection Types. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - There are two intersection types that are distinguished / - Transversal intersections / - Two edges of the two polygons intersect at one point / - Procedure: intersection is inserted in vertex list of both polygons / - Segment overlaps (non-transversal). The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Intersection Types' into a causal sentence instead of repeating the slide title?

### Page 38 - Contour Processing

Source cue: - In order to find the regions-enclosing contours, / one must eliminate overlaps of the contours / - Transversal intersections / - Take the contour edges of A / and insert the contour edges of B one after the other

Professor-style explanation: The slide 'Contour Processing' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - In order to find the regions-enclosing contours, / one must eliminate overlaps of the contours / - Transversal intersections / - Take the contour edges of A / and insert the contour edges of B one after the other. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Contour Processing. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - In order to find the regions-enclosing contours, / one must eliminate overlaps of the contours / - Transversal intersections / - Take the contour edges of A / and insert the contour edges of B one after the other. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Contour Processing' into a causal sentence instead of repeating the slide title?

### Page 39 - Evaluation

Source cue: - Extension to multiple polygons / - Efficiently possible through iterative application / - Alternatively, intersection points can be generated / for all polygons in in the first step / - Conclusion

Professor-style explanation: The slide 'Evaluation' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Extension to multiple polygons / - Efficiently possible through iterative application / - Alternatively, intersection points can be generated / for all polygons in in the first step / - Conclusion. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Evaluation. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Extension to multiple polygons / - Efficiently possible through iterative application / - Alternatively, intersection points can be generated / for all polygons in in the first step / - Conclusion. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Evaluation' into a causal sentence instead of repeating the slide title?

### Page 40 - 5.5 Greiner-Hormann Polygon Clipping

Source cue: Exploitation of the winding number to clip arbitrary polygons

Professor-style explanation: The slide '5.5 Greiner-Hormann Polygon Clipping' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: Exploitation of the winding number to clip arbitrary polygons. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about 5.5 Greiner-Hormann Polygon Clipping. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: Exploitation of the winding number to clip arbitrary polygons. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in '5.5 Greiner-Hormann Polygon Clipping'?

### Page 41 - Greiner-Hormann

Source cue: - Basic Idea: clipped region is made up of all edges of S that lie in C, / combined with all edges of C that lie in S / [Greiner & Hormann, TOG 1998]

Professor-style explanation: The slide 'Greiner-Hormann' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Basic Idea: clipped region is made up of all edges of S that lie in C, / combined with all edges of C that lie in S / [Greiner & Hormann, TOG 1998]. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Greiner-Hormann. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Basic Idea: clipped region is made up of all edges of S that lie in C, / combined with all edges of C that lie in S / [Greiner & Hormann, TOG 1998]. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Greiner-Hormann'?

### Page 42 - Chalk Wagon Metaphor

Source cue: - Using a chalk wagon metaphor / - Drive along all edges of A with a chalk wagon / that is only open when the current position is within B / - Drive along all edges of B with a chalk wagon / that is only open when the current position is within A

Professor-style explanation: The slide 'Chalk Wagon Metaphor' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Using a chalk wagon metaphor / - Drive along all edges of A with a chalk wagon / that is only open when the current position is within B / - Drive along all edges of B with a chalk wagon / that is only open when the current position is within A. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Chalk Wagon Metaphor. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Using a chalk wagon metaphor / - Drive along all edges of A with a chalk wagon / that is only open when the current position is within B / - Drive along all edges of B with a chalk wagon / that is only open when the current position is within A. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Chalk Wagon Metaphor' into a causal sentence instead of repeating the slide title?

### Page 43 - Contour Detection

Source cue: - The edges of polygon A within polygon B can thus be found as follows / - Insert in A all intersection points with B / - Start at any vertex v of A / - If v is within B, the edge flag is turned on, otherwise not / - Traverse edges of A and invert edge marker flag when intersecting with B

Professor-style explanation: The slide 'Contour Detection' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - The edges of polygon A within polygon B can thus be found as follows / - Insert in A all intersection points with B / - Start at any vertex v of A / - If v is within B, the edge flag is turned on, otherwise not / - Traverse edges of A and invert edge marker flag when intersecting with B. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Contour Detection. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - The edges of polygon A within polygon B can thus be found as follows / - Insert in A all intersection points with B / - Start at any vertex v of A / - If v is within B, the edge flag is turned on, otherwise not / - Traverse edges of A and invert edge marker flag when intersecting with B. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Contour Detection' into a causal sentence instead of repeating the slide title?

### Page 44 - Set Operations

Source cue: [Greiner & Hormann, TOG 1998]

Professor-style explanation: The slide 'Set Operations' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: [Greiner & Hormann, TOG 1998]. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Set Operations. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: [Greiner & Hormann, TOG 1998]. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Set Operations'?

### Page 45 - Data Structure 1/2

Source cue: - Polygons exist as a closed, double-linked list / P , P , P , ... , P = P / 0 1 2 n 0 / - The following segments are included / P P , P P , ... , P P = P P

Professor-style explanation: The slide 'Data Structure 1/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Polygons exist as a closed, double-linked list / P , P , P , ... , P = P / 0 1 2 n 0 / - The following segments are included / P P , P P , ... , P P = P P. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Data Structure 1/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Polygons exist as a closed, double-linked list / P , P , P , ... , P = P / 0 1 2 n 0 / - The following segments are included / P P , P P , ... , P P = P P. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Data Structure 1/2' into a causal sentence instead of repeating the slide title?

### Page 46 - Data Structure 2/2

Source cue: [Greiner & Hormann, TOG 1998]

Professor-style explanation: The slide 'Data Structure 2/2' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: [Greiner & Hormann, TOG 1998]. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Data Structure 2/2. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: [Greiner & Hormann, TOG 1998]. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Data Structure 2/2'?

### Page 47 - Proceeding

Source cue: - Create data structure / - Create doubly linked list with node data structure / - Add the intersections with the corresponding alpha values to the list / - Traverse the polygon to find entry and exit points / (use winding number rule)

Professor-style explanation: The slide 'Proceeding' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Create data structure / - Create doubly linked list with node data structure / - Add the intersections with the corresponding alpha values to the list / - Traverse the polygon to find entry and exit points / (use winding number rule). The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Proceeding. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Create data structure / - Create doubly linked list with node data structure / - Add the intersections with the corresponding alpha values to the list / - Traverse the polygon to find entry and exit points / (use winding number rule). The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Proceeding' into a causal sentence instead of repeating the slide title?

### Page 48 - Pseudo Code

Source cue: while unprocessed intersections in subject polygon / current = first unprocessed intersecting / point of subject polygon / newPolygon() / newVertex(current)

Professor-style explanation: The slide 'Pseudo Code' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: while unprocessed intersections in subject polygon / current = first unprocessed intersecting / point of subject polygon / newPolygon() / newVertex(current). The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Pseudo Code. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: while unprocessed intersections in subject polygon / current = first unprocessed intersecting / point of subject polygon / newPolygon() / newVertex(current). The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Pseudo Code' into a causal sentence instead of repeating the slide title?

### Page 49 - Winding Number 1/3

Source cue: - Winding number of a point A and a closed curve γ / indicates the number of times a ray that traverses the entire curve from A / winds around A / ω γ, A = dφ / - Counterclockwise: +1

Professor-style explanation: The slide 'Winding Number 1/3' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Winding number of a point A and a closed curve γ / indicates the number of times a ray that traverses the entire curve from A / winds around A / ω γ, A = dφ / - Counterclockwise: +1. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing.

Technical commentary: This slide is about Winding Number 1/3. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Winding number of a point A and a closed curve γ / indicates the number of times a ray that traverses the entire curve from A / winds around A / ω γ, A = dφ / - Counterclockwise: +1. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'Winding Number 1/3' works per object, per image region, per ray, or per fragment?

### Page 50 - Winding Number 2/3

Source cue: - The winding number of a point A has the following useful properties / 1. If A or the curve γ is continuously changed so that A maintains a / positive distance to γ, the winding number will not change / For curve γ, the winding number is constant in each region formed by γ / 2. When A moves and γ crosses once, winding number changes by exactly 1

Professor-style explanation: The slide 'Winding Number 2/3' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - The winding number of a point A has the following useful properties / 1. If A or the curve γ is continuously changed so that A maintains a / positive distance to γ, the winding number will not change / For curve γ, the winding number is constant in each region formed by γ / 2. When A moves and γ crosses once, winding number changes by exactly 1. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Winding Number 2/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - The winding number of a point A has the following useful properties / 1. If A or the curve γ is continuously changed so that A maintains a / positive distance to γ, the winding number will not change / For curve γ, the winding number is constant in each region formed by γ / 2. When A moves and γ crosses once, winding number changes by exactly 1. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Winding Number 2/3' into a causal sentence instead of repeating the slide title?

### Page 51 - Winding Number 3/3

Source cue: - From the second property follows / - A path that cuts a curve (= the clipping polygon) just once, / runs either from inside to outside, or from outside to inside / - Clipping operation can be performed by computing / [Greiner & Hormann, TOG 1998]

Professor-style explanation: The slide 'Winding Number 3/3' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - From the second property follows / - A path that cuts a curve (= the clipping polygon) just once, / runs either from inside to outside, or from outside to inside / - Clipping operation can be performed by computing / [Greiner & Hormann, TOG 1998]. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Winding Number 3/3. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - From the second property follows / - A path that cuts a curve (= the clipping polygon) just once, / runs either from inside to outside, or from outside to inside / - Clipping operation can be performed by computing / [Greiner & Hormann, TOG 1998]. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Winding Number 3/3'?

### Page 52 - Special Cases

Source cue: - Simple cases can be solved after unsuccessful intersection calculation / directly via winding number operation / - One polygon is contained in the other polygon / - Polygons have no overlaps / - Problem: One point lies on one edge

Professor-style explanation: The slide 'Special Cases' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Simple cases can be solved after unsuccessful intersection calculation / directly via winding number operation / - One polygon is contained in the other polygon / - Polygons have no overlaps / - Problem: One point lies on one edge. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Special Cases. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Simple cases can be solved after unsuccessful intersection calculation / directly via winding number operation / - One polygon is contained in the other polygon / - Polygons have no overlaps / - Problem: One point lies on one edge. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Special Cases' into a causal sentence instead of repeating the slide title?

### Page 53 - Evaluation

Source cue: - Allows efficient clipping of arbitrary 2D polygons / - Self overlaps and holes allowed / - Idea based on definition of winding number / - Very simple and efficient implementation possible / - Much easier than Weiler-Atherton,

Professor-style explanation: The slide 'Evaluation' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Allows efficient clipping of arbitrary 2D polygons / - Self overlaps and holes allowed / - Idea based on definition of winding number / - Very simple and efficient implementation possible / - Much easier than Weiler-Atherton,. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about Evaluation. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Allows efficient clipping of arbitrary 2D polygons / - Self overlaps and holes allowed / - Idea based on definition of winding number / - Very simple and efficient implementation possible / - Much easier than Weiler-Atherton,. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Evaluation'?

### Page 54 - by exploiting binary outcodes

Source cue: - Cohen-Sutherland enables line clipping against rectangle / by exploiting binary outcodes / - Cyrus-Beck line clipping enables line clipping against convex polygon / by exploiting parametric representations / - Sutherland-Hodgman polygon clipping enables polygon against convex polygon

Professor-style explanation: The slide 'by exploiting binary outcodes' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Cohen-Sutherland enables line clipping against rectangle / by exploiting binary outcodes / - Cyrus-Beck line clipping enables line clipping against convex polygon / by exploiting parametric representations / - Sutherland-Hodgman polygon clipping enables polygon against convex polygon. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion.

Technical commentary: This slide is about by exploiting binary outcodes. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Cohen-Sutherland enables line clipping against rectangle / by exploiting binary outcodes / - Cyrus-Beck line clipping enables line clipping against convex polygon / by exploiting parametric representations / - Sutherland-Hodgman polygon clipping enables polygon against convex polygon. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'by exploiting binary outcodes'?

### Page 55 - Literature and other sources used in this chapter

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Literature and other sources used in this chapter' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail.

Technical commentary: This slide is about Literature and other sources used in this chapter. The slide lists source material or chapter references that support the technical content and give names for further reading. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Reference slides provide the source trail for definitions, algorithms, and deeper explanations.

Check yourself: Can you identify which source or topic 'Literature and other sources used in this chapter' points to for deeper study?

### Page 56 - Addison-Wesley 2013.

Source cue: - Text Books / - J. Foley, A. van Dam, S. Feiner. "Computer Graphics: Principles and Practice (3rd Edition)", / Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner. "Fundamentals of Computer Graphics (4th / Edition)", AK Peters 2016.

Professor-style explanation: The slide 'Addison-Wesley 2013.' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Text Books / - J. Foley, A. van Dam, S. Feiner. "Computer Graphics: Principles and Practice (3rd Edition)", / Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner. "Fundamentals of Computer Graphics (4th / Edition)", AK Peters 2016. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Addison-Wesley 2013.. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Text Books / - J. Foley, A. van Dam, S. Feiner. "Computer Graphics: Principles and Practice (3rd Edition)", / Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner. "Fundamentals of Computer Graphics (4th / Edition)", AK Peters 2016. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Addison-Wesley 2013.' into a causal sentence instead of repeating the slide title?

## 05.1 Cohen-Sutherland Line Clipping

Source location: Section 5.1

### Commentary

Cohen-Sutherland assigns outcodes to line endpoints based on which side of the clipping window they lie on. These codes allow quick accept, quick reject, or partial clipping. The algorithm is efficient because many cases are decided before computing intersections.

The exam-friendly idea is the logic of region codes: if both endpoints are inside, keep the segment. If the bitwise AND of the outcodes is nonzero, both endpoints share an outside region and the segment can be rejected. Otherwise, compute an intersection and continue.

### Mental Model

Outcodes are a cheap classification before doing intersection math.

### Check Yourself

What does a nonzero bitwise AND of two endpoint outcodes imply?

## 05.2 Cyrus-Beck Line Clipping

Source location: Section 5.2

### Commentary

Cyrus-Beck treats the line parametrically and clips against convex boundaries. Instead of repeatedly using region codes, it finds entering and leaving parameter values along the line.

The key is to reason about the line parameter t. A clipped line segment is not a new unrelated line; it is a restricted interval of the original parametric line. Boundary tests shrink that interval.

### Mental Model

Clipping a parametric line means narrowing the valid t interval.

### Check Yourself

Why does Cyrus-Beck naturally require convex clipping regions?

## 05.3 Sutherland-Hodgman Polygon Clipping

Source location: Section 5.3

### Commentary

Sutherland-Hodgman clips a polygon against one boundary at a time. For each edge of the polygon, it decides whether vertices are inside or outside and emits zero, one, or two vertices depending on transitions across the boundary.

This algorithm is easiest to understand as a stream processor. Feed in a polygon, clip it against the left boundary, feed the result into the right boundary, and so on. Each boundary can add intersection vertices.

### Mental Model

Polygon clipping is repeated edge-by-edge filtering plus intersection insertion.

### Check Yourself

When can polygon clipping increase the number of vertices?

## 05.4 Weiler-Atherton and Greiner-Hormann

Source location: Sections 5.4-5.5

### Commentary

These algorithms address more complex polygon clipping scenarios, especially when polygon relationships are not as simple as convex-window clipping. They organize intersections and traversal rules to produce correct output boundaries.

For preparation, focus on why simpler algorithms are not enough. Complex polygon intersection can require following alternating boundaries of subject and clipping polygons. That is a topology problem, not only a line-intersection problem.

### Mental Model

Complex polygon clipping is about traversing boundary networks after intersections are known.

### Check Yourself

Why are intersection ordering and traversal rules important for polygon clipping?

## End-of-Lecture Summary

If you remember only one thing from Lecture 05, remember this: This lecture focuses on algorithms that remove or trim geometry against boundaries. Clipping is a geometric operation before rasterization, not a visibility test between overlapping objects.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
