Cloze Variants round_02
=======================
Copy sections into a cloze generator. Same concepts, different wording.

Fragments and Tests
-------------------
Rasterization does not directly produce final image pixels. It produces fragments, which still have to pass tests such as depth and stencil operations. Only surviving fragments can update framebuffer attachments such as the color or depth buffer.

Projection Difference
---------------------
Orthographic projection keeps parallel lines parallel and does not shrink far objects. Perspective projection creates depth-dependent size changes and requires homogeneous coordinates. The perspective divide is the step that makes the projected coordinates usable for later viewport mapping.

Clipping vs Culling
-------------------
Clipping and culling both reduce later work, but they are not the same. Clipping cuts geometry against a boundary and can create new vertices. Culling rejects complete primitives or objects, for example because a face points away from the camera.

Visibility
----------
Visibility determination decides which surfaces are seen from a viewpoint. In z-buffering, each incoming fragment depth is compared to a stored depth value. The fragment survives only if it satisfies the selected depth comparison rule.

OpenGL Debugging
----------------
A black or broken render can come from many pipeline stages. Common causes include missing uniforms, wrong shader outputs, disabled depth testing, bad texture coordinates, incorrect projection matrices, or normals in the wrong coordinate system.
