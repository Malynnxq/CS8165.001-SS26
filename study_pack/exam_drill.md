Exam Drill - Fragenkatalog
==========================
Antworten sollten immer mit Kursbegriffen und wenn moeglich Seitenmarken aus den Chunks belegt werden. Die Antwortanker sind keine vollstaendigen offiziellen Musterloesungen; sie nennen, was in einer guten Antwort vorkommen muss.

Kapitel 01: Introduction
------------------------
1. Definiere die wichtigsten Begriffe aus Introduction.
   Antwortanker: course goals, graphics applications, rendering overview, models, visibility. Danach Begriffe mit Seitenmarken im Kapitelchunk belegen.
2. Erklaere, welche Rolle Introduction im Kurs oder in der Rendering Pipeline spielt.
   Antwortanker: Explain what interactive computer graphics studies and why real-time constraints matter.
3. Beschreibe einen typischen Algorithmus oder Ablauf aus Introduction.
   Antwortanker: Distinguish modeling, rendering, visibility, illumination, and interaction at a high level.
4. Nenne typische Fehler, Artefakte oder Missverstaendnisse bei Introduction.
   Antwortanker: Do not treat the introduction as only organizational; it frames the whole pipeline.; Separate scene representation from image generation.; Remember that interactivity implies performance constraints, not just image quality.
5. Erstelle eine kleine Skizzenbeschreibung zu Introduction und erklaere sie.
   Antwortanker: Diagramm/Skizze aus dem passenden Kapitelchunk oder Visual Review Guide waehlen, dann Achsen/Objekte/Pipeline-Schritte erklaeren.

Kapitel 02: Rendering Pipeline
------------------------------
1. Definiere die wichtigsten Begriffe aus Rendering Pipeline.
   Antwortanker: object-based rendering, OpenGL, vertices, primitives, fragments. Danach Begriffe mit Seitenmarken im Kapitelchunk belegen.
2. Erklaere, welche Rolle Rendering Pipeline im Kurs oder in der Rendering Pipeline spielt.
   Antwortanker: Reproduce the pipeline order from vertices to pixels.
3. Beschreibe einen typischen Algorithmus oder Ablauf aus Rendering Pipeline.
   Antwortanker: Explain vertex processing, primitive assembly, rasterization, fragment processing, tests, and framebuffer operations.
4. Nenne typische Fehler, Artefakte oder Missverstaendnisse bei Rendering Pipeline.
   Antwortanker: Fragments are pixel candidates, not guaranteed final pixels.; Rasterization and fragment shading are separate stages.; OpenGL state influences rendering; do not describe it as purely functional code.
5. Erstelle eine kleine Skizzenbeschreibung zu Rendering Pipeline und erklaere sie.
   Antwortanker: Diagramm/Skizze aus dem passenden Kapitelchunk oder Visual Review Guide waehlen, dann Achsen/Objekte/Pipeline-Schritte erklaeren.

Kapitel 03: Geometric Transformations
-------------------------------------
1. Definiere die wichtigsten Begriffe aus Geometric Transformations.
   Antwortanker: matrices, vectors, affine transformations, composition, coordinate systems. Danach Begriffe mit Seitenmarken im Kapitelchunk belegen.
2. Erklaere, welche Rolle Geometric Transformations im Kurs oder in der Rendering Pipeline spielt.
   Antwortanker: Use homogeneous coordinates to represent translation, rotation, scaling, and affine transforms.
3. Beschreibe einen typischen Algorithmus oder Ablauf aus Geometric Transformations.
   Antwortanker: Explain why transformation order matters.
4. Nenne typische Fehler, Artefakte oder Missverstaendnisse bei Geometric Transformations.
   Antwortanker: Matrix multiplication is not commutative.; Normals usually require special handling under non-uniform scaling.; Changing coordinates and moving objects can look algebraically similar but mean different things.
5. Erstelle eine kleine Skizzenbeschreibung zu Geometric Transformations und erklaere sie.
   Antwortanker: Diagramm/Skizze aus dem passenden Kapitelchunk oder Visual Review Guide waehlen, dann Achsen/Objekte/Pipeline-Schritte erklaeren.

Kapitel 04: Geometric Projection
--------------------------------
1. Definiere die wichtigsten Begriffe aus Geometric Projection.
   Antwortanker: linear perspective, planar projections, camera, view volume, orthographic projection. Danach Begriffe mit Seitenmarken im Kapitelchunk belegen.
2. Erklaere, welche Rolle Geometric Projection im Kurs oder in der Rendering Pipeline spielt.
   Antwortanker: Explain perspective shortening and loss of depth in projection.
3. Beschreibe einen typischen Algorithmus oder Ablauf aus Geometric Projection.
   Antwortanker: Distinguish orthographic and perspective projection qualitatively and mathematically.
4. Nenne typische Fehler, Artefakte oder Missverstaendnisse bei Geometric Projection.
   Antwortanker: Do not confuse view transformation with projection transformation.; Perspective projection is not just scaling; the homogeneous divide is essential.; Depth is transformed for later visibility tests, even though the image is 2D.
5. Erstelle eine kleine Skizzenbeschreibung zu Geometric Projection und erklaere sie.
   Antwortanker: Diagramm/Skizze aus dem passenden Kapitelchunk oder Visual Review Guide waehlen, dann Achsen/Objekte/Pipeline-Schritte erklaeren.

Kapitel 05: Clipping
--------------------
1. Definiere die wichtigsten Begriffe aus Clipping.
   Antwortanker: analytical clipping, pixel-based clipping, canonical view volume, visible parts, optimized geometry processing. Danach Begriffe mit Seitenmarken im Kapitelchunk belegen.
2. Erklaere, welche Rolle Clipping im Kurs oder in der Rendering Pipeline spielt.
   Antwortanker: Explain why clipping is needed before costly later stages.
3. Beschreibe einen typischen Algorithmus oder Ablauf aus Clipping.
   Antwortanker: Distinguish analytical clipping from pixel-based clipping.
4. Nenne typische Fehler, Artefakte oder Missverstaendnisse bei Clipping.
   Antwortanker: Clipping is not the same as culling.; Clipping can create new vertices where primitives intersect clipping boundaries.; Pixel-based clipping happens later and has different cost behavior.
5. Erstelle eine kleine Skizzenbeschreibung zu Clipping und erklaere sie.
   Antwortanker: Diagramm/Skizze aus dem passenden Kapitelchunk oder Visual Review Guide waehlen, dann Achsen/Objekte/Pipeline-Schritte erklaeren.

Kapitel 06: Rasterization
-------------------------
1. Definiere die wichtigsten Begriffe aus Rasterization.
   Antwortanker: raster images, pixels, triangles, fragments, coverage. Danach Begriffe mit Seitenmarken im Kapitelchunk belegen.
2. Erklaere, welche Rolle Rasterization im Kurs oder in der Rendering Pipeline spielt.
   Antwortanker: Explain how continuous primitives become discrete fragments.
3. Beschreibe einen typischen Algorithmus oder Ablauf aus Rasterization.
   Antwortanker: Describe triangle rasterization and inside/outside tests.
4. Nenne typische Fehler, Artefakte oder Missverstaendnisse bei Rasterization.
   Antwortanker: A pixel is not a little square; be precise about samples and raster representation.; Attribute interpolation must be distinguished from geometric transformation.; Rasterization produces fragments before final visibility tests.
5. Erstelle eine kleine Skizzenbeschreibung zu Rasterization und erklaere sie.
   Antwortanker: Diagramm/Skizze aus dem passenden Kapitelchunk oder Visual Review Guide waehlen, dann Achsen/Objekte/Pipeline-Schritte erklaeren.

Kapitel 07: Visibility Determination
------------------------------------
1. Definiere die wichtigsten Begriffe aus Visibility Determination.
   Antwortanker: visible surface determination, hidden surface removal, z-buffer, depth, culling. Danach Begriffe mit Seitenmarken im Kapitelchunk belegen.
2. Erklaere, welche Rolle Visibility Determination im Kurs oder in der Rendering Pipeline spielt.
   Antwortanker: Define visibility determination / hidden surface removal.
3. Beschreibe einen typischen Algorithmus oder Ablauf aus Visibility Determination.
   Antwortanker: Explain z-buffering and depth comparison.
4. Nenne typische Fehler, Artefakte oder Missverstaendnisse bei Visibility Determination.
   Antwortanker: Culling removes geometry based on orientation or volume tests; depth testing resolves occlusion per fragment.; Depth precision can produce artifacts.; Visibility is tied to the current camera/viewpoint.
5. Erstelle eine kleine Skizzenbeschreibung zu Visibility Determination und erklaere sie.
   Antwortanker: Diagramm/Skizze aus dem passenden Kapitelchunk oder Visual Review Guide waehlen, dann Achsen/Objekte/Pipeline-Schritte erklaeren.

Kapitel 08: Local Illumination
------------------------------
1. Definiere die wichtigsten Begriffe aus Local Illumination.
   Antwortanker: physics of light, light sources, material models, ambient, diffuse. Danach Begriffe mit Seitenmarken im Kapitelchunk belegen.
2. Erklaere, welche Rolle Local Illumination im Kurs oder in der Rendering Pipeline spielt.
   Antwortanker: Explain local versus global illumination.
3. Beschreibe einen typischen Algorithmus oder Ablauf aus Local Illumination.
   Antwortanker: Decompose common local illumination into ambient, diffuse, and specular components.
4. Nenne typische Fehler, Artefakte oder Missverstaendnisse bei Local Illumination.
   Antwortanker: Local illumination ignores indirect light effects unless explicitly approximated.; Normals must be normalized and in the correct coordinate system.; Diffuse and specular terms model different visual phenomena.
5. Erstelle eine kleine Skizzenbeschreibung zu Local Illumination und erklaere sie.
   Antwortanker: Diagramm/Skizze aus dem passenden Kapitelchunk oder Visual Review Guide waehlen, dann Achsen/Objekte/Pipeline-Schritte erklaeren.

Kapitel 09: Texturing
---------------------
1. Definiere die wichtigsten Begriffe aus Texturing.
   Antwortanker: texture mapping, texture coordinates, texels, sampling, filtering. Danach Begriffe mit Seitenmarken im Kapitelchunk belegen.
2. Erklaere, welche Rolle Texturing im Kurs oder in der Rendering Pipeline spielt.
   Antwortanker: Explain textures as sampled data fields used during rendering.
3. Beschreibe einen typischen Algorithmus oder Ablauf aus Texturing.
   Antwortanker: Map texture coordinates to texture lookups and fragment shading.
4. Nenne typische Fehler, Artefakte oder Missverstaendnisse bei Texturing.
   Antwortanker: A texture is not only an image; it is sampled data for shading.; Texture coordinates live in their own domain and must be interpolated.; Filtering and mipmapping are about sampling quality, not geometry quality.
5. Erstelle eine kleine Skizzenbeschreibung zu Texturing und erklaere sie.
   Antwortanker: Diagramm/Skizze aus dem passenden Kapitelchunk oder Visual Review Guide waehlen, dann Achsen/Objekte/Pipeline-Schritte erklaeren.

Kapitel 10: Shadows
-------------------
1. Definiere die wichtigsten Begriffe aus Shadows.
   Antwortanker: shadows, visibility from light, shadow mapping, depth map, light space. Danach Begriffe mit Seitenmarken im Kapitelchunk belegen.
2. Erklaere, welche Rolle Shadows im Kurs oder in der Rendering Pipeline spielt.
   Antwortanker: Explain shadows as a visibility problem from the light source.
3. Beschreibe einen typischen Algorithmus oder Ablauf aus Shadows.
   Antwortanker: Describe the two-pass idea of shadow mapping.
4. Nenne typische Fehler, Artefakte oder Missverstaendnisse bei Shadows.
   Antwortanker: Shadow mapping stores depth from the light, not colors.; Bias is needed to reduce self-shadowing but can cause detached shadows.; Shadow quality depends on resolution, projection, and sampling.
5. Erstelle eine kleine Skizzenbeschreibung zu Shadows und erklaere sie.
   Antwortanker: Diagramm/Skizze aus dem passenden Kapitelchunk oder Visual Review Guide waehlen, dann Achsen/Objekte/Pipeline-Schritte erklaeren.

Mischfragen
-----------
1. Vergleiche Clipping, Culling und Depth Testing.
2. Erklaere den Weg eines Dreiecks von Objektkoordinaten bis zum sichtbaren Pixel.
3. Warum braucht man homogene Koordinaten fuer Transformation und Projektion?
4. Wie haengen Rasterization, Fragment Shader und Z-buffer zusammen?
5. Wie beeinflussen Normalen sowohl Beleuchtung als auch Texturing/Normal Mapping?
6. Warum sind Sampling, Aliasing und Mipmapping pruefungsrelevant?
7. Erklaere Shadow Mapping als Sichtbarkeitsproblem aus Sicht der Lichtquelle.
