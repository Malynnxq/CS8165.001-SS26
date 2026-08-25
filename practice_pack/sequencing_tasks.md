Sequencing Tasks
================
Shuffle the steps and restore the correct order.

Rendering pipeline order
------------------------
1. Vertex input
2. Vertex shader
3. Primitive assembly
4. Rasterization
5. Fragment shader
6. Depth/stencil/blending tests
7. Framebuffer write

Shadow mapping high-level order
-------------------------------
1. Render scene from light
2. Store light-space depth map
3. Render scene from camera
4. Transform fragment into light space
5. Compare fragment depth with shadow map
6. Shade lit or shadowed result

Texture lookup order
--------------------
1. Have/interpolate texture coordinates
2. Select texture object/sampler
3. Choose mip level/filter
4. Sample texel values
5. Use sampled value in shading

Projection path
---------------
1. Model coordinates
2. World coordinates
3. View/camera coordinates
4. Clip coordinates
5. Normalized device coordinates
6. Viewport/screen coordinates
