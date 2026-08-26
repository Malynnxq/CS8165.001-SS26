# Lecture 02 - Rendering Pipeline

Source chunk: `course_text_parts/03_lectures/02_rendering-pipeline.txt`
Extracted slide pages in source chunk: 94

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture turns the vague idea of rendering into a concrete sequence. It is the most important debugging map in the course: if an image is wrong, the pipeline tells you where the error could have entered.

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

### Page 2 - Object-based Rendering

Source cue: - Image generation done through rasterization / - Scene objects formed by 3D models (primitives) / are transformed through successive coordinate systems / - Primitives are rasterized into fragments, which are pixel predecessors / - A subset of the fragments becomes pixels

Professor-style explanation: The slide 'Object-based Rendering' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. The terms are successive representations in object-based rendering: - Image generation done through rasterization / - Scene objects formed by 3D models (primitives) / are transformed through successive coordinate systems / - Primitives are rasterized into fragments, which are pixel predecessors / - A subset of the fragments becomes pixels. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter. For examination purposes, the important content is the representation change at each stage: model data, vertices, primitives, fragments, fragment tests, and final framebuffer updates.

Technical commentary: This slide is about Object-based Rendering. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. The terms are successive representations in object-based rendering: - Image generation done through rasterization / - Scene objects formed by 3D models (primitives) / are transformed through successive coordinate systems / - Primitives are rasterized into fragments, which are pixel predecessors / - A subset of the fragments becomes pixels. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels.

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Exam-grade answer: A strong answer for 'Object-based Rendering' states what representation enters the stage, what representation leaves it, and which later stage depends on that output.

Common trap: Do not collapse 'Object-based Rendering' into 'the GPU draws it'; name the intermediate representations because that is where most errors and exam distinctions appear.

Check yourself: Can you name the input and output representation for 'Object-based Rendering' in the rendering pipeline?

### Page 3 - 2.1 Rendering Process

Source cue: 2.2 OpenGL Overview / 2.3 OpenGL Rendering / 2.4 OpenGL Rendering Pipeline / 2.5 Fragment Tests and Operations / 2.6 Framebuffer

Professor-style explanation: The outline '2.1 Rendering Process' gives the lecture its internal logic. The listed topics are the objects that will be connected during the chapter: first the problem space, then the mathematical or algorithmic tools, then the implementation consequences. The listed entries form a dependency order: 2.2 OpenGL Overview / 2.3 OpenGL Rendering / 2.4 OpenGL Rendering Pipeline / 2.5 Fragment Tests and Operations / 2.6 Framebuffer. Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary. The order matters because later items rely on earlier definitions. For example, an OpenGL mechanism is much easier to understand once the corresponding pipeline object or mathematical operation has already been introduced. The outline is therefore a compact dependency graph of the lecture rather than a collection of isolated labels. For examination purposes, the important content is the dependency structure: which concept introduces the vocabulary, which later algorithm uses it, and which implementation problem it solves.

Technical commentary: This slide is about 2.1 Rendering Process. The listed items define the lecture sequence: the topic begins with a problem statement, introduces the required objects or algorithms, and then connects them to rendering or implementation consequences. The listed entries form a dependency order: 2.2 OpenGL Overview / 2.3 OpenGL Rendering / 2.4 OpenGL Rendering Pipeline / 2.5 Fragment Tests and Operations / 2.6 Framebuffer. Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary.

Why it matters: Outlines tell you the dependency order. They are the safest way to avoid learning isolated bullet points.

Exam-grade answer: A strong answer for '2.1 Rendering Process' names the topics in order and explains at least one dependency between an earlier item and a later item.

Common trap: Do not memorize '2.1 Rendering Process' as a list of headings only; the exam-relevant part is how the headings depend on each other.

Check yourself: Can you explain where '2.1 Rendering Process' fits in the lecture order and what later section depends on it?

### Page 4 - 2.1 Rendering Process

Source cue: From 3D models over fragments to pixels

Professor-style explanation: The slide '2.1 Rendering Process' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. The terms are successive representations in object-based rendering: From 3D models over fragments to pixels. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter. For examination purposes, the important content is the representation change at each stage: model data, vertices, primitives, fragments, fragment tests, and final framebuffer updates.

Technical commentary: This slide is about 2.1 Rendering Process. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. The terms are successive representations in object-based rendering: From 3D models over fragments to pixels. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels.

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Exam-grade answer: A strong answer for '2.1 Rendering Process' states what representation enters the stage, what representation leaves it, and which later stage depends on that output.

Common trap: Do not collapse '2.1 Rendering Process' into 'the GPU draws it'; name the intermediate representations because that is where most errors and exam distinctions appear.

Check yourself: Can you name the input and output representation for '2.1 Rendering Process' in the rendering pipeline?

### Page 5 - Geometry-based Rendering 1/2

Source cue: CPU Application GPU Rendering Display Hardware / Rendering / 3D Model Framebuffer / Process / Video

Professor-style explanation: The slide 'Geometry-based Rendering 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: CPU Application GPU Rendering Display Hardware / Rendering / 3D Model Framebuffer / Process / Video. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Geometry-based Rendering 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: CPU Application GPU Rendering Display Hardware / Rendering / 3D Model Framebuffer / Process / Video. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Geometry-based Rendering 1/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Geometry-based Rendering 1/2'?

### Page 6 - Geometry-based Rendering 2/2

Source cue: - The rendering process is realized through the rendering pipeline / - Renders 3D models to 2D images / - Conceptually, the rendering pipeline consists of two GPU stages / - Geometry stage - processes geometric primitives / - Rasterization stage - processes fragments and pixels

Professor-style explanation: The slide 'Geometry-based Rendering 2/2' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. The terms are successive representations in object-based rendering: - The rendering process is realized through the rendering pipeline / - Renders 3D models to 2D images / - Conceptually, the rendering pipeline consists of two GPU stages / - Geometry stage - processes geometric primitives / - Rasterization stage - processes fragments and pixels. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter. For examination purposes, the important content is the representation change at each stage: model data, vertices, primitives, fragments, fragment tests, and final framebuffer updates.

Technical commentary: This slide is about Geometry-based Rendering 2/2. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. The terms are successive representations in object-based rendering: - The rendering process is realized through the rendering pipeline / - Renders 3D models to 2D images / - Conceptually, the rendering pipeline consists of two GPU stages / - Geometry stage - processes geometric primitives / - Rasterization stage - processes fragments and pixels. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels.

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Exam-grade answer: A strong answer for 'Geometry-based Rendering 2/2' states what representation enters the stage, what representation leaves it, and which later stage depends on that output.

Common trap: Do not collapse 'Geometry-based Rendering 2/2' into 'the GPU draws it'; name the intermediate representations because that is where most errors and exam distinctions appear.

Check yourself: Can you name the input and output representation for 'Geometry-based Rendering 2/2' in the rendering pipeline?

### Page 7 - Application Stage

Source cue: - Specification of the model elements and the scene / as well as interaction capabilities / - Scene modeling: arrangement and attribution of the scene objects / - Calculation of animation paths / - Collision detection

Professor-style explanation: The slide 'Application Stage' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. The terms are successive representations in object-based rendering: - Specification of the model elements and the scene / as well as interaction capabilities / - Scene modeling: arrangement and attribution of the scene objects / - Calculation of animation paths / - Collision detection. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter. For examination purposes, the important content is the representation change at each stage: model data, vertices, primitives, fragments, fragment tests, and final framebuffer updates.

Technical commentary: This slide is about Application Stage. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. The terms are successive representations in object-based rendering: - Specification of the model elements and the scene / as well as interaction capabilities / - Scene modeling: arrangement and attribution of the scene objects / - Calculation of animation paths / - Collision detection. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels.

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Exam-grade answer: A strong answer for 'Application Stage' states what representation enters the stage, what representation leaves it, and which later stage depends on that output.

Common trap: Do not collapse 'Application Stage' into 'the GPU draws it'; name the intermediate representations because that is where most errors and exam distinctions appear.

Check yourself: Can you name the input and output representation for 'Application Stage' in the rendering pipeline?

### Page 8 - Geometry Stage

Source cue: x x / - Geometric 3D transformation / Model Coordinate System World Coordinate System / - Alignment of individual scene objects in the overall scene / - Basic transformations: translation, scaling, rotation

Professor-style explanation: The slide 'Geometry Stage' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: x x / - Geometric 3D transformation / Model Coordinate System World Coordinate System / - Alignment of individual scene objects in the overall scene / - Basic transformations: translation, scaling, rotation. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Geometry Stage. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: x x / - Geometric 3D transformation / Model Coordinate System World Coordinate System / - Alignment of individual scene objects in the overall scene / - Basic transformations: translation, scaling, rotation. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Geometry Stage' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Geometry Stage' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Geometry Stage'?

### Page 9 - Rasterization Stage

Source cue: - Conversion of primitives into fragments (rasterization) / - Discretization takes place in relation to a target grid / - Rasterization algorithms optimized for certain primitives / (e.g., lines, triangles) / - After rasterization per-fragment tests are performed

Professor-style explanation: The slide 'Rasterization Stage' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Conversion of primitives into fragments (rasterization) / - Discretization takes place in relation to a target grid / - Rasterization algorithms optimized for certain primitives / (e.g., lines, triangles) / - After rasterization per-fragment tests are performed. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Rasterization Stage. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Conversion of primitives into fragments (rasterization) / - Discretization takes place in relation to a target grid / - Rasterization algorithms optimized for certain primitives / (e.g., lines, triangles) / - After rasterization per-fragment tests are performed. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Rasterization Stage' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Rasterization Stage'?

### Page 10 - 2.2 OpenGL Overview

Source cue: Library for real-time computer graphics

Professor-style explanation: The slide '2.2 OpenGL Overview' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: Library for real-time computer graphics. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about 2.2 OpenGL Overview. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: Library for real-time computer graphics. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for '2.2 OpenGL Overview' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2.2 OpenGL Overview'?

### Page 11 - OpenGL History

Source cue: - Unified graphics software interface was missing / as knowledge channeled into proprietary software packages / - HP's starbase / - SGI's Graphics Library (GL) / - Some standardization efforts existed

Professor-style explanation: The slide 'OpenGL History' explains the historical background behind the graphics concept. Computer graphics did not appear as one finished pipeline; it developed from older ideas such as artistic perspective, color representation, display hardware, interactive systems, and increasingly programmable rendering algorithms. The historical objects on the slide are people, systems, dates, or milestones, and each milestone marks a capability that later became normal in graphics software. The names, dates, and examples form a timeline: - Unified graphics software interface was missing / as knowledge channeled into proprietary software packages / - HP's starbase / - SGI's Graphics Library (GL) / - Some standardization efforts existed. Each item marks a capability or use case that pushed graphics from static image construction toward interactive, programmable rendering. This history matters because it shows why the course combines mathematics, image representation, hardware acceleration, and interaction. Modern real-time rendering is the result of these threads converging into a pipeline that can generate images fast enough for user input. For examination purposes, the important content is not the date alone but the reason the milestone matters: every historical item solved a limitation in representation, interaction, display, or computation.

Technical commentary: This slide is about OpenGL History. The slide places the technical topic into the historical development of computer graphics, showing how artistic perspective, display technology, interaction, and rendering algorithms evolved together. The names, dates, and examples form a timeline: - Unified graphics software interface was missing / as knowledge channeled into proprietary software packages / - HP's starbase / - SGI's Graphics Library (GL) / - Some standardization efforts existed. Each item marks a capability or use case that pushed graphics from static image construction toward interactive, programmable rendering.

Why it matters: Historical slides explain why the current pipeline exists and which older problems led to modern graphics concepts.

Exam-grade answer: A strong answer for 'OpenGL History' states the milestone and the graphics limitation it helped overcome, such as limited interaction, limited displays, missing 3D representation, or slow rendering.

Common trap: Do not learn 'OpenGL History' as trivia only; connect each historical item to the technical capability it introduced or made practical.

Check yourself: Can you name the graphics capability or idea represented by 'OpenGL History' and why it mattered historically?

### Page 12 - OpenGL

Source cue: - OpenGL (Open Graphics Library) / - Platform independent 2D and 3D graphics API / - API specification is provided by the Khronos Group / - Technical implementation / - Rendering pipeline consisting of static and programmable pipeline stages

Professor-style explanation: The slide 'OpenGL' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - OpenGL (Open Graphics Library) / - Platform independent 2D and 3D graphics API / - API specification is provided by the Khronos Group / - Technical implementation / - Rendering pipeline consisting of static and programmable pipeline stages. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - OpenGL (Open Graphics Library) / - Platform independent 2D and 3D graphics API / - API specification is provided by the Khronos Group / - Technical implementation / - Rendering pipeline consisting of static and programmable pipeline stages. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL'?

### Page 13 - OpenGL vs. Vulkan

Source cue: - How about Vulkan? / - More modern than OpenGL / - Designed for high performance and low-level GPU control / - Better suited for complex, large-scale rendering engines / - Vulkan also harder to learn and requires more setup/code

Professor-style explanation: The slide 'OpenGL vs. Vulkan' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - How about Vulkan? / - More modern than OpenGL / - Designed for high performance and low-level GPU control / - Better suited for complex, large-scale rendering engines / - Vulkan also harder to learn and requires more setup/code. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL vs. Vulkan. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - How about Vulkan? / - More modern than OpenGL / - Designed for high performance and low-level GPU control / - Better suited for complex, large-scale rendering engines / - Vulkan also harder to learn and requires more setup/code. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL vs. Vulkan' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL vs. Vulkan'?

### Page 14 - OpenGL Libraries

Source cue: - Different tastes of OpenGL / - OpenGL / - OpenGL ES - limited version for embedded systems / - WebGL - Javascript connection for Web Development / (functionality similar to OpenGL ES)

Professor-style explanation: The slide 'OpenGL Libraries' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Different tastes of OpenGL / - OpenGL / - OpenGL ES - limited version for embedded systems / - WebGL - Javascript connection for Web Development / (functionality similar to OpenGL ES). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL Libraries. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Different tastes of OpenGL / - OpenGL / - OpenGL ES - limited version for embedded systems / - WebGL - Javascript connection for Web Development / (functionality similar to OpenGL ES). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL Libraries' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Libraries'?

### Page 15 - OpenGL Functionality

Source cue: - Functional API / - Objects, scenes and images are described by a sequence of commands / (functional approach, low-level) / - Contrast: scene or object description (declarative approach, high-level) / - OpenGL context

Professor-style explanation: The slide 'OpenGL Functionality' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Functional API / - Objects, scenes and images are described by a sequence of commands / (functional approach, low-level) / - Contrast: scene or object description (declarative approach, high-level) / - OpenGL context. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL Functionality. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Functional API / - Objects, scenes and images are described by a sequence of commands / (functional approach, low-level) / - Contrast: scene or object description (declarative approach, high-level) / - OpenGL context. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL Functionality' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Functionality'?

### Page 16 - OpenGL Context

Source cue: - Context is created and modified by the application, / and contains all the state variables of the OpenGL engine / - Any number of contexts per application possible, / but at most one active context per application / - Context is generally tied to an output window

Professor-style explanation: The slide 'OpenGL Context' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Context is created and modified by the application, / and contains all the state variables of the OpenGL engine / - Any number of contexts per application possible, / but at most one active context per application / - Context is generally tied to an output window. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL Context. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Context is created and modified by the application, / and contains all the state variables of the OpenGL engine / - Any number of contexts per application possible, / but at most one active context per application / - Context is generally tied to an output window. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL Context' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Context'?

### Page 17 - OpenGL Rendering Process

Source cue: - Initiation from the developer's perspective / - Creation of the output window / - Creation of the context / - Specification of the scene geometry / - Uploading of the scene geometry to the GPU

Professor-style explanation: The slide 'OpenGL Rendering Process' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Initiation from the developer's perspective / - Creation of the output window / - Creation of the context / - Specification of the scene geometry / - Uploading of the scene geometry to the GPU. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL Rendering Process. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Initiation from the developer's perspective / - Creation of the output window / - Creation of the context / - Specification of the scene geometry / - Uploading of the scene geometry to the GPU. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL Rendering Process' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Rendering Process'?

### Page 18 - Window Creation with GLFW 1/2

Source cue: #include <GLFW/glfw3.h> / #include <stdlib.h> / #include <stdio.h> / static void error_callback(int error, const char* description) { / fputs(description, stderr);

Professor-style explanation: The slide 'Window Creation with GLFW 1/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: #include <GLFW/glfw3.h> / #include <stdlib.h> / #include <stdio.h> / static void error_callback(int error, const char* description) { / fputs(description, stderr). The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Window Creation with GLFW 1/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: #include <GLFW/glfw3.h> / #include <stdlib.h> / #include <stdio.h> / static void error_callback(int error, const char* description) { / fputs(description, stderr). The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Window Creation with GLFW 1/2' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Window Creation with GLFW 1/2' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Window Creation with GLFW 1/2' into a causal sentence instead of repeating the slide title?

### Page 19 - Window Creation with GLFW 2/2

Source cue: int main(void){ / GLFWwindow* window; / glfwSetErrorCallback(error_callback); / if (!glfwInit()) exit(EXIT_FAILURE); / window = glfwCreateWindow(640, 480, "Simple example", NULL, NULL);

Professor-style explanation: The slide 'Window Creation with GLFW 2/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: int main(void){ / GLFWwindow* window; / glfwSetErrorCallback(error_callback); / if (!glfwInit()) exit(EXIT_FAILURE); / window = glfwCreateWindow(640, 480, "Simple example", NULL, NULL). The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Window Creation with GLFW 2/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: int main(void){ / GLFWwindow* window; / glfwSetErrorCallback(error_callback); / if (!glfwInit()) exit(EXIT_FAILURE); / window = glfwCreateWindow(640, 480, "Simple example", NULL, NULL). The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Window Creation with GLFW 2/2' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Window Creation with GLFW 2/2' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Window Creation with GLFW 2/2' into a causal sentence instead of repeating the slide title?

### Page 20 - OpenGL Naming Conventions

Source cue: - Function-Prefix "gl" / - glClear, ... / - Constant-Prefix "GL" / - GL_POLYGON, GL_LINES, ... / - Parameter types are explicitly encoded in function names

Professor-style explanation: The slide 'OpenGL Naming Conventions' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Function-Prefix "gl" / - glClear, ... / - Constant-Prefix "GL" / - GL_POLYGON, GL_LINES, ... / - Parameter types are explicitly encoded in function names. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL Naming Conventions. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Function-Prefix "gl" / - glClear, ... / - Constant-Prefix "GL" / - GL_POLYGON, GL_LINES, ... / - Parameter types are explicitly encoded in function names. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL Naming Conventions' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Naming Conventions'?

### Page 21 - 2.3 OpenGL Rendering

Source cue: Transfer of 3D models to the GPU

Professor-style explanation: The slide '2.3 OpenGL Rendering' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: Transfer of 3D models to the GPU. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about 2.3 OpenGL Rendering. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: Transfer of 3D models to the GPU. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for '2.3 OpenGL Rendering' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2.3 OpenGL Rendering'?

### Page 22 - OpenGL Rendering (until V2.1)

Source cue: - Rendering is done through Immediate Mode / void renderScene() { / glColor3f(0.0f, 1.0f, 0.0f); // drawing color becomes green / glBegin(GL_POLYGON); // begin primitive / glVertex2f(-0.5f,-0.5f); // 1. vertex

Professor-style explanation: The slide 'OpenGL Rendering (until V2.1)' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Rendering is done through Immediate Mode / void renderScene() { / glColor3f(0.0f, 1.0f, 0.0f); // drawing color becomes green / glBegin(GL_POLYGON); // begin primitive / glVertex2f(-0.5f,-0.5f); // 1. vertex. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL Rendering (until V2.1). The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Rendering is done through Immediate Mode / void renderScene() { / glColor3f(0.0f, 1.0f, 0.0f); // drawing color becomes green / glBegin(GL_POLYGON); // begin primitive / glVertex2f(-0.5f,-0.5f); // 1. vertex. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL Rendering (until V2.1)' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Rendering (until V2.1)'?

### Page 23 - OpenGL Rendering (since V3.0)

Source cue: - Using Vertex Array Objects (VAOs) / - Vertex specification in CPU memory / - Vertex data transfer from CPU to GPU / - Memory layout description of the vertex data / - Number of vertices, number of components (x, y, z, ...)

Professor-style explanation: The slide 'OpenGL Rendering (since V3.0)' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Using Vertex Array Objects (VAOs) / - Vertex specification in CPU memory / - Vertex data transfer from CPU to GPU / - Memory layout description of the vertex data / - Number of vertices, number of components (x, y, z, ...). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL Rendering (since V3.0). The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Using Vertex Array Objects (VAOs) / - Vertex specification in CPU memory / - Vertex data transfer from CPU to GPU / - Memory layout description of the vertex data / - Number of vertices, number of components (x, y, z, ...). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL Rendering (since V3.0)' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Rendering (since V3.0)'?

### Page 24 - 1. Vertex Specification

Source cue: - Vertex data is specified as a C array / // vertices of two triangles / GLfloat vertices[6][2] = { // 6 vertices with two components each (x,y) / {0.0, 1.0}, {1.0, 1.0}, {1.0, 0.0}, // 1. triangle / {0.5, 0.5}, {1.0, 0.3}, {0.7, 1.0} // 2. triangle

Professor-style explanation: The outline '1. Vertex Specification' gives the lecture its internal logic. The listed topics are the objects that will be connected during the chapter: first the problem space, then the mathematical or algorithmic tools, then the implementation consequences. The listed entries form a dependency order: - Vertex data is specified as a C array / // vertices of two triangles / GLfloat vertices[6][2] = { // 6 vertices with two components each (x,y) / {0.0, 1.0}, {1.0, 1.0}, {1.0, 0.0}, // 1. triangle / {0.5, 0.5}, {1.0, 0.3}, {0.7, 1.0} // 2. triangle. Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary. The order matters because later items rely on earlier definitions. For example, an OpenGL mechanism is much easier to understand once the corresponding pipeline object or mathematical operation has already been introduced. The outline is therefore a compact dependency graph of the lecture rather than a collection of isolated labels. For examination purposes, the important content is the dependency structure: which concept introduces the vocabulary, which later algorithm uses it, and which implementation problem it solves.

Technical commentary: This slide is about 1. Vertex Specification. The listed items define the lecture sequence: the topic begins with a problem statement, introduces the required objects or algorithms, and then connects them to rendering or implementation consequences. The listed entries form a dependency order: - Vertex data is specified as a C array / // vertices of two triangles / GLfloat vertices[6][2] = { // 6 vertices with two components each (x,y) / {0.0, 1.0}, {1.0, 1.0}, {1.0, 0.0}, // 1. triangle / {0.5, 0.5}, {1.0, 0.3}, {0.7, 1.0} // 2. triangle. Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary.

Why it matters: Outlines tell you the dependency order. They are the safest way to avoid learning isolated bullet points.

Exam-grade answer: A strong answer for '1. Vertex Specification' names the topics in order and explains at least one dependency between an earlier item and a later item.

Common trap: Do not memorize '1. Vertex Specification' as a list of headings only; the exam-relevant part is how the headings depend on each other.

Check yourself: Can you explain where '1. Vertex Specification' fits in the lecture order and what later section depends on it?

### Page 25 - 2. Vertex Data Transfer

Source cue: - VBO allocation and data transfer via / - glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW); / - data - address in main memory (i.e., vertices or &vertices[0]) / - size - size of data in number of bytes / (i.e. sizeof(vertices) or numVertices*sizeof(GLfloat)*2)

Professor-style explanation: The slide '2. Vertex Data Transfer' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - VBO allocation and data transfer via / - glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW); / - data - address in main memory (i.e., vertices or &vertices[0]) / - size - size of data in number of bytes / (i.e. sizeof(vertices) or numVertices*sizeof(GLfloat)*2). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about 2. Vertex Data Transfer. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - VBO allocation and data transfer via / - glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW); / - data - address in main memory (i.e., vertices or &vertices[0]) / - size - size of data in number of bytes / (i.e. sizeof(vertices) or numVertices*sizeof(GLfloat)*2). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for '2. Vertex Data Transfer' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2. Vertex Data Transfer'?

### Page 26 - 3. Memory Layout Description

Source cue: - Memory layout is described by the following function / - glVertexAttribPointer(attribIndex, size, type, normalized, stride, offset); / - attribIndex - attribute number (0 for position, later more ...) / - size - number of components per vertex (2 for xy, 3 for xyz) / - type - base type (typically GL_FLOAT or GL_DOUBLE)

Professor-style explanation: The slide '3. Memory Layout Description' explains raster images as concrete stored data. A raster image is a rectangular grid of pixels. Each pixel stores one or more channel values, such as red, green, blue, and sometimes alpha. Color depth tells us how many bits are available per pixel or per channel, and that immediately determines both the number of representable colors and the memory footprint of the image. The numerical values belong to one memory calculation: - Memory layout is described by the following function / - glVertexAttribPointer(attribIndex, size, type, normalized, stride, offset); / - attribIndex - attribute number (0 for position, later more ...) / - size - number of components per vertex (2 for xy, 3 for xyz) / - type - base type (typically GL_FLOAT or GL_DOUBLE). Resolution gives the number of pixels, color depth gives bits per pixel, and their product gives storage and bandwidth cost. The object relation is pixel count, bits per pixel, color range, and memory size. This is why a simple image-resolution question is also a performance question: more pixels and more bits mean more memory traffic, more storage, and more work for display or image-processing operations. For examination purposes, the important content is the chain width x height -> pixel count -> bits per pixel -> memory size; this chain also explains bandwidth and performance pressure.

Technical commentary: This slide is about 3. Memory Layout Description. The slide describes image data as discrete samples: pixels, color channels, bit depth, memory layout, and the amount of storage needed for a raster image. The numerical values belong to one memory calculation: - Memory layout is described by the following function / - glVertexAttribPointer(attribIndex, size, type, normalized, stride, offset); / - attribIndex - attribute number (0 for position, later more ...) / - size - number of components per vertex (2 for xy, 3 for xyz) / - type - base type (typically GL_FLOAT or GL_DOUBLE). Resolution gives the number of pixels, color depth gives bits per pixel, and their product gives storage and bandwidth cost.

Why it matters: Pixel-data slides connect visual output to memory size, bandwidth, precision, and image-processing cost.

Exam-grade answer: A strong answer for '3. Memory Layout Description' includes the formula relation width x height x bits per pixel, distinguishes bits from bytes, and links larger images to memory bandwidth.

Common trap: Do not confuse bits with bytes in '3. Memory Layout Description', and do not ignore that alpha or higher precision changes memory size.

Check yourself: Can you compute or explain the pixel count, color depth, or memory relation in '3. Memory Layout Description'?

### Page 27 - 4. VAO Drawing 1/2

Source cue: - Drawing is done with the command / - glDrawArrays(mode, first, count); / - mode - specifies the primitive type (e.g., GL_TRIANGLES or GL_LINES) / - From all vertices, the next count vertices are drawn from index first / - Actual vertex data no longer needs to be specified

Professor-style explanation: The slide '4. VAO Drawing 1/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Drawing is done with the command / - glDrawArrays(mode, first, count); / - mode - specifies the primitive type (e.g., GL_TRIANGLES or GL_LINES) / - From all vertices, the next count vertices are drawn from index first / - Actual vertex data no longer needs to be specified. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about 4. VAO Drawing 1/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Drawing is done with the command / - glDrawArrays(mode, first, count); / - mode - specifies the primitive type (e.g., GL_TRIANGLES or GL_LINES) / - From all vertices, the next count vertices are drawn from index first / - Actual vertex data no longer needs to be specified. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for '4. VAO Drawing 1/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by '4. VAO Drawing 1/2'?

### Page 28 - 4. VAO Drawing 2/2

Source cue: - There is a small number of primitive types / - Points / - Lines, Line Strips, Line Loops / - Triangles, Triangle Strips, Triangle Fans, Patches / v2 v2 v2

Professor-style explanation: The slide '4. VAO Drawing 2/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - There is a small number of primitive types / - Points / - Lines, Line Strips, Line Loops / - Triangles, Triangle Strips, Triangle Fans, Patches / v2 v2 v2. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about 4. VAO Drawing 2/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - There is a small number of primitive types / - Points / - Lines, Line Strips, Line Loops / - Triangles, Triangle Strips, Triangle Fans, Patches / v2 v2 v2. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for '4. VAO Drawing 2/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by '4. VAO Drawing 2/2'?

### Page 29 - 5. GPU Memory Release

Source cue: - After usage VAO and VBO should be deleted from GPU memory / - glDeleteBuffers(...); / - glDeleteVertexArrays(...);

Professor-style explanation: The slide '5. GPU Memory Release' explains raster images as concrete stored data. A raster image is a rectangular grid of pixels. Each pixel stores one or more channel values, such as red, green, blue, and sometimes alpha. Color depth tells us how many bits are available per pixel or per channel, and that immediately determines both the number of representable colors and the memory footprint of the image. The numerical values belong to one memory calculation: - After usage VAO and VBO should be deleted from GPU memory / - glDeleteBuffers(...); / - glDeleteVertexArrays(...). Resolution gives the number of pixels, color depth gives bits per pixel, and their product gives storage and bandwidth cost. The object relation is pixel count, bits per pixel, color range, and memory size. This is why a simple image-resolution question is also a performance question: more pixels and more bits mean more memory traffic, more storage, and more work for display or image-processing operations. For examination purposes, the important content is the chain width x height -> pixel count -> bits per pixel -> memory size; this chain also explains bandwidth and performance pressure.

Technical commentary: This slide is about 5. GPU Memory Release. The slide describes image data as discrete samples: pixels, color channels, bit depth, memory layout, and the amount of storage needed for a raster image. The numerical values belong to one memory calculation: - After usage VAO and VBO should be deleted from GPU memory / - glDeleteBuffers(...); / - glDeleteVertexArrays(...). Resolution gives the number of pixels, color depth gives bits per pixel, and their product gives storage and bandwidth cost.

Why it matters: Pixel-data slides connect visual output to memory size, bandwidth, precision, and image-processing cost.

Exam-grade answer: A strong answer for '5. GPU Memory Release' includes the formula relation width x height x bits per pixel, distinguishes bits from bytes, and links larger images to memory bandwidth.

Common trap: Do not confuse bits with bytes in '5. GPU Memory Release', and do not ignore that alpha or higher precision changes memory size.

Check yourself: Can you compute or explain the pixel count, color depth, or memory relation in '5. GPU Memory Release'?

### Page 30 - Rendering Initialization 1/2

Source cue: static void init_render_scene(void) { / static const GLfloat vertices[6][2] = { / {0.0f, 1.0f}, {1.0f, 1.0f}, {1.0f, 0.0f}, /* 1st triangle */ / {0.5f, 0.5f}, {1.0f, 0.3f}, {0.7f, 1.0f} /* 2nd triangle */ / static const char* vs_src =

Professor-style explanation: The slide 'Rendering Initialization 1/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: static void init_render_scene(void) { / static const GLfloat vertices[6][2] = { / {0.0f, 1.0f}, {1.0f, 1.0f}, {1.0f, 0.0f}, /* 1st triangle */ / {0.5f, 0.5f}, {1.0f, 0.3f}, {0.7f, 1.0f} /* 2nd triangle */ / static const char* vs_src =. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Rendering Initialization 1/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: static void init_render_scene(void) { / static const GLfloat vertices[6][2] = { / {0.0f, 1.0f}, {1.0f, 1.0f}, {1.0f, 0.0f}, /* 1st triangle */ / {0.5f, 0.5f}, {1.0f, 0.3f}, {0.7f, 1.0f} /* 2nd triangle */ / static const char* vs_src =. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Rendering Initialization 1/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Rendering Initialization 1/2'?

### Page 31 - Rendering Initialization 2/2

Source cue: program = create_program(vs_src, fs_src); / glGenVertexArrays(1, &vao); / glGenBuffers(1, &vbo); / glBindVertexArray(vao); / glBindBuffer(GL_ARRAY_BUFFER, vbo);

Professor-style explanation: The slide 'Rendering Initialization 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: program = create_program(vs_src, fs_src); / glGenVertexArrays(1, &vao); / glGenBuffers(1, &vbo); / glBindVertexArray(vao); / glBindBuffer(GL_ARRAY_BUFFER, vbo). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Rendering Initialization 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: program = create_program(vs_src, fs_src); / glGenVertexArrays(1, &vao); / glGenBuffers(1, &vbo); / glBindVertexArray(vao); / glBindBuffer(GL_ARRAY_BUFFER, vbo). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Rendering Initialization 2/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Rendering Initialization 2/2'?

### Page 32 - Rendering

Source cue: static void render_scene(void) { / glClear(GL_COLOR_BUFFER_BIT); / glUseProgram(program); / glBindVertexArray(vao); / glDrawArrays(GL_TRIANGLES, 0, 6);

Professor-style explanation: The slide 'Rendering' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: static void render_scene(void) { / glClear(GL_COLOR_BUFFER_BIT); / glUseProgram(program); / glBindVertexArray(vao); / glDrawArrays(GL_TRIANGLES, 0, 6). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Rendering. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: static void render_scene(void) { / glClear(GL_COLOR_BUFFER_BIT); / glUseProgram(program); / glBindVertexArray(vao); / glDrawArrays(GL_TRIANGLES, 0, 6). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Rendering' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Rendering'?

### Page 33 - Additional Attributes

Source cue: - Additional attributes are necessary for drawing / - Color, normals, texture coordinates, ... / - There are two ways to assign these attributes to the vertex data / - Attributes are bound to the same VAO in separate VBO / - Attributes are stored interleaved with vertex data,

Professor-style explanation: The slide 'Additional Attributes' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Additional attributes are necessary for drawing / - Color, normals, texture coordinates, ... / - There are two ways to assign these attributes to the vertex data / - Attributes are bound to the same VAO in separate VBO / - Attributes are stored interleaved with vertex data,. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Additional Attributes. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Additional attributes are necessary for drawing / - Color, normals, texture coordinates, ... / - There are two ways to assign these attributes to the vertex data / - Attributes are bound to the same VAO in separate VBO / - Attributes are stored interleaved with vertex data,. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Additional Attributes' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Additional Attributes' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Additional Attributes'?

### Page 34 - 2.4 OpenGL Rendering Pipeline

Source cue: Programmable and static stages

Professor-style explanation: The slide '2.4 OpenGL Rendering Pipeline' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: Programmable and static stages. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about 2.4 OpenGL Rendering Pipeline. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: Programmable and static stages. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for '2.4 OpenGL Rendering Pipeline' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2.4 OpenGL Rendering Pipeline'?

### Page 35 - The Rendering Pipeline 1/2

Source cue: Scene Description Raster Image / Geometry Fragment / Rasterization / Processing Processing / Vertices Primitives Fragments Pixels

Professor-style explanation: The slide 'The Rendering Pipeline 1/2' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. The terms are successive representations in object-based rendering: Scene Description Raster Image / Geometry Fragment / Rasterization / Processing Processing / Vertices Primitives Fragments Pixels. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter. For examination purposes, the important content is the representation change at each stage: model data, vertices, primitives, fragments, fragment tests, and final framebuffer updates.

Technical commentary: This slide is about The Rendering Pipeline 1/2. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. The terms are successive representations in object-based rendering: Scene Description Raster Image / Geometry Fragment / Rasterization / Processing Processing / Vertices Primitives Fragments Pixels. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels.

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Exam-grade answer: A strong answer for 'The Rendering Pipeline 1/2' states what representation enters the stage, what representation leaves it, and which later stage depends on that output.

Common trap: Do not collapse 'The Rendering Pipeline 1/2' into 'the GPU draws it'; name the intermediate representations because that is where most errors and exam distinctions appear.

Check yourself: Can you name the input and output representation for 'The Rendering Pipeline 1/2' in the rendering pipeline?

### Page 36 - The Rendering Pipeline 2/2

Source cue: - Sequence of fixed and programmable stages Programmable / Vertex Processing / - Process is influenced by context and scene objects / Context Fixed Function / - Programmable levels are programmed

Professor-style explanation: The slide 'The Rendering Pipeline 2/2' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. The terms are successive representations in object-based rendering: - Sequence of fixed and programmable stages Programmable / Vertex Processing / - Process is influenced by context and scene objects / Context Fixed Function / - Programmable levels are programmed. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter. For examination purposes, the important content is the representation change at each stage: model data, vertices, primitives, fragments, fragment tests, and final framebuffer updates.

Technical commentary: This slide is about The Rendering Pipeline 2/2. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. The terms are successive representations in object-based rendering: - Sequence of fixed and programmable stages Programmable / Vertex Processing / - Process is influenced by context and scene objects / Context Fixed Function / - Programmable levels are programmed. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels.

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Exam-grade answer: A strong answer for 'The Rendering Pipeline 2/2' states what representation enters the stage, what representation leaves it, and which later stage depends on that output.

Common trap: Do not collapse 'The Rendering Pipeline 2/2' into 'the GPU draws it'; name the intermediate representations because that is where most errors and exam distinctions appear.

Check yourself: Can you name the input and output representation for 'The Rendering Pipeline 2/2' in the rendering pipeline?

### Page 37 - Shader Programming - History 1/2

Source cue: - There is special graphics hardware (dedicated) / and general graphics hardware (general purpose) / - Special graphics hardware / - Volume Rendering: VolumePro / - Game consoles: Custom NVIDIA chips in XBox

Professor-style explanation: The slide 'Shader Programming - History 1/2' explains the historical background behind the graphics concept. Computer graphics did not appear as one finished pipeline; it developed from older ideas such as artistic perspective, color representation, display hardware, interactive systems, and increasingly programmable rendering algorithms. The historical objects on the slide are people, systems, dates, or milestones, and each milestone marks a capability that later became normal in graphics software. The names, dates, and examples form a timeline: - There is special graphics hardware (dedicated) / and general graphics hardware (general purpose) / - Special graphics hardware / - Volume Rendering: VolumePro / - Game consoles: Custom NVIDIA chips in XBox. Each item marks a capability or use case that pushed graphics from static image construction toward interactive, programmable rendering. This history matters because it shows why the course combines mathematics, image representation, hardware acceleration, and interaction. Modern real-time rendering is the result of these threads converging into a pipeline that can generate images fast enough for user input. For examination purposes, the important content is not the date alone but the reason the milestone matters: every historical item solved a limitation in representation, interaction, display, or computation.

Technical commentary: This slide is about Shader Programming - History 1/2. The slide places the technical topic into the historical development of computer graphics, showing how artistic perspective, display technology, interaction, and rendering algorithms evolved together. The names, dates, and examples form a timeline: - There is special graphics hardware (dedicated) / and general graphics hardware (general purpose) / - Special graphics hardware / - Volume Rendering: VolumePro / - Game consoles: Custom NVIDIA chips in XBox. Each item marks a capability or use case that pushed graphics from static image construction toward interactive, programmable rendering.

Why it matters: Historical slides explain why the current pipeline exists and which older problems led to modern graphics concepts.

Exam-grade answer: A strong answer for 'Shader Programming - History 1/2' states the milestone and the graphics limitation it helped overcome, such as limited interaction, limited displays, missing 3D representation, or slow rendering.

Common trap: Do not learn 'Shader Programming - History 1/2' as trivia only; connect each historical item to the technical capability it introduced or made practical.

Check yourself: Can you name the graphics capability or idea represented by 'Shader Programming - History 1/2' and why it mattered historically?

### Page 38 - Shader Programming - History 2/2

Source cue: - Various vendor-dependent extensions are introduced / to provide extensibility for general graphics hardware / - Texture shaders and register combiners allowed modification / through the application of textures / - Applicability is very limited by the possibilities of graphics hardware

Professor-style explanation: The slide 'Shader Programming - History 2/2' explains the historical background behind the graphics concept. Computer graphics did not appear as one finished pipeline; it developed from older ideas such as artistic perspective, color representation, display hardware, interactive systems, and increasingly programmable rendering algorithms. The historical objects on the slide are people, systems, dates, or milestones, and each milestone marks a capability that later became normal in graphics software. The names, dates, and examples form a timeline: - Various vendor-dependent extensions are introduced / to provide extensibility for general graphics hardware / - Texture shaders and register combiners allowed modification / through the application of textures / - Applicability is very limited by the possibilities of graphics hardware. Each item marks a capability or use case that pushed graphics from static image construction toward interactive, programmable rendering. This history matters because it shows why the course combines mathematics, image representation, hardware acceleration, and interaction. Modern real-time rendering is the result of these threads converging into a pipeline that can generate images fast enough for user input. For examination purposes, the important content is not the date alone but the reason the milestone matters: every historical item solved a limitation in representation, interaction, display, or computation.

Technical commentary: This slide is about Shader Programming - History 2/2. The slide places the technical topic into the historical development of computer graphics, showing how artistic perspective, display technology, interaction, and rendering algorithms evolved together. The names, dates, and examples form a timeline: - Various vendor-dependent extensions are introduced / to provide extensibility for general graphics hardware / - Texture shaders and register combiners allowed modification / through the application of textures / - Applicability is very limited by the possibilities of graphics hardware. Each item marks a capability or use case that pushed graphics from static image construction toward interactive, programmable rendering.

Why it matters: Historical slides explain why the current pipeline exists and which older problems led to modern graphics concepts.

Exam-grade answer: A strong answer for 'Shader Programming - History 2/2' states the milestone and the graphics limitation it helped overcome, such as limited interaction, limited displays, missing 3D representation, or slow rendering.

Common trap: Do not learn 'Shader Programming - History 2/2' as trivia only; connect each historical item to the technical capability it introduced or made practical.

Check yourself: Can you name the graphics capability or idea represented by 'Shader Programming - History 2/2' and why it mattered historically?

### Page 39 - Assembler Shader

Source cue: - First OpenGL extensions support shader programming in assembler code / !! ARBvp1.0 / ATTRIB iPos = vertex.position ; / ATTRIB iNormal = vertex.normal ; / ...

Professor-style explanation: The slide 'Assembler Shader' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - First OpenGL extensions support shader programming in assembler code / !! ARBvp1.0 / ATTRIB iPos = vertex.position ; / ATTRIB iNormal = vertex.normal ; / . Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Assembler Shader. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - First OpenGL extensions support shader programming in assembler code / !! ARBvp1.0 / ATTRIB iPos = vertex.position ; / ATTRIB iNormal = vertex.normal ; / . Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Assembler Shader' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Assembler Shader'?

### Page 40 - High-Level Shading Languages 1/2

Source cue: - Assembler code is hard to read and hard to maintain / - High-level languages f or shading are specified in C-like syntax / - Source code is translated by the compiler into appropriate ASM statements / - Using shaders after initial binding automatically when rendering geometry / - Interface to OpenGL by passing appropriate variables or changing the OpenGL

Professor-style explanation: The slide 'High-Level Shading Languages 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Assembler code is hard to read and hard to maintain / - High-level languages f or shading are specified in C-like syntax / - Source code is translated by the compiler into appropriate ASM statements / - Using shaders after initial binding automatically when rendering geometry / - Interface to OpenGL by passing appropriate variables or changing the OpenGL. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about High-Level Shading Languages 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Assembler code is hard to read and hard to maintain / - High-level languages f or shading are specified in C-like syntax / - Source code is translated by the compiler into appropriate ASM statements / - Using shaders after initial binding automatically when rendering geometry / - Interface to OpenGL by passing appropriate variables or changing the OpenGL. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'High-Level Shading Languages 1/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'High-Level Shading Languages 1/2'?

### Page 41 - High-Level Shading Languages 2/2

Source cue: - Existing high level languages f or shader development / - CG - C for Graphics by NVIDIA / - CG was introduced in 2003 by NVIDIA as a platform independent solution / (in practice rather semi-platform independent) / - HLSL - High Level Shading Language from Microsoft

Professor-style explanation: The slide 'High-Level Shading Languages 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Existing high level languages f or shader development / - CG - C for Graphics by NVIDIA / - CG was introduced in 2003 by NVIDIA as a platform independent solution / (in practice rather semi-platform independent) / - HLSL - High Level Shading Language from Microsoft. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about High-Level Shading Languages 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Existing high level languages f or shader development / - CG - C for Graphics by NVIDIA / - CG was introduced in 2003 by NVIDIA as a platform independent solution / (in practice rather semi-platform independent) / - HLSL - High Level Shading Language from Microsoft. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'High-Level Shading Languages 2/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'High-Level Shading Languages 2/2'?

### Page 42 - Shader Types

Source cue: - Pipeline concept has been kept in place / and shaders are responsible for different stages / - First, geometry level programming was done by vertex shaders / - Vertex shaders allow modifiability of vertex transformations and lighting / - After that, there was an extension for image-based algorithms by fragment

Professor-style explanation: The slide 'Shader Types' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Pipeline concept has been kept in place / and shaders are responsible for different stages / - First, geometry level programming was done by vertex shaders / - Vertex shaders allow modifiability of vertex transformations and lighting / - After that, there was an extension for image-based algorithms by fragment. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Shader Types. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Pipeline concept has been kept in place / and shaders are responsible for different stages / - First, geometry level programming was done by vertex shaders / - Vertex shaders allow modifiability of vertex transformations and lighting / - After that, there was an extension for image-based algorithms by fragment. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Shader Types' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Types'?

### Page 43 - Vertex Shader Concepts

Source cue: - Vertex shaders enable the programmable modification of processed geometry / - Possibilities of a vertex shader / Programmable / - Geometric transformation of vertices and normals / Vertex Processing

Professor-style explanation: The slide 'Vertex Shader Concepts' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Vertex shaders enable the programmable modification of processed geometry / - Possibilities of a vertex shader / Programmable / - Geometric transformation of vertices and normals / Vertex Processing. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Vertex Shader Concepts. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Vertex shaders enable the programmable modification of processed geometry / - Possibilities of a vertex shader / Programmable / - Geometric transformation of vertices and normals / Vertex Processing. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Vertex Shader Concepts' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Concepts'?

### Page 44 - Vertex Shader Examples 1/2

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Vertex Shader Examples 1/2' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Vertex Shader Examples 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Vertex Shader Examples 1/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Examples 1/2'?

### Page 45 - Vertex Shader Examples 2/2

Source cue: - Morphing / - Shadow volume calculation for shadow effects / [ID Software‘s Doom III]

Professor-style explanation: The slide 'Vertex Shader Examples 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Morphing / - Shadow volume calculation for shadow effects / [ID Software‘s Doom III]. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Vertex Shader Examples 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Morphing / - Shadow volume calculation for shadow effects / [ID Software‘s Doom III]. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Vertex Shader Examples 2/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Examples 2/2'?

### Page 46 - Vertex Shader Coordinate Systems 1/2

Source cue: - Vertex shaders are executed for each vertex / - Vertex shaders calculate coordinates in clipping coordinates as output / - Vertex shaders can not / - Access adjacent vertices / - Change the number of vertices (i.e., generate or discard vertices)

Professor-style explanation: The slide 'Vertex Shader Coordinate Systems 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Vertex shaders are executed for each vertex / - Vertex shaders calculate coordinates in clipping coordinates as output / - Vertex shaders can not / - Access adjacent vertices / - Change the number of vertices (i.e., generate or discard vertices). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Vertex Shader Coordinate Systems 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Vertex shaders are executed for each vertex / - Vertex shaders calculate coordinates in clipping coordinates as output / - Vertex shaders can not / - Access adjacent vertices / - Change the number of vertices (i.e., generate or discard vertices). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Vertex Shader Coordinate Systems 1/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Coordinate Systems 1/2'?

### Page 47 - Vertex Shader Coordinate Systems 2/2

Source cue: Local Space World Space View Space Clip Space Screen Space / Viewport / M M M / model view project Transform

Professor-style explanation: The slide 'Vertex Shader Coordinate Systems 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: Local Space World Space View Space Clip Space Screen Space / Viewport / M M M / model view project Transform. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Vertex Shader Coordinate Systems 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: Local Space World Space View Space Clip Space Screen Space / Viewport / M M M / model view project Transform. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Vertex Shader Coordinate Systems 2/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Coordinate Systems 2/2'?

### Page 48 - Local Space

Source cue: - Coordinates of your object relative to its local origin / - 3D vertex positions

Professor-style explanation: The slide 'Local Space' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Coordinates of your object relative to its local origin / - 3D vertex positions. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Local Space. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Coordinates of your object relative to its local origin / - 3D vertex positions. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Local Space' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Local Space' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Local Space'?

### Page 49 - World Space

Source cue: - Coordinates in respect of a larger world / - Relative to some global origin of the world / - Together with many other objects

Professor-style explanation: The slide 'World Space' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Coordinates in respect of a larger world / - Relative to some global origin of the world / - Together with many other objects. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about World Space. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Coordinates in respect of a larger world / - Relative to some global origin of the world / - Together with many other objects. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'World Space' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'World Space' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'World Space'?

### Page 50 - View Space

Source cue: - Coordinates as seen from the camera

Professor-style explanation: The slide 'View Space' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Coordinates as seen from the camera. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about View Space. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Coordinates as seen from the camera. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'View Space' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'View Space' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'View Space'?

### Page 51 - Clip Space

Source cue: - Clip coordinates range from -1 to 1 / - Projection (Orthographic, Perspective)

Professor-style explanation: The slide 'Clip Space' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Clip coordinates range from -1 to 1 / - Projection (Orthographic, Perspective). Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Clip Space. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Clip coordinates range from -1 to 1 / - Projection (Orthographic, Perspective). Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Clip Space' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Clip Space' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Clip Space'?

### Page 52 - Screen Space

Source cue: - Transform to image coordinates with glViewport / - Results are sent to the rasterizer

Professor-style explanation: The slide 'Screen Space' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Transform to image coordinates with glViewport / - Results are sent to the rasterizer. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Screen Space. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Transform to image coordinates with glViewport / - Results are sent to the rasterizer. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Screen Space' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Screen Space' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Screen Space'?

### Page 53 - Coordinate Systems

Source cue: Local Space World Space View Space Clip Space Screen Space / Viewport / M M M / model view project Transform

Professor-style explanation: The slide 'Coordinate Systems' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: Local Space World Space View Space Clip Space Screen Space / Viewport / M M M / model view project Transform. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Coordinate Systems. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: Local Space World Space View Space Clip Space Screen Space / Viewport / M M M / model view project Transform. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Coordinate Systems' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Coordinate Systems' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Coordinate Systems'?

### Page 54 - Vertex Shader Variables

Source cue: - Input types / - Uniforms: read only in VS (& FS) // Intrinsic vertex attributes / out gl_PerVertex { / - For example: light position or light color / vec4 gl_Position;

Professor-style explanation: The slide 'Vertex Shader Variables' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Input types / - Uniforms: read only in VS (& FS) // Intrinsic vertex attributes / out gl_PerVertex { / - For example: light position or light color / vec4 gl_Position. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Vertex Shader Variables. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Input types / - Uniforms: read only in VS (& FS) // Intrinsic vertex attributes / out gl_PerVertex { / - For example: light position or light color / vec4 gl_Position. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Vertex Shader Variables' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Variables'?

### Page 55 - Fixed Function Vertex Postprocessing

Source cue: - Clipping / - Discard invisible geometries / Programmable / - Perspective Division / Vertex Processing

Professor-style explanation: The slide 'Fixed Function Vertex Postprocessing' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Clipping / - Discard invisible geometries / Programmable / - Perspective Division / Vertex Processing. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion. For examination purposes, the important content is classification: inside, outside, crossing, intersection point, and the newly produced primitive segment or polygon.

Technical commentary: This slide is about Fixed Function Vertex Postprocessing. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Clipping / - Discard invisible geometries / Programmable / - Perspective Division / Vertex Processing. A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Exam-grade answer: A strong answer for 'Fixed Function Vertex Postprocessing' classifies geometry relative to the boundary, explains intersection creation, and names the geometry passed to rasterization.

Common trap: Do not describe clipping as only deletion; crossing primitives can be cut and replaced by new vertices or primitive pieces.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Fixed Function Vertex Postprocessing'?

### Page 56 - Fixed Function Rasterization

Source cue: - Geometry is converted to raster coordinates / Programmable / Vertex Processing / Fixed Function / Primitives Fragments Vertex Postprocessing

Professor-style explanation: The slide 'Fixed Function Rasterization' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: - Geometry is converted to raster coordinates / Programmable / Vertex Processing / Fixed Function / Primitives Fragments Vertex Postprocessing. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Fixed Function Rasterization. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: - Geometry is converted to raster coordinates / Programmable / Vertex Processing / Fixed Function / Primitives Fragments Vertex Postprocessing. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Fixed Function Rasterization' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Fixed Function Rasterization' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Fixed Function Rasterization'?

### Page 57 - Fragment Shader Concept 1/2

Source cue: - Fragment shaders set the color of a pixel / - Possibilities of a fragment shader / Programmable / - Glare of textures / Vertex Processing

Professor-style explanation: The slide 'Fragment Shader Concept 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Fragment shaders set the color of a pixel / - Possibilities of a fragment shader / Programmable / - Glare of textures / Vertex Processing. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Fragment Shader Concept 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Fragment shaders set the color of a pixel / - Possibilities of a fragment shader / Programmable / - Glare of textures / Vertex Processing. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Fragment Shader Concept 1/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Fragment Shader Concept 1/2'?

### Page 58 - Fragment Shader Concept 2/2

Source cue: - Fragment shaders are executed for fragments (= pixel predecessors) / - Fragment shaders calculate the color and depth value of the current fragment / - No information about adjacent fragments available / - The number of fragments can be changed / - Fragment shaders can not generate fragments

Professor-style explanation: The slide 'Fragment Shader Concept 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Fragment shaders are executed for fragments (= pixel predecessors) / - Fragment shaders calculate the color and depth value of the current fragment / - No information about adjacent fragments available / - The number of fragments can be changed / - Fragment shaders can not generate fragments. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Fragment Shader Concept 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Fragment shaders are executed for fragments (= pixel predecessors) / - Fragment shaders calculate the color and depth value of the current fragment / - No information about adjacent fragments available / - The number of fragments can be changed / - Fragment shaders can not generate fragments. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Fragment Shader Concept 2/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Fragment Shader Concept 2/2'?

### Page 59 - Shader Example

Source cue: layout (std140) uniform Matrices { Vertex Shader / mat4 projModelViewMatrix; / mat3 normalMatrix; /** Fragment Shader / }; * Set fragment color to red. / in vec3 position;

Professor-style explanation: The slide 'Shader Example' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: layout (std140) uniform Matrices { Vertex Shader / mat4 projModelViewMatrix; / mat3 normalMatrix; /** Fragment Shader / }; * Set fragment color to red. / in vec3 position. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Shader Example. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: layout (std140) uniform Matrices { Vertex Shader / mat4 projModelViewMatrix; / mat3 normalMatrix; /** Fragment Shader / }; * Set fragment color to red. / in vec3 position. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Shader Example' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Example'?

### Page 60 - GLSL Shader Functions

Source cue: - Trigonometry functions / - radians, degrees, sin, cos, tan, asin, acos, atan / - Power calculations / - pow, exp2, log2, sqrt, inversesqrt / - General

Professor-style explanation: The slide 'GLSL Shader Functions' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Trigonometry functions / - radians, degrees, sin, cos, tan, asin, acos, atan / - Power calculations / - pow, exp2, log2, sqrt, inversesqrt / - General. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about GLSL Shader Functions. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Trigonometry functions / - radians, degrees, sin, cos, tan, asin, acos, atan / - Power calculations / - pow, exp2, log2, sqrt, inversesqrt / - General. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'GLSL Shader Functions' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'GLSL Shader Functions'?

### Page 61 - Shader Usage

Source cue: - One or multiple shaders are attached to a shader program / Vertex Shader / glCreateShader glCreateProgram / Fragment Shader / glShaderSource glAttachShader glCreateShader

Professor-style explanation: The slide 'Shader Usage' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - One or multiple shaders are attached to a shader program / Vertex Shader / glCreateShader glCreateProgram / Fragment Shader / glShaderSource glAttachShader glCreateShader. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Shader Usage. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - One or multiple shaders are attached to a shader program / Vertex Shader / glCreateShader glCreateProgram / Fragment Shader / glShaderSource glAttachShader glCreateShader. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Shader Usage' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Usage'?

### Page 62 - Binding Shaders

Source cue: v = glCreateShader(GL_VERTEX_SHADER); // vertex shader / char* vs = readTextFile("vertex-shader.vert"); / const char* vv = vs; / glShaderSource(v, 1, &vv, NULL); / free(vs);

Professor-style explanation: The slide 'Binding Shaders' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: v = glCreateShader(GL_VERTEX_SHADER); // vertex shader / char* vs = readTextFile("vertex-shader.vert"); / const char* vv = vs; / glShaderSource(v, 1, &vv, NULL); / free(vs). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Binding Shaders. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: v = glCreateShader(GL_VERTEX_SHADER); // vertex shader / char* vs = readTextFile("vertex-shader.vert"); / const char* vv = vs; / glShaderSource(v, 1, &vv, NULL); / free(vs). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Binding Shaders' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Binding Shaders'?

### Page 63 - Setting Uniforms

Source cue: - Uniforms are used to communicate between CPU and GPU / - Data is bound to uniform locations / - Must be updated after each linking process / GLint loc0 = glGetUniformLocation(p, "isoValue_"); / glUniform1f(loc0, 0.45f);

Professor-style explanation: The slide 'Setting Uniforms' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Uniforms are used to communicate between CPU and GPU / - Data is bound to uniform locations / - Must be updated after each linking process / GLint loc0 = glGetUniformLocation(p, "isoValue_"); / glUniform1f(loc0, 0.45f). The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Setting Uniforms. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Uniforms are used to communicate between CPU and GPU / - Data is bound to uniform locations / - Must be updated after each linking process / GLint loc0 = glGetUniformLocation(p, "isoValue_"); / glUniform1f(loc0, 0.45f). The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Setting Uniforms' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Setting Uniforms' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Setting Uniforms' into a causal sentence instead of repeating the slide title?

### Page 64 - Shader Performance

Source cue: - Guidelines for efficient shaders / - Since fragment shaders are executed for a large number of fragments, / they should contain as few instructions as possible / - There should be as little as possible a change of the active shaders, / because they have their own state and, accordingly, the pipeline may need

Professor-style explanation: The slide 'Shader Performance' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Guidelines for efficient shaders / - Since fragment shaders are executed for a large number of fragments, / they should contain as few instructions as possible / - There should be as little as possible a change of the active shaders, / because they have their own state and, accordingly, the pipeline may need. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Shader Performance. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Guidelines for efficient shaders / - Since fragment shaders are executed for a large number of fragments, / they should contain as few instructions as possible / - There should be as little as possible a change of the active shaders, / because they have their own state and, accordingly, the pipeline may need. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Shader Performance' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Performance'?

### Page 65 - Shader Development Environments 1/2

Source cue: - FX Composer, NVPerfHUD (NVIDIA) / - HLSL Shader IDE with performance analytics / www.developer.nvidia.com/page/tools.html / - RenderMonkey (ATI) / - HLSL, GLSL Shader IDE with performance analytics

Professor-style explanation: The slide 'Shader Development Environments 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - FX Composer, NVPerfHUD (NVIDIA) / - HLSL Shader IDE with performance analytics / www.developer.nvidia.com/page/tools.html / - RenderMonkey (ATI) / - HLSL, GLSL Shader IDE with performance analytics. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Shader Development Environments 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - FX Composer, NVPerfHUD (NVIDIA) / - HLSL Shader IDE with performance analytics / www.developer.nvidia.com/page/tools.html / - RenderMonkey (ATI) / - HLSL, GLSL Shader IDE with performance analytics. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Shader Development Environments 1/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Development Environments 1/2'?

### Page 66 - Shader Development Environments 2/2

Source cue: - Shdr online GLSL editor: https://shdr.bkcore.com/

Professor-style explanation: The slide 'Shader Development Environments 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Shdr online GLSL editor: https://shdr.bkcore.com/. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Shader Development Environments 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Shdr online GLSL editor: https://shdr.bkcore.com/. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Shader Development Environments 2/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Development Environments 2/2'?

### Page 67 - 2.5 Fragment Tests and Operations

Source cue: Towards the finishing line to the pixel

Professor-style explanation: The slide '2.5 Fragment Tests and Operations' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: Towards the finishing line to the pixel. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about 2.5 Fragment Tests and Operations. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: Towards the finishing line to the pixel. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for '2.5 Fragment Tests and Operations' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by '2.5 Fragment Tests and Operations'?

### Page 68 - Fragment Tests and Operations 1/2

Source cue: - After fragments have been generated, they must go through the per-fragment / tests and operations / Programmable / - Only if all these tests are successful, / Vertex Processing

Professor-style explanation: The slide 'Fragment Tests and Operations 1/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - After fragments have been generated, they must go through the per-fragment / tests and operations / Programmable / - Only if all these tests are successful, / Vertex Processing. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Fragment Tests and Operations 1/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - After fragments have been generated, they must go through the per-fragment / tests and operations / Programmable / - Only if all these tests are successful, / Vertex Processing. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Fragment Tests and Operations 1/2' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Fragment Tests and Operations 1/2' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Fragment Tests and Operations 1/2' into a causal sentence instead of repeating the slide title?

### Page 69 - Fragment Tests and Operations 2/2

Source cue: Fragment Pixel Ownership Scissor Alpha / Data Test Test Test / Depth Stencil / Framebuffer Dithering Blending / Test Test

Professor-style explanation: The slide 'Fragment Tests and Operations 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: Fragment Pixel Ownership Scissor Alpha / Data Test Test Test / Depth Stencil / Framebuffer Dithering Blending / Test Test. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Fragment Tests and Operations 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: Fragment Pixel Ownership Scissor Alpha / Data Test Test Test / Depth Stencil / Framebuffer Dithering Blending / Test Test. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Fragment Tests and Operations 2/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Fragment Tests and Operations 2/2'?

### Page 70 - Alpha Test

Source cue: - If framebuffer is an RGBA buffer, the alpha test can be performed / - The test must first be activated / glEnable(GL_ALPHA_TEST); / - The comparison function indicates which fragments survive the test / glAlphaFunc(func, value);

Professor-style explanation: The slide 'Alpha Test' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - If framebuffer is an RGBA buffer, the alpha test can be performed / - The test must first be activated / glEnable(GL_ALPHA_TEST); / - The comparison function indicates which fragments survive the test / glAlphaFunc(func, value). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Alpha Test. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - If framebuffer is an RGBA buffer, the alpha test can be performed / - The test must first be activated / glEnable(GL_ALPHA_TEST); / - The comparison function indicates which fragments survive the test / glAlphaFunc(func, value). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Alpha Test' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Alpha Test'?

### Page 71 - Stencil Test

Source cue: - Stencil Buffer / - Is a frame buffer component / - Is (indirectly) filled by drawing operations / - No special stencil drawing operations / - Stencil operation

Professor-style explanation: The slide 'Stencil Test' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Stencil Buffer / - Is a frame buffer component / - Is (indirectly) filled by drawing operations / - No special stencil drawing operations / - Stencil operation. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Stencil Test. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Stencil Buffer / - Is a frame buffer component / - Is (indirectly) filled by drawing operations / - No special stencil drawing operations / - Stencil operation. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Stencil Test' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Stencil Test'?

### Page 72 - Depth Test

Source cue: - If the framebuffer has a depth buffer, the depth test can be performed / - The test must first be activated / glEnable(GL_DEPTH_TEST); / - The comparison is made with the depth value already in the buffer / - The comparison function indicates which fragments survive the test

Professor-style explanation: The slide 'Depth Test' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - If the framebuffer has a depth buffer, the depth test can be performed / - The test must first be activated / glEnable(GL_DEPTH_TEST); / - The comparison is made with the depth value already in the buffer / - The comparison function indicates which fragments survive the test. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Depth Test. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - If the framebuffer has a depth buffer, the depth test can be performed / - The test must first be activated / glEnable(GL_DEPTH_TEST); / - The comparison is made with the depth value already in the buffer / - The comparison function indicates which fragments survive the test. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Depth Test' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Depth Test'?

### Page 73 - Image Composition and Mixture

Source cue: - Alpha values of the pixels / - control the combination of pixel values / - are specified as color components of color pixels / - P = [R, G, B, A], with R, G, B, A ∈ [0,1] / - Applications are manifold

Professor-style explanation: The slide 'Image Composition and Mixture' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Alpha values of the pixels / - control the combination of pixel values / - are specified as color components of color pixels / - P = [R, G, B, A], with R, G, B, A ∈ [0,1] / - Applications are manifold. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Image Composition and Mixture. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Alpha values of the pixels / - control the combination of pixel values / - are specified as color components of color pixels / - P = [R, G, B, A], with R, G, B, A ∈ [0,1] / - Applications are manifold. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Image Composition and Mixture' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Image Composition and Mixture' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Image Composition and Mixture' into a causal sentence instead of repeating the slide title?

### Page 74 - Blending Application

Source cue: - Example application for transparency: drawing with semi-transparent brush

Professor-style explanation: The slide 'Blending Application' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Example application for transparency: drawing with semi-transparent brush. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Blending Application. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Example application for transparency: drawing with semi-transparent brush. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Blending Application' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Blending Application' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Blending Application' into a causal sentence instead of repeating the slide title?

### Page 75 - Blending Process 1/2

Source cue: - Blending is an operation called per fragment / - Fragments are modified after rasterization, / but before writing to the framebuffer with a blending function / - Combination of a source fragment to be written with the destination pixel / in the frame buffer by using a blending function

Professor-style explanation: The slide 'Blending Process 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Blending is an operation called per fragment / - Fragments are modified after rasterization, / but before writing to the framebuffer with a blending function / - Combination of a source fragment to be written with the destination pixel / in the frame buffer by using a blending function. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Blending Process 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Blending is an operation called per fragment / - Fragments are modified after rasterization, / but before writing to the framebuffer with a blending function / - Combination of a source fragment to be written with the destination pixel / in the frame buffer by using a blending function. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Blending Process 1/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Blending Process 1/2'?

### Page 76 - Blending Process 2/2

Source cue: - Source factor: F / - Destination factor: F / - Source fragment: [P , P , P , P ] / s,r s,g s,b s,a / - Destination pixel: [P , P , P , P ]

Professor-style explanation: The slide 'Blending Process 2/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Source factor: F / - Destination factor: F / - Source fragment: [P , P , P , P ] / s,r s,g s,b s,a / - Destination pixel: [P , P , P , P ]. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Blending Process 2/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Source factor: F / - Destination factor: F / - Source fragment: [P , P , P , P ] / s,r s,g s,b s,a / - Destination pixel: [P , P , P , P ]. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Blending Process 2/2' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Blending Process 2/2' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Blending Process 2/2' into a causal sentence instead of repeating the slide title?

### Page 77 - Applying Blending

Source cue: - Switch on (or switch off) blending / - glEnable(GL_BLEND); / - glDisable(GL_BLEND); / - Defining Blending Factors / - glBlendFunc(srcFac, destFac);

Professor-style explanation: The slide 'Applying Blending' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Switch on (or switch off) blending / - glEnable(GL_BLEND); / - glDisable(GL_BLEND); / - Defining Blending Factors / - glBlendFunc(srcFac, destFac). The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Applying Blending. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Switch on (or switch off) blending / - glEnable(GL_BLEND); / - glDisable(GL_BLEND); / - Defining Blending Factors / - glBlendFunc(srcFac, destFac). The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Applying Blending' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Applying Blending' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Applying Blending' into a causal sentence instead of repeating the slide title?

### Page 78 - Blending Examples

Source cue: - Example 1: Copy source pixels and overwrite destination pixels / - glBlendFunc(GL_ONE, GL_ZERO); / - P = [P , P , P , P ] / blend s,r s,g s,b s,a / - Example 2: Alpha-based mixing of source pixels and destination pixels

Professor-style explanation: The slide 'Blending Examples' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Example 1: Copy source pixels and overwrite destination pixels / - glBlendFunc(GL_ONE, GL_ZERO); / - P = [P , P , P , P ] / blend s,r s,g s,b s,a / - Example 2: Alpha-based mixing of source pixels and destination pixels. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Blending Examples. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Example 1: Copy source pixels and overwrite destination pixels / - glBlendFunc(GL_ONE, GL_ZERO); / - P = [P , P , P , P ] / blend s,r s,g s,b s,a / - Example 2: Alpha-based mixing of source pixels and destination pixels. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Blending Examples' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Blending Examples' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Blending Examples' into a causal sentence instead of repeating the slide title?

### Page 79 - 2.6 Framebuffer

Source cue: Contains everything that is (in)visible on the screen

Professor-style explanation: The slide '2.6 Framebuffer' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: Contains everything that is (in)visible on the screen. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about 2.6 Framebuffer. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: Contains everything that is (in)visible on the screen. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for '2.6 Framebuffer' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2.6 Framebuffer'?

### Page 80 - Viewport

Source cue: - Rectangular area in pixel grid, set explicitly / - Rendering operations are limited to this area / - All primitives that are completely or partially outside / are clipped at the viewport area (clipping)

Professor-style explanation: The slide 'Viewport' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. The terms describe boundary decisions: - Rectangular area in pixel grid, set explicitly / - Rendering operations are limited to this area / - All primitives that are completely or partially outside / are clipped at the viewport area (clipping). A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion. For examination purposes, the important content is classification: inside, outside, crossing, intersection point, and the newly produced primitive segment or polygon.

Technical commentary: This slide is about Viewport. The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces. The terms describe boundary decisions: - Rectangular area in pixel grid, set explicitly / - Rendering operations are limited to this area / - All primitives that are completely or partially outside / are clipped at the viewport area (clipping). A primitive is classified against a clipping region, rejected if outside, preserved if inside, or cut at intersections if it crosses a boundary.

Why it matters: Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.

Exam-grade answer: A strong answer for 'Viewport' classifies geometry relative to the boundary, explains intersection creation, and names the geometry passed to rasterization.

Common trap: Do not describe clipping as only deletion; crossing primitives can be cut and replaced by new vertices or primitive pieces.

Check yourself: Can you decide what is accepted, rejected, or newly intersected in 'Viewport'?

### Page 81 - Framebuffer

Source cue: - Context-bound raster with a resolution and structure / specified by the application / - Physical realization on the GPU / - Logical subdivision / - Color memory

Professor-style explanation: The slide 'Framebuffer' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Context-bound raster with a resolution and structure / specified by the application / - Physical realization on the GPU / - Logical subdivision / - Color memory. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Framebuffer. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Context-bound raster with a resolution and structure / specified by the application / - Physical realization on the GPU / - Logical subdivision / - Color memory. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Framebuffer' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Framebuffer'?

### Page 82 - OpenGL Framebuffers 1/3

Source cue: - Typical OpenGL framebuffer configuration / 8bit Stencil Buffer / 32bit Depth Buffer / = 32bit Color Buffer

Professor-style explanation: The slide 'OpenGL Framebuffers 1/3' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Typical OpenGL framebuffer configuration / 8bit Stencil Buffer / 32bit Depth Buffer / = 32bit Color Buffer. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL Framebuffers 1/3. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Typical OpenGL framebuffer configuration / 8bit Stencil Buffer / 32bit Depth Buffer / = 32bit Color Buffer. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL Framebuffers 1/3' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Framebuffers 1/3'?

### Page 83 - OpenGL Framebuffers 2/3

Source cue: - All buffers of a frame buffer have the same grid size / - Number of bitplanes per buffer can be configured individually / - Individual buffers are directly supported by the hardware / - Buffer identifier / - GL_COLOR_BUFFER_BIT

Professor-style explanation: The slide 'OpenGL Framebuffers 2/3' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - All buffers of a frame buffer have the same grid size / - Number of bitplanes per buffer can be configured individually / - Individual buffers are directly supported by the hardware / - Buffer identifier / - GL_COLOR_BUFFER_BIT. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about OpenGL Framebuffers 2/3. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - All buffers of a frame buffer have the same grid size / - Number of bitplanes per buffer can be configured individually / - Individual buffers are directly supported by the hardware / - Buffer identifier / - GL_COLOR_BUFFER_BIT. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'OpenGL Framebuffers 2/3' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Framebuffers 2/3'?

### Page 84 - OpenGL Framebuffers 3/3

Source cue: - Delete a buffer / glClear(GLbitfield mask); / - Set the initialization color for the color buffer / glClearColor(1.0,1.0,1.0,1.0); / glClear(GL_COLOR_BUFFER_BIT);

Professor-style explanation: The outline 'OpenGL Framebuffers 3/3' gives the lecture its internal logic. The listed topics are the objects that will be connected during the chapter: first the problem space, then the mathematical or algorithmic tools, then the implementation consequences. The listed entries form a dependency order: - Delete a buffer / glClear(GLbitfield mask); / - Set the initialization color for the color buffer / glClearColor(1.0,1.0,1.0,1.0); / glClear(GL_COLOR_BUFFER_BIT). Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary. The order matters because later items rely on earlier definitions. For example, an OpenGL mechanism is much easier to understand once the corresponding pipeline object or mathematical operation has already been introduced. The outline is therefore a compact dependency graph of the lecture rather than a collection of isolated labels. For examination purposes, the important content is the dependency structure: which concept introduces the vocabulary, which later algorithm uses it, and which implementation problem it solves.

Technical commentary: This slide is about OpenGL Framebuffers 3/3. The listed items define the lecture sequence: the topic begins with a problem statement, introduces the required objects or algorithms, and then connects them to rendering or implementation consequences. The listed entries form a dependency order: - Delete a buffer / glClear(GLbitfield mask); / - Set the initialization color for the color buffer / glClearColor(1.0,1.0,1.0,1.0); / glClear(GL_COLOR_BUFFER_BIT). Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary.

Why it matters: Outlines tell you the dependency order. They are the safest way to avoid learning isolated bullet points.

Exam-grade answer: A strong answer for 'OpenGL Framebuffers 3/3' names the topics in order and explains at least one dependency between an earlier item and a later item.

Common trap: Do not memorize 'OpenGL Framebuffers 3/3' as a list of headings only; the exam-relevant part is how the headings depend on each other.

Check yourself: Can you explain where 'OpenGL Framebuffers 3/3' fits in the lecture order and what later section depends on it?

### Page 85 - Double Buffering

Source cue: - Use of two color buffers to avoid flicker effects / - Image buildup takes place in the background (back buffer) / - Visible image is independent of this (front buffer) / Rendering / Process

Professor-style explanation: The slide 'Double Buffering' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Use of two color buffers to avoid flicker effects / - Image buildup takes place in the background (back buffer) / - Visible image is independent of this (front buffer) / Rendering / Process. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Double Buffering. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Use of two color buffers to avoid flicker effects / - Image buildup takes place in the background (back buffer) / - Visible image is independent of this (front buffer) / Rendering / Process. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Double Buffering' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Double Buffering'?

### Page 86 - 2.7 Pixel-based Rendering

Source cue: Direct pixel processing without involving 3D models

Professor-style explanation: The slide '2.7 Pixel-based Rendering' explains raster images as concrete stored data. A raster image is a rectangular grid of pixels. Each pixel stores one or more channel values, such as red, green, blue, and sometimes alpha. Color depth tells us how many bits are available per pixel or per channel, and that immediately determines both the number of representable colors and the memory footprint of the image. The numerical values belong to one memory calculation: Direct pixel processing without involving 3D models. Resolution gives the number of pixels, color depth gives bits per pixel, and their product gives storage and bandwidth cost. The object relation is pixel count, bits per pixel, color range, and memory size. This is why a simple image-resolution question is also a performance question: more pixels and more bits mean more memory traffic, more storage, and more work for display or image-processing operations. For examination purposes, the important content is the chain width x height -> pixel count -> bits per pixel -> memory size; this chain also explains bandwidth and performance pressure.

Technical commentary: This slide is about 2.7 Pixel-based Rendering. The slide describes image data as discrete samples: pixels, color channels, bit depth, memory layout, and the amount of storage needed for a raster image. The numerical values belong to one memory calculation: Direct pixel processing without involving 3D models. Resolution gives the number of pixels, color depth gives bits per pixel, and their product gives storage and bandwidth cost.

Why it matters: Pixel-data slides connect visual output to memory size, bandwidth, precision, and image-processing cost.

Exam-grade answer: A strong answer for '2.7 Pixel-based Rendering' includes the formula relation width x height x bits per pixel, distinguishes bits from bytes, and links larger images to memory bandwidth.

Common trap: Do not confuse bits with bytes in '2.7 Pixel-based Rendering', and do not ignore that alpha or higher precision changes memory size.

Check yourself: Can you compute or explain the pixel count, color depth, or memory relation in '2.7 Pixel-based Rendering'?

### Page 87 - Pixel-based Rendering Operations

Source cue: - Generally / - Read and write operations for various image data formats, / usually as an external library (e.g., DevIl) / - Conversions between image data types / - In OpenGL done with framebuffer objects

Professor-style explanation: The slide 'Pixel-based Rendering Operations' explains raster images as concrete stored data. A raster image is a rectangular grid of pixels. Each pixel stores one or more channel values, such as red, green, blue, and sometimes alpha. Color depth tells us how many bits are available per pixel or per channel, and that immediately determines both the number of representable colors and the memory footprint of the image. The numerical values belong to one memory calculation: - Generally / - Read and write operations for various image data formats, / usually as an external library (e.g., DevIl) / - Conversions between image data types / - In OpenGL done with framebuffer objects. Resolution gives the number of pixels, color depth gives bits per pixel, and their product gives storage and bandwidth cost. The object relation is pixel count, bits per pixel, color range, and memory size. This is why a simple image-resolution question is also a performance question: more pixels and more bits mean more memory traffic, more storage, and more work for display or image-processing operations. For examination purposes, the important content is the chain width x height -> pixel count -> bits per pixel -> memory size; this chain also explains bandwidth and performance pressure.

Technical commentary: This slide is about Pixel-based Rendering Operations. The slide describes image data as discrete samples: pixels, color channels, bit depth, memory layout, and the amount of storage needed for a raster image. The numerical values belong to one memory calculation: - Generally / - Read and write operations for various image data formats, / usually as an external library (e.g., DevIl) / - Conversions between image data types / - In OpenGL done with framebuffer objects. Resolution gives the number of pixels, color depth gives bits per pixel, and their product gives storage and bandwidth cost.

Why it matters: Pixel-data slides connect visual output to memory size, bandwidth, precision, and image-processing cost.

Exam-grade answer: A strong answer for 'Pixel-based Rendering Operations' includes the formula relation width x height x bits per pixel, distinguishes bits from bytes, and links larger images to memory bandwidth.

Common trap: Do not confuse bits with bytes in 'Pixel-based Rendering Operations', and do not ignore that alpha or higher precision changes memory size.

Check yourself: Can you compute or explain the pixel count, color depth, or memory relation in 'Pixel-based Rendering Operations'?

### Page 88 - Image Operations

Source cue: - Rendering image data with OpenGL / Copy Pixel Data / Draw/Read / Pixel / Geometry

Professor-style explanation: The slide 'Image Operations' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Rendering image data with OpenGL / Copy Pixel Data / Draw/Read / Pixel / Geometry. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Image Operations. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Rendering image data with OpenGL / Copy Pixel Data / Draw/Read / Pixel / Geometry. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Image Operations' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Image Operations'?

### Page 89 - Write Pixels into Framebuffer

Source cue: - glDrawPixels(x, y, width, height, format, type, pixels); / - Example / // 64x64 array with rgb components / GLubyte img[64][64][3]; / void draw() {

Professor-style explanation: The slide 'Write Pixels into Framebuffer' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - glDrawPixels(x, y, width, height, format, type, pixels); / - Example / // 64x64 array with rgb components / GLubyte img[64][64][3]; / void draw() {. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Write Pixels into Framebuffer. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - glDrawPixels(x, y, width, height, format, type, pixels); / - Example / // 64x64 array with rgb components / GLubyte img[64][64][3]; / void draw() {. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Write Pixels into Framebuffer' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Write Pixels into Framebuffer'?

### Page 90 - Read Pixels from Framebuffer

Source cue: - glReadPixels(x, y, width, height, format, type, pixels); / - Example / GLubyte* img = 0; / int width, height; // canvas size / void snapshot() {

Professor-style explanation: The slide 'Read Pixels from Framebuffer' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - glReadPixels(x, y, width, height, format, type, pixels); / - Example / GLubyte* img = 0; / int width, height; // canvas size / void snapshot() {. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Read Pixels from Framebuffer. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - glReadPixels(x, y, width, height, format, type, pixels); / - Example / GLubyte* img = 0; / int width, height; // canvas size / void snapshot() {. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Read Pixels from Framebuffer' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Read Pixels from Framebuffer'?

### Page 91 - Formats & Data Types

Source cue: - Format information for pixel array operations / - GL_RGB - red-green-blue values of the frame buffer (FB) / - GL_RED - red values of the FB / - GL_ALPHA - transparency values of the FB / - GL_RGBA - red-Green-Blue-Alpha values of the FB

Professor-style explanation: The slide 'Formats & Data Types' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: - Format information for pixel array operations / - GL_RGB - red-green-blue values of the frame buffer (FB) / - GL_RED - red values of the FB / - GL_ALPHA - transparency values of the FB / - GL_RGBA - red-Green-Blue-Alpha values of the FB. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Formats & Data Types. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: - Format information for pixel array operations / - GL_RGB - red-green-blue values of the frame buffer (FB) / - GL_RED - red values of the FB / - GL_ALPHA - transparency values of the FB / - GL_RGBA - red-Green-Blue-Alpha values of the FB. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Formats & Data Types' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Formats & Data Types'?

### Page 92 - coordinate systems in the geometry stage

Source cue: - Rendering pipeline consist of geometry stage and rasterization stage / - Geometric primitives (mostly triangles) are transformed through different / coordinate systems in the geometry stage / - Rasterization results in fragments, which are pixel predecessors / - Fragments have to endure a sequence of tests in the rasterization stage, in

Professor-style explanation: The slide 'coordinate systems in the geometry stage' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. The terms are successive representations in object-based rendering: - Rendering pipeline consist of geometry stage and rasterization stage / - Geometric primitives (mostly triangles) are transformed through different / coordinate systems in the geometry stage / - Rasterization results in fragments, which are pixel predecessors / - Fragments have to endure a sequence of tests in the rasterization stage, in. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter. For examination purposes, the important content is the representation change at each stage: model data, vertices, primitives, fragments, fragment tests, and final framebuffer updates.

Technical commentary: This slide is about coordinate systems in the geometry stage. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. The terms are successive representations in object-based rendering: - Rendering pipeline consist of geometry stage and rasterization stage / - Geometric primitives (mostly triangles) are transformed through different / coordinate systems in the geometry stage / - Rasterization results in fragments, which are pixel predecessors / - Fragments have to endure a sequence of tests in the rasterization stage, in. Scene data becomes vertices, vertices become primitives, primitives become fragments, and only passing fragments update pixels.

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Exam-grade answer: A strong answer for 'coordinate systems in the geometry stage' states what representation enters the stage, what representation leaves it, and which later stage depends on that output.

Common trap: Do not collapse 'coordinate systems in the geometry stage' into 'the GPU draws it'; name the intermediate representations because that is where most errors and exam distinctions appear.

Check yourself: Can you name the input and output representation for 'coordinate systems in the geometry stage' in the rendering pipeline?

### Page 93 - Literature and other sources used in this chapter

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Literature and other sources used in this chapter' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Literature and other sources used in this chapter. The slide lists source material or chapter references that support the technical content and give names for further reading. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Reference slides provide the source trail for definitions, algorithms, and deeper explanations.

Exam-grade answer: A strong answer for 'Literature and other sources used in this chapter' identifies what kind of source is listed and which course concept or algorithm that source supports.

Common trap: Do not skip 'Literature and other sources used in this chapter' if it names a standard algorithm or source that defines terminology used later in the chapter.

Check yourself: Can you identify which source or topic 'Literature and other sources used in this chapter' points to for deeper study?

### Page 94 - Guide: The Official Guide to Learning OpenGL

Source cue: - Text Books / - D. Shreiner, G. Sellers, J. Kessenich, B. Licea-Kane: OpenGL Programming / Guide: The Official Guide to Learning OpenGL / (8th Edition), Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer

Professor-style explanation: The slide 'Guide: The Official Guide to Learning OpenGL' collects the source material behind the chapter. References are not rendering objects themselves, but they identify the books, papers, or external resources from which the lecture's terminology and algorithms are drawn. The listed sources support the chapter content: - Text Books / - D. Shreiner, G. Sellers, J. Kessenich, B. Licea-Kane: OpenGL Programming / Guide: The Official Guide to Learning OpenGL / (8th Edition), Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer. They point to the books, papers, or resources behind the definitions and algorithms used in the lecture. In practical terms, a reference slide marks the boundary of the chapter and tells us where the formal definitions, derivations, or extended examples can be found if a topic needs more depth than the lecture slides provide. For examination purposes, the important content is source attribution and vocabulary: references tell where precise definitions and standard algorithms come from.

Technical commentary: This slide is about Guide: The Official Guide to Learning OpenGL. The slide lists source material or chapter references that support the technical content and give names for further reading. The listed sources support the chapter content: - Text Books / - D. Shreiner, G. Sellers, J. Kessenich, B. Licea-Kane: OpenGL Programming / Guide: The Official Guide to Learning OpenGL / (8th Edition), Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer. They point to the books, papers, or resources behind the definitions and algorithms used in the lecture.

Why it matters: Reference slides provide the source trail for definitions, algorithms, and deeper explanations.

Exam-grade answer: A strong answer for 'Guide: The Official Guide to Learning OpenGL' identifies what kind of source is listed and which course concept or algorithm that source supports.

Common trap: Do not skip 'Guide: The Official Guide to Learning OpenGL' if it names a standard algorithm or source that defines terminology used later in the chapter.

Check yourself: Can you identify which source or topic 'Guide: The Official Guide to Learning OpenGL' points to for deeper study?

## 02.1 Rendering Process

Source location: Section 2.1

### Commentary

Object-based rendering starts with scene objects represented as primitives. The pipeline transforms vertices, assembles primitives, rasterizes them into fragments, and lets only some fragments become pixels. The important detail is that the representation changes at every stage.

The application stage prepares data and state. The geometry stage handles positions and primitives. The rasterization stage creates fragments and applies fragment operations. This separation helps you explain both theory questions and black-screen OpenGL bugs.

### Mental Model

Vertices become primitives, primitives become fragments, and fragments compete to become pixel updates.

### Check Yourself

What is the difference between a fragment and a final pixel?

## 02.2 OpenGL Overview

Source location: Section 2.2

### Commentary

OpenGL is an API for controlling a graphics pipeline. It is not a renderer by itself in the sense of a single command that understands your scene. You create a context, provide buffers, set state, compile shaders, bind objects, and issue draw calls.

Modern OpenGL is stateful and shader-based. Many errors happen because the programmer assumes that a later call carries more information than it really does. The GPU uses the currently bound objects and current state at draw time.

### Mental Model

OpenGL draw calls consume the state machine as it exists right now.

### Check Yourself

Why can binding the wrong vertex array or shader program produce a valid draw call with wrong output?

## 02.3 OpenGL Rendering

Source location: Section 2.3

### Commentary

Older OpenGL exposed a fixed-function style where many transformations and lighting choices were configured through predefined calls. Modern OpenGL expects you to write shader programs and explicitly manage data flow.

This is not just historical trivia. It explains why shader code, vertex attributes, uniforms, and buffer objects are central in the exercises. If the shader expects an attribute and the vertex layout does not provide it, the pipeline has no magic fallback.

### Mental Model

Modern OpenGL makes the data path explicit; that gives control but also creates responsibility.

### Check Yourself

Which data usually goes into vertex attributes, and which data usually goes into uniforms?

## 02.4 OpenGL Rendering Pipeline

Source location: Section 2.4

### Commentary

The vertex shader runs per vertex and usually outputs clip-space position plus attributes for later interpolation. Primitive assembly groups vertices into points, lines, or triangles. Clipping handles geometry outside the view volume. Rasterization creates fragments.

The fragment shader computes candidate fragment output, often using interpolated attributes, uniforms, and textures. After that, tests and operations such as depth testing, stencil testing, blending, and masking decide what reaches the framebuffer.

### Mental Model

Programmable shaders compute values; fixed pipeline stages decide coverage, interpolation, tests, and output rules.

### Check Yourself

If your geometry appears in wireframe but colors are wrong, which stages become suspicious?

## 02.5 Fragment Tests, Framebuffer, and Pixel-Based Rendering

Source location: Sections 2.5-2.7

### Commentary

Fragment tests are the gatekeepers after shading. A fragment can have a perfectly valid color and still fail because depth, stencil, scissor, masking, or blending state prevents a visible update. This is why final pixels are a subset of generated fragments.

The framebuffer stores the final render targets: color buffers, depth buffers, stencil buffers, or custom attachments. Pixel-based rendering starts from image data instead of geometric primitives, which is useful for image processing but conceptually different from the object-to-pixel pipeline.

### Mental Model

The framebuffer is the destination; fragment operations are the rules for writing into it.

### Check Yourself

Why can two fragments with different colors produce only one visible pixel color?

## End-of-Lecture Summary

If you remember only one thing from Lecture 02, remember this: This lecture turns the vague idea of rendering into a concrete sequence. It is the most important debugging map in the course: if an image is wrong, the pipeline tells you where the error could have entered.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
