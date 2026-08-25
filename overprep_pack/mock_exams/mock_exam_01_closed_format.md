Closed-Format Mock Exam 1
=========================
No vague open answers. Use only selecting, matching, ordering, filling blanks, and labeling checklists.

Section A - Multiple Choice
---------------------------
1. A fragment is best described as:
   A. A final visible pixel
   B. A pixel candidate before final tests
   C. A triangle vertex
   D. A texture sample
   Answer: B
2. The z-buffer primarily stores:
   A. Color
   B. Depth
   C. Normals
   D. Texture coordinates
   Answer: B
3. Which operation can create new vertices?
   A. Analytical clipping
   B. Back-face culling
   C. Depth testing
   D. Framebuffer clearing
   Answer: A
4. The perspective divide divides by:
   A. x
   B. y
   C. z
   D. w
   Answer: D
5. Mipmaps mainly reduce:
   A. Geometry count
   B. Texture aliasing
   C. Specular highlights
   D. Camera movement
   Answer: B
6. A shadow map stores:
   A. Light-space depth
   B. Final colors
   C. Normals
   D. Texture coordinates
   Answer: A
7. Matrix multiplication order matters because:
   A. Matrices are always diagonal
   B. It is generally not commutative
   C. Vectors have no direction
   D. OpenGL disables order
   Answer: B
8. A vertex shader usually processes:
   A. Per-vertex data
   B. Final framebuffer pixels
   C. Only texture files
   D. Only UI events
   Answer: A
9. A fragment shader usually computes:
   A. Per-fragment outputs
   B. CPU memory layout
   C. CMake settings
   D. Mesh topology only
   Answer: A
10. Back-face culling is usually valid for:
   A. Closed opaque objects
   B. Transparent all-sided surfaces
   C. Audio buffers
   D. Texture files only
   Answer: A

Section B - Fill In
-------------------
1. The pipeline transforms vertices, assembles primitives, rasterizes them into ____ and writes surviving results to the ____.
   Answers: fragments, framebuffer
2. In homogeneous coordinates, translation and projection can be represented using ____ multiplication.
   Answers: matrix
3. Perspective projection relies on dividing by the homogeneous coordinate ____.
   Answers: w
4. ____ clipping may cut primitives and create new vertices at boundaries.
   Answers: Analytical
5. The ____ buffer stores depth values for hidden surface removal.
   Answers: z
6. A texture sample is called a ____.
   Answers: texel

Section C - Matching
--------------------
1. Vertex
2. Primitive
3. Fragment
4. Framebuffer
5. Homogeneous coordinates
6. Affine transformation
7. Projection matrix
8. Perspective divide
A. Point with attributes such as position or normal.
B. Geometric unit assembled from vertices.
C. Pixel candidate before final tests.
D. Storage for final render buffers.
E. Coordinate representation with w component.
F. Line-preserving transform such as translation or rotation.
G. Matrix mapping view space toward clip/projection space.
H. Division by w after projection.
Answer key: 1-A, 2-B, 3-C, 4-D, 5-E, 6-F, 7-G, 8-H

Section D - Sequencing
----------------------
Task: Put these steps in order: Pipeline
- Framebuffer write
- Depth/blend tests
- Fragment shader
- Rasterization
- Primitive assembly
- Vertex shader
- Vertex input
Answer: Vertex input -> Vertex shader -> Primitive assembly -> Rasterization -> Fragment shader -> Depth/blend tests -> Framebuffer write

Section E - Diagram Label Checklist
-----------------------------------
Diagram: Rendering pipeline
Your drawing is complete only if it includes:
- [ ] Vertex input
- [ ] Vertex shader
- [ ] Primitive assembly
- [ ] Rasterization
- [ ] Fragment shader
- [ ] Tests/operations
- [ ] Framebuffer
