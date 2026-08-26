# Lecture 03 - Geometric Transformations

Source chunk: `course_text_parts/03_lectures/03_geometric-transformations.txt`
Extracted slide pages in source chunk: 54

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture explains how geometry moves between coordinate systems. Almost every later topic assumes that you can track where a point or vector currently lives.

## How To Read This Lecture

- First read the big picture and the mental models.
- Then open the source chunk and compare the slide bullets to the commentary.
- After each section, answer the check question without notes.
- If the check feels vague, revisit the source pages listed for that section.

## Per-Slide Commentary

Every extracted slide page gets its own reading note. This is the part to use when the original PDF is too terse or visually dense.

### Page 1 - Untitled slide

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Professor-style explanation: For 'Untitled slide', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Untitled slide. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Untitled slide' into a causal sentence instead of repeating the slide title?

### Page 2 - Transforming 3D Models

Source cue: - 3D models need to be positioned and oriented in the virtual world / (sometimes scaling and other modifications are necessary) / - These modifications are performed by applying transformations to the / vertices describing a 3D model / - Transformations are applied through

Professor-style explanation: For 'Transforming 3D Models', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - 3D models need to be positioned and oriented in the virtual world / (sometimes scaling and other modifications are necessary) / - These modifications are performed by applying transformations to the / vertices describing a 3D model / - Transformations are applied through. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Transforming 3D Models. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - 3D models need to be positioned and oriented in the virtual world / (sometimes scaling and other modifications are necessary) / - These modifications are performed by applying transformations to the / vertices describing a 3D model / - Transformations are applied through

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Transforming 3D Models'?

### Page 3 - 3.1 Mathematical Foundations

Source cue: 3.2 Affine Transformations / 3.3 Composition of Transformations / 3.4 Coordinate System Change / 3.5 Transformations in OpenGL

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. '3.1 Mathematical Foundations' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: 3.2 Affine Transformations / 3.3 Composition of Transformations / 3.4 Coordinate System Change / 3.5 Transformations in OpenGL. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about 3.1 Mathematical Foundations. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: 3.2 Affine Transformations / 3.3 Composition of Transformations / 3.4 Coordinate System Change / 3.5 Transformations in OpenGL

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '3.1 Mathematical Foundations'?

### Page 4 - 3.1 Mathematical Foundations

Source cue: Vector and Matrix Calculus

Professor-style explanation: For '3.1 Mathematical Foundations', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: Vector and Matrix Calculus. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about 3.1 Mathematical Foundations. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: Vector and Matrix Calculus

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after '3.1 Mathematical Foundations'?

### Page 5 - Vertices as Vectors

Source cue: - Vectors are used to represent geometric objects (coordinates) / - Vectors have real numbers as components, so they are elements of ℝ2, ℝ3 , ℝ4 / - In computer graphics mostly ℝ3 or ℝ4 vectors used / - Vertices of a polygon are represented as column vectors / x 𝑣

Professor-style explanation: For 'Vertices as Vectors', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Vectors are used to represent geometric objects (coordinates) / - Vectors have real numbers as components, so they are elements of ℝ2, ℝ3 , ℝ4 / - In computer graphics mostly ℝ3 or ℝ4 vectors used / - Vertices of a polygon are represented as column vectors / x 𝑣. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Vertices as Vectors. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Vectors are used to represent geometric objects (coordinates) / - Vectors have real numbers as components, so they are elements of ℝ2, ℝ3 , ℝ4 / - In computer graphics mostly ℝ3 or ℝ4 vectors used / - Vertices of a polygon are represented as column vectors / x 𝑣

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Vertices as Vectors'?

### Page 6 - Transformations as Matrices

Source cue: - Matrices are used to represent transformations / - In computer graphics mainly 4 × 4 square matrices are used / 𝑎 𝑏 𝑐 𝑑 / 𝑒 𝑓 𝑔 ℎ / 𝑀 =

Professor-style explanation: For 'Transformations as Matrices', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Matrices are used to represent transformations / - In computer graphics mainly 4 × 4 square matrices are used / 𝑎 𝑏 𝑐 𝑑 / 𝑒 𝑓 𝑔 ℎ / 𝑀 =. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Transformations as Matrices. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Matrices are used to represent transformations / - In computer graphics mainly 4 × 4 square matrices are used / 𝑎 𝑏 𝑐 𝑑 / 𝑒 𝑓 𝑔 ℎ / 𝑀 =

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Transformations as Matrices'?

### Page 7 - Matrix Vector Multiplication

Source cue: - Since vectors describe vertices and matrices describe transformations, / transformations can be applied through matrix vector multiplication / - Input: 𝑚 × 𝑛 matrix 𝐴 and ℝm vector 𝐵 / - Result: ℝn vector 𝐶, whereby is 𝐵 transformed through 𝐴 / - Example for 4 × 4 matrix 𝐴 and ℝ4 vector 𝐵:

Professor-style explanation: For 'Matrix Vector Multiplication', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Since vectors describe vertices and matrices describe transformations, / transformations can be applied through matrix vector multiplication / - Input: 𝑚 × 𝑛 matrix 𝐴 and ℝm vector 𝐵 / - Result: ℝn vector 𝐶, whereby is 𝐵 transformed through 𝐴 / - Example for 4 × 4 matrix 𝐴 and ℝ4 vector 𝐵. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Matrix Vector Multiplication. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Since vectors describe vertices and matrices describe transformations, / transformations can be applied through matrix vector multiplication / - Input: 𝑚 × 𝑛 matrix 𝐴 and ℝm vector 𝐵 / - Result: ℝn vector 𝐶, whereby is 𝐵 transformed through 𝐴 / - Example for 4 × 4 matrix 𝐴 and ℝ4 vector 𝐵:

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Matrix Vector Multiplication'?

### Page 8 - 3.2 Affine Transformations

Source cue: Translation, Rotation, Scaling, and more

Professor-style explanation: For '3.2 Affine Transformations', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: Translation, Rotation, Scaling, and more. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about 3.2 Affine Transformations. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: Translation, Rotation, Scaling, and more

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after '3.2 Affine Transformations'?

### Page 9 - Translations – Moving 3D Models

Source cue: - Matrix representation of a translation / 1 0 0 𝑑 / 0 1 0 𝑑 / 𝑇 𝑑 , 𝑑 , 𝑑 = / x y z

Professor-style explanation: For 'Translations – Moving 3D Models', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Matrix representation of a translation / 1 0 0 𝑑 / 0 1 0 𝑑 / 𝑇 𝑑 , 𝑑 , 𝑑 = / x y z. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Translations – Moving 3D Models. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Matrix representation of a translation / 1 0 0 𝑑 / 0 1 0 𝑑 / 𝑇 𝑑 , 𝑑 , 𝑑 = / x y z

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Translations – Moving 3D Models'?

### Page 10 - Translation Properties

Source cue: - Lengths and angles are preserved / - Identity: 𝑇(0, 0, 0) = 𝐼 (identity matrix) / - Changing order of translations: / - 𝑇(𝑑1 , 𝑑1 , 𝑑1 ) ⋅ 𝑇(𝑑2 , 𝑑2 , 𝑑2 ) = 𝑇(𝑑2 , 𝑑2 , 𝑑2 ) ⋅ 𝑇(𝑑1 , 𝑑1 , 𝑑1 ) / x y z x y z x y z x y z

Professor-style explanation: For 'Translation Properties', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Lengths and angles are preserved / - Identity: 𝑇(0, 0, 0) = 𝐼 (identity matrix) / - Changing order of translations: / - 𝑇(𝑑1 , 𝑑1 , 𝑑1 ) ⋅ 𝑇(𝑑2 , 𝑑2 , 𝑑2 ) = 𝑇(𝑑2 , 𝑑2 , 𝑑2 ) ⋅ 𝑇(𝑑1 , 𝑑1 , 𝑑1 ) / x y z x y z x y z x y z. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Translation Properties. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Lengths and angles are preserved / - Identity: 𝑇(0, 0, 0) = 𝐼 (identity matrix) / - Changing order of translations: / - 𝑇(𝑑1 , 𝑑1 , 𝑑1 ) ⋅ 𝑇(𝑑2 , 𝑑2 , 𝑑2 ) = 𝑇(𝑑2 , 𝑑2 , 𝑑2 ) ⋅ 𝑇(𝑑1 , 𝑑1 , 𝑑1 ) / x y z x y z x y z x y z

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Translation Properties'?

### Page 11 - Scaling – Resizing 3D Models

Source cue: - Matrix representation of a scaling / 𝑠 0 0 0 / 0 𝑠 0 0 / 𝑆 𝑠 , 𝑠 , 𝑠 = / x y z

Professor-style explanation: For 'Scaling – Resizing 3D Models', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Matrix representation of a scaling / 𝑠 0 0 0 / 0 𝑠 0 0 / 𝑆 𝑠 , 𝑠 , 𝑠 = / x y z. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Scaling – Resizing 3D Models. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Matrix representation of a scaling / 𝑠 0 0 0 / 0 𝑠 0 0 / 𝑆 𝑠 , 𝑠 , 𝑠 = / x y z

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Scaling – Resizing 3D Models'?

### Page 12 - Scaling Properties

Source cue: - Lengths are not preserved, angles only for uniform scalings / - Identity: 𝑆(1, 1, 1) = 𝐼 (identity matrix) / - Changing order of scalings: / - 𝑆(𝑠1 , 𝑠1 , 𝑠1 ) ⋅ 𝑆(𝑠2 , 𝑠2 , 𝑠2 ) = 𝑆(𝑠2 , 𝑠2 , 𝑠2 ) ⋅ 𝑆(𝑠1 , 𝑠1 , 𝑠1 ) / x y z x y z x y z x y z

Professor-style explanation: For 'Scaling Properties', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Lengths are not preserved, angles only for uniform scalings / - Identity: 𝑆(1, 1, 1) = 𝐼 (identity matrix) / - Changing order of scalings: / - 𝑆(𝑠1 , 𝑠1 , 𝑠1 ) ⋅ 𝑆(𝑠2 , 𝑠2 , 𝑠2 ) = 𝑆(𝑠2 , 𝑠2 , 𝑠2 ) ⋅ 𝑆(𝑠1 , 𝑠1 , 𝑠1 ) / x y z x y z x y z x y z. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Scaling Properties. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Lengths are not preserved, angles only for uniform scalings / - Identity: 𝑆(1, 1, 1) = 𝐼 (identity matrix) / - Changing order of scalings: / - 𝑆(𝑠1 , 𝑠1 , 𝑠1 ) ⋅ 𝑆(𝑠2 , 𝑠2 , 𝑠2 ) = 𝑆(𝑠2 , 𝑠2 , 𝑠2 ) ⋅ 𝑆(𝑠1 , 𝑠1 , 𝑠1 ) / x y z x y z x y z x y z

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Scaling Properties'?

### Page 13 - Rotation – Changing Orientation of 3D Models 1/2

Source cue: - Matrix representation of a rotation around x-, y- and z-axis / 1 0 0 0 / 0 cos 𝜃 −𝑠𝑖𝑛𝜃 0 / 𝑅 𝜃 = / 0 𝑠𝑖𝑛𝜃 𝑐𝑜𝑠𝜃 0

Professor-style explanation: For 'Rotation – Changing Orientation of 3D Models 1/2', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Matrix representation of a rotation around x-, y- and z-axis / 1 0 0 0 / 0 cos 𝜃 −𝑠𝑖𝑛𝜃 0 / 𝑅 𝜃 = / 0 𝑠𝑖𝑛𝜃 𝑐𝑜𝑠𝜃 0. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Rotation – Changing Orientation of 3D Models 1/2. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Matrix representation of a rotation around x-, y- and z-axis / 1 0 0 0 / 0 cos 𝜃 −𝑠𝑖𝑛𝜃 0 / 𝑅 𝜃 = / 0 𝑠𝑖𝑛𝜃 𝑐𝑜𝑠𝜃 0

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Rotation – Changing Orientation of 3D Models 1/2'?

### Page 14 - Rotation – Changing Orientation of 3D Models 2/2

Source cue: - Rotations are made in the right-handed coordinate system so that when we / look along a positive axis to the origin, a 90° rotation about that axis / interleaves the positive axes as follows / - Rotation around x-axis transforms +y to +z / - Rotation around y-axis transforms +z to +x

Professor-style explanation: For 'Rotation – Changing Orientation of 3D Models 2/2', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Rotations are made in the right-handed coordinate system so that when we / look along a positive axis to the origin, a 90° rotation about that axis / interleaves the positive axes as follows / - Rotation around x-axis transforms +y to +z / - Rotation around y-axis transforms +z to +x. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Rotation – Changing Orientation of 3D Models 2/2. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Rotations are made in the right-handed coordinate system so that when we / look along a positive axis to the origin, a 90° rotation about that axis / interleaves the positive axes as follows / - Rotation around x-axis transforms +y to +z / - Rotation around y-axis transforms +z to +x

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Rotation – Changing Orientation of 3D Models 2/2'?

### Page 15 - Rotation Properties

Source cue: - Lengths and angles are preserved / - Identity: 𝑅 0 = 𝑅 0 = 𝑅 0 = I (identity matrix) / x y z / - Changing order of rotations around same axis: / - 𝑅 (𝜃) ⋅ 𝑅 (𝜑) = 𝑅 (𝜑) ⋅ 𝑅 (𝜃)

Professor-style explanation: For 'Rotation Properties', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Lengths and angles are preserved / - Identity: 𝑅 0 = 𝑅 0 = 𝑅 0 = I (identity matrix) / x y z / - Changing order of rotations around same axis: / - 𝑅 (𝜃) ⋅ 𝑅 (𝜑) = 𝑅 (𝜑) ⋅ 𝑅 (𝜃). The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Rotation Properties. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Lengths and angles are preserved / - Identity: 𝑅 0 = 𝑅 0 = 𝑅 0 = I (identity matrix) / x y z / - Changing order of rotations around same axis: / - 𝑅 (𝜃) ⋅ 𝑅 (𝜑) = 𝑅 (𝜑) ⋅ 𝑅 (𝜃)

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Rotation Properties'?

### Page 16 - Mirroring – Reflecting 3D Models on a Plane

Source cue: - Matrix representation of mirroring along x-y plane / 1 0 0 0 / 0 1 0 0 / 𝑀 = / 0 0 −1 0

Professor-style explanation: For 'Mirroring – Reflecting 3D Models on a Plane', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Matrix representation of mirroring along x-y plane / 1 0 0 0 / 0 1 0 0 / 𝑀 = / 0 0 −1 0. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Mirroring – Reflecting 3D Models on a Plane. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Matrix representation of mirroring along x-y plane / 1 0 0 0 / 0 1 0 0 / 𝑀 = / 0 0 −1 0

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Mirroring – Reflecting 3D Models on a Plane'?

### Page 17 - Shearing – Skewing 3D Models

Source cue: - Matrix representation of a shearing / 1 ℎ ℎ 0 / xy xz / ℎ 1 ℎ 0 / yx yz

Professor-style explanation: For 'Shearing – Skewing 3D Models', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Matrix representation of a shearing / 1 ℎ ℎ 0 / xy xz / ℎ 1 ℎ 0 / yx yz. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Shearing – Skewing 3D Models. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Matrix representation of a shearing / 1 ℎ ℎ 0 / xy xz / ℎ 1 ℎ 0 / yx yz

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Shearing – Skewing 3D Models'?

### Page 18 - 3.3 Composition of Transformations

Source cue: Concatenation of several transformation steps

Professor-style explanation: For '3.3 Composition of Transformations', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: Concatenation of several transformation steps. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about 3.3 Composition of Transformations. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: Concatenation of several transformation steps

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after '3.3 Composition of Transformations'?

### Page 19 - Composition of Transformations

Source cue: - Composition of transformations 𝑇 is done / by multiplying the respective transformation matrices / - (𝑇 ⋅ 𝑇 ⋅ … ⋅ 𝑇 ⋅ 𝑇 ) ⋅ 𝑣 = (𝑇 ⋅ (𝑇 ⋅ (… ⋅ (𝑇 ⋅ (𝑇 ⋅ 𝑣))))) / 1 2 n−1 n 1 2 n−1 n / - Interpretation: apply first transformation 𝑇 , then 𝑇 , ..., and finally 𝑇

Professor-style explanation: For 'Composition of Transformations', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Composition of transformations 𝑇 is done / by multiplying the respective transformation matrices / - (𝑇 ⋅ 𝑇 ⋅ … ⋅ 𝑇 ⋅ 𝑇 ) ⋅ 𝑣 = (𝑇 ⋅ (𝑇 ⋅ (… ⋅ (𝑇 ⋅ (𝑇 ⋅ 𝑣))))) / 1 2 n−1 n 1 2 n−1 n / - Interpretation: apply first transformation 𝑇 , then 𝑇 , ..., and finally 𝑇. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Composition of Transformations. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Composition of transformations 𝑇 is done / by multiplying the respective transformation matrices / - (𝑇 ⋅ 𝑇 ⋅ … ⋅ 𝑇 ⋅ 𝑇 ) ⋅ 𝑣 = (𝑇 ⋅ (𝑇 ⋅ (… ⋅ (𝑇 ⋅ (𝑇 ⋅ 𝑣))))) / 1 2 n−1 n 1 2 n−1 n / - Interpretation: apply first transformation 𝑇 , then 𝑇 , ..., and finally 𝑇

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Composition of Transformations'?

### Page 20 - Reference Points 1/2

Source cue: - Rotation and scaling happen in relation to origin (reference point)

Professor-style explanation: For 'Reference Points 1/2', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Rotation and scaling happen in relation to origin (reference point). Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Reference Points 1/2. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Rotation and scaling happen in relation to origin (reference point)

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Reference Points 1/2' into a causal sentence instead of repeating the slide title?

### Page 21 - Reference Points 2/2

Source cue: - In order to rotate (or scale) 3D models at an arbitrary reference point, / a sequence of transformations is necessary / - Move the 3D model from reference point 𝑀 to the origin 𝑂 / - Rotate (or scale) the 3D model / - Move the 3D model back to 𝑀

Professor-style explanation: For 'Reference Points 2/2', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - In order to rotate (or scale) 3D models at an arbitrary reference point, / a sequence of transformations is necessary / - Move the 3D model from reference point 𝑀 to the origin 𝑂 / - Rotate (or scale) the 3D model / - Move the 3D model back to 𝑀. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Reference Points 2/2. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - In order to rotate (or scale) 3D models at an arbitrary reference point, / a sequence of transformations is necessary / - Move the 3D model from reference point 𝑀 to the origin 𝑂 / - Rotate (or scale) the 3D model / - Move the 3D model back to 𝑀

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Reference Points 2/2'?

### Page 22 - Rotation Around Arbitrary Axis

Source cue: - Rotation around any axis / - Axis given by center of rotation 𝑃 and direction 𝑈 = (𝑢 , 𝑢 , 𝑢 ) / x y z / - Rotation by 𝜃 degrees / - Construction of transformation as transformation sequence

Professor-style explanation: For 'Rotation Around Arbitrary Axis', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Rotation around any axis / - Axis given by center of rotation 𝑃 and direction 𝑈 = (𝑢 , 𝑢 , 𝑢 ) / x y z / - Rotation by 𝜃 degrees / - Construction of transformation as transformation sequence. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Rotation Around Arbitrary Axis. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Rotation around any axis / - Axis given by center of rotation 𝑃 and direction 𝑈 = (𝑢 , 𝑢 , 𝑢 ) / x y z / - Rotation by 𝜃 degrees / - Construction of transformation as transformation sequence

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Rotation Around Arbitrary Axis'?

### Page 23 - Reminder: Vector Calculus

Source cue: - Length of a vector is expressed as follows / 𝑣⃑ = 𝑣 2 + 𝑣 2 + 𝑣 2 / x y z / - Vectors of length 𝑣⃑ = 1 are normalized and called unit vectors / - Arbitrary vectors can be normalized as follows

Professor-style explanation: This slide belongs to local shading. For 'Reminder: Vector Calculus', imagine one visible surface point and ask how bright or colored it should become. The slide gives us this anchor: - Length of a vector is expressed as follows / 𝑣⃑ = 𝑣 2 + 𝑣 2 + 𝑣 2 / x y z / - Vectors of length 𝑣⃑ = 1 are normalized and called unit vectors / - Arbitrary vectors can be normalized as follows. The professor explanation must name the normal, light direction, view direction, material response, and whether the calculation is done per vertex or per fragment.

Technical commentary: This slide is about Reminder: Vector Calculus. Read it as local shading. Identify normal, light direction, view direction, material coefficients, and where the computation is evaluated. The visible cue is: - Length of a vector is expressed as follows / 𝑣⃑ = 𝑣 2 + 𝑣 2 + 𝑣 2 / x y z / - Vectors of length 𝑣⃑ = 1 are normalized and called unit vectors / - Arbitrary vectors can be normalized as follows

Why it matters: Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.

Check yourself: Can you identify the normal, light vector, view vector, and material term relevant to 'Reminder: Vector Calculus'?

### Page 24 - Reminder: Cross Product (= vector product)

Source cue: - Given two vectors 𝑢 and 𝑣⃑ in ℝ3 / - Cross product 𝑢 × 𝑣⃑ of 𝑢 and 𝑣⃑ is a vector defined as follows / 𝑢 𝑣 𝑢 ⋅ 𝑣 − 𝑢 ⋅ 𝑣 / x x y z z y / 𝑢 × 𝑣⃑ = 𝑢 × 𝑣 = 𝑢 ⋅ 𝑣 − 𝑢 ⋅ 𝑣

Professor-style explanation: For 'Reminder: Cross Product (= vector product)', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Given two vectors 𝑢 and 𝑣⃑ in ℝ3 / - Cross product 𝑢 × 𝑣⃑ of 𝑢 and 𝑣⃑ is a vector defined as follows / 𝑢 𝑣 𝑢 ⋅ 𝑣 − 𝑢 ⋅ 𝑣 / x x y z z y / 𝑢 × 𝑣⃑ = 𝑢 × 𝑣 = 𝑢 ⋅ 𝑣 − 𝑢 ⋅ 𝑣. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Reminder: Cross Product (= vector product). Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Given two vectors 𝑢 and 𝑣⃑ in ℝ3 / - Cross product 𝑢 × 𝑣⃑ of 𝑢 and 𝑣⃑ is a vector defined as follows / 𝑢 𝑣 𝑢 ⋅ 𝑣 − 𝑢 ⋅ 𝑣 / x x y z z y / 𝑢 × 𝑣⃑ = 𝑢 × 𝑣 = 𝑢 ⋅ 𝑣 − 𝑢 ⋅ 𝑣

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Reminder: Cross Product (= vector product)' into a causal sentence instead of repeating the slide title?

### Page 25 - Example – Transforming Directed Line Segment 1/7

Source cue: - Example transformation task / - Given line segments 𝑃 𝑃 and 𝑃 𝑃 / 1 2 1 3 / - Transform it into the yz-plane so that 𝑃 𝑃 lies on the z-axis / 1 2

Professor-style explanation: For 'Example – Transforming Directed Line Segment 1/7', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Example transformation task / - Given line segments 𝑃 𝑃 and 𝑃 𝑃 / 1 2 1 3 / - Transform it into the yz-plane so that 𝑃 𝑃 lies on the z-axis / 1 2. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example – Transforming Directed Line Segment 1/7. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Example transformation task / - Given line segments 𝑃 𝑃 and 𝑃 𝑃 / 1 2 1 3 / - Transform it into the yz-plane so that 𝑃 𝑃 lies on the z-axis / 1 2

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example – Transforming Directed Line Segment 1/7'?

### Page 26 - Example – Transforming Directed Line Segment 2/7

Source cue: - Approach 1: Determine rotation angles for rotation sequence / - Move 𝑃 = x , y , z into the origin / 1 1 1 1 / - Rotate around the y-axis so that 𝑃 𝑃 lies in the yz-plane / 1 2

Professor-style explanation: For 'Example – Transforming Directed Line Segment 2/7', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Approach 1: Determine rotation angles for rotation sequence / - Move 𝑃 = x , y , z into the origin / 1 1 1 1 / - Rotate around the y-axis so that 𝑃 𝑃 lies in the yz-plane / 1 2. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example – Transforming Directed Line Segment 2/7. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Approach 1: Determine rotation angles for rotation sequence / - Move 𝑃 = x , y , z into the origin / 1 1 1 1 / - Rotate around the y-axis so that 𝑃 𝑃 lies in the yz-plane / 1 2

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example – Transforming Directed Line Segment 2/7'?

### Page 27 - Example – Transforming Directed Line Segment 3/7

Source cue: - Step 2 – Rotation of 𝑃′ 𝑃′ around y-axis into yz-plane / 1 2 / - Rotation 𝑅 (𝜃– 90°) / - Rotation angle – (90°– 𝜃) = 𝜃– 90° / - Matrix ingredients

Professor-style explanation: For 'Example – Transforming Directed Line Segment 3/7', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Step 2 – Rotation of 𝑃′ 𝑃′ around y-axis into yz-plane / 1 2 / - Rotation 𝑅 (𝜃– 90°) / - Rotation angle – (90°– 𝜃) = 𝜃– 90° / - Matrix ingredients. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example – Transforming Directed Line Segment 3/7. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Step 2 – Rotation of 𝑃′ 𝑃′ around y-axis into yz-plane / 1 2 / - Rotation 𝑅 (𝜃– 90°) / - Rotation angle – (90°– 𝜃) = 𝜃– 90° / - Matrix ingredients

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example – Transforming Directed Line Segment 3/7'?

### Page 28 - Example – Transforming Directed Line Segment 4/7

Source cue: - Step 3 – Rotation of 𝑃′′ 𝑃′′ around x-axis onto z-axis / 1 2 / - Rotation 𝑅 (φ) / - Matrix ingredients / z′′

Professor-style explanation: For 'Example – Transforming Directed Line Segment 4/7', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Step 3 – Rotation of 𝑃′′ 𝑃′′ around x-axis onto z-axis / 1 2 / - Rotation 𝑅 (φ) / - Matrix ingredients / z′′. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example – Transforming Directed Line Segment 4/7. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Step 3 – Rotation of 𝑃′′ 𝑃′′ around x-axis onto z-axis / 1 2 / - Rotation 𝑅 (φ) / - Matrix ingredients / z′′

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example – Transforming Directed Line Segment 4/7'?

### Page 29 - Example – Transforming Directed Line Segment 5/7

Source cue: - Step 4 – Rotation of 𝑃′′′ 𝑃′′′ into yz-plane / 1 3 / - Rotation 𝑅 (α) / y / - Matrix ingredients

Professor-style explanation: For 'Example – Transforming Directed Line Segment 5/7', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Step 4 – Rotation of 𝑃′′′ 𝑃′′′ into yz-plane / 1 3 / - Rotation 𝑅 (α) / y / - Matrix ingredients. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example – Transforming Directed Line Segment 5/7. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Step 4 – Rotation of 𝑃′′′ 𝑃′′′ into yz-plane / 1 3 / - Rotation 𝑅 (α) / y / - Matrix ingredients

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example – Transforming Directed Line Segment 5/7'?

### Page 30 - Example – Transforming Directed Line Segment 6/7

Source cue: - Approach 2: Construct orthogonal matrix which obeys following properties / - Each row and column corresponds to a unit length vector / - Row and column vectors are orthogonal to each other / - Each row vector rotates on one main axis / (𝑅 on x-axis, 𝑅 on y-axis, 𝑅 on z-axis)

Professor-style explanation: For 'Example – Transforming Directed Line Segment 6/7', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Approach 2: Construct orthogonal matrix which obeys following properties / - Each row and column corresponds to a unit length vector / - Row and column vectors are orthogonal to each other / - Each row vector rotates on one main axis / (𝑅 on x-axis, 𝑅 on y-axis, 𝑅 on z-axis). The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example – Transforming Directed Line Segment 6/7. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Approach 2: Construct orthogonal matrix which obeys following properties / - Each row and column corresponds to a unit length vector / - Row and column vectors are orthogonal to each other / - Each row vector rotates on one main axis / (𝑅 on x-axis, 𝑅 on y-axis, 𝑅 on z-axis)

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example – Transforming Directed Line Segment 6/7'?

### Page 31 - Example – Transforming Directed Line Segment 7/7

Source cue: - Consideration 2: Formulate 𝑅 as unit vector / orthogonal to the plane spanned by 𝑃 , 𝑃 , and 𝑃 / 1 2 3 / 𝑃 𝑃 ×𝑃 𝑃 / - 𝑅 = 𝑟 𝑟 𝑟 𝑇 = 1 3 1 2

Professor-style explanation: For 'Example – Transforming Directed Line Segment 7/7', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Consideration 2: Formulate 𝑅 as unit vector / orthogonal to the plane spanned by 𝑃 , 𝑃 , and 𝑃 / 1 2 3 / 𝑃 𝑃 ×𝑃 𝑃 / - 𝑅 = 𝑟 𝑟 𝑟 𝑇 = 1 3 1 2. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example – Transforming Directed Line Segment 7/7. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Consideration 2: Formulate 𝑅 as unit vector / orthogonal to the plane spanned by 𝑃 , 𝑃 , and 𝑃 / 1 2 3 / 𝑃 𝑃 ×𝑃 𝑃 / - 𝑅 = 𝑟 𝑟 𝑟 𝑇 = 1 3 1 2

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example – Transforming Directed Line Segment 7/7'?

### Page 32 - Example – Direction of Flight Transformation 1/3

Source cue: - Example transformation task / - Given 3D model centered in origin of x -, y -, z -coordinate system / 𝑝 𝑝 𝑝 / - Transform it such that / - it is centered in arbitrary point 𝑃, and

Professor-style explanation: For 'Example – Direction of Flight Transformation 1/3', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Example transformation task / - Given 3D model centered in origin of x -, y -, z -coordinate system / 𝑝 𝑝 𝑝 / - Transform it such that / - it is centered in arbitrary point 𝑃, and. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example – Direction of Flight Transformation 1/3. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Example transformation task / - Given 3D model centered in origin of x -, y -, z -coordinate system / 𝑝 𝑝 𝑝 / - Transform it such that / - it is centered in arbitrary point 𝑃, and

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example – Direction of Flight Transformation 1/3'?

### Page 33 - Example – Direction of Flight Transformation 2/3

Source cue: 𝑟 𝑟 𝑟 / 1x 2x 3x / - Step 1 – create orthogonal rotation matrix 𝑅 = 𝑟 𝑟 𝑟 / 1y 2y 3y / 𝑟 𝑟 𝑟

Professor-style explanation: For 'Example – Direction of Flight Transformation 2/3', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: 𝑟 𝑟 𝑟 / 1x 2x 3x / - Step 1 – create orthogonal rotation matrix 𝑅 = 𝑟 𝑟 𝑟 / 1y 2y 3y / 𝑟 𝑟 𝑟. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example – Direction of Flight Transformation 2/3. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: 𝑟 𝑟 𝑟 / 1x 2x 3x / - Step 1 – create orthogonal rotation matrix 𝑅 = 𝑟 𝑟 𝑟 / 1y 2y 3y / 𝑟 𝑟 𝑟

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example – Direction of Flight Transformation 2/3'?

### Page 34 - Example – Direction of Flight Transformation 3/3

Source cue: - Transformation 𝑀 is described by a translation and an orthogonal matrix / 𝑟 𝑟 𝑟 0 / 1x 2x 3x / 𝑟 𝑟 𝑟 0 / 1y 2y 3y

Professor-style explanation: For 'Example – Direction of Flight Transformation 3/3', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Transformation 𝑀 is described by a translation and an orthogonal matrix / 𝑟 𝑟 𝑟 0 / 1x 2x 3x / 𝑟 𝑟 𝑟 0 / 1y 2y 3y. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example – Direction of Flight Transformation 3/3. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Transformation 𝑀 is described by a translation and an orthogonal matrix / 𝑟 𝑟 𝑟 0 / 1x 2x 3x / 𝑟 𝑟 𝑟 0 / 1y 2y 3y

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example – Direction of Flight Transformation 3/3'?

### Page 35 - 3.4 Coordinate System Change

Source cue: Transformation as change of frame of reference

Professor-style explanation: For '3.4 Coordinate System Change', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: Transformation as change of frame of reference. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about 3.4 Coordinate System Change. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: Transformation as change of frame of reference

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after '3.4 Coordinate System Change'?

### Page 36 - Coordinate System Change

Source cue: - Alternative view on transformations: / - transformations change the coordinate system of 3D model / Example 1 Example 2

Professor-style explanation: For 'Coordinate System Change', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Alternative view on transformations: / - transformations change the coordinate system of 3D model / Example 1 Example 2. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Coordinate System Change. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Alternative view on transformations: / - transformations change the coordinate system of 3D model / Example 1 Example 2

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Coordinate System Change'?

### Page 37 - Local Coordinate Systems

Source cue: - Application in OpenGL / - Individual 3D models of a scene have their own, local coordinate system / - Local coordinate systems of the 3D models must be changed / into a common coordinate system, the world coordinate system / - Transformation between coordinate systems (CS)

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Local Coordinate Systems' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Application in OpenGL / - Individual 3D models of a scene have their own, local coordinate system / - Local coordinate systems of the 3D models must be changed / into a common coordinate system, the world coordinate system / - Transformation between coordinate systems (CS). If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Local Coordinate Systems. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Application in OpenGL / - Individual 3D models of a scene have their own, local coordinate system / - Local coordinate systems of the 3D models must be changed / into a common coordinate system, the world coordinate system / - Transformation between coordinate systems (CS)

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Local Coordinate Systems'?

### Page 38 - Example 1 – Coordinate System Change 1/2

Source cue: x(1) / - Example transformation task y y(5) / - Rotation and scaling of an object around its center 𝑀 / y(1) / and subsequent translation to a point 𝑄

Professor-style explanation: For 'Example 1 – Coordinate System Change 1/2', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: x(1) / - Example transformation task y y(5) / - Rotation and scaling of an object around its center 𝑀 / y(1) / and subsequent translation to a point 𝑄. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example 1 – Coordinate System Change 1/2. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: x(1) / - Example transformation task y y(5) / - Rotation and scaling of an object around its center 𝑀 / y(1) / and subsequent translation to a point 𝑄

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example 1 – Coordinate System Change 1/2'?

### Page 39 - Example 1 – Coordinate System Change 2/2

Source cue: y y y y y / x x x x x / 3D Model Transformation / y(5) / y(2) y(3)

Professor-style explanation: For 'Example 1 – Coordinate System Change 2/2', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: y y y y y / x x x x x / 3D Model Transformation / y(5) / y(2) y(3). The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example 1 – Coordinate System Change 2/2. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: y y y y y / x x x x x / 3D Model Transformation / y(5) / y(2) y(3)

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example 1 – Coordinate System Change 2/2'?

### Page 40 - Example 2 – Hierarchical Coordinate Systems 1/2

Source cue: - To model complex scenes, a hierarchy of coordinate systems is helpful / - Example: modeling of a tricycle / - World-coordinate system / - Tricycle-coordinate system / - Wheel-coordinate system

Professor-style explanation: For 'Example 2 – Hierarchical Coordinate Systems 1/2', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - To model complex scenes, a hierarchy of coordinate systems is helpful / - Example: modeling of a tricycle / - World-coordinate system / - Tricycle-coordinate system / - Wheel-coordinate system. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example 2 – Hierarchical Coordinate Systems 1/2. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - To model complex scenes, a hierarchy of coordinate systems is helpful / - Example: modeling of a tricycle / - World-coordinate system / - Tricycle-coordinate system / - Wheel-coordinate system

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example 2 – Hierarchical Coordinate Systems 1/2'?

### Page 41 - Example 2 – Hierarchical Coordinate Systems 1/2

Source cue: - Scene graphs are used to represent hierarchical coordinate systems / and the required transformations / Tricycle Translation T / Steering Rotation R (α) / y-tr

Professor-style explanation: For 'Example 2 – Hierarchical Coordinate Systems 1/2', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Scene graphs are used to represent hierarchical coordinate systems / and the required transformations / Tricycle Translation T / Steering Rotation R (α) / y-tr. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Example 2 – Hierarchical Coordinate Systems 1/2. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Scene graphs are used to represent hierarchical coordinate systems / and the required transformations / Tricycle Translation T / Steering Rotation R (α) / y-tr

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Example 2 – Hierarchical Coordinate Systems 1/2'?

### Page 42 - 3.5 Transformations in OpenGL

Source cue: Implementation with GLM und GLSL

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. '3.5 Transformations in OpenGL' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: Implementation with GLM und GLSL. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about 3.5 Transformations in OpenGL. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: Implementation with GLM und GLSL

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in '3.5 Transformations in OpenGL'?

### Page 43 - Geometric Transformations in OpenGL

Source cue: - Supported coordinate systems / - Floating-point coordinate system for 2D and 3D / - Integer coordinate system (2D) as a special case / - Representation of vectors / - 2D vector by one-dimensional array with 2 elements

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'Geometric Transformations in OpenGL' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Supported coordinate systems / - Floating-point coordinate system for 2D and 3D / - Integer coordinate system (2D) as a special case / - Representation of vectors / - 2D vector by one-dimensional array with 2 elements. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about Geometric Transformations in OpenGL. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Supported coordinate systems / - Floating-point coordinate system for 2D and 3D / - Integer coordinate system (2D) as a special case / - Representation of vectors / - 2D vector by one-dimensional array with 2 elements

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'Geometric Transformations in OpenGL'?

### Page 44 - OpenGL Transformation Pipeline

Source cue: - Model-View matrix / - Transformation matrix for model space related transformations / - Additionally contains the transformation of the scene / into the camera coordinate system (view transformation, not projection!) / - Transformation pipeline

Professor-style explanation: On this slide, I would emphasize that OpenGL is a controlled state machine around the GPU pipeline. 'OpenGL Transformation Pipeline' is not about one magic render call; it is about objects, bindings, shader interfaces, buffers, and state being consistent at draw time. The slide gives us this anchor: - Model-View matrix / - Transformation matrix for model space related transformations / - Additionally contains the transformation of the scene / into the camera coordinate system (view transformation, not projection!) / - Transformation pipeline. If the output is wrong, you inspect which object owns the data, which shader consumes it, and which state changes the result.

Technical commentary: This slide is about OpenGL Transformation Pipeline. Read it as concrete API state and GPU data movement. Ask which object is bound, which shader stage consumes it, and which state affects the draw call. The visible cue is: - Model-View matrix / - Transformation matrix for model space related transformations / - Additionally contains the transformation of the scene / into the camera coordinate system (view transformation, not projection!) / - Transformation pipeline

Why it matters: OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.

Check yourself: Can you name the OpenGL object, state, shader stage, or buffer involved in 'OpenGL Transformation Pipeline'?

### Page 45 - Example – Translation and Scaling

Source cue: - Drawing cylinder objects / - drawCylinder draws a cylinder centered at the origin, / with respect to the y-axis, with a given radius and height / - By translation this "unit cylinder" can be positioned / - By scaling this "unit cylinder" can be resized

Professor-style explanation: For 'Example – Translation and Scaling', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Drawing cylinder objects / - drawCylinder draws a cylinder centered at the origin, / with respect to the y-axis, with a given radius and height / - By translation this "unit cylinder" can be positioned / - By scaling this "unit cylinder" can be resized. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Example – Translation and Scaling. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Drawing cylinder objects / - drawCylinder draws a cylinder centered at the origin, / with respect to the y-axis, with a given radius and height / - By translation this "unit cylinder" can be positioned / - By scaling this "unit cylinder" can be resized

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Example – Translation and Scaling' into a causal sentence instead of repeating the slide title?

### Page 46 - Matrix Specification

Source cue: - Matrices are often specified in form of a C array / void draw(...) { / ... / GLfloat M[4][4]; / M[0][0] = ....;

Professor-style explanation: For 'Matrix Specification', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - Matrices are often specified in form of a C array / void draw(...) { / ... / GLfloat M[4][4]; / M[0][0] = . The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about Matrix Specification. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - Matrices are often specified in form of a C array / void draw(...) { / ... / GLfloat M[4][4]; / M[0][0] = ....;

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'Matrix Specification'?

### Page 47 - Example – Portico Modeling 1/5

Source cue: - Columned hall consists of floor space, H·0.1 / top surface and columns / - Columns are evenly distributed / along the edge of the round floor surface H / - Total height of a column is 𝐻,

Professor-style explanation: For 'Example – Portico Modeling 1/5', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Columned hall consists of floor space, H·0.1 / top surface and columns / - Columns are evenly distributed / along the edge of the round floor surface H / - Total height of a column is 𝐻,. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Example – Portico Modeling 1/5. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Columned hall consists of floor space, H·0.1 / top surface and columns / - Columns are evenly distributed / along the edge of the round floor surface H / - Total height of a column is 𝐻,

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Example – Portico Modeling 1/5' into a causal sentence instead of repeating the slide title?

### Page 48 - Example – Portico Modeling 2/5

Source cue: - Drawing a cylinder closed at top and bottom / - Each column should "stand" in the y-axis / - Each column should have a lid surface at the top and bottom / - Disk primitive is embedded in the xy-plane / - Cylinder primitive consists only of lateral surface

Professor-style explanation: For 'Example – Portico Modeling 2/5', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Drawing a cylinder closed at top and bottom / - Each column should "stand" in the y-axis / - Each column should have a lid surface at the top and bottom / - Disk primitive is embedded in the xy-plane / - Cylinder primitive consists only of lateral surface. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Example – Portico Modeling 2/5. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Drawing a cylinder closed at top and bottom / - Each column should "stand" in the y-axis / - Each column should have a lid surface at the top and bottom / - Disk primitive is embedded in the xy-plane / - Cylinder primitive consists only of lateral surface

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Example – Portico Modeling 2/5' into a causal sentence instead of repeating the slide title?

### Page 49 - Example – Portico Modeling 3/5

Source cue: - Drawing a single column / - Composition of 5 cylinder objects / - Rotation into y-axis to match orientation / - Positioning of the parts by translation along the y-axis / - Incremental translation around the partial column height

Professor-style explanation: For 'Example – Portico Modeling 3/5', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Drawing a single column / - Composition of 5 cylinder objects / - Rotation into y-axis to match orientation / - Positioning of the parts by translation along the y-axis / - Incremental translation around the partial column height. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Example – Portico Modeling 3/5. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Drawing a single column / - Composition of 5 cylinder objects / - Rotation into y-axis to match orientation / - Positioning of the parts by translation along the y-axis / - Incremental translation around the partial column height

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Example – Portico Modeling 3/5' into a causal sentence instead of repeating the slide title?

### Page 50 - Example – Portico Modeling 4/5

Source cue: - Drawing the group of columns / - Columns are evenly distributed on a circle with radius 𝑅 / - Number 𝑁, radius 𝑅 of the columns as well as floor radius 𝑅 adjustable

Professor-style explanation: For 'Example – Portico Modeling 4/5', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Drawing the group of columns / - Columns are evenly distributed on a circle with radius 𝑅 / - Number 𝑁, radius 𝑅 of the columns as well as floor radius 𝑅 adjustable. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Example – Portico Modeling 4/5. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Drawing the group of columns / - Columns are evenly distributed on a circle with radius 𝑅 / - Number 𝑁, radius 𝑅 of the columns as well as floor radius 𝑅 adjustable

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Example – Portico Modeling 4/5' into a causal sentence instead of repeating the slide title?

### Page 51 - Example – Portico Modeling 5/5

Source cue: - Drawing the hall / - Use cylinder primitive as floor area / - Use cone primitive as a roof

Professor-style explanation: For 'Example – Portico Modeling 5/5', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Drawing the hall / - Use cylinder primitive as floor area / - Use cone primitive as a roof. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Example – Portico Modeling 5/5. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Drawing the hall / - Use cylinder primitive as floor area / - Use cone primitive as a roof

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Example – Portico Modeling 5/5' into a causal sentence instead of repeating the slide title?

### Page 52 - by applying affine transformations to their vertices

Source cue: - 3D models can be positioned, resized and oriented in the 3D world / by applying affine transformations to their vertices / - An affine transformation is represented by a 4x4 matrix / - Affine transformations can be more efficiently applied / when concatenated to a single matrix through matrix multiplication

Professor-style explanation: For 'by applying affine transformations to their vertices', put the formula aside for a moment and name the coordinate spaces. A transformation only makes sense when we know where the point, vector, or normal starts and where it should end. The slide gives us this anchor: - 3D models can be positioned, resized and oriented in the 3D world / by applying affine transformations to their vertices / - An affine transformation is represented by a 4x4 matrix / - Affine transformations can be more efficiently applied / when concatenated to a single matrix through matrix multiplication. The professor-level way to read this slide is to narrate the movement: model space to world space, world to view, view to clip, or whichever step the slide is showing.

Technical commentary: This slide is about by applying affine transformations to their vertices. Read it as a coordinate-space operation. Name the input space, the matrix or transformation, and the output space before memorizing formulas. The visible cue is: - 3D models can be positioned, resized and oriented in the 3D world / by applying affine transformations to their vertices / - An affine transformation is represented by a 4x4 matrix / - Affine transformations can be more efficiently applied / when concatenated to a single matrix through matrix multiplication

Why it matters: A wrong coordinate-space assumption can make correct formulas produce wrong images.

Check yourself: Can you state the coordinate space before and after 'by applying affine transformations to their vertices'?

### Page 53 - Literature and other sources used in this chapter

Source cue: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Professor-style explanation: For 'Literature and other sources used in this chapter', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about Literature and other sources used in this chapter. Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: The extracted slide text is mostly visual or metadata; use the original PDF page for the diagram or image.

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn 'Literature and other sources used in this chapter' into a causal sentence instead of repeating the slide title?

### Page 54 - (3rd Edition), Addison-Wesley 2013. (Chapters 10 & 11)

Source cue: - Text Books / - J. Foley, A. van Dam, S. Feiner: Computer Graphics: Principles and Practice / (3rd Edition), Addison-Wesley 2013. (Chapters 10 & 11) / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer

Professor-style explanation: For '(3rd Edition), Addison-Wesley 2013. (Chapters 10 & 11)', I would not just read the bullet points aloud. I would ask what problem the slide is solving and how it connects to the previous and next stage. The slide gives us this anchor: - Text Books / - J. Foley, A. van Dam, S. Feiner: Computer Graphics: Principles and Practice / (3rd Edition), Addison-Wesley 2013. (Chapters 10 & 11) / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer. Turn the slide into a causal explanation: this input is processed by this idea, which produces this result, and that result matters later.

Technical commentary: This slide is about (3rd Edition), Addison-Wesley 2013. (Chapters 10 & 11). Connect the bullet terms causally: what problem is being solved, what data is used, what output is produced, and which later pipeline stage depends on it. The visible cue is: - Text Books / - J. Foley, A. van Dam, S. Feiner: Computer Graphics: Principles and Practice / (3rd Edition), Addison-Wesley 2013. (Chapters 10 & 11) / - P. Shirley, M. Ashikhmin, S. Marschner: Fundamentals of Computer

Why it matters: Even a sparse slide usually names a relation you must be able to explain in words.

Check yourself: Can you turn '(3rd Edition), Addison-Wesley 2013. (Chapters 10 & 11)' into a causal sentence instead of repeating the slide title?

## 03.1 Mathematical Foundations

Source location: Section 3.1

### Commentary

The lecture uses vectors and matrices to express geometric operations. A vector can represent a point position, a direction, an offset, or an attribute depending on context. A matrix expresses a linear map or, with homogeneous coordinates, an affine transformation.

The central exam habit is to name the coordinate space. A point in model coordinates and a light direction in view coordinates cannot be mixed safely. Many visual bugs are coordinate-space bugs.

### Mental Model

A numeric vector is incomplete until you know what coordinate system it belongs to.

### Check Yourself

Why is a normal vector not transformed exactly like a point under all transformations?

## 03.2 Affine Transformations

Source location: Section 3.2

### Commentary

Affine transformations include translation, rotation, scaling, shearing, and combinations of these. Homogeneous coordinates allow translation to be represented in matrix form together with other transformations.

Translation moves positions but not pure directions. Rotation changes orientation while preserving lengths if it is a proper rotation. Scaling can change lengths and can also affect normals. These distinctions matter later in lighting.

### Mental Model

Use 4D homogeneous coordinates so that a single matrix pipeline can move 3D points through the scene.

### Check Yourself

What does the homogeneous w component let a transformation matrix express?

## 03.3 Composition of Transformations

Source location: Section 3.3

### Commentary

Composition means applying several transformations in sequence. The order matters because matrix multiplication is generally not commutative. Rotating an object around its own origin and then translating it is different from translating it and then rotating around the world origin.

When you read a formula such as projection * view * model * position, read it from right to left for the point: first model, then view, then projection. The resulting matrix chain is compact, but the conceptual steps remain separate.

### Mental Model

Matrix chains are compressed stories of movement through coordinate spaces.

### Check Yourself

Why can swapping model and view matrices destroy the intended camera/object relation?

## 03.4 Coordinate System Change

Source location: Section 3.4

### Commentary

A transformation can be read actively as moving an object, or passively as changing the coordinate frame used to describe it. Both interpretations are valid, but mixing them carelessly causes sign and order errors.

The view matrix is a classic example: conceptually you position a camera, but the pipeline usually transforms the world by the inverse of the camera transform so that the camera becomes the origin of view space.

### Mental Model

Moving the camera one way is equivalent to moving the world the opposite way for rendering.

### Check Yourself

Why is the view transform often related to the inverse camera transform?

## 03.5 Transformations in OpenGL

Source location: Section 3.5

### Commentary

Modern OpenGL does not automatically manage the old matrix stacks. You usually compute model, view, and projection matrices in application code and pass them to shaders as uniforms.

The vertex shader is where the final clip-space position is normally computed. That means a wrong matrix uniform, wrong multiplication order, or wrong convention can make geometry vanish even though buffers and draw calls are correct.

### Mental Model

The shader is the place where abstract transformation math becomes GPU execution.

### Check Yourself

Which matrix would you inspect first if an object follows the camera instead of staying in the world?

## End-of-Lecture Summary

If you remember only one thing from Lecture 03, remember this: This lecture explains how geometry moves between coordinate systems. Almost every later topic assumes that you can track where a point or vector currently lives.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
