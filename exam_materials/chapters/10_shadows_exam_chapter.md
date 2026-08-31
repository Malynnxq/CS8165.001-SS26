# Lecture 10 - Shadows Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/10_shadows.txt`
Extracted source pages: 60
Primary assignment connection: Rendering contest and integrated lighting tasks

This is the chapter itself: a readable explanation for studying before you drill the material. Read it before using cloze, matching, MC, sequencing, or assignment practice.

## 1. What Problem This Chapter Solves

Shadows are visibility tests from the light source, not only dark shapes seen by the camera. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `shadow`: Reduced direct illumination where an object blocks light from reaching a receiver. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 10.1 Definitions

Source location: Section 10.1

A shadow is not simply a dark texture. It is evidence that light visibility is blocked. Important distinctions include hard versus soft shadows, umbra versus penumbra, and geometric versus precomputed approaches.

For real-time graphics, shadows are usually approximated. The approximation must answer a visibility question cheaply enough for interactive rendering.

Study meaning: Shadows are light-space visibility made visible in the camera image.

Closed check: Why is shadow computation related to visibility determination?

### 10.2 Ground Plane Shadows

Source location: Section 10.2

Ground plane shadows project an object onto a receiving plane. This is simple and can look convincing in restricted scenes, but it assumes a known planar receiver and does not handle general shadowing between arbitrary objects.

The method is useful pedagogically because it makes the geometric nature of shadows explicit: a light source, an occluder, and a receiver define where the shadow lands.

Study meaning: A planar shadow is projected geometry on a known receiver.

Closed check: What scene limitation makes ground plane shadows less general than shadow maps?

### 10.3 Light Maps

Source location: Section 10.3

Light maps store precomputed lighting or shadow information in textures. They can be efficient at runtime, but they are limited when lights, objects, or geometry move dynamically.

This is another example of a recurring graphics tradeoff: precompute for speed, but lose flexibility. Real-time rendering often mixes precomputed and dynamic techniques.

Study meaning: A light map spends storage and preprocessing to save runtime shading work.

Closed check: Why are light maps less suitable for fully dynamic moving lights?

### 10.4 Shadow Volumes

Source location: Section 10.4

Shadow volumes construct the volume of space blocked from a light by an occluder. The camera view can then determine whether visible points lie inside that volume. Stencil buffer techniques are often associated with this method.

The strength is geometric precision for hard shadows. The cost is handling silhouette edges, volume construction, and robust stencil operations. It is a good contrast to shadow maps, which are image-based from the light view.

Study meaning: A shadow volume is the 3D region where the light cannot reach.

Closed check: Why are silhouette edges important for constructing shadow volumes?

### 10.5 Shadow Maps

Source location: Section 10.5

Shadow mapping renders the scene from the light's point of view and stores depth. During the camera pass, a surface point is transformed into light space and compared against the stored depth. If it is farther than what the light saw, it is in shadow.

This method is practical and widely used, but it has artifacts. Shadow acne comes from precision/self-comparison issues. Bias can reduce acne but too much bias causes detached shadows. Resolution, filtering, and light projection strongly affect quality.

Study meaning: Shadow maps reuse the depth-buffer idea, but from the light's camera.

Closed check: What exactly is stored in a shadow map?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### shadow

Reduced direct illumination where an object blocks light from reaching a receiver. In an exam answer, connect `shadow` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

### occluder

Object that blocks light. In an exam answer, connect `occluder` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

### receiver

Surface where the shadow appears. In an exam answer, connect `receiver` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

### shadow map

Depth image rendered from the light's point of view for later visibility comparison. In an exam answer, connect `shadow map` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

### shadow volume

Volume of space hidden from a light by an occluder. In an exam answer, connect `shadow volume` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

### projective shadow

Shadow construction based on projecting geometry onto a receiver. In an exam answer, connect `projective shadow` to the chapter chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`point is shadowed if something is closer to the light along the same light ray`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `Rendering contest and integrated lighting tasks`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.

The trap is dangerous because it usually sounds close to the truth. High exam performance depends on catching these near-misses quickly. When a multiple-choice option looks plausible, test it against the full chain: input, operation, output, next use. If one of those links is missing or wrong, the option is probably a distractor.

## 8. What A Strong Answer Must Contain

- The problem this chapter solves.
- The important data or object representation.
- The operation, algorithm, formula, or API mechanism.
- The output representation.
- The next pipeline stage or later use.
- One assignment or OpenGL/software connection.
- One typical mistake and the corrected distinction.

## 9. Closed-Format Self-Test

1. Complete the chain: `light -> possible blocker -> ____ -> light-space visibility test -> lit or shadowed result`
2. Match `occluder` to its role: Object that blocks light.
3. Select the dangerous misconception: Do not explain a shadow only from the camera view; the key test is light-space visibility.
4. Explain in one sentence why `receiver` belongs in this chapter.

## 10. End Condition

You are done with Lecture 10 only when you can read a new question, recognize that it belongs to `Shadows`, and reconstruct the relevant part of `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.
