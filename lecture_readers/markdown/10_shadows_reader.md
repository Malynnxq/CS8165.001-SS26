# Lecture 10 - Shadows

Source chunk: `course_text_parts/03_lectures/10_shadows.txt`
Extracted slide pages in source chunk: 60

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture explains shadows as a visibility problem from the light source. A point is lit if the light can see it; it is shadowed if another object blocks that visibility.

## How To Read This Lecture

- First read the big picture and the mental models.
- Then open the source chunk and compare the slide bullets to the commentary.
- After each section, answer the check question without notes.
- If the check feels vague, revisit the source pages listed for that section.

## Slide Walkthrough

This section adds a short reading comment for every extracted slide page. Use it when the original PDF page is too terse.

- Page 1: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 2: **Shadow Perception 1/3**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 3: **Shadow Perception 2/3**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 4: **Shadow Perception 3/3**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 5: **Shadow Atmosphere**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 6: **▪ Shadows createa certain atmosphere**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 7: **Shadow Atmosphere**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 8: **Overview**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 9: **10.1 Definitions**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 10: **Classification of scene objects**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 11: **Umbra and Penumbra**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 12: **Hard and Soft Shadows**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 13: **Description of Shadows**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 14: **▪ Shadows can be described differently**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 15: **Observations 1/2**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 16: **Observations 2/2**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 17: **Shadow Calculation Methods**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 18: **10.2 Ground Plane Shadows**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 19: **Static Shadow Polygons**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 20: **Render Static Shadow Polygons 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 21: **Render Static Shadow Polygons 2/2**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 22: **Static Shadow Polygons**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 23: **Dynamic Shadow Polygons**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 24: **Shadow Projection**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 25: **Rendering Dynamic Shadow Polygons**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 26: **10.3 Light Maps**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 27: **Light Maps**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 28: **Soft Shadows with Light Maps 1/2**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 29: **Soft Shadows with Light Maps 2/2**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 30: **10.4 Shadow Volumes**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 31: **Shadow Volumes**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 32: **Initial Considerations**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 33: **Shadow Volume Geometry**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 34: **Shadow Volume Realization**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 35: **Shadow Volume Properties 1/2**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 36: **Shadow Volume Properties 2/2**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 37: **Stencil Shadow Volume**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 38: **Implementation**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 39: **Special Case: COP in the shadows**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 40: **Shadow Volume Example**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 41: **Shadow Volume Conclusions**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 42: **10.5 Shadow Maps**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 43: **Shadow Mapping**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 44: **Projected Shadows**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 45: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 46: **Depth Comparison**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 47: **Coordinate Systems**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 48: **Pseudo Code**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 49: **Properties**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 50: **View Volume Problem**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 51: **Bias Problem 1/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 52: **Bias Problem 2/2**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.
- Page 53: **Aliasing Problem 1/3**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 54: **Aliasing Problem 2/3**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 55: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 56: **Aliasing Problem 3/3**
  - Reading comment: Read this as sampled data. Identify the texture coordinates, sampling rule, filtering mode, and shader interpretation.
- Page 57: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 58: **▪ Shadows in Visual Perception**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 59: **Literature and other sources used in this chapter**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 60: **▪ Text Books**
  - Reading comment: Read this as light-space visibility. Ask what blocks the light, what representation stores that information, and which artifact can appear.

## 10.1 Definitions

Source location: Section 10.1

### Commentary

A shadow is not simply a dark texture. It is evidence that light visibility is blocked. Important distinctions include hard versus soft shadows, umbra versus penumbra, and geometric versus precomputed approaches.

For real-time graphics, shadows are usually approximated. The approximation must answer a visibility question cheaply enough for interactive rendering.

### Mental Model

Shadows are light-space visibility made visible in the camera image.

### Check Yourself

Why is shadow computation related to visibility determination?

## 10.2 Ground Plane Shadows

Source location: Section 10.2

### Commentary

Ground plane shadows project an object onto a receiving plane. This is simple and can look convincing in restricted scenes, but it assumes a known planar receiver and does not handle general shadowing between arbitrary objects.

The method is useful pedagogically because it makes the geometric nature of shadows explicit: a light source, an occluder, and a receiver define where the shadow lands.

### Mental Model

A planar shadow is projected geometry on a known receiver.

### Check Yourself

What scene limitation makes ground plane shadows less general than shadow maps?

## 10.3 Light Maps

Source location: Section 10.3

### Commentary

Light maps store precomputed lighting or shadow information in textures. They can be efficient at runtime, but they are limited when lights, objects, or geometry move dynamically.

This is another example of a recurring graphics tradeoff: precompute for speed, but lose flexibility. Real-time rendering often mixes precomputed and dynamic techniques.

### Mental Model

A light map spends storage and preprocessing to save runtime shading work.

### Check Yourself

Why are light maps less suitable for fully dynamic moving lights?

## 10.4 Shadow Volumes

Source location: Section 10.4

### Commentary

Shadow volumes construct the volume of space blocked from a light by an occluder. The camera view can then determine whether visible points lie inside that volume. Stencil buffer techniques are often associated with this method.

The strength is geometric precision for hard shadows. The cost is handling silhouette edges, volume construction, and robust stencil operations. It is a good contrast to shadow maps, which are image-based from the light view.

### Mental Model

A shadow volume is the 3D region where the light cannot reach.

### Check Yourself

Why are silhouette edges important for constructing shadow volumes?

## 10.5 Shadow Maps

Source location: Section 10.5

### Commentary

Shadow mapping renders the scene from the light's point of view and stores depth. During the camera pass, a surface point is transformed into light space and compared against the stored depth. If it is farther than what the light saw, it is in shadow.

This method is practical and widely used, but it has artifacts. Shadow acne comes from precision/self-comparison issues. Bias can reduce acne but too much bias causes detached shadows. Resolution, filtering, and light projection strongly affect quality.

### Mental Model

Shadow maps reuse the depth-buffer idea, but from the light's camera.

### Check Yourself

What exactly is stored in a shadow map?

## End-of-Lecture Summary

If you remember only one thing from Lecture 10, remember this: This lecture explains shadows as a visibility problem from the light source. A point is lit if the light can see it; it is shadowed if another object blocks that visibility.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
