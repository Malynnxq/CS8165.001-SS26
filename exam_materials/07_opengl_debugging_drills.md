# 07 - OpenGL And Software Debugging Drills

Closed-format debugging practice. Choose the most likely conceptual area and the first checks.

## D1. Black screen after draw call

Choose the best diagnosis:

A. The issue is most likely only historical background.
B. The issue belongs to OpenGL state/binding.
C. The issue can be solved by memorizing the slide title.
D. The issue proves rasterization is not involved in rendering.

First checks:

- [ ] Write the checks here before looking at the answer.

## D2. Object appears but does not move

Choose the best diagnosis:

A. The issue is most likely only historical background.
B. The issue belongs to Transformations.
C. The issue can be solved by memorizing the slide title.
D. The issue proves rasterization is not involved in rendering.

First checks:

- [ ] Write the checks here before looking at the answer.

## D3. Triangle has wrong colors

Choose the best diagnosis:

A. The issue is most likely only historical background.
B. The issue belongs to Rasterization/shader interpolation.
C. The issue can be solved by memorizing the slide title.
D. The issue proves rasterization is not involved in rendering.

First checks:

- [ ] Write the checks here before looking at the answer.

## D4. Texture looks blocky or wrong

Choose the best diagnosis:

A. The issue is most likely only historical background.
B. The issue belongs to Texturing.
C. The issue can be solved by memorizing the slide title.
D. The issue proves rasterization is not involved in rendering.

First checks:

- [ ] Write the checks here before looking at the answer.

## D5. Near object is hidden behind far object

Choose the best diagnosis:

A. The issue is most likely only historical background.
B. The issue belongs to Visibility.
C. The issue can be solved by memorizing the slide title.
D. The issue proves rasterization is not involved in rendering.

First checks:

- [ ] Write the checks here before looking at the answer.

## D6. Lighting changes when camera moves incorrectly

Choose the best diagnosis:

A. The issue is most likely only historical background.
B. The issue belongs to Local illumination.
C. The issue can be solved by memorizing the slide title.
D. The issue proves rasterization is not involved in rendering.

First checks:

- [ ] Write the checks here before looking at the answer.

## D7. Shadow appears detached or inverted

Choose the best diagnosis:

A. The issue is most likely only historical background.
B. The issue belongs to Shadows.
C. The issue can be solved by memorizing the slide title.
D. The issue proves rasterization is not involved in rendering.

First checks:

- [ ] Write the checks here before looking at the answer.

# Answers

D1: B. Check context, bound VAO/VBO, shader program, viewport, clear color, framebuffer target.
D2: B. Check model/view/projection matrix update and multiplication order.
D3: B. Check vertex attributes, layout locations, interpolation, and fragment shader output.
D4: B. Check UV coordinates, texture binding, sampler filtering, wrapping, mipmap completeness, and shader sampler uniform.
D5: B. Check depth buffer creation, depth test enable, depth clear, and depth function.
D6: B. Check normal transformation, coordinate space consistency, light vector, and view vector.
D7: B. Check light-space transform, depth comparison, bias, and which object acts as occluder or receiver.
