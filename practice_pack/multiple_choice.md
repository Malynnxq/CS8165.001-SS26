Multiple Choice Practice
========================

1. What is a fragment?
   A. A final visible pixel
   B. A pixel candidate before final tests
   C. A vertex attribute
   D. A framebuffer attachment
   Correct: B
   Explanation: A fragment may be discarded by depth or other tests.

2. Why does transformation order matter?
   A. Matrices are commutative
   B. Matrix multiplication is generally not commutative
   C. Only translations matter
   D. OpenGL ignores order
   Correct: B
   Explanation: Changing order changes the resulting transform.

3. What does clipping do?
   A. Removes invisible light
   B. Cuts/removes geometry outside a clip region
   C. Computes shading
   D. Creates texture coordinates
   Correct: B
   Explanation: Clipping is a geometric visibility step before or around rasterization.

4. What does the z-buffer store?
   A. Colors
   B. Normals
   C. Depth values
   D. Texture coordinates
   Correct: C
   Explanation: Depth values are compared for visibility.

5. What is a mipmap used for?
   A. Perspective projection
   B. Reducing texture aliasing during minification
   C. Creating vertices
   D. Computing normals
   Correct: B
   Explanation: Mipmaps provide prefiltered lower-resolution texture levels.

6. What is shadow mapping based on?
   A. Color comparison
   B. Visibility from the light source
   C. Only ambient light
   D. Back-face culling only
   Correct: B
   Explanation: A depth map from the light is compared during camera rendering.
