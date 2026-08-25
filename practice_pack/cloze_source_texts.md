Cloze Source Texts
==================
Copy one section into your cloze/Lueckentext generator. These texts are coherent and intentionally redundant enough for active recall.

Rendering Pipeline
------------------
In object-based rendering, a scene is represented by primitives such as triangles. The rendering pipeline transforms vertices through several coordinate systems, assembles primitives, rasterizes them into fragments, executes fragment processing, applies tests such as the depth test, and finally writes surviving results into the framebuffer. A fragment is only a pixel candidate; it becomes visible only if it survives the later tests and operations.

OpenGL and Shaders
------------------
OpenGL rendering is controlled by API calls, objects, buffers, state, and programmable shaders. A vertex shader usually transforms vertex positions and forwards attributes. A fragment shader computes per-fragment outputs such as color. The final image also depends on fixed-function operations such as depth testing, blending, and framebuffer configuration.

Geometric Transformations
-------------------------
Geometric transformations position, orient, and scale models. Homogeneous coordinates make it possible to represent translation, rotation, scaling, and projection in matrix form. Transformation order matters because matrix multiplication is not commutative. Points, directions, and normals must be handled carefully, especially when non-uniform scaling is used.

Projection
----------
Projection maps three-dimensional geometry to a two-dimensional image. Orthographic projection preserves parallel lines and does not create perspective shortening. Perspective projection makes distant objects appear smaller and relies on homogeneous coordinates and the perspective divide. The camera model, view volume, projection matrix, and viewport mapping are all part of the path from world coordinates to screen coordinates.

Clipping
--------
Clipping removes or cuts parts of primitives outside the relevant view or clip region. Analytical clipping happens before rasterization and may create new vertices where a primitive intersects a clipping boundary. Pixel-based clipping happens later and keeps only pixels or fragments inside a clip region. Clipping is not the same as culling, because culling rejects whole primitives based on tests such as orientation or volume.

Rasterization
-------------
Rasterization converts geometric primitives into fragments on a raster grid. For triangles, rasterization requires deciding which sample positions are covered by the triangle. Attributes such as depth, color, normals, and texture coordinates are interpolated across the primitive, often using barycentric coordinates. Rasterization happens before final visibility decisions such as the depth test.

Visibility
----------
Visibility determination decides which parts of a scene are visible from the current camera. The z-buffer algorithm stores depth values and compares incoming fragment depths against previously stored values. Back-face culling can reject surfaces pointing away from the camera for closed opaque objects. Depth precision, occlusion, and viewpoint dependence are common sources of mistakes.

Local Illumination
------------------
Local illumination computes direct lighting at a surface point. Common models combine ambient, diffuse, and specular components. Diffuse reflection depends on the angle between the surface normal and the light direction. Specular reflection depends on the view direction and models highlights. Phong and Blinn-Phong are common local illumination models.

Texturing
---------
A texture is a sampled data field used during rendering. Texture coordinates map a surface point to a lookup in texture space. A texel is a texture sample. Filtering determines how texture values are reconstructed between samples, and mipmapping uses prefiltered levels to reduce aliasing when textures are minified.

Shadows
-------
Shadow computation can be treated as a visibility problem from the light source. In shadow mapping, the scene is first rendered from the light to store a depth map. During normal rendering, a fragment is transformed into light space and compared against the stored light-space depth. Bias, resolution, and sampling influence shadow artifacts such as acne or detached shadows.
