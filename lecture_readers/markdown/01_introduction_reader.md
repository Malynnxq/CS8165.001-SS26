# Lecture 01 - Introduction

Source chunk: `course_text_parts/03_lectures/01_introduction.txt`
Extracted slide pages in source chunk: 51

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture is the orientation layer for the whole course. It explains why interactive computer graphics is a pipeline problem: a scene must be represented, processed under time constraints, sampled into an image, and displayed fast enough for interaction.

## How To Read This Lecture

- First read the big picture and the mental models.
- Then open the source chunk and compare the slide bullets to the commentary.
- After each section, answer the check question without notes.
- If the check feels vague, revisit the source pages listed for that section.

## Slide Walkthrough

This section adds a short reading comment for every extracted slide page. Use it when the original PDF page is too terse.

- Page 1: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 2: **Course Learning Outcomes**
  - Reading comment: Read this as organization and relevance information: it tells you how lecture theory, exercises, and exam preparation connect.
- Page 3: **Real-Time Rendering Contest Results 1/3**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 4: **Real-Time Rendering Contest Results 2/3**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 5: **Real-Time Rendering Contest Results 3/3**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 6: **1.1 Course Organization**
  - Reading comment: Read this as organization and relevance information: it tells you how lecture theory, exercises, and exam preparation connect.
- Page 7: **Teachers**
  - Reading comment: Read this as organization and relevance information: it tells you how lecture theory, exercises, and exam preparation connect.
- Page 8: **Course Format**
  - Reading comment: Read this as organization and relevance information: it tells you how lecture theory, exercises, and exam preparation connect.
- Page 9: **Course Format**
  - Reading comment: Read this as organization and relevance information: it tells you how lecture theory, exercises, and exam preparation connect.
- Page 10: **Exercises**
  - Reading comment: Read this as organization and relevance information: it tells you how lecture theory, exercises, and exam preparation connect.
- Page 11: **Successful Course Completion**
  - Reading comment: Read this as organization and relevance information: it tells you how lecture theory, exercises, and exam preparation connect.
- Page 12: **Course Overview**
  - Reading comment: Read this as organization and relevance information: it tells you how lecture theory, exercises, and exam preparation connect.
- Page 13: **Literature**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 14: **Relevant Chapters and Link to Lecture Course**
  - Reading comment: Read this as organization and relevance information: it tells you how lecture theory, exercises, and exam preparation connect.
- Page 15: **(1.1 Course Organization)**
  - Reading comment: Read this as organization and relevance information: it tells you how lecture theory, exercises, and exam preparation connect.
- Page 16: **1.2 Computer Graphics Overview**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 17: **Computer Graphics History**
  - Reading comment: Read this as camera geometry. Track how view-space positions become clip, normalized, and screen coordinates.
- Page 18: **Computer Graphics History**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 19: **Computer Graphics History**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 20: **Computer Graphics History**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 21: **Computer Graphics History**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 22: **Related Disciplines**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 23: **Applications**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 24: **1.3 Pixel-based Representations**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 25: **Raster Images**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 26: **Pixel**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 27: **Color**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 28: **LCD Raster Screen**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 29: **Raster Image Sizes**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 30: **1.4 3D Models**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 31: **3D Model Types**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 32: **Implicit Surfaces**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 33: **Quadrics**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 34: **Object Representation**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 35: **Polygonal Models 1/3**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 36: **Polygonal Models 1/4**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 37: **Polygonal Models 2/4**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 38: **Polygonal Models 3/4**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 39: **Polygonal Models 4/4**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 40: **Volumetric Models**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 41: **Model Generation**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 42: **Coordinate Systems**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 43: **Rendering**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 44: **1.5 Algorithmic Paradigms**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 45: **Photorealistic Rendering**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 46: **Non-Photorealistic Rendering (NPR)**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 47: **Image-Based Algorithms**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 48: **Object-Based Algorithms**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 49: **are assigned**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 50: **Literature and other sources used in this chapter**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 51: **Peters 2016. (Chapters 1, 3 & 21)**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.

## 01.1 Course Organization

Source location: Slides around 6-15

### Commentary

The organizational slides matter because they explain how the theory and programming parts fit together. The exercises are not separate from the lecture; they are the practical version of the same pipeline ideas. When the course says that slides are generally not self-explanatory, that is a warning: the bullet points are anchors, not a textbook.

Treat every exercise sheet as an applied checkpoint. Rendering pipeline, primitive types, shaders, transformations, projection, clipping, and rasterization are introduced in the lectures and then turned into OpenGL tasks. If a topic appears both in a lecture and an exercise, it is more likely to be exam relevant.

### Mental Model

Lecture slides give the vocabulary; exercises force you to connect that vocabulary to code and visible output.

### Check Yourself

Can you list the five exercise themes and connect each one to a later lecture chapter?

## 01.2 Computer Graphics Overview

Source location: Section 1.2

### Commentary

Computer graphics is about generating images from descriptions. The description can be pixel-based, object-based, physically motivated, artistic, or algorithmic. The common thread is that the computer must decide what color belongs at image samples.

Interactive graphics adds a time constraint. The image is not computed once and admired; it must respond to camera motion, user input, animation, and changing state. That is why real-time rendering often uses approximations and specialized GPU stages.

### Mental Model

Graphics is controlled image generation. Interactive graphics is controlled image generation under a strict time budget.

### Check Yourself

What changes when a renderer must be interactive rather than offline?

## 01.3 Pixel-Based Representations

Source location: Section 1.3

### Commentary

A pixel-based representation stores an image directly as samples on a grid. It is easy to display and edit locally, but it does not know the underlying 3D scene. If you zoom into a raster image, you reveal the sampling grid, not more geometry.

This is the first place where sampling becomes important. Resolution, color depth, aliasing, and frame time are not cosmetic details. They decide what information can be represented and how much data must be processed per second.

### Mental Model

A raster image is already the answer. It contains color samples, not the geometric reasons behind them.

### Check Yourself

Why can a pixel image be easy to display but hard to reinterpret as a 3D scene?

## 01.4 3D Models

Source location: Section 1.4

### Commentary

A 3D model is a structured description of objects before they become pixels. It may contain vertices, primitives, topology, normals, materials, textures, and transformations. Unlike a pixel image, it can be viewed from different camera positions.

The course mostly follows object-based rendering: start from model data, transform it, project it, rasterize it, shade it, test visibility, and finally update pixels. Later chapters explain these steps one by one.

### Mental Model

A model is not an image. It is a cause from which many possible images can be generated.

### Check Yourself

Which model attributes can influence final color besides vertex positions?

## 01.5 Algorithmic Paradigms

Source location: Section 1.5

### Commentary

The lecture contrasts ways to generate images. Rasterization works from objects toward pixels and is the dominant real-time pipeline. Ray-based methods work from image samples into the scene and are powerful for visibility and lighting but can be more expensive.

Do not memorize these paradigms as names only. Ask what direction information flows. Does the algorithm start from geometry and find covered pixels, or from pixels/rays and find visible geometry? That direction explains the strengths and weaknesses.

### Mental Model

Rasterization asks, 'Which samples does this primitive cover?' Ray casting asks, 'What does this sample see?'

### Check Yourself

Which paradigm fits OpenGL's standard real-time pipeline most directly?

## End-of-Lecture Summary

If you remember only one thing from Lecture 01, remember this: This lecture is the orientation layer for the whole course. It explains why interactive computer graphics is a pipeline problem: a scene must be represented, processed under time constraints, sampled into an image, and displayed fast enough for interaction.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
