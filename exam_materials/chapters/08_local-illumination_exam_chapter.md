# Lecture 08 - Local Illumination Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/08_local-illumination.txt`
Extracted source pages: 62
Primary assignment connection: Rendering contest and shader-related tasks

This is the chapter itself: a readable explanation for studying before you drill the material. Read it before using cloze, matching, MC, sequencing, or assignment practice.

## 1. What Problem This Chapter Solves

Local illumination computes color from surface orientation, light direction, view direction, and material response. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `surface point + normal + light + view + material -> lighting equation -> shaded color`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `surface normal`: Vector describing surface orientation and controlling diffuse/specular response. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 08.1 Physics of Light

Source location: Section 8.1

The physics slides provide intuition for light as energy interacting with surfaces. For this course, the goal is not full physical simulation but a usable model for real-time rendering.

Important terms are reflection, absorption, wavelength/color, intensity, and direction. These terms become shader inputs or material parameters later. The simplified model must still preserve the relation between light direction, surface orientation, and observed brightness.

Study meaning: Shading is an approximation of light-surface interaction that is cheap enough for rendering.

Closed check: Why does surface orientation affect diffuse brightness?

### 08.2 Light Sources

Source location: Section 8.2

Light source models define where light comes from and how its direction and intensity are computed. Directional lights approximate distant sources with parallel rays. Point lights emit from a position and often include attenuation. Spotlights add a directional cone.

In shader code, the type of light determines how you compute the light vector. A directional light can use a fixed direction; a point light requires subtracting the surface position from the light position.

Study meaning: Different light types mainly change how the light direction and intensity are computed at the surface point.

Closed check: What is the difference between a directional light vector and a point light vector?

### 08.3 Material Models

Source location: Section 8.3

A material model tells the shader how a surface responds to light. Diffuse material scatters light broadly; specular material creates view-dependent highlights; ambient terms approximate background illumination.

Material coefficients are not arbitrary decoration. They scale the contribution of each lighting term. If the specular coefficient is zero, the surface should not show a specular highlight under that model.

Study meaning: Light asks what arrives; material answers how the surface reacts.

Closed check: Which material parameter would you adjust to reduce shiny highlights?

### 08.4 Phong Illumination Model

Source location: Section 8.4

The Phong illumination model combines ambient, diffuse, and specular terms. Diffuse lighting uses the angle between normal and light direction. Specular lighting also depends on the viewer because highlights move with the view direction.

The formula is less important than the decomposition. Ambient is a rough constant approximation. Diffuse is orientation-dependent matte reflection. Specular is view-dependent shininess. A correct answer should name the vectors and normalize them.

Study meaning: Phong-style lighting is a sum of simple terms, each modeling a different visual effect.

Closed check: Why does the specular term depend on the view direction?

### 08.5 Shading

Source location: Section 8.5

Shading decides where the illumination calculation is evaluated and how results are interpolated. Flat shading uses one value per primitive. Gouraud shading evaluates at vertices and interpolates colors. Phong shading interpolates normals and evaluates lighting per fragment.

Per-fragment shading is more expensive but can represent highlights more accurately. This connects directly to the pipeline: interpolation during rasterization provides the data used by the fragment shader.

Study meaning: The shading method decides what is computed at vertices and what is computed at fragments.

Closed check: Why can Gouraud shading miss a small specular highlight?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### surface normal

Vector describing surface orientation and controlling diffuse/specular response. In an exam answer, connect `surface normal` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

### ambient term

Approximate base illumination independent of direct light direction. In an exam answer, connect `ambient term` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

### diffuse reflection

View-independent light response based on the angle between normal and light direction. In an exam answer, connect `diffuse reflection` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

### specular reflection

View-dependent highlight term based on reflection or half-vector alignment. In an exam answer, connect `specular reflection` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

### Phong model

Local illumination model combining ambient, diffuse, and specular components. In an exam answer, connect `Phong model` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

### material coefficient

Parameter controlling how strongly a surface responds to lighting terms. In an exam answer, connect `material coefficient` to the chapter chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`color = ambient + diffuse + specular`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `Rendering contest and shader-related tasks`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `surface point + normal + light + view + material -> lighting equation -> shaded color`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.

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

1. Complete the chain: `surface point + normal + light + view + material -> ____ -> shaded color`
2. Match `ambient term` to its role: Approximate base illumination independent of direct light direction.
3. Select the dangerous misconception: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
4. Explain in one sentence why `diffuse reflection` belongs in this chapter.

## 10. End Condition

You are done with Lecture 08 only when you can read a new question, recognize that it belongs to `Local Illumination`, and reconstruct the relevant part of `surface point + normal + light + view + material -> lighting equation -> shaded color` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.
