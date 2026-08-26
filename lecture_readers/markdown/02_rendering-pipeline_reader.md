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

Professor-style explanation: The slide 'Visual or title slide' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. On the slide, the concrete items are: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail.

Technical commentary: This slide is about Visual or title slide. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Visual or title slide' into a causal sentence instead of repeating the slide title?

### Page 2 - Object-based Rendering

Source cue: - Image generation done through rasterization / - Scene objects formed by 3D models (primitives) / are transformed through successive coordinate systems / - Primitives are rasterized into fragments, which are pixel predecessors / - A subset of the fragments becomes pixels

Professor-style explanation: The slide 'Object-based Rendering' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. On the slide, the concrete items are: - Image generation done through rasterization / - Scene objects formed by 3D models (primitives) / are transformed through successive coordinate systems / - Primitives are rasterized into fragments, which are pixel predecessors / - A subset of the fragments becomes pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter.

Technical commentary: This slide is about Object-based Rendering. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. Concrete items shown: - Image generation done through rasterization / - Scene objects formed by 3D models (primitives) / are transformed through successive coordinate systems / - Primitives are rasterized into fragments, which are pixel predecessors / - A subset of the fragments becomes pixels

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'Object-based Rendering' in the rendering pipeline?

### Page 3 - 2.1 Rendering Process

Source cue: 2.2 OpenGL Overview / 2.3 OpenGL Rendering / 2.4 OpenGL Rendering Pipeline / 2.5 Fragment Tests and Operations / 2.6 Framebuffer

Professor-style explanation: The slide '2.1 Rendering Process' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. On the slide, the concrete items are: 2.2 OpenGL Overview / 2.3 OpenGL Rendering / 2.4 OpenGL Rendering Pipeline / 2.5 Fragment Tests and Operations / 2.6 Framebuffer. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter.

Technical commentary: This slide is about 2.1 Rendering Process. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. Concrete items shown: 2.2 OpenGL Overview / 2.3 OpenGL Rendering / 2.4 OpenGL Rendering Pipeline / 2.5 Fragment Tests and Operations / 2.6 Framebuffer

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for '2.1 Rendering Process' in the rendering pipeline?

### Page 4 - 2.1 Rendering Process

Source cue: From 3D models over fragments to pixels

Professor-style explanation: The slide '2.1 Rendering Process' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. On the slide, the concrete items are: From 3D models over fragments to pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter.

Technical commentary: This slide is about 2.1 Rendering Process. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. Concrete items shown: From 3D models over fragments to pixels

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for '2.1 Rendering Process' in the rendering pipeline?

### Page 5 - Geometry-based Rendering 1/2

Source cue: CPU Application GPU Rendering Display Hardware / Rendering / 3D Model Framebuffer / Process / Video

Professor-style explanation: The slide 'Geometry-based Rendering 1/2' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. On the slide, the concrete items are: CPU Application GPU Rendering Display Hardware / Rendering / 3D Model Framebuffer / Process / Video. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter.

Technical commentary: This slide is about Geometry-based Rendering 1/2. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. Concrete items shown: CPU Application GPU Rendering Display Hardware / Rendering / 3D Model Framebuffer / Process / Video

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'Geometry-based Rendering 1/2' in the rendering pipeline?

### Page 6 - Geometry-based Rendering 2/2

Source cue: - The rendering process is realized through the rendering pipeline / - Renders 3D models to 2D images / - Conceptually, the rendering pipeline consists of two GPU stages / - Geometry stage – processes geometric primitives / - Rasterization stage – processes fragments and pixels

Professor-style explanation: The slide 'Geometry-based Rendering 2/2' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. On the slide, the concrete items are: - The rendering process is realized through the rendering pipeline / - Renders 3D models to 2D images / - Conceptually, the rendering pipeline consists of two GPU stages / - Geometry stage – processes geometric primitives / - Rasterization stage – processes fragments and pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter.

Technical commentary: This slide is about Geometry-based Rendering 2/2. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. Concrete items shown: - The rendering process is realized through the rendering pipeline / - Renders 3D models to 2D images / - Conceptually, the rendering pipeline consists of two GPU stages / - Geometry stage – processes geometric primitives / - Rasterization stage – processes fragments and pixels

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'Geometry-based Rendering 2/2' in the rendering pipeline?

### Page 7 - Application Stage

Source cue: - Specification of the model elements and the scene / as well as interaction capabilities / - Scene modeling: arrangement and attribution of the scene objects / - Calculation of animation paths / - Collision detection

Professor-style explanation: The slide 'Application Stage' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. On the slide, the concrete items are: - Specification of the model elements and the scene / as well as interaction capabilities / - Scene modeling: arrangement and attribution of the scene objects / - Calculation of animation paths / - Collision detection. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Application Stage. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: - Specification of the model elements and the scene / as well as interaction capabilities / - Scene modeling: arrangement and attribution of the scene objects / - Calculation of animation paths / - Collision detection

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Application Stage' into a causal sentence instead of repeating the slide title?

### Page 8 - Geometry Stage

Source cue: x x / - Geometric 3D transformation / Model Coordinate System World Coordinate System / - Alignment of individual scene objects in the overall scene / - Basic transformations: translation, scaling, rotation

Professor-style explanation: The slide 'Geometry Stage' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. On the slide, the concrete items are: x x / - Geometric 3D transformation / Model Coordinate System World Coordinate System / - Alignment of individual scene objects in the overall scene / - Basic transformations: translation, scaling, rotation. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear.

Technical commentary: This slide is about Geometry Stage. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. Concrete items shown: x x / - Geometric 3D transformation / Model Coordinate System World Coordinate System / - Alignment of individual scene objects in the overall scene / - Basic transformations: translation, scaling, rotation

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Geometry Stage'?

### Page 9 - Rasterization Stage

Source cue: - Conversion of primitives into fragments (rasterization) / - Discretization takes place in relation to a target grid / - Rasterization algorithms optimized for certain primitives / (e.g., lines, triangles) / - After rasterization per-fragment tests are performed

Professor-style explanation: The slide 'Rasterization Stage' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. On the slide, the concrete items are: - Conversion of primitives into fragments (rasterization) / - Discretization takes place in relation to a target grid / - Rasterization algorithms optimized for certain primitives / (e.g., lines, triangles) / - After rasterization per-fragment tests are performed. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations.

Technical commentary: This slide is about Rasterization Stage. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: - Conversion of primitives into fragments (rasterization) / - Discretization takes place in relation to a target grid / - Rasterization algorithms optimized for certain primitives / (e.g., lines, triangles) / - After rasterization per-fragment tests are performed

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Rasterization Stage'?

### Page 10 - 2.2 OpenGL Overview

Source cue: Library for real-time computer graphics

Professor-style explanation: The slide '2.2 OpenGL Overview' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: Library for real-time computer graphics. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about 2.2 OpenGL Overview. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: Library for real-time computer graphics

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2.2 OpenGL Overview'?

### Page 11 - OpenGL History

Source cue: - Unified graphics software interface was missing / as knowledge channeled into proprietary software packages / - HP's starbase / - SGI's Graphics Library (GL) / - Some standardization efforts existed

Professor-style explanation: The slide 'OpenGL History' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Unified graphics software interface was missing / as knowledge channeled into proprietary software packages / - HP's starbase / - SGI's Graphics Library (GL) / - Some standardization efforts existed. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about OpenGL History. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Unified graphics software interface was missing / as knowledge channeled into proprietary software packages / - HP's starbase / - SGI's Graphics Library (GL) / - Some standardization efforts existed

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL History'?

### Page 12 - OpenGL

Source cue: - OpenGL (Open Graphics Library) / - Platform independent 2D and 3D graphics API / - API specification is provided by the Khronos Group / - Technical implementation / - Rendering pipeline consisting of static and programmable pipeline stages

Professor-style explanation: The slide 'OpenGL' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. On the slide, the concrete items are: - OpenGL (Open Graphics Library) / - Platform independent 2D and 3D graphics API / - API specification is provided by the Khronos Group / - Technical implementation / - Rendering pipeline consisting of static and programmable pipeline stages. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter.

Technical commentary: This slide is about OpenGL. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. Concrete items shown: - OpenGL (Open Graphics Library) / - Platform independent 2D and 3D graphics API / - API specification is provided by the Khronos Group / - Technical implementation / - Rendering pipeline consisting of static and programmable pipeline stages

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'OpenGL' in the rendering pipeline?

### Page 13 - OpenGL vs. Vulkan

Source cue: - How about Vulkan? / - More modern than OpenGL / - Designed for high performance and low-level GPU control / - Better suited for complex, large-scale rendering engines / - Vulkan also harder to learn and requires more setup/code

Professor-style explanation: The slide 'OpenGL vs. Vulkan' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - How about Vulkan? / - More modern than OpenGL / - Designed for high performance and low-level GPU control / - Better suited for complex, large-scale rendering engines / - Vulkan also harder to learn and requires more setup/code. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about OpenGL vs. Vulkan. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - How about Vulkan? / - More modern than OpenGL / - Designed for high performance and low-level GPU control / - Better suited for complex, large-scale rendering engines / - Vulkan also harder to learn and requires more setup/code

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL vs. Vulkan'?

### Page 14 - OpenGL Libraries

Source cue: - Different tastes of OpenGL / - OpenGL / - OpenGL ES - limited version for embedded systems / - WebGL - Javascript connection for Web Development / (functionality similar to OpenGL ES)

Professor-style explanation: The slide 'OpenGL Libraries' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Different tastes of OpenGL / - OpenGL / - OpenGL ES - limited version for embedded systems / - WebGL - Javascript connection for Web Development / (functionality similar to OpenGL ES). The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about OpenGL Libraries. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Different tastes of OpenGL / - OpenGL / - OpenGL ES - limited version for embedded systems / - WebGL - Javascript connection for Web Development / (functionality similar to OpenGL ES)

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Libraries'?

### Page 15 - OpenGL Functionality

Source cue: - Functional API / - Objects, scenes and images are described by a sequence of commands / (functional approach, low-level) / - Contrast: scene or object description (declarative approach, high-level) / - OpenGL context

Professor-style explanation: The slide 'OpenGL Functionality' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Functional API / - Objects, scenes and images are described by a sequence of commands / (functional approach, low-level) / - Contrast: scene or object description (declarative approach, high-level) / - OpenGL context. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about OpenGL Functionality. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Functional API / - Objects, scenes and images are described by a sequence of commands / (functional approach, low-level) / - Contrast: scene or object description (declarative approach, high-level) / - OpenGL context

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Functionality'?

### Page 16 - OpenGL Context

Source cue: - Context is created and modified by the application, / and contains all the state variables of the OpenGL engine / - Any number of contexts per application possible, / but at most one active context per application / - Context is generally tied to an output window

Professor-style explanation: The slide 'OpenGL Context' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Context is created and modified by the application, / and contains all the state variables of the OpenGL engine / - Any number of contexts per application possible, / but at most one active context per application / - Context is generally tied to an output window. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about OpenGL Context. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Context is created and modified by the application, / and contains all the state variables of the OpenGL engine / - Any number of contexts per application possible, / but at most one active context per application / - Context is generally tied to an output window

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Context'?

### Page 17 - OpenGL Rendering Process

Source cue: - Initiation from the developer's perspective / - Creation of the output window / - Creation of the context / - Specification of the scene geometry / - Uploading of the scene geometry to the GPU

Professor-style explanation: The slide 'OpenGL Rendering Process' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. On the slide, the concrete items are: - Initiation from the developer's perspective / - Creation of the output window / - Creation of the context / - Specification of the scene geometry / - Uploading of the scene geometry to the GPU. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter.

Technical commentary: This slide is about OpenGL Rendering Process. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. Concrete items shown: - Initiation from the developer's perspective / - Creation of the output window / - Creation of the context / - Specification of the scene geometry / - Uploading of the scene geometry to the GPU

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'OpenGL Rendering Process' in the rendering pipeline?

### Page 18 - Window Creation with GLFW 1/2

Source cue: #include <GLFW/glfw3.h> / #include <stdlib.h> / #include <stdio.h> / static void error_callback(int error, const char* description) { / fputs(description, stderr);

Professor-style explanation: The slide 'Window Creation with GLFW 1/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. On the slide, the concrete items are: #include <GLFW/glfw3.h> / #include <stdlib.h> / #include <stdio.h> / static void error_callback(int error, const char* description) { / fputs(description, stderr). The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Window Creation with GLFW 1/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: #include <GLFW/glfw3.h> / #include <stdlib.h> / #include <stdio.h> / static void error_callback(int error, const char* description) { / fputs(description, stderr);

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Window Creation with GLFW 1/2' into a causal sentence instead of repeating the slide title?

### Page 19 - Window Creation with GLFW 2/2

Source cue: int main(void){ / GLFWwindow* window; / glfwSetErrorCallback(error_callback); / if (!glfwInit()) exit(EXIT_FAILURE); / window = glfwCreateWindow(640, 480, "Simple example", NULL, NULL);

Professor-style explanation: The slide 'Window Creation with GLFW 2/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. On the slide, the concrete items are: int main(void){ / GLFWwindow* window; / glfwSetErrorCallback(error_callback); / if (!glfwInit()) exit(EXIT_FAILURE); / window = glfwCreateWindow(640, 480, "Simple example", NULL, NULL). The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Window Creation with GLFW 2/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: int main(void){ / GLFWwindow* window; / glfwSetErrorCallback(error_callback); / if (!glfwInit()) exit(EXIT_FAILURE); / window = glfwCreateWindow(640, 480, "Simple example", NULL, NULL);

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Window Creation with GLFW 2/2' into a causal sentence instead of repeating the slide title?

### Page 20 - OpenGL Naming Conventions

Source cue: - Function-Prefix "gl" / - glClear, ... / - Constant-Prefix "GL" / - GL_POLYGON, GL_LINES, ... / - Parameter types are explicitly encoded in function names

Professor-style explanation: The slide 'OpenGL Naming Conventions' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Function-Prefix "gl" / - glClear, ... / - Constant-Prefix "GL" / - GL_POLYGON, GL_LINES, ... / - Parameter types are explicitly encoded in function names. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about OpenGL Naming Conventions. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Function-Prefix "gl" / - glClear, ... / - Constant-Prefix "GL" / - GL_POLYGON, GL_LINES, ... / - Parameter types are explicitly encoded in function names

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Naming Conventions'?

### Page 21 - 2.3 OpenGL Rendering

Source cue: Transfer of 3D models to the GPU

Professor-style explanation: The slide '2.3 OpenGL Rendering' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: Transfer of 3D models to the GPU. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about 2.3 OpenGL Rendering. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: Transfer of 3D models to the GPU

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2.3 OpenGL Rendering'?

### Page 22 - OpenGL Rendering (until V2.1)

Source cue: - Rendering is done through Immediate Mode / void renderScene() { / glColor3f(0.0f, 1.0f, 0.0f); // drawing color becomes green / glBegin(GL_POLYGON); // begin primitive / glVertex2f(-0.5f,-0.5f); // 1. vertex

Professor-style explanation: The slide 'OpenGL Rendering (until V2.1)' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Rendering is done through Immediate Mode / void renderScene() { / glColor3f(0.0f, 1.0f, 0.0f); // drawing color becomes green / glBegin(GL_POLYGON); // begin primitive / glVertex2f(-0.5f,-0.5f); // 1. vertex. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about OpenGL Rendering (until V2.1). The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Rendering is done through Immediate Mode / void renderScene() { / glColor3f(0.0f, 1.0f, 0.0f); // drawing color becomes green / glBegin(GL_POLYGON); // begin primitive / glVertex2f(-0.5f,-0.5f); // 1. vertex

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Rendering (until V2.1)'?

### Page 23 - OpenGL Rendering (since V3.0)

Source cue: - Using Vertex Array Objects (VAOs) / - Vertex specification in CPU memory / - Vertex data transfer from CPU to GPU / - Memory layout description of the vertex data / - Number of vertices, number of components (x, y, z, ...)

Professor-style explanation: The slide 'OpenGL Rendering (since V3.0)' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Using Vertex Array Objects (VAOs) / - Vertex specification in CPU memory / - Vertex data transfer from CPU to GPU / - Memory layout description of the vertex data / - Number of vertices, number of components (x, y, z, ...). The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about OpenGL Rendering (since V3.0). The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Using Vertex Array Objects (VAOs) / - Vertex specification in CPU memory / - Vertex data transfer from CPU to GPU / - Memory layout description of the vertex data / - Number of vertices, number of components (x, y, z, ...)

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Rendering (since V3.0)'?

### Page 24 - 1. Vertex Specification

Source cue: - Vertex data is specified as a C array / // vertices of two triangles / GLfloat vertices[6][2] = { // 6 vertices with two components each (x,y) / {0.0, 1.0}, {1.0, 1.0}, {1.0, 0.0}, // 1. triangle / {0.5, 0.5}, {1.0, 0.3}, {0.7, 1.0} // 2. triangle

Professor-style explanation: The slide '1. Vertex Specification' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. On the slide, the concrete items are: - Vertex data is specified as a C array / // vertices of two triangles / GLfloat vertices[6][2] = { // 6 vertices with two components each (x,y) / {0.0, 1.0}, {1.0, 1.0}, {1.0, 0.0}, // 1. triangle / {0.5, 0.5}, {1.0, 0.3}, {0.7, 1.0} // 2. triangle. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations.

Technical commentary: This slide is about 1. Vertex Specification. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: - Vertex data is specified as a C array / // vertices of two triangles / GLfloat vertices[6][2] = { // 6 vertices with two components each (x,y) / {0.0, 1.0}, {1.0, 1.0}, {1.0, 0.0}, // 1. triangle / {0.5, 0.5}, {1.0, 0.3}, {0.7, 1.0} // 2. triangle

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by '1. Vertex Specification'?

### Page 25 - 2. Vertex Data Transfer

Source cue: - VBO allocation and data transfer via / - glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW); / - data – address in main memory (i.e., vertices or &vertices[0]) / - size – size of data in number of bytes / (i.e. sizeof(vertices) or numVertices*sizeof(GLfloat)*2)

Professor-style explanation: The slide '2. Vertex Data Transfer' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - VBO allocation and data transfer via / - glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW); / - data – address in main memory (i.e., vertices or &vertices[0]) / - size – size of data in number of bytes / (i.e. sizeof(vertices) or numVertices*sizeof(GLfloat)*2). The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about 2. Vertex Data Transfer. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - VBO allocation and data transfer via / - glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW); / - data – address in main memory (i.e., vertices or &vertices[0]) / - size – size of data in number of bytes / (i.e. sizeof(vertices) or numVertices*sizeof(GLfloat)*2)

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2. Vertex Data Transfer'?

### Page 26 - 3. Memory Layout Description

Source cue: - Memory layout is described by the following function / - glVertexAttribPointer(attribIndex, size, type, normalized, stride, offset); / - attribIndex – attribute number (0 for position, later more ...) / - size – number of components per vertex (2 for xy, 3 for xyz) / - type – base type (typically GL_FLOAT or GL_DOUBLE)

Professor-style explanation: The slide '3. Memory Layout Description' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. On the slide, the concrete items are: - Memory layout is described by the following function / - glVertexAttribPointer(attribIndex, size, type, normalized, stride, offset); / - attribIndex – attribute number (0 for position, later more ...) / - size – number of components per vertex (2 for xy, 3 for xyz) / - type – base type (typically GL_FLOAT or GL_DOUBLE). The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type.

Technical commentary: This slide is about 3. Memory Layout Description. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Memory layout is described by the following function / - glVertexAttribPointer(attribIndex, size, type, normalized, stride, offset); / - attribIndex – attribute number (0 for position, later more ...) / - size – number of components per vertex (2 for xy, 3 for xyz) / - type – base type (typically GL_FLOAT or GL_DOUBLE)

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '3. Memory Layout Description'?

### Page 27 - 4. VAO Drawing 1/2

Source cue: - Drawing is done with the command / - glDrawArrays(mode, first, count); / - mode – specifies the primitive type (e.g., GL_TRIANGLES or GL_LINES) / - From all vertices, the next count vertices are drawn from index first / - Actual vertex data no longer needs to be specified

Professor-style explanation: The slide '4. VAO Drawing 1/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. On the slide, the concrete items are: - Drawing is done with the command / - glDrawArrays(mode, first, count); / - mode – specifies the primitive type (e.g., GL_TRIANGLES or GL_LINES) / - From all vertices, the next count vertices are drawn from index first / - Actual vertex data no longer needs to be specified. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations.

Technical commentary: This slide is about 4. VAO Drawing 1/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: - Drawing is done with the command / - glDrawArrays(mode, first, count); / - mode – specifies the primitive type (e.g., GL_TRIANGLES or GL_LINES) / - From all vertices, the next count vertices are drawn from index first / - Actual vertex data no longer needs to be specified

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by '4. VAO Drawing 1/2'?

### Page 28 - 4. VAO Drawing 2/2

Source cue: - There is a small number of primitive types / - Points / - Lines, Line Strips, Line Loops / - Triangles, Triangle Strips, Triangle Fans, Patches / v2 v2 v2

Professor-style explanation: The slide '4. VAO Drawing 2/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. On the slide, the concrete items are: - There is a small number of primitive types / - Points / - Lines, Line Strips, Line Loops / - Triangles, Triangle Strips, Triangle Fans, Patches / v2 v2 v2. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations.

Technical commentary: This slide is about 4. VAO Drawing 2/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: - There is a small number of primitive types / - Points / - Lines, Line Strips, Line Loops / - Triangles, Triangle Strips, Triangle Fans, Patches / v2 v2 v2

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by '4. VAO Drawing 2/2'?

### Page 29 - 5. GPU Memory Release

Source cue: - After usage VAO and VBO should be deleted from GPU memory / - glDeleteBuffers(…); / - glDeleteVertexArrays(…);

Professor-style explanation: The slide '5. GPU Memory Release' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - After usage VAO and VBO should be deleted from GPU memory / - glDeleteBuffers(…); / - glDeleteVertexArrays(…). The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about 5. GPU Memory Release. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - After usage VAO and VBO should be deleted from GPU memory / - glDeleteBuffers(…); / - glDeleteVertexArrays(…);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '5. GPU Memory Release'?

### Page 30 - Rendering Initialization 1/2

Source cue: static void init_render_scene(void) { / static const GLfloat vertices[6][2] = { / {0.0f, 1.0f}, {1.0f, 1.0f}, {1.0f, 0.0f}, /* 1st triangle */ / {0.5f, 0.5f}, {1.0f, 0.3f}, {0.7f, 1.0f} /* 2nd triangle */ / static const char* vs_src =

Professor-style explanation: The slide 'Rendering Initialization 1/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. On the slide, the concrete items are: static void init_render_scene(void) { / static const GLfloat vertices[6][2] = { / {0.0f, 1.0f}, {1.0f, 1.0f}, {1.0f, 0.0f}, /* 1st triangle */ / {0.5f, 0.5f}, {1.0f, 0.3f}, {0.7f, 1.0f} /* 2nd triangle */ / static const char* vs_src =. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations.

Technical commentary: This slide is about Rendering Initialization 1/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: static void init_render_scene(void) { / static const GLfloat vertices[6][2] = { / {0.0f, 1.0f}, {1.0f, 1.0f}, {1.0f, 0.0f}, /* 1st triangle */ / {0.5f, 0.5f}, {1.0f, 0.3f}, {0.7f, 1.0f} /* 2nd triangle */ / static const char* vs_src =

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Rendering Initialization 1/2'?

### Page 31 - Rendering Initialization 2/2

Source cue: program = create_program(vs_src, fs_src); / glGenVertexArrays(1, &vao); / glGenBuffers(1, &vbo); / glBindVertexArray(vao); / glBindBuffer(GL_ARRAY_BUFFER, vbo);

Professor-style explanation: The slide 'Rendering Initialization 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: program = create_program(vs_src, fs_src); / glGenVertexArrays(1, &vao); / glGenBuffers(1, &vbo); / glBindVertexArray(vao); / glBindBuffer(GL_ARRAY_BUFFER, vbo). The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Rendering Initialization 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: program = create_program(vs_src, fs_src); / glGenVertexArrays(1, &vao); / glGenBuffers(1, &vbo); / glBindVertexArray(vao); / glBindBuffer(GL_ARRAY_BUFFER, vbo);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Rendering Initialization 2/2'?

### Page 32 - Rendering

Source cue: static void render_scene(void) { / glClear(GL_COLOR_BUFFER_BIT); / glUseProgram(program); / glBindVertexArray(vao); / glDrawArrays(GL_TRIANGLES, 0, 6);

Professor-style explanation: The slide 'Rendering' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: static void render_scene(void) { / glClear(GL_COLOR_BUFFER_BIT); / glUseProgram(program); / glBindVertexArray(vao); / glDrawArrays(GL_TRIANGLES, 0, 6). The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Rendering. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: static void render_scene(void) { / glClear(GL_COLOR_BUFFER_BIT); / glUseProgram(program); / glBindVertexArray(vao); / glDrawArrays(GL_TRIANGLES, 0, 6);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Rendering'?

### Page 33 - Additional Attributes

Source cue: - Additional attributes are necessary for drawing / - Color, normals, texture coordinates, ... / - There are two ways to assign these attributes to the vertex data / - Attributes are bound to the same VAO in separate VBO / - Attributes are stored interleaved with vertex data,

Professor-style explanation: The slide 'Additional Attributes' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. On the slide, the concrete items are: - Additional attributes are necessary for drawing / - Color, normals, texture coordinates, ... / - There are two ways to assign these attributes to the vertex data / - Attributes are bound to the same VAO in separate VBO / - Attributes are stored interleaved with vertex data,. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear.

Technical commentary: This slide is about Additional Attributes. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. Concrete items shown: - Additional attributes are necessary for drawing / - Color, normals, texture coordinates, ... / - There are two ways to assign these attributes to the vertex data / - Attributes are bound to the same VAO in separate VBO / - Attributes are stored interleaved with vertex data,

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Additional Attributes'?

### Page 34 - 2.4 OpenGL Rendering Pipeline

Source cue: Programmable and static stages

Professor-style explanation: The slide '2.4 OpenGL Rendering Pipeline' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. On the slide, the concrete items are: Programmable and static stages. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter.

Technical commentary: This slide is about 2.4 OpenGL Rendering Pipeline. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. Concrete items shown: Programmable and static stages

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for '2.4 OpenGL Rendering Pipeline' in the rendering pipeline?

### Page 35 - The Rendering Pipeline 1/2

Source cue: Scene Description Raster Image / Geometry Fragment / Rasterization / Processing Processing / Vertices Primitives Fragments Pixels

Professor-style explanation: The slide 'The Rendering Pipeline 1/2' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. On the slide, the concrete items are: Scene Description Raster Image / Geometry Fragment / Rasterization / Processing Processing / Vertices Primitives Fragments Pixels. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter.

Technical commentary: This slide is about The Rendering Pipeline 1/2. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. Concrete items shown: Scene Description Raster Image / Geometry Fragment / Rasterization / Processing Processing / Vertices Primitives Fragments Pixels

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'The Rendering Pipeline 1/2' in the rendering pipeline?

### Page 36 - The Rendering Pipeline 2/2

Source cue: - Sequence of fixed and programmable stages Programmable / Vertex Processing / - Process is influenced by context and scene objects / Context Fixed Function / - Programmable levels are programmed

Professor-style explanation: The slide 'The Rendering Pipeline 2/2' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. On the slide, the concrete items are: - Sequence of fixed and programmable stages Programmable / Vertex Processing / - Process is influenced by context and scene objects / Context Fixed Function / - Programmable levels are programmed. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter.

Technical commentary: This slide is about The Rendering Pipeline 2/2. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. Concrete items shown: - Sequence of fixed and programmable stages Programmable / Vertex Processing / - Process is influenced by context and scene objects / Context Fixed Function / - Programmable levels are programmed

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'The Rendering Pipeline 2/2' in the rendering pipeline?

### Page 37 - Shader Programming – History 1/2

Source cue: - There is special graphics hardware (dedicated) / and general graphics hardware (general purpose) / - Special graphics hardware / - Volume Rendering: VolumePro / - Game consoles: Custom NVIDIA chips in XBox

Professor-style explanation: The slide 'Shader Programming – History 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - There is special graphics hardware (dedicated) / and general graphics hardware (general purpose) / - Special graphics hardware / - Volume Rendering: VolumePro / - Game consoles: Custom NVIDIA chips in XBox. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Shader Programming – History 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - There is special graphics hardware (dedicated) / and general graphics hardware (general purpose) / - Special graphics hardware / - Volume Rendering: VolumePro / - Game consoles: Custom NVIDIA chips in XBox

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Programming – History 1/2'?

### Page 38 - Shader Programming – History 2/2

Source cue: - Various vendor-dependent extensions are introduced / to provide extensibility for general graphics hardware / - Texture shaders and register combiners allowed modification / through the application of textures / - Applicability is very limited by the possibilities of graphics hardware

Professor-style explanation: The slide 'Shader Programming – History 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Various vendor-dependent extensions are introduced / to provide extensibility for general graphics hardware / - Texture shaders and register combiners allowed modification / through the application of textures / - Applicability is very limited by the possibilities of graphics hardware. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Shader Programming – History 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Various vendor-dependent extensions are introduced / to provide extensibility for general graphics hardware / - Texture shaders and register combiners allowed modification / through the application of textures / - Applicability is very limited by the possibilities of graphics hardware

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Programming – History 2/2'?

### Page 39 - Assembler Shader

Source cue: - First OpenGL extensions support shader programming in assembler code / !! ARBvp1.0 / ATTRIB iPos = vertex.position ; / ATTRIB iNormal = vertex.normal ; / ...

Professor-style explanation: The slide 'Assembler Shader' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - First OpenGL extensions support shader programming in assembler code / !! ARBvp1.0 / ATTRIB iPos = vertex.position ; / ATTRIB iNormal = vertex.normal ; / . The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Assembler Shader. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - First OpenGL extensions support shader programming in assembler code / !! ARBvp1.0 / ATTRIB iPos = vertex.position ; / ATTRIB iNormal = vertex.normal ; / ...

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Assembler Shader'?

### Page 40 - High-Level Shading Languages 1/2

Source cue: - Assembler code is hard to read and hard to maintain / - High-level languages f or shading are specified in C-like syntax / - Source code is translated by the compiler into appropriate ASM statements / - Using shaders after initial binding automatically when rendering geometry / - Interface to OpenGL by passing appropriate variables or changing the OpenGL

Professor-style explanation: The slide 'High-Level Shading Languages 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Assembler code is hard to read and hard to maintain / - High-level languages f or shading are specified in C-like syntax / - Source code is translated by the compiler into appropriate ASM statements / - Using shaders after initial binding automatically when rendering geometry / - Interface to OpenGL by passing appropriate variables or changing the OpenGL. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about High-Level Shading Languages 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Assembler code is hard to read and hard to maintain / - High-level languages f or shading are specified in C-like syntax / - Source code is translated by the compiler into appropriate ASM statements / - Using shaders after initial binding automatically when rendering geometry / - Interface to OpenGL by passing appropriate variables or changing the OpenGL

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'High-Level Shading Languages 1/2'?

### Page 41 - High-Level Shading Languages 2/2

Source cue: - Existing high level languages f or shader development / - CG - C for Graphics by NVIDIA / - CG was introduced in 2003 by NVIDIA as a platform independent solution / (in practice rather semi-platform independent) / - HLSL - High Level Shading Language from Microsoft

Professor-style explanation: The slide 'High-Level Shading Languages 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Existing high level languages f or shader development / - CG - C for Graphics by NVIDIA / - CG was introduced in 2003 by NVIDIA as a platform independent solution / (in practice rather semi-platform independent) / - HLSL - High Level Shading Language from Microsoft. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about High-Level Shading Languages 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Existing high level languages f or shader development / - CG - C for Graphics by NVIDIA / - CG was introduced in 2003 by NVIDIA as a platform independent solution / (in practice rather semi-platform independent) / - HLSL - High Level Shading Language from Microsoft

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'High-Level Shading Languages 2/2'?

### Page 42 - Shader Types

Source cue: - Pipeline concept has been kept in place / and shaders are responsible for different stages / - First, geometry level programming was done by vertex shaders / - Vertex shaders allow modifiability of vertex transformations and lighting / - After that, there was an extension for image-based algorithms by fragment

Professor-style explanation: The slide 'Shader Types' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Pipeline concept has been kept in place / and shaders are responsible for different stages / - First, geometry level programming was done by vertex shaders / - Vertex shaders allow modifiability of vertex transformations and lighting / - After that, there was an extension for image-based algorithms by fragment. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Shader Types. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Pipeline concept has been kept in place / and shaders are responsible for different stages / - First, geometry level programming was done by vertex shaders / - Vertex shaders allow modifiability of vertex transformations and lighting / - After that, there was an extension for image-based algorithms by fragment

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Types'?

### Page 43 - Vertex Shader Concepts

Source cue: - Vertex shaders enable the programmable modification of processed geometry / - Possibilities of a vertex shader / Programmable / - Geometric transformation of vertices and normals / Vertex Processing

Professor-style explanation: The slide 'Vertex Shader Concepts' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Vertex shaders enable the programmable modification of processed geometry / - Possibilities of a vertex shader / Programmable / - Geometric transformation of vertices and normals / Vertex Processing. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Vertex Shader Concepts. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Vertex shaders enable the programmable modification of processed geometry / - Possibilities of a vertex shader / Programmable / - Geometric transformation of vertices and normals / Vertex Processing

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Concepts'?

### Page 44 - Vertex Shader Examples 1/2

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Vertex Shader Examples 1/2' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. On the slide, the concrete items are: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail.

Technical commentary: This slide is about Vertex Shader Examples 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Examples 1/2'?

### Page 45 - Vertex Shader Examples 2/2

Source cue: - Morphing / - Shadow volume calculation for shadow effects / [ID Software‘s Doom III]

Professor-style explanation: The slide 'Vertex Shader Examples 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Morphing / - Shadow volume calculation for shadow effects / [ID Software‘s Doom III]. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Vertex Shader Examples 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Morphing / - Shadow volume calculation for shadow effects / [ID Software‘s Doom III]

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Examples 2/2'?

### Page 46 - Vertex Shader Coordinate Systems 1/2

Source cue: - Vertex shaders are executed for each vertex / - Vertex shaders calculate coordinates in clipping coordinates as output / - Vertex shaders can not / - Access adjacent vertices / - Change the number of vertices (i.e., generate or discard vertices)

Professor-style explanation: The slide 'Vertex Shader Coordinate Systems 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Vertex shaders are executed for each vertex / - Vertex shaders calculate coordinates in clipping coordinates as output / - Vertex shaders can not / - Access adjacent vertices / - Change the number of vertices (i.e., generate or discard vertices). The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Vertex Shader Coordinate Systems 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Vertex shaders are executed for each vertex / - Vertex shaders calculate coordinates in clipping coordinates as output / - Vertex shaders can not / - Access adjacent vertices / - Change the number of vertices (i.e., generate or discard vertices)

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Coordinate Systems 1/2'?

### Page 47 - Vertex Shader Coordinate Systems 2/2

Source cue: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform

Professor-style explanation: The slide 'Vertex Shader Coordinate Systems 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Vertex Shader Coordinate Systems 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Coordinate Systems 2/2'?

### Page 48 - Local Space

Source cue: - Coordinates of your object relative to its local origin / - 3D vertex positions

Professor-style explanation: The slide 'Local Space' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. On the slide, the concrete items are: - Coordinates of your object relative to its local origin / - 3D vertex positions. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear.

Technical commentary: This slide is about Local Space. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. Concrete items shown: - Coordinates of your object relative to its local origin / - 3D vertex positions

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Local Space'?

### Page 49 - World Space

Source cue: - Coordinates in respect of a larger world / - Relative to some global origin of the world / - Together with many other objects

Professor-style explanation: The slide 'World Space' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. On the slide, the concrete items are: - Coordinates in respect of a larger world / - Relative to some global origin of the world / - Together with many other objects. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear.

Technical commentary: This slide is about World Space. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. Concrete items shown: - Coordinates in respect of a larger world / - Relative to some global origin of the world / - Together with many other objects

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'World Space'?

### Page 50 - View Space

Source cue: - Coordinates as seen from the camera

Professor-style explanation: The slide 'View Space' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. On the slide, the concrete items are: - Coordinates as seen from the camera. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear.

Technical commentary: This slide is about View Space. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. Concrete items shown: - Coordinates as seen from the camera

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'View Space'?

### Page 51 - Clip Space

Source cue: - Clip coordinates range from -1 to 1 / - Projection (Orthographic, Perspective)

Professor-style explanation: The slide 'Clip Space' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. On the slide, the concrete items are: - Clip coordinates range from -1 to 1 / - Projection (Orthographic, Perspective). The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear.

Technical commentary: This slide is about Clip Space. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. Concrete items shown: - Clip coordinates range from -1 to 1 / - Projection (Orthographic, Perspective)

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Clip Space'?

### Page 52 - Screen Space

Source cue: - Transform to image coordinates with glViewport / - Results are sent to the rasterizer

Professor-style explanation: The slide 'Screen Space' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. On the slide, the concrete items are: - Transform to image coordinates with glViewport / - Results are sent to the rasterizer. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear.

Technical commentary: This slide is about Screen Space. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. Concrete items shown: - Transform to image coordinates with glViewport / - Results are sent to the rasterizer

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Screen Space'?

### Page 53 - Coordinate Systems

Source cue: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform

Professor-style explanation: The slide 'Coordinate Systems' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. On the slide, the concrete items are: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear.

Technical commentary: This slide is about Coordinate Systems. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. Concrete items shown: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Coordinate Systems'?

### Page 54 - Vertex Shader Variables

Source cue: - Input types / - Uniforms: read only in VS (& FS) // Intrinsic vertex attributes / out gl_PerVertex { / - For example: light position or light color / vec4 gl_Position;

Professor-style explanation: The slide 'Vertex Shader Variables' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Input types / - Uniforms: read only in VS (& FS) // Intrinsic vertex attributes / out gl_PerVertex { / - For example: light position or light color / vec4 gl_Position. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Vertex Shader Variables. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Input types / - Uniforms: read only in VS (& FS) // Intrinsic vertex attributes / out gl_PerVertex { / - For example: light position or light color / vec4 gl_Position;

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Variables'?

### Page 55 - Fixed Function Vertex Postprocessing

Source cue: - Clipping / - Discard invisible geometries / Programmable / - Perspective Division / Vertex Processing

Professor-style explanation: The slide 'Fixed Function Vertex Postprocessing' explains how camera geometry turns a 3D scene into image coordinates. In view space, objects are described relative to the camera. The projection matrix then maps that camera-centered geometry into clip space, where the viewing volume and clipping boundaries can be handled consistently. Perspective projection uses the homogeneous coordinate so that the later divide by w creates foreshortening: farther objects occupy less image space. Orthographic projection removes that depth-based size change and keeps parallel structures visually parallel. On the slide, the concrete items are: - Clipping / - Discard invisible geometries / Programmable / - Perspective Division / Vertex Processing. The object chain is view-space position, projection matrix, clip coordinate, normalized device coordinate, and viewport coordinate. The slide is therefore connecting camera setup, visual appearance, and the numeric coordinate pipeline that rasterization later consumes.

Technical commentary: This slide is about Fixed Function Vertex Postprocessing. The projection objects on the slide convert view-space geometry into clip coordinates, normalized coordinates, and finally screen-related positions. Concrete items shown: - Clipping / - Discard invisible geometries / Programmable / - Perspective Division / Vertex Processing

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Check yourself: Can you explain how 'Fixed Function Vertex Postprocessing' changes positions before rasterization?

### Page 56 - Fixed Function Rasterization

Source cue: - Geometry is converted to raster coordinates / Programmable / Vertex Processing / Fixed Function / Primitives Fragments Vertex Postprocessing

Professor-style explanation: The slide 'Fixed Function Rasterization' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. On the slide, the concrete items are: - Geometry is converted to raster coordinates / Programmable / Vertex Processing / Fixed Function / Primitives Fragments Vertex Postprocessing. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear.

Technical commentary: This slide is about Fixed Function Rasterization. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. Concrete items shown: - Geometry is converted to raster coordinates / Programmable / Vertex Processing / Fixed Function / Primitives Fragments Vertex Postprocessing

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Fixed Function Rasterization'?

### Page 57 - Fragment Shader Concept 1/2

Source cue: - Fragment shaders set the color of a pixel / - Possibilities of a fragment shader / Programmable / - Glare of textures / Vertex Processing

Professor-style explanation: The slide 'Fragment Shader Concept 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Fragment shaders set the color of a pixel / - Possibilities of a fragment shader / Programmable / - Glare of textures / Vertex Processing. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Fragment Shader Concept 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Fragment shaders set the color of a pixel / - Possibilities of a fragment shader / Programmable / - Glare of textures / Vertex Processing

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Fragment Shader Concept 1/2'?

### Page 58 - Fragment Shader Concept 2/2

Source cue: - Fragment shaders are executed for fragments (= pixel predecessors) / - Fragment shaders calculate the color and depth value of the current fragment / - No information about adjacent fragments available / - The number of fragments can be changed / - Fragment shaders can not generate fragments

Professor-style explanation: The slide 'Fragment Shader Concept 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Fragment shaders are executed for fragments (= pixel predecessors) / - Fragment shaders calculate the color and depth value of the current fragment / - No information about adjacent fragments available / - The number of fragments can be changed / - Fragment shaders can not generate fragments. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Fragment Shader Concept 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Fragment shaders are executed for fragments (= pixel predecessors) / - Fragment shaders calculate the color and depth value of the current fragment / - No information about adjacent fragments available / - The number of fragments can be changed / - Fragment shaders can not generate fragments

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Fragment Shader Concept 2/2'?

### Page 59 - Shader Example

Source cue: layout (std140) uniform Matrices { Vertex Shader / mat4 projModelViewMatrix; / mat3 normalMatrix; /** Fragment Shader / }; * Set fragment color to red. / in vec3 position;

Professor-style explanation: The slide 'Shader Example' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: layout (std140) uniform Matrices { Vertex Shader / mat4 projModelViewMatrix; / mat3 normalMatrix; /** Fragment Shader / }; * Set fragment color to red. / in vec3 position. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Shader Example. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: layout (std140) uniform Matrices { Vertex Shader / mat4 projModelViewMatrix; / mat3 normalMatrix; /** Fragment Shader / }; * Set fragment color to red. / in vec3 position;

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Example'?

### Page 60 - GLSL Shader Functions

Source cue: - Trigonometry functions / - radians, degrees, sin, cos, tan, asin, acos, atan / - Power calculations / - pow, exp2, log2, sqrt, inversesqrt / - General

Professor-style explanation: The slide 'GLSL Shader Functions' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Trigonometry functions / - radians, degrees, sin, cos, tan, asin, acos, atan / - Power calculations / - pow, exp2, log2, sqrt, inversesqrt / - General. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about GLSL Shader Functions. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Trigonometry functions / - radians, degrees, sin, cos, tan, asin, acos, atan / - Power calculations / - pow, exp2, log2, sqrt, inversesqrt / - General

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'GLSL Shader Functions'?

### Page 61 - Shader Usage

Source cue: - One or multiple shaders are attached to a shader program / Vertex Shader / glCreateShader glCreateProgram / Fragment Shader / glShaderSource glAttachShader glCreateShader

Professor-style explanation: The slide 'Shader Usage' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - One or multiple shaders are attached to a shader program / Vertex Shader / glCreateShader glCreateProgram / Fragment Shader / glShaderSource glAttachShader glCreateShader. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Shader Usage. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - One or multiple shaders are attached to a shader program / Vertex Shader / glCreateShader glCreateProgram / Fragment Shader / glShaderSource glAttachShader glCreateShader

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Usage'?

### Page 62 - Binding Shaders

Source cue: v = glCreateShader(GL_VERTEX_SHADER); // vertex shader / char* vs = readTextFile(”vertex-shader.vert"); / const char* vv = vs; / glShaderSource(v, 1, &vv, NULL); / free(vs);

Professor-style explanation: The slide 'Binding Shaders' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: v = glCreateShader(GL_VERTEX_SHADER); // vertex shader / char* vs = readTextFile(”vertex-shader.vert"); / const char* vv = vs; / glShaderSource(v, 1, &vv, NULL); / free(vs). The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Binding Shaders. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: v = glCreateShader(GL_VERTEX_SHADER); // vertex shader / char* vs = readTextFile(”vertex-shader.vert"); / const char* vv = vs; / glShaderSource(v, 1, &vv, NULL); / free(vs);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Binding Shaders'?

### Page 63 - Setting Uniforms

Source cue: - Uniforms are used to communicate between CPU and GPU / - Data is bound to uniform locations / - Must be updated after each linking process / GLint loc0 = glGetUniformLocation(p, ”isoValue_"); / glUniform1f(loc0, 0.45f);

Professor-style explanation: The slide 'Setting Uniforms' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. On the slide, the concrete items are: - Uniforms are used to communicate between CPU and GPU / - Data is bound to uniform locations / - Must be updated after each linking process / GLint loc0 = glGetUniformLocation(p, ”isoValue_"); / glUniform1f(loc0, 0.45f). The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Setting Uniforms. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: - Uniforms are used to communicate between CPU and GPU / - Data is bound to uniform locations / - Must be updated after each linking process / GLint loc0 = glGetUniformLocation(p, ”isoValue_"); / glUniform1f(loc0, 0.45f);

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Setting Uniforms' into a causal sentence instead of repeating the slide title?

### Page 64 - Shader Performance

Source cue: - Guidelines for efficient shaders / - Since fragment shaders are executed for a large number of fragments, / they should contain as few instructions as possible / - There should be as little as possible a change of the active shaders, / because they have their own state and, accordingly, the pipeline may need

Professor-style explanation: The slide 'Shader Performance' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Guidelines for efficient shaders / - Since fragment shaders are executed for a large number of fragments, / they should contain as few instructions as possible / - There should be as little as possible a change of the active shaders, / because they have their own state and, accordingly, the pipeline may need. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Shader Performance. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Guidelines for efficient shaders / - Since fragment shaders are executed for a large number of fragments, / they should contain as few instructions as possible / - There should be as little as possible a change of the active shaders, / because they have their own state and, accordingly, the pipeline may need

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Performance'?

### Page 65 - Shader Development Environments 1/2

Source cue: - FX Composer, NVPerfHUD (NVIDIA) / - HLSL Shader IDE with performance analytics / www.developer.nvidia.com/page/tools.html / - RenderMonkey (ATI) / - HLSL, GLSL Shader IDE with performance analytics

Professor-style explanation: The slide 'Shader Development Environments 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - FX Composer, NVPerfHUD (NVIDIA) / - HLSL Shader IDE with performance analytics / www.developer.nvidia.com/page/tools.html / - RenderMonkey (ATI) / - HLSL, GLSL Shader IDE with performance analytics. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Shader Development Environments 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - FX Composer, NVPerfHUD (NVIDIA) / - HLSL Shader IDE with performance analytics / www.developer.nvidia.com/page/tools.html / - RenderMonkey (ATI) / - HLSL, GLSL Shader IDE with performance analytics

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Development Environments 1/2'?

### Page 66 - Shader Development Environments 2/2

Source cue: - Shdr online GLSL editor: https://shdr.bkcore.com/

Professor-style explanation: The slide 'Shader Development Environments 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Shdr online GLSL editor: https://shdr.bkcore.com/. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Shader Development Environments 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Shdr online GLSL editor: https://shdr.bkcore.com/

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Development Environments 2/2'?

### Page 67 - 2.5 Fragment Tests and Operations

Source cue: Towards the finishing line to the pixel

Professor-style explanation: The slide '2.5 Fragment Tests and Operations' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. On the slide, the concrete items are: Towards the finishing line to the pixel. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations.

Technical commentary: This slide is about 2.5 Fragment Tests and Operations. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: Towards the finishing line to the pixel

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by '2.5 Fragment Tests and Operations'?

### Page 68 - Fragment Tests and Operations 1/2

Source cue: - After fragments have been generated, they must go through the per-fragment / tests and operations / Programmable / - Only if all these tests are successful, / Vertex Processing

Professor-style explanation: The slide 'Fragment Tests and Operations 1/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. On the slide, the concrete items are: - After fragments have been generated, they must go through the per-fragment / tests and operations / Programmable / - Only if all these tests are successful, / Vertex Processing. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Fragment Tests and Operations 1/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: - After fragments have been generated, they must go through the per-fragment / tests and operations / Programmable / - Only if all these tests are successful, / Vertex Processing

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Fragment Tests and Operations 1/2' into a causal sentence instead of repeating the slide title?

### Page 69 - Fragment Tests and Operations 2/2

Source cue: Fragment Pixel Ownership Scissor Alpha / Data Test Test Test / Depth Stencil / Framebuffer Dithering Blending / Test Test

Professor-style explanation: The slide 'Fragment Tests and Operations 2/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: Fragment Pixel Ownership Scissor Alpha / Data Test Test Test / Depth Stencil / Framebuffer Dithering Blending / Test Test. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Fragment Tests and Operations 2/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: Fragment Pixel Ownership Scissor Alpha / Data Test Test Test / Depth Stencil / Framebuffer Dithering Blending / Test Test

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Fragment Tests and Operations 2/2'?

### Page 70 - Alpha Test

Source cue: - If framebuffer is an RGBA buffer, the alpha test can be performed / - The test must first be activated / glEnable(GL_ALPHA_TEST); / - The comparison function indicates which fragments survive the test / glAlphaFunc(func, value);

Professor-style explanation: The slide 'Alpha Test' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - If framebuffer is an RGBA buffer, the alpha test can be performed / - The test must first be activated / glEnable(GL_ALPHA_TEST); / - The comparison function indicates which fragments survive the test / glAlphaFunc(func, value). The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Alpha Test. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - If framebuffer is an RGBA buffer, the alpha test can be performed / - The test must first be activated / glEnable(GL_ALPHA_TEST); / - The comparison function indicates which fragments survive the test / glAlphaFunc(func, value);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Alpha Test'?

### Page 71 - Stencil Test

Source cue: - Stencil Buffer / - Is a frame buffer component / - Is (indirectly) filled by drawing operations / - No special stencil drawing operations / - Stencil operation

Professor-style explanation: The slide 'Stencil Test' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Stencil Buffer / - Is a frame buffer component / - Is (indirectly) filled by drawing operations / - No special stencil drawing operations / - Stencil operation. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Stencil Test. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Stencil Buffer / - Is a frame buffer component / - Is (indirectly) filled by drawing operations / - No special stencil drawing operations / - Stencil operation

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Stencil Test'?

### Page 72 - Depth Test

Source cue: - If the framebuffer has a depth buffer, the depth test can be performed / - The test must first be activated / glEnable(GL_DEPTH_TEST); / - The comparison is made with the depth value already in the buffer / - The comparison function indicates which fragments survive the test

Professor-style explanation: The slide 'Depth Test' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - If the framebuffer has a depth buffer, the depth test can be performed / - The test must first be activated / glEnable(GL_DEPTH_TEST); / - The comparison is made with the depth value already in the buffer / - The comparison function indicates which fragments survive the test. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Depth Test. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - If the framebuffer has a depth buffer, the depth test can be performed / - The test must first be activated / glEnable(GL_DEPTH_TEST); / - The comparison is made with the depth value already in the buffer / - The comparison function indicates which fragments survive the test

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Depth Test'?

### Page 73 - Image Composition and Mixture

Source cue: - Alpha values o f the pixels / - control the combination of pixel values / - are specified as color components of color pixels / - 𝑃 = [𝑅, 𝐺, 𝐵, 𝐴], 𝑤𝑖𝑡ℎ 𝑅, 𝐺, 𝐵, 𝐴 ∈ [0,1] / - Applications are manifold

Professor-style explanation: The slide 'Image Composition and Mixture' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. On the slide, the concrete items are: - Alpha values o f the pixels / - control the combination of pixel values / - are specified as color components of color pixels / - 𝑃 = [𝑅, 𝐺, 𝐵, 𝐴], 𝑤𝑖𝑡ℎ 𝑅, 𝐺, 𝐵, 𝐴 ∈ [0,1] / - Applications are manifold. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Image Composition and Mixture. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: - Alpha values o f the pixels / - control the combination of pixel values / - are specified as color components of color pixels / - 𝑃 = [𝑅, 𝐺, 𝐵, 𝐴], 𝑤𝑖𝑡ℎ 𝑅, 𝐺, 𝐵, 𝐴 ∈ [0,1] / - Applications are manifold

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Image Composition and Mixture' into a causal sentence instead of repeating the slide title?

### Page 74 - Blending Application

Source cue: - Example application for transparency: drawing with semi-transparent brush

Professor-style explanation: The slide 'Blending Application' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. On the slide, the concrete items are: - Example application for transparency: drawing with semi-transparent brush. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Blending Application. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: - Example application for transparency: drawing with semi-transparent brush

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Blending Application' into a causal sentence instead of repeating the slide title?

### Page 75 - Blending Process 1/2

Source cue: - Blending is an operation called per fragment / - Fragments are modified after rasterization, / but before writing to the framebuffer with a blending function / - Combination of a source fragment to be written with the destination pixel / in the frame buffer by using a blending function

Professor-style explanation: The slide 'Blending Process 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Blending is an operation called per fragment / - Fragments are modified after rasterization, / but before writing to the framebuffer with a blending function / - Combination of a source fragment to be written with the destination pixel / in the frame buffer by using a blending function. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Blending Process 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Blending is an operation called per fragment / - Fragments are modified after rasterization, / but before writing to the framebuffer with a blending function / - Combination of a source fragment to be written with the destination pixel / in the frame buffer by using a blending function

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Blending Process 1/2'?

### Page 76 - Blending Process 2/2

Source cue: - Source factor: 𝐹 / - Destination factor: 𝐹 / - Source fragment: [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Destination pixel: [𝑃 , 𝑃 , 𝑃 , 𝑃 ]

Professor-style explanation: The slide 'Blending Process 2/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. On the slide, the concrete items are: - Source factor: 𝐹 / - Destination factor: 𝐹 / - Source fragment: [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Destination pixel: [𝑃 , 𝑃 , 𝑃 , 𝑃 ]. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Blending Process 2/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: - Source factor: 𝐹 / - Destination factor: 𝐹 / - Source fragment: [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Destination pixel: [𝑃 , 𝑃 , 𝑃 , 𝑃 ]

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Blending Process 2/2' into a causal sentence instead of repeating the slide title?

### Page 77 - Applying Blending

Source cue: - Switch on (or switch off) blending / - glEnable(GL_BLEND); / - glDisable(GL_BLEND); / - Defining Blending Factors / - glBlendFunc(srcFac, destFac);

Professor-style explanation: The slide 'Applying Blending' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. On the slide, the concrete items are: - Switch on (or switch off) blending / - glEnable(GL_BLEND); / - glDisable(GL_BLEND); / - Defining Blending Factors / - glBlendFunc(srcFac, destFac). The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Applying Blending. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: - Switch on (or switch off) blending / - glEnable(GL_BLEND); / - glDisable(GL_BLEND); / - Defining Blending Factors / - glBlendFunc(srcFac, destFac);

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Applying Blending' into a causal sentence instead of repeating the slide title?

### Page 78 - Blending Examples

Source cue: - Example 1: Copy source pixels and overwrite destination pixels / - glBlendFunc(GL_ONE, GL_ZERO); / - 𝑃 = [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑏𝑙𝑒𝑛𝑑 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Example 2: Alpha-based mixing of source pixels and destination pixels

Professor-style explanation: The slide 'Blending Examples' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. On the slide, the concrete items are: - Example 1: Copy source pixels and overwrite destination pixels / - glBlendFunc(GL_ONE, GL_ZERO); / - 𝑃 = [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑏𝑙𝑒𝑛𝑑 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Example 2: Alpha-based mixing of source pixels and destination pixels. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about Blending Examples. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: - Example 1: Copy source pixels and overwrite destination pixels / - glBlendFunc(GL_ONE, GL_ZERO); / - 𝑃 = [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑏𝑙𝑒𝑛𝑑 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Example 2: Alpha-based mixing of source pixels and destination pixels

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Blending Examples' into a causal sentence instead of repeating the slide title?

### Page 79 - 2.6 Framebuffer

Source cue: Contains everything that is (in)visible on the screen

Professor-style explanation: The slide '2.6 Framebuffer' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: Contains everything that is (in)visible on the screen. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about 2.6 Framebuffer. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: Contains everything that is (in)visible on the screen

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2.6 Framebuffer'?

### Page 80 - Viewport

Source cue: - Rectangular area in pixel grid, set explicitly / - Rendering operations are limited to this area / - All primitives that are completely or partially outside / are clipped at the viewport area (clipping)

Professor-style explanation: The slide 'Viewport' explains how camera geometry turns a 3D scene into image coordinates. In view space, objects are described relative to the camera. The projection matrix then maps that camera-centered geometry into clip space, where the viewing volume and clipping boundaries can be handled consistently. Perspective projection uses the homogeneous coordinate so that the later divide by w creates foreshortening: farther objects occupy less image space. Orthographic projection removes that depth-based size change and keeps parallel structures visually parallel. On the slide, the concrete items are: - Rectangular area in pixel grid, set explicitly / - Rendering operations are limited to this area / - All primitives that are completely or partially outside / are clipped at the viewport area (clipping). The object chain is view-space position, projection matrix, clip coordinate, normalized device coordinate, and viewport coordinate. The slide is therefore connecting camera setup, visual appearance, and the numeric coordinate pipeline that rasterization later consumes.

Technical commentary: This slide is about Viewport. The projection objects on the slide convert view-space geometry into clip coordinates, normalized coordinates, and finally screen-related positions. Concrete items shown: - Rectangular area in pixel grid, set explicitly / - Rendering operations are limited to this area / - All primitives that are completely or partially outside / are clipped at the viewport area (clipping)

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Check yourself: Can you explain how 'Viewport' changes positions before rasterization?

### Page 81 - Framebuffer

Source cue: - Context-bound raster with a resolution and structure / specified by the application / - Physical realization on the GPU / - Logical subdivision / - Color memory

Professor-style explanation: The slide 'Framebuffer' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Context-bound raster with a resolution and structure / specified by the application / - Physical realization on the GPU / - Logical subdivision / - Color memory. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Framebuffer. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Context-bound raster with a resolution and structure / specified by the application / - Physical realization on the GPU / - Logical subdivision / - Color memory

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Framebuffer'?

### Page 82 - OpenGL Framebuffers 1/3

Source cue: - Typical OpenGL framebuffer configuration / 8bit Stencil Buffer / 32bit Depth Buffer / = 32bit Color Buffer

Professor-style explanation: The slide 'OpenGL Framebuffers 1/3' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Typical OpenGL framebuffer configuration / 8bit Stencil Buffer / 32bit Depth Buffer / = 32bit Color Buffer. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about OpenGL Framebuffers 1/3. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Typical OpenGL framebuffer configuration / 8bit Stencil Buffer / 32bit Depth Buffer / = 32bit Color Buffer

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Framebuffers 1/3'?

### Page 83 - OpenGL Framebuffers 2/3

Source cue: - All buffers of a frame buffer have the same grid size / - Number of bitplanes per buffer can be configured individually / - Individual buffers are directly supported by the hardware / - Buffer identifier / - GL_COLOR_BUFFER_BIT

Professor-style explanation: The slide 'OpenGL Framebuffers 2/3' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - All buffers of a frame buffer have the same grid size / - Number of bitplanes per buffer can be configured individually / - Individual buffers are directly supported by the hardware / - Buffer identifier / - GL_COLOR_BUFFER_BIT. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about OpenGL Framebuffers 2/3. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - All buffers of a frame buffer have the same grid size / - Number of bitplanes per buffer can be configured individually / - Individual buffers are directly supported by the hardware / - Buffer identifier / - GL_COLOR_BUFFER_BIT

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Framebuffers 2/3'?

### Page 84 - OpenGL Framebuffers 3/3

Source cue: - Delete a buffer / glClear(GLbitfield mask); / - Set the initialization color for the color buffer / glClearColor(1.0,1.0,1.0,1.0); / glClear(GL_COLOR_BUFFER_BIT);

Professor-style explanation: The slide 'OpenGL Framebuffers 3/3' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Delete a buffer / glClear(GLbitfield mask); / - Set the initialization color for the color buffer / glClearColor(1.0,1.0,1.0,1.0); / glClear(GL_COLOR_BUFFER_BIT). The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about OpenGL Framebuffers 3/3. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Delete a buffer / glClear(GLbitfield mask); / - Set the initialization color for the color buffer / glClearColor(1.0,1.0,1.0,1.0); / glClear(GL_COLOR_BUFFER_BIT);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Framebuffers 3/3'?

### Page 85 - Double Buffering

Source cue: - Use of two color buffers to avoid flicker effects / - Image buildup takes place in the background (back buffer) / - Visible image is independent of this (front buffer) / Rendering / Process

Professor-style explanation: The slide 'Double Buffering' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Use of two color buffers to avoid flicker effects / - Image buildup takes place in the background (back buffer) / - Visible image is independent of this (front buffer) / Rendering / Process. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Double Buffering. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Use of two color buffers to avoid flicker effects / - Image buildup takes place in the background (back buffer) / - Visible image is independent of this (front buffer) / Rendering / Process

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Double Buffering'?

### Page 86 - 2.7 Pixel-based Rendering

Source cue: Direct pixel processing without involving 3D models

Professor-style explanation: The slide '2.7 Pixel-based Rendering' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. On the slide, the concrete items are: Direct pixel processing without involving 3D models. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation.

Technical commentary: This slide is about 2.7 Pixel-based Rendering. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: Direct pixel processing without involving 3D models

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn '2.7 Pixel-based Rendering' into a causal sentence instead of repeating the slide title?

### Page 87 - Pixel-based Rendering Operations

Source cue: - Generally / - Read and write operations for various image data formats, / usually as an external library (e.g., DevIl) / - Conversions between image data types / - In OpenGL done with framebuffer objects

Professor-style explanation: The slide 'Pixel-based Rendering Operations' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Generally / - Read and write operations for various image data formats, / usually as an external library (e.g., DevIl) / - Conversions between image data types / - In OpenGL done with framebuffer objects. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Pixel-based Rendering Operations. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Generally / - Read and write operations for various image data formats, / usually as an external library (e.g., DevIl) / - Conversions between image data types / - In OpenGL done with framebuffer objects

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Pixel-based Rendering Operations'?

### Page 88 - Image Operations

Source cue: - Rendering image data with OpenGL / Copy Pixel Data / Draw/Read / Pixel / Geometry

Professor-style explanation: The slide 'Image Operations' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Rendering image data with OpenGL / Copy Pixel Data / Draw/Read / Pixel / Geometry. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Image Operations. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Rendering image data with OpenGL / Copy Pixel Data / Draw/Read / Pixel / Geometry

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Image Operations'?

### Page 89 - Write Pixels into Framebuffer

Source cue: - glDrawPixels(x, y, width, height, format, type, pixels); / - Example / // 64x64 array with rgb components / GLubyte img[64][64][3]; / void draw() {

Professor-style explanation: The slide 'Write Pixels into Framebuffer' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - glDrawPixels(x, y, width, height, format, type, pixels); / - Example / // 64x64 array with rgb components / GLubyte img[64][64][3]; / void draw() {. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Write Pixels into Framebuffer. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - glDrawPixels(x, y, width, height, format, type, pixels); / - Example / // 64x64 array with rgb components / GLubyte img[64][64][3]; / void draw() {

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Write Pixels into Framebuffer'?

### Page 90 - Read Pixels from Framebuffer

Source cue: - glReadPixels(x, y, width, height, format, type, pixels); / - Example / GLubyte* img = 0; / int width, height; // canvas size / void snapshot() {

Professor-style explanation: The slide 'Read Pixels from Framebuffer' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - glReadPixels(x, y, width, height, format, type, pixels); / - Example / GLubyte* img = 0; / int width, height; // canvas size / void snapshot() {. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Read Pixels from Framebuffer. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - glReadPixels(x, y, width, height, format, type, pixels); / - Example / GLubyte* img = 0; / int width, height; // canvas size / void snapshot() {

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Read Pixels from Framebuffer'?

### Page 91 - Formats & Data Types

Source cue: - Format information for pixel array operations / - GL_RGB – red-green-blue values of the frame buffer (FB) / - GL_RED – red values o f the FB / - GL_ALPHA – transparency values of the FB / - GL_RGBA – red-Green-Blue-Alpha values of the FB

Professor-style explanation: The slide 'Formats & Data Types' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Format information for pixel array operations / - GL_RGB – red-green-blue values of the frame buffer (FB) / - GL_RED – red values o f the FB / - GL_ALPHA – transparency values of the FB / - GL_RGBA – red-Green-Blue-Alpha values of the FB. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Formats & Data Types. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Format information for pixel array operations / - GL_RGB – red-green-blue values of the frame buffer (FB) / - GL_RED – red values o f the FB / - GL_ALPHA – transparency values of the FB / - GL_RGBA – red-Green-Blue-Alpha values of the FB

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Formats & Data Types'?

### Page 92 - coordinate systems in the geometry stage

Source cue: - Rendering pipeline consist of geometry stage and rasterization stage / - Geometric primitives (mostly triangles) are transformed through different / coordinate systems in the geometry stage / - Rasterization results in fragments, which are pixel predecessors / - Fragments have to endure a sequence of tests in the rasterization stage, in

Professor-style explanation: The slide 'coordinate systems in the geometry stage' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. On the slide, the concrete items are: - Rendering pipeline consist of geometry stage and rasterization stage / - Geometric primitives (mostly triangles) are transformed through different / coordinate systems in the geometry stage / - Rasterization results in fragments, which are pixel predecessors / - Fragments have to endure a sequence of tests in the rasterization stage, in. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter.

Technical commentary: This slide is about coordinate systems in the geometry stage. Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion. Concrete items shown: - Rendering pipeline consist of geometry stage and rasterization stage / - Geometric primitives (mostly triangles) are transformed through different / coordinate systems in the geometry stage / - Rasterization results in fragments, which are pixel predecessors / - Fragments have to endure a sequence of tests in the rasterization stage, in

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'coordinate systems in the geometry stage' in the rendering pipeline?

### Page 93 - Literature and other sources used in this chapter

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Literature and other sources used in this chapter' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. On the slide, the concrete items are: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail.

Technical commentary: This slide is about Literature and other sources used in this chapter. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Literature and other sources used in this chapter' into a causal sentence instead of repeating the slide title?

### Page 94 - Guide: The Official Guide to Learning OpenGL

Source cue: - Text Books / - D. Shreiner, G. Sellers, J. Kessenich, B. Licea-Kane: OpenGL Programming / Guide: The Official Guide to Learning OpenGL / (8th Edition), Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer

Professor-style explanation: The slide 'Guide: The Official Guide to Learning OpenGL' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. On the slide, the concrete items are: - Text Books / - D. Shreiner, G. Sellers, J. Kessenich, B. Licea-Kane: OpenGL Programming / Guide: The Official Guide to Learning OpenGL / (8th Edition), Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image.

Technical commentary: This slide is about Guide: The Official Guide to Learning OpenGL. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. Concrete items shown: - Text Books / - D. Shreiner, G. Sellers, J. Kessenich, B. Licea-Kane: OpenGL Programming / Guide: The Official Guide to Learning OpenGL / (8th Edition), Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Guide: The Official Guide to Learning OpenGL'?

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
