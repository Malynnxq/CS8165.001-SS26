Cloze Variants round_01
=======================
Copy sections into a cloze generator. Same concepts, different wording.

Pipeline as a Factory
---------------------
Think of the rendering pipeline as a factory line. Vertex data enters first, shader stages transform and enrich it, primitives are formed, rasterization creates fragment candidates, tests decide which candidates survive, and the framebuffer stores the final output. The important distinction is that fragments are not automatically pixels.

Transform Chain
---------------
A model normally starts in its own object coordinates. Transformations place it into the world, then into the camera view, then through projection into clip space. After the perspective divide and viewport mapping, the geometry can be related to screen positions. The order of these transformations changes the result.

Lighting Terms
--------------
Local lighting is computed from direct interactions between light, material, normal, and view direction. Ambient light is a simple constant contribution, diffuse light depends on the normal-light angle, and specular light creates a view-dependent highlight.

Texture Sampling
----------------
Texture mapping uses coordinates on a surface to sample a data field. The result may be a color or another value used by the shader. Filtering reconstructs values between texels, while mipmaps reduce aliasing when many texels project to a small screen area.

Shadow Map Idea
---------------
Shadow mapping asks whether a camera fragment is visible from the light. A first pass stores light-space depths in a shadow map. A later pass transforms a fragment into light space and compares its depth with the stored depth.
