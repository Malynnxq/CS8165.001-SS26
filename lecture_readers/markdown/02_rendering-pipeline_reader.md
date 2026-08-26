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

## Slide Walkthrough

This section adds a short reading comment for every extracted slide page. Use it when the original PDF page is too terse.

- Page 1: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 2: **Object-based Rendering**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 3: **2.1 Rendering Process**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 4: **2.1 Rendering Process**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 5: **Geometry-based Rendering 1/2**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 6: **Geometry-based Rendering 2/2**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 7: **Application Stage**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 8: **Geometry Stage**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 9: **Rasterization Stage**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 10: **2.2 OpenGL Overview**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 11: **OpenGL History**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 12: **OpenGL**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 13: **OpenGL vs. Vulkan**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 14: **OpenGL Libraries**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 15: **OpenGL Functionality**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 16: **OpenGL Context**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 17: **OpenGL Rendering Process**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 18: **Window Creation with GLFW 1/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 19: **Window Creation with GLFW 2/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 20: **OpenGL Naming Conventions**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 21: **2.3 OpenGL Rendering**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 22: **OpenGL Rendering (until V2.1)**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 23: **OpenGL Rendering (since V3.0)**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 24: **1. Vertex Specification**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 25: **2. Vertex Data Transfer**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 26: **3. Memory Layout Description**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 27: **4. VAO Drawing 1/2**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 28: **4. VAO Drawing 2/2**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 29: **5. GPU Memory Release**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 30: **Rendering Initialization 1/2**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 31: **Rendering Initialization 2/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 32: **Rendering**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 33: **Additional Attributes**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 34: **2.4 OpenGL Rendering Pipeline**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 35: **The Rendering Pipeline 1/2**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 36: **The Rendering Pipeline 2/2**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 37: **Shader Programming – History 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 38: **Shader Programming – History 2/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 39: **Assembler Shader**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 40: **High-Level Shading Languages 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 41: **High-Level Shading Languages 2/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 42: **Shader Types**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 43: **Vertex Shader Concepts**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 44: **Vertex Shader Examples 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 45: **Vertex Shader Examples 2/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 46: **Vertex Shader Coordinate Systems 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 47: **Vertex Shader Coordinate Systems 2/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 48: **Local Space**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 49: **World Space**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 50: **View Space**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 51: **Clip Space**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 52: **Screen Space**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 53: **Coordinate Systems**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 54: **Vertex Shader Variables**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 55: **Fixed Function Vertex Postprocessing**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 56: **Fixed Function Rasterization**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 57: **Fragment Shader Concept 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 58: **Fragment Shader Concept 2/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 59: **Shader Example**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 60: **GLSL Shader Functions**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 61: **Shader Usage**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 62: **Binding Shaders**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 63: **Setting Uniforms**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 64: **Shader Performance**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 65: **Shader Development Environments 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 66: **Shader Development Environments 2/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 67: **2.5 Fragment Tests and Operations**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 68: **Fragment Tests and Operations 1/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 69: **Fragment Tests and Operations 2/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 70: **Alpha Test**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 71: **Stencil Test**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 72: **Depth Test**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 73: **Image Composition and Mixture**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 74: **Blending Application**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 75: **Blending Process 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 76: **Blending Process 2/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 77: **Applying Blending**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 78: **Blending Examples**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 79: **2.6 Framebuffer**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 80: **Viewport**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 81: **Framebuffer**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 82: **OpenGL Framebuffers 1/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 83: **OpenGL Framebuffers 2/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 84: **OpenGL Framebuffers 3/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 85: **Double Buffering**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 86: **2.7 Pixel-based Rendering**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 87: **Pixel-based Rendering Operations**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 88: **Image Operations**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 89: **Write Pixels into Framebuffer**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 90: **Read Pixels from Framebuffer**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 91: **Formats & Data Types**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 92: **coordinate systems in the geometry stage**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 93: **Literature and other sources used in this chapter**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 94: **Guide: The Official Guide to Learning OpenGL**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.

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
