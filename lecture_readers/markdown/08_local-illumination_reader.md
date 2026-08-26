# Lecture 08 - Local Illumination

Source chunk: `course_text_parts/03_lectures/08_local-illumination.txt`
Extracted slide pages in source chunk: 62

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture explains how visible surface points receive color from local light, material, normal, and view information. It is about shading a point, not solving all global light transport.

## How To Read This Lecture

- First read the big picture and the mental models.
- Then open the source chunk and compare the slide bullets to the commentary.
- After each section, answer the check question without notes.
- If the check feels vague, revisit the source pages listed for that section.

## Per-Slide Commentary

Every extracted slide page gets its own reading note. This is the part to use when the original PDF is too terse or visually dense.

### Page 1 - Untitled slide

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Untitled slide' introduces a concrete graphics object, operation, or relation. The named terms describe input data, a processing step, and an output used elsewhere in the rendering workflow. On the slide, the concrete items are: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content. The object-level relation is therefore input, operation, output, and the later graphics stage that consumes the output.

Technical commentary: This slide is about Untitled slide. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Untitled slide' into a causal sentence instead of repeating the slide title?

### Page 2 - Local Illumination

Source cue: - Illumination is the process of simulating light interactions in a virtual scene / - Requires light and material properties / - Achieved through illumination model / - Essential for scene perception / without iIllumination with illumination

Professor-style explanation: The slide 'Local Illumination' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Illumination is the process of simulating light interactions in a virtual scene / - Requires light and material properties / - Achieved through illumination model / - Essential for scene perception / without iIllumination with illumination. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Local Illumination. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Illumination is the process of simulating light interactions in a virtual scene / - Requires light and material properties / - Achieved through illumination model / - Essential for scene perception / without iIllumination with illumination

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Local Illumination'?

### Page 3 - 8.1 Physics of Light

Source cue: 8.2 Light Sources / 8.3 Material Models / 8.4 Phong Illumination Model / 8.5 Shading

Professor-style explanation: The slide '8.1 Physics of Light' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: 8.2 Light Sources / 8.3 Material Models / 8.4 Phong Illumination Model / 8.5 Shading. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about 8.1 Physics of Light. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: 8.2 Light Sources / 8.3 Material Models / 8.4 Phong Illumination Model / 8.5 Shading

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '8.1 Physics of Light'?

### Page 4 - 8.1 Physics of Light

Source cue: Understanding light in the real world

Professor-style explanation: The slide '8.1 Physics of Light' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: Understanding light in the real world. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about 8.1 Physics of Light. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: Understanding light in the real world

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '8.1 Physics of Light'?

### Page 5 - Electromagnetic Radiation

Source cue: - Electromagnetic radiation is defined by a spectrum of wavelengths / Wave length λ / - Visible light is subset of electromagnetic spectrum between 400 and 700nm, / which humans perceive as colors

Professor-style explanation: The slide 'Electromagnetic Radiation' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Electromagnetic radiation is defined by a spectrum of wavelengths / Wave length λ / - Visible light is subset of electromagnetic spectrum between 400 and 700nm, / which humans perceive as colors. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Electromagnetic Radiation. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Electromagnetic radiation is defined by a spectrum of wavelengths / Wave length λ / - Visible light is subset of electromagnetic spectrum between 400 and 700nm, / which humans perceive as colors

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Electromagnetic Radiation'?

### Page 6 - Visible Light

Source cue: 1000 nm / Infrared / Radio / 700 nm / TV Red

Professor-style explanation: The slide 'Visible Light' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: 1000 nm / Infrared / Radio / 700 nm / TV Red. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Visible Light. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: 1000 nm / Infrared / Radio / 700 nm / TV Red

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Visible Light'?

### Page 7 - Visible Light

Source cue: 1000 nm / Infrared / Radio / 700 nm / TV Red

Professor-style explanation: The slide 'Visible Light' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: 1000 nm / Infrared / Radio / 700 nm / TV Red. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Visible Light. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: 1000 nm / Infrared / Radio / 700 nm / TV Red

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Visible Light'?

### Page 8 - Light Spectra

Source cue: - Different light sources have different light spectra / - Intensity differs based on wavelength in visible spectrum / [http://www.micro.magnet.fsu.edu/optics/lightandcolor/sources.html]

Professor-style explanation: The slide 'Light Spectra' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Different light sources have different light spectra / - Intensity differs based on wavelength in visible spectrum / [http://www.micro.magnet.fsu.edu/optics/lightandcolor/sources.html]. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Light Spectra. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Different light sources have different light spectra / - Intensity differs based on wavelength in visible spectrum / [http://www.micro.magnet.fsu.edu/optics/lightandcolor/sources.html]

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Spectra'?

### Page 9 - Black-Body Radiation

Source cue: - A continuous spectrum emitted by a black body at a certain temperature / Steel / > 1570 K / 820 K / Stars

Professor-style explanation: The slide 'Black-Body Radiation' introduces a concrete graphics object, operation, or relation. The named terms describe input data, a processing step, and an output used elsewhere in the rendering workflow. On the slide, the concrete items are: - A continuous spectrum emitted by a black body at a certain temperature / Steel / > 1570 K / 820 K / Stars. The object-level relation is therefore input, operation, output, and the later graphics stage that consumes the output.

Technical commentary: This slide is about Black-Body Radiation. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: - A continuous spectrum emitted by a black body at a certain temperature / Steel / > 1570 K / 820 K / Stars

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Black-Body Radiation' into a causal sentence instead of repeating the slide title?

### Page 10 - Black-Body Radiation

Source cue: Stars / https://www.tec-science.com/thermodynamics/temperature/black-body-radiation/ 23/06/2026 10

Professor-style explanation: The slide 'Black-Body Radiation' introduces a concrete graphics object, operation, or relation. The named terms describe input data, a processing step, and an output used elsewhere in the rendering workflow. On the slide, the concrete items are: Stars / https://www.tec-science.com/thermodynamics/temperature/black-body-radiation/ 23/06/2026 10. The object-level relation is therefore input, operation, output, and the later graphics stage that consumes the output.

Technical commentary: This slide is about Black-Body Radiation. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: Stars / https://www.tec-science.com/thermodynamics/temperature/black-body-radiation/ 23/06/2026 10

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Black-Body Radiation' into a causal sentence instead of repeating the slide title?

### Page 11 - Spectral Density Function (SDF)

Source cue: - Light spectra are represented as spectral density functions / - Spectral density functions provide the light intensity (=energy) per wavelength / 400 Wavelength λ (nm) 700 / ygrenE / 400 Wavelength λ (nm) 700

Professor-style explanation: The slide 'Spectral Density Function (SDF)' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Light spectra are represented as spectral density functions / - Spectral density functions provide the light intensity (=energy) per wavelength / 400 Wavelength λ (nm) 700 / ygrenE / 400 Wavelength λ (nm) 700. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Spectral Density Function (SDF). The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Light spectra are represented as spectral density functions / - Spectral density functions provide the light intensity (=energy) per wavelength / 400 Wavelength λ (nm) 700 / ygrenE / 400 Wavelength λ (nm) 700

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Spectral Density Function (SDF)'?

### Page 12 - Light Perception

Source cue: - Humans perceive light spectra / as differently colored lights / - Often described using three / main properties (HSL/HSV model) / - Hue - primary color tone

Professor-style explanation: The slide 'Light Perception' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Humans perceive light spectra / as differently colored lights / - Often described using three / main properties (HSL/HSV model) / - Hue - primary color tone. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Light Perception. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Humans perceive light spectra / as differently colored lights / - Often described using three / main properties (HSL/HSV model) / - Hue - primary color tone

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Perception'?

### Page 13 - Interpreting SDFs

Source cue: - Shape of an SDF depicts how humans perceive represented light / - Hue: dominant wavelength / - Saturation: % of energy in dom. wavelength / - Luminance: total energy (SDF integral) / 400 Wavelength λ (nm) 700

Professor-style explanation: The slide 'Interpreting SDFs' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Shape of an SDF depicts how humans perceive represented light / - Hue: dominant wavelength / - Saturation: % of energy in dom. wavelength / - Luminance: total energy (SDF integral) / 400 Wavelength λ (nm) 700. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Interpreting SDFs. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Shape of an SDF depicts how humans perceive represented light / - Hue: dominant wavelength / - Saturation: % of energy in dom. wavelength / - Luminance: total energy (SDF integral) / 400 Wavelength λ (nm) 700

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Interpreting SDFs'?

### Page 14 - Representing SDFs

Source cue: - In spectral rendering SDFs are discretized as arrays / - Cell number represents differentiable wavelength ranges / - Cell values represent energy per wavelength range / - Much more frequently SDFs are represented as three-channel color / - HSL values are derived from SDF

Professor-style explanation: The slide 'Representing SDFs' explains visibility as the decision of which surface is seen from the current viewpoint. Some methods compare or sort objects, some subdivide image regions, some cast rays, and the depth buffer compares per-fragment depth values. On the slide, the concrete items are: - In spectral rendering SDFs are discretized as arrays / - Cell number represents differentiable wavelength ranges / - Cell values represent energy per wavelength range / - Much more frequently SDFs are represented as three-channel color / - HSL values are derived from SDF. The object-level relation is viewpoint, candidate surface, visibility test, and visible result.

Technical commentary: This slide is about Representing SDFs. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. Concrete items shown: - In spectral rendering SDFs are discretized as arrays / - Cell number represents differentiable wavelength ranges / - Cell values represent energy per wavelength range / - Much more frequently SDFs are represented as three-channel color / - HSL values are derived from SDF

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'Representing SDFs' works per object, per image region, per ray, or per fragment?

### Page 15 - 8.2 Light Sources

Source cue: How to represent light sources in computer graphics

Professor-style explanation: The slide '8.2 Light Sources' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: How to represent light sources in computer graphics. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about 8.2 Light Sources. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: How to represent light sources in computer graphics

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '8.2 Light Sources'?

### Page 16 - Light Sources

Source cue: - All light sources have a RGB color property representing their SDF / - Light sources are also defined through their location, orientation and extent / within a virtual scene / - Different light source types omit different spatial properties / - Light sources have no associated geometry

Professor-style explanation: The slide 'Light Sources' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - All light sources have a RGB color property representing their SDF / - Light sources are also defined through their location, orientation and extent / within a virtual scene / - Different light source types omit different spatial properties / - Light sources have no associated geometry. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Light Sources. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - All light sources have a RGB color property representing their SDF / - Light sources are also defined through their location, orientation and extent / within a virtual scene / - Different light source types omit different spatial properties / - Light sources have no associated geometry

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Sources'?

### Page 17 - Point Light Sources

Source cue: - Point light sources 𝐿 = 𝑃, 𝐶 have a geometric center 𝑃 = (x, y, z) / and radiate light with color 𝐶 = (𝑅, 𝐺, 𝐵) evenly in all directions

Professor-style explanation: The slide 'Point Light Sources' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Point light sources 𝐿 = 𝑃, 𝐶 have a geometric center 𝑃 = (x, y, z) / and radiate light with color 𝐶 = (𝑅, 𝐺, 𝐵) evenly in all directions. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Point Light Sources. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Point light sources 𝐿 = 𝑃, 𝐶 have a geometric center 𝑃 = (x, y, z) / and radiate light with color 𝐶 = (𝑅, 𝐺, 𝐵) evenly in all directions

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Point Light Sources'?

### Page 18 - Cone Light Sources

Source cue: - Special point light source with geometric center / - Radiation of light restricted to a cone-shaped area with its tip in the center / - Specified by cut-off angle and exponents for the decrease / of brightness with distance to the center / (spot light exponent)

Professor-style explanation: The slide 'Cone Light Sources' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Special point light source with geometric center / - Radiation of light restricted to a cone-shaped area with its tip in the center / - Specified by cut-off angle and exponents for the decrease / of brightness with distance to the center / (spot light exponent). The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Cone Light Sources. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Special point light source with geometric center / - Radiation of light restricted to a cone-shaped area with its tip in the center / - Specified by cut-off angle and exponents for the decrease / of brightness with distance to the center / (spot light exponent)

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Cone Light Sources'?

### Page 19 - Light Attenuation

Source cue: - Light attenuation is inversely proportional to the square / of the distance 𝑑 between the light source and the object / - Attenuation factor / 𝑓 = min , 1 / 𝑎𝑡𝑡 𝑐 + 𝑐 ⋅ 𝑑 + 𝑐 ⋅ 𝑑2

Professor-style explanation: The slide 'Light Attenuation' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Light attenuation is inversely proportional to the square / of the distance 𝑑 between the light source and the object / - Attenuation factor / 𝑓 = min , 1 / 𝑎𝑡𝑡 𝑐 + 𝑐 ⋅ 𝑑 + 𝑐 ⋅ 𝑑2. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Light Attenuation. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Light attenuation is inversely proportional to the square / of the distance 𝑑 between the light source and the object / - Attenuation factor / 𝑓 = min , 1 / 𝑎𝑡𝑡 𝑐 + 𝑐 ⋅ 𝑑 + 𝑐 ⋅ 𝑑2

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Attenuation'?

### Page 20 - Area Light Sources

Source cue: - Light source with geometric center and geometric extension / - Mostly of planar shape / - Transmission of light over the entire surface analogous to a point light source

Professor-style explanation: The slide 'Area Light Sources' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Light source with geometric center and geometric extension / - Mostly of planar shape / - Transmission of light over the entire surface analogous to a point light source. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Area Light Sources. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Light source with geometric center and geometric extension / - Mostly of planar shape / - Transmission of light over the entire surface analogous to a point light source

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Area Light Sources'?

### Page 21 - Directed Light

Source cue: - Infinity-far away imaginary light source / - Light rays run parallel and evenly throughout the scene, / direction is specified as a vector / - Light intensity does not diminish / with increasing distance

Professor-style explanation: The slide 'Directed Light' explains visibility as the decision of which surface is seen from the current viewpoint. Some methods compare or sort objects, some subdivide image regions, some cast rays, and the depth buffer compares per-fragment depth values. On the slide, the concrete items are: - Infinity-far away imaginary light source / - Light rays run parallel and evenly throughout the scene, / direction is specified as a vector / - Light intensity does not diminish / with increasing distance. The object-level relation is viewpoint, candidate surface, visibility test, and visible result.

Technical commentary: This slide is about Directed Light. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. Concrete items shown: - Infinity-far away imaginary light source / - Light rays run parallel and evenly throughout the scene, / direction is specified as a vector / - Light intensity does not diminish / with increasing distance

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'Directed Light' works per object, per image region, per ray, or per fragment?

### Page 22 - Local vs. Gobal Illumination

Source cue: - Simple case: Local lighting / - Consideration of direct illumination by light sources / (without obstacles or reflection) / - Simplified light models approximate / real lighting effect

Professor-style explanation: The slide 'Local vs. Gobal Illumination' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Simple case: Local lighting / - Consideration of direct illumination by light sources / (without obstacles or reflection) / - Simplified light models approximate / real lighting effect. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Local vs. Gobal Illumination. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Simple case: Local lighting / - Consideration of direct illumination by light sources / (without obstacles or reflection) / - Simplified light models approximate / real lighting effect

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Local vs. Gobal Illumination'?

### Page 23 - Ambient Light

Source cue: - Undirected light rays, evenly distributed / - Light intensity constant, regardless of distance / - Simulates general room brightness (basic brightness)

Professor-style explanation: The slide 'Ambient Light' explains visibility as the decision of which surface is seen from the current viewpoint. Some methods compare or sort objects, some subdivide image regions, some cast rays, and the depth buffer compares per-fragment depth values. On the slide, the concrete items are: - Undirected light rays, evenly distributed / - Light intensity constant, regardless of distance / - Simulates general room brightness (basic brightness). The object-level relation is viewpoint, candidate surface, visibility test, and visible result.

Technical commentary: This slide is about Ambient Light. The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint. Concrete items shown: - Undirected light rays, evenly distributed / - Light intensity constant, regardless of distance / - Simulates general room brightness (basic brightness)

Why it matters: Visibility decides which generated candidates are actually seen from the current viewpoint.

Check yourself: Can you decide whether 'Ambient Light' works per object, per image region, per ray, or per fragment?

### Page 24 - 8.3 Material Models

Source cue: How to represent materials in computer graphics

Professor-style explanation: The slide '8.3 Material Models' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: How to represent materials in computer graphics. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about 8.3 Material Models. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: How to represent materials in computer graphics

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '8.3 Material Models'?

### Page 25 - Material Models

Source cue: - Material models capture the different properties of materials / - Materials can have a wide variety of appearances / - Different groups of materials can be classified / based on appearance / - Metal – shiny and specular appearance

Professor-style explanation: The slide 'Material Models' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Material models capture the different properties of materials / - Materials can have a wide variety of appearances / - Different groups of materials can be classified / based on appearance / - Metal – shiny and specular appearance. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Material Models. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Material models capture the different properties of materials / - Materials can have a wide variety of appearances / - Different groups of materials can be classified / based on appearance / - Metal – shiny and specular appearance

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Material Models'?

### Page 26 - Materials vs. Textures

Source cue: - Material models specify the material properties for an infinitesimal surface / - No material variance with respect to location is supported / (i.e., structures such as wood grain cannot be represented) / - Textures are able to support material variance with respect to location

Professor-style explanation: The slide 'Materials vs. Textures' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Material models specify the material properties for an infinitesimal surface / - No material variance with respect to location is supported / (i.e., structures such as wood grain cannot be represented) / - Textures are able to support material variance with respect to location. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Materials vs. Textures. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Material models specify the material properties for an infinitesimal surface / - No material variance with respect to location is supported / (i.e., structures such as wood grain cannot be represented) / - Textures are able to support material variance with respect to location

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Materials vs. Textures'?

### Page 27 - Light Material Interaction 1/3

Source cue: - Material appearance is influenced by three wavelength-dependent effects / - Reflection – light energy bounces off / - Absorption – light energy is reduced / - Transmission – light passes through the object (refraction occurs) / R = reflected energy

Professor-style explanation: The slide 'Light Material Interaction 1/3' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Material appearance is influenced by three wavelength-dependent effects / - Reflection – light energy bounces off / - Absorption – light energy is reduced / - Transmission – light passes through the object (refraction occurs) / R = reflected energy. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Light Material Interaction 1/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Material appearance is influenced by three wavelength-dependent effects / - Reflection – light energy bounces off / - Absorption – light energy is reduced / - Transmission – light passes through the object (refraction occurs) / R = reflected energy

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Material Interaction 1/3'?

### Page 28 - Light Material Interaction 2/3

Source cue: - Material properties determine weight of the individual effects / opaque colored material opaque black material / A > 0 , T = 0, R > 0 A = I ,T = 0, R = 0 / perfect mirror material transparent material / A = 0, T = 0, R = I A ~= 0, R ~= 0, T ~= I

Professor-style explanation: The slide 'Light Material Interaction 2/3' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Material properties determine weight of the individual effects / opaque colored material opaque black material / A > 0 , T = 0, R > 0 A = I ,T = 0, R = 0 / perfect mirror material transparent material / A = 0, T = 0, R = I A ~= 0, R ~= 0, T ~= I. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Light Material Interaction 2/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Material properties determine weight of the individual effects / opaque colored material opaque black material / A > 0 , T = 0, R > 0 A = I ,T = 0, R = 0 / perfect mirror material transparent material / A = 0, T = 0, R = I A ~= 0, R ~= 0, T ~= I

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Material Interaction 2/3'?

### Page 29 - Light Material Interaction 3/3

Source cue: - Light-material interaction described by the Spectral Response Function (SRF) / 400 Wavelength λ (nm) 700 / ygrenE / 100% / All pass Filter ( ideal, real)

Professor-style explanation: The slide 'Light Material Interaction 3/3' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Light-material interaction described by the Spectral Response Function (SRF) / 400 Wavelength λ (nm) 700 / ygrenE / 100% / All pass Filter ( ideal, real). The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Light Material Interaction 3/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Light-material interaction described by the Spectral Response Function (SRF) / 400 Wavelength λ (nm) 700 / ygrenE / 100% / All pass Filter ( ideal, real)

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Light Material Interaction 3/3'?

### Page 30 - Reflection = SDF x SRF

Source cue: - Light-material interaction results are the product of the SDF and SRF / 100% × 100% / SDF SRF / 0% 0% / 400 Wavelength λ (nm) 700 400 Wavelength λ (nm) 700

Professor-style explanation: The slide 'Reflection = SDF x SRF' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Light-material interaction results are the product of the SDF and SRF / 100% × 100% / SDF SRF / 0% 0% / 400 Wavelength λ (nm) 700 400 Wavelength λ (nm) 700. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Reflection = SDF x SRF. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Light-material interaction results are the product of the SDF and SRF / 100% × 100% / SDF SRF / 0% 0% / 400 Wavelength λ (nm) 700 400 Wavelength λ (nm) 700

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Reflection = SDF x SRF'?

### Page 31 - Reflection Modeling 1/2

Source cue: - All light sources can be described by their Spectral Density Functions / - Natural light: sun, fire, ... / - Artificial light: light bulb, laser, neon tube, LED, ... / - All material properties can be described by Spectral Response Functions / - Glass, Water: SRF for transmission

Professor-style explanation: The slide 'Reflection Modeling 1/2' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - All light sources can be described by their Spectral Density Functions / - Natural light: sun, fire, ... / - Artificial light: light bulb, laser, neon tube, LED, ... / - All material properties can be described by Spectral Response Functions / - Glass, Water: SRF for transmission. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Reflection Modeling 1/2. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - All light sources can be described by their Spectral Density Functions / - Natural light: sun, fire, ... / - Artificial light: light bulb, laser, neon tube, LED, ... / - All material properties can be described by Spectral Response Functions / - Glass, Water: SRF for transmission

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Reflection Modeling 1/2'?

### Page 32 - Reflection Modeling 2/2

Source cue: - Synthetic and natural objects are in general not self-emitting / - Light is reflected at its surfaces, i.e., re-emitted into the scene / - Reflection is dependent on surface properties / - Rough surface: scattering of light / - Smooth surface: reflection of light

Professor-style explanation: The slide 'Reflection Modeling 2/2' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Synthetic and natural objects are in general not self-emitting / - Light is reflected at its surfaces, i.e., re-emitted into the scene / - Reflection is dependent on surface properties / - Rough surface: scattering of light / - Smooth surface: reflection of light. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Reflection Modeling 2/2. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Synthetic and natural objects are in general not self-emitting / - Light is reflected at its surfaces, i.e., re-emitted into the scene / - Reflection is dependent on surface properties / - Rough surface: scattering of light / - Smooth surface: reflection of light

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Reflection Modeling 2/2'?

### Page 33 - 8.4 Phong Illumination Model

Source cue: Determining the color of vertices

Professor-style explanation: The slide '8.4 Phong Illumination Model' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: Determining the color of vertices. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about 8.4 Phong Illumination Model. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: Determining the color of vertices

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to '8.4 Phong Illumination Model'?

### Page 34 - Empirical Observations

Source cue: - Light reflections are / - Dependent on the position of the observer / „... position of the observer...“ / - Dependent on the material properties of the surface / „… the specular properties of the object.“ Photo

Professor-style explanation: The slide 'Empirical Observations' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Light reflections are / - Dependent on the position of the observer / „... position of the observer...“ / - Dependent on the material properties of the surface / „… the specular properties of the object.“ Photo. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Empirical Observations. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Light reflections are / - Dependent on the position of the observer / „... position of the observer...“ / - Dependent on the material properties of the surface / „… the specular properties of the object.“ Photo

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Empirical Observations'?

### Page 35 - Illumination Models

Source cue: - Illumination models calculate the color of scene objects / based on the following properties / - Location – Position 𝑃 = (x, y, z) of the selected point 𝑃 / - Orientation – normal direction 𝑁 = (𝑛 , 𝑛 , 𝑛 ) of surface in 𝑃 / x y z

Professor-style explanation: The slide 'Illumination Models' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Illumination models calculate the color of scene objects / based on the following properties / - Location – Position 𝑃 = (x, y, z) of the selected point 𝑃 / - Orientation – normal direction 𝑁 = (𝑛 , 𝑛 , 𝑛 ) of surface in 𝑃 / x y z. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Illumination Models. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Illumination models calculate the color of scene objects / based on the following properties / - Location – Position 𝑃 = (x, y, z) of the selected point 𝑃 / - Orientation – normal direction 𝑁 = (𝑛 , 𝑛 , 𝑛 ) of surface in 𝑃 / x y z

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Illumination Models'?

### Page 36 - yaR

Source cue: thgiL / Diffuse Intensity 1/3 / - Simulation of light reflections on diffuse surfaces / - Model assumption / - Diffuse light reflections are non-directional (scattering)

Professor-style explanation: The slide 'yaR' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: thgiL / Diffuse Intensity 1/3 / - Simulation of light reflections on diffuse surfaces / - Model assumption / - Diffuse light reflections are non-directional (scattering). The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about yaR. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: thgiL / Diffuse Intensity 1/3 / - Simulation of light reflections on diffuse surfaces / - Model assumption / - Diffuse light reflections are non-directional (scattering)

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'yaR'?

### Page 37 - Diffuse Intensity 2/3

Source cue: - Equation / 𝐼 = 𝑙𝑘⋅ 𝑛⋅ 𝐿 ⋅ max( 0, ) / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑 / - 𝑘 diffuse material properties (surface dependent) / - 𝐿 diffuse light intensity (light source dependent)

Professor-style explanation: The slide 'Diffuse Intensity 2/3' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Equation / 𝐼 = 𝑙𝑘⋅ 𝑛⋅ 𝐿 ⋅ max( 0, ) / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑 / - 𝑘 diffuse material properties (surface dependent) / - 𝐿 diffuse light intensity (light source dependent). The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Diffuse Intensity 2/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Equation / 𝐼 = 𝑙𝑘⋅ 𝑛⋅ 𝐿 ⋅ max( 0, ) / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑 / - 𝑘 diffuse material properties (surface dependent) / - 𝐿 diffuse light intensity (light source dependent)

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Diffuse Intensity 2/3'?

### Page 38 - Diffuse Intensity 3/3

Source cue: 𝐼 = 𝑘 ⋅ 𝐿 ⋅ 𝑚𝑎x(0, 𝑙⃗ ⋅ 𝑛) / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑 / https://bit.ly/2XFhbcM / Extrahierte Tabellen: / [Tabelle 1]

Professor-style explanation: The slide 'Diffuse Intensity 3/3' introduces a concrete graphics object, operation, or relation. The named terms describe input data, a processing step, and an output used elsewhere in the rendering workflow. On the slide, the concrete items are: 𝐼 = 𝑘 ⋅ 𝐿 ⋅ 𝑚𝑎x(0, 𝑙⃗ ⋅ 𝑛) / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑 / https://bit.ly/2XFhbcM / Extrahierte Tabellen: / [Tabelle 1]. The object-level relation is therefore input, operation, output, and the later graphics stage that consumes the output.

Technical commentary: This slide is about Diffuse Intensity 3/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: 𝐼 = 𝑘 ⋅ 𝐿 ⋅ 𝑚𝑎x(0, 𝑙⃗ ⋅ 𝑛) / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑 / https://bit.ly/2XFhbcM / Extrahierte Tabellen: / [Tabelle 1]

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Diffuse Intensity 3/3' into a causal sentence instead of repeating the slide title?

### Page 39 - Ambient Intensity 1/2

Source cue: - Simulation of the general room brightness / - Indirect light incidence or multiple reflections / - Model assumptions / - Constant influence on all scene objects / - No influence of position or alignment

Professor-style explanation: The slide 'Ambient Intensity 1/2' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Simulation of the general room brightness / - Indirect light incidence or multiple reflections / - Model assumptions / - Constant influence on all scene objects / - No influence of position or alignment. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Ambient Intensity 1/2. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Simulation of the general room brightness / - Indirect light incidence or multiple reflections / - Model assumptions / - Constant influence on all scene objects / - No influence of position or alignment

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Ambient Intensity 1/2'?

### Page 40 - Ambient Intensity 2/2

Source cue: 𝐼 = 𝑘 ⋅ 𝐿 / 𝑎𝑚𝑏𝑖𝑒𝑛𝑡 𝑎 𝑎 / https://bit.ly/2XGn61n / Extrahierte Tabellen: / [Tabelle 1]

Professor-style explanation: The slide 'Ambient Intensity 2/2' introduces a concrete graphics object, operation, or relation. The named terms describe input data, a processing step, and an output used elsewhere in the rendering workflow. On the slide, the concrete items are: 𝐼 = 𝑘 ⋅ 𝐿 / 𝑎𝑚𝑏𝑖𝑒𝑛𝑡 𝑎 𝑎 / https://bit.ly/2XGn61n / Extrahierte Tabellen: / [Tabelle 1]. The object-level relation is therefore input, operation, output, and the later graphics stage that consumes the output.

Technical commentary: This slide is about Ambient Intensity 2/2. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: 𝐼 = 𝑘 ⋅ 𝐿 / 𝑎𝑚𝑏𝑖𝑒𝑛𝑡 𝑎 𝑎 / https://bit.ly/2XGn61n / Extrahierte Tabellen: / [Tabelle 1]

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Ambient Intensity 2/2' into a causal sentence instead of repeating the slide title?

### Page 41 - Specular Intensity 1/3

Source cue: - Simulation of light reflections on specular surfaces / - Model assumption / - Reflection of light are directed (reflection) / - Observations / - Reflections of light are observer-dependent

Professor-style explanation: The slide 'Specular Intensity 1/3' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Simulation of light reflections on specular surfaces / - Model assumption / - Reflection of light are directed (reflection) / - Observations / - Reflections of light are observer-dependent. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Specular Intensity 1/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Simulation of light reflections on specular surfaces / - Model assumption / - Reflection of light are directed (reflection) / - Observations / - Reflections of light are observer-dependent

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Specular Intensity 1/3'?

### Page 42 - Reflection Vector 𝑟⃗

Source cue: - Calculation of the reflection vector / - Incidence angle corresponds to exit angle / - Equation / ⃗ ⃗ / 𝑟⃗ = 2𝑛 ⋅⋅ 𝑛 ⋅ 𝑙 − 𝑙

Professor-style explanation: The slide 'Reflection Vector 𝑟⃗' introduces a concrete graphics object, operation, or relation. The named terms describe input data, a processing step, and an output used elsewhere in the rendering workflow. On the slide, the concrete items are: - Calculation of the reflection vector / - Incidence angle corresponds to exit angle / - Equation / ⃗ ⃗ / 𝑟⃗ = 2𝑛 ⋅⋅ 𝑛 ⋅ 𝑙 − 𝑙. The object-level relation is therefore input, operation, output, and the later graphics stage that consumes the output.

Technical commentary: This slide is about Reflection Vector 𝑟⃗. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: - Calculation of the reflection vector / - Incidence angle corresponds to exit angle / - Equation / ⃗ ⃗ / 𝑟⃗ = 2𝑛 ⋅⋅ 𝑛 ⋅ 𝑙 − 𝑙

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Reflection Vector 𝑟⃗' into a causal sentence instead of repeating the slide title?

### Page 43 - Specular Intensity 2/3

Source cue: - Equation / 𝐼 = 𝑘𝑟⃗ ⋅ ⋅𝑣⃗ 𝐿 ⋅ max( 0, ) / 𝑠𝑝𝑒𝑐𝑢𝑙𝑎𝑟 𝑠 𝑠 / - 𝑘 specular material properties (surface dependant) / - 𝐿 specular light intensity (light source dependent)

Professor-style explanation: The slide 'Specular Intensity 2/3' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Equation / 𝐼 = 𝑘𝑟⃗ ⋅ ⋅𝑣⃗ 𝐿 ⋅ max( 0, ) / 𝑠𝑝𝑒𝑐𝑢𝑙𝑎𝑟 𝑠 𝑠 / - 𝑘 specular material properties (surface dependant) / - 𝐿 specular light intensity (light source dependent). The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Specular Intensity 2/3. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Equation / 𝐼 = 𝑘𝑟⃗ ⋅ ⋅𝑣⃗ 𝐿 ⋅ max( 0, ) / 𝑠𝑝𝑒𝑐𝑢𝑙𝑎𝑟 𝑠 𝑠 / - 𝑘 specular material properties (surface dependant) / - 𝐿 specular light intensity (light source dependent)

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Specular Intensity 2/3'?

### Page 44 - Specular Exponent 𝑝

Source cue: - 𝑝 influences fall off of specular highlight (𝑝 ∊ [1, 𝑀] mit 𝑀 ≈ 100) / 𝑝 = 1 / 𝑚𝑎x(0, 𝑟⃗ ⋅ 𝑣⃗)1 / 𝑝 = 5 / 𝑚𝑎x(0, 𝑟⃗ ⋅ 𝑣⃗)5

Professor-style explanation: The slide 'Specular Exponent 𝑝' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - 𝑝 influences fall off of specular highlight (𝑝 ∊ [1, 𝑀] mit 𝑀 ≈ 100) / 𝑝 = 1 / 𝑚𝑎x(0, 𝑟⃗ ⋅ 𝑣⃗)1 / 𝑝 = 5 / 𝑚𝑎x(0, 𝑟⃗ ⋅ 𝑣⃗)5. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Specular Exponent 𝑝. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - 𝑝 influences fall off of specular highlight (𝑝 ∊ [1, 𝑀] mit 𝑀 ≈ 100) / 𝑝 = 1 / 𝑚𝑎x(0, 𝑟⃗ ⋅ 𝑣⃗)1 / 𝑝 = 5 / 𝑚𝑎x(0, 𝑟⃗ ⋅ 𝑣⃗)5

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Specular Exponent 𝑝'?

### Page 45 - Specular Intensity 3/3

Source cue: 𝑟⃗ = 2 ⋅ 𝑛 ⋅ 𝑛 ⋅ 𝑙⃗ − 𝑙⃗ / https://bit.ly/2XbPc7s 𝐼 = 𝑘 ⋅ 𝐿 ⋅ 𝑚𝑎x(0, 𝑟⃗ ⋅ 𝑣⃗)𝑝 / 𝑠𝑝𝑒𝑐𝑢𝑙𝑎𝑟 𝑠 𝑠 / Extrahierte Tabellen: / [Tabelle 1]

Professor-style explanation: The slide 'Specular Intensity 3/3' introduces a concrete graphics object, operation, or relation. The named terms describe input data, a processing step, and an output used elsewhere in the rendering workflow. On the slide, the concrete items are: 𝑟⃗ = 2 ⋅ 𝑛 ⋅ 𝑛 ⋅ 𝑙⃗ − 𝑙⃗ / https://bit.ly/2XbPc7s 𝐼 = 𝑘 ⋅ 𝐿 ⋅ 𝑚𝑎x(0, 𝑟⃗ ⋅ 𝑣⃗)𝑝 / 𝑠𝑝𝑒𝑐𝑢𝑙𝑎𝑟 𝑠 𝑠 / Extrahierte Tabellen: / [Tabelle 1]. The object-level relation is therefore input, operation, output, and the later graphics stage that consumes the output.

Technical commentary: This slide is about Specular Intensity 3/3. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: 𝑟⃗ = 2 ⋅ 𝑛 ⋅ 𝑛 ⋅ 𝑙⃗ − 𝑙⃗ / https://bit.ly/2XbPc7s 𝐼 = 𝑘 ⋅ 𝐿 ⋅ 𝑚𝑎x(0, 𝑟⃗ ⋅ 𝑣⃗)𝑝 / 𝑠𝑝𝑒𝑐𝑢𝑙𝑎𝑟 𝑠 𝑠 / Extrahierte Tabellen: / [Tabelle 1]

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Specular Intensity 3/3' into a causal sentence instead of repeating the slide title?

### Page 46 - Blinn-Phong Illumination Model 1/2

Source cue: - Alternative simulation of specular relfections / - Replace mirror direction 𝑟⃗ with Halfway-Vector ℎ / - ℎ = 𝑙 + 𝑣⃗ / - ℎ is halfway between 𝑙 and 𝑣⃗ / - Equation

Professor-style explanation: The slide 'Blinn-Phong Illumination Model 1/2' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Alternative simulation of specular relfections / - Replace mirror direction 𝑟⃗ with Halfway-Vector ℎ / - ℎ = 𝑙 + 𝑣⃗ / - ℎ is halfway between 𝑙 and 𝑣⃗ / - Equation. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Blinn-Phong Illumination Model 1/2. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Alternative simulation of specular relfections / - Replace mirror direction 𝑟⃗ with Halfway-Vector ℎ / - ℎ = 𝑙 + 𝑣⃗ / - ℎ is halfway between 𝑙 and 𝑣⃗ / - Equation

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Blinn-Phong Illumination Model 1/2'?

### Page 47 - Blinn-Phong Illumination Model 2/2

Source cue: ℎ = 𝑙⃗ + 𝑣⃗ / https://bit.ly/2ICDwBD 𝐼 = 𝑘 ⋅ 𝐿 ⋅ 𝑚𝑎x(0, ℎ ⋅ 𝑛)𝑝 / 𝑠𝑝𝑒𝑐𝑢𝑙𝑎𝑟 𝑠 𝑠 / Extrahierte Tabellen: / [Tabelle 1]

Professor-style explanation: The slide 'Blinn-Phong Illumination Model 2/2' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: ℎ = 𝑙⃗ + 𝑣⃗ / https://bit.ly/2ICDwBD 𝐼 = 𝑘 ⋅ 𝐿 ⋅ 𝑚𝑎x(0, ℎ ⋅ 𝑛)𝑝 / 𝑠𝑝𝑒𝑐𝑢𝑙𝑎𝑟 𝑠 𝑠 / Extrahierte Tabellen: / [Tabelle 1]. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Blinn-Phong Illumination Model 2/2. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: ℎ = 𝑙⃗ + 𝑣⃗ / https://bit.ly/2ICDwBD 𝐼 = 𝑘 ⋅ 𝐿 ⋅ 𝑚𝑎x(0, ℎ ⋅ 𝑛)𝑝 / 𝑠𝑝𝑒𝑐𝑢𝑙𝑎𝑟 𝑠 𝑠 / Extrahierte Tabellen: / [Tabelle 1]

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Blinn-Phong Illumination Model 2/2'?

### Page 48 - Phong Illumination Model

Source cue: - Additive combination of all factors / 𝐼 = 𝑘 ⋅ 𝐿 / 𝑎𝑚𝑏𝑖𝑒𝑛𝑡 𝑎 𝑎 / 𝐼 = 𝑘 ⋅ 𝐿 ⋅ max 0, 𝑛 ⋅ 𝑙 / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑

Professor-style explanation: The slide 'Phong Illumination Model' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Additive combination of all factors / 𝐼 = 𝑘 ⋅ 𝐿 / 𝑎𝑚𝑏𝑖𝑒𝑛𝑡 𝑎 𝑎 / 𝐼 = 𝑘 ⋅ 𝐿 ⋅ max 0, 𝑛 ⋅ 𝑙 / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Phong Illumination Model. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Additive combination of all factors / 𝐼 = 𝑘 ⋅ 𝐿 / 𝑎𝑚𝑏𝑖𝑒𝑛𝑡 𝑎 𝑎 / 𝐼 = 𝑘 ⋅ 𝐿 ⋅ max 0, 𝑛 ⋅ 𝑙 / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Phong Illumination Model'?

### Page 49 - Phong Illumination Model

Source cue: - Additive combination of all factors / 𝐼 = 𝑘 ⋅ 𝐿 / 𝑎𝑚𝑏𝑖𝑒𝑛𝑡 𝑎 𝑎 / 𝐼 = 𝑘 ⋅ 𝐿 ⋅ max 0, 𝑛 ⋅ 𝑙 / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑

Professor-style explanation: The slide 'Phong Illumination Model' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Additive combination of all factors / 𝐼 = 𝑘 ⋅ 𝐿 / 𝑎𝑚𝑏𝑖𝑒𝑛𝑡 𝑎 𝑎 / 𝐼 = 𝑘 ⋅ 𝐿 ⋅ max 0, 𝑛 ⋅ 𝑙 / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Phong Illumination Model. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Additive combination of all factors / 𝐼 = 𝑘 ⋅ 𝐿 / 𝑎𝑚𝑏𝑖𝑒𝑛𝑡 𝑎 𝑎 / 𝐼 = 𝑘 ⋅ 𝐿 ⋅ max 0, 𝑛 ⋅ 𝑙 / 𝑑𝑖𝑓𝑓𝑢𝑠𝑒 𝑑 𝑑

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Phong Illumination Model'?

### Page 50 - 8.5 Shading

Source cue: Coloring triangles when using vertex-based illumination

Professor-style explanation: The slide '8.5 Shading' explains the conversion from continuous geometry to a discrete sample grid. A mathematical line, triangle, or region is tested against pixel/sample positions. Covered samples become fragments, and attributes such as depth, color, normals, or texture coordinates can be interpolated across the primitive. On the slide, the concrete items are: Coloring triangles when using vertex-based illumination. Rasterization creates fragment candidates; later tests decide whether those candidates become visible pixel updates.

Technical commentary: This slide is about 8.5 Shading. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: Coloring triangles when using vertex-based illumination

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by '8.5 Shading'?

### Page 51 - Shading

Source cue: - Illumination model usually applied in the fragment stage / - Vertex-based illumination also possible to save compute / - Requires to spread the illumination information of the vertices / over the triangle / Flat Gouroud Phong

Professor-style explanation: The slide 'Shading' explains the conversion from continuous geometry to a discrete sample grid. A mathematical line, triangle, or region is tested against pixel/sample positions. Covered samples become fragments, and attributes such as depth, color, normals, or texture coordinates can be interpolated across the primitive. On the slide, the concrete items are: - Illumination model usually applied in the fragment stage / - Vertex-based illumination also possible to save compute / - Requires to spread the illumination information of the vertices / over the triangle / Flat Gouroud Phong. Rasterization creates fragment candidates; later tests decide whether those candidates become visible pixel updates.

Technical commentary: This slide is about Shading. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: - Illumination model usually applied in the fragment stage / - Vertex-based illumination also possible to save compute / - Requires to spread the illumination information of the vertices / over the triangle / Flat Gouroud Phong

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Shading'?

### Page 52 - Shading Computation

Source cue: - Tasks of shading procedures / - Colorize surfaces based on colors calculated by illumination model / - Shading is closely linked to the rasterization process and integrated into it / - Distribute lighting and shading / - Calculate light intensity for surface points

Professor-style explanation: The slide 'Shading Computation' explains the conversion from continuous geometry to a discrete sample grid. A mathematical line, triangle, or region is tested against pixel/sample positions. Covered samples become fragments, and attributes such as depth, color, normals, or texture coordinates can be interpolated across the primitive. On the slide, the concrete items are: - Tasks of shading procedures / - Colorize surfaces based on colors calculated by illumination model / - Shading is closely linked to the rasterization process and integrated into it / - Distribute lighting and shading / - Calculate light intensity for surface points. Rasterization creates fragment candidates; later tests decide whether those candidates become visible pixel updates.

Technical commentary: This slide is about Shading Computation. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: - Tasks of shading procedures / - Colorize surfaces based on colors calculated by illumination model / - Shading is closely linked to the rasterization process and integrated into it / - Distribute lighting and shading / - Calculate light intensity for surface points

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Shading Computation'?

### Page 53 - Flat Shading

Source cue: - Operation / - Calling the lighting model for a single point of a surface / (e.g., polygon center) / - Shading of the entire polygon in the determined intensity / - Useful if the following assumptions apply

Professor-style explanation: The slide 'Flat Shading' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Operation / - Calling the lighting model for a single point of a surface / (e.g., polygon center) / - Shading of the entire polygon in the determined intensity / - Useful if the following assumptions apply. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Flat Shading. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Operation / - Calling the lighting model for a single point of a surface / (e.g., polygon center) / - Shading of the entire polygon in the determined intensity / - Useful if the following assumptions apply

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Flat Shading'?

### Page 54 - Gouraud Shading 1/5

Source cue: - Shading method for polygons based on the interpolation / of intensity values a t the polygon vertices / - Requirements / - Area decomposition in polygons (usually triangles) / - Normals for polygon corners (vertex normals)

Professor-style explanation: The slide 'Gouraud Shading 1/5' explains the conversion from continuous geometry to a discrete sample grid. A mathematical line, triangle, or region is tested against pixel/sample positions. Covered samples become fragments, and attributes such as depth, color, normals, or texture coordinates can be interpolated across the primitive. On the slide, the concrete items are: - Shading method for polygons based on the interpolation / of intensity values a t the polygon vertices / - Requirements / - Area decomposition in polygons (usually triangles) / - Normals for polygon corners (vertex normals). Rasterization creates fragment candidates; later tests decide whether those candidates become visible pixel updates.

Technical commentary: This slide is about Gouraud Shading 1/5. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: - Shading method for polygons based on the interpolation / of intensity values a t the polygon vertices / - Requirements / - Area decomposition in polygons (usually triangles) / - Normals for polygon corners (vertex normals)

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Gouraud Shading 1/5'?

### Page 55 - Gouraud Shading 2/5

Source cue: - Proceeding / - Compute intensity values 𝑙 for polygon corners 𝑣 / 𝑖 𝑖 / - Linear interpolation of the intensity values a long the edges / - Linear interpolation of the intensity values a long the scanlines

Professor-style explanation: The slide 'Gouraud Shading 2/5' explains the conversion from continuous geometry to a discrete sample grid. A mathematical line, triangle, or region is tested against pixel/sample positions. Covered samples become fragments, and attributes such as depth, color, normals, or texture coordinates can be interpolated across the primitive. On the slide, the concrete items are: - Proceeding / - Compute intensity values 𝑙 for polygon corners 𝑣 / 𝑖 𝑖 / - Linear interpolation of the intensity values a long the edges / - Linear interpolation of the intensity values a long the scanlines. Rasterization creates fragment candidates; later tests decide whether those candidates become visible pixel updates.

Technical commentary: This slide is about Gouraud Shading 2/5. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: - Proceeding / - Compute intensity values 𝑙 for polygon corners 𝑣 / 𝑖 𝑖 / - Linear interpolation of the intensity values a long the edges / - Linear interpolation of the intensity values a long the scanlines

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Gouraud Shading 2/5'?

### Page 56 - Gouraud Shading 3/5

Source cue: - Shading at conceptually smooth transitions / - Geometrically "hard" edges instead of conceptually "soft" edges / - Gouraud shading can create visually smooth transitions / through smooth shading / - Example: 𝑃 / 𝑃 smooth transition, 𝑃 / 𝑃 hard transition

Professor-style explanation: The slide 'Gouraud Shading 3/5' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Shading at conceptually smooth transitions / - Geometrically "hard" edges instead of conceptually "soft" edges / - Gouraud shading can create visually smooth transitions / through smooth shading / - Example: 𝑃 / 𝑃 smooth transition, 𝑃 / 𝑃 hard transition. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Gouraud Shading 3/5. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Shading at conceptually smooth transitions / - Geometrically "hard" edges instead of conceptually "soft" edges / - Gouraud shading can create visually smooth transitions / through smooth shading / - Example: 𝑃 / 𝑃 smooth transition, 𝑃 / 𝑃 hard transition

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Gouraud Shading 3/5'?

### Page 57 - Gouraud Shading 4/5

Source cue: - interpolation problems / - The shading inside a triangle results from interpolation / - Intensity fluctuations in the interior are not taken into account / - Intensity fluctuations can only be considered by finer tessellation / - Example: Spotlight shines into the interior of a triangle

Professor-style explanation: The slide 'Gouraud Shading 4/5' explains the conversion from continuous geometry to a discrete sample grid. A mathematical line, triangle, or region is tested against pixel/sample positions. Covered samples become fragments, and attributes such as depth, color, normals, or texture coordinates can be interpolated across the primitive. On the slide, the concrete items are: - interpolation problems / - The shading inside a triangle results from interpolation / - Intensity fluctuations in the interior are not taken into account / - Intensity fluctuations can only be considered by finer tessellation / - Example: Spotlight shines into the interior of a triangle. Rasterization creates fragment candidates; later tests decide whether those candidates become visible pixel updates.

Technical commentary: This slide is about Gouraud Shading 4/5. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: - interpolation problems / - The shading inside a triangle results from interpolation / - Intensity fluctuations in the interior are not taken into account / - Intensity fluctuations can only be considered by finer tessellation / - Example: Spotlight shines into the interior of a triangle

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Gouraud Shading 4/5'?

### Page 58 - Gouraud Shading 5/5

Source cue: - Interpolation problems / - Contiguous polygons that do not fully share the same edges / will be shaded differently

Professor-style explanation: The slide 'Gouraud Shading 5/5' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Interpolation problems / - Contiguous polygons that do not fully share the same edges / will be shaded differently. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Gouraud Shading 5/5. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Interpolation problems / - Contiguous polygons that do not fully share the same edges / will be shaded differently

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Gouraud Shading 5/5'?

### Page 59 - Phong Shading 1/2

Source cue: - Interpolation of the corner normals instead of the corner intensities / - Proceeding / - Calculation of the corner normals / - Interpolation of the normals between the corners / - Interpolation between the endpoints of a scanline

Professor-style explanation: The slide 'Phong Shading 1/2' explains the conversion from continuous geometry to a discrete sample grid. A mathematical line, triangle, or region is tested against pixel/sample positions. Covered samples become fragments, and attributes such as depth, color, normals, or texture coordinates can be interpolated across the primitive. On the slide, the concrete items are: - Interpolation of the corner normals instead of the corner intensities / - Proceeding / - Calculation of the corner normals / - Interpolation of the normals between the corners / - Interpolation between the endpoints of a scanline. Rasterization creates fragment candidates; later tests decide whether those candidates become visible pixel updates.

Technical commentary: This slide is about Phong Shading 1/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: - Interpolation of the corner normals instead of the corner intensities / - Proceeding / - Calculation of the corner normals / - Interpolation of the normals between the corners / - Interpolation between the endpoints of a scanline

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Phong Shading 1/2'?

### Page 60 - Phong Shading 2/2

Source cue: - Advantages / - Pixel-based (i.e., image-precise) evaluation of the light sources / - Highly focused highlights at corners are not interpolated over the edge / - Highlights inside a triangle can be displayed / - Disadvantage

Professor-style explanation: The slide 'Phong Shading 2/2' explains the conversion from continuous geometry to a discrete sample grid. A mathematical line, triangle, or region is tested against pixel/sample positions. Covered samples become fragments, and attributes such as depth, color, normals, or texture coordinates can be interpolated across the primitive. On the slide, the concrete items are: - Advantages / - Pixel-based (i.e., image-precise) evaluation of the light sources / - Highly focused highlights at corners are not interpolated over the edge / - Highlights inside a triangle can be displayed / - Disadvantage. Rasterization creates fragment candidates; later tests decide whether those candidates become visible pixel updates.

Technical commentary: This slide is about Phong Shading 2/2. The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes. Concrete items shown: - Advantages / - Pixel-based (i.e., image-precise) evaluation of the light sources / - Highly focused highlights at corners are not interpolated over the edge / - Highlights inside a triangle can be displayed / - Disadvantage

Why it matters: Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.

Check yourself: Can you explain which samples/fragments are generated by 'Phong Shading 2/2'?

### Page 61 - Literature and other sources used in this chapter

Source cue: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Professor-style explanation: The slide 'Literature and other sources used in this chapter' introduces a concrete graphics object, operation, or relation. The named terms describe input data, a processing step, and an output used elsewhere in the rendering workflow. On the slide, the concrete items are: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content. The object-level relation is therefore input, operation, output, and the later graphics stage that consumes the output.

Technical commentary: This slide is about Literature and other sources used in this chapter. The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume. Concrete items shown: No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Literature and other sources used in this chapter' into a causal sentence instead of repeating the slide title?

### Page 62 - Lesen und Ausprobieren

Source cue: - Zum Lesen - Zum Ausprobieren / Marschner, Steve und Peter Shirley: / - Simulation von drei / Fundamentals of Computer Graphics, / ausgewählten Materialien

Professor-style explanation: The slide 'Lesen und Ausprobieren' explains local illumination at a surface point. The surface normal defines orientation, the light vector defines incoming light, the view vector defines the observer, and material parameters scale ambient, diffuse, or specular terms. On the slide, the concrete items are: - Zum Lesen - Zum Ausprobieren / Marschner, Steve und Peter Shirley: / - Simulation von drei / Fundamentals of Computer Graphics, / ausgewählten Materialien. The object-level relation is light source, surface point, material response, and computed color.

Technical commentary: This slide is about Lesen und Ausprobieren. The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color. Concrete items shown: - Zum Lesen - Zum Ausprobieren / Marschner, Steve und Peter Shirley: / - Simulation von drei / Fundamentals of Computer Graphics, / ausgewählten Materialien

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Lesen und Ausprobieren'?

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
