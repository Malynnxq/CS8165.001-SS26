# Lecture 10 - Shadows

Source chunk: `course_text_parts/03_lectures/10_shadows.txt`
Extracted slide pages in source chunk: 60

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture explains shadows as a visibility problem from the light source. A point is lit if the light can see it; it is shadowed if another object blocks that visibility.

## How To Read This Lecture

- First read the big picture and the mental models.
- Then open the source chunk and compare the slide bullets to the commentary.
- After each section, answer the check question without notes.
- If the check feels vague, revisit the source pages listed for that section.

## Per-Slide Commentary

Every extracted slide page gets its own reading note. This is the part to use when the original PDF is too terse or visually dense.

### Page 1 - Untitled slide

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Untitled slide. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Untitled slide' into a causal sentence instead of repeating the slide title?

### Page 2 - Shadow Perception 1/3

Source cue: ▪ Visual perception of an environment is influenced by shadows / • Object object relationships / • Object space relationships / ▪ Improved depth perception is made possible by shadows / ▪ Shadows provide appealing visual effects

Commentary: This slide is about Shadow Perception 1/3. Read it as an occlusion decision. Decide whether the method reasons about objects, image regions, rays, or per-fragment depth comparisons. The visible cue is: ▪ Visual perception of an environment is influenced by shadows / • Object object relationships / • Object space relationships / ▪ Improved depth perception is made possible by shadows / ▪ Shadows provide appealing visual effects

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'Shadow Perception 1/3' works per object, per image region, per ray, or per fragment?

### Page 3 - Shadow Perception 2/3

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Shadow Perception 2/3. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Perception 2/3'?

### Page 4 - Shadow Perception 3/3

Source cue: ▪ KerstenD. Knill, D. C., Mamassian, P. and BülthoffⅠ. Illusory motion from shadows, Nature, 379 (31), / 1996.

Commentary: This slide is about Shadow Perception 3/3. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: ▪ KerstenD. Knill, D. C., Mamassian, P. and BülthoffⅠ. Illusory motion from shadows, Nature, 379 (31), / 1996.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Perception 3/3'?

### Page 5 - Shadow Atmosphere

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Shadow Atmosphere. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Atmosphere'?

### Page 6 - ▪ Shadows createa certain atmosphere

Source cue: ▪ The Lighthouse (2019)

Commentary: This slide is about ▪ Shadows createa certain atmosphere. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: ▪ The Lighthouse (2019)

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '▪ Shadows createa certain atmosphere'?

### Page 7 - Shadow Atmosphere

Source cue: ▪ Shadows createa certain atmosphere / ▪ The Lighthouse (2019) / ▪ Kill Bill: Volume 1 (2003)

Commentary: This slide is about Shadow Atmosphere. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: ▪ Shadows createa certain atmosphere / ▪ The Lighthouse (2019) / ▪ Kill Bill: Volume 1 (2003)

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Shadow Atmosphere'?

### Page 8 - Overview

Source cue: 10.1 Definitions / 10.2 Ground Plane Shadows / 10.3 Light Maps / 10.4 Shadow Volumes / 10.5 Shadow Maps

Commentary: This slide is about Overview. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: 10.1 Definitions / 10.2 Ground Plane Shadows / 10.3 Light Maps / 10.4 Shadow Volumes / 10.5 Shadow Maps

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Overview'?

### Page 9 - 10.1 Definitions

Source cue: About shadow-receiving and shadow-casting scene objects

Commentary: This slide is about 10.1 Definitions. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: About shadow-receiving and shadow-casting scene objects

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in '10.1 Definitions'?

### Page 10 - Classification of scene objects

Source cue: ▪ Distinction between / • Shadow-casting scene objects(Occluder) / • Shadow-receiving scene objects (Receiver) / ▪ Classify shadow-casting and shadow-receiving objects in a preprocess? / • Self-shadowing results from same object casting and receiving shadows

Commentary: This slide is about Classification of scene objects. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: ▪ Distinction between / • Shadow-casting scene objects(Occluder) / • Shadow-receiving scene objects (Receiver) / ▪ Classify shadow-casting and shadow-receiving objects in a preprocess? / • Self-shadowing results from same object casting and receiving shadows

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Classification of scene objects'?

### Page 11 - Umbra and Penumbra

Source cue: ▪ Point light sources / • Result in hard shadows / • High intensity contrast between shadowed andnon-shadowed region / ▪ Area light sources / • Result in soft shadows

Commentary: This slide is about Umbra and Penumbra. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: ▪ Point light sources / • Result in hard shadows / • High intensity contrast between shadowed andnon-shadowed region / ▪ Area light sources / • Result in soft shadows

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Umbra and Penumbra'?

### Page 12 - Hard and Soft Shadows

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Hard and Soft Shadows. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Hard and Soft Shadows'?

### Page 13 - Description of Shadows

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Description of Shadows. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Description of Shadows'?

### Page 14 - ▪ Shadows can be described differently

Source cue: ▪ Shadows can be modeled as / • Separate objects / • Surfaces not seen when lookinginto scene from light source / • Volumetric regions with reduced lighting

Commentary: This slide is about ▪ Shadows can be described differently. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: ▪ Shadows can be modeled as / • Separate objects / • Surfaces not seen when lookinginto scene from light source / • Volumetric regions with reduced lighting

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '▪ Shadows can be described differently'?

### Page 15 - Observations 1/2

Source cue: ▪ Possible shadow generation approaches / • Shadows as surfaces: exploit hidden-surface algorithms / • Shadows as projection: create shadows from A to Bby projecting A onto B from light source / ▪ Static vs. dynamic scenes / • Shadows are static in scenes with static lighting and scene objects (shadow computation

Commentary: This slide is about Observations 1/2. Read it as camera geometry. Track how 3D view-space positions become clip coordinates, normalized device coordinates, and finally screen locations. The visible cue is: ▪ Possible shadow generation approaches / • Shadows as surfaces: exploit hidden-surface algorithms / • Shadows as projection: create shadows from A to Bby projecting A onto B from light source / ▪ Static vs. dynamic scenes / • Shadows are static in scenes with static lighting and scene objects (shadow computation

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Check yourself: Can you explain how 'Observations 1/2' changes positions before rasterization?

### Page 16 - Observations 2/2

Source cue: ▪ Shadow shape can be obtained by projection / • Trivial for projection on flat surfaces / • Algorithmically very complex for projection in general case / ▪ Shadow intensity / • Shadows attenuate the incoming light used in illumination model

Commentary: This slide is about Observations 2/2. Read it as camera geometry. Track how 3D view-space positions become clip coordinates, normalized device coordinates, and finally screen locations. The visible cue is: ▪ Shadow shape can be obtained by projection / • Trivial for projection on flat surfaces / • Algorithmically very complex for projection in general case / ▪ Shadow intensity / • Shadows attenuate the incoming light used in illumination model

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Check yourself: Can you explain how 'Observations 2/2' changes positions before rasterization?

### Page 17 - Shadow Calculation Methods

Source cue: ▪ Ground plane shadows / • Static shadow polygons / • Dynamic shadow polygons / ▪ Projected shadows / ▪ Light maps

Commentary: This slide is about Shadow Calculation Methods. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: ▪ Ground plane shadows / • Static shadow polygons / • Dynamic shadow polygons / ▪ Projected shadows / ▪ Light maps

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Shadow Calculation Methods'?

### Page 18 - 10.2 Ground Plane Shadows

Source cue: Static and dynamic shadow polygons

Commentary: This slide is about 10.2 Ground Plane Shadows. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: Static and dynamic shadow polygons

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in '10.2 Ground Plane Shadows'?

### Page 19 - Static Shadow Polygons

Source cue: ▪ Render dark polygons to represent shadow regions / • Cast ray from light source through center of shadow-casting objects / • Position dark polygon where ray intersects shadow-receiving object / ▪ Disadvantages / • Static shapes cannot represent geometry of dynamic scene objects

Commentary: This slide is about Static Shadow Polygons. Read it as an occlusion decision. Decide whether the method reasons about objects, image regions, rays, or per-fragment depth comparisons. The visible cue is: ▪ Render dark polygons to represent shadow regions / • Cast ray from light source through center of shadow-casting objects / • Position dark polygon where ray intersects shadow-receiving object / ▪ Disadvantages / • Static shapes cannot represent geometry of dynamic scene objects

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'Static Shadow Polygons' works per object, per image region, per ray, or per fragment?

### Page 20 - Render Static Shadow Polygons 1/2

Source cue: ▪ Depth value identical with thatof shadow-receiving polygon(care must be taken wrt. z-buffer / fighting) / ▪ Depth value smaller than that of shadow-receiving polygon(shadow can be too large)

Commentary: This slide is about Render Static Shadow Polygons 1/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: ▪ Depth value identical with thatof shadow-receiving polygon(care must be taken wrt. z-buffer / fighting) / ▪ Depth value smaller than that of shadow-receiving polygon(shadow can be too large)

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Render Static Shadow Polygons 1/2'?

### Page 21 - Render Static Shadow Polygons 2/2

Source cue: ▪ Disable depth test / • Cast ray to determine shadow visibility / • Show entire shadow polygon / ▪ Shadow too large and possibly in wrong places / ▪ Test corners for shadow visibility

Commentary: This slide is about Render Static Shadow Polygons 2/2. Read it as an occlusion decision. Decide whether the method reasons about objects, image regions, rays, or per-fragment depth comparisons. The visible cue is: ▪ Disable depth test / • Cast ray to determine shadow visibility / • Show entire shadow polygon / ▪ Shadow too large and possibly in wrong places / ▪ Test corners for shadow visibility

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'Render Static Shadow Polygons 2/2' works per object, per image region, per ray, or per fragment?

### Page 22 - Static Shadow Polygons

Source cue: ▪ Good for car racing games (static scene geometry) / ▪ With fast movements and proximity of casters and receivers,wrong shadows are often not detected / as such

Commentary: This slide is about Static Shadow Polygons. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: ▪ Good for car racing games (static scene geometry) / ▪ With fast movements and proximity of casters and receivers,wrong shadows are often not detected / as such

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Static Shadow Polygons'?

### Page 23 - Dynamic Shadow Polygons

Source cue: ▪ Project shadow-casting scene objects onto shadow-receiving objectby modifying shape / ▪ Accurate procedure for semi-transparent shadows,but only if shadows do not overlap / ▪ Restrictions / • Only planar polygons on shadow-receivingscene objects possible / • No self-shadowing possible

Commentary: This slide is about Dynamic Shadow Polygons. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: ▪ Project shadow-casting scene objects onto shadow-receiving objectby modifying shape / ▪ Accurate procedure for semi-transparent shadows,but only if shadows do not overlap / ▪ Restrictions / • Only planar polygons on shadow-receivingscene objects possible / • No self-shadowing possible

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Dynamic Shadow Polygons'?

### Page 24 - Shadow Projection

Source cue: S L / ▪ Shadow point (= vertex of the shadow polygon) lies on a line between light source and vertex / of shadow-casting scene object / S = P − α ⋅ L / S z = 0 α =

Commentary: This slide is about Shadow Projection. Read it as camera geometry. Track how 3D view-space positions become clip coordinates, normalized device coordinates, and finally screen locations. The visible cue is: S L / ▪ Shadow point (= vertex of the shadow polygon) lies on a line between light source and vertex / of shadow-casting scene object / S = P − α ⋅ L / S z = 0 α =

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Check yourself: Can you explain how 'Shadow Projection' changes positions before rasterization?

### Page 25 - Rendering Dynamic Shadow Polygons

Source cue: ▪ Matrix transforms object into its shadow polygon / ▪ Render scene object with shadows / • Render scene object / • Multiply current model-view -matrix with / • Render scene object in shadow color with b lending

Commentary: This slide is about Rendering Dynamic Shadow Polygons. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: ▪ Matrix transforms object into its shadow polygon / ▪ Render scene object with shadows / • Render scene object / • Multiply current model-view -matrix with / • Render scene object in shadow color with b lending

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Rendering Dynamic Shadow Polygons'?

### Page 26 - 10.3 Light Maps

Source cue: Structured lighting with textures

Commentary: This slide is about 10.3 Light Maps. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: Structured lighting with textures

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '10.3 Light Maps'?

### Page 27 - Light Maps

Source cue: ▪ Static shadows can be precomputed and stored in light maps / ▪ When precomputing light maps, shadows are calculated offline(e.g. with ray tracing) / ▪ Soft shadows in lightmaps / • Interpolation of the lightmap creates soft shadow approximations / • Light source sampling results in better results,sending multiple rays to different points of the

Commentary: This slide is about Light Maps. Read it as an occlusion decision. Decide whether the method reasons about objects, image regions, rays, or per-fragment depth comparisons. The visible cue is: ▪ Static shadows can be precomputed and stored in light maps / ▪ When precomputing light maps, shadows are calculated offline(e.g. with ray tracing) / ▪ Soft shadows in lightmaps / • Interpolation of the lightmap creates soft shadow approximations / • Light source sampling results in better results,sending multiple rays to different points of the

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'Light Maps' works per object, per image region, per ray, or per fragment?

### Page 28 - Soft Shadows with Light Maps 1/2

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Soft Shadows with Light Maps 1/2. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Soft Shadows with Light Maps 1/2'?

### Page 29 - Soft Shadows with Light Maps 2/2

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Soft Shadows with Light Maps 2/2. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Soft Shadows with Light Maps 2/2'?

### Page 30 - 10.4 Shadow Volumes

Source cue: Representation of shadows by geometry enclosing them

Commentary: This slide is about 10.4 Shadow Volumes. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: Representation of shadows by geometry enclosing them

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in '10.4 Shadow Volumes'?

### Page 31 - Shadow Volumes

Source cue: ▪ Shadows are considered as volume in space / ▪ Originally developed by Crow in 1977 / ▪ Extension by Brotman and Badler in 1984 / ▪ Heidmann introduced the technology for efficientrendering of shadow volumes in 1991

Commentary: This slide is about Shadow Volumes. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: ▪ Shadows are considered as volume in space / ▪ Originally developed by Crow in 1977 / ▪ Extension by Brotman and Badler in 1984 / ▪ Heidmann introduced the technology for efficientrendering of shadow volumes in 1991

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Volumes'?

### Page 32 - Initial Considerations

Source cue: ▪ Shadow volume shape depends on shape and positionof light source and shadow-caster / ▪ All points inside shadow volume are shadowed / ▪ Shadow volume generation / • Find silhouettes of shadow-casterregarding light source / • Extrudes silhouettes in light ray directionto create polygons

Commentary: This slide is about Initial Considerations. Read it as an occlusion decision. Decide whether the method reasons about objects, image regions, rays, or per-fragment depth comparisons. The visible cue is: ▪ Shadow volume shape depends on shape and positionof light source and shadow-caster / ▪ All points inside shadow volume are shadowed / ▪ Shadow volume generation / • Find silhouettes of shadow-casterregarding light source / • Extrudes silhouettes in light ray directionto create polygons

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'Initial Considerations' works per object, per image region, per ray, or per fragment?

### Page 33 - Shadow Volume Geometry

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Shadow Volume Geometry. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Volume Geometry'?

### Page 34 - Shadow Volume Realization

Source cue: ▪ Silhouettes edges can be found by analyzing normals / • Silhouette edge lies between front and back face (as seen from light source) / ▪ Silhouette edges are stored as vertex list containing vertices / ▪ For convex shadow-casters / L V

Commentary: This slide is about Shadow Volume Realization. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: ▪ Silhouettes edges can be found by analyzing normals / • Silhouette edge lies between front and back face (as seen from light source) / ▪ Silhouette edges are stored as vertex list containing vertices / ▪ For convex shadow-casters / L V

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Shadow Volume Realization'?

### Page 35 - Shadow Volume Properties 1/2

Source cue: ▪ All points inside shadow volume are shadowed / ▪ Shadowing can be determined for each view ray by intersection tests / • Assumption: Camera not in shadow volume / • At each intersection with front-face shadow polygon, intersection counter cnt is incremented / • At each intersection with back-face shadow polygon, intersection counter cnt is decremented

Commentary: This slide is about Shadow Volume Properties 1/2. Read it as camera geometry. Track how 3D view-space positions become clip coordinates, normalized device coordinates, and finally screen locations. The visible cue is: ▪ All points inside shadow volume are shadowed / ▪ Shadowing can be determined for each view ray by intersection tests / • Assumption: Camera not in shadow volume / • At each intersection with front-face shadow polygon, intersection counter cnt is incremented / • At each intersection with back-face shadow polygon, intersection counter cnt is decremented

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Check yourself: Can you explain how 'Shadow Volume Properties 1/2' changes positions before rasterization?

### Page 36 - Shadow Volume Properties 2/2

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Shadow Volume Properties 2/2. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Volume Properties 2/2'?

### Page 37 - Stencil Shadow Volume

Source cue: ▪ Generation of shadow volumes per frame / • Works well for scenes with few moving objects / • Expensive for complex shadow volumes / • Improvement by simplifying shadow-casting geometries / ▪ Four rendering passes required

Commentary: This slide is about Stencil Shadow Volume. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: ▪ Generation of shadow volumes per frame / • Works well for scenes with few moving objects / • Expensive for complex shadow volumes / • Improvement by simplifying shadow-casting geometries / ▪ Four rendering passes required

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Stencil Shadow Volume'?

### Page 38 - Implementation

Source cue: ▪ Determine visible scene objects / • Render scene without writing in color buffer / ▪ Represent shadow volume in stencil buffer / • Initialize stencil buffer with 0 / • Render front-face shadow polygons and increment stencil buffer by 1

Commentary: This slide is about Implementation. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: ▪ Determine visible scene objects / • Render scene without writing in color buffer / ▪ Represent shadow volume in stencil buffer / • Initialize stencil buffer with 0 / • Render front-face shadow polygons and increment stencil buffer by 1

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Implementation'?

### Page 39 - Special Case: COP in the shadows

Source cue: ▪ When COP lies in a shadow volume, the situation can be unclear / • Near - or far -plane can intersect shadow volume / ▪ Possible solutions / s = 0 / • Test COP against all shadow volumes cnt

Commentary: This slide is about Special Case: COP in the shadows. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: ▪ When COP lies in a shadow volume, the situation can be unclear / • Near - or far -plane can intersect shadow volume / ▪ Possible solutions / s = 0 / • Test COP against all shadow volumes cnt

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Special Case: COP in the shadows'?

### Page 40 - Shadow Volume Example

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Shadow Volume Example. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Volume Example'?

### Page 41 - Shadow Volume Conclusions

Source cue: ▪ Advantages / • Shadow-casting and shadow-receiving objects can have arbitrary shapes / • Applicable for multiple light sources / • Level-of-detail adaptable through approximated geometries / • Shadow volumes for static pairs of objects and lights can be precalculated

Commentary: This slide is about Shadow Volume Conclusions. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: ▪ Advantages / • Shadow-casting and shadow-receiving objects can have arbitrary shapes / • Applicable for multiple light sources / • Level-of-detail adaptable through approximated geometries / • Shadow volumes for static pairs of objects and lights can be precalculated

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Shadow Volume Conclusions'?

### Page 42 - 10.5 Shadow Maps

Source cue: Depth test from the point of view of the light source

Commentary: This slide is about 10.5 Shadow Maps. Read it as an occlusion decision. Decide whether the method reasons about objects, image regions, rays, or per-fragment depth comparisons. The visible cue is: Depth test from the point of view of the light source

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether '10.5 Shadow Maps' works per object, per image region, per ray, or per fragment?

### Page 43 - Shadow Mapping

Source cue: ▪ Based on z-Buffer (contains depth relative to the light source) / ▪ First used within Pixar’s Renderman

Commentary: This slide is about Shadow Mapping. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: ▪ Based on z-Buffer (contains depth relative to the light source) / ▪ First used within Pixar’s Renderman

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shadow Mapping'?

### Page 44 - Projected Shadows

Source cue: ▪ depth texture / ▪ Rendering algorithm / • Render shadow-casting objectsas seen from the light source into depth texture / • Project depth texture using projective texturingwhen rendering shadow-receiving objects / ▪ Characteristics of the process

Commentary: This slide is about Projected Shadows. Read it as an occlusion decision. Decide whether the method reasons about objects, image regions, rays, or per-fragment depth comparisons. The visible cue is: ▪ depth texture / ▪ Rendering algorithm / • Render shadow-casting objectsas seen from the light source into depth texture / • Project depth texture using projective texturingwhen rendering shadow-receiving objects / ▪ Characteristics of the process

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'Projected Shadows' works per object, per image region, per ray, or per fragment?

### Page 45 - Untitled slide

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Untitled slide. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Untitled slide' into a causal sentence instead of repeating the slide title?

### Page 46 - Depth Comparison

Source cue: ▪ For each vertex in world coordinates determine associated depth value in shadow map / • Transform into camera’s eye space / • Use light source’s 4x4 transformation matrix to transform into light’s clip space / • Compare depth value with associated depth value in shadow map

Commentary: This slide is about Depth Comparison. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: ▪ For each vertex in world coordinates determine associated depth value in shadow map / • Transform into camera’s eye space / • Use light source’s 4x4 transformation matrix to transform into light’s clip space / • Compare depth value with associated depth value in shadow map

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Depth Comparison'?

### Page 47 - Coordinate Systems

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Coordinate Systems. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Coordinate Systems'?

### Page 48 - Pseudo Code

Source cue: // generate shadow map w.r.t light source / generateShadowMap(); / // render scene from COP / for all rasterized fragments do { / Transform fragment xyz into lights coordinate system

Commentary: This slide is about Pseudo Code. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: // generate shadow map w.r.t light source / generateShadowMap(); / // render scene from COP / for all rasterized fragments do { / Transform fragment xyz into lights coordinate system

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Pseudo Code'?

### Page 49 - Properties

Source cue: ▪ Shadow maps are static when scene and lighting are static / ▪ Shadow quality depends on shadow map resolution / ▪ Shadow mapping has three main problems / • View volume problem / • Bias problem

Commentary: This slide is about Properties. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: ▪ Shadow maps are static when scene and lighting are static / ▪ Shadow quality depends on shadow map resolution / ▪ Shadow mapping has three main problems / • View volume problem / • Bias problem

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Properties'?

### Page 50 - View Volume Problem

Source cue: ▪ When vertex lies outside light source’s view volume,required depth information is missing / ▪ Possible remedies / • Use cubic shadow map (similar to cubic environment map) / • Use only spotlights

Commentary: This slide is about View Volume Problem. Read it as an occlusion decision. Decide whether the method reasons about objects, image regions, rays, or per-fragment depth comparisons. The visible cue is: ▪ When vertex lies outside light source’s view volume,required depth information is missing / ▪ Possible remedies / • Use cubic shadow map (similar to cubic environment map) / • Use only spotlights

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'View Volume Problem' works per object, per image region, per ray, or per fragment?

### Page 51 - Bias Problem 1/2

Source cue: Incorrect self-shadowing occurs for / all fragments with ShadowMap(x',y') ≈ z’ / Can be corrected by / increasing depth precision of z-buffer / applying z-bias

Commentary: This slide is about Bias Problem 1/2. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: Incorrect self-shadowing occurs for / all fragments with ShadowMap(x',y') ≈ z’ / Can be corrected by / increasing depth precision of z-buffer / applying z-bias

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Bias Problem 1/2'?

### Page 52 - Bias Problem 2/2

Source cue: It is difficult to choose a good z-bias / ShadowMap(x',y') + bias ? / ▪ good / ▪ too low / ▪ too high

Commentary: This slide is about Bias Problem 2/2. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: It is difficult to choose a good z-bias / ShadowMap(x',y') + bias ? / ▪ good / ▪ too low / ▪ too high

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Bias Problem 2/2'?

### Page 53 - Aliasing Problem 1/3

Source cue: ▪ Aliasing occurs when shadow map is undersampled(i.e., a texel in shadow map covers several / pixels) / ▪ Particularly bad when camera and light source are facing each other

Commentary: This slide is about Aliasing Problem 1/3. Read it as camera geometry. Track how 3D view-space positions become clip coordinates, normalized device coordinates, and finally screen locations. The visible cue is: ▪ Aliasing occurs when shadow map is undersampled(i.e., a texel in shadow map covers several / pixels) / ▪ Particularly bad when camera and light source are facing each other

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Check yourself: Can you explain how 'Aliasing Problem 1/3' changes positions before rasterization?

### Page 54 - Aliasing Problem 2/3

Source cue: ▪ Filter (= weighted average formation over neighbors) of a depth valuedoes not make sense / ▪ Percentage Closest Filtering (PCF) / • Filter results of shadow tests (weighted average of comparison results) / • Bias selection is made even more difficult / ▪ Choosing the filter kernel

Commentary: This slide is about Aliasing Problem 2/3. Read it as an occlusion decision. Decide whether the method reasons about objects, image regions, rays, or per-fragment depth comparisons. The visible cue is: ▪ Filter (= weighted average formation over neighbors) of a depth valuedoes not make sense / ▪ Percentage Closest Filtering (PCF) / • Filter results of shadow tests (weighted average of comparison results) / • Bias selection is made even more difficult / ▪ Choosing the filter kernel

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'Aliasing Problem 2/3' works per object, per image region, per ray, or per fragment?

### Page 55 - Untitled slide

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Untitled slide. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Untitled slide' into a causal sentence instead of repeating the slide title?

### Page 56 - Aliasing Problem 3/3

Source cue: ▪ Averaging Filter / ▪ Percentage Closest Filtering

Commentary: This slide is about Aliasing Problem 3/3. Read it as sampled data access. Identify coordinates, texture object/state, filtering, mip level, and how the shader interprets the sampled value. The visible cue is: ▪ Averaging Filter / ▪ Percentage Closest Filtering

Why it matters: Texture sampling is a major source of visual detail and a common source of artifacts.

Check yourself: Can you identify the sampled data, coordinate, and filtering/state issue in 'Aliasing Problem 3/3'?

### Page 57 - Untitled slide

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Untitled slide. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Untitled slide' into a causal sentence instead of repeating the slide title?

### Page 58 - ▪ Shadows in Visual Perception

Source cue: • Enhance depth perception and object relationships / • Create appealing visual effects and atmosphere / ▪ Shadow Definitions and Types / • Shadow-casting (Occluder) vs. shadow-receiving (Receiver) objects / • Self-shadowing: Same object casts and receives shadow

Commentary: This slide is about ▪ Shadows in Visual Perception. Read it as an occlusion decision. Decide whether the method reasons about objects, image regions, rays, or per-fragment depth comparisons. The visible cue is: • Enhance depth perception and object relationships / • Create appealing visual effects and atmosphere / ▪ Shadow Definitions and Types / • Shadow-casting (Occluder) vs. shadow-receiving (Receiver) objects / • Self-shadowing: Same object casts and receives shadow

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether '▪ Shadows in Visual Perception' works per object, per image region, per ray, or per fragment?

### Page 59 - Literature and other sources used in this chapter

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Commentary: This slide is about Literature and other sources used in this chapter. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Literature and other sources used in this chapter' into a causal sentence instead of repeating the slide title?

### Page 60 - ▪ Text Books

Source cue: • P. Shirley, M. AshikhminS. Marschner: Fundamentals of Computer Graphics (3rd ed. Edition), AK / ▪ Research Publications / • Crow, F., Shadows Algorithms for Computers Graphics, SIGGRAPH 1977. / • Lance Williams: Casting curved shadows on curved surfaces, SIGGRAPH 1978.

Commentary: This slide is about ▪ Text Books. Read it as visibility from the light source. Ask what blocks the light, how that blocking is represented, and which artifact the method may create. The visible cue is: • P. Shirley, M. AshikhminS. Marschner: Fundamentals of Computer Graphics (3rd ed. Edition), AK / ▪ Research Publications / • Crow, F., Shadows Algorithms for Computers Graphics, SIGGRAPH 1977. / • Lance Williams: Casting curved shadows on curved surfaces, SIGGRAPH 1978.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in '▪ Text Books'?

## 10.1 Definitions

Source location: Section 10.1

### Commentary

A shadow is not simply a dark texture. It is evidence that light visibility is blocked. Important distinctions include hard versus soft shadows, umbra versus penumbra, and geometric versus precomputed approaches.

For real-time graphics, shadows are usually approximated. The approximation must answer a visibility question cheaply enough for interactive rendering.

### Mental Model

Shadows are light-space visibility made visible in the camera image.

### Check Yourself

Why is shadow computation related to visibility determination?

## 10.2 Ground Plane Shadows

Source location: Section 10.2

### Commentary

Ground plane shadows project an object onto a receiving plane. This is simple and can look convincing in restricted scenes, but it assumes a known planar receiver and does not handle general shadowing between arbitrary objects.

The method is useful pedagogically because it makes the geometric nature of shadows explicit: a light source, an occluder, and a receiver define where the shadow lands.

### Mental Model

A planar shadow is projected geometry on a known receiver.

### Check Yourself

What scene limitation makes ground plane shadows less general than shadow maps?

## 10.3 Light Maps

Source location: Section 10.3

### Commentary

Light maps store precomputed lighting or shadow information in textures. They can be efficient at runtime, but they are limited when lights, objects, or geometry move dynamically.

This is another example of a recurring graphics tradeoff: precompute for speed, but lose flexibility. Real-time rendering often mixes precomputed and dynamic techniques.

### Mental Model

A light map spends storage and preprocessing to save runtime shading work.

### Check Yourself

Why are light maps less suitable for fully dynamic moving lights?

## 10.4 Shadow Volumes

Source location: Section 10.4

### Commentary

Shadow volumes construct the volume of space blocked from a light by an occluder. The camera view can then determine whether visible points lie inside that volume. Stencil buffer techniques are often associated with this method.

The strength is geometric precision for hard shadows. The cost is handling silhouette edges, volume construction, and robust stencil operations. It is a good contrast to shadow maps, which are image-based from the light view.

### Mental Model

A shadow volume is the 3D region where the light cannot reach.

### Check Yourself

Why are silhouette edges important for constructing shadow volumes?

## 10.5 Shadow Maps

Source location: Section 10.5

### Commentary

Shadow mapping renders the scene from the light's point of view and stores depth. During the camera pass, a surface point is transformed into light space and compared against the stored depth. If it is farther than what the light saw, it is in shadow.

This method is practical and widely used, but it has artifacts. Shadow acne comes from precision/self-comparison issues. Bias can reduce acne but too much bias causes detached shadows. Resolution, filtering, and light projection strongly affect quality.

### Mental Model

Shadow maps reuse the depth-buffer idea, but from the light's camera.

### Check Yourself

What exactly is stored in a shadow map?

## End-of-Lecture Summary

If you remember only one thing from Lecture 10, remember this: This lecture explains shadows as a visibility problem from the light source. A point is lit if the light can see it; it is shadowed if another object blocks that visibility.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
