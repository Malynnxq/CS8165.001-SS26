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

### Page 1 - Untitled slide

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Professor-style explanation: For 'Untitled slide', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Untitled slide. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Untitled slide' into a causal sentence instead of repeating the slide title?

### Page 2 - Object-based Rendering

Source cue: - Image generation done through rasterization / - Scene objects formed by 3D models (primitives) / are transformed through successive coordinate systems / - Primitives are rasterized into fragments, which are pixel predecessors / - A subset of the fragments becomes pixels

Professor-style explanation: For 'Object-based Rendering', imagine following one piece of scene data through the renderer. It starts as model or application data, then passes through transformations, primitive processing, rasterization, fragment processing, tests, and finally the framebuffer. The slide gives us this anchor: - Image generation done through rasterization / - Scene objects formed by 3D models (primitives) / are transformed through successive coordinate systems / - Primitives are rasterized into fragments, which are pixel predecessors / - A subset of the fragments becomes pixels. The important point is that each stage changes the representation, so debugging means asking where the representation first became wrong.

Technical commentary: This slide is about Object-based Rendering. Read it as a data-flow explanation: scene or model data is processed step by step until valid framebuffer updates remain. The visible cue is: - Image generation done through rasterization / - Scene objects formed by 3D models (primitives) / are transformed through successive coordinate systems / - Primitives are rasterized into fragments, which are pixel predecessors / - A subset of the fragments becomes pixels

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'Object-based Rendering' in the rendering pipeline?

### Page 3 - 2.1 Rendering Process

Source cue: 2.2 OpenGL Overview / 2.3 OpenGL Rendering / 2.4 OpenGL Rendering Pipeline / 2.5 Fragment Tests and Operations / 2.6 Framebuffer

Professor-style explanation: For '2.1 Rendering Process', imagine following one piece of scene data through the renderer. It starts as model or application data, then passes through transformations, primitive processing, rasterization, fragment processing, tests, and finally the framebuffer. The slide gives us this anchor: 2.2 OpenGL Overview / 2.3 OpenGL Rendering / 2.4 OpenGL Rendering Pipeline / 2.5 Fragment Tests and Operations / 2.6 Framebuffer. The important point is that each stage changes the representation, so debugging means asking where the representation first became wrong.

Technical commentary: This slide is about 2.1 Rendering Process. Read it as a data-flow explanation: scene or model data is processed step by step until valid framebuffer updates remain. The visible cue is: 2.2 OpenGL Overview / 2.3 OpenGL Rendering / 2.4 OpenGL Rendering Pipeline / 2.5 Fragment Tests and Operations / 2.6 Framebuffer

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for '2.1 Rendering Process' in the rendering pipeline?

### Page 4 - 2.1 Rendering Process

Source cue: From 3D models over fragments to pixels

Professor-style explanation: For '2.1 Rendering Process', imagine following one piece of scene data through the renderer. It starts as model or application data, then passes through transformations, primitive processing, rasterization, fragment processing, tests, and finally the framebuffer. The slide gives us this anchor: From 3D models over fragments to pixels. The important point is that each stage changes the representation, so debugging means asking where the representation first became wrong.

Technical commentary: This slide is about 2.1 Rendering Process. Read it as a data-flow explanation: scene or model data is processed step by step until valid framebuffer updates remain. The visible cue is: From 3D models over fragments to pixels

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for '2.1 Rendering Process' in the rendering pipeline?

### Page 5 - Geometry-based Rendering 1/2

Source cue: CPU Application GPU Rendering Display Hardware / Rendering / 3D Model Framebuffer / Process / Video

Professor-style explanation: For 'Geometry-based Rendering 1/2', imagine following one piece of scene data through the renderer. It starts as model or application data, then passes through transformations, primitive processing, rasterization, fragment processing, tests, and finally the framebuffer. The slide gives us this anchor: CPU Application GPU Rendering Display Hardware / Rendering / 3D Model Framebuffer / Process / Video. The important point is that each stage changes the representation, so debugging means asking where the representation first became wrong.

Technical commentary: This slide is about Geometry-based Rendering 1/2. Read it as a data-flow explanation: scene or model data is processed step by step until valid framebuffer updates remain. The visible cue is: CPU Application GPU Rendering Display Hardware / Rendering / 3D Model Framebuffer / Process / Video

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'Geometry-based Rendering 1/2' in the rendering pipeline?

### Page 6 - Geometry-based Rendering 2/2

Source cue: - The rendering process is realized through the rendering pipeline / - Renders 3D models to 2D images / - Conceptually, the rendering pipeline consists of two GPU stages / - Geometry stage – processes geometric primitives / - Rasterization stage – processes fragments and pixels

Professor-style explanation: For 'Geometry-based Rendering 2/2', imagine following one piece of scene data through the renderer. It starts as model or application data, then passes through transformations, primitive processing, rasterization, fragment processing, tests, and finally the framebuffer. The slide gives us this anchor: - The rendering process is realized through the rendering pipeline / - Renders 3D models to 2D images / - Conceptually, the rendering pipeline consists of two GPU stages / - Geometry stage – processes geometric primitives / - Rasterization stage – processes fragments and pixels. The important point is that each stage changes the representation, so debugging means asking where the representation first became wrong.

Technical commentary: This slide is about Geometry-based Rendering 2/2. Read it as a data-flow explanation: scene or model data is processed step by step until valid framebuffer updates remain. The visible cue is: - The rendering process is realized through the rendering pipeline / - Renders 3D models to 2D images / - Conceptually, the rendering pipeline consists of two GPU stages / - Geometry stage – processes geometric primitives / - Rasterization stage – processes fragments and pixels

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'Geometry-based Rendering 2/2' in the rendering pipeline?

### Page 7 - Application Stage

Source cue: - Specification of the model elements and the scene / as well as interaction capabilities / - Scene modeling: arrangement and attribution of the scene objects / - Calculation of animation paths / - Collision detection

Professor-style explanation: For 'Application Stage', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Specification of the model elements and the scene / as well as interaction capabilities / - Scene modeling: arrangement and attribution of the scene objects / - Calculation of animation paths / - Collision detection. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Application Stage. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Specification of the model elements and the scene / as well as interaction capabilities / - Scene modeling: arrangement and attribution of the scene objects / - Calculation of animation paths / - Collision detection

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Application Stage' into a causal sentence instead of repeating the slide title?

### Page 8 - Geometry Stage

Source cue: x x / - Geometric 3D transformation / Model Coordinate System World Coordinate System / - Alignment of individual scene objects in the overall scene / - Basic transformations: translation, scaling, rotation

Professor-style explanation: For 'Geometry Stage', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: x x / - Geometric 3D transformation / Model Coordinate System World Coordinate System / - Alignment of individual scene objects in the overall scene / - Basic transformations: translation, scaling, rotation. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Geometry Stage. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: x x / - Geometric 3D transformation / Model Coordinate System World Coordinate System / - Alignment of individual scene objects in the overall scene / - Basic transformations: translation, scaling, rotation

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Geometry Stage'?

### Page 9 - Rasterization Stage

Source cue: - Conversion of primitives into fragments (rasterization) / - Discretization takes place in relation to a target grid / - Rasterization algorithms optimized for certain primitives / (e.g., lines, triangles) / - After rasterization per-fragment tests are performed

Professor-style explanation: Here the lecture moves from continuous geometry to a discrete grid. 'Rasterization Stage' asks which pixels or samples are covered by an ideal mathematical primitive. The slide gives us this anchor: - Conversion of primitives into fragments (rasterization) / - Discretization takes place in relation to a target grid / - Rasterization algorithms optimized for certain primitives / (e.g., lines, triangles) / - After rasterization per-fragment tests are performed. The key spoken explanation is: rasterization creates fragment candidates and interpolated values, but it does not by itself guarantee that a fragment becomes the final visible pixel.

Technical commentary: This slide is about Rasterization Stage. Read it as continuous-to-discrete conversion. The core question is which samples are covered and which interpolated values each fragment receives. The visible cue is: - Conversion of primitives into fragments (rasterization) / - Discretization takes place in relation to a target grid / - Rasterization algorithms optimized for certain primitives / (e.g., lines, triangles) / - After rasterization per-fragment tests are performed

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Rasterization Stage'?

### Page 10 - 2.2 OpenGL Overview

Source cue: Library for real-time computer graphics

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. '2.2 OpenGL Overview' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: Library for real-time computer graphics. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about 2.2 OpenGL Overview. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: Library for real-time computer graphics

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2.2 OpenGL Overview'?

### Page 11 - OpenGL History

Source cue: - Unified graphics software interface was missing / as knowledge channeled into proprietary software packages / - HP's starbase / - SGI's Graphics Library (GL) / - Some standardization efforts existed

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL History' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Unified graphics software interface was missing / as knowledge channeled into proprietary software packages / - HP's starbase / - SGI's Graphics Library (GL) / - Some standardization efforts existed. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL History. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Unified graphics software interface was missing / as knowledge channeled into proprietary software packages / - HP's starbase / - SGI's Graphics Library (GL) / - Some standardization efforts existed

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL History'?

### Page 12 - OpenGL

Source cue: - OpenGL (Open Graphics Library) / - Platform independent 2D and 3D graphics API / - API specification is provided by the Khronos Group / - Technical implementation / - Rendering pipeline consisting of static and programmable pipeline stages

Professor-style explanation: For 'OpenGL', imagine following one piece of scene data through the renderer. It starts as model or application data, then passes through transformations, primitive processing, rasterization, fragment processing, tests, and finally the framebuffer. The slide gives us this anchor: - OpenGL (Open Graphics Library) / - Platform independent 2D and 3D graphics API / - API specification is provided by the Khronos Group / - Technical implementation / - Rendering pipeline consisting of static and programmable pipeline stages. The important point is that each stage changes the representation, so debugging means asking where the representation first became wrong.

Technical commentary: This slide is about OpenGL. Read it as a data-flow explanation: scene or model data is processed step by step until valid framebuffer updates remain. The visible cue is: - OpenGL (Open Graphics Library) / - Platform independent 2D and 3D graphics API / - API specification is provided by the Khronos Group / - Technical implementation / - Rendering pipeline consisting of static and programmable pipeline stages

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'OpenGL' in the rendering pipeline?

### Page 13 - OpenGL vs. Vulkan

Source cue: - How about Vulkan? / - More modern than OpenGL / - Designed for high performance and low-level GPU control / - Better suited for complex, large-scale rendering engines / - Vulkan also harder to learn and requires more setup/code

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL vs. Vulkan' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - How about Vulkan? / - More modern than OpenGL / - Designed for high performance and low-level GPU control / - Better suited for complex, large-scale rendering engines / - Vulkan also harder to learn and requires more setup/code. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL vs. Vulkan. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - How about Vulkan? / - More modern than OpenGL / - Designed for high performance and low-level GPU control / - Better suited for complex, large-scale rendering engines / - Vulkan also harder to learn and requires more setup/code

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL vs. Vulkan'?

### Page 14 - OpenGL Libraries

Source cue: - Different tastes of OpenGL / - OpenGL / - OpenGL ES - limited version for embedded systems / - WebGL - Javascript connection for Web Development / (functionality similar to OpenGL ES)

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL Libraries' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Different tastes of OpenGL / - OpenGL / - OpenGL ES - limited version for embedded systems / - WebGL - Javascript connection for Web Development / (functionality similar to OpenGL ES). If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL Libraries. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Different tastes of OpenGL / - OpenGL / - OpenGL ES - limited version for embedded systems / - WebGL - Javascript connection for Web Development / (functionality similar to OpenGL ES)

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Libraries'?

### Page 15 - OpenGL Functionality

Source cue: - Functional API / - Objects, scenes and images are described by a sequence of commands / (functional approach, low-level) / - Contrast: scene or object description (declarative approach, high-level) / - OpenGL context

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL Functionality' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Functional API / - Objects, scenes and images are described by a sequence of commands / (functional approach, low-level) / - Contrast: scene or object description (declarative approach, high-level) / - OpenGL context. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL Functionality. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Functional API / - Objects, scenes and images are described by a sequence of commands / (functional approach, low-level) / - Contrast: scene or object description (declarative approach, high-level) / - OpenGL context

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Functionality'?

### Page 16 - OpenGL Context

Source cue: - Context is created and modified by the application, / and contains all the state variables of the OpenGL engine / - Any number of contexts per application possible, / but at most one active context per application / - Context is generally tied to an output window

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL Context' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Context is created and modified by the application, / and contains all the state variables of the OpenGL engine / - Any number of contexts per application possible, / but at most one active context per application / - Context is generally tied to an output window. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL Context. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Context is created and modified by the application, / and contains all the state variables of the OpenGL engine / - Any number of contexts per application possible, / but at most one active context per application / - Context is generally tied to an output window

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Context'?

### Page 17 - OpenGL Rendering Process

Source cue: - Initiation from the developer's perspective / - Creation of the output window / - Creation of the context / - Specification of the scene geometry / - Uploading of the scene geometry to the GPU

Professor-style explanation: For 'OpenGL Rendering Process', imagine following one piece of scene data through the renderer. It starts as model or application data, then passes through transformations, primitive processing, rasterization, fragment processing, tests, and finally the framebuffer. The slide gives us this anchor: - Initiation from the developer's perspective / - Creation of the output window / - Creation of the context / - Specification of the scene geometry / - Uploading of the scene geometry to the GPU. The important point is that each stage changes the representation, so debugging means asking where the representation first became wrong.

Technical commentary: This slide is about OpenGL Rendering Process. Read it as a data-flow explanation: scene or model data is processed step by step until valid framebuffer updates remain. The visible cue is: - Initiation from the developer's perspective / - Creation of the output window / - Creation of the context / - Specification of the scene geometry / - Uploading of the scene geometry to the GPU

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'OpenGL Rendering Process' in the rendering pipeline?

### Page 18 - Window Creation with GLFW 1/2

Source cue: #include <GLFW/glfw3.h> / #include <stdlib.h> / #include <stdio.h> / static void error_callback(int error, const char* description) { / fputs(description, stderr);

Professor-style explanation: For 'Window Creation with GLFW 1/2', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: #include <GLFW/glfw3.h> / #include <stdlib.h> / #include <stdio.h> / static void error_callback(int error, const char* description) { / fputs(description, stderr). Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Window Creation with GLFW 1/2. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: #include <GLFW/glfw3.h> / #include <stdlib.h> / #include <stdio.h> / static void error_callback(int error, const char* description) { / fputs(description, stderr);

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Window Creation with GLFW 1/2' into a causal sentence instead of repeating the slide title?

### Page 19 - Window Creation with GLFW 2/2

Source cue: int main(void){ / GLFWwindow* window; / glfwSetErrorCallback(error_callback); / if (!glfwInit()) exit(EXIT_FAILURE); / window = glfwCreateWindow(640, 480, "Simple example", NULL, NULL);

Professor-style explanation: For 'Window Creation with GLFW 2/2', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: int main(void){ / GLFWwindow* window; / glfwSetErrorCallback(error_callback); / if (!glfwInit()) exit(EXIT_FAILURE); / window = glfwCreateWindow(640, 480, "Simple example", NULL, NULL). Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Window Creation with GLFW 2/2. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: int main(void){ / GLFWwindow* window; / glfwSetErrorCallback(error_callback); / if (!glfwInit()) exit(EXIT_FAILURE); / window = glfwCreateWindow(640, 480, "Simple example", NULL, NULL);

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Window Creation with GLFW 2/2' into a causal sentence instead of repeating the slide title?

### Page 20 - OpenGL Naming Conventions

Source cue: - Function-Prefix "gl" / - glClear, ... / - Constant-Prefix "GL" / - GL_POLYGON, GL_LINES, ... / - Parameter types are explicitly encoded in function names

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL Naming Conventions' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Function-Prefix "gl" / - glClear, ... / - Constant-Prefix "GL" / - GL_POLYGON, GL_LINES, ... / - Parameter types are explicitly encoded in function names. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL Naming Conventions. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Function-Prefix "gl" / - glClear, ... / - Constant-Prefix "GL" / - GL_POLYGON, GL_LINES, ... / - Parameter types are explicitly encoded in function names

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Naming Conventions'?

### Page 21 - 2.3 OpenGL Rendering

Source cue: Transfer of 3D models to the GPU

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. '2.3 OpenGL Rendering' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: Transfer of 3D models to the GPU. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about 2.3 OpenGL Rendering. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: Transfer of 3D models to the GPU

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2.3 OpenGL Rendering'?

### Page 22 - OpenGL Rendering (until V2.1)

Source cue: - Rendering is done through Immediate Mode / void renderScene() { / glColor3f(0.0f, 1.0f, 0.0f); // drawing color becomes green / glBegin(GL_POLYGON); // begin primitive / glVertex2f(-0.5f,-0.5f); // 1. vertex

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL Rendering (until V2.1)' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Rendering is done through Immediate Mode / void renderScene() { / glColor3f(0.0f, 1.0f, 0.0f); // drawing color becomes green / glBegin(GL_POLYGON); // begin primitive / glVertex2f(-0.5f,-0.5f); // 1. vertex. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL Rendering (until V2.1). Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Rendering is done through Immediate Mode / void renderScene() { / glColor3f(0.0f, 1.0f, 0.0f); // drawing color becomes green / glBegin(GL_POLYGON); // begin primitive / glVertex2f(-0.5f,-0.5f); // 1. vertex

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Rendering (until V2.1)'?

### Page 23 - OpenGL Rendering (since V3.0)

Source cue: - Using Vertex Array Objects (VAOs) / - Vertex specification in CPU memory / - Vertex data transfer from CPU to GPU / - Memory layout description of the vertex data / - Number of vertices, number of components (x, y, z, ...)

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL Rendering (since V3.0)' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Using Vertex Array Objects (VAOs) / - Vertex specification in CPU memory / - Vertex data transfer from CPU to GPU / - Memory layout description of the vertex data / - Number of vertices, number of components (x, y, z, ...). If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL Rendering (since V3.0). Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Using Vertex Array Objects (VAOs) / - Vertex specification in CPU memory / - Vertex data transfer from CPU to GPU / - Memory layout description of the vertex data / - Number of vertices, number of components (x, y, z, ...)

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Rendering (since V3.0)'?

### Page 24 - 1. Vertex Specification

Source cue: - Vertex data is specified as a C array / // vertices of two triangles / GLfloat vertices[6][2] = { // 6 vertices with two components each (x,y) / {0.0, 1.0}, {1.0, 1.0}, {1.0, 0.0}, // 1. triangle / {0.5, 0.5}, {1.0, 0.3}, {0.7, 1.0} // 2. triangle

Professor-style explanation: Here the lecture moves from continuous geometry to a discrete grid. '1. Vertex Specification' asks which pixels or samples are covered by an ideal mathematical primitive. The slide gives us this anchor: - Vertex data is specified as a C array / // vertices of two triangles / GLfloat vertices[6][2] = { // 6 vertices with two components each (x,y) / {0.0, 1.0}, {1.0, 1.0}, {1.0, 0.0}, // 1. triangle / {0.5, 0.5}, {1.0, 0.3}, {0.7, 1.0} // 2. triangle. The key spoken explanation is: rasterization creates fragment candidates and interpolated values, but it does not by itself guarantee that a fragment becomes the final visible pixel.

Technical commentary: This slide is about 1. Vertex Specification. Read it as continuous-to-discrete conversion. The core question is which samples are covered and which interpolated values each fragment receives. The visible cue is: - Vertex data is specified as a C array / // vertices of two triangles / GLfloat vertices[6][2] = { // 6 vertices with two components each (x,y) / {0.0, 1.0}, {1.0, 1.0}, {1.0, 0.0}, // 1. triangle / {0.5, 0.5}, {1.0, 0.3}, {0.7, 1.0} // 2. triangle

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by '1. Vertex Specification'?

### Page 25 - 2. Vertex Data Transfer

Source cue: - VBO allocation and data transfer via / - glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW); / - data – address in main memory (i.e., vertices or &vertices[0]) / - size – size of data in number of bytes / (i.e. sizeof(vertices) or numVertices*sizeof(GLfloat)*2)

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. '2. Vertex Data Transfer' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - VBO allocation and data transfer via / - glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW); / - data – address in main memory (i.e., vertices or &vertices[0]) / - size – size of data in number of bytes / (i.e. sizeof(vertices) or numVertices*sizeof(GLfloat)*2). If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about 2. Vertex Data Transfer. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - VBO allocation and data transfer via / - glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW); / - data – address in main memory (i.e., vertices or &vertices[0]) / - size – size of data in number of bytes / (i.e. sizeof(vertices) or numVertices*sizeof(GLfloat)*2)

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2. Vertex Data Transfer'?

### Page 26 - 3. Memory Layout Description

Source cue: - Memory layout is described by the following function / - glVertexAttribPointer(attribIndex, size, type, normalized, stride, offset); / - attribIndex – attribute number (0 for position, later more ...) / - size – number of components per vertex (2 for xy, 3 for xyz) / - type – base type (typically GL_FLOAT or GL_DOUBLE)

Professor-style explanation: This slide belongs to local shading. For '3. Memory Layout Description', imagine one visible surface point and ask how bright or colored it should become. The slide gives us this anchor: - Memory layout is described by the following function / - glVertexAttribPointer(attribIndex, size, type, normalized, stride, offset); / - attribIndex – attribute number (0 for position, later more ...) / - size – number of components per vertex (2 for xy, 3 for xyz) / - type – base type (typically GL_FLOAT or GL_DOUBLE). The professor explanation must name the normal, light direction, view direction, material response, and whether the calculation is done per vertex or per fragment.

Technical commentary: This slide is about 3. Memory Layout Description. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: - Memory layout is described by the following function / - glVertexAttribPointer(attribIndex, size, type, normalized, stride, offset); / - attribIndex – attribute number (0 for position, later more ...) / - size – number of components per vertex (2 for xy, 3 for xyz) / - type – base type (typically GL_FLOAT or GL_DOUBLE)

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '3. Memory Layout Description'?

### Page 27 - 4. VAO Drawing 1/2

Source cue: - Drawing is done with the command / - glDrawArrays(mode, first, count); / - mode – specifies the primitive type (e.g., GL_TRIANGLES or GL_LINES) / - From all vertices, the next count vertices are drawn from index first / - Actual vertex data no longer needs to be specified

Professor-style explanation: Here the lecture moves from continuous geometry to a discrete grid. '4. VAO Drawing 1/2' asks which pixels or samples are covered by an ideal mathematical primitive. The slide gives us this anchor: - Drawing is done with the command / - glDrawArrays(mode, first, count); / - mode – specifies the primitive type (e.g., GL_TRIANGLES or GL_LINES) / - From all vertices, the next count vertices are drawn from index first / - Actual vertex data no longer needs to be specified. The key spoken explanation is: rasterization creates fragment candidates and interpolated values, but it does not by itself guarantee that a fragment becomes the final visible pixel.

Technical commentary: This slide is about 4. VAO Drawing 1/2. Read it as continuous-to-discrete conversion. The core question is which samples are covered and which interpolated values each fragment receives. The visible cue is: - Drawing is done with the command / - glDrawArrays(mode, first, count); / - mode – specifies the primitive type (e.g., GL_TRIANGLES or GL_LINES) / - From all vertices, the next count vertices are drawn from index first / - Actual vertex data no longer needs to be specified

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by '4. VAO Drawing 1/2'?

### Page 28 - 4. VAO Drawing 2/2

Source cue: - There is a small number of primitive types / - Points / - Lines, Line Strips, Line Loops / - Triangles, Triangle Strips, Triangle Fans, Patches / v2 v2 v2

Professor-style explanation: Here the lecture moves from continuous geometry to a discrete grid. '4. VAO Drawing 2/2' asks which pixels or samples are covered by an ideal mathematical primitive. The slide gives us this anchor: - There is a small number of primitive types / - Points / - Lines, Line Strips, Line Loops / - Triangles, Triangle Strips, Triangle Fans, Patches / v2 v2 v2. The key spoken explanation is: rasterization creates fragment candidates and interpolated values, but it does not by itself guarantee that a fragment becomes the final visible pixel.

Technical commentary: This slide is about 4. VAO Drawing 2/2. Read it as continuous-to-discrete conversion. The core question is which samples are covered and which interpolated values each fragment receives. The visible cue is: - There is a small number of primitive types / - Points / - Lines, Line Strips, Line Loops / - Triangles, Triangle Strips, Triangle Fans, Patches / v2 v2 v2

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by '4. VAO Drawing 2/2'?

### Page 29 - 5. GPU Memory Release

Source cue: - After usage VAO and VBO should be deleted from GPU memory / - glDeleteBuffers(…); / - glDeleteVertexArrays(…);

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. '5. GPU Memory Release' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - After usage VAO and VBO should be deleted from GPU memory / - glDeleteBuffers(…); / - glDeleteVertexArrays(…). If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about 5. GPU Memory Release. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - After usage VAO and VBO should be deleted from GPU memory / - glDeleteBuffers(…); / - glDeleteVertexArrays(…);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '5. GPU Memory Release'?

### Page 30 - Rendering Initialization 1/2

Source cue: static void init_render_scene(void) { / static const GLfloat vertices[6][2] = { / {0.0f, 1.0f}, {1.0f, 1.0f}, {1.0f, 0.0f}, /* 1st triangle */ / {0.5f, 0.5f}, {1.0f, 0.3f}, {0.7f, 1.0f} /* 2nd triangle */ / static const char* vs_src =

Professor-style explanation: Here the lecture moves from continuous geometry to a discrete grid. 'Rendering Initialization 1/2' asks which pixels or samples are covered by an ideal mathematical primitive. The slide gives us this anchor: static void init_render_scene(void) { / static const GLfloat vertices[6][2] = { / {0.0f, 1.0f}, {1.0f, 1.0f}, {1.0f, 0.0f}, /* 1st triangle */ / {0.5f, 0.5f}, {1.0f, 0.3f}, {0.7f, 1.0f} /* 2nd triangle */ / static const char* vs_src =. The key spoken explanation is: rasterization creates fragment candidates and interpolated values, but it does not by itself guarantee that a fragment becomes the final visible pixel.

Technical commentary: This slide is about Rendering Initialization 1/2. Read it as continuous-to-discrete conversion. The core question is which samples are covered and which interpolated values each fragment receives. The visible cue is: static void init_render_scene(void) { / static const GLfloat vertices[6][2] = { / {0.0f, 1.0f}, {1.0f, 1.0f}, {1.0f, 0.0f}, /* 1st triangle */ / {0.5f, 0.5f}, {1.0f, 0.3f}, {0.7f, 1.0f} /* 2nd triangle */ / static const char* vs_src =

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Rendering Initialization 1/2'?

### Page 31 - Rendering Initialization 2/2

Source cue: program = create_program(vs_src, fs_src); / glGenVertexArrays(1, &vao); / glGenBuffers(1, &vbo); / glBindVertexArray(vao); / glBindBuffer(GL_ARRAY_BUFFER, vbo);

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Rendering Initialization 2/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: program = create_program(vs_src, fs_src); / glGenVertexArrays(1, &vao); / glGenBuffers(1, &vbo); / glBindVertexArray(vao); / glBindBuffer(GL_ARRAY_BUFFER, vbo). If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Rendering Initialization 2/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: program = create_program(vs_src, fs_src); / glGenVertexArrays(1, &vao); / glGenBuffers(1, &vbo); / glBindVertexArray(vao); / glBindBuffer(GL_ARRAY_BUFFER, vbo);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Rendering Initialization 2/2'?

### Page 32 - Rendering

Source cue: static void render_scene(void) { / glClear(GL_COLOR_BUFFER_BIT); / glUseProgram(program); / glBindVertexArray(vao); / glDrawArrays(GL_TRIANGLES, 0, 6);

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Rendering' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: static void render_scene(void) { / glClear(GL_COLOR_BUFFER_BIT); / glUseProgram(program); / glBindVertexArray(vao); / glDrawArrays(GL_TRIANGLES, 0, 6). If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Rendering. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: static void render_scene(void) { / glClear(GL_COLOR_BUFFER_BIT); / glUseProgram(program); / glBindVertexArray(vao); / glDrawArrays(GL_TRIANGLES, 0, 6);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Rendering'?

### Page 33 - Additional Attributes

Source cue: - Additional attributes are necessary for drawing / - Color, normals, texture coordinates, ... / - There are two ways to assign these attributes to the vertex data / - Attributes are bound to the same VAO in separate VBO / - Attributes are stored interleaved with vertex data,

Professor-style explanation: For 'Additional Attributes', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Additional attributes are necessary for drawing / - Color, normals, texture coordinates, ... / - There are two ways to assign these attributes to the vertex data / - Attributes are bound to the same VAO in separate VBO / - Attributes are stored interleaved with vertex data,. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Additional Attributes. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Additional attributes are necessary for drawing / - Color, normals, texture coordinates, ... / - There are two ways to assign these attributes to the vertex data / - Attributes are bound to the same VAO in separate VBO / - Attributes are stored interleaved with vertex data,

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Additional Attributes'?

### Page 34 - 2.4 OpenGL Rendering Pipeline

Source cue: Programmable and static stages

Professor-style explanation: For '2.4 OpenGL Rendering Pipeline', imagine following one piece of scene data through the renderer. It starts as model or application data, then passes through transformations, primitive processing, rasterization, fragment processing, tests, and finally the framebuffer. The slide gives us this anchor: Programmable and static stages. The important point is that each stage changes the representation, so debugging means asking where the representation first became wrong.

Technical commentary: This slide is about 2.4 OpenGL Rendering Pipeline. Read it as a data-flow explanation: scene or model data is processed step by step until valid framebuffer updates remain. The visible cue is: Programmable and static stages

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for '2.4 OpenGL Rendering Pipeline' in the rendering pipeline?

### Page 35 - The Rendering Pipeline 1/2

Source cue: Scene Description Raster Image / Geometry Fragment / Rasterization / Processing Processing / Vertices Primitives Fragments Pixels

Professor-style explanation: For 'The Rendering Pipeline 1/2', imagine following one piece of scene data through the renderer. It starts as model or application data, then passes through transformations, primitive processing, rasterization, fragment processing, tests, and finally the framebuffer. The slide gives us this anchor: Scene Description Raster Image / Geometry Fragment / Rasterization / Processing Processing / Vertices Primitives Fragments Pixels. The important point is that each stage changes the representation, so debugging means asking where the representation first became wrong.

Technical commentary: This slide is about The Rendering Pipeline 1/2. Read it as a data-flow explanation: scene or model data is processed step by step until valid framebuffer updates remain. The visible cue is: Scene Description Raster Image / Geometry Fragment / Rasterization / Processing Processing / Vertices Primitives Fragments Pixels

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'The Rendering Pipeline 1/2' in the rendering pipeline?

### Page 36 - The Rendering Pipeline 2/2

Source cue: - Sequence of fixed and programmable stages Programmable / Vertex Processing / - Process is influenced by context and scene objects / Context Fixed Function / - Programmable levels are programmed

Professor-style explanation: For 'The Rendering Pipeline 2/2', imagine following one piece of scene data through the renderer. It starts as model or application data, then passes through transformations, primitive processing, rasterization, fragment processing, tests, and finally the framebuffer. The slide gives us this anchor: - Sequence of fixed and programmable stages Programmable / Vertex Processing / - Process is influenced by context and scene objects / Context Fixed Function / - Programmable levels are programmed. The important point is that each stage changes the representation, so debugging means asking where the representation first became wrong.

Technical commentary: This slide is about The Rendering Pipeline 2/2. Read it as a data-flow explanation: scene or model data is processed step by step until valid framebuffer updates remain. The visible cue is: - Sequence of fixed and programmable stages Programmable / Vertex Processing / - Process is influenced by context and scene objects / Context Fixed Function / - Programmable levels are programmed

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'The Rendering Pipeline 2/2' in the rendering pipeline?

### Page 37 - Shader Programming – History 1/2

Source cue: - There is special graphics hardware (dedicated) / and general graphics hardware (general purpose) / - Special graphics hardware / - Volume Rendering: VolumePro / - Game consoles: Custom NVIDIA chips in XBox

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Shader Programming – History 1/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - There is special graphics hardware (dedicated) / and general graphics hardware (general purpose) / - Special graphics hardware / - Volume Rendering: VolumePro / - Game consoles: Custom NVIDIA chips in XBox. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Shader Programming – History 1/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - There is special graphics hardware (dedicated) / and general graphics hardware (general purpose) / - Special graphics hardware / - Volume Rendering: VolumePro / - Game consoles: Custom NVIDIA chips in XBox

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Programming – History 1/2'?

### Page 38 - Shader Programming – History 2/2

Source cue: - Various vendor-dependent extensions are introduced / to provide extensibility for general graphics hardware / - Texture shaders and register combiners allowed modification / through the application of textures / - Applicability is very limited by the possibilities of graphics hardware

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Shader Programming – History 2/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Various vendor-dependent extensions are introduced / to provide extensibility for general graphics hardware / - Texture shaders and register combiners allowed modification / through the application of textures / - Applicability is very limited by the possibilities of graphics hardware. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Shader Programming – History 2/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Various vendor-dependent extensions are introduced / to provide extensibility for general graphics hardware / - Texture shaders and register combiners allowed modification / through the application of textures / - Applicability is very limited by the possibilities of graphics hardware

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Programming – History 2/2'?

### Page 39 - Assembler Shader

Source cue: - First OpenGL extensions support shader programming in assembler code / !! ARBvp1.0 / ATTRIB iPos = vertex.position ; / ATTRIB iNormal = vertex.normal ; / ...

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Assembler Shader' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - First OpenGL extensions support shader programming in assembler code / !! ARBvp1.0 / ATTRIB iPos = vertex.position ; / ATTRIB iNormal = vertex.normal ; / . If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Assembler Shader. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - First OpenGL extensions support shader programming in assembler code / !! ARBvp1.0 / ATTRIB iPos = vertex.position ; / ATTRIB iNormal = vertex.normal ; / ...

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Assembler Shader'?

### Page 40 - High-Level Shading Languages 1/2

Source cue: - Assembler code is hard to read and hard to maintain / - High-level languages f or shading are specified in C-like syntax / - Source code is translated by the compiler into appropriate ASM statements / - Using shaders after initial binding automatically when rendering geometry / - Interface to OpenGL by passing appropriate variables or changing the OpenGL

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'High-Level Shading Languages 1/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Assembler code is hard to read and hard to maintain / - High-level languages f or shading are specified in C-like syntax / - Source code is translated by the compiler into appropriate ASM statements / - Using shaders after initial binding automatically when rendering geometry / - Interface to OpenGL by passing appropriate variables or changing the OpenGL. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about High-Level Shading Languages 1/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Assembler code is hard to read and hard to maintain / - High-level languages f or shading are specified in C-like syntax / - Source code is translated by the compiler into appropriate ASM statements / - Using shaders after initial binding automatically when rendering geometry / - Interface to OpenGL by passing appropriate variables or changing the OpenGL

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'High-Level Shading Languages 1/2'?

### Page 41 - High-Level Shading Languages 2/2

Source cue: - Existing high level languages f or shader development / - CG - C for Graphics by NVIDIA / - CG was introduced in 2003 by NVIDIA as a platform independent solution / (in practice rather semi-platform independent) / - HLSL - High Level Shading Language from Microsoft

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'High-Level Shading Languages 2/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Existing high level languages f or shader development / - CG - C for Graphics by NVIDIA / - CG was introduced in 2003 by NVIDIA as a platform independent solution / (in practice rather semi-platform independent) / - HLSL - High Level Shading Language from Microsoft. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about High-Level Shading Languages 2/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Existing high level languages f or shader development / - CG - C for Graphics by NVIDIA / - CG was introduced in 2003 by NVIDIA as a platform independent solution / (in practice rather semi-platform independent) / - HLSL - High Level Shading Language from Microsoft

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'High-Level Shading Languages 2/2'?

### Page 42 - Shader Types

Source cue: - Pipeline concept has been kept in place / and shaders are responsible for different stages / - First, geometry level programming was done by vertex shaders / - Vertex shaders allow modifiability of vertex transformations and lighting / - After that, there was an extension for image-based algorithms by fragment

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Shader Types' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Pipeline concept has been kept in place / and shaders are responsible for different stages / - First, geometry level programming was done by vertex shaders / - Vertex shaders allow modifiability of vertex transformations and lighting / - After that, there was an extension for image-based algorithms by fragment. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Shader Types. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Pipeline concept has been kept in place / and shaders are responsible for different stages / - First, geometry level programming was done by vertex shaders / - Vertex shaders allow modifiability of vertex transformations and lighting / - After that, there was an extension for image-based algorithms by fragment

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Types'?

### Page 43 - Vertex Shader Concepts

Source cue: - Vertex shaders enable the programmable modification of processed geometry / - Possibilities of a vertex shader / Programmable / - Geometric transformation of vertices and normals / Vertex Processing

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Vertex Shader Concepts' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Vertex shaders enable the programmable modification of processed geometry / - Possibilities of a vertex shader / Programmable / - Geometric transformation of vertices and normals / Vertex Processing. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Vertex Shader Concepts. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Vertex shaders enable the programmable modification of processed geometry / - Possibilities of a vertex shader / Programmable / - Geometric transformation of vertices and normals / Vertex Processing

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Concepts'?

### Page 44 - Vertex Shader Examples 1/2

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Vertex Shader Examples 1/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Vertex Shader Examples 1/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Examples 1/2'?

### Page 45 - Vertex Shader Examples 2/2

Source cue: - Morphing / - Shadow volume calculation for shadow effects / [ID Software‘s Doom III]

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Vertex Shader Examples 2/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Morphing / - Shadow volume calculation for shadow effects / [ID Software‘s Doom III]. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Vertex Shader Examples 2/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Morphing / - Shadow volume calculation for shadow effects / [ID Software‘s Doom III]

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Examples 2/2'?

### Page 46 - Vertex Shader Coordinate Systems 1/2

Source cue: - Vertex shaders are executed for each vertex / - Vertex shaders calculate coordinates in clipping coordinates as output / - Vertex shaders can not / - Access adjacent vertices / - Change the number of vertices (i.e., generate or discard vertices)

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Vertex Shader Coordinate Systems 1/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Vertex shaders are executed for each vertex / - Vertex shaders calculate coordinates in clipping coordinates as output / - Vertex shaders can not / - Access adjacent vertices / - Change the number of vertices (i.e., generate or discard vertices). If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Vertex Shader Coordinate Systems 1/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Vertex shaders are executed for each vertex / - Vertex shaders calculate coordinates in clipping coordinates as output / - Vertex shaders can not / - Access adjacent vertices / - Change the number of vertices (i.e., generate or discard vertices)

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Coordinate Systems 1/2'?

### Page 47 - Vertex Shader Coordinate Systems 2/2

Source cue: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Vertex Shader Coordinate Systems 2/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Vertex Shader Coordinate Systems 2/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Coordinate Systems 2/2'?

### Page 48 - Local Space

Source cue: - Coordinates of your object relative to its local origin / - 3D vertex positions

Professor-style explanation: For 'Local Space', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Coordinates of your object relative to its local origin / - 3D vertex positions. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Local Space. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Coordinates of your object relative to its local origin / - 3D vertex positions

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Local Space'?

### Page 49 - World Space

Source cue: - Coordinates in respect of a larger world / - Relative to some global origin of the world / - Together with many other objects

Professor-style explanation: For 'World Space', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Coordinates in respect of a larger world / - Relative to some global origin of the world / - Together with many other objects. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about World Space. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Coordinates in respect of a larger world / - Relative to some global origin of the world / - Together with many other objects

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'World Space'?

### Page 50 - View Space

Source cue: - Coordinates as seen from the camera

Professor-style explanation: For 'View Space', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Coordinates as seen from the camera. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about View Space. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Coordinates as seen from the camera

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'View Space'?

### Page 51 - Clip Space

Source cue: - Clip coordinates range from -1 to 1 / - Projection (Orthographic, Perspective)

Professor-style explanation: For 'Clip Space', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Clip coordinates range from -1 to 1 / - Projection (Orthographic, Perspective). The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Clip Space. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Clip coordinates range from -1 to 1 / - Projection (Orthographic, Perspective)

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Clip Space'?

### Page 52 - Screen Space

Source cue: - Transform to image coordinates with glViewport / - Results are sent to the rasterizer

Professor-style explanation: For 'Screen Space', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Transform to image coordinates with glViewport / - Results are sent to the rasterizer. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Screen Space. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Transform to image coordinates with glViewport / - Results are sent to the rasterizer

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Screen Space'?

### Page 53 - Coordinate Systems

Source cue: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform

Professor-style explanation: For 'Coordinate Systems', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Coordinate Systems. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: Local Space World Space View Space Clip Space Screen Space / Viewport / 𝑀 𝑀 𝑀 / 𝑚𝑜𝑑𝑒𝑙 𝑣𝑖𝑒𝑤 𝑝𝑟𝑜𝑗𝑒𝑐𝑡 Transform

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Coordinate Systems'?

### Page 54 - Vertex Shader Variables

Source cue: - Input types / - Uniforms: read only in VS (& FS) // Intrinsic vertex attributes / out gl_PerVertex { / - For example: light position or light color / vec4 gl_Position;

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Vertex Shader Variables' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Input types / - Uniforms: read only in VS (& FS) // Intrinsic vertex attributes / out gl_PerVertex { / - For example: light position or light color / vec4 gl_Position. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Vertex Shader Variables. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Input types / - Uniforms: read only in VS (& FS) // Intrinsic vertex attributes / out gl_PerVertex { / - For example: light position or light color / vec4 gl_Position;

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Vertex Shader Variables'?

### Page 55 - Fixed Function Vertex Postprocessing

Source cue: - Clipping / - Discard invisible geometries / Programmable / - Perspective Division / Vertex Processing

Professor-style explanation: This slide should be read as camera geometry. With 'Fixed Function Vertex Postprocessing', the question is how a 3D view becomes coordinates that can be clipped, divided, mapped to the viewport, and rasterized. The slide gives us this anchor: - Clipping / - Discard invisible geometries / Programmable / - Perspective Division / Vertex Processing. Keep separate the camera/view transform, the projection matrix, the perspective divide, and the final viewport transform; many mistakes come from blending these steps together.

Technical commentary: This slide is about Fixed Function Vertex Postprocessing. Read it as camera geometry. Track how 3D view-space positions become clip coordinates, normalized device coordinates, and finally screen locations. The visible cue is: - Clipping / - Discard invisible geometries / Programmable / - Perspective Division / Vertex Processing

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Check yourself: Can you explain how 'Fixed Function Vertex Postprocessing' changes positions before rasterization?

### Page 56 - Fixed Function Rasterization

Source cue: - Geometry is converted to raster coordinates / Programmable / Vertex Processing / Fixed Function / Primitives Fragments Vertex Postprocessing

Professor-style explanation: For 'Fixed Function Rasterization', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Geometry is converted to raster coordinates / Programmable / Vertex Processing / Fixed Function / Primitives Fragments Vertex Postprocessing. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Fixed Function Rasterization. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Geometry is converted to raster coordinates / Programmable / Vertex Processing / Fixed Function / Primitives Fragments Vertex Postprocessing

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Fixed Function Rasterization'?

### Page 57 - Fragment Shader Concept 1/2

Source cue: - Fragment shaders set the color of a pixel / - Possibilities of a fragment shader / Programmable / - Glare of textures / Vertex Processing

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Fragment Shader Concept 1/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Fragment shaders set the color of a pixel / - Possibilities of a fragment shader / Programmable / - Glare of textures / Vertex Processing. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Fragment Shader Concept 1/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Fragment shaders set the color of a pixel / - Possibilities of a fragment shader / Programmable / - Glare of textures / Vertex Processing

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Fragment Shader Concept 1/2'?

### Page 58 - Fragment Shader Concept 2/2

Source cue: - Fragment shaders are executed for fragments (= pixel predecessors) / - Fragment shaders calculate the color and depth value of the current fragment / - No information about adjacent fragments available / - The number of fragments can be changed / - Fragment shaders can not generate fragments

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Fragment Shader Concept 2/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Fragment shaders are executed for fragments (= pixel predecessors) / - Fragment shaders calculate the color and depth value of the current fragment / - No information about adjacent fragments available / - The number of fragments can be changed / - Fragment shaders can not generate fragments. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Fragment Shader Concept 2/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Fragment shaders are executed for fragments (= pixel predecessors) / - Fragment shaders calculate the color and depth value of the current fragment / - No information about adjacent fragments available / - The number of fragments can be changed / - Fragment shaders can not generate fragments

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Fragment Shader Concept 2/2'?

### Page 59 - Shader Example

Source cue: layout (std140) uniform Matrices { Vertex Shader / mat4 projModelViewMatrix; / mat3 normalMatrix; /** Fragment Shader / }; * Set fragment color to red. / in vec3 position;

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Shader Example' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: layout (std140) uniform Matrices { Vertex Shader / mat4 projModelViewMatrix; / mat3 normalMatrix; /** Fragment Shader / }; * Set fragment color to red. / in vec3 position. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Shader Example. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: layout (std140) uniform Matrices { Vertex Shader / mat4 projModelViewMatrix; / mat3 normalMatrix; /** Fragment Shader / }; * Set fragment color to red. / in vec3 position;

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Example'?

### Page 60 - GLSL Shader Functions

Source cue: - Trigonometry functions / - radians, degrees, sin, cos, tan, asin, acos, atan / - Power calculations / - pow, exp2, log2, sqrt, inversesqrt / - General

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'GLSL Shader Functions' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Trigonometry functions / - radians, degrees, sin, cos, tan, asin, acos, atan / - Power calculations / - pow, exp2, log2, sqrt, inversesqrt / - General. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about GLSL Shader Functions. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Trigonometry functions / - radians, degrees, sin, cos, tan, asin, acos, atan / - Power calculations / - pow, exp2, log2, sqrt, inversesqrt / - General

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'GLSL Shader Functions'?

### Page 61 - Shader Usage

Source cue: - One or multiple shaders are attached to a shader program / Vertex Shader / glCreateShader glCreateProgram / Fragment Shader / glShaderSource glAttachShader glCreateShader

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Shader Usage' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - One or multiple shaders are attached to a shader program / Vertex Shader / glCreateShader glCreateProgram / Fragment Shader / glShaderSource glAttachShader glCreateShader. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Shader Usage. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - One or multiple shaders are attached to a shader program / Vertex Shader / glCreateShader glCreateProgram / Fragment Shader / glShaderSource glAttachShader glCreateShader

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Usage'?

### Page 62 - Binding Shaders

Source cue: v = glCreateShader(GL_VERTEX_SHADER); // vertex shader / char* vs = readTextFile(”vertex-shader.vert"); / const char* vv = vs; / glShaderSource(v, 1, &vv, NULL); / free(vs);

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Binding Shaders' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: v = glCreateShader(GL_VERTEX_SHADER); // vertex shader / char* vs = readTextFile(”vertex-shader.vert"); / const char* vv = vs; / glShaderSource(v, 1, &vv, NULL); / free(vs). If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Binding Shaders. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: v = glCreateShader(GL_VERTEX_SHADER); // vertex shader / char* vs = readTextFile(”vertex-shader.vert"); / const char* vv = vs; / glShaderSource(v, 1, &vv, NULL); / free(vs);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Binding Shaders'?

### Page 63 - Setting Uniforms

Source cue: - Uniforms are used to communicate between CPU and GPU / - Data is bound to uniform locations / - Must be updated after each linking process / GLint loc0 = glGetUniformLocation(p, ”isoValue_"); / glUniform1f(loc0, 0.45f);

Professor-style explanation: For 'Setting Uniforms', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Uniforms are used to communicate between CPU and GPU / - Data is bound to uniform locations / - Must be updated after each linking process / GLint loc0 = glGetUniformLocation(p, ”isoValue_"); / glUniform1f(loc0, 0.45f). Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Setting Uniforms. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Uniforms are used to communicate between CPU and GPU / - Data is bound to uniform locations / - Must be updated after each linking process / GLint loc0 = glGetUniformLocation(p, ”isoValue_"); / glUniform1f(loc0, 0.45f);

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Setting Uniforms' into a causal sentence instead of repeating the slide title?

### Page 64 - Shader Performance

Source cue: - Guidelines for efficient shaders / - Since fragment shaders are executed for a large number of fragments, / they should contain as few instructions as possible / - There should be as little as possible a change of the active shaders, / because they have their own state and, accordingly, the pipeline may need

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Shader Performance' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Guidelines for efficient shaders / - Since fragment shaders are executed for a large number of fragments, / they should contain as few instructions as possible / - There should be as little as possible a change of the active shaders, / because they have their own state and, accordingly, the pipeline may need. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Shader Performance. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Guidelines for efficient shaders / - Since fragment shaders are executed for a large number of fragments, / they should contain as few instructions as possible / - There should be as little as possible a change of the active shaders, / because they have their own state and, accordingly, the pipeline may need

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Performance'?

### Page 65 - Shader Development Environments 1/2

Source cue: - FX Composer, NVPerfHUD (NVIDIA) / - HLSL Shader IDE with performance analytics / www.developer.nvidia.com/page/tools.html / - RenderMonkey (ATI) / - HLSL, GLSL Shader IDE with performance analytics

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Shader Development Environments 1/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - FX Composer, NVPerfHUD (NVIDIA) / - HLSL Shader IDE with performance analytics / www.developer.nvidia.com/page/tools.html / - RenderMonkey (ATI) / - HLSL, GLSL Shader IDE with performance analytics. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Shader Development Environments 1/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - FX Composer, NVPerfHUD (NVIDIA) / - HLSL Shader IDE with performance analytics / www.developer.nvidia.com/page/tools.html / - RenderMonkey (ATI) / - HLSL, GLSL Shader IDE with performance analytics

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Development Environments 1/2'?

### Page 66 - Shader Development Environments 2/2

Source cue: - Shdr online GLSL editor: https://shdr.bkcore.com/

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Shader Development Environments 2/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Shdr online GLSL editor: https://shdr.bkcore.com/. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Shader Development Environments 2/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Shdr online GLSL editor: https://shdr.bkcore.com/

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shader Development Environments 2/2'?

### Page 67 - 2.5 Fragment Tests and Operations

Source cue: Towards the finishing line to the pixel

Professor-style explanation: Here the lecture moves from continuous geometry to a discrete grid. '2.5 Fragment Tests and Operations' asks which pixels or samples are covered by an ideal mathematical primitive. The slide gives us this anchor: Towards the finishing line to the pixel. The key spoken explanation is: rasterization creates fragment candidates and interpolated values, but it does not by itself guarantee that a fragment becomes the final visible pixel.

Technical commentary: This slide is about 2.5 Fragment Tests and Operations. Read it as continuous-to-discrete conversion. The core question is which samples are covered and which interpolated values each fragment receives. The visible cue is: Towards the finishing line to the pixel

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by '2.5 Fragment Tests and Operations'?

### Page 68 - Fragment Tests and Operations 1/2

Source cue: - After fragments have been generated, they must go through the per-fragment / tests and operations / Programmable / - Only if all these tests are successful, / Vertex Processing

Professor-style explanation: For 'Fragment Tests and Operations 1/2', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - After fragments have been generated, they must go through the per-fragment / tests and operations / Programmable / - Only if all these tests are successful, / Vertex Processing. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Fragment Tests and Operations 1/2. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - After fragments have been generated, they must go through the per-fragment / tests and operations / Programmable / - Only if all these tests are successful, / Vertex Processing

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Fragment Tests and Operations 1/2' into a causal sentence instead of repeating the slide title?

### Page 69 - Fragment Tests and Operations 2/2

Source cue: Fragment Pixel Ownership Scissor Alpha / Data Test Test Test / Depth Stencil / Framebuffer Dithering Blending / Test Test

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Fragment Tests and Operations 2/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: Fragment Pixel Ownership Scissor Alpha / Data Test Test Test / Depth Stencil / Framebuffer Dithering Blending / Test Test. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Fragment Tests and Operations 2/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: Fragment Pixel Ownership Scissor Alpha / Data Test Test Test / Depth Stencil / Framebuffer Dithering Blending / Test Test

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Fragment Tests and Operations 2/2'?

### Page 70 - Alpha Test

Source cue: - If framebuffer is an RGBA buffer, the alpha test can be performed / - The test must first be activated / glEnable(GL_ALPHA_TEST); / - The comparison function indicates which fragments survive the test / glAlphaFunc(func, value);

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Alpha Test' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - If framebuffer is an RGBA buffer, the alpha test can be performed / - The test must first be activated / glEnable(GL_ALPHA_TEST); / - The comparison function indicates which fragments survive the test / glAlphaFunc(func, value). If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Alpha Test. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - If framebuffer is an RGBA buffer, the alpha test can be performed / - The test must first be activated / glEnable(GL_ALPHA_TEST); / - The comparison function indicates which fragments survive the test / glAlphaFunc(func, value);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Alpha Test'?

### Page 71 - Stencil Test

Source cue: - Stencil Buffer / - Is a frame buffer component / - Is (indirectly) filled by drawing operations / - No special stencil drawing operations / - Stencil operation

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Stencil Test' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Stencil Buffer / - Is a frame buffer component / - Is (indirectly) filled by drawing operations / - No special stencil drawing operations / - Stencil operation. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Stencil Test. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Stencil Buffer / - Is a frame buffer component / - Is (indirectly) filled by drawing operations / - No special stencil drawing operations / - Stencil operation

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Stencil Test'?

### Page 72 - Depth Test

Source cue: - If the framebuffer has a depth buffer, the depth test can be performed / - The test must first be activated / glEnable(GL_DEPTH_TEST); / - The comparison is made with the depth value already in the buffer / - The comparison function indicates which fragments survive the test

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Depth Test' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - If the framebuffer has a depth buffer, the depth test can be performed / - The test must first be activated / glEnable(GL_DEPTH_TEST); / - The comparison is made with the depth value already in the buffer / - The comparison function indicates which fragments survive the test. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Depth Test. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - If the framebuffer has a depth buffer, the depth test can be performed / - The test must first be activated / glEnable(GL_DEPTH_TEST); / - The comparison is made with the depth value already in the buffer / - The comparison function indicates which fragments survive the test

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Depth Test'?

### Page 73 - Image Composition and Mixture

Source cue: - Alpha values o f the pixels / - control the combination of pixel values / - are specified as color components of color pixels / - 𝑃 = [𝑅, 𝐺, 𝐵, 𝐴], 𝑤𝑖𝑡ℎ 𝑅, 𝐺, 𝐵, 𝐴 ∈ [0,1] / - Applications are manifold

Professor-style explanation: For 'Image Composition and Mixture', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Alpha values o f the pixels / - control the combination of pixel values / - are specified as color components of color pixels / - 𝑃 = [𝑅, 𝐺, 𝐵, 𝐴], 𝑤𝑖𝑡ℎ 𝑅, 𝐺, 𝐵, 𝐴 ∈ [0,1] / - Applications are manifold. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Image Composition and Mixture. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Alpha values o f the pixels / - control the combination of pixel values / - are specified as color components of color pixels / - 𝑃 = [𝑅, 𝐺, 𝐵, 𝐴], 𝑤𝑖𝑡ℎ 𝑅, 𝐺, 𝐵, 𝐴 ∈ [0,1] / - Applications are manifold

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Image Composition and Mixture' into a causal sentence instead of repeating the slide title?

### Page 74 - Blending Application

Source cue: - Example application for transparency: drawing with semi-transparent brush

Professor-style explanation: For 'Blending Application', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Example application for transparency: drawing with semi-transparent brush. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Blending Application. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Example application for transparency: drawing with semi-transparent brush

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Blending Application' into a causal sentence instead of repeating the slide title?

### Page 75 - Blending Process 1/2

Source cue: - Blending is an operation called per fragment / - Fragments are modified after rasterization, / but before writing to the framebuffer with a blending function / - Combination of a source fragment to be written with the destination pixel / in the frame buffer by using a blending function

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Blending Process 1/2' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Blending is an operation called per fragment / - Fragments are modified after rasterization, / but before writing to the framebuffer with a blending function / - Combination of a source fragment to be written with the destination pixel / in the frame buffer by using a blending function. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Blending Process 1/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Blending is an operation called per fragment / - Fragments are modified after rasterization, / but before writing to the framebuffer with a blending function / - Combination of a source fragment to be written with the destination pixel / in the frame buffer by using a blending function

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Blending Process 1/2'?

### Page 76 - Blending Process 2/2

Source cue: - Source factor: 𝐹 / - Destination factor: 𝐹 / - Source fragment: [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Destination pixel: [𝑃 , 𝑃 , 𝑃 , 𝑃 ]

Professor-style explanation: For 'Blending Process 2/2', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Source factor: 𝐹 / - Destination factor: 𝐹 / - Source fragment: [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Destination pixel: [𝑃 , 𝑃 , 𝑃 , 𝑃 ]. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Blending Process 2/2. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Source factor: 𝐹 / - Destination factor: 𝐹 / - Source fragment: [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Destination pixel: [𝑃 , 𝑃 , 𝑃 , 𝑃 ]

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Blending Process 2/2' into a causal sentence instead of repeating the slide title?

### Page 77 - Applying Blending

Source cue: - Switch on (or switch off) blending / - glEnable(GL_BLEND); / - glDisable(GL_BLEND); / - Defining Blending Factors / - glBlendFunc(srcFac, destFac);

Professor-style explanation: For 'Applying Blending', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Switch on (or switch off) blending / - glEnable(GL_BLEND); / - glDisable(GL_BLEND); / - Defining Blending Factors / - glBlendFunc(srcFac, destFac). Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Applying Blending. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Switch on (or switch off) blending / - glEnable(GL_BLEND); / - glDisable(GL_BLEND); / - Defining Blending Factors / - glBlendFunc(srcFac, destFac);

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Applying Blending' into a causal sentence instead of repeating the slide title?

### Page 78 - Blending Examples

Source cue: - Example 1: Copy source pixels and overwrite destination pixels / - glBlendFunc(GL_ONE, GL_ZERO); / - 𝑃 = [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑏𝑙𝑒𝑛𝑑 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Example 2: Alpha-based mixing of source pixels and destination pixels

Professor-style explanation: For 'Blending Examples', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Example 1: Copy source pixels and overwrite destination pixels / - glBlendFunc(GL_ONE, GL_ZERO); / - 𝑃 = [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑏𝑙𝑒𝑛𝑑 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Example 2: Alpha-based mixing of source pixels and destination pixels. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Blending Examples. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Example 1: Copy source pixels and overwrite destination pixels / - glBlendFunc(GL_ONE, GL_ZERO); / - 𝑃 = [𝑃 , 𝑃 , 𝑃 , 𝑃 ] / 𝑏𝑙𝑒𝑛𝑑 𝑠,𝑟 𝑠,𝑔 𝑠,𝑏 𝑠,𝑎 / - Example 2: Alpha-based mixing of source pixels and destination pixels

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Blending Examples' into a causal sentence instead of repeating the slide title?

### Page 79 - 2.6 Framebuffer

Source cue: Contains everything that is (in)visible on the screen

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. '2.6 Framebuffer' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: Contains everything that is (in)visible on the screen. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about 2.6 Framebuffer. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: Contains everything that is (in)visible on the screen

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '2.6 Framebuffer'?

### Page 80 - Viewport

Source cue: - Rectangular area in pixel grid, set explicitly / - Rendering operations are limited to this area / - All primitives that are completely or partially outside / are clipped at the viewport area (clipping)

Professor-style explanation: This slide should be read as camera geometry. With 'Viewport', the question is how a 3D view becomes coordinates that can be clipped, divided, mapped to the viewport, and rasterized. The slide gives us this anchor: - Rectangular area in pixel grid, set explicitly / - Rendering operations are limited to this area / - All primitives that are completely or partially outside / are clipped at the viewport area (clipping). Keep separate the camera/view transform, the projection matrix, the perspective divide, and the final viewport transform; many mistakes come from blending these steps together.

Technical commentary: This slide is about Viewport. Read it as camera geometry. Track how 3D view-space positions become clip coordinates, normalized device coordinates, and finally screen locations. The visible cue is: - Rectangular area in pixel grid, set explicitly / - Rendering operations are limited to this area / - All primitives that are completely or partially outside / are clipped at the viewport area (clipping)

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Check yourself: Can you explain how 'Viewport' changes positions before rasterization?

### Page 81 - Framebuffer

Source cue: - Context-bound raster with a resolution and structure / specified by the application / - Physical realization on the GPU / - Logical subdivision / - Color memory

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Framebuffer' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Context-bound raster with a resolution and structure / specified by the application / - Physical realization on the GPU / - Logical subdivision / - Color memory. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Framebuffer. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Context-bound raster with a resolution and structure / specified by the application / - Physical realization on the GPU / - Logical subdivision / - Color memory

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Framebuffer'?

### Page 82 - OpenGL Framebuffers 1/3

Source cue: - Typical OpenGL framebuffer configuration / 8bit Stencil Buffer / 32bit Depth Buffer / = 32bit Color Buffer

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL Framebuffers 1/3' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Typical OpenGL framebuffer configuration / 8bit Stencil Buffer / 32bit Depth Buffer / = 32bit Color Buffer. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL Framebuffers 1/3. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Typical OpenGL framebuffer configuration / 8bit Stencil Buffer / 32bit Depth Buffer / = 32bit Color Buffer

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Framebuffers 1/3'?

### Page 83 - OpenGL Framebuffers 2/3

Source cue: - All buffers of a frame buffer have the same grid size / - Number of bitplanes per buffer can be configured individually / - Individual buffers are directly supported by the hardware / - Buffer identifier / - GL_COLOR_BUFFER_BIT

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL Framebuffers 2/3' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - All buffers of a frame buffer have the same grid size / - Number of bitplanes per buffer can be configured individually / - Individual buffers are directly supported by the hardware / - Buffer identifier / - GL_COLOR_BUFFER_BIT. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL Framebuffers 2/3. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - All buffers of a frame buffer have the same grid size / - Number of bitplanes per buffer can be configured individually / - Individual buffers are directly supported by the hardware / - Buffer identifier / - GL_COLOR_BUFFER_BIT

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Framebuffers 2/3'?

### Page 84 - OpenGL Framebuffers 3/3

Source cue: - Delete a buffer / glClear(GLbitfield mask); / - Set the initialization color for the color buffer / glClearColor(1.0,1.0,1.0,1.0); / glClear(GL_COLOR_BUFFER_BIT);

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL Framebuffers 3/3' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Delete a buffer / glClear(GLbitfield mask); / - Set the initialization color for the color buffer / glClearColor(1.0,1.0,1.0,1.0); / glClear(GL_COLOR_BUFFER_BIT). If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL Framebuffers 3/3. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Delete a buffer / glClear(GLbitfield mask); / - Set the initialization color for the color buffer / glClearColor(1.0,1.0,1.0,1.0); / glClear(GL_COLOR_BUFFER_BIT);

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Framebuffers 3/3'?

### Page 85 - Double Buffering

Source cue: - Use of two color buffers to avoid flicker effects / - Image buildup takes place in the background (back buffer) / - Visible image is independent of this (front buffer) / Rendering / Process

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Double Buffering' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Use of two color buffers to avoid flicker effects / - Image buildup takes place in the background (back buffer) / - Visible image is independent of this (front buffer) / Rendering / Process. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Double Buffering. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Use of two color buffers to avoid flicker effects / - Image buildup takes place in the background (back buffer) / - Visible image is independent of this (front buffer) / Rendering / Process

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Double Buffering'?

### Page 86 - 2.7 Pixel-based Rendering

Source cue: Direct pixel processing without involving 3D models

Professor-style explanation: For '2.7 Pixel-based Rendering', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: Direct pixel processing without involving 3D models. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about 2.7 Pixel-based Rendering. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: Direct pixel processing without involving 3D models

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn '2.7 Pixel-based Rendering' into a causal sentence instead of repeating the slide title?

### Page 87 - Pixel-based Rendering Operations

Source cue: - Generally / - Read and write operations for various image data formats, / usually as an external library (e.g., DevIl) / - Conversions between image data types / - In OpenGL done with framebuffer objects

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Pixel-based Rendering Operations' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Generally / - Read and write operations for various image data formats, / usually as an external library (e.g., DevIl) / - Conversions between image data types / - In OpenGL done with framebuffer objects. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Pixel-based Rendering Operations. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Generally / - Read and write operations for various image data formats, / usually as an external library (e.g., DevIl) / - Conversions between image data types / - In OpenGL done with framebuffer objects

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Pixel-based Rendering Operations'?

### Page 88 - Image Operations

Source cue: - Rendering image data with OpenGL / Copy Pixel Data / Draw/Read / Pixel / Geometry

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Image Operations' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Rendering image data with OpenGL / Copy Pixel Data / Draw/Read / Pixel / Geometry. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Image Operations. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Rendering image data with OpenGL / Copy Pixel Data / Draw/Read / Pixel / Geometry

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Image Operations'?

### Page 89 - Write Pixels into Framebuffer

Source cue: - glDrawPixels(x, y, width, height, format, type, pixels); / - Example / // 64x64 array with rgb components / GLubyte img[64][64][3]; / void draw() {

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Write Pixels into Framebuffer' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - glDrawPixels(x, y, width, height, format, type, pixels); / - Example / // 64x64 array with rgb components / GLubyte img[64][64][3]; / void draw() {. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Write Pixels into Framebuffer. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - glDrawPixels(x, y, width, height, format, type, pixels); / - Example / // 64x64 array with rgb components / GLubyte img[64][64][3]; / void draw() {

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Write Pixels into Framebuffer'?

### Page 90 - Read Pixels from Framebuffer

Source cue: - glReadPixels(x, y, width, height, format, type, pixels); / - Example / GLubyte* img = 0; / int width, height; // canvas size / void snapshot() {

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Read Pixels from Framebuffer' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - glReadPixels(x, y, width, height, format, type, pixels); / - Example / GLubyte* img = 0; / int width, height; // canvas size / void snapshot() {. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Read Pixels from Framebuffer. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - glReadPixels(x, y, width, height, format, type, pixels); / - Example / GLubyte* img = 0; / int width, height; // canvas size / void snapshot() {

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Read Pixels from Framebuffer'?

### Page 91 - Formats & Data Types

Source cue: - Format information for pixel array operations / - GL_RGB – red-green-blue values of the frame buffer (FB) / - GL_RED – red values o f the FB / - GL_ALPHA – transparency values of the FB / - GL_RGBA – red-Green-Blue-Alpha values of the FB

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Formats & Data Types' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Format information for pixel array operations / - GL_RGB – red-green-blue values of the frame buffer (FB) / - GL_RED – red values o f the FB / - GL_ALPHA – transparency values of the FB / - GL_RGBA – red-Green-Blue-Alpha values of the FB. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Formats & Data Types. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Format information for pixel array operations / - GL_RGB – red-green-blue values of the frame buffer (FB) / - GL_RED – red values o f the FB / - GL_ALPHA – transparency values of the FB / - GL_RGBA – red-Green-Blue-Alpha values of the FB

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Formats & Data Types'?

### Page 92 - coordinate systems in the geometry stage

Source cue: - Rendering pipeline consist of geometry stage and rasterization stage / - Geometric primitives (mostly triangles) are transformed through different / coordinate systems in the geometry stage / - Rasterization results in fragments, which are pixel predecessors / - Fragments have to endure a sequence of tests in the rasterization stage, in

Professor-style explanation: For 'coordinate systems in the geometry stage', imagine following one piece of scene data through the renderer. It starts as model or application data, then passes through transformations, primitive processing, rasterization, fragment processing, tests, and finally the framebuffer. The slide gives us this anchor: - Rendering pipeline consist of geometry stage and rasterization stage / - Geometric primitives (mostly triangles) are transformed through different / coordinate systems in the geometry stage / - Rasterization results in fragments, which are pixel predecessors / - Fragments have to endure a sequence of tests in the rasterization stage, in. The important point is that each stage changes the representation, so debugging means asking where the representation first became wrong.

Technical commentary: This slide is about coordinate systems in the geometry stage. Read it as a data-flow explanation: scene or model data is processed step by step until valid framebuffer updates remain. The visible cue is: - Rendering pipeline consist of geometry stage and rasterization stage / - Geometric primitives (mostly triangles) are transformed through different / coordinate systems in the geometry stage / - Rasterization results in fragments, which are pixel predecessors / - Fragments have to endure a sequence of tests in the rasterization stage, in

Why it matters: Pipeline understanding lets you localize rendering errors instead of guessing randomly.

Check yourself: Can you name the input and output representation for 'coordinate systems in the geometry stage' in the rendering pipeline?

### Page 93 - Literature and other sources used in this chapter

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Professor-style explanation: For 'Literature and other sources used in this chapter', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Literature and other sources used in this chapter. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Literature and other sources used in this chapter' into a causal sentence instead of repeating the slide title?

### Page 94 - Guide: The Official Guide to Learning OpenGL

Source cue: - Text Books / - D. Shreiner, G. Sellers, J. Kessenich, B. Licea-Kane: OpenGL Programming / Guide: The Official Guide to Learning OpenGL / (8th Edition), Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Guide: The Official Guide to Learning OpenGL' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Text Books / - D. Shreiner, G. Sellers, J. Kessenich, B. Licea-Kane: OpenGL Programming / Guide: The Official Guide to Learning OpenGL / (8th Edition), Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Guide: The Official Guide to Learning OpenGL. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Text Books / - D. Shreiner, G. Sellers, J. Kessenich, B. Licea-Kane: OpenGL Programming / Guide: The Official Guide to Learning OpenGL / (8th Edition), Addison-Wesley 2013. / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer

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
