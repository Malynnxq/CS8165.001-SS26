# Lecture 08 - Local Illumination

Source chunk: `course_text_parts/03_lectures/08_local-illumination.txt`
Extracted slide pages in source chunk: 62


## Big Picture

This lecture explains how visible surface points receive color from local light, material, normal, and view information. It is about shading a point, not solving all global light transport.

## Per-Slide Commentary


### Page 1 - Visual or title slide

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Visual or title slide' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Visual or title slide. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer links this visual or title page to the closest surrounding concept slide and names the topic transition it introduces.


Check yourself: Can you turn 'Visual or title slide' into a causal sentence instead of repeating the slide title?

### Page 2 - Local Illumination

Source cue: - Illumination is the process of simulating light interactions in a virtual scene / - Requires light and material properties / - Achieved through illumination model / - Essential for scene perception / without iIllumination with illumination

Professor-style explanation: The slide 'Local Illumination' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Illumination is the process of simulating light interactions in a virtual scene / - Requires light and material properties / - Achieved through illumination model / - Essential for scene perception / without iIllumination with illumination. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Local Illumination. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Illumination is the process of simulating light interactions in a virtual scene / - Requires light and material properties / - Achieved through illumination model / - Essential for scene perception / without iIllumination with illumination. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Local Illumination' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Local Illumination'?

### Page 3 - 8.1 Physics of Light

Source cue: 8.2 Light Sources / 8.3 Material Models / 8.4 Phong Illumination Model / 8.5 Shading

Professor-style explanation: The outline '8.1 Physics of Light' gives the lecture its internal logic. The listed topics are the objects that will be connected during the chapter: first the problem space, then the mathematical or algorithmic tools, then the implementation consequences. The listed entries form a dependency order: 8.2 Light Sources / 8.3 Material Models / 8.4 Phong Illumination Model / 8.5 Shading. Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary. The order matters because later items rely on earlier definitions. For example, an OpenGL mechanism is much easier to understand once the corresponding pipeline object or mathematical operation has already been introduced. The outline is therefore a compact dependency graph of the lecture rather than a collection of isolated labels. For examination purposes, the important content is the dependency structure: which concept introduces the vocabulary, which later algorithm uses it, and which implementation problem it solves.

Technical commentary: This slide is about 8.1 Physics of Light. The listed items define the lecture sequence: the topic begins with a problem statement, introduces the required objects or algorithms, and then connects them to rendering or implementation consequences. The listed entries form a dependency order: 8.2 Light Sources / 8.3 Material Models / 8.4 Phong Illumination Model / 8.5 Shading. Earlier entries introduce the vocabulary and problem setting; later entries build algorithms, API details, or consequences on top of that vocabulary.

Why it matters: Outlines tell you the dependency order. They are the safest way to avoid learning isolated bullet points.

Exam-grade answer: A strong answer for '8.1 Physics of Light' names the topics in order and explains at least one dependency between an earlier item and a later item.

Common trap: Do not memorize '8.1 Physics of Light' as a list of headings only; the exam-relevant part is how the headings depend on each other.

Check yourself: Can you explain where '8.1 Physics of Light' fits in the lecture order and what later section depends on it?

### Page 4 - 8.1 Physics of Light

Source cue: Understanding light in the real world

Professor-style explanation: The slide '8.1 Physics of Light' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: Understanding light in the real world. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about 8.1 Physics of Light. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: Understanding light in the real world. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for '8.1 Physics of Light' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '8.1 Physics of Light'?

### Page 5 - Electromagnetic Radiation

Source cue: - Electromagnetic radiation is defined by a spectrum of wavelengths / Wave length λ / - Visible light is subset of electromagnetic spectrum between 400 and 700nm, / which humans perceive as colors

Professor-style explanation: The slide 'Electromagnetic Radiation' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Electromagnetic radiation is defined by a spectrum of wavelengths / Wave length λ / - Visible light is subset of electromagnetic spectrum between 400 and 700nm, / which humans perceive as colors. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Electromagnetic Radiation. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Electromagnetic radiation is defined by a spectrum of wavelengths / Wave length λ / - Visible light is subset of electromagnetic spectrum between 400 and 700nm, / which humans perceive as colors. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Electromagnetic Radiation' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Electromagnetic Radiation'?

### Page 6 - Visible Light

Source cue: 1000 nm / Infrared / Radio / 700 nm / TV Red

Professor-style explanation: The slide 'Visible Light' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: 1000 nm / Infrared / Radio / 700 nm / TV Red. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Visible Light. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: 1000 nm / Infrared / Radio / 700 nm / TV Red. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Visible Light' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Visible Light'?

### Page 7 - Visible Light

Source cue: 1000 nm / Infrared / Radio / 700 nm / TV Red

Professor-style explanation: The slide 'Visible Light' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: 1000 nm / Infrared / Radio / 700 nm / TV Red. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Visible Light. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: 1000 nm / Infrared / Radio / 700 nm / TV Red. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Visible Light' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Visible Light'?

### Page 8 - Light Spectra

Source cue: - Different light sources have different light spectra / - Intensity differs based on wavelength in visible spectrum / [http://www.micro.magnet.fsu.edu/optics/lightandcolor/sources.html]

Professor-style explanation: The slide 'Light Spectra' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Different light sources have different light spectra / - Intensity differs based on wavelength in visible spectrum / [http://www.micro.magnet.fsu.edu/optics/lightandcolor/sources.html]. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Light Spectra. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Different light sources have different light spectra / - Intensity differs based on wavelength in visible spectrum / [http://www.micro.magnet.fsu.edu/optics/lightandcolor/sources.html]. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Light Spectra' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Spectra'?

### Page 9 - Black-Body Radiation

Source cue: - A continuous spectrum emitted by a black body at a certain temperature / Steel / > 1570 K / 820 K / Stars

Professor-style explanation: The slide 'Black-Body Radiation' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - A continuous spectrum emitted by a black body at a certain temperature / Steel / > 1570 K / 820 K / Stars. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Black-Body Radiation. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - A continuous spectrum emitted by a black body at a certain temperature / Steel / > 1570 K / 820 K / Stars. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Black-Body Radiation' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Black-Body Radiation' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Black-Body Radiation' into a causal sentence instead of repeating the slide title?

### Page 10 - Black-Body Radiation

Source cue: Stars / https://www.tec-science.com/thermodynamics/temperature/black-body-radiation/ 23/06/2026 10

Professor-style explanation: The slide 'Black-Body Radiation' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: Stars / https://www.tec-science.com/thermodynamics/temperature/black-body-radiation/ 23/06/2026 10. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Black-Body Radiation. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: Stars / https://www.tec-science.com/thermodynamics/temperature/black-body-radiation/ 23/06/2026 10. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Black-Body Radiation' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Black-Body Radiation' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Black-Body Radiation' into a causal sentence instead of repeating the slide title?

### Page 11 - Spectral Density Function (SDF)

Source cue: - Light spectra are represented as spectral density functions / - Spectral density functions provide the light intensity (=energy) per wavelength / 400 Wavelength λ (nm) 700 / ygrenE / 400 Wavelength λ (nm) 700

Professor-style explanation: The slide 'Spectral Density Function (SDF)' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Light spectra are represented as spectral density functions / - Spectral density functions provide the light intensity (=energy) per wavelength / 400 Wavelength λ (nm) 700 / ygrenE / 400 Wavelength λ (nm) 700. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Spectral Density Function (SDF). The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Light spectra are represented as spectral density functions / - Spectral density functions provide the light intensity (=energy) per wavelength / 400 Wavelength λ (nm) 700 / ygrenE / 400 Wavelength λ (nm) 700. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Spectral Density Function (SDF)' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Spectral Density Function (SDF)'?

### Page 12 - Light Perception

Source cue: - Humans perceive light spectra / as differently colored lights / - Often described using three / main properties (HSL/HSV model) / - Hue - primary color tone

Professor-style explanation: The slide 'Light Perception' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Humans perceive light spectra / as differently colored lights / - Often described using three / main properties (HSL/HSV model) / - Hue - primary color tone. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Light Perception. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Humans perceive light spectra / as differently colored lights / - Often described using three / main properties (HSL/HSV model) / - Hue - primary color tone. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Light Perception' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Perception'?

### Page 13 - Interpreting SDFs

Source cue: - Shape of an SDF depicts how humans perceive represented light / - Hue: dominant wavelength / - Saturation: % of energy in dom. wavelength / - Luminance: total energy (SDF integral) / 400 Wavelength λ (nm) 700

Professor-style explanation: The slide 'Interpreting SDFs' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Shape of an SDF depicts how humans perceive represented light / - Hue: dominant wavelength / - Saturation: % of energy in dom. wavelength / - Luminance: total energy (SDF integral) / 400 Wavelength λ (nm) 700. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Interpreting SDFs. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Shape of an SDF depicts how humans perceive represented light / - Hue: dominant wavelength / - Saturation: % of energy in dom. wavelength / - Luminance: total energy (SDF integral) / 400 Wavelength λ (nm) 700. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Interpreting SDFs' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Interpreting SDFs'?

### Page 14 - Representing SDFs

Source cue: - In spectral rendering SDFs are discretized as arrays / - Cell number represents differentiable wavelength ranges / - Cell values represent energy per wavelength range / - Much more frequently SDFs are represented as three-channel color / - HSL values are derived from SDF

Professor-style explanation: The slide 'Representing SDFs' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - In spectral rendering SDFs are discretized as arrays / - Cell number represents differentiable wavelength ranges / - Cell values represent energy per wavelength range / - Much more frequently SDFs are represented as three-channel color / - HSL values are derived from SDF. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Representing SDFs. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - In spectral rendering SDFs are discretized as arrays / - Cell number represents differentiable wavelength ranges / - Cell values represent energy per wavelength range / - Much more frequently SDFs are represented as three-channel color / - HSL values are derived from SDF. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Representing SDFs' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Representing SDFs' works per object, per image region, per ray, or per fragment?

### Page 15 - 8.2 Light Sources

Source cue: How to represent light sources in computer graphics

Professor-style explanation: The slide '8.2 Light Sources' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: How to represent light sources in computer graphics. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about 8.2 Light Sources. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: How to represent light sources in computer graphics. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for '8.2 Light Sources' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '8.2 Light Sources'?

### Page 16 - Light Sources

Source cue: - All light sources have a RGB color property representing their SDF / - Light sources are also defined through their location, orientation and extent / within a virtual scene / - Different light source types omit different spatial properties / - Light sources have no associated geometry

Professor-style explanation: The slide 'Light Sources' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - All light sources have a RGB color property representing their SDF / - Light sources are also defined through their location, orientation and extent / within a virtual scene / - Different light source types omit different spatial properties / - Light sources have no associated geometry. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Light Sources. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - All light sources have a RGB color property representing their SDF / - Light sources are also defined through their location, orientation and extent / within a virtual scene / - Different light source types omit different spatial properties / - Light sources have no associated geometry. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Light Sources' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Sources'?

### Page 17 - Point Light Sources

Source cue: - Point light sources L = P, C have a geometric center P = (x, y, z) / and radiate light with color C = (R, G, B) evenly in all directions

Professor-style explanation: The slide 'Point Light Sources' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Point light sources L = P, C have a geometric center P = (x, y, z) / and radiate light with color C = (R, G, B) evenly in all directions. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Point Light Sources. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Point light sources L = P, C have a geometric center P = (x, y, z) / and radiate light with color C = (R, G, B) evenly in all directions. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Point Light Sources' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Point Light Sources'?

### Page 18 - Cone Light Sources

Source cue: - Special point light source with geometric center / - Radiation of light restricted to a cone-shaped area with its tip in the center / - Specified by cut-off angle and exponents for the decrease / of brightness with distance to the center / (spot light exponent)

Professor-style explanation: The slide 'Cone Light Sources' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Special point light source with geometric center / - Radiation of light restricted to a cone-shaped area with its tip in the center / - Specified by cut-off angle and exponents for the decrease / of brightness with distance to the center / (spot light exponent). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Cone Light Sources. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Special point light source with geometric center / - Radiation of light restricted to a cone-shaped area with its tip in the center / - Specified by cut-off angle and exponents for the decrease / of brightness with distance to the center / (spot light exponent). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Cone Light Sources' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Cone Light Sources'?

### Page 19 - Light Attenuation

Source cue: - Light attenuation is inversely proportional to the square / of the distance d between the light source and the object / - Attenuation factor / f = min , 1 / att c + c ⋅ d + c ⋅ d2

Professor-style explanation: The slide 'Light Attenuation' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Light attenuation is inversely proportional to the square / of the distance d between the light source and the object / - Attenuation factor / f = min , 1 / att c + c ⋅ d + c ⋅ d2. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Light Attenuation. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Light attenuation is inversely proportional to the square / of the distance d between the light source and the object / - Attenuation factor / f = min , 1 / att c + c ⋅ d + c ⋅ d2. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Light Attenuation' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Attenuation'?

### Page 20 - Area Light Sources

Source cue: - Light source with geometric center and geometric extension / - Mostly of planar shape / - Transmission of light over the entire surface analogous to a point light source

Professor-style explanation: The slide 'Area Light Sources' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Light source with geometric center and geometric extension / - Mostly of planar shape / - Transmission of light over the entire surface analogous to a point light source. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Area Light Sources. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Light source with geometric center and geometric extension / - Mostly of planar shape / - Transmission of light over the entire surface analogous to a point light source. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Area Light Sources' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Area Light Sources'?

### Page 21 - Directed Light

Source cue: - Infinity-far away imaginary light source / - Light rays run parallel and evenly throughout the scene, / direction is specified as a vector / - Light intensity does not diminish / with increasing distance

Professor-style explanation: The slide 'Directed Light' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Infinity-far away imaginary light source / - Light rays run parallel and evenly throughout the scene, / direction is specified as a vector / - Light intensity does not diminish / with increasing distance. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Directed Light. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Infinity-far away imaginary light source / - Light rays run parallel and evenly throughout the scene, / direction is specified as a vector / - Light intensity does not diminish / with increasing distance. Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Directed Light' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Directed Light' works per object, per image region, per ray, or per fragment?

### Page 22 - Local vs. Gobal Illumination

Source cue: - Simple case: Local lighting / - Consideration of direct illumination by light sources / (without obstacles or reflection) / - Simplified light models approximate / real lighting effect

Professor-style explanation: The slide 'Local vs. Gobal Illumination' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Simple case: Local lighting / - Consideration of direct illumination by light sources / (without obstacles or reflection) / - Simplified light models approximate / real lighting effect. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Local vs. Gobal Illumination. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Simple case: Local lighting / - Consideration of direct illumination by light sources / (without obstacles or reflection) / - Simplified light models approximate / real lighting effect. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Local vs. Gobal Illumination' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Local vs. Gobal Illumination'?

### Page 23 - Ambient Light

Source cue: - Undirected light rays, evenly distributed / - Light intensity constant, regardless of distance / - Simulates general room brightness (basic brightness)

Professor-style explanation: The slide 'Ambient Light' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. The terms describe an occlusion test: - Undirected light rays, evenly distributed / - Light intensity constant, regardless of distance / - Simulates general room brightness (basic brightness). Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing. For examination purposes, the important content is the comparison rule: which candidate is visible according to depth, ordering, image subdivision, or ray intersection.

Technical commentary: This slide is about Ambient Light. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. The terms describe an occlusion test: - Undirected light rays, evenly distributed / - Light intensity constant, regardless of distance / - Simulates general room brightness (basic brightness). Candidate surfaces or ray hits are compared so the renderer can decide which object is actually visible from the current viewpoint.

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Exam-grade answer: A strong answer for 'Ambient Light' identifies the competing candidates, the space in which the algorithm works, and the rule that selects the visible result.

Common trap: Do not assume the first generated primitive is visible; visibility requires an ordering, depth, region, or ray comparison.

Check yourself: Can you decide whether 'Ambient Light' works per object, per image region, per ray, or per fragment?

### Page 24 - 8.3 Material Models

Source cue: How to represent materials in computer graphics

Professor-style explanation: The slide '8.3 Material Models' explains how scene objects exist before they are rendered. A 3D model is not an image yet; it is a structured description of geometry and attributes. The central objects are vertices, edges, faces, triangles or other primitives, and sometimes additional data such as normals, texture coordinates, colors, materials, or connectivity. The terms describe model representation before rendering: How to represent materials in computer graphics. Geometric primitives define shape, vertices provide positions and attributes, and later pipeline stages transform, project, rasterize, and shade that representation. This matters because the rendering pipeline needs this representation as input. The model describes what exists in the scene, while later stages decide where it appears, which parts are visible, how it is sampled into fragments, and how it is shaded into final pixel colors. For examination purposes, the important content is that models are structured causes of images, not images themselves; positions, topology, attributes, and materials become input for later rendering stages.

Technical commentary: This slide is about 8.3 Material Models. The slide describes scene objects before rendering: geometric models, primitives, vertices, topology, attributes, and the representation used as input to the pipeline. The terms describe model representation before rendering: How to represent materials in computer graphics. Geometric primitives define shape, vertices provide positions and attributes, and later pipeline stages transform, project, rasterize, and shade that representation.

Why it matters: Model slides explain the input objects that later transformations, projection, rasterization, and shading operate on.

Exam-grade answer: A strong answer for '8.3 Material Models' distinguishes model data from rendered image data and names the geometric or attribute data that later pipeline stages consume.

Common trap: Do not describe '8.3 Material Models' as if the model were already a pixel image; a model is data that still needs transformation, visibility, and shading.

Check yourself: Can you name the geometric objects and attributes represented by '8.3 Material Models' before rendering begins?

### Page 25 - Material Models

Source cue: - Material models capture the different properties of materials / - Materials can have a wide variety of appearances / - Different groups of materials can be classified / based on appearance / - Metal - shiny and specular appearance

Professor-style explanation: The slide 'Material Models' explains how scene objects exist before they are rendered. A 3D model is not an image yet; it is a structured description of geometry and attributes. The central objects are vertices, edges, faces, triangles or other primitives, and sometimes additional data such as normals, texture coordinates, colors, materials, or connectivity. The terms describe model representation before rendering: - Material models capture the different properties of materials / - Materials can have a wide variety of appearances / - Different groups of materials can be classified / based on appearance / - Metal - shiny and specular appearance. Geometric primitives define shape, vertices provide positions and attributes, and later pipeline stages transform, project, rasterize, and shade that representation. This matters because the rendering pipeline needs this representation as input. The model describes what exists in the scene, while later stages decide where it appears, which parts are visible, how it is sampled into fragments, and how it is shaded into final pixel colors. For examination purposes, the important content is that models are structured causes of images, not images themselves; positions, topology, attributes, and materials become input for later rendering stages.

Technical commentary: This slide is about Material Models. The slide describes scene objects before rendering: geometric models, primitives, vertices, topology, attributes, and the representation used as input to the pipeline. The terms describe model representation before rendering: - Material models capture the different properties of materials / - Materials can have a wide variety of appearances / - Different groups of materials can be classified / based on appearance / - Metal - shiny and specular appearance. Geometric primitives define shape, vertices provide positions and attributes, and later pipeline stages transform, project, rasterize, and shade that representation.

Why it matters: Model slides explain the input objects that later transformations, projection, rasterization, and shading operate on.

Exam-grade answer: A strong answer for 'Material Models' distinguishes model data from rendered image data and names the geometric or attribute data that later pipeline stages consume.

Common trap: Do not describe 'Material Models' as if the model were already a pixel image; a model is data that still needs transformation, visibility, and shading.

Check yourself: Can you name the geometric objects and attributes represented by 'Material Models' before rendering begins?

### Page 26 - Materials vs. Textures

Source cue: - Material models specify the material properties for an infinitesimal surface / - No material variance with respect to location is supported / (i.e., structures such as wood grain cannot be represented) / - Textures are able to support material variance with respect to location

Professor-style explanation: The slide 'Materials vs. Textures' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Material models specify the material properties for an infinitesimal surface / - No material variance with respect to location is supported / (i.e., structures such as wood grain cannot be represented) / - Textures are able to support material variance with respect to location. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Materials vs. Textures. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Material models specify the material properties for an infinitesimal surface / - No material variance with respect to location is supported / (i.e., structures such as wood grain cannot be represented) / - Textures are able to support material variance with respect to location. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Materials vs. Textures' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Materials vs. Textures'?

### Page 27 - Light Material Interaction 1/3

Source cue: - Material appearance is influenced by three wavelength-dependent effects / - Reflection - light energy bounces off / - Absorption - light energy is reduced / - Transmission - light passes through the object (refraction occurs) / R = reflected energy

Professor-style explanation: The slide 'Light Material Interaction 1/3' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Material appearance is influenced by three wavelength-dependent effects / - Reflection - light energy bounces off / - Absorption - light energy is reduced / - Transmission - light passes through the object (refraction occurs) / R = reflected energy. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Light Material Interaction 1/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Material appearance is influenced by three wavelength-dependent effects / - Reflection - light energy bounces off / - Absorption - light energy is reduced / - Transmission - light passes through the object (refraction occurs) / R = reflected energy. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Light Material Interaction 1/3' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Material Interaction 1/3'?

### Page 28 - Light Material Interaction 2/3

Source cue: - Material properties determine weight of the individual effects / opaque colored material opaque black material / A > 0 , T = 0, R > 0 A = I ,T = 0, R = 0 / perfect mirror material transparent material / A = 0, T = 0, R = I A ~= 0, R ~= 0, T ~= I

Professor-style explanation: The slide 'Light Material Interaction 2/3' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Material properties determine weight of the individual effects / opaque colored material opaque black material / A > 0 , T = 0, R > 0 A = I ,T = 0, R = 0 / perfect mirror material transparent material / A = 0, T = 0, R = I A ~= 0, R ~= 0, T ~= I. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Light Material Interaction 2/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Material properties determine weight of the individual effects / opaque colored material opaque black material / A > 0 , T = 0, R > 0 A = I ,T = 0, R = 0 / perfect mirror material transparent material / A = 0, T = 0, R = I A ~= 0, R ~= 0, T ~= I. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Light Material Interaction 2/3' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Material Interaction 2/3'?

### Page 29 - Light Material Interaction 3/3

Source cue: - Light-material interaction described by the Spectral Response Function (SRF) / 400 Wavelength λ (nm) 700 / ygrenE / 100% / All pass Filter ( ideal, real)

Professor-style explanation: The slide 'Light Material Interaction 3/3' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Light-material interaction described by the Spectral Response Function (SRF) / 400 Wavelength λ (nm) 700 / ygrenE / 100% / All pass Filter ( ideal, real). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Light Material Interaction 3/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Light-material interaction described by the Spectral Response Function (SRF) / 400 Wavelength λ (nm) 700 / ygrenE / 100% / All pass Filter ( ideal, real). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Light Material Interaction 3/3' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Material Interaction 3/3'?

### Page 30 - Reflection = SDF x SRF

Source cue: - Light-material interaction results are the product of the SDF and SRF / 100% × 100% / SDF SRF / 0% 0% / 400 Wavelength λ (nm) 700 400 Wavelength λ (nm) 700

Professor-style explanation: The slide 'Reflection = SDF x SRF' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Light-material interaction results are the product of the SDF and SRF / 100% × 100% / SDF SRF / 0% 0% / 400 Wavelength λ (nm) 700 400 Wavelength λ (nm) 700. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Reflection = SDF x SRF. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Light-material interaction results are the product of the SDF and SRF / 100% × 100% / SDF SRF / 0% 0% / 400 Wavelength λ (nm) 700 400 Wavelength λ (nm) 700. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Reflection = SDF x SRF' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Reflection = SDF x SRF'?

### Page 31 - Reflection Modeling 1/2

Source cue: - All light sources can be described by their Spectral Density Functions / - Natural light: sun, fire, ... / - Artificial light: light bulb, laser, neon tube, LED, ... / - All material properties can be described by Spectral Response Functions / - Glass, Water: SRF for transmission

Professor-style explanation: The slide 'Reflection Modeling 1/2' explains how scene objects exist before they are rendered. A 3D model is not an image yet; it is a structured description of geometry and attributes. The central objects are vertices, edges, faces, triangles or other primitives, and sometimes additional data such as normals, texture coordinates, colors, materials, or connectivity. The terms describe model representation before rendering: - All light sources can be described by their Spectral Density Functions / - Natural light: sun, fire, ... / - Artificial light: light bulb, laser, neon tube, LED, ... / - All material properties can be described by Spectral Response Functions / - Glass, Water: SRF for transmission. Geometric primitives define shape, vertices provide positions and attributes, and later pipeline stages transform, project, rasterize, and shade that representation. This matters because the rendering pipeline needs this representation as input. The model describes what exists in the scene, while later stages decide where it appears, which parts are visible, how it is sampled into fragments, and how it is shaded into final pixel colors. For examination purposes, the important content is that models are structured causes of images, not images themselves; positions, topology, attributes, and materials become input for later rendering stages.

Technical commentary: This slide is about Reflection Modeling 1/2. The slide describes scene objects before rendering: geometric models, primitives, vertices, topology, attributes, and the representation used as input to the pipeline. The terms describe model representation before rendering: - All light sources can be described by their Spectral Density Functions / - Natural light: sun, fire, ... / - Artificial light: light bulb, laser, neon tube, LED, ... / - All material properties can be described by Spectral Response Functions / - Glass, Water: SRF for transmission. Geometric primitives define shape, vertices provide positions and attributes, and later pipeline stages transform, project, rasterize, and shade that representation.

Why it matters: Model slides explain the input objects that later transformations, projection, rasterization, and shading operate on.

Exam-grade answer: A strong answer for 'Reflection Modeling 1/2' distinguishes model data from rendered image data and names the geometric or attribute data that later pipeline stages consume.

Common trap: Do not describe 'Reflection Modeling 1/2' as if the model were already a pixel image; a model is data that still needs transformation, visibility, and shading.

Check yourself: Can you name the geometric objects and attributes represented by 'Reflection Modeling 1/2' before rendering begins?

### Page 32 - Reflection Modeling 2/2

Source cue: - Synthetic and natural objects are in general not self-emitting / - Light is reflected at its surfaces, i.e., re-emitted into the scene / - Reflection is dependent on surface properties / - Rough surface: scattering of light / - Smooth surface: reflection of light

Professor-style explanation: The slide 'Reflection Modeling 2/2' explains how scene objects exist before they are rendered. A 3D model is not an image yet; it is a structured description of geometry and attributes. The central objects are vertices, edges, faces, triangles or other primitives, and sometimes additional data such as normals, texture coordinates, colors, materials, or connectivity. The terms describe model representation before rendering: - Synthetic and natural objects are in general not self-emitting / - Light is reflected at its surfaces, i.e., re-emitted into the scene / - Reflection is dependent on surface properties / - Rough surface: scattering of light / - Smooth surface: reflection of light. Geometric primitives define shape, vertices provide positions and attributes, and later pipeline stages transform, project, rasterize, and shade that representation. This matters because the rendering pipeline needs this representation as input. The model describes what exists in the scene, while later stages decide where it appears, which parts are visible, how it is sampled into fragments, and how it is shaded into final pixel colors. For examination purposes, the important content is that models are structured causes of images, not images themselves; positions, topology, attributes, and materials become input for later rendering stages.

Technical commentary: This slide is about Reflection Modeling 2/2. The slide describes scene objects before rendering: geometric models, primitives, vertices, topology, attributes, and the representation used as input to the pipeline. The terms describe model representation before rendering: - Synthetic and natural objects are in general not self-emitting / - Light is reflected at its surfaces, i.e., re-emitted into the scene / - Reflection is dependent on surface properties / - Rough surface: scattering of light / - Smooth surface: reflection of light. Geometric primitives define shape, vertices provide positions and attributes, and later pipeline stages transform, project, rasterize, and shade that representation.

Why it matters: Model slides explain the input objects that later transformations, projection, rasterization, and shading operate on.

Exam-grade answer: A strong answer for 'Reflection Modeling 2/2' distinguishes model data from rendered image data and names the geometric or attribute data that later pipeline stages consume.

Common trap: Do not describe 'Reflection Modeling 2/2' as if the model were already a pixel image; a model is data that still needs transformation, visibility, and shading.

Check yourself: Can you name the geometric objects and attributes represented by 'Reflection Modeling 2/2' before rendering begins?

### Page 33 - 8.4 Phong Illumination Model

Source cue: Determining the color of vertices

Professor-style explanation: The slide '8.4 Phong Illumination Model' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: Determining the color of vertices. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about 8.4 Phong Illumination Model. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: Determining the color of vertices. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for '8.4 Phong Illumination Model' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '8.4 Phong Illumination Model'?

### Page 34 - Empirical Observations

Source cue: - Light reflections are / - Dependent on the position of the observer / "... position of the observer..." / - Dependent on the material properties of the surface / "... the specular properties of the object." Photo

Professor-style explanation: The slide 'Empirical Observations' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Light reflections are / - Dependent on the position of the observer / "... position of the observer..." / - Dependent on the material properties of the surface / "... the specular properties of the object." Photo. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Empirical Observations. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Light reflections are / - Dependent on the position of the observer / "... position of the observer..." / - Dependent on the material properties of the surface / "... the specular properties of the object." Photo. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Empirical Observations' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Empirical Observations'?

### Page 35 - Illumination Models

Source cue: - Illumination models calculate the color of scene objects / based on the following properties / - Location - Position P = (x, y, z) of the selected point P / - Orientation - normal direction N = (n , n , n ) of surface in P / x y z

Professor-style explanation: The slide 'Illumination Models' explains how scene objects exist before they are rendered. A 3D model is not an image yet; it is a structured description of geometry and attributes. The central objects are vertices, edges, faces, triangles or other primitives, and sometimes additional data such as normals, texture coordinates, colors, materials, or connectivity. The terms describe model representation before rendering: - Illumination models calculate the color of scene objects / based on the following properties / - Location - Position P = (x, y, z) of the selected point P / - Orientation - normal direction N = (n , n , n ) of surface in P / x y z. Geometric primitives define shape, vertices provide positions and attributes, and later pipeline stages transform, project, rasterize, and shade that representation. This matters because the rendering pipeline needs this representation as input. The model describes what exists in the scene, while later stages decide where it appears, which parts are visible, how it is sampled into fragments, and how it is shaded into final pixel colors. For examination purposes, the important content is that models are structured causes of images, not images themselves; positions, topology, attributes, and materials become input for later rendering stages.

Technical commentary: This slide is about Illumination Models. The slide describes scene objects before rendering: geometric models, primitives, vertices, topology, attributes, and the representation used as input to the pipeline. The terms describe model representation before rendering: - Illumination models calculate the color of scene objects / based on the following properties / - Location - Position P = (x, y, z) of the selected point P / - Orientation - normal direction N = (n , n , n ) of surface in P / x y z. Geometric primitives define shape, vertices provide positions and attributes, and later pipeline stages transform, project, rasterize, and shade that representation.

Why it matters: Model slides explain the input objects that later transformations, projection, rasterization, and shading operate on.

Exam-grade answer: A strong answer for 'Illumination Models' distinguishes model data from rendered image data and names the geometric or attribute data that later pipeline stages consume.

Common trap: Do not describe 'Illumination Models' as if the model were already a pixel image; a model is data that still needs transformation, visibility, and shading.

Check yourself: Can you name the geometric objects and attributes represented by 'Illumination Models' before rendering begins?

### Page 36 - yaR

Source cue: thgiL / Diffuse Intensity 1/3 / - Simulation of light reflections on diffuse surfaces / - Model assumption / - Diffuse light reflections are non-directional (scattering)

Professor-style explanation: The slide 'yaR' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: thgiL / Diffuse Intensity 1/3 / - Simulation of light reflections on diffuse surfaces / - Model assumption / - Diffuse light reflections are non-directional (scattering). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about yaR. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: thgiL / Diffuse Intensity 1/3 / - Simulation of light reflections on diffuse surfaces / - Model assumption / - Diffuse light reflections are non-directional (scattering). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'yaR' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'yaR'?

### Page 37 - Diffuse Intensity 2/3

Source cue: - Equation / I = lk⋅ n⋅ L ⋅ max( 0, ) / diffuse d d / - k diffuse material properties (surface dependent) / - L diffuse light intensity (light source dependent)

Professor-style explanation: The slide 'Diffuse Intensity 2/3' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Equation / I = lk⋅ n⋅ L ⋅ max( 0, ) / diffuse d d / - k diffuse material properties (surface dependent) / - L diffuse light intensity (light source dependent). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Diffuse Intensity 2/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Equation / I = lk⋅ n⋅ L ⋅ max( 0, ) / diffuse d d / - k diffuse material properties (surface dependent) / - L diffuse light intensity (light source dependent). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Diffuse Intensity 2/3' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Diffuse Intensity 2/3'?

### Page 38 - Diffuse Intensity 3/3

Source cue: I = k ⋅ L ⋅ max(0, l⃗ ⋅ n) / diffuse d d / https://bit.ly/2XFhbcM / Extrahierte Tabellen: / [Tabelle 1]

Professor-style explanation: The slide 'Diffuse Intensity 3/3' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: I = k ⋅ L ⋅ max(0, l⃗ ⋅ n) / diffuse d d / https://bit.ly/2XFhbcM / Extrahierte Tabellen: / [Tabelle 1]. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Diffuse Intensity 3/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: I = k ⋅ L ⋅ max(0, l⃗ ⋅ n) / diffuse d d / https://bit.ly/2XFhbcM / Extrahierte Tabellen: / [Tabelle 1]. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Diffuse Intensity 3/3' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Diffuse Intensity 3/3' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Diffuse Intensity 3/3' into a causal sentence instead of repeating the slide title?

### Page 39 - Ambient Intensity 1/2

Source cue: - Simulation of the general room brightness / - Indirect light incidence or multiple reflections / - Model assumptions / - Constant influence on all scene objects / - No influence of position or alignment

Professor-style explanation: The slide 'Ambient Intensity 1/2' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Simulation of the general room brightness / - Indirect light incidence or multiple reflections / - Model assumptions / - Constant influence on all scene objects / - No influence of position or alignment. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Ambient Intensity 1/2. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Simulation of the general room brightness / - Indirect light incidence or multiple reflections / - Model assumptions / - Constant influence on all scene objects / - No influence of position or alignment. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Ambient Intensity 1/2' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Ambient Intensity 1/2'?

### Page 40 - Ambient Intensity 2/2

Source cue: I = k ⋅ L / ambient a a / https://bit.ly/2XGn61n / Extrahierte Tabellen: / [Tabelle 1]

Professor-style explanation: The slide 'Ambient Intensity 2/2' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: I = k ⋅ L / ambient a a / https://bit.ly/2XGn61n / Extrahierte Tabellen: / [Tabelle 1]. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Ambient Intensity 2/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: I = k ⋅ L / ambient a a / https://bit.ly/2XGn61n / Extrahierte Tabellen: / [Tabelle 1]. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Ambient Intensity 2/2' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Ambient Intensity 2/2' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Ambient Intensity 2/2' into a causal sentence instead of repeating the slide title?

### Page 41 - Specular Intensity 1/3

Source cue: - Simulation of light reflections on specular surfaces / - Model assumption / - Reflection of light are directed (reflection) / - Observations / - Reflections of light are observer-dependent

Professor-style explanation: The slide 'Specular Intensity 1/3' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Simulation of light reflections on specular surfaces / - Model assumption / - Reflection of light are directed (reflection) / - Observations / - Reflections of light are observer-dependent. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Specular Intensity 1/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Simulation of light reflections on specular surfaces / - Model assumption / - Reflection of light are directed (reflection) / - Observations / - Reflections of light are observer-dependent. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Specular Intensity 1/3' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Specular Intensity 1/3'?

### Page 42 - Reflection Vector r⃗

Source cue: - Calculation of the reflection vector / - Incidence angle corresponds to exit angle / - Equation / ⃗ ⃗ / r⃗ = 2n ⋅⋅ n ⋅ l − l

Professor-style explanation: The slide 'Reflection Vector r⃗' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: - Calculation of the reflection vector / - Incidence angle corresponds to exit angle / - Equation / ⃗ ⃗ / r⃗ = 2n ⋅⋅ n ⋅ l − l. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Reflection Vector r⃗. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: - Calculation of the reflection vector / - Incidence angle corresponds to exit angle / - Equation / ⃗ ⃗ / r⃗ = 2n ⋅⋅ n ⋅ l − l. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Reflection Vector r⃗' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Reflection Vector r⃗' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Reflection Vector r⃗' into a causal sentence instead of repeating the slide title?

### Page 43 - Specular Intensity 2/3

Source cue: - Equation / I = kr⃗ ⋅ ⋅v⃗ L ⋅ max( 0, ) / specular s s / - k specular material properties (surface dependant) / - L specular light intensity (light source dependent)

Professor-style explanation: The slide 'Specular Intensity 2/3' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Equation / I = kr⃗ ⋅ ⋅v⃗ L ⋅ max( 0, ) / specular s s / - k specular material properties (surface dependant) / - L specular light intensity (light source dependent). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Specular Intensity 2/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Equation / I = kr⃗ ⋅ ⋅v⃗ L ⋅ max( 0, ) / specular s s / - k specular material properties (surface dependant) / - L specular light intensity (light source dependent). Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Specular Intensity 2/3' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Specular Intensity 2/3'?

### Page 44 - Specular Exponent p

Source cue: - p influences fall off of specular highlight (p ∊ [1, M] mit M ≈ 100) / p = 1 / max(0, r⃗ ⋅ v⃗)1 / p = 5 / max(0, r⃗ ⋅ v⃗)5

Professor-style explanation: The slide 'Specular Exponent p' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - p influences fall off of specular highlight (p ∊ [1, M] mit M ≈ 100) / p = 1 / max(0, r⃗ ⋅ v⃗)1 / p = 5 / max(0, r⃗ ⋅ v⃗)5. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Specular Exponent p. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - p influences fall off of specular highlight (p ∊ [1, M] mit M ≈ 100) / p = 1 / max(0, r⃗ ⋅ v⃗)1 / p = 5 / max(0, r⃗ ⋅ v⃗)5. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Specular Exponent p' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Specular Exponent p'?

### Page 45 - Specular Intensity 3/3

Source cue: r⃗ = 2 ⋅ n ⋅ n ⋅ l⃗ − l⃗ / https://bit.ly/2XbPc7s I = k ⋅ L ⋅ max(0, r⃗ ⋅ v⃗)p / specular s s / Extrahierte Tabellen: / [Tabelle 1]

Professor-style explanation: The slide 'Specular Intensity 3/3' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. The terms form an input-operation-output relation: r⃗ = 2 ⋅ n ⋅ n ⋅ l⃗ − l⃗ / https://bit.ly/2XbPc7s I = k ⋅ L ⋅ max(0, r⃗ ⋅ v⃗)p / specular s s / Extrahierte Tabellen: / [Tabelle 1]. The slide groups them because one object or quantity is processed into another result used later in rendering. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation. For examination purposes, the important content is the causal pattern: input object, operation or test, produced result, and the next stage that consumes it.

Technical commentary: This slide is about Specular Intensity 3/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. The terms form an input-operation-output relation: r⃗ = 2 ⋅ n ⋅ n ⋅ l⃗ − l⃗ / https://bit.ly/2XbPc7s I = k ⋅ L ⋅ max(0, r⃗ ⋅ v⃗)p / specular s s / Extrahierte Tabellen: / [Tabelle 1]. The slide groups them because one object or quantity is processed into another result used later in rendering.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Exam-grade answer: A strong answer for 'Specular Intensity 3/3' turns the title into a precise cause-and-effect statement with input, processing rule, output, and later use.

Common trap: Do not answer 'Specular Intensity 3/3' by repeating the title; name what changes, why it changes, and what the next rendering step receives.

Check yourself: Can you turn 'Specular Intensity 3/3' into a causal sentence instead of repeating the slide title?

### Page 46 - Blinn-Phong Illumination Model 1/2

Source cue: - Alternative simulation of specular relfections / - Replace mirror direction r⃗ with Halfway-Vector h / - h = l + v⃗ / - h is halfway between l and v⃗ / - Equation

Professor-style explanation: The slide 'Blinn-Phong Illumination Model 1/2' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Alternative simulation of specular relfections / - Replace mirror direction r⃗ with Halfway-Vector h / - h = l + v⃗ / - h is halfway between l and v⃗ / - Equation. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Blinn-Phong Illumination Model 1/2. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Alternative simulation of specular relfections / - Replace mirror direction r⃗ with Halfway-Vector h / - h = l + v⃗ / - h is halfway between l and v⃗ / - Equation. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Blinn-Phong Illumination Model 1/2' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Blinn-Phong Illumination Model 1/2'?

### Page 47 - Blinn-Phong Illumination Model 2/2

Source cue: h = l⃗ + v⃗ / https://bit.ly/2ICDwBD I = k ⋅ L ⋅ max(0, h ⋅ n)p / specular s s / Extrahierte Tabellen: / [Tabelle 1]

Professor-style explanation: The slide 'Blinn-Phong Illumination Model 2/2' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: h = l⃗ + v⃗ / https://bit.ly/2ICDwBD I = k ⋅ L ⋅ max(0, h ⋅ n)p / specular s s / Extrahierte Tabellen: / [Tabelle 1]. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Blinn-Phong Illumination Model 2/2. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: h = l⃗ + v⃗ / https://bit.ly/2ICDwBD I = k ⋅ L ⋅ max(0, h ⋅ n)p / specular s s / Extrahierte Tabellen: / [Tabelle 1]. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Blinn-Phong Illumination Model 2/2' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Blinn-Phong Illumination Model 2/2'?

### Page 48 - Phong Illumination Model

Source cue: - Additive combination of all factors / I = k ⋅ L / ambient a a / I = k ⋅ L ⋅ max 0, n ⋅ l / diffuse d d

Professor-style explanation: The slide 'Phong Illumination Model' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Additive combination of all factors / I = k ⋅ L / ambient a a / I = k ⋅ L ⋅ max 0, n ⋅ l / diffuse d d. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Phong Illumination Model. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Additive combination of all factors / I = k ⋅ L / ambient a a / I = k ⋅ L ⋅ max 0, n ⋅ l / diffuse d d. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Phong Illumination Model' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Phong Illumination Model'?

### Page 49 - Phong Illumination Model

Source cue: - Additive combination of all factors / I = k ⋅ L / ambient a a / I = k ⋅ L ⋅ max 0, n ⋅ l / diffuse d d

Professor-style explanation: The slide 'Phong Illumination Model' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Additive combination of all factors / I = k ⋅ L / ambient a a / I = k ⋅ L ⋅ max 0, n ⋅ l / diffuse d d. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Phong Illumination Model. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Additive combination of all factors / I = k ⋅ L / ambient a a / I = k ⋅ L ⋅ max 0, n ⋅ l / diffuse d d. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Phong Illumination Model' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Phong Illumination Model'?

### Page 50 - 8.5 Shading

Source cue: Coloring triangles when using vertex-based illumination

Professor-style explanation: The slide '8.5 Shading' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: Coloring triangles when using vertex-based illumination. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about 8.5 Shading. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: Coloring triangles when using vertex-based illumination. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for '8.5 Shading' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by '8.5 Shading'?

### Page 51 - Shading

Source cue: - Illumination model usually applied in the fragment stage / - Vertex-based illumination also possible to save compute / - Requires to spread the illumination information of the vertices / over the triangle / Flat Gouroud Phong

Professor-style explanation: The slide 'Shading' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Illumination model usually applied in the fragment stage / - Vertex-based illumination also possible to save compute / - Requires to spread the illumination information of the vertices / over the triangle / Flat Gouroud Phong. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Shading. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Illumination model usually applied in the fragment stage / - Vertex-based illumination also possible to save compute / - Requires to spread the illumination information of the vertices / over the triangle / Flat Gouroud Phong. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Shading' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Shading'?

### Page 52 - Shading Computation

Source cue: - Tasks of shading procedures / - Colorize surfaces based on colors calculated by illumination model / - Shading is closely linked to the rasterization process and integrated into it / - Distribute lighting and shading / - Calculate light intensity for surface points

Professor-style explanation: The slide 'Shading Computation' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Tasks of shading procedures / - Colorize surfaces based on colors calculated by illumination model / - Shading is closely linked to the rasterization process and integrated into it / - Distribute lighting and shading / - Calculate light intensity for surface points. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Shading Computation. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Tasks of shading procedures / - Colorize surfaces based on colors calculated by illumination model / - Shading is closely linked to the rasterization process and integrated into it / - Distribute lighting and shading / - Calculate light intensity for surface points. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Shading Computation' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Shading Computation'?

### Page 53 - Flat Shading

Source cue: - Operation / - Calling the lighting model for a single point of a surface / (e.g., polygon center) / - Shading of the entire polygon in the determined intensity / - Useful if the following assumptions apply

Professor-style explanation: The slide 'Flat Shading' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Operation / - Calling the lighting model for a single point of a surface / (e.g., polygon center) / - Shading of the entire polygon in the determined intensity / - Useful if the following assumptions apply. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Flat Shading. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Operation / - Calling the lighting model for a single point of a surface / (e.g., polygon center) / - Shading of the entire polygon in the determined intensity / - Useful if the following assumptions apply. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Flat Shading' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Flat Shading'?

### Page 54 - Gouraud Shading 1/5

Source cue: - Shading method for polygons based on the interpolation / of intensity values a t the polygon vertices / - Requirements / - Area decomposition in polygons (usually triangles) / - Normals for polygon corners (vertex normals)

Professor-style explanation: The slide 'Gouraud Shading 1/5' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Shading method for polygons based on the interpolation / of intensity values a t the polygon vertices / - Requirements / - Area decomposition in polygons (usually triangles) / - Normals for polygon corners (vertex normals). A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Gouraud Shading 1/5. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Shading method for polygons based on the interpolation / of intensity values a t the polygon vertices / - Requirements / - Area decomposition in polygons (usually triangles) / - Normals for polygon corners (vertex normals). A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Gouraud Shading 1/5' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Gouraud Shading 1/5'?

### Page 55 - Gouraud Shading 2/5

Source cue: - Proceeding / - Compute intensity values l for polygon corners v / i i / - Linear interpolation of the intensity values a long the edges / - Linear interpolation of the intensity values a long the scanlines

Professor-style explanation: The slide 'Gouraud Shading 2/5' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Proceeding / - Compute intensity values l for polygon corners v / i i / - Linear interpolation of the intensity values a long the edges / - Linear interpolation of the intensity values a long the scanlines. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Gouraud Shading 2/5. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Proceeding / - Compute intensity values l for polygon corners v / i i / - Linear interpolation of the intensity values a long the edges / - Linear interpolation of the intensity values a long the scanlines. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Gouraud Shading 2/5' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Gouraud Shading 2/5'?

### Page 56 - Gouraud Shading 3/5

Source cue: - Shading at conceptually smooth transitions / - Geometrically "hard" edges instead of conceptually "soft" edges / - Gouraud shading can create visually smooth transitions / through smooth shading / - Example: P / P smooth transition, P / P hard transition

Professor-style explanation: The slide 'Gouraud Shading 3/5' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Shading at conceptually smooth transitions / - Geometrically "hard" edges instead of conceptually "soft" edges / - Gouraud shading can create visually smooth transitions / through smooth shading / - Example: P / P smooth transition, P / P hard transition. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Gouraud Shading 3/5. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Shading at conceptually smooth transitions / - Geometrically "hard" edges instead of conceptually "soft" edges / - Gouraud shading can create visually smooth transitions / through smooth shading / - Example: P / P smooth transition, P / P hard transition. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Gouraud Shading 3/5' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Gouraud Shading 3/5'?

### Page 57 - Gouraud Shading 4/5

Source cue: - interpolation problems / - The shading inside a triangle results from interpolation / - Intensity fluctuations in the interior are not taken into account / - Intensity fluctuations can only be considered by finer tessellation / - Example: Spotlight shines into the interior of a triangle

Professor-style explanation: The slide 'Gouraud Shading 4/5' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - interpolation problems / - The shading inside a triangle results from interpolation / - Intensity fluctuations in the interior are not taken into account / - Intensity fluctuations can only be considered by finer tessellation / - Example: Spotlight shines into the interior of a triangle. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Gouraud Shading 4/5. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - interpolation problems / - The shading inside a triangle results from interpolation / - Intensity fluctuations in the interior are not taken into account / - Intensity fluctuations can only be considered by finer tessellation / - Example: Spotlight shines into the interior of a triangle. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Gouraud Shading 4/5' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Gouraud Shading 4/5'?

### Page 58 - Gouraud Shading 5/5

Source cue: - Interpolation problems / - Contiguous polygons that do not fully share the same edges / will be shaded differently

Professor-style explanation: The slide 'Gouraud Shading 5/5' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. The terms describe local shading inputs: - Interpolation problems / - Contiguous polygons that do not fully share the same edges / will be shaded differently. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type. For examination purposes, the important content is the vector and material relation: normal, light direction, view direction, reflection term, and color contribution.

Technical commentary: This slide is about Gouraud Shading 5/5. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. The terms describe local shading inputs: - Interpolation problems / - Contiguous polygons that do not fully share the same edges / will be shaded differently. Surface position, normal, light direction, view direction, and material response combine to produce the final color contribution.

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Exam-grade answer: A strong answer for 'Gouraud Shading 5/5' names the surface point, normal, light direction, view direction, material parameters, and the resulting ambient, diffuse, or specular contribution.

Common trap: Do not mix up normal direction, light direction, and view direction; changing one changes the lighting term in a different way.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Gouraud Shading 5/5'?

### Page 59 - Phong Shading 1/2

Source cue: - Interpolation of the corner normals instead of the corner intensities / - Proceeding / - Calculation of the corner normals / - Interpolation of the normals between the corners / - Interpolation between the endpoints of a scanline

Professor-style explanation: The slide 'Phong Shading 1/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Interpolation of the corner normals instead of the corner intensities / - Proceeding / - Calculation of the corner normals / - Interpolation of the normals between the corners / - Interpolation between the endpoints of a scanline. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Phong Shading 1/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Interpolation of the corner normals instead of the corner intensities / - Proceeding / - Calculation of the corner normals / - Interpolation of the normals between the corners / - Interpolation between the endpoints of a scanline. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Phong Shading 1/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Phong Shading 1/2'?

### Page 60 - Phong Shading 2/2

Source cue: - Advantages / - Pixel-based (i.e., image-precise) evaluation of the light sources / - Highly focused highlights at corners are not interpolated over the edge / - Highlights inside a triangle can be displayed / - Disadvantage

Professor-style explanation: The slide 'Phong Shading 2/2' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. The terms describe sample generation: - Advantages / - Pixel-based (i.e., image-precise) evaluation of the light sources / - Highly focused highlights at corners are not interpolated over the edge / - Highlights inside a triangle can be displayed / - Disadvantage. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations. For examination purposes, the important content is that rasterization creates fragment candidates from projected primitives; later tests decide whether those candidates affect pixels.

Technical commentary: This slide is about Phong Shading 2/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. The terms describe sample generation: - Advantages / - Pixel-based (i.e., image-precise) evaluation of the light sources / - Highly focused highlights at corners are not interpolated over the edge / - Highlights inside a triangle can be displayed / - Disadvantage. A continuous primitive is tested against the pixel grid, covered samples become fragments, and interpolated attributes travel with those fragments.

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Exam-grade answer: A strong answer for 'Phong Shading 2/2' explains coverage, fragment creation, interpolation, and the difference between a generated fragment and a final pixel update.

Common trap: Do not call every fragment a pixel; fragments are candidates and can still fail tests or be blended before the framebuffer is updated.

Check yourself: Can you explain which samples/fragments are generated by 'Phong Shading 2/2'?

### Page 61 - Literature and other sources used in this chapter

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Literature and other sources used in this chapter' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail. For examination purposes, this page should be linked to the nearest surrounding text-heavy slides: it introduces a topic boundary or visual example, while the neighboring pages provide the precise vocabulary and algorithmic details.

Technical commentary: This slide is about Literature and other sources used in this chapter. The slide lists source material or chapter references that support the technical content and give names for further reading. The extracted text does not expose object-level labels for this page. Within the lecture flow, the page functions as a visual, diagram, or title transition, so its connection is established by the surrounding slides rather than by readable bullet text.

Why it matters: Reference slides provide the source trail for definitions, algorithms, and deeper explanations.

Exam-grade answer: A strong answer for 'Literature and other sources used in this chapter' identifies what kind of source is listed and which course concept or algorithm that source supports.

Common trap: Do not skip 'Literature and other sources used in this chapter' if it names a standard algorithm or source that defines terminology used later in the chapter.

Check yourself: Can you identify which source or topic 'Literature and other sources used in this chapter' points to for deeper study?

### Page 62 - Lesen und Ausprobieren

Source cue: - Zum Lesen - Zum Ausprobieren / Marschner, Steve und Peter Shirley: / - Simulation von drei / Fundamentals of Computer Graphics, / ausgewählten Materialien

Professor-style explanation: The slide 'Lesen und Ausprobieren' collects the source material behind the chapter. References are not rendering objects themselves, but they identify the books, papers, or external resources from which the lecture's terminology and algorithms are drawn. The listed sources support the chapter content: - Zum Lesen - Zum Ausprobieren / Marschner, Steve und Peter Shirley: / - Simulation von drei / Fundamentals of Computer Graphics, / ausgewählten Materialien. They point to the books, papers, or resources behind the definitions and algorithms used in the lecture. In practical terms, a reference slide marks the boundary of the chapter and tells us where the formal definitions, derivations, or extended examples can be found if a topic needs more depth than the lecture slides provide. For examination purposes, the important content is source attribution and vocabulary: references tell where precise definitions and standard algorithms come from.

Technical commentary: This slide is about Lesen und Ausprobieren. The slide lists source material or chapter references that support the technical content and give names for further reading. The listed sources support the chapter content: - Zum Lesen - Zum Ausprobieren / Marschner, Steve und Peter Shirley: / - Simulation von drei / Fundamentals of Computer Graphics, / ausgewählten Materialien. They point to the books, papers, or resources behind the definitions and algorithms used in the lecture.

Why it matters: Reference slides provide the source trail for definitions, algorithms, and deeper explanations.

Exam-grade answer: A strong answer for 'Lesen und Ausprobieren' identifies what kind of source is listed and which course concept or algorithm that source supports.

Common trap: Do not skip 'Lesen und Ausprobieren' if it names a standard algorithm or source that defines terminology used later in the chapter.

Check yourself: Can you identify which source or topic 'Lesen und Ausprobieren' points to for deeper study?

## 08.1 Physics of Light

Source location: Section 8.1

### Commentary

The physics slides provide intuition for light as energy interacting with surfaces. For this course, the goal is not full physical simulation but a usable model for real-time rendering.

Important terms are reflection, absorption, wavelength/color, intensity, and direction. These terms become shader inputs or material parameters later. The simplified model must still preserve the relation between light direction, surface orientation, and observed brightness.

### Mental Model

Shading is an approximation of light-surface interaction that is cheap enough for rendering.

### Check Yourself

Why does surface orientation affect diffuse brightness?

## 08.2 Light Sources

Source location: Section 8.2

### Commentary

Light source models define where light comes from and how its direction and intensity are computed. Directional lights approximate distant sources with parallel rays. Point lights emit from a position and often include attenuation. Spotlights add a directional cone.

In shader code, the type of light determines how you compute the light vector. A directional light can use a fixed direction; a point light requires subtracting the surface position from the light position.

### Mental Model

Different light types mainly change how the light direction and intensity are computed at the surface point.

### Check Yourself

What is the difference between a directional light vector and a point light vector?

## 08.3 Material Models

Source location: Section 8.3

### Commentary

A material model tells the shader how a surface responds to light. Diffuse material scatters light broadly; specular material creates view-dependent highlights; ambient terms approximate background illumination.

Material coefficients are not arbitrary decoration. They scale the contribution of each lighting term. If the specular coefficient is zero, the surface should not show a specular highlight under that model.

### Mental Model

Light asks what arrives; material answers how the surface reacts.

### Check Yourself

Which material parameter would you adjust to reduce shiny highlights?

## 08.4 Phong Illumination Model

Source location: Section 8.4

### Commentary

The Phong illumination model combines ambient, diffuse, and specular terms. Diffuse lighting uses the angle between normal and light direction. Specular lighting also depends on the viewer because highlights move with the view direction.

The formula is less important than the decomposition. Ambient is a rough constant approximation. Diffuse is orientation-dependent matte reflection. Specular is view-dependent shininess. A correct answer should name the vectors and normalize them.

### Mental Model

Phong-style lighting is a sum of simple terms, each modeling a different visual effect.

### Check Yourself

Why does the specular term depend on the view direction?

## 08.5 Shading

Source location: Section 8.5

### Commentary

Shading decides where the illumination calculation is evaluated and how results are interpolated. Flat shading uses one value per primitive. Gouraud shading evaluates at vertices and interpolates colors. Phong shading interpolates normals and evaluates lighting per fragment.

Per-fragment shading is more expensive but can represent highlights more accurately. This connects directly to the pipeline: interpolation during rasterization provides the data used by the fragment shader.

### Mental Model

The shading method decides what is computed at vertices and what is computed at fragments.

### Check Yourself

Why can Gouraud shading miss a small specular highlight?

## End-of-Lecture Summary

If you remember only one thing from Lecture 08, remember this: This lecture explains how visible surface points receive color from local light, material, normal, and view information. It is about shading a point, not solving all global light transport.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
