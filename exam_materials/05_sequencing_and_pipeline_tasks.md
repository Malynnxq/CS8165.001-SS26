# 05 - Sequencing And Pipeline Tasks

Put the listed items in the correct conceptual order. Answers are at the end.

## S1 - Lecture 01 Introduction

Scrambled steps:

- representation choice
- visible image
- scene or image description
- sampling or rendering process
- interaction or analysis

Correct order:

- [ ] Fill this in without notes.

## S2 - Lecture 02 Rendering Pipeline

Scrambled steps:

- geometry stage
- rasterization
- framebuffer
- application data
- primitive assembly
- fragment operations

Correct order:

- [ ] Fill this in without notes.

## S3 - Lecture 03 Geometric Transformations

Scrambled steps:

- model matrix
- view matrix
- object/model coordinates
- world coordinates
- camera/view coordinates

Correct order:

- [ ] Fill this in without notes.

## S4 - Lecture 04 Geometric Projection

Scrambled steps:

- projection matrix
- perspective divide
- viewport coordinates
- view-space position
- clip coordinates
- NDC

Correct order:

- [ ] Fill this in without notes.

## S5 - Lecture 05 Clipping

Scrambled steps:

- boundary tests
- intersections
- primitive
- inside/outside classification
- clipped primitive

Correct order:

- [ ] Fill this in without notes.

## S6 - Lecture 06 Rasterization

Scrambled steps:

- sample coverage
- attribute interpolation
- projected primitive
- fragment generation
- fragment tests

Correct order:

- [ ] Fill this in without notes.

## S7 - Lecture 07 Visibility Determination

Scrambled steps:

- comparison rule
- final image contribution
- many projected or intersected candidates
- visible surface or fragment

Correct order:

- [ ] Fill this in without notes.

## S8 - Lecture 08 Local Illumination

Scrambled steps:

- lighting equation
- surface point + normal + light + view + material
- shaded color

Correct order:

- [ ] Fill this in without notes.

## S9 - Lecture 09 Texturing

Scrambled steps:

- texture coordinates
- texel fetch
- fragment coordinates
- sampler/filter/wrap state
- shader meaning

Correct order:

- [ ] Fill this in without notes.

## S10 - Lecture 10 Shadows

Scrambled steps:

- possible blocker
- light-space visibility test
- light
- receiver point
- lit or shadowed result

Correct order:

- [ ] Fill this in without notes.

# Answer Key

S1: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis
S2: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer
S3: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates
S4: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates
S5: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive
S6: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests
S7: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution
S8: surface point + normal + light + view + material -> lighting equation -> shaded color
S9: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning
S10: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result
