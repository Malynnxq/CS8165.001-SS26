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

### Page 1 - Visual or title slide

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Visual or title slide' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Visual or title slide. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer links this visual or title page to the closest surrounding concept slide and names the topic transition it introduces.

Common trap: Do not invent details that are not visible in the extracted text; use this page as a boundary marker and rely on adjacent slides for technical content.

Check yourself: Can you turn 'Visual or title slide' into a causal sentence instead of repeating the slide title?

### Page 2 - Shadow Perception 1/3

Source cue: ▪ Visual perception of an environment is influenced by shadows / • Object object relationships / • Object space relationships / ▪ Improved depth perception is made possible by shadows / ▪ Shadows provide appealing visual effects

Professor-style explanation: The slide 'Shadow Perception 1/3' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: ▪ Visual perception of an environment is influenced by shadows / • Object object relationships / • Object space relationships / ▪ Improved depth perception is made possible by shadows / ▪ Shadows provide appealing visual effects. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Shadow Perception 1/3. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: ▪ Visual perception of an environment is influenced by shadows / • Object object relationships / • Object space relationships / ▪ Improved depth perception is made possible by shadows / ▪ Shadows provide appealing visual effects. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Shadow Perception 1/3' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Shadow Perception 1/3' works per object, per image region, per ray, or per fragment?

### Page 3 - Shadow Perception 2/3

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Shadow Perception 2/3' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Shadow Perception 2/3. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Shadow Perception 2/3' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Perception 2/3'?

### Page 4 - Shadow Perception 3/3

Source cue: ▪ KerstenD. Knill, D. C., Mamassian, P. and BülthoffI. Illusory motion from shadows, Nature, 379 (31), / 1996.

Professor-style explanation: The slide 'Shadow Perception 3/3' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. The terms describe light-space visibility: ▪ KerstenD. Knill, D. C., Mamassian, P. and BülthoffI. Illusory motion from shadows, Nature, 379 (31), / 1996. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image. For examination purposes, the important content is light-space visibility: a point is shadowed because another object blocks the path from the light.

Technical commentary: This slide is about Shadow Perception 3/3. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The terms describe light-space visibility: ▪ KerstenD. Knill, D. C., Mamassian, P. and BülthoffI. Illusory motion from shadows, Nature, 379 (31), / 1996. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Shadow Perception 3/3' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Perception 3/3'?

### Page 5 - Shadow Atmosphere

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Shadow Atmosphere' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Shadow Atmosphere. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Shadow Atmosphere' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Atmosphere'?

### Page 6 - ▪ Shadows createa certain atmosphere

Source cue: ▪ The Lighthouse (2019)

Professor-style explanation: The slide '▪ Shadows createa certain atmosphere' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: ▪ The Lighthouse (2019). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about ▪ Shadows createa certain atmosphere. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: ▪ The Lighthouse (2019). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for '▪ Shadows createa certain atmosphere' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '▪ Shadows createa certain atmosphere'?

### Page 7 - Shadow Atmosphere

Source cue: ▪ Shadows createa certain atmosphere / ▪ The Lighthouse (2019) / ▪ Kill Bill: Volume 1 (2003)

Professor-style explanation: The slide 'Shadow Atmosphere' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: ▪ Shadows createa certain atmosphere / ▪ The Lighthouse (2019) / ▪ Kill Bill: Volume 1 (2003). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Shadow Atmosphere. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: ▪ Shadows createa certain atmosphere / ▪ The Lighthouse (2019) / ▪ Kill Bill: Volume 1 (2003). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Shadow Atmosphere' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Shadow Atmosphere'?

### Page 8 - Overview

Source cue: 10.1 Definitions / 10.2 Ground Plane Shadows / 10.3 Light Maps / 10.4 Shadow Volumes / 10.5 Shadow Maps

Professor-style explanation: The outline 'Overview' gives the lecture its internal logic. The listed topics are the objects that will be connected during the chapter: first the problem space, then the mathematical or algorithmic tools, then the implementation consequences. The listed entries form a dependency order: 10.1 Definitions / 10.2 Ground Plane Shadows / 10.3 Light Maps / 10.4 Shadow Volumes / 10.5 Shadow Maps. Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary. The order matters because later items rely on earlier definitions. For example, an OpenGL mechanism is much easier to understand once the corresponding pipeline object or mathematical operation has already been introduced. The outline is therefore a compact dependency graph of the lecture rather than a collection of isolated labels. For examination purposes, the important content is the dependency structure: which concept introduces the vocabulary, which later algorithm uses it, and which implementation problem it solves.

Technical commentary: This slide is about Overview. The listed items define the lecture sequence: the topic begins with a problem statement, introduces the required objects or algorithms, and then connects them to rendering or implementation consequences. The listed entries form a dependency order: 10.1 Definitions / 10.2 Ground Plane Shadows / 10.3 Light Maps / 10.4 Shadow Volumes / 10.5 Shadow Maps. Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary.

Why it matters: Outlines tell you the dependency order. They are the safest way to avoid learning isolated bullet points.

Exam-grade answer: A strong answer for 'Overview' names the topics in order and explains at least one dependency between an earlier item and a later item.

Common trap: Do not memorize 'Overview' as a list of headings only; the exam-relevant part is how the headings depend on each other.

Check yourself: Can you explain where 'Overview' fits in the lecture order and what later section depends on it?

### Page 9 - 10.1 Definitions

Source cue: About shadow-receiving and shadow-casting scene objects

Professor-style explanation: The slide '10.1 Definitions' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. The terms describe light-space visibility: About shadow-receiving and shadow-casting scene objects. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image. For examination purposes, the important content is light-space visibility: a point is shadowed because another object blocks the path from the light.

Technical commentary: This slide is about 10.1 Definitions. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The terms describe light-space visibility: About shadow-receiving and shadow-casting scene objects. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for '10.1 Definitions' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in '10.1 Definitions'?

### Page 10 - Classification of scene objects

Source cue: ▪ Distinction between / • Shadow-casting scene objects(Occluder) / • Shadow-receiving scene objects (Receiver) / ▪ Classify shadow-casting and shadow-receiving objects in a preprocess? / • Self-shadowing results from same object casting and receiving shadows

Professor-style explanation: The slide 'Classification of scene objects' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. The terms describe light-space visibility: ▪ Distinction between / • Shadow-casting scene objects(Occluder) / • Shadow-receiving scene objects (Receiver) / ▪ Classify shadow-casting and shadow-receiving objects in a preprocess? / • Self-shadowing results from same object casting and receiving shadows. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image. For examination purposes, the important content is light-space visibility: a point is shadowed because another object blocks the path from the light.

Technical commentary: This slide is about Classification of scene objects. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The terms describe light-space visibility: ▪ Distinction between / • Shadow-casting scene objects(Occluder) / • Shadow-receiving scene objects (Receiver) / ▪ Classify shadow-casting and shadow-receiving objects in a preprocess? / • Self-shadowing results from same object casting and receiving shadows. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Classification of scene objects' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Classification of scene objects'?

### Page 11 - Umbra and Penumbra

Source cue: ▪ Point light sources / • Result in hard shadows / • High intensity contrast between shadowed andnon-shadowed region / ▪ Area light sources / • Result in soft shadows

Professor-style explanation: The slide 'Umbra and Penumbra' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: ▪ Point light sources / • Result in hard shadows / • High intensity contrast between shadowed andnon-shadowed region / ▪ Area light sources / • Result in soft shadows. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Umbra and Penumbra. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: ▪ Point light sources / • Result in hard shadows / • High intensity contrast between shadowed andnon-shadowed region / ▪ Area light sources / • Result in soft shadows. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Umbra and Penumbra' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Umbra and Penumbra'?

### Page 12 - Hard and Soft Shadows

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Hard and Soft Shadows' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Hard and Soft Shadows. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Hard and Soft Shadows' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Hard and Soft Shadows'?

### Page 13 - Description of Shadows

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Description of Shadows' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Description of Shadows. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Description of Shadows' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Description of Shadows'?

### Page 14 - ▪ Shadows can be described differently

Source cue: ▪ Shadows can be modeled as / • Separate objects / • Surfaces not seen when lookinginto scene from light source / • Volumetric regions with reduced lighting

Professor-style explanation: The slide '▪ Shadows can be described differently' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: ▪ Shadows can be modeled as / • Separate objects / • Surfaces not seen when lookinginto scene from light source / • Volumetric regions with reduced lighting. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about ▪ Shadows can be described differently. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: ▪ Shadows can be modeled as / • Separate objects / • Surfaces not seen when lookinginto scene from light source / • Volumetric regions with reduced lighting. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for '▪ Shadows can be described differently' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '▪ Shadows can be described differently'?

### Page 15 - Observations 1/2

Source cue: ▪ Possible shadow generation approaches / • Shadows as surfaces: exploit hidden-surface algorithms / • Shadows as projection: create shadows from A to Bby projecting A onto B from light source / ▪ Static vs. dynamic scenes / • Shadows are static in scenes with static lighting and scene objects (shadow computation

Professor-style explanation: The slide 'Observations 1/2' explains how camera geometry turns a 3D scene into image coordinates. In view space, objects are described relative to the camera. The projection matrix then maps that camera-centered geometry into clip space, where the viewing volume and clipping boundaries can be handled consistently. Perspective projection uses the homogeneous coordinate so that the later divide by w creates foreshortening: farther objects occupy less image space. Orthographic projection removes that depth-based size change and keeps parallel structures visually parallel. The terms describe camera-to-screen mapping: ▪ Possible shadow generation approaches / • Shadows as surfaces: exploit hidden-surface algorithms / • Shadows as projection: create shadows from A to Bby projecting A onto B from light source / ▪ Static vs. dynamic scenes / • Shadows are static in scenes with static lighting and scene objects (shadow computation. View-space geometry is mapped by a projection matrix, clipped, divided into normalized coordinates, and finally mapped to a viewport. The object chain is view-space position, projection matrix, clip coordinate, normalized device coordinate, and viewport coordinate. The slide is therefore connecting camera setup, visual appearance, and the numeric coordinate pipeline that rasterization later consumes. For examination purposes, the important content is the camera-to-screen chain: view coordinates, projection matrix, clip coordinates, perspective divide, normalized device coordinates, and viewport mapping.

Technical commentary: This slide is about Observations 1/2. The projection objects on the slide convert view-space geometry into clip coordinates, normalized coordinates, and finally screen-related positions. The terms describe camera-to-screen mapping: ▪ Possible shadow generation approaches / • Shadows as surfaces: exploit hidden-surface algorithms / • Shadows as projection: create shadows from A to Bby projecting A onto B from light source / ▪ Static vs. dynamic scenes / • Shadows are static in scenes with static lighting and scene objects (shadow computation. View-space geometry is mapped by a projection matrix, clipped, divided into normalized coordinates, and finally mapped to a viewport.

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Exam-grade answer: A strong answer for 'Observations 1/2' explains the mapping from view space through clip space and perspective divide to normalized and viewport coordinates.

Common trap: Do not confuse projection with viewport mapping; projection creates clip coordinates and the perspective divide comes before final screen mapping.

Check yourself: Can you explain how 'Observations 1/2' changes positions before rasterization?

### Page 16 - Observations 2/2

Source cue: ▪ Shadow shape can be obtained by projection / • Trivial for projection on flat surfaces / • Algorithmically very complex for projection in general case / ▪ Shadow intensity / • Shadows attenuate the incoming light used in illumination model

Professor-style explanation: The slide 'Observations 2/2' explains how camera geometry turns a 3D scene into image coordinates. In view space, objects are described relative to the camera. The projection matrix then maps that camera-centered geometry into clip space, where the viewing volume and clipping boundaries can be handled consistently. Perspective projection uses the homogeneous coordinate so that the later divide by w creates foreshortening: farther objects occupy less image space. Orthographic projection removes that depth-based size change and keeps parallel structures visually parallel. The terms describe camera-to-screen mapping: ▪ Shadow shape can be obtained by projection / • Trivial for projection on flat surfaces / • Algorithmically very complex for projection in general case / ▪ Shadow intensity / • Shadows attenuate the incoming light used in illumination model. View-space geometry is mapped by a projection matrix, clipped, divided into normalized coordinates, and finally mapped to a viewport. The object chain is view-space position, projection matrix, clip coordinate, normalized device coordinate, and viewport coordinate. The slide is therefore connecting camera setup, visual appearance, and the numeric coordinate pipeline that rasterization later consumes. For examination purposes, the important content is the camera-to-screen chain: view coordinates, projection matrix, clip coordinates, perspective divide, normalized device coordinates, and viewport mapping.

Technical commentary: This slide is about Observations 2/2. The projection objects on the slide convert view-space geometry into clip coordinates, normalized coordinates, and finally screen-related positions. The terms describe camera-to-screen mapping: ▪ Shadow shape can be obtained by projection / • Trivial for projection on flat surfaces / • Algorithmically very complex for projection in general case / ▪ Shadow intensity / • Shadows attenuate the incoming light used in illumination model. View-space geometry is mapped by a projection matrix, clipped, divided into normalized coordinates, and finally mapped to a viewport.

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Exam-grade answer: A strong answer for 'Observations 2/2' explains the mapping from view space through clip space and perspective divide to normalized and viewport coordinates.

Common trap: Do not confuse projection with viewport mapping; projection creates clip coordinates and the perspective divide comes before final screen mapping.

Check yourself: Can you explain how 'Observations 2/2' changes positions before rasterization?

### Page 17 - Shadow Calculation Methods

Source cue: ▪ Ground plane shadows / • Static shadow polygons / • Dynamic shadow polygons / ▪ Projected shadows / ▪ Light maps

Professor-style explanation: The slide 'Shadow Calculation Methods' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: ▪ Ground plane shadows / • Static shadow polygons / • Dynamic shadow polygons / ▪ Projected shadows / ▪ Light maps. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Shadow Calculation Methods. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: ▪ Ground plane shadows / • Static shadow polygons / • Dynamic shadow polygons / ▪ Projected shadows / ▪ Light maps. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Shadow Calculation Methods' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Shadow Calculation Methods'?

### Page 18 - 10.2 Ground Plane Shadows

Source cue: Static and dynamic shadow polygons

Professor-style explanation: The slide '10.2 Ground Plane Shadows' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. The terms describe light-space visibility: Static and dynamic shadow polygons. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image. For examination purposes, the important content is light-space visibility: a point is shadowed because another object blocks the path from the light.

Technical commentary: This slide is about 10.2 Ground Plane Shadows. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The terms describe light-space visibility: Static and dynamic shadow polygons. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for '10.2 Ground Plane Shadows' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in '10.2 Ground Plane Shadows'?

### Page 19 - Static Shadow Polygons

Source cue: ▪ Render dark polygons to represent shadow regions / • Cast ray from light source through center of shadow-casting objects / • Position dark polygon where ray intersects shadow-receiving object / ▪ Disadvantages / • Static shapes cannot represent geometry of dynamic scene objects

Professor-style explanation: The slide 'Static Shadow Polygons' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: ▪ Render dark polygons to represent shadow regions / • Cast ray from light source through center of shadow-casting objects / • Position dark polygon where ray intersects shadow-receiving object / ▪ Disadvantages / • Static shapes cannot represent geometry of dynamic scene objects. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Static Shadow Polygons. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: ▪ Render dark polygons to represent shadow regions / • Cast ray from light source through center of shadow-casting objects / • Position dark polygon where ray intersects shadow-receiving object / ▪ Disadvantages / • Static shapes cannot represent geometry of dynamic scene objects. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Static Shadow Polygons' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Static Shadow Polygons' works per object, per image region, per ray, or per fragment?

### Page 20 - Render Static Shadow Polygons 1/2

Source cue: ▪ Depth value identical with thatof shadow-receiving polygon(care must be taken wrt. z-buffer / fighting) / ▪ Depth value smaller than that of shadow-receiving polygon(shadow can be too large)

Professor-style explanation: The slide 'Render Static Shadow Polygons 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: ▪ Depth value identical with thatof shadow-receiving polygon(care must be taken wrt. z-buffer / fighting) / ▪ Depth value smaller than that of shadow-receiving polygon(shadow can be too large). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Render Static Shadow Polygons 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: ▪ Depth value identical with thatof shadow-receiving polygon(care must be taken wrt. z-buffer / fighting) / ▪ Depth value smaller than that of shadow-receiving polygon(shadow can be too large). Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Render Static Shadow Polygons 1/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Render Static Shadow Polygons 1/2'?

### Page 21 - Render Static Shadow Polygons 2/2

Source cue: ▪ Disable depth test / • Cast ray to determine shadow visibility / • Show entire shadow polygon / ▪ Shadow too large and possibly in wrong places / ▪ Test corners for shadow visibility

Professor-style explanation: The slide 'Render Static Shadow Polygons 2/2' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: ▪ Disable depth test / • Cast ray to determine shadow visibility / • Show entire shadow polygon / ▪ Shadow too large and possibly in wrong places / ▪ Test corners for shadow visibility. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Render Static Shadow Polygons 2/2. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: ▪ Disable depth test / • Cast ray to determine shadow visibility / • Show entire shadow polygon / ▪ Shadow too large and possibly in wrong places / ▪ Test corners for shadow visibility. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Render Static Shadow Polygons 2/2' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Render Static Shadow Polygons 2/2' works per object, per image region, per ray, or per fragment?

### Page 22 - Static Shadow Polygons

Source cue: ▪ Good for car racing games (static scene geometry) / ▪ With fast movements and proximity of casters and receivers,wrong shadows are often not detected / as such

Professor-style explanation: The slide 'Static Shadow Polygons' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. The terms describe light-space visibility: ▪ Good for car racing games (static scene geometry) / ▪ With fast movements and proximity of casters and receivers,wrong shadows are often not detected / as such. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image. For examination purposes, the important content is light-space visibility: a point is shadowed because another object blocks the path from the light.

Technical commentary: This slide is about Static Shadow Polygons. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The terms describe light-space visibility: ▪ Good for car racing games (static scene geometry) / ▪ With fast movements and proximity of casters and receivers,wrong shadows are often not detected / as such. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Static Shadow Polygons' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Static Shadow Polygons'?

### Page 23 - Dynamic Shadow Polygons

Source cue: ▪ Project shadow-casting scene objects onto shadow-receiving objectby modifying shape / ▪ Accurate procedure for semi-transparent shadows,but only if shadows do not overlap / ▪ Restrictions / • Only planar polygons on shadow-receivingscene objects possible / • No self-shadowing possible

Professor-style explanation: The slide 'Dynamic Shadow Polygons' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. The terms describe light-space visibility: ▪ Project shadow-casting scene objects onto shadow-receiving objectby modifying shape / ▪ Accurate procedure for semi-transparent shadows,but only if shadows do not overlap / ▪ Restrictions / • Only planar polygons on shadow-receivingscene objects possible / • No self-shadowing possible. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image. For examination purposes, the important content is light-space visibility: a point is shadowed because another object blocks the path from the light.

Technical commentary: This slide is about Dynamic Shadow Polygons. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The terms describe light-space visibility: ▪ Project shadow-casting scene objects onto shadow-receiving objectby modifying shape / ▪ Accurate procedure for semi-transparent shadows,but only if shadows do not overlap / ▪ Restrictions / • Only planar polygons on shadow-receivingscene objects possible / • No self-shadowing possible. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Dynamic Shadow Polygons' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Dynamic Shadow Polygons'?

### Page 24 - Shadow Projection

Source cue: S L / ▪ Shadow point (= vertex of the shadow polygon) lies on a line between light source and vertex / of shadow-casting scene object / S = P − α ⋅ L / S z = 0 α =

Professor-style explanation: The slide 'Shadow Projection' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: S L / ▪ Shadow point (= vertex of the shadow polygon) lies on a line between light source and vertex / of shadow-casting scene object / S = P − α ⋅ L / S z = 0 α =. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Shadow Projection. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: S L / ▪ Shadow point (= vertex of the shadow polygon) lies on a line between light source and vertex / of shadow-casting scene object / S = P − α ⋅ L / S z = 0 α =. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Shadow Projection' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Shadow Projection'?

### Page 25 - Rendering Dynamic Shadow Polygons

Source cue: ▪ Matrix transforms object into its shadow polygon / ▪ Render scene object with shadows / • Render scene object / • Multiply current model-view -matrix with / • Render scene object in shadow color with b lending

Professor-style explanation: The slide 'Rendering Dynamic Shadow Polygons' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: ▪ Matrix transforms object into its shadow polygon / ▪ Render scene object with shadows / • Render scene object / • Multiply current model-view -matrix with / • Render scene object in shadow color with b lending. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Rendering Dynamic Shadow Polygons. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: ▪ Matrix transforms object into its shadow polygon / ▪ Render scene object with shadows / • Render scene object / • Multiply current model-view -matrix with / • Render scene object in shadow color with b lending. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Rendering Dynamic Shadow Polygons' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Rendering Dynamic Shadow Polygons' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Rendering Dynamic Shadow Polygons'?

### Page 26 - 10.3 Light Maps

Source cue: Structured lighting with textures

Professor-style explanation: The slide '10.3 Light Maps' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: Structured lighting with textures. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about 10.3 Light Maps. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: Structured lighting with textures. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for '10.3 Light Maps' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '10.3 Light Maps'?

### Page 27 - Light Maps

Source cue: ▪ Static shadows can be precomputed and stored in light maps / ▪ When precomputing light maps, shadows are calculated offline(e.g. with ray tracing) / ▪ Soft shadows in lightmaps / • Interpolation of the lightmap creates soft shadow approximations / • Light source sampling results in better results,sending multiple rays to different points of the

Professor-style explanation: The slide 'Light Maps' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: ▪ Static shadows can be precomputed and stored in light maps / ▪ When precomputing light maps, shadows are calculated offline(e.g. with ray tracing) / ▪ Soft shadows in lightmaps / • Interpolation of the lightmap creates soft shadow approximations / • Light source sampling results in better results,sending multiple rays to different points of the. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Light Maps. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: ▪ Static shadows can be precomputed and stored in light maps / ▪ When precomputing light maps, shadows are calculated offline(e.g. with ray tracing) / ▪ Soft shadows in lightmaps / • Interpolation of the lightmap creates soft shadow approximations / • Light source sampling results in better results,sending multiple rays to different points of the. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Light Maps' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Light Maps' works per object, per image region, per ray, or per fragment?

### Page 28 - Soft Shadows with Light Maps 1/2

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Soft Shadows with Light Maps 1/2' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Soft Shadows with Light Maps 1/2. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Soft Shadows with Light Maps 1/2' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Soft Shadows with Light Maps 1/2'?

### Page 29 - Soft Shadows with Light Maps 2/2

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Soft Shadows with Light Maps 2/2' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Soft Shadows with Light Maps 2/2. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Soft Shadows with Light Maps 2/2' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Soft Shadows with Light Maps 2/2'?

### Page 30 - 10.4 Shadow Volumes

Source cue: Representation of shadows by geometry enclosing them

Professor-style explanation: The slide '10.4 Shadow Volumes' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. The terms describe light-space visibility: Representation of shadows by geometry enclosing them. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image. For examination purposes, the important content is light-space visibility: a point is shadowed because another object blocks the path from the light.

Technical commentary: This slide is about 10.4 Shadow Volumes. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The terms describe light-space visibility: Representation of shadows by geometry enclosing them. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for '10.4 Shadow Volumes' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in '10.4 Shadow Volumes'?

### Page 31 - Shadow Volumes

Source cue: ▪ Shadows are considered as volume in space / ▪ Originally developed by Crow in 1977 / ▪ Extension by Brotman and Badler in 1984 / ▪ Heidmann introduced the technology for efficientrendering of shadow volumes in 1991

Professor-style explanation: The slide 'Shadow Volumes' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. The terms describe light-space visibility: ▪ Shadows are considered as volume in space / ▪ Originally developed by Crow in 1977 / ▪ Extension by Brotman and Badler in 1984 / ▪ Heidmann introduced the technology for efficientrendering of shadow volumes in 1991. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image. For examination purposes, the important content is light-space visibility: a point is shadowed because another object blocks the path from the light.

Technical commentary: This slide is about Shadow Volumes. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The terms describe light-space visibility: ▪ Shadows are considered as volume in space / ▪ Originally developed by Crow in 1977 / ▪ Extension by Brotman and Badler in 1984 / ▪ Heidmann introduced the technology for efficientrendering of shadow volumes in 1991. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Shadow Volumes' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Volumes'?

### Page 32 - Initial Considerations

Source cue: ▪ Shadow volume shape depends on shape and positionof light source and shadow-caster / ▪ All points inside shadow volume are shadowed / ▪ Shadow volume generation / • Find silhouettes of shadow-casterregarding light source / • Extrudes silhouettes in light ray directionto create polygons

Professor-style explanation: The slide 'Initial Considerations' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: ▪ Shadow volume shape depends on shape and positionof light source and shadow-caster / ▪ All points inside shadow volume are shadowed / ▪ Shadow volume generation / • Find silhouettes of shadow-casterregarding light source / • Extrudes silhouettes in light ray directionto create polygons. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Initial Considerations. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: ▪ Shadow volume shape depends on shape and positionof light source and shadow-caster / ▪ All points inside shadow volume are shadowed / ▪ Shadow volume generation / • Find silhouettes of shadow-casterregarding light source / • Extrudes silhouettes in light ray directionto create polygons. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Initial Considerations' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Initial Considerations' works per object, per image region, per ray, or per fragment?

### Page 33 - Shadow Volume Geometry

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Shadow Volume Geometry' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Shadow Volume Geometry. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Shadow Volume Geometry' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Volume Geometry'?

### Page 34 - Shadow Volume Realization

Source cue: ▪ Silhouettes edges can be found by analyzing normals / • Silhouette edge lies between front and back face (as seen from light source) / ▪ Silhouette edges are stored as vertex list containing vertices / ▪ For convex shadow-casters / L V

Professor-style explanation: The slide 'Shadow Volume Realization' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: ▪ Silhouettes edges can be found by analyzing normals / • Silhouette edge lies between front and back face (as seen from light source) / ▪ Silhouette edges are stored as vertex list containing vertices / ▪ For convex shadow-casters / L V. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Shadow Volume Realization. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: ▪ Silhouettes edges can be found by analyzing normals / • Silhouette edge lies between front and back face (as seen from light source) / ▪ Silhouette edges are stored as vertex list containing vertices / ▪ For convex shadow-casters / L V. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Shadow Volume Realization' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Shadow Volume Realization'?

### Page 35 - Shadow Volume Properties 1/2

Source cue: ▪ All points inside shadow volume are shadowed / ▪ Shadowing can be determined for each view ray by intersection tests / • Assumption: Camera not in shadow volume / • At each intersection with front-face shadow polygon, intersection counter cnt is incremented / • At each intersection with back-face shadow polygon, intersection counter cnt is decremented

Professor-style explanation: The slide 'Shadow Volume Properties 1/2' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: ▪ All points inside shadow volume are shadowed / ▪ Shadowing can be determined for each view ray by intersection tests / • Assumption: Camera not in shadow volume / • At each intersection with front-face shadow polygon, intersection counter cnt is incremented / • At each intersection with back-face shadow polygon, intersection counter cnt is decremented. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Shadow Volume Properties 1/2. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: ▪ All points inside shadow volume are shadowed / ▪ Shadowing can be determined for each view ray by intersection tests / • Assumption: Camera not in shadow volume / • At each intersection with front-face shadow polygon, intersection counter cnt is incremented / • At each intersection with back-face shadow polygon, intersection counter cnt is decremented. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Shadow Volume Properties 1/2' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Shadow Volume Properties 1/2' works per object, per image region, per ray, or per fragment?

### Page 36 - Shadow Volume Properties 2/2

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Shadow Volume Properties 2/2' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Shadow Volume Properties 2/2. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Shadow Volume Properties 2/2' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Volume Properties 2/2'?

### Page 37 - Stencil Shadow Volume

Source cue: ▪ Generation of shadow volumes per frame / • Works well for scenes with few moving objects / • Expensive for complex shadow volumes / • Improvement by simplifying shadow-casting geometries / ▪ Four rendering passes required

Professor-style explanation: The slide 'Stencil Shadow Volume' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. The terms describe light-space visibility: ▪ Generation of shadow volumes per frame / • Works well for scenes with few moving objects / • Expensive for complex shadow volumes / • Improvement by simplifying shadow-casting geometries / ▪ Four rendering passes required. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image. For examination purposes, the important content is light-space visibility: a point is shadowed because another object blocks the path from the light.

Technical commentary: This slide is about Stencil Shadow Volume. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The terms describe light-space visibility: ▪ Generation of shadow volumes per frame / • Works well for scenes with few moving objects / • Expensive for complex shadow volumes / • Improvement by simplifying shadow-casting geometries / ▪ Four rendering passes required. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Stencil Shadow Volume' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Stencil Shadow Volume'?

### Page 38 - Implementation

Source cue: ▪ Determine visible scene objects / • Render scene without writing in color buffer / ▪ Represent shadow volume in stencil buffer / • Initialize stencil buffer with 0 / • Render front-face shadow polygons and increment stencil buffer by 1

Professor-style explanation: The slide 'Implementation' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: ▪ Determine visible scene objects / • Render scene without writing in color buffer / ▪ Represent shadow volume in stencil buffer / • Initialize stencil buffer with 0 / • Render front-face shadow polygons and increment stencil buffer by 1. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Implementation. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: ▪ Determine visible scene objects / • Render scene without writing in color buffer / ▪ Represent shadow volume in stencil buffer / • Initialize stencil buffer with 0 / • Render front-face shadow polygons and increment stencil buffer by 1. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Implementation' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Implementation'?

### Page 39 - Special Case: COP in the shadows

Source cue: ▪ When COP lies in a shadow volume, the situation can be unclear / • Near - or far -plane can intersect shadow volume / ▪ Possible solutions / s = 0 / • Test COP against all shadow volumes cnt

Professor-style explanation: The slide 'Special Case: COP in the shadows' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. The terms describe light-space visibility: ▪ When COP lies in a shadow volume, the situation can be unclear / • Near - or far -plane can intersect shadow volume / ▪ Possible solutions / s = 0 / • Test COP against all shadow volumes cnt. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image. For examination purposes, the important content is light-space visibility: a point is shadowed because another object blocks the path from the light.

Technical commentary: This slide is about Special Case: COP in the shadows. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The terms describe light-space visibility: ▪ When COP lies in a shadow volume, the situation can be unclear / • Near - or far -plane can intersect shadow volume / ▪ Possible solutions / s = 0 / • Test COP against all shadow volumes cnt. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Special Case: COP in the shadows' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Special Case: COP in the shadows'?

### Page 40 - Shadow Volume Example

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Shadow Volume Example' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Shadow Volume Example. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Shadow Volume Example' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Shadow Volume Example'?

### Page 41 - Shadow Volume Conclusions

Source cue: ▪ Advantages / • Shadow-casting and shadow-receiving objects can have arbitrary shapes / • Applicable for multiple light sources / • Level-of-detail adaptable through approximated geometries / • Shadow volumes for static pairs of objects and lights can be precalculated

Professor-style explanation: The slide 'Shadow Volume Conclusions' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: ▪ Advantages / • Shadow-casting and shadow-receiving objects can have arbitrary shapes / • Applicable for multiple light sources / • Level-of-detail adaptable through approximated geometries / • Shadow volumes for static pairs of objects and lights can be precalculated. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Shadow Volume Conclusions. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: ▪ Advantages / • Shadow-casting and shadow-receiving objects can have arbitrary shapes / • Applicable for multiple light sources / • Level-of-detail adaptable through approximated geometries / • Shadow volumes for static pairs of objects and lights can be precalculated. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Shadow Volume Conclusions' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Shadow Volume Conclusions'?

### Page 42 - 10.5 Shadow Maps

Source cue: Depth test from the point of view of the light source

Professor-style explanation: The slide '10.5 Shadow Maps' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: Depth test from the point of view of the light source. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about 10.5 Shadow Maps. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: Depth test from the point of view of the light source. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for '10.5 Shadow Maps' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether '10.5 Shadow Maps' works per object, per image region, per ray, or per fragment?

### Page 43 - Shadow Mapping

Source cue: ▪ Based on z-Buffer (contains depth relative to the light source) / ▪ First used within Pixar's Renderman

Professor-style explanation: The slide 'Shadow Mapping' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: ▪ Based on z-Buffer (contains depth relative to the light source) / ▪ First used within Pixar's Renderman. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Shadow Mapping. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: ▪ Based on z-Buffer (contains depth relative to the light source) / ▪ First used within Pixar's Renderman. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Shadow Mapping' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Shadow Mapping'?

### Page 44 - Projected Shadows

Source cue: ▪ depth texture / ▪ Rendering algorithm / • Render shadow-casting objectsas seen from the light source into depth texture / • Project depth texture using projective texturingwhen rendering shadow-receiving objects / ▪ Characteristics of the process

Professor-style explanation: The slide 'Projected Shadows' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: ▪ depth texture / ▪ Rendering algorithm / • Render shadow-casting objectsas seen from the light source into depth texture / • Project depth texture using projective texturingwhen rendering shadow-receiving objects / ▪ Characteristics of the process. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Projected Shadows. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: ▪ depth texture / ▪ Rendering algorithm / • Render shadow-casting objectsas seen from the light source into depth texture / • Project depth texture using projective texturingwhen rendering shadow-receiving objects / ▪ Characteristics of the process. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Projected Shadows' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Projected Shadows' works per object, per image region, per ray, or per fragment?

### Page 45 - Visual or title slide

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Visual or title slide' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Visual or title slide. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer links this visual or title page to the closest surrounding concept slide and names the topic transition it introduces.

Common trap: Do not invent details that are not visible in the extracted text; use this page as a boundary marker and rely on adjacent slides for technical content.

Check yourself: Can you turn 'Visual or title slide' into a causal sentence instead of repeating the slide title?

### Page 46 - Depth Comparison

Source cue: ▪ For each vertex in world coordinates determine associated depth value in shadow map / • Transform into camera's eye space / • Use light source's 4x4 transformation matrix to transform into light's clip space / • Compare depth value with associated depth value in shadow map

Professor-style explanation: The slide 'Depth Comparison' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: ▪ For each vertex in world coordinates determine associated depth value in shadow map / • Transform into camera's eye space / • Use light source's 4x4 transformation matrix to transform into light's clip space / • Compare depth value with associated depth value in shadow map. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Depth Comparison. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: ▪ For each vertex in world coordinates determine associated depth value in shadow map / • Transform into camera's eye space / • Use light source's 4x4 transformation matrix to transform into light's clip space / • Compare depth value with associated depth value in shadow map. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Depth Comparison' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Depth Comparison' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Depth Comparison'?

### Page 47 - Coordinate Systems

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Coordinate Systems' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Coordinate Systems. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Coordinate Systems' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Coordinate Systems' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Coordinate Systems'?

### Page 48 - Pseudo Code

Source cue: // generate shadow map w.r.t light source / generateShadowMap(); / // render scene from COP / for all rasterized fragments do { / Transform fragment xyz into lights coordinate system

Professor-style explanation: The slide 'Pseudo Code' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. The terms describe a coordinate-space conversion: // generate shadow map w.r.t light source / generateShadowMap(); / // render scene from COP / for all rasterized fragments do { / Transform fragment xyz into lights coordinate system. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. A formula is only meaningful after the two coordinate spaces around it are clear. For examination purposes, the important content is space awareness: name the source space, the matrix operation, and the target space before applying any formula.

Technical commentary: This slide is about Pseudo Code. The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations. The terms describe a coordinate-space conversion: // generate shadow map w.r.t light source / generateShadowMap(); / // render scene from COP / for all rasterized fragments do { / Transform fragment xyz into lights coordinate system. Input positions or vectors are transformed by matrices so the same object can be expressed in model, world, view, or clip space.

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Exam-grade answer: A strong answer for 'Pseudo Code' names source space, target space, the transformation type, and whether the object is a point, direction vector, normal, or coordinate frame.

Common trap: Do not multiply matrices mechanically in 'Pseudo Code' without naming coordinate spaces and order of operations.

Check yourself: Can you state the coordinate space before and after 'Pseudo Code'?

### Page 49 - Properties

Source cue: ▪ Shadow maps are static when scene and lighting are static / ▪ Shadow quality depends on shadow map resolution / ▪ Shadow mapping has three main problems / • View volume problem / • Bias problem

Professor-style explanation: The slide 'Properties' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: ▪ Shadow maps are static when scene and lighting are static / ▪ Shadow quality depends on shadow map resolution / ▪ Shadow mapping has three main problems / • View volume problem / • Bias problem. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Properties. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: ▪ Shadow maps are static when scene and lighting are static / ▪ Shadow quality depends on shadow map resolution / ▪ Shadow mapping has three main problems / • View volume problem / • Bias problem. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Properties' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Properties'?

### Page 50 - View Volume Problem

Source cue: ▪ When vertex lies outside light source's view volume,required depth information is missing / ▪ Possible remedies / • Use cubic shadow map (similar to cubic environment map) / • Use only spotlights

Professor-style explanation: The slide 'View Volume Problem' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: ▪ When vertex lies outside light source's view volume,required depth information is missing / ▪ Possible remedies / • Use cubic shadow map (similar to cubic environment map) / • Use only spotlights. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about View Volume Problem. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: ▪ When vertex lies outside light source's view volume,required depth information is missing / ▪ Possible remedies / • Use cubic shadow map (similar to cubic environment map) / • Use only spotlights. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'View Volume Problem' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'View Volume Problem' works per object, per image region, per ray, or per fragment?

### Page 51 - Bias Problem 1/2

Source cue: Incorrect self-shadowing occurs for / all fragments with ShadowMap(x',y') ≈ z' / Can be corrected by / increasing depth precision of z-buffer / applying z-bias

Professor-style explanation: The slide 'Bias Problem 1/2' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. The terms connect CPU-side API control with GPU execution: Incorrect self-shadowing occurs for / all fragments with ShadowMap(x',y') ≈ z' / Can be corrected by / increasing depth precision of z-buffer / applying z-bias. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image. For examination purposes, the important content is state plus binding plus shader interface: OpenGL draws from the currently bound objects and active settings.

Technical commentary: This slide is about Bias Problem 1/2. The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time. The terms connect CPU-side API control with GPU execution: Incorrect self-shadowing occurs for / all fragments with ShadowMap(x',y') ≈ z' / Can be corrected by / increasing depth precision of z-buffer / applying z-bias. Objects, bindings, shader interfaces, buffers, and framebuffer state determine what data is processed and where results are written.

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Exam-grade answer: A strong answer for 'Bias Problem 1/2' names the OpenGL object or state involved, where the data lives, which shader or pipeline stage consumes it, and how a wrong binding would show up visually.

Common trap: Do not assume an OpenGL call is enough by itself; the result depends on the complete active context state and currently bound resources.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Bias Problem 1/2'?

### Page 52 - Bias Problem 2/2

Source cue: It is difficult to choose a good z-bias / ShadowMap(x',y') + bias ? / ▪ good / ▪ too low / ▪ too high

Professor-style explanation: The slide 'Bias Problem 2/2' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. The terms describe light-space visibility: It is difficult to choose a good z-bias / ShadowMap(x',y') + bias ? / ▪ good / ▪ too low / ▪ too high. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image. For examination purposes, the important content is light-space visibility: a point is shadowed because another object blocks the path from the light.

Technical commentary: This slide is about Bias Problem 2/2. The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation. The terms describe light-space visibility: It is difficult to choose a good z-bias / ShadowMap(x',y') + bias ? / ▪ good / ▪ too low / ▪ too high. A light, an occluder, a receiver, and a stored or computed visibility representation determine where illumination is blocked.

Why it matters: Shadow algorithms reuse visibility ideas, but from the light's point of view.

Exam-grade answer: A strong answer for 'Bias Problem 2/2' names the light, blocker, receiver, visibility representation, and the reason a region receives reduced direct illumination.

Common trap: Do not explain a shadow only from the camera view; the key visibility test is usually from the light's point of view.

Check yourself: Can you explain what the light can or cannot see in 'Bias Problem 2/2'?

### Page 53 - Aliasing Problem 1/3

Source cue: ▪ Aliasing occurs when shadow map is undersampled(i.e., a texel in shadow map covers several / pixels) / ▪ Particularly bad when camera and light source are facing each other

Professor-style explanation: The slide 'Aliasing Problem 1/3' explains how camera geometry turns a 3D scene into image coordinates. In view space, objects are described relative to the camera. The projection matrix then maps that camera-centered geometry into clip space, where the viewing volume and clipping boundaries can be handled consistently. Perspective projection uses the homogeneous coordinate so that the later divide by w creates foreshortening: farther objects occupy less image space. Orthographic projection removes that depth-based size change and keeps parallel structures visually parallel. The terms describe camera-to-screen mapping: ▪ Aliasing occurs when shadow map is undersampled(i.e., a texel in shadow map covers several / pixels) / ▪ Particularly bad when camera and light source are facing each other. View-space geometry is mapped by a projection matrix, clipped, divided into normalized coordinates, and finally mapped to a viewport. The object chain is view-space position, projection matrix, clip coordinate, normalized device coordinate, and viewport coordinate. The slide is therefore connecting camera setup, visual appearance, and the numeric coordinate pipeline that rasterization later consumes. For examination purposes, the important content is the camera-to-screen chain: view coordinates, projection matrix, clip coordinates, perspective divide, normalized device coordinates, and viewport mapping.

Technical commentary: This slide is about Aliasing Problem 1/3. The projection objects on the slide convert view-space geometry into clip coordinates, normalized coordinates, and finally screen-related positions. The terms describe camera-to-screen mapping: ▪ Aliasing occurs when shadow map is undersampled(i.e., a texel in shadow map covers several / pixels) / ▪ Particularly bad when camera and light source are facing each other. View-space geometry is mapped by a projection matrix, clipped, divided into normalized coordinates, and finally mapped to a viewport.

Why it matters: Projection controls both image composition and depth precision, so it affects visibility and rasterization later.

Exam-grade answer: A strong answer for 'Aliasing Problem 1/3' explains the mapping from view space through clip space and perspective divide to normalized and viewport coordinates.

Common trap: Do not confuse projection with viewport mapping; projection creates clip coordinates and the perspective divide comes before final screen mapping.

Check yourself: Can you explain how 'Aliasing Problem 1/3' changes positions before rasterization?

### Page 54 - Aliasing Problem 2/3

Source cue: ▪ Filter (= weighted average formation over neighbors) of a depth valuedoes not make sense / ▪ Percentage Closest Filtering (PCF) / • Filter results of shadow tests (weighted average of comparison results) / • Bias selection is made even more difficult / ▪ Choosing the filter kernel

Professor-style explanation: The slide 'Aliasing Problem 2/3' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: ▪ Filter (= weighted average formation over neighbors) of a depth valuedoes not make sense / ▪ Percentage Closest Filtering (PCF) / • Filter results of shadow tests (weighted average of comparison results) / • Bias selection is made even more difficult / ▪ Choosing the filter kernel. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Aliasing Problem 2/3. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: ▪ Filter (= weighted average formation over neighbors) of a depth valuedoes not make sense / ▪ Percentage Closest Filtering (PCF) / • Filter results of shadow tests (weighted average of comparison results) / • Bias selection is made even more difficult / ▪ Choosing the filter kernel. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Aliasing Problem 2/3' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Aliasing Problem 2/3' works per object, per image region, per ray, or per fragment?

### Page 55 - Visual or title slide

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Visual or title slide' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Visual or title slide. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer links this visual or title page to the closest surrounding concept slide and names the topic transition it introduces.

Common trap: Do not invent details that are not visible in the extracted text; use this page as a boundary marker and rely on adjacent slides for technical content.

Check yourself: Can you turn 'Visual or title slide' into a causal sentence instead of repeating the slide title?

### Page 56 - Aliasing Problem 3/3

Source cue: ▪ Averaging Filter / ▪ Percentage Closest Filtering

Professor-style explanation: The slide 'Aliasing Problem 3/3' explains textures as sampled data fields used during shading. A texture is not only a picture; it is a structured array of texels that can store color, normals, depth, material values, environment data, or volume data. A fragment supplies texture coordinates, the texture object supplies stored samples, sampler state controls wrapping and filtering, and the shader decides what the fetched value means. The terms describe sampled data access: ▪ Averaging Filter / ▪ Percentage Closest Filtering. Coordinates select texels, sampler state controls reconstruction, and the shader interprets the fetched value as color, normal, material, or other data. The object-level relation is coordinate, texture memory, sampling rule, and shader interpretation. This relation explains why texture bugs often look visual but originate from data addressing, filtering state, mipmap completeness, or a mismatch between stored values and shader expectations. For examination purposes, the important content is coordinate-driven lookup: texture coordinates select stored texels, sampler state reconstructs values, and the shader interprets the result.

Technical commentary: This slide is about Aliasing Problem 3/3. The texturing objects on the slide define sampled data, coordinates, filtering rules, mip levels, and shader interpretation of fetched values. The terms describe sampled data access: ▪ Averaging Filter / ▪ Percentage Closest Filtering. Coordinates select texels, sampler state controls reconstruction, and the shader interprets the fetched value as color, normal, material, or other data.

Why it matters: Texture sampling is a major source of visual detail and a common source of artifacts.

Exam-grade answer: A strong answer for 'Aliasing Problem 3/3' names the texture data, texture coordinates, filtering or wrapping state, and shader interpretation of the sampled value.

Common trap: Do not reduce texturing to 'putting an image on an object'; coordinates, sampler state, mipmaps, and shader meaning are part of the concept.

Check yourself: Can you identify the sampled data, coordinate, and filtering/state issue in 'Aliasing Problem 3/3'?

### Page 57 - Visual or title slide

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Visual or title slide' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Visual or title slide. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer links this visual or title page to the closest surrounding concept slide and names the topic transition it introduces.

Common trap: Do not invent details that are not visible in the extracted text; use this page as a boundary marker and rely on adjacent slides for technical content.

Check yourself: Can you turn 'Visual or title slide' into a causal sentence instead of repeating the slide title?

### Page 58 - ▪ Shadows in Visual Perception

Source cue: • Enhance depth perception and object relationships / • Create appealing visual effects and atmosphere / ▪ Shadow Definitions and Types / • Shadow-casting (Occluder) vs. shadow-receiving (Receiver) objects / • Self-shadowing: Same object casts and receives shadow

Professor-style explanation: The slide '▪ Shadows in Visual Perception' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: • Enhance depth perception and object relationships / • Create appealing visual effects and atmosphere / ▪ Shadow Definitions and Types / • Shadow-casting (Occluder) vs. shadow-receiving (Receiver) objects / • Self-shadowing: Same object casts and receives shadow. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about ▪ Shadows in Visual Perception. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: • Enhance depth perception and object relationships / • Create appealing visual effects and atmosphere / ▪ Shadow Definitions and Types / • Shadow-casting (Occluder) vs. shadow-receiving (Receiver) objects / • Self-shadowing: Same object casts and receives shadow. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for '▪ Shadows in Visual Perception' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether '▪ Shadows in Visual Perception' works per object, per image region, per ray, or per fragment?

### Page 59 - Literature and other sources used in this chapter

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Literature and other sources used in this chapter' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Literature and other sources used in this chapter. The slide lists source material or chapter references that support the technical content and give names for further reading. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Reference slides provide the source trail for definitions, algorithms, and deeper explanations.

Exam-grade answer: A strong answer for 'Literature and other sources used in this chapter' identifies what kind of source is listed and which course concept or algorithm that source supports.

Common trap: Do not skip 'Literature and other sources used in this chapter' if it names a standard algorithm or source that defines terminology used later in the chapter.

Check yourself: Can you identify which source or topic 'Literature and other sources used in this chapter' points to for deeper study?

### Page 60 - ▪ Text Books

Source cue: • P. Shirley, M. AshikhminS. Marschner: Fundamentals of Computer Graphics (3rd ed. Edition), AK / ▪ Research Publications / • Crow, F., Shadows Algorithms for Computers Graphics, SIGGRAPH 1977. / • Lance Williams: Casting curved shadows on curved surfaces, SIGGRAPH 1978.

Professor-style explanation: The slide '▪ Text Books' collects the source material behind the chapter. References are not rendering objects themselves, but they identify the books, papers, or external resources from which the lecture's terminology and algorithms are drawn. The listed sources support the chapter content: • P. Shirley, M. AshikhminS. Marschner: Fundamentals of Computer Graphics (3rd ed. Edition), AK / ▪ Research Publications / • Crow, F., Shadows Algorithms for Computers Graphics, SIGGRAPH 1977. / • Lance Williams: Casting curved shadows on curved surfaces, SIGGRAPH 1978. They point to the books, papers, or resources behind the definitions and algorithms used in the lecture. In practical terms, a reference slide marks the boundary of the chapter and tells us where the formal definitions, derivations, or extended examples can be found if a topic needs more depth than the lecture slides provide. For examination purposes, the important content is source attribution and vocabulary: references tell where precise definitions and standard algorithms come from.

Technical commentary: This slide is about ▪ Text Books. The slide lists source material or chapter references that support the technical content and give names for further reading. The listed sources support the chapter content: • P. Shirley, M. AshikhminS. Marschner: Fundamentals of Computer Graphics (3rd ed. Edition), AK / ▪ Research Publications / • Crow, F., Shadows Algorithms for Computers Graphics, SIGGRAPH 1977. / • Lance Williams: Casting curved shadows on curved surfaces, SIGGRAPH 1978. They point to the books, papers, or resources behind the definitions and algorithms used in the lecture.

Why it matters: Reference slides provide the source trail for definitions, algorithms, and deeper explanations.

Exam-grade answer: A strong answer for '▪ Text Books' identifies what kind of source is listed and which course concept or algorithm that source supports.

Common trap: Do not skip '▪ Text Books' if it names a standard algorithm or source that defines terminology used later in the chapter.

Check yourself: Can you identify which source or topic '▪ Text Books' points to for deeper study?

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
