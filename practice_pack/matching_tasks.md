Matching Tasks
==============
Use `matching_pairs.tsv` for generators. For manual practice: cover the right column and explain each term.

Chapter 02
----------
Terms:
- Vertex
- Primitive
- Fragment
- Framebuffer
- Vertex shader
- Fragment shader
Definitions:
- A point with attributes such as position, normal, color, or texture coordinates.
- A geometric unit assembled from vertices, commonly a triangle.
- A pixel candidate produced by rasterization before final tests.
- Storage for rendered output and related buffers such as color and depth.
- Programmable stage that processes vertices and often applies transformations.
- Programmable stage that computes per-fragment outputs such as color.

Chapter 03
----------
Terms:
- Homogeneous coordinates
- Affine transformation
Definitions:
- Coordinate representation enabling affine transformations and perspective projection.
- Line-preserving transformation such as translation, rotation, scaling, or shear.

Chapter 04
----------
Terms:
- View transformation
- Projection matrix
- Perspective divide
Definitions:
- Transforms world-space coordinates into camera/view space.
- Maps view-space geometry into clip or projection space.
- Division by the homogeneous coordinate that creates perspective effects.

Chapter 05
----------
Terms:
- Clipping
- Culling
Definitions:
- Cutting or removing primitive parts outside a clip region.
- Rejecting whole primitives or objects based on tests such as orientation.

Chapter 06
----------
Terms:
- Rasterization
- Barycentric coordinates
Definitions:
- Conversion of primitives into fragments on a raster grid.
- Weights relative to triangle vertices used for interpolation.

Chapter 07
----------
Terms:
- Z-buffer
- Back-face culling
Definitions:
- Depth buffer method for hidden surface removal.
- Rejecting surfaces facing away from the camera.

Chapter 08
----------
Terms:
- Ambient term
- Diffuse term
- Specular term
Definitions:
- Simple constant approximation of background light.
- View-independent reflection based on normal and light direction.
- View-dependent highlight component.

Chapter 09
----------
Terms:
- Texture
- Texel
- Mipmapping
Definitions:
- Sampled data field used during rendering.
- A single sample in texture space.
- Prefiltered texture levels used to reduce aliasing.

Chapter 10
----------
Terms:
- Shadow map
- Shadow bias
Definitions:
- Depth map rendered from the light source.
- Offset used to reduce self-shadowing in shadow mapping.
