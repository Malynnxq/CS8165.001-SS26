Cloze Variants round_03
=======================
Copy sections into a cloze generator. Same concepts, different wording.

Triangle Work
-------------
A triangle becomes visible through several steps. Its vertices are transformed, the primitive is assembled and clipped if needed, rasterization finds covered sample positions, attributes are interpolated, and depth testing decides whether generated fragments remain visible.

Coordinate Spaces
-----------------
Object, world, view, clip, normalized device, and screen coordinates describe different stages of the same geometry. Confusing these spaces often leads to wrong matrices, disappearing objects, or lighting calculations in incompatible coordinate systems.

Illumination Pitfalls
---------------------
Lighting calculations depend on normalized vectors in a consistent coordinate system. The surface normal, light direction, view direction, and material parameters influence the final result. Diffuse and specular terms should not be treated as interchangeable.

Aliasing and Mipmaps
--------------------
Aliasing appears when high-frequency texture information is sampled too sparsely. Mipmaps store prefiltered texture levels, allowing the renderer to sample a level closer to the projected screen footprint.

Shadow Artifacts
----------------
Shadow maps are practical but imperfect. Too little bias can cause self-shadowing artifacts, while too much bias can detach shadows from casters. Resolution and sampling also affect the final appearance.
