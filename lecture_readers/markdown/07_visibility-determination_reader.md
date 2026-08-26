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

## Slide Walkthrough

This section adds a short reading comment for every extracted slide page. Use it when the original PDF page is too terse.

- Page 1: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 2: **Visibility Determination**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 3: **Object-Based Algorithms**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 4: **Image-Based Algorithms**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 5: **7.1 Object-Based Algorithms**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 6: **7.1 Object-Based Algorithms**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 7: **Painter‘s Algorithm 1/3**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 8: **Painter‘s Algorithm 2/3**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 9: **Painter‘s Algorithm 3/3**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 10: **Weiler-Atherton Algorithm 1/3**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 11: **Weiler-Atherton Algorithm 2/3**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 12: **Weiler-Atherton Algorithm 3/3**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 13: **Back Face Culling 1/2**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 14: **Back Face Culling 2/2**
  - Reading comment: Read this as the main data-flow story: scene/model data is processed step by step until only valid framebuffer updates remain.
- Page 15: **Robert‘s Algorithm**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 16: **Assessment Robert‘s Algorithm**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 17: **7.2 Binary Space Partitioning**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 18: **Spatial Data Structures**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 19: **BSP Trees 1/2**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 20: **BSP Trees 2/2**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 21: **Node Data Structure**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 22: **BSP Tree Construction**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 23: **BSP Tree Construction - Example**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 24: **BSP Tree Construction – Pseudo Code**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 25: **Visibility Determination**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 26: **Visibility Determination – Pseudo Code**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 27: **BSP Tree Traversal - Example**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 28: **Splitting Planes Selection**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 29: **Traversal Optimization**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 30: **Assessment BSP Trees**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 31: **7.3 Warnock Algorithm**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 32: **Warnock Algorithm**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 33: **Region-Based Visibility Determination**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 34: **Procedure**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 35: **Pseudo Code**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 36: **Assessment Warnock Algorithm**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 37: **7.4 Depth Buffer Algorithm**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 38: **Depth Buffer Algorithm 1/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 39: **Depth Buffer Algorithm 2/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 40: **Depth Buffer Algorithm 3/3**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 41: **Pseudo Code – Depth Buffer Test**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 42: **OpenGL Depth Buffer**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 43: **Depth Buffer Precision**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 44: **Z-Fighting 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 45: **Z-Fighting 2/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 46: **Assessment Depth Buffering**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 47: **7.5 Depth Buffer Extensions**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 48: **Semi-Transparent Objects 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 49: **Semi-Transparent Objects 2/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 50: **Order-Independent Transparency 1/4**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 51: **Order-Independent Transparency 2/4**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 52: **Order-Independent Transparency 3/4**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 53: **Order-Independent Transparency 4/4**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 54: **Generating Haloes 1/2**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 55: **Generating Haloes 2/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 56: **7.6 Ray Casting**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 57: **Ray Casting Principle**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 58: **Ray Initialization 1/3**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 59: **Ray Initialization 2/3**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 60: **Ray Initialization 3/3**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 61: **Intersection Calculation**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 62: **Implicit Surface Intersection Calculation**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 63: **Intersection Calculation - Triangle**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 64: **Pseudo Code – Analytic Intersection Computation**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 65: **Pseudo Code - Iterative Intersection Calculation (Ray Marching)**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 66: **Assessment Ray Casting**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 67: **but are crucial for accurate visibility determination**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 68: **Literature and other sources used in this chapter**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 69: **Practice, Addison-Wesley.**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?

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
