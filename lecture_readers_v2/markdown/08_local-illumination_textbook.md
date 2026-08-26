# Chapter 8 — Local Illumination

> **Purpose.** This chapter reconstructs Lecture 8 as a readable lesson rather than a transcription of slides. We begin with the physical question—why a surface has a particular visible color—and progressively simplify it until we obtain practical illumination and shading equations used in interactive graphics.
>
> **Primary course source:** `course_text_parts/03_lectures/08_local-illumination.txt` (Lecture 8 slides, 23 June 2026).

## 1. We can now draw geometry—but why does it look like anything?

The previous lectures built most of a rendering pipeline:

```text
3D geometry
→ transformations
→ projection
→ clipping
→ rasterization
→ visibility determination
→ visible fragments
```

At this point we know **where** a visible fragment is. But we have not yet answered:

> What color/intensity should that fragment have?

If every triangle were assigned one constant RGB value, a sphere could look like a flat disk and complex geometry would be difficult to perceive. Human perception relies strongly on brightness gradients and highlights to infer orientation, curvature, and material.

**Illumination** simulates the interaction between light and surfaces so that we can calculate those colors.

The basic ingredients are:

```text
light source
+ surface position
+ surface orientation
+ material
+ viewer
→ illumination model
→ outgoing/displayed color
```

---

## 2. Local versus global illumination

Suppose a lamp illuminates a red ball.

A **local illumination model** asks primarily:

> How does light arriving directly from the modeled light source interact with this particular surface point?

It does not fully simulate all paths that light may have taken through the scene.

A **global illumination model** additionally considers interactions involving other objects—for example indirect reflected light, physically generated shadows, and interreflection.

Real light transport is global. Local illumination is a computational approximation chosen because it is much cheaper and often visually convincing enough for interactive rendering.

The Phong model studied later in this chapter is a local illumination model.

---

# Part I — What is light?

## 3. Light as electromagnetic radiation

Electromagnetic radiation spans a huge range of wavelengths. Human vision detects only a small interval, approximately **400–700 nm**, which we call visible light.

Different wavelengths stimulate our visual system differently and are perceived as different colors.

Wavelength `λ` and frequency `f` are related by

\[
c=\lambda f,
\]

so

\[
\lambda=\frac{c}{f},
\]

where `c` is the speed of light.

For computer graphics, the important idea is not to memorize the entire electromagnetic spectrum. It is that **light has a wavelength-dependent distribution of energy**.

---

## 4. A light source does not emit “an RGB number” in nature

Real light sources emit spectra.

A **spectral density function (SDF)** describes how much energy a light contains at each wavelength:

\[
S(\lambda)=\text{energy/intensity at wavelength }\lambda.
\]

Two lights that both look approximately white can have very different spectral distributions.

Examples include:

- a narrow spectral peak;
- a broad approximately uniform spectrum;
- a broad spectrum with one dominant wavelength;
- arbitrary mixtures of wavelengths.

Black-body radiation provides an important physical example: the emitted spectrum changes with temperature, which is why heated objects and stars can have different apparent colors.

---

## 5. From spectra to perceived color

The lecture connects spectral shape to familiar perceptual descriptions:

- **hue** — roughly associated with dominant wavelength/color family;
- **saturation** — how strongly one color dominates rather than being mixed toward neutral light;
- **lightness/value/luminance-like brightness** — associated with total perceived intensity.

A full spectral renderer can discretize the wavelength axis and carry many spectral samples.

Most interactive graphics instead compresses color to three channels:

\[
C=(R,G,B).
\]

This is computationally convenient but is only an approximation to full spectral behavior.

---

# Part II — Modeling light sources

## 6. A graphics light is an abstraction

A virtual light source normally has parameters such as color, position, direction, and extent. It does **not** necessarily have visible geometry.

For example, a point light can illuminate a room even though no polygonal light bulb exists at that position.

This distinction matters:

> A **light source** is part of the illumination model; a **visible lamp model** is scene geometry. They are separate concepts unless explicitly connected.

---

## 7. Point lights

A **point light** has a position

\[
P_L=(x_L,y_L,z_L)
\]

and a light color/intensity such as

\[
C_L=(R_L,G_L,B_L).
\]

It radiates in all directions from one idealized point.

For a surface point `P`, the direction toward the light is obtained from

\[
L=P_L-P,
\]

usually followed by normalization:

\[
l=\frac{L}{\|L\|}.
\]

This vector `l` will soon enter the diffuse and specular equations.

---

## 8. Spot/cone lights

A spotlight is essentially a point-like source whose radiation is restricted to a cone.

It needs additional parameters such as:

- a direction;
- a cutoff angle;
- a falloff/exponent controlling how intensity decreases toward the cone boundary.

The important conceptual step is that illumination can depend not only on distance from a light, but also on **direction relative to the light source itself**.

---

## 9. Distance attenuation

If a point-like source spreads a fixed amount of energy over larger and larger spherical surfaces, the same energy is distributed over an area proportional to `d²`. This motivates inverse-square behavior.

Interactive graphics often uses a tunable attenuation approximation such as

\[
f_{att}=\min\left(\frac{1}{c_1+c_2d+c_3d^2},1\right),
\]

where `d` is distance to the light and the coefficients are chosen for the desired behavior.

The `min(...,1)` prevents attenuation from accidentally amplifying the source beyond its base intensity.

When attenuation is used, a light contribution is multiplied by `f_att`.

---

## 10. Area lights

A real lamp has nonzero area. An **area light** models an emitting region rather than one mathematical point.

Why should this matter?

Different points on the area source illuminate a surface from slightly different directions. This becomes especially important for effects such as soft shadows in more advanced/global illumination methods.

In a local model, an area light may be approximated by samples or simplified representations.

---

## 11. Directional lights

A **directional light** models a source so far away that its rays can be treated as parallel throughout the scene.

The classic example is sunlight for a scene whose size is tiny relative to the Sun's distance.

Instead of a light position, store essentially a direction.

Because the idealized source is infinitely far away, the model normally does not attenuate with distance across the scene.

---

## 12. Ambient light

Local illumination has a problem: if a surface receives no direct modeled light, it can become completely black even though real rooms contain indirect illumination from many reflections.

The old/simple solution is **ambient light**:

> Add a constant undirected baseline brightness everywhere.

Ambient light is not a physical simulation of the actual indirect paths. It is a cheap approximation to “the rest of the room is not perfectly dark.”

This distinction will matter when interpreting the Phong model.

---

# Part III — Why materials have colors

## 13. Light can be reflected, absorbed, or transmitted

When incoming light reaches a material, its energy can undergo several processes:

- **reflection** — energy leaves the surface back into the surrounding space;
- **absorption** — energy is taken up by the material;
- **transmission** — energy passes through the material, often with refraction.

Very roughly:

```text
incoming energy I
       ↓
 ┌─────┼─────┐
 ↓     ↓     ↓
 R     A     T
reflection absorption transmission
```

Different materials distribute energy differently, and the distribution can depend on wavelength.

An opaque colored material reflects some wavelengths and absorbs others. A black surface absorbs most visible light. An ideal mirror reflects essentially all incoming energy in a specific direction. A transparent medium transmits much of it.

Lecture 8 mainly concentrates on reflection/absorption behavior suitable for local surface illumination.

---

## 14. Spectral response functions: the material as a wavelength filter

A material can be described spectrally by a **spectral response function (SRF)**:

\[
R(\lambda)=\text{fraction/response at wavelength }\lambda.
\]

If incoming light has spectrum `S(λ)`, then the reflected spectrum is conceptually related to

\[
S_{reflected}(\lambda)=S(\lambda)R(\lambda).
\]

This explains an important everyday fact:

> An object's apparent color is not solely an intrinsic property of the object. It depends on both the material response **and the spectrum of the illuminating light**.

A red material under illumination containing almost no red wavelength energy cannot magically reflect strong red energy.

Sensors—the eye, film, or a digital camera—also have wavelength-dependent responses. Ultimately perceived/measured color depends on light spectrum × material response × sensor response.

---

## 15. Why RGB multiplication makes conceptual sense

Real spectral multiplication is expensive. In RGB rendering we approximate the same idea channel-wise.

If a light has

\[
L=(L_R,L_G,L_B)
\]

and a diffuse material has

\[
k_d=(k_R,k_G,k_B),
\]

then the color interaction is approximated by component-wise multiplication:

\[
k_d\odot L
=
(k_RL_R,\;k_GL_G,\;k_BL_B).
\]

So when you later see `k_d L_d` in an illumination equation, it is useful to think:

> **light spectrum approximation × material response approximation.**

---

# Part IV — From physics to a practical illumination model

## 16. What information does an illumination model need?

At a surface point `P`, a practical local illumination model needs some combination of:

- surface position `P`;
- surface normal `n`;
- direction toward the light `l`;
- direction toward the viewer `v`;
- light properties;
- material properties.

The normal is especially important because it describes the local surface orientation.

The Phong model decomposes visible reflection into three terms:

```text
ambient + diffuse + specular
```

Each term approximates a visually distinct phenomenon.

---

# Part V — Diffuse reflection

## 17. Why a matte surface gets darker when tilted away from a light

Imagine a small patch of matte white paper.

When it faces the light directly, incoming rays are concentrated over a relatively small surface area. When the patch is tilted, the same bundle of rays is effectively spread across a larger surface area, so illumination per unit area decreases.

This angular dependence is modeled by **Lambert's cosine law**.

Let

- `n` = normalized surface normal;
- `l` = normalized direction from the surface toward the light.

Then

\[
n\cdot l=\cos\theta.
\]

When the light is aligned with the normal, `θ=0` and the dot product is `1`.

At grazing incidence, `θ≈90°` and the dot product approaches `0`.

If the light is behind the surface, the dot product becomes negative; ordinary diffuse reflection should not become “negative light,” so clamp it:

\[
\max(0,n\cdot l).
\]

---

## 18. The diffuse term

The lecture's diffuse contribution is

\[
I_{diffuse}=k_d L_d\max(0,n\cdot l).
\]

Interpret every factor:

- `k_d` — how strongly the material diffusely reflects light (usually RGB/component-wise);
- `L_d` — diffuse light intensity/color;
- `n·l` — orientation factor.

A crucial property:

> Ideal diffuse reflection is **viewer-independent**.

Once a surface is illuminated, rotating the camera around it does not change the Lambertian diffuse term, assuming the surface point, normal, and light remain fixed.

---

# Part VI — Ambient reflection

## 19. The ambient term

Phong-style ambient illumination is extremely simple:

\[
I_{ambient}=k_aL_a.
\]

Here

- `k_a` = material's ambient coefficient;
- `L_a` = scene ambient light intensity.

There is no `n·l`, no viewer vector, and normally no position dependence.

That simplicity tells you exactly what the model is doing: it is not tracing indirect light. It is adding an empirical baseline.

---

# Part VII — Specular reflection

## 20. Why shiny highlights move when the viewer moves

A polished surface behaves differently from matte chalk. Reflection is concentrated around a preferred mirror direction.

Therefore specular brightness depends on **where the viewer is**.

Define:

- `l` = direction toward the light;
- `n` = surface normal;
- `r` = ideal mirror-reflection direction;
- `v` = direction toward the viewer.

The highlight is strongest when

\[
r\approx v.
\]

Because both are normalized,

\[
r\cdot v=\cos\alpha
\]

measures their angular alignment.

---

## 21. Deriving the reflection vector

The lecture uses

\[
r=2n(n\cdot l)-l,
\]

assuming normalized `n` and `l` and the stated direction convention.

Why?

The projection of `l` onto the normal is

\[
(n\cdot l)n.
\]

Geometric reflection mirrors the incident direction around the normal. Doubling the normal projection and subtracting the original direction gives the reflected direction.

You do not need to regard this as a magical memorized formula. It is vector decomposition plus symmetry around the normal.

---

## 22. The Phong specular term

The model uses

\[
I_{specular}=k_sL_s\max(0,r\cdot v)^p.
\]

Interpretation:

- `k_s` — material's specular reflectivity;
- `L_s` — specular light intensity/color;
- `r·v` — how close the viewer is to the ideal reflection direction;
- `p` — specular/shininess exponent.

### What does `p` do?

For numbers between `0` and `1`, raising them to a larger power makes them shrink faster.

For example:

```text
0.8^1   = 0.8
0.8^5   ≈ 0.33
0.8^100 ≈ almost 0
```

Only directions extremely close to perfect alignment survive a large exponent.

Therefore:

- small `p` → broad highlight;
- large `p` → narrow, concentrated highlight.

This is a mathematical control for apparent shininess.

---

# Part VIII — Blinn–Phong

## 23. Replace the reflection vector with a halfway vector

Blinn–Phong uses a different angular comparison.

Construct the halfway direction between the light and viewer:

\[
h=\frac{l+v}{\|l+v\|}.
\]

Then compare `h` to the surface normal:

\[
I_{specular}=k_sL_s\max(0,n\cdot h)^p.
\]

The geometric idea is simple:

> If the normal points toward the direction halfway between light and viewer, the surface is oriented appropriately for a strong specular reflection toward the viewer.

Be careful with slide shorthand such as `h=l+v`: for a dot product interpreted as a cosine, the halfway vector should be normalized.

Phong and Blinn–Phong are related empirical approximations, but their exponents are not numerically interchangeable in a strict physical sense.

---

# Part IX — Assemble the Phong illumination model

## 24. Add the components

For one light, the classic local model is conceptually

\[
I=I_{ambient}+I_{diffuse}+I_{specular}.
\]

Using Phong specular reflection:

\[
I=
 k_aL_a
 +k_dL_d\max(0,n\cdot l)
 +k_sL_s\max(0,r\cdot v)^p.
\]

Or using Blinn–Phong:

\[
I=
 k_aL_a
 +k_dL_d\max(0,n\cdot l)
 +k_sL_s\max(0,n\cdot h)^p.
\]

If a positional light uses attenuation, its direct terms can additionally be scaled by `f_att`.

For multiple lights, the direct contributions are normally accumulated across light sources while the ambient treatment depends on the chosen implementation.

---

## 25. Understand the equation instead of memorizing it

Read the Phong equation as three questions:

### Ambient

> How much baseline illumination should this material receive?

No geometry required.

### Diffuse

> How directly does the surface face the light?

Uses `n·l`; viewer irrelevant.

### Specular

> Is the viewer near the preferred reflection direction?

Uses `r·v` (Phong) or `n·h` (Blinn–Phong); viewer matters.

This decomposition makes the formula much easier to reconstruct in an exam.

---

# Part X — Illumination model versus shading model

## 26. These terms are not synonyms

This distinction is essential.

An **illumination model** answers:

> Given one surface point, its normal, material, lights, and viewer, what intensity/color should that point have?

Examples: Phong or Blinn–Phong illumination.

A **shading method** answers:

> Across a polygonal surface made of discrete vertices and fragments, where do we evaluate illumination and what do we interpolate?

Examples:

- flat shading;
- Gouraud shading;
- Phong shading.

**Phong illumination** and **Phong shading** are therefore different concepts despite sharing Phong's name.

---

# Part XI — Flat shading

## 27. One illumination calculation for the entire polygon

Flat shading evaluates illumination once for a polygon—perhaps at a representative point—and uses that result everywhere on the polygon.

```text
one polygon
→ one normal / one illumination result
→ one approximately constant color
```

This is cheap and appropriate when the polygon is intended to represent an actual planar facet.

But if many triangles approximate a smooth curved surface, each triangle can have a visibly different constant shade. The mesh looks faceted.

---

# Part XII — Gouraud shading

## 28. Move illumination calculations to the vertices

Gouraud shading improves smoothness by computing illumination at vertices.

For each vertex:

1. obtain a vertex normal;
2. evaluate the illumination model;
3. obtain a vertex intensity/color.

Then rasterization interpolates these intensities/colors across the triangle.

Symbolically, if barycentric coordinates at a fragment are `α,β,γ`, then

\[
I(P)=\alpha I_0+\beta I_1+\gamma I_2,
\]

with

\[
\alpha+\beta+\gamma=1.
\]

This directly connects to the interpolation machinery from Lecture 6.

---

## 29. Where do smooth vertex normals come from?

A triangle mesh has geometric **face normals**. But a smooth surface approximation should not necessarily look like independent flat triangles.

At a shared smooth vertex, construct a vertex normal from neighboring face normals, often through some weighted average, and normalize it.

Adjacent triangles that share the same vertex normal then produce continuous-looking illumination across the common edge.

But not every edge should be smooth. At a cube corner, averaging all adjacent normals would make the cube look rounded.

So a model must distinguish:

- **soft/smooth edges** → share/average vertex normals;
- **hard edges** → use separate normals on each side.

This is a modeling decision, not merely a rendering switch.

---

## 30. Gouraud shading's fundamental limitation

Gouraud interpolates **already calculated colors/intensities**.

Suppose a small bright specular highlight lies in the middle of a large triangle but none of the triangle's vertices lies inside the highlight.

Then all vertex illumination values may be dark. Interpolating dark values cannot invent a bright center.

```text
vertex: dark -------- dark :vertex
             ↑
     true highlight here
     but no vertex sampled it
```

Therefore Gouraud shading can miss interior lighting variation.

Finer tessellation helps because more vertices sample the illumination field, but that increases geometry.

---

# Part XIII — Phong shading

## 31. Interpolate normals, not final colors

Phong shading changes what is interpolated.

At each vertex, provide a normal. Rasterization interpolates the normal across the triangle:

\[
n'(P)=\alpha n_0+\beta n_1+\gamma n_2.
\]

The interpolated vector generally no longer has unit length, so normalize it:

\[
n(P)=\frac{n'(P)}{\|n'(P)\|}.
\]

Then evaluate the illumination model **per fragment** using that normal.

So:

```text
Gouraud:
vertex normals
→ lighting at vertices
→ interpolate colors

Phong shading:
vertex normals
→ interpolate normals
→ lighting at fragments
```

That one distinction explains most of their visual difference.

---

## 32. Why Phong shading captures highlights better

A highlight can exist at an interior fragment even when no vertex is highlighted.

With Phong shading, the fragment receives its own interpolated normal and the illumination equation is evaluated there. Thus the angular relationship between normal, light, and viewer can produce the highlight exactly where it belongs at image resolution.

Advantages:

- smoother appearance;
- interior specular highlights can appear;
- lighting is evaluated per fragment.

Cost:

- many more illumination calculations;
- interpolated normals require renormalization.

Modern GPUs make this tradeoff practical, which is why per-fragment lighting is common.

---

# Part XIV — Connecting Lectures 6, 7, and 8

## 33. What happens to one triangle?

You can now connect three lectures into one pipeline.

### Lecture 6: rasterization

Determine which fragments the triangle covers and interpolate attributes.

### Lecture 7: visibility

Use fragment depth to determine whether each candidate fragment is visible.

### Lecture 8: illumination/shading

Use material, light, view direction, and interpolated normal/attributes to determine the visible fragment's color.

Conceptually:

```text
triangle vertices
(position, normal, material attributes)
        ↓
rasterization
        ↓
fragment + interpolated depth/normal/etc.
        ↓
depth test
        ↓
visible fragment
        ↓
local illumination
        ↓
RGB output
```

In an actual GPU pipeline, the precise ordering of fragment shading and early/late depth tests can be optimized, but this conceptual sequence is the right mental model for the course material.

---

# Part XV — Worked reasoning examples

## 34. Diffuse orientation

Let

\[
n=(0,0,1).
\]

If the normalized light direction is also

\[
l=(0,0,1),
\]

then

\[
n\cdot l=1,
\]

so the diffuse orientation factor is maximal.

If

\[
l=(1,0,0),
\]

then

\[
n\cdot l=0,
\]

so the light is tangent to the surface and contributes no Lambertian diffuse term.

If

\[
l=(0,0,-1),
\]

then

\[
n\cdot l=-1,
\]

but clamping gives

\[
\max(0,-1)=0.
\]

The light is on the back side of the surface.

---

## 35. Why specular reflection is viewer-dependent

Keep light and surface fixed, so `r` is fixed.

Viewer A has

\[
r\cdot v_A\approx1.
\]

Viewer B has

\[
r\cdot v_B\approx0.4.
\]

For `p=20`:

\[
1^{20}=1,
\]

while

\[
0.4^{20}\approx 1.1\times10^{-8}.
\]

So A sees a strong highlight while B essentially does not.

This is why highlights seem to move over an object as you move your head.

---

## 36. Why Gouraud can miss a highlight

Suppose a triangle's vertex specular intensities are

\[
I_0=0.02,\quad I_1=0.02,\quad I_2=0.02.
\]

Any linear interpolation of these values is still `0.02`.

But the true illumination equation at the center might produce `0.9` because the interpolated local normal happens to align with the reflection condition there.

Gouraud never evaluates that condition at the center, so it cannot discover it.

Phong shading can.

---

# Part XVI — Common confusions

## 37. “Phong model” versus “Phong shading”

Do not say they are the same.

- **Phong illumination model:** ambient + diffuse + specular equation.
- **Phong shading:** interpolate normals and evaluate illumination per fragment.

You can use Phong shading with a different illumination model, and conceptually you can use the Phong illumination equation with different shading strategies.

---

## 38. “Ambient light is global illumination”

Not really.

Ambient light is a **local-model approximation** intended to imitate some visual consequence of indirect/global illumination. It does not calculate actual interreflection paths.

---

## 39. “The normal is just for geometry”

The normal is one of the most important illumination inputs. It determines how the local surface is oriented relative to the light and viewer.

Changing normals without changing vertex positions can radically change the perceived shape of a mesh.

---

## 40. “A material has one fixed observed color”

Its appearance depends on illumination. In the spectral view, reflected light is determined by incoming spectrum and material response. In the RGB approximation, light and material channels interact multiplicatively.

---

# Part XVII — Exam-oriented mastery

## 41. What you should be able to derive or explain

You should be able to explain, not merely recite:

1. What illumination adds to the rendering pipeline.
2. Local versus global illumination.
3. What an SDF represents.
4. Why different light spectra can produce different perceived colors.
5. Point, spotlight, area, directional, and ambient light abstractions.
6. Why point-light intensity is often attenuated with distance.
7. Reflection, absorption, and transmission.
8. What an SRF represents.
9. Why reflected spectrum can be understood as incoming SDF × material response.
10. Why RGB component multiplication approximates spectral interaction.
11. Which vectors/parameters a local illumination model needs.
12. Why Lambertian diffuse intensity contains `max(0,n·l)`.
13. Why diffuse reflection is viewer-independent.
14. Why the ambient term contains no angular factor.
15. How the reflection vector relates to the surface normal.
16. Why Phong specular uses `r·v`.
17. What increasing the specular exponent does.
18. How Blinn–Phong replaces `r·v` with a halfway-vector relationship.
19. How ambient, diffuse, and specular contributions combine.
20. Illumination model versus shading model.
21. Flat versus Gouraud versus Phong shading.
22. How vertex normals create visually smooth surfaces.
23. Why hard edges sometimes require separate normals.
24. Why Gouraud shading can miss an interior highlight.
25. Why interpolated normals must be renormalized for Phong shading.

---

## 42. Compact comparison

| Method | Illumination evaluated | Interpolated quantity | Main consequence |
|---|---|---|---|
| Flat shading | once per face | usually nothing relevant to lighting | cheap, faceted |
| Gouraud shading | at vertices | intensity/color | smooth but can miss interior highlights |
| Phong shading | per fragment | normal | better highlights, more computation |

And for the reflection terms:

| Term | Main vectors | Viewer-dependent? | Visual role |
|---|---|---:|---|
| Ambient | none | No | baseline brightness |
| Diffuse | `n`, `l` | No | matte orientation cue |
| Phong specular | `r`, `v` | Yes | shiny highlight |
| Blinn–Phong specular | `n`, `h` | Yes | alternative shiny highlight |

---

# 43. Final mental model

Remember the chapter as one causal chain:

```text
Real light has a wavelength spectrum
        ↓
Light sources provide incoming energy
        ↓
Materials absorb / reflect / transmit wavelengths
        ↓
We approximate spectra with RGB
        ↓
Surface orientation controls diffuse reflection
        ↓
Viewer/reflection alignment controls specular reflection
        ↓
Phong combines
ambient + diffuse + specular
        ↓
But a mesh has only discrete vertices
        ↓
Shading decides how lighting information spreads across triangles
        ↓
flat: one result per face
Gouraud: interpolate vertex colors
Phong: interpolate normals, light per fragment
```

The deepest idea is:

> **Illumination determines how light and material interact at a surface point; shading determines how that information is evaluated and distributed across rasterized geometry.**

Once that distinction is clear, most of Lecture 8 becomes a connected system rather than a collection of formulas.
