# 06 - Diagram Label Tasks

Use these as drawing or labeling tasks. They avoid vague essays: label the objects and arrows.

## Lecture 01 - Introduction

Draw boxes for:

- scene or image description
- representation choice
- sampling or rendering process
- visible image
- interaction or analysis

Label arrows with:

- what changes
- what data is preserved
- what can go wrong

Trap label that must appear somewhere: Do not confuse an image representation with the geometric cause of the image.

## Lecture 02 - Rendering Pipeline

Draw boxes for:

- application data
- geometry stage
- primitive assembly
- rasterization
- fragment operations
- framebuffer

Label arrows with:

- what changes
- what data is preserved
- what can go wrong

Trap label that must appear somewhere: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.

## Lecture 03 - Geometric Transformations

Draw boxes for:

- object/model coordinates
- model matrix
- world coordinates
- view matrix
- camera/view coordinates

Label arrows with:

- what changes
- what data is preserved
- what can go wrong

Trap label that must appear somewhere: Do not multiply matrices without naming source space, target space, and order.

## Lecture 04 - Geometric Projection

Draw boxes for:

- view-space position
- projection matrix
- clip coordinates
- perspective divide
- NDC
- viewport coordinates

Label arrows with:

- what changes
- what data is preserved
- what can go wrong

Trap label that must appear somewhere: Do not confuse projection with viewport mapping; the perspective divide sits between them.

## Lecture 05 - Clipping

Draw boxes for:

- primitive
- boundary tests
- inside/outside classification
- intersections
- clipped primitive

Label arrows with:

- what changes
- what data is preserved
- what can go wrong

Trap label that must appear somewhere: Do not describe clipping as only deletion; crossing primitives can create new vertices.

## Lecture 06 - Rasterization

Draw boxes for:

- projected primitive
- sample coverage
- fragment generation
- attribute interpolation
- fragment tests

Label arrows with:

- what changes
- what data is preserved
- what can go wrong

Trap label that must appear somewhere: Do not call every generated fragment a final pixel.

## Lecture 07 - Visibility Determination

Draw boxes for:

- many projected or intersected candidates
- comparison rule
- visible surface or fragment
- final image contribution

Label arrows with:

- what changes
- what data is preserved
- what can go wrong

Trap label that must appear somewhere: Do not confuse generating a fragment with proving that it is visible.

## Lecture 08 - Local Illumination

Draw boxes for:

- surface point + normal + light + view + material
- lighting equation
- shaded color

Label arrows with:

- what changes
- what data is preserved
- what can go wrong

Trap label that must appear somewhere: Do not mix up normal, light direction, and view direction; each changes a different lighting term.

## Lecture 09 - Texturing

Draw boxes for:

- fragment coordinates
- texture coordinates
- sampler/filter/wrap state
- texel fetch
- shader meaning

Label arrows with:

- what changes
- what data is preserved
- what can go wrong

Trap label that must appear somewhere: Do not reduce texturing to pasting an image onto geometry.

## Lecture 10 - Shadows

Draw boxes for:

- light
- possible blocker
- receiver point
- light-space visibility test
- lit or shadowed result

Label arrows with:

- what changes
- what data is preserved
- what can go wrong

Trap label that must appear somewhere: Do not explain a shadow only from the camera view; the key test is light-space visibility.
