# 04 - Closed-Format Drills

These are designed for selection, matching, completion, and quick decision practice. Answers are at the end.

## Lecture 01 - Introduction

Q1. Which statement best describes the core idea?

A. The lecture is mainly a list of unrelated definitions.
B. The lecture is only relevant for historical context.
C. The lecture can be ignored if the final image looks correct.
D. Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.

Q2. Complete the chain:

`scene or image description -> representation choice -> ____ -> visible image -> interaction or analysis`

Q3. Match the term `raster image`.

A. A final exam score calculation.
B. A file organization convention only.
C. A grid of stored pixel samples; it is already an image, not a 3D scene.
D. Same meaning as `pixel`.

Q4. Select the dangerous misconception.

A. It can be practiced with matching and sequencing tasks.
B. Do not confuse an image representation with the geometric cause of the image.
C. The concept has an input, operation, output, and later use.
D. It connects to 00 Introduction to C++.

## Lecture 02 - Rendering Pipeline

Q5. Which statement best describes the core idea?

A. The lecture is only relevant for historical context.
B. The lecture can be ignored if the final image looks correct.
C. Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
D. The lecture is mainly a list of unrelated definitions.

Q6. Complete the chain:

`application data -> geometry stage -> primitive assembly -> ____ -> fragment operations -> framebuffer`

Q7. Match the term `application stage`.

A. A file organization convention only.
B. CPU-side preparation of models, scene data, interaction, animation, and rendering state.
C. Same meaning as `geometry stage`.
D. A final exam score calculation.

Q8. Select the dangerous misconception.

A. Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
B. The concept has an input, operation, output, and later use.
C. It connects to 01 Rendering Pipeline.
D. It can be practiced with matching and sequencing tasks.

## Lecture 03 - Geometric Transformations

Q9. Which statement best describes the core idea?

A. The lecture can be ignored if the final image looks correct.
B. Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
C. The lecture is mainly a list of unrelated definitions.
D. The lecture is only relevant for historical context.

Q10. Complete the chain:

`object/model coordinates -> ____ -> world coordinates -> view matrix -> camera/view coordinates`

Q11. Match the term `homogeneous coordinates`.

A. Coordinates with an additional component that make translation and projection expressible by matrices.
B. Same meaning as `translation`.
C. A final exam score calculation.
D. A file organization convention only.

Q12. Select the dangerous misconception.

A. The concept has an input, operation, output, and later use.
B. It connects to 03 Geometric Transformations.
C. It can be practiced with matching and sequencing tasks.
D. Do not multiply matrices without naming source space, target space, and order.

## Lecture 04 - Geometric Projection

Q13. Which statement best describes the core idea?

A. Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
B. The lecture is mainly a list of unrelated definitions.
C. The lecture is only relevant for historical context.
D. The lecture can be ignored if the final image looks correct.

Q14. Complete the chain:

`view-space position -> ____ -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`

Q15. Match the term `view volume`.

A. Same meaning as `orthographic projection`.
B. A final exam score calculation.
C. A file organization convention only.
D. The 3D region visible to the camera before mapping to the screen.

Q16. Select the dangerous misconception.

A. It connects to 04 Projections and Clipping.
B. It can be practiced with matching and sequencing tasks.
C. Do not confuse projection with viewport mapping; the perspective divide sits between them.
D. The concept has an input, operation, output, and later use.

## Lecture 05 - Clipping

Q17. Which statement best describes the core idea?

A. The lecture is mainly a list of unrelated definitions.
B. The lecture is only relevant for historical context.
C. The lecture can be ignored if the final image looks correct.
D. Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.

Q18. Complete the chain:

`primitive -> boundary tests -> inside/outside classification -> ____ -> clipped primitive`

Q19. Match the term `clipping`.

A. A final exam score calculation.
B. A file organization convention only.
C. Removing or cutting geometry outside a valid window, plane, or volume.
D. Same meaning as `Cohen-Sutherland`.

Q20. Select the dangerous misconception.

A. It can be practiced with matching and sequencing tasks.
B. Do not describe clipping as only deletion; crossing primitives can create new vertices.
C. The concept has an input, operation, output, and later use.
D. It connects to 04 Projections and Clipping.

## Lecture 06 - Rasterization

Q21. Which statement best describes the core idea?

A. The lecture is only relevant for historical context.
B. The lecture can be ignored if the final image looks correct.
C. Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
D. The lecture is mainly a list of unrelated definitions.

Q22. Complete the chain:

`projected primitive -> ____ -> fragment generation -> attribute interpolation -> fragment tests`

Q23. Match the term `scan conversion`.

A. A file organization convention only.
B. Determining which discrete samples are covered by an ideal geometric primitive.
C. Same meaning as `triangle coverage`.
D. A final exam score calculation.

Q24. Select the dangerous misconception.

A. Do not call every generated fragment a final pixel.
B. The concept has an input, operation, output, and later use.
C. It connects to 05 Rasterization.
D. It can be practiced with matching and sequencing tasks.

## Lecture 07 - Visibility Determination

Q25. Which statement best describes the core idea?

A. The lecture can be ignored if the final image looks correct.
B. Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
C. The lecture is mainly a list of unrelated definitions.
D. The lecture is only relevant for historical context.

Q26. Complete the chain:

`many projected or intersected candidates -> comparison rule -> ____ -> final image contribution`

Q27. Match the term `depth buffer`.

A. Per-pixel storage of depth values used to keep the nearest visible fragment.
B. Same meaning as `z-buffer algorithm`.
C. A final exam score calculation.
D. A file organization convention only.

Q28. Select the dangerous misconception.

A. The concept has an input, operation, output, and later use.
B. It connects to Rasterization and integrated rendering tasks.
C. It can be practiced with matching and sequencing tasks.
D. Do not confuse generating a fragment with proving that it is visible.

## Lecture 08 - Local Illumination

Q29. Which statement best describes the core idea?

A. Local illumination computes color from surface orientation, light direction, view direction, and material response.
B. The lecture is mainly a list of unrelated definitions.
C. The lecture is only relevant for historical context.
D. The lecture can be ignored if the final image looks correct.

Q30. Complete the chain:

`surface point + normal + light + view + material -> ____ -> shaded color`

Q31. Match the term `surface normal`.

A. Same meaning as `ambient term`.
B. A final exam score calculation.
C. A file organization convention only.
D. Vector describing surface orientation and controlling diffuse/specular response.

Q32. Select the dangerous misconception.

A. It connects to Rendering contest and shader-related tasks.
B. It can be practiced with matching and sequencing tasks.
C. Do not mix up normal, light direction, and view direction; each changes a different lighting term.
D. The concept has an input, operation, output, and later use.

## Lecture 09 - Texturing

Q33. Which statement best describes the core idea?

A. The lecture is mainly a list of unrelated definitions.
B. The lecture is only relevant for historical context.
C. The lecture can be ignored if the final image looks correct.
D. Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.

Q34. Complete the chain:

`fragment coordinates -> ____ -> sampler/filter/wrap state -> texel fetch -> shader meaning`

Q35. Match the term `texture`.

A. A final exam score calculation.
B. A file organization convention only.
C. Sampled data array used for color, normals, material data, depth, or other shader inputs.
D. Same meaning as `texel`.

Q36. Select the dangerous misconception.

A. It can be practiced with matching and sequencing tasks.
B. Do not reduce texturing to pasting an image onto geometry.
C. The concept has an input, operation, output, and later use.
D. It connects to Rendering contest and texture/shader tasks.

## Lecture 10 - Shadows

Q37. Which statement best describes the core idea?

A. The lecture is only relevant for historical context.
B. The lecture can be ignored if the final image looks correct.
C. Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
D. The lecture is mainly a list of unrelated definitions.

Q38. Complete the chain:

`light -> possible blocker -> ____ -> light-space visibility test -> lit or shadowed result`

Q39. Match the term `shadow`.

A. A file organization convention only.
B. Reduced direct illumination where an object blocks light from reaching a receiver.
C. Same meaning as `occluder`.
D. A final exam score calculation.

Q40. Select the dangerous misconception.

A. Do not explain a shadow only from the camera view; the key test is light-space visibility.
B. The concept has an input, operation, output, and later use.
C. It connects to Rendering contest and integrated lighting tasks.
D. It can be practiced with matching and sequencing tasks.

# Answer Key

Q1: D
Q2: sampling or rendering process. Full chain: `scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis`
Q3: C
Q4: B
Q5: C
Q6: rasterization. Full chain: `application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer`
Q7: B
Q8: A
Q9: B
Q10: model matrix. Full chain: `object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates`
Q11: A
Q12: D
Q13: A
Q14: projection matrix. Full chain: `view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates`
Q15: D
Q16: C
Q17: D
Q18: intersections. Full chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`
Q19: C
Q20: B
Q21: C
Q22: sample coverage. Full chain: `projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests`
Q23: B
Q24: A
Q25: B
Q26: visible surface or fragment. Full chain: `many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution`
Q27: A
Q28: D
Q29: A
Q30: lighting equation. Full chain: `surface point + normal + light + view + material -> lighting equation -> shaded color`
Q31: D
Q32: C
Q33: D
Q34: texture coordinates. Full chain: `fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning`
Q35: C
Q36: B
Q37: C
Q38: receiver point. Full chain: `light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result`
Q39: B
Q40: A
