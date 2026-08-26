# Lecture 04 - Geometric Projection

Source chunk: `course_text_parts/03_lectures/04_geometric-projection.txt`
Extracted slide pages in source chunk: 61

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture explains how a 3D view becomes a 2D image. Projection is where camera geometry, homogeneous coordinates, clipping planes, depth precision, and viewport mapping meet.

## How To Read This Lecture

- First read the big picture and the mental models.
- Then open the source chunk and compare the slide bullets to the commentary.
- After each section, answer the check question without notes.
- If the check feels vague, revisit the source pages listed for that section.

## Slide Walkthrough

This section adds a short reading comment for every extracted slide page. Use it when the original PDF page is too terse.

- Page 1: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 2: **Projecting 3D Models**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 3: **4.1 Linear Perspective**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 4: **4.1 Linear Perspective**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 5: **Linear Perspective**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 6: **Drawing by Projecting**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 7: **Projection in the Arts 1/5**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 8: **Projection in the Arts 2/5**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 9: **Projection in the Arts 3/5**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 10: **Projection in the Arts 4/5**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 11: **Projection in the Arts 4/5**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 12: **Projection in the Arts 5/5**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 13: **Projection in the Arts 6/5**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 14: **Projection Technics 1/3**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 15: **Projection Technics 1/3**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 16: **Projection Technics 2/3**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 17: **Projection Technics 3/3**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 18: **Projection Technics 3/3**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 19: **4.2 Planar Projections**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 20: **Geometric Projections**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 21: **Projection Types 1/2**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 22: **Projection Types 2/2**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 23: **Orthographic Projections**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 24: **Axonometric Projections**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 25: **Isometric Projections**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 26: **Oblique Projection 1/2**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 27: **Oblique Projection 2/2**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 28: **Properties of Parallel Projections**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 29: **Perspective Projections 1/3**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 30: **Perspective Projections 2/3**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 31: **Perspective Projections 3/3**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 32: **4.3 Camera Modeling**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 33: **Camera Modeling**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 34: **View Volume**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 35: **Projection Specification**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 36: **View Angle**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 37: **Clipping Planes**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 38: **4.4 Specifying Projections in OpenGL**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 39: **Projection Matrix Generation 1/3**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 40: **Projection Matrix Generation 2/3**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 41: **Projection Matrix Generation 3/3**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 42: **Orthographic Matrix Specification**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 43: **4.5 Orthographic Projection Derivation**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 44: **Canonical View Volume**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 45: **Orthographic Projection 1/4**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 46: **Orthographic Projection 2/4**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 47: **Orthographic Projection 3/4**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 48: **Orthographic Projection 4/4**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 49: **4.6 Perspective Projection Derivation**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 50: **Perspective Projection**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 51: **Transformation of z-Values 1/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 52: **Transformation of z-Values 2/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 53: **Transformation of x- and y-Values 1/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 54: **Transformation of x- and y-Values 2/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 55: **4.7 Viewport Transformation**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 56: **Screen Coordinate Mapping**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 57: **Viewport Transformation 1/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 58: **Viewport Transformation 2/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 59: **volume, we can differentiate different projection types**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 60: **Literature and other sources used in this chapter**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 61: **- Text Books**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?

## 04.1 Linear Perspective and Planar Projections

Source location: Sections 4.1-4.2

### Commentary

Perspective projection models the visual effect that farther objects appear smaller. Orthographic projection removes this distance-based size change and keeps parallel lines parallel. Both are useful, but they communicate different spatial relationships.

Planar projection means mapping points onto an image plane. The lecture's art examples are not decoration; they show that projection is a geometric rule for constructing an image from a viewpoint.

### Mental Model

Projection is the rule that turns 3D positions into image-plane positions.

### Check Yourself

What visual cue does perspective projection add that orthographic projection lacks?

## 04.2 Camera Modeling

Source location: Section 4.3

### Commentary

A virtual camera is defined by position, orientation, projection type, viewing volume, and image/viewport settings. The view transform places the world relative to the camera. The projection transform maps that view into clip coordinates.

Near and far clipping planes are part of the camera model. They decide what range of depths is represented and strongly affect depth buffer precision. A careless near/far setup can create z-fighting even if the scene geometry is correct.

### Mental Model

A camera is not only an eye position; it is also a volume and a mapping rule.

### Check Yourself

Why can changing the near plane affect depth artifacts?

## 04.3 Specifying Projections in OpenGL

Source location: Section 4.4

### Commentary

In OpenGL, projection is usually encoded in a projection matrix sent to a shader. The matrix maps view-space coordinates to clip space. Clipping and the perspective divide then lead toward normalized device coordinates.

Aspect ratio and field of view must match the intended viewport. If the aspect ratio is wrong, objects appear stretched. If the field of view is extreme, the image can look distorted even though the math is functioning.

### Mental Model

The projection matrix is the camera lens encoded as linear algebra in homogeneous coordinates.

### Check Yourself

What symptom suggests that the projection aspect ratio does not match the window?

## 04.4 Orthographic and Perspective Derivations

Source location: Sections 4.5-4.6

### Commentary

The derivations are there to explain where the matrix entries come from. Orthographic projection maps a box-shaped view volume into normalized coordinates. Perspective projection maps a frustum and uses the homogeneous component for the later divide.

You do not need to treat these matrices as random formulas. Each part maps a coordinate range into a standard range. The perspective matrix additionally arranges w so that the perspective divide creates foreshortening.

### Mental Model

Projection matrices normalize a viewing volume; perspective also prepares the divide by w.

### Check Yourself

What does the perspective divide do to x and y coordinates?

## 04.5 Viewport Transformation

Source location: Section 4.7

### Commentary

After normalized device coordinates, the viewport transform maps the normalized range to actual window coordinates. This is the last geometric mapping before rasterization uses the target grid.

Separating projection from viewport mapping helps debugging. A wrong projection can produce wrong normalized coordinates; a wrong viewport can map otherwise valid coordinates into the wrong part of the window.

### Mental Model

Projection decides normalized position; viewport decides where that position lands on the screen.

### Check Yourself

Why is resizing a window related to both viewport and projection settings?

## End-of-Lecture Summary

If you remember only one thing from Lecture 04, remember this: This lecture explains how a 3D view becomes a 2D image. Projection is where camera geometry, homogeneous coordinates, clipping planes, depth precision, and viewport mapping meet.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
