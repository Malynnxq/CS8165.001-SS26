# Lecture 08 - Local Illumination

Source chunk: `course_text_parts/03_lectures/08_local-illumination.txt`
Extracted slide pages in source chunk: 62

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture explains how visible surface points receive color from local light, material, normal, and view information. It is about shading a point, not solving all global light transport.

## How To Read This Lecture

- First read the big picture and the mental models.
- Then open the source chunk and compare the slide bullets to the commentary.
- After each section, answer the check question without notes.
- If the check feels vague, revisit the source pages listed for that section.

## Slide Walkthrough

This section adds a short reading comment for every extracted slide page. Use it when the original PDF page is too terse.

- Page 1: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 2: **Local Illumination**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 3: **8.1 Physics of Light**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 4: **8.1 Physics of Light**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 5: **Electromagnetic Radiation**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 6: **Visible Light**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 7: **Visible Light**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 8: **Light Spectra**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 9: **Black-Body Radiation**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 10: **Black-Body Radiation**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 11: **Spectral Density Function (SDF)**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 12: **Light Perception**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 13: **Interpreting SDFs**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 14: **Representing SDFs**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 15: **8.2 Light Sources**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 16: **Light Sources**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 17: **Point Light Sources**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 18: **Cone Light Sources**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 19: **Light Attenuation**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 20: **Area Light Sources**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 21: **Directed Light**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 22: **Local vs. Gobal Illumination**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 23: **Ambient Light**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 24: **8.3 Material Models**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 25: **Material Models**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 26: **Materials vs. Textures**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 27: **Light Material Interaction 1/3**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 28: **Light Material Interaction 2/3**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 29: **Light Material Interaction 3/3**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 30: **Reflection = SDF x SRF**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 31: **Reflection Modeling 1/2**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 32: **Reflection Modeling 2/2**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 33: **8.4 Phong Illumination Model**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 34: **Empirical Observations**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 35: **Illumination Models**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 36: **yaR**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 37: **Diffuse Intensity 2/3**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 38: **Diffuse Intensity 3/3**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 39: **Ambient Intensity 1/2**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 40: **Ambient Intensity 2/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 41: **Specular Intensity 1/3**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 42: **Reflection Vector 𝑟⃗**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 43: **Specular Intensity 2/3**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 44: **Specular Exponent 𝑝**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 45: **Specular Intensity 3/3**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 46: **Blinn-Phong Illumination Model 1/2**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 47: **Blinn-Phong Illumination Model 2/2**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 48: **Phong Illumination Model**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 49: **Phong Illumination Model**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 50: **8.5 Shading**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 51: **Shading**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 52: **Shading Computation**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 53: **Flat Shading**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 54: **Gouraud Shading 1/5**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 55: **Gouraud Shading 2/5**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 56: **Gouraud Shading 3/5**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 57: **Gouraud Shading 4/5**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 58: **Gouraud Shading 5/5**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.
- Page 59: **Phong Shading 1/2**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 60: **Phong Shading 2/2**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 61: **Literature and other sources used in this chapter**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 62: **Lesen und Ausprobieren**
  - Reading comment: Read this as local shading. Name the normal, light vector, view vector, material term, and where the computation happens.

## 08.1 Physics of Light

Source location: Section 8.1

### Commentary

The physics slides provide intuition for light as energy interacting with surfaces. For this course, the goal is not full physical simulation but a usable model for real-time rendering.

Important terms are reflection, absorption, wavelength/color, intensity, and direction. These terms become shader inputs or material parameters later. The simplified model must still preserve the relation between light direction, surface orientation, and observed brightness.

### Mental Model

Shading is an approximation of light-surface interaction that is cheap enough for rendering.

### Check Yourself

Why does surface orientation affect diffuse brightness?

## 08.2 Light Sources

Source location: Section 8.2

### Commentary

Light source models define where light comes from and how its direction and intensity are computed. Directional lights approximate distant sources with parallel rays. Point lights emit from a position and often include attenuation. Spotlights add a directional cone.

In shader code, the type of light determines how you compute the light vector. A directional light can use a fixed direction; a point light requires subtracting the surface position from the light position.

### Mental Model

Different light types mainly change how the light direction and intensity are computed at the surface point.

### Check Yourself

What is the difference between a directional light vector and a point light vector?

## 08.3 Material Models

Source location: Section 8.3

### Commentary

A material model tells the shader how a surface responds to light. Diffuse material scatters light broadly; specular material creates view-dependent highlights; ambient terms approximate background illumination.

Material coefficients are not arbitrary decoration. They scale the contribution of each lighting term. If the specular coefficient is zero, the surface should not show a specular highlight under that model.

### Mental Model

Light asks what arrives; material answers how the surface reacts.

### Check Yourself

Which material parameter would you adjust to reduce shiny highlights?

## 08.4 Phong Illumination Model

Source location: Section 8.4

### Commentary

The Phong illumination model combines ambient, diffuse, and specular terms. Diffuse lighting uses the angle between normal and light direction. Specular lighting also depends on the viewer because highlights move with the view direction.

The formula is less important than the decomposition. Ambient is a rough constant approximation. Diffuse is orientation-dependent matte reflection. Specular is view-dependent shininess. A correct answer should name the vectors and normalize them.

### Mental Model

Phong-style lighting is a sum of simple terms, each modeling a different visual effect.

### Check Yourself

Why does the specular term depend on the view direction?

## 08.5 Shading

Source location: Section 8.5

### Commentary

Shading decides where the illumination calculation is evaluated and how results are interpolated. Flat shading uses one value per primitive. Gouraud shading evaluates at vertices and interpolates colors. Phong shading interpolates normals and evaluates lighting per fragment.

Per-fragment shading is more expensive but can represent highlights more accurately. This connects directly to the pipeline: interpolation during rasterization provides the data used by the fragment shader.

### Mental Model

The shading method decides what is computed at vertices and what is computed at fragments.

### Check Yourself

Why can Gouraud shading miss a small specular highlight?

## End-of-Lecture Summary

If you remember only one thing from Lecture 08, remember this: This lecture explains how visible surface points receive color from local light, material, normal, and view information. It is about shading a point, not solving all global light transport.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
