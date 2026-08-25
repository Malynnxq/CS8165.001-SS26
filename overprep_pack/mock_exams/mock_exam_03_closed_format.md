Closed-Format Mock Exam 3
=========================
No vague open answers. Use only selecting, matching, ordering, filling blanks, and labeling checklists.

Section A - Multiple Choice
---------------------------
1. A fragment shader usually computes:
   A. Per-fragment outputs
   B. CPU memory layout
   C. CMake settings
   D. Mesh topology only
   Answer: A
2. Back-face culling is usually valid for:
   A. Closed opaque objects
   B. Transparent all-sided surfaces
   C. Audio buffers
   D. Texture files only
   Answer: A
3. Diffuse lighting depends most directly on:
   A. Normal and light direction
   B. Framebuffer size only
   C. Filename extension
   D. Mouse input
   Answer: A
4. Specular lighting is:
   A. View-dependent
   B. Always constant
   C. Only a clipping operation
   D. The same as ambient
   Answer: A
5. Texture coordinates are used to:
   A. Index/sample texture data
   B. Choose the CPU compiler
   C. Replace the depth buffer
   D. Disable projection
   Answer: A
6. Clipping happens to:
   A. Geometry or fragments outside a region
   B. Only shader source comments
   C. Only Git files
   D. Only final exam answers
   Answer: A
7. Rasterization converts:
   A. Primitives to fragments
   B. Textures to compilers
   C. Pixels to vertices
   D. Light to camera
   Answer: A

Section B - Fill In
-------------------
1. Perspective projection relies on dividing by the homogeneous coordinate ____.
   Answers: w
2. ____ clipping may cut primitives and create new vertices at boundaries.
   Answers: Analytical
3. The ____ buffer stores depth values for hidden surface removal.
   Answers: z
4. A texture sample is called a ____.
   Answers: texel
5. ____ mapping renders depth from the light source first.
   Answers: Shadow
6. The diffuse term often uses max(0, dot(n, l)) where n is the surface ____.
   Answers: normal

Section C - Matching
--------------------
1. Rasterization
2. Barycentric coordinates
3. Z-buffer
4. Back-face culling
5. Ambient term
6. Diffuse term
7. Specular term
8. Texture
A. Converting primitives into fragments.
B. Triangle-relative weights for interpolation.
C. Depth-based hidden surface removal buffer.
D. Rejecting surfaces facing away from camera.
E. Constant approximation of indirect/background light.
F. Normal-light dependent matte reflection.
G. View-dependent highlight.
H. Sampled data field used during rendering.
Answer key: 1-A, 2-B, 3-C, 4-D, 5-E, 6-F, 7-G, 8-H

Section D - Sequencing
----------------------
Task: Put these steps in order: Shadow mapping
- Apply lit/shadowed shading
- Compare depth
- Transform fragment to light space
- Render from camera
- Store depth map
- Render from light
Answer: Render from light -> Store depth map -> Render from camera -> Transform fragment to light space -> Compare depth -> Apply lit/shadowed shading

Section E - Diagram Label Checklist
-----------------------------------
Diagram: Triangle rasterization
Your drawing is complete only if it includes:
- [ ] Vertices
- [ ] Edges
- [ ] Sample points
- [ ] Covered fragments
- [ ] Interpolated attributes
- [ ] Depth values
