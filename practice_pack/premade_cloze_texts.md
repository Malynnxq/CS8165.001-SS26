Premade Cloze Texts
===================
Use these if your tool supports blanks directly. Answers are in parentheses after each paragraph.

Rendering Pipeline
------------------
In ____1____ ____2____, a scene is ____3____ by ____4____ such as ____5____. The ____6____ ____7____ ____8____ vertices through several coordinate systems, assembles primitives, rasterizes them into fragments, executes fragment processing, applies tests such as the depth test, and finally writes surviving results into the framebuffer. A fragment is only a pixel candidate; it becomes visible only if it survives the later tests and operations.
Answers: 1=object-based, 2=rendering, 3=represented, 4=primitives, 5=triangles, 6=rendering, 7=pipeline, 8=transforms

OpenGL and Shaders
------------------
____1____ ____2____ is ____3____ by API calls, ____4____, ____5____, state, and ____6____ ____7____. A ____8____ shader usually transforms vertex positions and forwards attributes. A fragment shader computes per-fragment outputs such as color. The final image also depends on fixed-function operations such as depth testing, blending, and framebuffer configuration.
Answers: 1=OpenGL, 2=rendering, 3=controlled, 4=objects, 5=buffers, 6=programmable, 7=shaders, 8=vertex

Geometric Transformations
-------------------------
____1____ ____2____ ____3____, ____4____, and scale ____5____. ____6____ ____7____ make it ____8____ to represent translation, rotation, scaling, and projection in matrix form. Transformation order matters because matrix multiplication is not commutative. Points, directions, and normals must be handled carefully, especially when non-uniform scaling is used.
Answers: 1=Geometric, 2=transformations, 3=position, 4=orient, 5=models, 6=Homogeneous, 7=coordinates, 8=possible

Projection
----------
____1____ maps ____2____ ____3____ to a ____4____ image. ____5____ ____6____ ____7____ ____8____ lines and does not create perspective shortening. Perspective projection makes distant objects appear smaller and relies on homogeneous coordinates and the perspective divide. The camera model, view volume, projection matrix, and viewport mapping are all part of the path from world coordinates to screen coordinates.
Answers: 1=Projection, 2=three-dimensional, 3=geometry, 4=two-dimensional, 5=Orthographic, 6=projection, 7=preserves, 8=parallel

Clipping
--------
____1____ ____2____ or cuts parts of ____3____ ____4____ the ____5____ view or clip ____6____. ____7____ ____8____ happens before rasterization and may create new vertices where a primitive intersects a clipping boundary. Pixel-based clipping happens later and keeps only pixels or fragments inside a clip region. Clipping is not the same as culling, because culling rejects whole primitives based on tests such as orientation or volume.
Answers: 1=Clipping, 2=removes, 3=primitives, 4=outside, 5=relevant, 6=region, 7=Analytical, 8=clipping

Rasterization
-------------
____1____ ____2____ ____3____ ____4____ into ____5____ on a ____6____ grid. For ____7____, ____8____ requires deciding which sample positions are covered by the triangle. Attributes such as depth, color, normals, and texture coordinates are interpolated across the primitive, often using barycentric coordinates. Rasterization happens before final visibility decisions such as the depth test.
Answers: 1=Rasterization, 2=converts, 3=geometric, 4=primitives, 5=fragments, 6=raster, 7=triangles, 8=rasterization

Visibility
----------
____1____ ____2____ ____3____ which parts of a scene are ____4____ from the ____5____ ____6____. The ____7____ ____8____ stores depth values and compares incoming fragment depths against previously stored values. Back-face culling can reject surfaces pointing away from the camera for closed opaque objects. Depth precision, occlusion, and viewpoint dependence are common sources of mistakes.
Answers: 1=Visibility, 2=determination, 3=decides, 4=visible, 5=current, 6=camera, 7=z-buffer, 8=algorithm

Local Illumination
------------------
Local ____1____ ____2____ ____3____ ____4____ at a ____5____ point. ____6____ ____7____ ____8____ ambient, diffuse, and specular components. Diffuse reflection depends on the angle between the surface normal and the light direction. Specular reflection depends on the view direction and models highlights. Phong and Blinn-Phong are common local illumination models.
Answers: 1=illumination, 2=computes, 3=direct, 4=lighting, 5=surface, 6=Common, 7=models, 8=combine

Texturing
---------
A ____1____ is a ____2____ data field used ____3____ ____4____. ____5____ ____6____ map a ____7____ point to a ____8____ in texture space. A texel is a texture sample. Filtering determines how texture values are reconstructed between samples, and mipmapping uses prefiltered levels to reduce aliasing when textures are minified.
Answers: 1=texture, 2=sampled, 3=during, 4=rendering, 5=Texture, 6=coordinates, 7=surface, 8=lookup

Shadows
-------
____1____ ____2____ can be ____3____ as a ____4____ ____5____ from the light ____6____. In ____7____ ____8____, the scene is first rendered from the light to store a depth map. During normal rendering, a fragment is transformed into light space and compared against the stored light-space depth. Bias, resolution, and sampling influence shadow artifacts such as acne or detached shadows.
Answers: 1=Shadow, 2=computation, 3=treated, 4=visibility, 5=problem, 6=source, 7=shadow, 8=mapping
