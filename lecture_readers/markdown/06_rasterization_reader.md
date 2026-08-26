# Lecture 06 - Rasterization

Source chunk: `course_text_parts/03_lectures/06_rasterization.txt`
Extracted slide pages in source chunk: 61

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture explains how continuous primitives become discrete fragments on a grid. Rasterization is the bridge from geometric descriptions to sample-based image generation.

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

### Page 2 - Rasterization 1/2

Source cue: - Pixels ... / - ... are picture elements A Pixel Is NotA Little Square, / A Pixel Is NotA Little Square, / - ... are the smallest elements of a raster image / A Pixel Is NotA Little Square!

Professor-style explanation: The slide 'Rasterization 1/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Pixels ... / - ... are picture elements A Pixel Is NotA Little Square, / A Pixel Is NotA Little Square, / - ... are the smallest elements of a raster image / A Pixel Is NotA Little Square!. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Rasterization 1/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Pixels ... / - ... are picture elements A Pixel Is NotA Little Square, / A Pixel Is NotA Little Square, / - ... are the smallest elements of a raster image / A Pixel Is NotA Little Square!. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Rasterization 1/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Rasterization 1/2'?

### Page 3 - Rasterization 2/2

Source cue: - Pixel-based displays require discretization of primitives into pixels / - Discretization is done by rasterization algorithms / - Rasterization is time-critical / - Avoid expensive operations / - Optimize for hardware implementation

Professor-style explanation: The slide 'Rasterization 2/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Pixel-based displays require discretization of primitives into pixels / - Discretization is done by rasterization algorithms / - Rasterization is time-critical / - Avoid expensive operations / - Optimize for hardware implementation. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Rasterization 2/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Pixel-based displays require discretization of primitives into pixels / - Discretization is done by rasterization algorithms / - Rasterization is time-critical / - Avoid expensive operations / - Optimize for hardware implementation. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Rasterization 2/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Rasterization 2/2'?

### Page 4 - 6.1 Line Rasterization

Source cue: 6.2 Triangle Edge Rasterization / 6.3 Region Filling / 6.4 Scanline-Based Triangle Rasterization / 6.5 Block-Based Triangle Rasterization

Professor-style explanation: The outline '6.1 Line Rasterization' gives the lecture its internal logic. The listed topics are the objects that will be connected during the chapter: first the problem space, then the mathematical or algorithmic tools, then the implementation consequences. The listed entries form a dependency order: 6.2 Triangle Edge Rasterization / 6.3 Region Filling / 6.4 Scanline-Based Triangle Rasterization / 6.5 Block-Based Triangle Rasterization. Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary. The order matters because later items rely on earlier definitions. For example, an OpenGL mechanism is much easier to understand once the corresponding pipeline object or mathematical operation has already been introduced. The outline is therefore a compact dependency graph of the lecture rather than a collection of isolated labels. For examination purposes, the important content is the dependency structure: which concept introduces the vocabulary, which later algorithm uses it, and which implementation problem it solves.

Technical commentary: This slide is about 6.1 Line Rasterization. The listed items define the lecture sequence: the topic begins with a problem statement, introduces the required objects or algorithms, and then connects them to rendering or implementation consequences. The listed entries form a dependency order: 6.2 Triangle Edge Rasterization / 6.3 Region Filling / 6.4 Scanline-Based Triangle Rasterization / 6.5 Block-Based Triangle Rasterization. Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary.

Why it matters: Outlines tell you the dependency order. They are the safest way to avoid learning isolated bullet points.

Exam-grade answer: A strong answer for '6.1 Line Rasterization' names the topics in order and explains at least one dependency between an earlier item and a later item.

Common trap: Do not memorize '6.1 Line Rasterization' as a list of headings only; the exam-relevant part is how the headings depend on each other.

Check yourself: Can you explain where '6.1 Line Rasterization' fits in the lecture order and what later section depends on it?

### Page 5 - 6.1 Line Rasterization

Source cue: Drawing a one pixel thick line

Professor-style explanation: The slide '6.1 Line Rasterization' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: Drawing a one pixel thick line. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about 6.1 Line Rasterization. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: Drawing a one pixel thick line. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for '6.1 Line Rasterization' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by '6.1 Line Rasterization'?

### Page 6 - Line Rasterization

Source cue: - Given two 2D endpoints in integer coordinates, / determine pixels depicting 1-pixel wide line segment between endpoints / - Trivial cases / - Horizontal line segments / - Vertical line segments

Professor-style explanation: The slide 'Line Rasterization' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Given two 2D endpoints in integer coordinates, / determine pixels depicting 1-pixel wide line segment between endpoints / - Trivial cases / - Horizontal line segments / - Vertical line segments. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Line Rasterization. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Given two 2D endpoints in integer coordinates, / determine pixels depicting 1-pixel wide line segment between endpoints / - Trivial cases / - Horizontal line segments / - Vertical line segments. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Line Rasterization' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Line Rasterization' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Line Rasterization'?

### Page 7 - Quality Criteria

Source cue: - For all line segments with a slope |m| ≤ 1, / one pixel should be drawn per column / - For all line segments with a slope |m| ≥ 1, / one pixel per line should be drawn / |m| > 1

Professor-style explanation: The slide 'Quality Criteria' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - For all line segments with a slope |m| ≤ 1, / one pixel should be drawn per column / - For all line segments with a slope |m| ≥ 1, / one pixel per line should be drawn / |m| > 1. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Quality Criteria. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - For all line segments with a slope |m| ≤ 1, / one pixel should be drawn per column / - For all line segments with a slope |m| ≥ 1, / one pixel per line should be drawn / |m| > 1. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Quality Criteria' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Quality Criteria'?

### Page 8 - Naïve Algorithm 1/2

Source cue: - Utilization of the Cartesian normal form of the straight line equation / y = m · x + B / - Assumptions (without restriction of generality) / - Line segments lie between (x , y ) and (x , y ) / 0 0 1 1

Professor-style explanation: The slide 'Naïve Algorithm 1/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Utilization of the Cartesian normal form of the straight line equation / y = m · x + B / - Assumptions (without restriction of generality) / - Line segments lie between (x , y ) and (x , y ) / 0 0 1 1. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Naïve Algorithm 1/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Utilization of the Cartesian normal form of the straight line equation / y = m · x + B / - Assumptions (without restriction of generality) / - Line segments lie between (x , y ) and (x , y ) / 0 0 1 1. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Naïve Algorithm 1/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Naïve Algorithm 1/2'?

### Page 9 - Naïve Algorithm 2/2

Source cue: - Downsides / - Does not work for x = x / 0 1 / - Does not work for |m| > 1, since gaps arise / (solution: swap the roles of x and y for |m| > 1)

Professor-style explanation: The slide 'Naïve Algorithm 2/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Downsides / - Does not work for x = x / 0 1 / - Does not work for |m| > 1, since gaps arise / (solution: swap the roles of x and y for |m| > 1). The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Naïve Algorithm 2/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Downsides / - Does not work for x = x / 0 1 / - Does not work for |m| > 1, since gaps arise / (solution: swap the roles of x and y for |m| > 1). The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Naïve Algorithm 2/2' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Naïve Algorithm 2/2' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Naïve Algorithm 2/2' into a causal sentence instead of repeating the slide title?

### Page 10 - Digital Difference Analyzer (DDA) 1/3

Source cue: - Reuse the last computed y to avoid multiplications in the loop / x → x + 1 ⇒ (x, y) → (x + 1, y + m) / void drawLine(int x0, int y0, int x1, int y1) { / float m = float(y1 - y0) / float(x1 - x0); // Calculate the slope / float y = y0; // Start y at y0

Professor-style explanation: The slide 'Digital Difference Analyzer (DDA) 1/3' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Reuse the last computed y to avoid multiplications in the loop / x → x + 1 ⇒ (x, y) → (x + 1, y + m) / void drawLine(int x0, int y0, int x1, int y1) { / float m = float(y1 - y0) / float(x1 - x0); // Calculate the slope / float y = y0; // Start y at y0. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Digital Difference Analyzer (DDA) 1/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Reuse the last computed y to avoid multiplications in the loop / x → x + 1 ⇒ (x, y) → (x + 1, y + m) / void drawLine(int x0, int y0, int x1, int y1) { / float m = float(y1 - y0) / float(x1 - x0); // Calculate the slope / float y = y0; // Start y at y0. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Digital Difference Analyzer (DDA) 1/3' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Digital Difference Analyzer (DDA) 1/3' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Digital Difference Analyzer (DDA) 1/3' into a causal sentence instead of repeating the slide title?

### Page 11 - Digital Difference Analyzer (DDA) 2/3

Source cue: - Algorithm can be extended to relax endpoint order / void drawLine(int x0, int y0, int x1, int y1) { / int sx = (x0 < x1 ? 1 : -1); // Determine x direction / float sm = sx * float(y1 - y0) / float(x1 - x0); // Calculate slope multiplied by step / float y = y0; // Start y at y0

Professor-style explanation: The slide 'Digital Difference Analyzer (DDA) 2/3' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Algorithm can be extended to relax endpoint order / void drawLine(int x0, int y0, int x1, int y1) { / int sx = (x0 < x1 ? 1 : -1); // Determine x direction / float sm = sx * float(y1 - y0) / float(x1 - x0); // Calculate slope multiplied by step / float y = y0; // Start y at y0. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Digital Difference Analyzer (DDA) 2/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Algorithm can be extended to relax endpoint order / void drawLine(int x0, int y0, int x1, int y1) { / int sx = (x0 < x1 ? 1 : -1); // Determine x direction / float sm = sx * float(y1 - y0) / float(x1 - x0); // Calculate slope multiplied by step / float y = y0; // Start y at y0. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Digital Difference Analyzer (DDA) 2/3' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Digital Difference Analyzer (DDA) 2/3' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Digital Difference Analyzer (DDA) 2/3' into a causal sentence instead of repeating the slide title?

### Page 12 - Digital Difference Analyzer (DDA) 3/3

Source cue: - Downsides / - Does not work for x = x / 0 1 / - Does not work for |m| > 1, since gaps arise / (solution: swap the roles of x and y for |m| > 1)

Professor-style explanation: The slide 'Digital Difference Analyzer (DDA) 3/3' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Downsides / - Does not work for x = x / 0 1 / - Does not work for |m| > 1, since gaps arise / (solution: swap the roles of x and y for |m| > 1). The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Digital Difference Analyzer (DDA) 3/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Downsides / - Does not work for x = x / 0 1 / - Does not work for |m| > 1, since gaps arise / (solution: swap the roles of x and y for |m| > 1). The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Digital Difference Analyzer (DDA) 3/3' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Digital Difference Analyzer (DDA) 3/3' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Digital Difference Analyzer (DDA) 3/3' into a causal sentence instead of repeating the slide title?

### Page 13 - Midpoint-Line Algorithm 1/2

Source cue: - Assumption 1: 0 ≤ m ≤ 1 / (without loss of generality, as otherwise mirroring on axes/diagonals) / - Lower left end point P = (x , y ), / 0 0 0 / upper right end point P = (x , y )

Professor-style explanation: The slide 'Midpoint-Line Algorithm 1/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Assumption 1: 0 ≤ m ≤ 1 / (without loss of generality, as otherwise mirroring on axes/diagonals) / - Lower left end point P = (x , y ), / 0 0 0 / upper right end point P = (x , y ). A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Midpoint-Line Algorithm 1/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Assumption 1: 0 ≤ m ≤ 1 / (without loss of generality, as otherwise mirroring on axes/diagonals) / - Lower left end point P = (x , y ), / 0 0 0 / upper right end point P = (x , y ). A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Midpoint-Line Algorithm 1/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Midpoint-Line Algorithm 1/2'?

### Page 14 - Midpoint-Line Algorithm 2/2

Source cue: - Observation / - E is closer to the line if M is above the line / - NE is closer to the line if M is below the line / - Vertical distance between pixel to chose / and the actual line segment is always < 0.5

Professor-style explanation: The slide 'Midpoint-Line Algorithm 2/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Observation / - E is closer to the line if M is above the line / - NE is closer to the line if M is below the line / - Vertical distance between pixel to chose / and the actual line segment is always < 0.5. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Midpoint-Line Algorithm 2/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Observation / - E is closer to the line if M is above the line / - NE is closer to the line if M is below the line / - Vertical distance between pixel to chose / and the actual line segment is always < 0.5. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Midpoint-Line Algorithm 2/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Midpoint-Line Algorithm 2/2'?

### Page 15 - Implicit Function

Source cue: - Line equation usually given as explicit function f(x) / f x = y = m ⋅ x + B = ⋅ x + B, with dx = x − x and dy = y − y / 1 o 1 o / - Line equation can also be written as implicit function F(x, y) / F x, y = a ⋅ x + b ⋅ y + c = 0

Professor-style explanation: The slide 'Implicit Function' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Line equation usually given as explicit function f(x) / f x = y = m ⋅ x + B = ⋅ x + B, with dx = x − x and dy = y − y / 1 o 1 o / - Line equation can also be written as implicit function F(x, y) / F x, y = a ⋅ x + b ⋅ y + c = 0. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Implicit Function. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Line equation usually given as explicit function f(x) / f x = y = m ⋅ x + B = ⋅ x + B, with dx = x − x and dy = y − y / 1 o 1 o / - Line equation can also be written as implicit function F(x, y) / F x, y = a ⋅ x + b ⋅ y + c = 0. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Implicit Function' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Implicit Function'?

### Page 16 - Decision Variable d

Source cue: - Sign of F(M) is sufficient to decide which point is chosen / - Define decision variable d as d = F M = F(x + 1, y + ) / p p / - If d > 0, select NE (M below the line) / - If d < 0, select E (M above the line)

Professor-style explanation: The slide 'Decision Variable d' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Sign of F(M) is sufficient to decide which point is chosen / - Define decision variable d as d = F M = F(x + 1, y + ) / p p / - If d > 0, select NE (M below the line) / - If d < 0, select E (M above the line). The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Decision Variable d. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Sign of F(M) is sufficient to decide which point is chosen / - Define decision variable d as d = F M = F(x + 1, y + ) / p p / - If d > 0, select NE (M below the line) / - If d < 0, select E (M above the line). The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Decision Variable d' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Decision Variable d' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Decision Variable d' into a causal sentence instead of repeating the slide title?

### Page 17 - Update of d for E

Source cue: - Previous decision variable was given by / 1 1 / d = F x + 1, y + = a ⋅ x + 1 + b ⋅ y + + c / old p p p p / 2 2

Professor-style explanation: The slide 'Update of d for E' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Previous decision variable was given by / 1 1 / d = F x + 1, y + = a ⋅ x + 1 + b ⋅ y + + c / old p p p p / 2 2. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Update of d for E. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Previous decision variable was given by / 1 1 / d = F x + 1, y + = a ⋅ x + 1 + b ⋅ y + + c / old p p p p / 2 2. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Update of d for E' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Update of d for E' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Update of d for E' into a causal sentence instead of repeating the slide title?

### Page 18 - Update of d for NE

Source cue: - Previous decision variable was given by / 1 1 / d = F x + 1, y + = a ⋅ x + 1 + b ⋅ y + + c / old p p p p / 2 2

Professor-style explanation: The slide 'Update of d for NE' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Previous decision variable was given by / 1 1 / d = F x + 1, y + = a ⋅ x + 1 + b ⋅ y + + c / old p p p p / 2 2. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Update of d for NE. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Previous decision variable was given by / 1 1 / d = F x + 1, y + = a ⋅ x + 1 + b ⋅ y + + c / old p p p p / 2 2. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Update of d for NE' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Update of d for NE' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Update of d for NE' into a causal sentence instead of repeating the slide title?

### Page 19 - Proceeding

Source cue: - In each step, the algorithm selects between two pixels NE and E / based on sign of decision variable d / - Depending on the choice, decision variable is updated / by adding difference ΔNE or ΔE

Professor-style explanation: The slide 'Proceeding' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - In each step, the algorithm selects between two pixels NE and E / based on sign of decision variable d / - Depending on the choice, decision variable is updated / by adding difference ΔNE or ΔE. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Proceeding. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - In each step, the algorithm selects between two pixels NE and E / based on sign of decision variable d / - Depending on the choice, decision variable is updated / by adding difference ΔNE or ΔE. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Proceeding' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Proceeding' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Proceeding' into a causal sentence instead of repeating the slide title?

### Page 20 - Initializing d

Source cue: - First midpoint M is located at (x + 1, y + ) / 0 0 / 1 1 b / F x + 1, y + = a ⋅ x + 1 + b ⋅ y + + c = a ⋅ x + b ⋅ y + c + a + / 0 0 0 0 0 0

Professor-style explanation: The slide 'Initializing d' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - First midpoint M is located at (x + 1, y + ) / 0 0 / 1 1 b / F x + 1, y + = a ⋅ x + 1 + b ⋅ y + + c = a ⋅ x + b ⋅ y + c + a + / 0 0 0 0 0 0. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Initializing d. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - First midpoint M is located at (x + 1, y + ) / 0 0 / 1 1 b / F x + 1, y + = a ⋅ x + 1 + b ⋅ y + + c = a ⋅ x + b ⋅ y + c + a + / 0 0 0 0 0 0. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Initializing d' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Initializing d' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Initializing d' into a causal sentence instead of repeating the slide title?

### Page 21 - Using d

Source cue: - Midpoint line algorithms uses d as follows / d = 2 · dy - dx / start / ΔNE = 2 · dy - dx / ΔE = 2 · dy

Professor-style explanation: The slide 'Using d' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Midpoint line algorithms uses d as follows / d = 2 · dy - dx / start / ΔNE = 2 · dy - dx / ΔE = 2 · dy. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Using d. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Midpoint line algorithms uses d as follows / d = 2 · dy - dx / start / ΔNE = 2 · dy - dx / ΔE = 2 · dy. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Using d' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Using d'?

### Page 22 - Pseudo Code - Simple Version

Source cue: void midPointLine(int x0, int y0, int x1, int y1) { / int dx = x1 - x0; // Calculate delta x / int dy = y1 - y0; // Calculate delta y / int d = 2 * dy - dx; // Initial decision variable / int dE = 2 * dy; // Increment used for move to E

Professor-style explanation: The slide 'Pseudo Code - Simple Version' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: void midPointLine(int x0, int y0, int x1, int y1) { / int dx = x1 - x0; // Calculate delta x / int dy = y1 - y0; // Calculate delta y / int d = 2 * dy - dx; // Initial decision variable / int dE = 2 * dy; // Increment used for move to E. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Pseudo Code - Simple Version. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: void midPointLine(int x0, int y0, int x1, int y1) { / int dx = x1 - x0; // Calculate delta x / int dy = y1 - y0; // Calculate delta y / int d = 2 * dy - dx; // Initial decision variable / int dE = 2 * dy; // Increment used for move to E. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Pseudo Code - Simple Version' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Pseudo Code - Simple Version' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Pseudo Code - Simple Version' into a causal sentence instead of repeating the slide title?

### Page 23 - Example

Source cue: - Draw line from (5, 8) to (9, 11) / - Order of values for d / - 2, 0, 6, 4 / - Order of chosen pixels / - NE, E, NE, NE

Professor-style explanation: The slide 'Example' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Draw line from (5, 8) to (9, 11) / - Order of values for d / - 2, 0, 6, 4 / - Order of chosen pixels / - NE, E, NE, NE. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Example. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Draw line from (5, 8) to (9, 11) / - Order of values for d / - 2, 0, 6, 4 / - Order of chosen pixels / - NE, E, NE, NE. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Example' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Example'?

### Page 24 - Evaluation

Source cue: - Necessary arithmetic operations / - As only integer values are used, only integer operations are necessary / - Additions/subtractions only and multiplication by 2 / (left shift by 1 bit position) / - No multiplications in the loop

Professor-style explanation: The slide 'Evaluation' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Necessary arithmetic operations / - As only integer values are used, only integer operations are necessary / - Additions/subtractions only and multiplication by 2 / (left shift by 1 bit position) / - No multiplications in the loop. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Evaluation. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Necessary arithmetic operations / - As only integer values are used, only integer operations are necessary / - Additions/subtractions only and multiplication by 2 / (left shift by 1 bit position) / - No multiplications in the loop. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Evaluation' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Evaluation' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Evaluation' into a causal sentence instead of repeating the slide title?

### Page 25 - Pseudo Code - Reversible

Source cue: void drawLine(int x0, int y0, int x1, int y1) { / int dx = abs(x1 - x0); // Calculate absolute delta x / int sx = (x0 < x1 ? 1 : -1); // Set step x based on direction / int dy = abs(y1 - y0); // Calculate absolute delta y / int sy = (y0 < y1 ? 1 : -1); // Set step y based on direction

Professor-style explanation: The slide 'Pseudo Code - Reversible' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: void drawLine(int x0, int y0, int x1, int y1) { / int dx = abs(x1 - x0); // Calculate absolute delta x / int sx = (x0 < x1 ? 1 : -1); // Set step x based on direction / int dy = abs(y1 - y0); // Calculate absolute delta y / int sy = (y0 < y1 ? 1 : -1); // Set step y based on direction. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Pseudo Code - Reversible. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: void drawLine(int x0, int y0, int x1, int y1) { / int dx = abs(x1 - x0); // Calculate absolute delta x / int sx = (x0 < x1 ? 1 : -1); // Set step x based on direction / int dy = abs(y1 - y0); // Calculate absolute delta y / int sy = (y0 < y1 ? 1 : -1); // Set step y based on direction. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Pseudo Code - Reversible' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Pseudo Code - Reversible' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Pseudo Code - Reversible' into a causal sentence instead of repeating the slide title?

### Page 26 - 6.2 Triangle Edge Rasterization

Source cue: Drawing a one pixel thick triangle edge

Professor-style explanation: The slide '6.2 Triangle Edge Rasterization' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: Drawing a one pixel thick triangle edge. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about 6.2 Triangle Edge Rasterization. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: Drawing a one pixel thick triangle edge. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for '6.2 Triangle Edge Rasterization' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by '6.2 Triangle Edge Rasterization'?

### Page 27 - Triangle Edges 1/2

Source cue: - Using midpoint line algorithm for triangle edge rasterization / - Provides pixels closest to triangle edge / - Does not consider if pixel lies inside or outside triangle / ⇒ Edge pixels can penetrate into interior of adjacent triangles

Professor-style explanation: The slide 'Triangle Edges 1/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Using midpoint line algorithm for triangle edge rasterization / - Provides pixels closest to triangle edge / - Does not consider if pixel lies inside or outside triangle / ⇒ Edge pixels can penetrate into interior of adjacent triangles. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Triangle Edges 1/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Using midpoint line algorithm for triangle edge rasterization / - Provides pixels closest to triangle edge / - Does not consider if pixel lies inside or outside triangle / ⇒ Edge pixels can penetrate into interior of adjacent triangles. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Triangle Edges 1/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Triangle Edges 1/2'?

### Page 28 - Triangle Edges 2/2

Source cue: - Midpoint line algorithm must consider inside vs. outside pixels / - Adaptation of the midpoint line algorithm / - Restriction to pixels strictly inside triangle / - Must be applied to line rasterization also for consistency reasons / - Definition of triangle inside:

Professor-style explanation: The slide 'Triangle Edges 2/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Midpoint line algorithm must consider inside vs. outside pixels / - Adaptation of the midpoint line algorithm / - Restriction to pixels strictly inside triangle / - Must be applied to line rasterization also for consistency reasons / - Definition of triangle inside. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Triangle Edges 2/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Midpoint line algorithm must consider inside vs. outside pixels / - Adaptation of the midpoint line algorithm / - Restriction to pixels strictly inside triangle / - Must be applied to line rasterization also for consistency reasons / - Definition of triangle inside. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Triangle Edges 2/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Triangle Edges 2/2'?

### Page 29 - Edge Rasterization 1/3

Source cue: - Triangle edge rasterization can exploit edge coherence / - Two edges of triangle intersect a scanline / - Same edges intersected by scanline i likely also intersect scanline i + 1 / - Due to coherence, intersections can be calculated incrementally / - For each increase of y → y + 1

Professor-style explanation: The slide 'Edge Rasterization 1/3' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Triangle edge rasterization can exploit edge coherence / - Two edges of triangle intersect a scanline / - Same edges intersected by scanline i likely also intersect scanline i + 1 / - Due to coherence, intersections can be calculated incrementally / - For each increase of y → y + 1. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Edge Rasterization 1/3. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Triangle edge rasterization can exploit edge coherence / - Two edges of triangle intersect a scanline / - Same edges intersected by scanline i likely also intersect scanline i + 1 / - Due to coherence, intersections can be calculated incrementally / - For each increase of y → y + 1. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Edge Rasterization 1/3' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Edge Rasterization 1/3'?

### Page 30 - Edge Rasterization 2/3

Source cue: - Integer arithmetic can be used for (left) edges with slopes > 1 / - Consider dxdy = (xmax − xmin)/(ymax − ymin) / - x is only changed by dxdy / ⇒ x can be represented as a fraction with denominator (ymax − ymin) / - Let a be the integer part

Professor-style explanation: The slide 'Edge Rasterization 2/3' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Integer arithmetic can be used for (left) edges with slopes > 1 / - Consider dxdy = (xmax − xmin)/(ymax − ymin) / - x is only changed by dxdy / ⇒ x can be represented as a fraction with denominator (ymax − ymin) / - Let a be the integer part. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Edge Rasterization 2/3. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Integer arithmetic can be used for (left) edges with slopes > 1 / - Consider dxdy = (xmax − xmin)/(ymax − ymin) / - x is only changed by dxdy / ⇒ x can be represented as a fraction with denominator (ymax − ymin) / - Let a be the integer part. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Edge Rasterization 2/3' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Edge Rasterization 2/3'?

### Page 31 - Edge Rasterization 3/3

Source cue: void leftEdgeScan(int x0, int y0, int x1, int y1) { // slope > 1 / int d = y1 - y0; // denominator (Nenner) / int n = x1 - x0; // numerator (Zähler) / int a = x0; // integer part of x / int b = d; // fraction part of x plus d

Professor-style explanation: The slide 'Edge Rasterization 3/3' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: void leftEdgeScan(int x0, int y0, int x1, int y1) { // slope > 1 / int d = y1 - y0; // denominator (Nenner) / int n = x1 - x0; // numerator (Zähler) / int a = x0; // integer part of x / int b = d; // fraction part of x plus d. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Edge Rasterization 3/3. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: void leftEdgeScan(int x0, int y0, int x1, int y1) { // slope > 1 / int d = y1 - y0; // denominator (Nenner) / int n = x1 - x0; // numerator (Zähler) / int a = x0; // integer part of x / int b = d; // fraction part of x plus d. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Edge Rasterization 3/3' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Edge Rasterization 3/3'?

### Page 32 - 6.3 Region Filling

Source cue: Homogeneous coloring of regions

Professor-style explanation: The slide '6.3 Region Filling' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: Homogeneous coloring of regions. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about 6.3 Region Filling. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: Homogeneous coloring of regions. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for '6.3 Region Filling' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by '6.3 Region Filling'?

### Page 33 - Region Types 1/2

Source cue: - 4-connected / - All pixels of region can be reached by following movements / - Left, right, bottom, top / - 8-connected / - All pixels of region can be reached by following movements

Professor-style explanation: The slide 'Region Types 1/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - 4-connected / - All pixels of region can be reached by following movements / - Left, right, bottom, top / - 8-connected / - All pixels of region can be reached by following movements. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Region Types 1/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - 4-connected / - All pixels of region can be reached by following movements / - Left, right, bottom, top / - 8-connected / - All pixels of region can be reached by following movements. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Region Types 1/2' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Region Types 1/2' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Region Types 1/2' into a causal sentence instead of repeating the slide title?

### Page 34 - Region Types 2/2

Source cue: - Examples / 4-connected 8-connected 8-connected

Professor-style explanation: The slide 'Region Types 2/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Examples / 4-connected 8-connected 8-connected. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Region Types 2/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Examples / 4-connected 8-connected 8-connected. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Region Types 2/2' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Region Types 2/2' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Region Types 2/2' into a causal sentence instead of repeating the slide title?

### Page 35 - Region Spezification

Source cue: - Color-based / - Starting at pixel P, determine largest contiguous region / which pixels have a specific color / - Color assignment done by flood fill algorithms / - Border-based

Professor-style explanation: The slide 'Region Spezification' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Color-based / - Starting at pixel P, determine largest contiguous region / which pixels have a specific color / - Color assignment done by flood fill algorithms / - Border-based. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Region Spezification. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Color-based / - Starting at pixel P, determine largest contiguous region / which pixels have a specific color / - Color assignment done by flood fill algorithms / - Border-based. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Region Spezification' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Region Spezification' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Region Spezification' into a causal sentence instead of repeating the slide title?

### Page 36 - Flood Fill Algorithm

Source cue: void floodFill4(int x, int y, Color oldC, Color newC) { / if ((x < 0) || (x >= width)) return; // Return if x is out of bounds / if ((y < 0) || (y >= height)) return; // Return if y is out of bounds / if (oldC == readPixel(x, y)) { // Check if the current color matches oldC / writePixel(x, y, newC); // Change the color of the pixel

Professor-style explanation: The slide 'Flood Fill Algorithm' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: void floodFill4(int x, int y, Color oldC, Color newC) { / if ((x < 0) || (x >= width)) return; // Return if x is out of bounds / if ((y < 0) || (y >= height)) return; // Return if y is out of bounds / if (oldC == readPixel(x, y)) { // Check if the current color matches oldC / writePixel(x, y, newC); // Change the color of the pixel. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Flood Fill Algorithm. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: void floodFill4(int x, int y, Color oldC, Color newC) { / if ((x < 0) || (x >= width)) return; // Return if x is out of bounds / if ((y < 0) || (y >= height)) return; // Return if y is out of bounds / if (oldC == readPixel(x, y)) { // Check if the current color matches oldC / writePixel(x, y, newC); // Change the color of the pixel. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Flood Fill Algorithm' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Flood Fill Algorithm' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Flood Fill Algorithm' into a causal sentence instead of repeating the slide title?

### Page 37 - Boundary Fill Algorithm

Source cue: void boundaryFill4(int x, int y, Color oldC, Color newC) { / if ((x < 0) || (x >= width)) return; // Return if x is out of bounds / if ((y < 0) || (y >= height)) return; // Return if y is out of bounds / Color c = readPixel(x, y); / if (c == oldC) return; // Return if pixel is a boundary pixel

Professor-style explanation: The slide 'Boundary Fill Algorithm' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: void boundaryFill4(int x, int y, Color oldC, Color newC) { / if ((x < 0) || (x >= width)) return; // Return if x is out of bounds / if ((y < 0) || (y >= height)) return; // Return if y is out of bounds / Color c = readPixel(x, y); / if (c == oldC) return; // Return if pixel is a boundary pixel. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Boundary Fill Algorithm. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: void boundaryFill4(int x, int y, Color oldC, Color newC) { / if ((x < 0) || (x >= width)) return; // Return if x is out of bounds / if ((y < 0) || (y >= height)) return; // Return if y is out of bounds / Color c = readPixel(x, y); / if (c == oldC) return; // Return if pixel is a boundary pixel. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Boundary Fill Algorithm' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Boundary Fill Algorithm' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Boundary Fill Algorithm' into a causal sentence instead of repeating the slide title?

### Page 38 - Fill Algorithms

Source cue: - High number of recursions can lead to stack overflow / - Use smarter data structures, i.e., queues and stacks / Queue Stack

Professor-style explanation: The slide 'Fill Algorithms' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - High number of recursions can lead to stack overflow / - Use smarter data structures, i.e., queues and stacks / Queue Stack. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Fill Algorithms. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - High number of recursions can lead to stack overflow / - Use smarter data structures, i.e., queues and stacks / Queue Stack. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Fill Algorithms' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Fill Algorithms' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Fill Algorithms' into a causal sentence instead of repeating the slide title?

### Page 39 - 6.4 Scanline-Based Triangle Rasterization

Source cue: Segment-based rasterization of the simplest type of polygon

Professor-style explanation: The slide '6.4 Scanline-Based Triangle Rasterization' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: Segment-based rasterization of the simplest type of polygon. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about 6.4 Scanline-Based Triangle Rasterization. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: Segment-based rasterization of the simplest type of polygon. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for '6.4 Scanline-Based Triangle Rasterization' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by '6.4 Scanline-Based Triangle Rasterization'?

### Page 40 - Triangle Rasterization

Source cue: - Triangle rasterization / - Rasterize filled triangles is main task in real-time rendering / - Realization through graphics hardware desired / - General polygons split into triangles through tessellation / - Rasterization requires three steps

Professor-style explanation: The slide 'Triangle Rasterization' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Triangle rasterization / - Rasterize filled triangles is main task in real-time rendering / - Realization through graphics hardware desired / - General polygons split into triangles through tessellation / - Rasterization requires three steps. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Triangle Rasterization. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Triangle rasterization / - Rasterize filled triangles is main task in real-time rendering / - Realization through graphics hardware desired / - General polygons split into triangles through tessellation / - Rasterization requires three steps. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Triangle Rasterization' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Triangle Rasterization'?

### Page 41 - Scanline-Based Rasterization

Source cue: - Rasterization through scanline conversion exploits spatial coherence / - Pixels of a scanline are colored similarly / - Adjacent scanlines span similar pixels / - Adjacent scanlines are colored similarly / - Scanline segments can be calculated

Professor-style explanation: The slide 'Scanline-Based Rasterization' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Rasterization through scanline conversion exploits spatial coherence / - Pixels of a scanline are colored similarly / - Adjacent scanlines span similar pixels / - Adjacent scanlines are colored similarly / - Scanline segments can be calculated. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Scanline-Based Rasterization. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Rasterization through scanline conversion exploits spatial coherence / - Pixels of a scanline are colored similarly / - Adjacent scanlines span similar pixels / - Adjacent scanlines are colored similarly / - Scanline segments can be calculated. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Scanline-Based Rasterization' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Scanline-Based Rasterization'?

### Page 42 - Algorithm Overview

Source cue: - Observation: triangle can be split into top an bottom half / - For each half two edge pixels and one segment exist / - Segments differ only slightly, depending on edge slope / - Procedure / - Sort triangle vertices based on y-coordinate

Professor-style explanation: The slide 'Algorithm Overview' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Observation: triangle can be split into top an bottom half / - For each half two edge pixels and one segment exist / - Segments differ only slightly, depending on edge slope / - Procedure / - Sort triangle vertices based on y-coordinate. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Algorithm Overview. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Observation: triangle can be split into top an bottom half / - For each half two edge pixels and one segment exist / - Segments differ only slightly, depending on edge slope / - Procedure / - Sort triangle vertices based on y-coordinate. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Algorithm Overview' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Algorithm Overview' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Algorithm Overview'?

### Page 43 - Slope Calculation

Source cue: - Calculate slope for each triangle edge: 1/A = dx/dy / - Δ = (x − x )/(y − y ) / 02 2 0 2 0 / - Δ = (x − x )/(y − y ) / 01 1 0 1 0

Professor-style explanation: The slide 'Slope Calculation' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Calculate slope for each triangle edge: 1/A = dx/dy / - Δ = (x − x )/(y − y ) / 02 2 0 2 0 / - Δ = (x − x )/(y − y ) / 01 1 0 1 0. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Slope Calculation. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Calculate slope for each triangle edge: 1/A = dx/dy / - Δ = (x − x )/(y − y ) / 02 2 0 2 0 / - Δ = (x − x )/(y − y ) / 01 1 0 1 0. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Slope Calculation' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Slope Calculation'?

### Page 44 - Pseudo Code

Source cue: void processTriangle(int x0, int y0, float delta02, float delta01, int Nbottom, int Ntop) { / float XLeft = x0; // Start position for left x / float XRight = x0; // Start position for right x / int Y = y0; // Start position for y / float DeltaLeft = delta02; // Delta for left x for bottom half

Professor-style explanation: The slide 'Pseudo Code' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: void processTriangle(int x0, int y0, float delta02, float delta01, int Nbottom, int Ntop) { / float XLeft = x0; // Start position for left x / float XRight = x0; // Start position for right x / int Y = y0; // Start position for y / float DeltaLeft = delta02; // Delta for left x for bottom half. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Pseudo Code. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: void processTriangle(int x0, int y0, float delta02, float delta01, int Nbottom, int Ntop) { / float XLeft = x0; // Start position for left x / float XRight = x0; // Start position for right x / int Y = y0; // Start position for y / float DeltaLeft = delta02; // Delta for left x for bottom half. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Pseudo Code' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Pseudo Code'?

### Page 45 - Segment Rasterization

Source cue: - Each segment generates fragments / - Rendering pipeline processes generated fragments / (x , y ) / (e.g., depth testing, alpha blending) right s / (x , y )

Professor-style explanation: The slide 'Segment Rasterization' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. The terms are successive representations in object-based rendering: - Each segment generates fragments / - Rendering pipeline processes generated fragments / (x , y ) / (e.g., depth testing, alpha blending) right s / (x , y ). Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter. For examination purposes, the important content is the representation change at each stage: model data, vertices, primitives, fragments, fragment tests, and final framebuffer updates.

Technical commentary: This slide is about Segment Rasterization. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. The terms are successive representations in object-based rendering: - Each segment generates fragments / - Rendering pipeline processes generated fragments / (x , y ) / (e.g., depth testing, alpha blending) right s / (x , y ). Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels.

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Exam-grade answer: A strong answer for 'Segment Rasterization' states what representation enters the stage, what representation leaves it, and which later stage depends on that output.

Common trap: Do not collapse 'Segment Rasterization' into 'the GPU draws it'; name the intermediate representations because that is where most errors and exam distinctions appear.

Check yourself: Can you name the input and output representation for 'Segment Rasterization' in the rendering pipeline?

### Page 46 - Vertex Attribute Interpolation

Source cue: - During rasterization vertex attributes (e.g., color, depth) / must be interpolated over triangle / (x , y , z ) / right s right / - Bilinear interpolation can be used

Professor-style explanation: The slide 'Vertex Attribute Interpolation' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - During rasterization vertex attributes (e.g., color, depth) / must be interpolated over triangle / (x , y , z ) / right s right / - Bilinear interpolation can be used. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Vertex Attribute Interpolation. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - During rasterization vertex attributes (e.g., color, depth) / must be interpolated over triangle / (x , y , z ) / right s right / - Bilinear interpolation can be used. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Vertex Attribute Interpolation' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Vertex Attribute Interpolation'?

### Page 47 - Incremental Interpolation 1/3

Source cue: - Spatial coherence allows for an incremental attribute interpolation / - Example: consider triangle's plane equation for calculating z increments / - Ax + By + Cz + D = 0 / - With plane coefficients A, B, C: A, B, C = V − V × (V − V ) / 2 0 1 2

Professor-style explanation: The slide 'Incremental Interpolation 1/3' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Spatial coherence allows for an incremental attribute interpolation / - Example: consider triangle's plane equation for calculating z increments / - Ax + By + Cz + D = 0 / - With plane coefficients A, B, C: A, B, C = V − V × (V − V ) / 2 0 1 2. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Incremental Interpolation 1/3. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Spatial coherence allows for an incremental attribute interpolation / - Example: consider triangle's plane equation for calculating z increments / - Ax + By + Cz + D = 0 / - With plane coefficients A, B, C: A, B, C = V − V × (V − V ) / 2 0 1 2. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Incremental Interpolation 1/3' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Incremental Interpolation 1/3'?

### Page 48 - Incremental Interpolation 2/3

Source cue: - Increments dzdx and dzdy are used to incrementally modify given z value, / i.e., when moving from (x, y) to (x + 1, y) or (x, y + 1) / - Case 1: next fragment in scanline (horizontal change by +1) / - x → x ⇒ z ≔ z + dzdx / i i+1 i

Professor-style explanation: The slide 'Incremental Interpolation 2/3' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Increments dzdx and dzdy are used to incrementally modify given z value, / i.e., when moving from (x, y) to (x + 1, y) or (x, y + 1) / - Case 1: next fragment in scanline (horizontal change by +1) / - x → x ⇒ z ≔ z + dzdx / i i+1 i. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Incremental Interpolation 2/3. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Increments dzdx and dzdy are used to incrementally modify given z value, / i.e., when moving from (x, y) to (x + 1, y) or (x, y + 1) / - Case 1: next fragment in scanline (horizontal change by +1) / - x → x ⇒ z ≔ z + dzdx / i i+1 i. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Incremental Interpolation 2/3' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Incremental Interpolation 2/3'?

### Page 49 - Incremental Interpolation 3/3

Source cue: - All vertex attributes can be interpolated incrementally analogous to depth / - Colors (r, g, b, a) / - Texture coordinates (u, v) / - ... / - For each attribute θ define

Professor-style explanation: The slide 'Incremental Interpolation 3/3' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - All vertex attributes can be interpolated incrementally analogous to depth / - Colors (r, g, b, a) / - Texture coordinates (u, v) / - ... / - For each attribute θ define. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Incremental Interpolation 3/3. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - All vertex attributes can be interpolated incrementally analogous to depth / - Colors (r, g, b, a) / - Texture coordinates (u, v) / - ... / - For each attribute θ define. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Incremental Interpolation 3/3' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Incremental Interpolation 3/3' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Incremental Interpolation 3/3'?

### Page 50 - 6.5 Tile-Based Triangle Rasterization

Source cue: Parallel tile-based triangle rasterization

Professor-style explanation: The slide '6.5 Tile-Based Triangle Rasterization' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: Parallel tile-based triangle rasterization. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about 6.5 Tile-Based Triangle Rasterization. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: Parallel tile-based triangle rasterization. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for '6.5 Tile-Based Triangle Rasterization' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by '6.5 Tile-Based Triangle Rasterization'?

### Page 51 - Tile-Based Triangle Rasterization

Source cue: - Modern GPUs have a block-wise structure, / where one processor is responsible for one screen tile of adjacent pixels / - Segment-based triangled rasterization is difficult to parallelize / - Tile-based rasterization is a better fit with modern GPUs / - Advantage

Professor-style explanation: The slide 'Tile-Based Triangle Rasterization' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Modern GPUs have a block-wise structure, / where one processor is responsible for one screen tile of adjacent pixels / - Segment-based triangled rasterization is difficult to parallelize / - Tile-based rasterization is a better fit with modern GPUs / - Advantage. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Tile-Based Triangle Rasterization. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Modern GPUs have a block-wise structure, / where one processor is responsible for one screen tile of adjacent pixels / - Segment-based triangled rasterization is difficult to parallelize / - Tile-based rasterization is a better fit with modern GPUs / - Advantage. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Tile-Based Triangle Rasterization' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Tile-Based Triangle Rasterization'?

### Page 52 - Edge-Based Triangle Representation 1/2

Source cue: - Edge-based area representation is possible through implicit edge functions / - Implicit edge function can be defined based on two edge vertices / V = (x , y ) and V = (x , y ) / 0 0 0 1 1 1 / - For a given coordinate (x, y), the implicit edge function is defined as

Professor-style explanation: The slide 'Edge-Based Triangle Representation 1/2' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Edge-based area representation is possible through implicit edge functions / - Implicit edge function can be defined based on two edge vertices / V = (x , y ) and V = (x , y ) / 0 0 0 1 1 1 / - For a given coordinate (x, y), the implicit edge function is defined as. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Edge-Based Triangle Representation 1/2. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Edge-based area representation is possible through implicit edge functions / - Implicit edge function can be defined based on two edge vertices / V = (x , y ) and V = (x , y ) / 0 0 0 1 1 1 / - For a given coordinate (x, y), the implicit edge function is defined as. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Edge-Based Triangle Representation 1/2' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Edge-Based Triangle Representation 1/2' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Edge-Based Triangle Representation 1/2'?

### Page 53 - Edge-Based Triangle Representation 2/2

Source cue: - To represent a triangle, three implicit edge functions are combined / - E x, y = y − y ⋅ x − x − x ⋅ y + B ⋅ x − x / 01 1 0 1 0 01 1 0 / - E x, y = y − y ⋅ x − x − x ⋅ y + B ⋅ x − x / 12 2 1 2 1 12 2 1

Professor-style explanation: The slide 'Edge-Based Triangle Representation 2/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - To represent a triangle, three implicit edge functions are combined / - E x, y = y − y ⋅ x − x − x ⋅ y + B ⋅ x − x / 01 1 0 1 0 01 1 0 / - E x, y = y − y ⋅ x − x − x ⋅ y + B ⋅ x − x / 12 2 1 2 1 12 2 1. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Edge-Based Triangle Representation 2/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - To represent a triangle, three implicit edge functions are combined / - E x, y = y − y ⋅ x − x − x ⋅ y + B ⋅ x − x / 01 1 0 1 0 01 1 0 / - E x, y = y − y ⋅ x − x − x ⋅ y + B ⋅ x − x / 12 2 1 2 1 12 2 1. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Edge-Based Triangle Representation 2/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Edge-Based Triangle Representation 2/2'?

### Page 54 - Rasterization Procedure

Source cue: 1. Determine tiles which are (partially) covering triangle / (e.g., easiest approximation would be bounding box) / 2. For each covering tile / - For each pixel / - If all implicit edge functions evaluate to < 0 2

Professor-style explanation: The slide 'Rasterization Procedure' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: 1. Determine tiles which are (partially) covering triangle / (e.g., easiest approximation would be bounding box) / 2. For each covering tile / - For each pixel / - If all implicit edge functions evaluate to < 0 2. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Rasterization Procedure. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: 1. Determine tiles which are (partially) covering triangle / (e.g., easiest approximation would be bounding box) / 2. For each covering tile / - For each pixel / - If all implicit edge functions evaluate to < 0 2. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Rasterization Procedure' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Rasterization Procedure'?

### Page 55 - between adjacent triangles

Source cue: - Pixel-based displays require the rasterization of primitives / - Rasterization fidelity is critical for image quality / - Rasterization is time-critical and should be optimized for hardware / - Focus on triangles due to speed and ease of tessellation of other polygons / - Segment-based triangle rasterization avoids overlap

Professor-style explanation: The slide 'between adjacent triangles' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Pixel-based displays require the rasterization of primitives / - Rasterization fidelity is critical for image quality / - Rasterization is time-critical and should be optimized for hardware / - Focus on triangles due to speed and ease of tessellation of other polygons / - Segment-based triangle rasterization avoids overlap. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about between adjacent triangles. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Pixel-based displays require the rasterization of primitives / - Rasterization fidelity is critical for image quality / - Rasterization is time-critical and should be optimized for hardware / - Focus on triangles due to speed and ease of tessellation of other polygons / - Segment-based triangle rasterization avoids overlap. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'between adjacent triangles' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'between adjacent triangles'?

### Page 56 - Literature and other sources used in this chapter

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Literature and other sources used in this chapter' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Literature and other sources used in this chapter. The slide lists source material or chapter references that support the technical content and give names for further reading. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Reference slides provide the source trail for definitions, algorithms, and deeper explanations.

Exam-grade answer: A strong answer for 'Literature and other sources used in this chapter' identifies what kind of source is listed and which course concept or algorithm that source supports.

Common trap: Do not skip 'Literature and other sources used in this chapter' if it names a standard algorithm or source that defines terminology used later in the chapter.

Check yourself: Can you identify which source or topic 'Literature and other sources used in this chapter' points to for deeper study?

### Page 57 - Practice, Addison-Wesley.

Source cue: - Text Books / - Foley J., van Dam, A., Feiner, S. (2013). Computer Graphics: Principles and / Practice, Addison-Wesley. / - Research Publications / - Bresenham, J. E. (1998). Algorithm for computer control of a digital plotter.

Professor-style explanation: The slide 'Practice, Addison-Wesley.' collects the source material behind the chapter. References are not rendering objects themselves, but they identify the books, papers, or external resources from which the lecture's terminology and algorithms are drawn. The listed sources support the chapter content: - Text Books / - Foley J., van Dam, A., Feiner, S. (2013). Computer Graphics: Principles and / Practice, Addison-Wesley. / - Research Publications / - Bresenham, J. E. (1998). Algorithm for computer control of a digital plotter. They point to the books, papers, or resources behind the definitions and algorithms used in the lecture. In practical terms, a reference slide marks the boundary of the chapter and tells us where the formal definitions, derivations, or extended examples can be found if a topic needs more depth than the lecture slides provide. For examination purposes, the important content is source attribution and vocabulary: references tell where precise definitions and standard algorithms come from.

Technical commentary: This slide is about Practice, Addison-Wesley.. The slide lists source material or chapter references that support the technical content and give names for further reading. The listed sources support the chapter content: - Text Books / - Foley J., van Dam, A., Feiner, S. (2013). Computer Graphics: Principles and / Practice, Addison-Wesley. / - Research Publications / - Bresenham, J. E. (1998). Algorithm for computer control of a digital plotter. They point to the books, papers, or resources behind the definitions and algorithms used in the lecture.

Why it matters: Reference slides provide the source trail for definitions, algorithms, and deeper explanations.

Exam-grade answer: A strong answer for 'Practice, Addison-Wesley.' identifies what kind of source is listed and which course concept or algorithm that source supports.

Common trap: Do not skip 'Practice, Addison-Wesley.' if it names a standard algorithm or source that defines terminology used later in the chapter.

Check yourself: Can you identify which source or topic 'Practice, Addison-Wesley.' points to for deeper study?

### Page 58 - Slide for Future: Sustainability in CG (@ EG25)

Source cue: also @ IEEE VR

Professor-style explanation: The slide 'Slide for Future: Sustainability in CG (@ EG25)' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: also @ IEEE VR. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Slide for Future: Sustainability in CG (@ EG25). The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: also @ IEEE VR. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Slide for Future: Sustainability in CG (@ EG25)' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Slide for Future: Sustainability in CG (@ EG25)' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Slide for Future: Sustainability in CG (@ EG25)' into a causal sentence instead of repeating the slide title?

### Page 59 - Slide for Future: Sustainability in CG (@ EG25)

Source cue: Unoptimized Optimized Unoptimized Optimized / Inverse Simulation of Radiative Thermal Transport / Christian Freude, Lukas Lipp, Matthias Zezulka, Florian Rist, Michael Wimmer, David Hahn

Professor-style explanation: The slide 'Slide for Future: Sustainability in CG (@ EG25)' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: Unoptimized Optimized Unoptimized Optimized / Inverse Simulation of Radiative Thermal Transport / Christian Freude, Lukas Lipp, Matthias Zezulka, Florian Rist, Michael Wimmer, David Hahn. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Slide for Future: Sustainability in CG (@ EG25). The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: Unoptimized Optimized Unoptimized Optimized / Inverse Simulation of Radiative Thermal Transport / Christian Freude, Lukas Lipp, Matthias Zezulka, Florian Rist, Michael Wimmer, David Hahn. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Slide for Future: Sustainability in CG (@ EG25)' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Slide for Future: Sustainability in CG (@ EG25)' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Slide for Future: Sustainability in CG (@ EG25)' into a causal sentence instead of repeating the slide title?

### Page 60 - Slide for Future: Sustainability in CG (@ EG25)

Source cue: Optimizing Free-Form Grid Shells with Reclaimed Elements under Inventory Constraints / Andrea Favilli, Francesco Laccone, Paolo Cignoni, Luigi Malomo, Daniela Giorgi

Professor-style explanation: The slide 'Slide for Future: Sustainability in CG (@ EG25)' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: Optimizing Free-Form Grid Shells with Reclaimed Elements under Inventory Constraints / Andrea Favilli, Francesco Laccone, Paolo Cignoni, Luigi Malomo, Daniela Giorgi. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Slide for Future: Sustainability in CG (@ EG25). The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: Optimizing Free-Form Grid Shells with Reclaimed Elements under Inventory Constraints / Andrea Favilli, Francesco Laccone, Paolo Cignoni, Luigi Malomo, Daniela Giorgi. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Slide for Future: Sustainability in CG (@ EG25)' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Slide for Future: Sustainability in CG (@ EG25)' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Slide for Future: Sustainability in CG (@ EG25)' into a causal sentence instead of repeating the slide title?

### Page 61 - Slide for Future: Sustainability in CG (@ EG25)

Source cue: Stress-Aligned Hexahedral Lattice Structures / Dennis Bukenberger, Junpeng Wang, Jun Wu, Rüdiger Westermann

Professor-style explanation: The slide 'Slide for Future: Sustainability in CG (@ EG25)' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: Stress-Aligned Hexahedral Lattice Structures / Dennis Bukenberger, Junpeng Wang, Jun Wu, Rüdiger Westermann. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Slide for Future: Sustainability in CG (@ EG25). The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: Stress-Aligned Hexahedral Lattice Structures / Dennis Bukenberger, Junpeng Wang, Jun Wu, Rüdiger Westermann. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Slide for Future: Sustainability in CG (@ EG25)' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Slide for Future: Sustainability in CG (@ EG25)' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Slide for Future: Sustainability in CG (@ EG25)' into a causal sentence instead of repeating the slide title?

## 06.1 Line Rasterization

Source location: Section 6.1

### Commentary

A mathematical line has infinitely many points, but a raster display has a finite grid. Line rasterization decides which grid cells or samples best approximate the ideal line. The algorithm must balance accuracy, speed, and consistency.

Incremental algorithms avoid recomputing expensive formulas for every pixel. The important idea is to step along one axis and update an error term that decides when to step along the other axis.

### Mental Model

Rasterizing a line means approximating a continuous path by grid decisions.

### Check Yourself

Why are incremental error updates useful in line rasterization?

## 06.2 Triangle Edge Rasterization

Source location: Section 6.2

### Commentary

Triangles are the core primitive in real-time rendering. Edge functions or half-space tests decide whether a sample lies inside the triangle. This allows the rasterizer to test coverage systematically.

Coverage is not final visibility. A covered sample becomes a fragment candidate. Depth testing, stencil testing, blending, and other operations still decide whether the framebuffer changes.

### Mental Model

Triangle rasterization answers the question: which samples are inside this projected triangle?

### Check Yourself

What later stage can reject a fragment after triangle coverage succeeds?

## 06.3 Region Filling

Source location: Section 6.3

### Commentary

Region filling generalizes the idea of determining interior samples. The algorithm must identify connected areas or spans that should receive color. This connects rasterization to scan conversion and image-space reasoning.

The practical issue is avoiding gaps, double fills, or inconsistent boundary handling. Small choices at edges can become visible artifacts when many primitives meet.

### Mental Model

Filling is about turning boundary descriptions into consistent interior samples.

### Check Yourself

Why can inconsistent edge rules create cracks between adjacent primitives?

## 06.4 Scanline-Based Triangle Rasterization

Source location: Section 6.4

### Commentary

Scanline rasterization processes horizontal rows of the image. For each row that crosses a triangle, the algorithm finds the covered interval and fills the span. Attribute interpolation can be updated along edges and across each span.

The method is intuitive because it follows the memory layout of many images. It also demonstrates why interpolation is tied to rasterization: once you know a sample location inside the primitive, you can interpolate depth, color, normals, or texture coordinates.

### Mental Model

Each scanline asks: where does this triangle enter and leave this row?

### Check Yourself

Which attributes might be interpolated while filling triangle spans?

## 06.5 Tile-Based Triangle Rasterization

Source location: Section 6.5

### Commentary

Tile- or block-based approaches group pixels into small regions. This can improve locality and parallel work distribution. Modern GPUs often reason in blocks or tiles internally because rendering is massively parallel.

For the exam, connect this to efficiency. The mathematical goal is still coverage, but the implementation is organized to use hardware resources well.

### Mental Model

Block-based rasterization keeps the same coverage problem but changes the work organization.

### Check Yourself

Why is block organization attractive for parallel graphics hardware?

## End-of-Lecture Summary

If you remember only one thing from Lecture 06, remember this: This lecture explains how continuous primitives become discrete fragments on a grid. Rasterization is the bridge from geometric descriptions to sample-based image generation.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
