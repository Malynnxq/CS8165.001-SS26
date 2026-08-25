Closed-Format Mock Exam 2
=========================
No vague open answers. Use only selecting, matching, ordering, filling blanks, and labeling checklists.

Section A - Multiple Choice
---------------------------
1. The perspective divide divides by:
   A. x
   B. y
   C. z
   D. w
   Answer: D
2. Mipmaps mainly reduce:
   A. Geometry count
   B. Texture aliasing
   C. Specular highlights
   D. Camera movement
   Answer: B
3. A shadow map stores:
   A. Light-space depth
   B. Final colors
   C. Normals
   D. Texture coordinates
   Answer: A
4. Matrix multiplication order matters because:
   A. Matrices are always diagonal
   B. It is generally not commutative
   C. Vectors have no direction
   D. OpenGL disables order
   Answer: B
5. A vertex shader usually processes:
   A. Per-vertex data
   B. Final framebuffer pixels
   C. Only texture files
   D. Only UI events
   Answer: A
6. A fragment shader usually computes:
   A. Per-fragment outputs
   B. CPU memory layout
   C. CMake settings
   D. Mesh topology only
   Answer: A
7. Back-face culling is usually valid for:
   A. Closed opaque objects
   B. Transparent all-sided surfaces
   C. Audio buffers
   D. Texture files only
   Answer: A
8. Diffuse lighting depends most directly on:
   A. Normal and light direction
   B. Framebuffer size only
   C. Filename extension
   D. Mouse input
   Answer: A
9. Specular lighting is:
   A. View-dependent
   B. Always constant
   C. Only a clipping operation
   D. The same as ambient
   Answer: A
10. Texture coordinates are used to:
   A. Index/sample texture data
   B. Choose the CPU compiler
   C. Replace the depth buffer
   D. Disable projection
   Answer: A

Section B - Fill In
-------------------
1. In homogeneous coordinates, translation and projection can be represented using ____ multiplication.
   Answers: matrix
2. Perspective projection relies on dividing by the homogeneous coordinate ____.
   Answers: w
3. ____ clipping may cut primitives and create new vertices at boundaries.
   Answers: Analytical
4. The ____ buffer stores depth values for hidden surface removal.
   Answers: z
5. A texture sample is called a ____.
   Answers: texel
6. ____ mapping renders depth from the light source first.
   Answers: Shadow

Section C - Matching
--------------------
1. Affine transformation
2. Projection matrix
3. Perspective divide
4. Clipping
5. Culling
6. Rasterization
7. Barycentric coordinates
8. Z-buffer
A. Line-preserving transform such as translation or rotation.
B. Matrix mapping view space toward clip/projection space.
C. Division by w after projection.
D. Cutting/removing geometry outside a region.
E. Rejecting whole objects or primitives based on a test.
F. Converting primitives into fragments.
G. Triangle-relative weights for interpolation.
H. Depth-based hidden surface removal buffer.
Answer key: 1-A, 2-B, 3-C, 4-D, 5-E, 6-F, 7-G, 8-H

Section D - Sequencing
----------------------
Task: Put these steps in order: Coordinate path
- Viewport coordinates
- NDC
- Clip coordinates
- View coordinates
- World coordinates
- Object coordinates
Answer: Object coordinates -> World coordinates -> View coordinates -> Clip coordinates -> NDC -> Viewport coordinates

Section E - Diagram Label Checklist
-----------------------------------
Diagram: Projection pipeline
Your drawing is complete only if it includes:
- [ ] Object
- [ ] World
- [ ] View
- [ ] Clip
- [ ] NDC
- [ ] Viewport/screen
