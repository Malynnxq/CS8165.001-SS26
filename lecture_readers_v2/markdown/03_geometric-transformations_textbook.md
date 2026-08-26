# Lecture 03 - Geometric Transformations

Primary source: `course_text_parts/03_lectures/03_geometric-transformations.txt`

A beginner-friendly textbook chapter for a student who missed the lecture. The goal is not to paraphrase slides one by one, but to reconstruct the logic of the lecture: why transformations are needed, why matrices are used, what each basic transformation actually does, why order matters, how coordinate systems fit into the story, and how all of this appears in OpenGL.

## How to use this chapter

Read this chapter in order. The lecture becomes much easier once one distinction is clear from the start:

- a **point/vector** is data being transformed;
- a **matrix** describes the transformation;
- the **coordinate system** tells you what the numbers mean;
- a **matrix product** lets several transformations become one composite transformation.

Do not try to memorize the 4x4 matrices before you understand what each one is supposed to accomplish geometrically.

## Source anchors

- Slides 2-7: why 3D models must be transformed; vectors, matrices, matrix-vector multiplication.
- Slides 9-17: translation, scaling, rotation, mirroring, shearing.
- Slides 19-22: composition, reference points, arbitrary-axis rotation.
- Slides 23-34: vector length, normalization, cross product, orthogonal-basis construction, flight-direction example.
- Slides 35-39: coordinate-system changes and local-to-world interpretation.
- Slides 43-51: OpenGL/GLM representation and modeling examples.
- Slide 52: chapter summary.

## 1. Why geometric transformations exist

Source focus: slides 2-3

A 3D model is usually created in a convenient local coordinate system. A cube might be centered at the origin, a cylinder might stand on one axis, and a character model might be modeled around its own local center. But a scene needs many objects at different positions, orientations, and sizes.

That creates the central problem of this lecture: **how can the same model be reused while changing where it is, how large it is, and which direction it faces?**

The answer is to transform the model's vertices. If a model contains thousands of vertices, we do not want to rewrite each vertex by hand. Instead, we describe the desired geometric operation with a matrix and apply the same matrix to all relevant vertices.

So the basic pattern is:

`vertex -> transformation matrix -> transformed vertex`

A transformation is therefore not an abstract algebra trick. It is the mechanism that lets one stored model appear in many different places and configurations in the virtual world.

### Concrete example

Suppose a unit cube is modeled around the origin. To place one cube at the left side of the scene and another cube at the right side, the stored cube geometry can stay unchanged. You use two different translation matrices when rendering the two copies.

### Check yourself

Why is transforming model vertices more useful than storing a separate mesh for every possible object position and size?

## 2. Vectors and matrices: what role does each play?

Source focus: slides 5-7

A vertex position is represented as a vector. In ordinary 3D geometry we think of a point as `(x, y, z)`. In graphics, 4-component vectors `(x, y, z, w)` are extremely common because they let translation fit into the same matrix framework as rotation and scaling.

A matrix describes how coordinates should be combined to produce new coordinates. In this lecture, the central object is a 4x4 matrix.

Matrix-vector multiplication means that each output component is computed from a weighted combination of the input components. If `v` is the original vertex and `M` is a transformation matrix, then

`v' = M v`

means: apply transformation `M` to vertex `v`, producing transformed vertex `v'`.

The identity matrix `I` is the do-nothing transformation. Multiplying by `I` leaves the vector unchanged. An inverse matrix `M^-1`, when it exists, undoes the effect of `M`:

`M^-1 M = I`.

This inverse idea will later become important for reversing transformations and for changing coordinate systems.

### Why 4D vectors for 3D graphics?

Rotation and scaling can be written as ordinary 3x3 linear transformations, but translation cannot be represented as a 3x3 matrix acting on `(x,y,z)` alone. Homogeneous coordinates solve this by representing a 3D point as `(x,y,z,1)`. Then translation can be encoded in a 4x4 matrix as well.

The extra `w` component is therefore what allows one consistent 4x4 matrix pipeline to handle many affine transformations.

### Check yourself

What is the conceptual difference between the vector `v` and the matrix `M` in `v' = Mv`?

## 3. Translation: changing position without changing shape

Source focus: slides 9-10

A translation moves every point by the same displacement `(dx, dy, dz)`.

Conceptually:

`(x, y, z) -> (x + dx, y + dy, z + dz)`.

Because every point receives the same offset, the relative distances between points do not change. Angles do not change either. The object moves, but its shape and orientation stay the same.

In homogeneous coordinates, translation is represented by a 4x4 matrix whose last column contains the displacement. The crucial idea is not the memorized matrix layout; it is that multiplying a point with `w=1` adds the displacement to its spatial coordinates.

Translations along different directions commute with one another. Moving +2 in x and then +3 in y gives the same final location as moving +3 in y and then +2 in x. Multiple translations can be concatenated by adding their displacement vectors.

The inverse of a translation simply negates the displacement.

### Concrete example

If an object center is at `(1,2,3)` and you translate by `(4,-1,2)`, the new center becomes `(5,1,5)`.

### Check yourself

Why does translation preserve lengths and angles?

## 4. Scaling: changing size and sometimes shape

Source focus: slides 11-12

Scaling multiplies coordinate components by scale factors:

`(x,y,z) -> (sx x, sy y, sz z)`.

If all three factors are equal, the scaling is **uniform**. A cube remains a cube, only larger or smaller. If the factors differ, the scaling is **non-uniform**. A cube can become a rectangular box.

Unlike translation and rotation, scaling generally does not preserve lengths. Non-uniform scaling can also change angles.

The identity scaling is `(1,1,1)`. The inverse scaling uses reciprocal factors, provided no scale factor is zero.

### Concrete example

Scaling `(x,y,z)` by `(2,1,0.5)` stretches the object twice as much along x, leaves y unchanged, and compresses z to half its original size.

### Important consequence

Scaling is always relative to the origin of the coordinate system. If an object is not centered at the origin, scaling may also change its apparent position. This becomes important in the section on reference points.

### Check yourself

Why can non-uniform scaling alter the shape of an object even though every vertex is processed by the same matrix?

## 5. Rotation: changing orientation

Source focus: slides 13-15

Rotation changes orientation while preserving lengths and angles. In a right-handed coordinate system, the lecture defines standard rotations around the x-, y-, and z-axes.

The sine/cosine entries in a rotation matrix encode how one coordinate axis is mixed into another. For example, rotating around z changes x and y while leaving z unchanged.

A key property is that rotations around the **same axis** can be combined by adding angles. But rotations around **different axes generally do not commute**.

That is one of the most important facts in the entire lecture.

`Rx(a) Ry(b) != Ry(b) Rx(a)` in general.

The reason is geometric: after the first rotation, the object has changed orientation, so the second rotation acts on a differently oriented object.

The inverse of a rotation by angle `theta` is a rotation by `-theta`. For pure rotation matrices, the inverse is also the transpose.

### Concrete example

Take a book lying flat on a table. Rotate it 90 degrees around x, then 90 degrees around y. Compare that with rotating around y first, then x. The final orientation differs.

### Check yourself

Why do rotations around different axes fail to commute, even though translations do?

## 6. Mirroring and shearing

Source focus: slides 16-17

Mirroring reflects geometry across a plane. The lecture's example flips the z coordinate to mirror across the xy-plane.

Mirroring preserves lengths and angles, but it reverses orientation. That can matter for polygon winding and handedness. A right-handed coordinate system can become left-handed after a reflection.

Shearing is different: it skews an object by making one coordinate depend on another. A simple x-by-y shear has the form

`x' = x + a y`, while `y' = y` and `z' = z`.

This means higher y values create larger x displacements. Rectangles can become parallelograms.

### Check yourself

What geometric property can mirroring change even though lengths are preserved?

## 7. Composition: why matrix order matters

Source focus: slides 18-19

Real modeling tasks rarely use only one transformation. You might scale a model, rotate it, then move it into position.

Instead of applying each matrix separately to every vertex, we can multiply the matrices together first and obtain one composite matrix.

For column vectors, the rightmost matrix acts first:

`M = T R S`

means

`v' = T (R (S v))`.

So the vertex is first scaled, then rotated, then translated.

This right-to-left reading is essential. Matrix multiplication is associative, so products can be grouped, but it is generally not commutative, so the order cannot be freely swapped.

### Concrete example

Suppose a point is at `(1,0)`. If you first rotate it 90 degrees around the origin and then translate by `(2,0)`, you get a different result than translating first and then rotating. In the second case the translation itself is rotated around the origin.

### Check yourself

In `T R S v`, which transformation acts on `v` first?

## 8. Reference points: rotate or scale around something other than the origin

Source focus: slides 20-21

Rotation and scaling are naturally performed around the origin. But objects often need to rotate around another point.

The general strategy is:

1. translate the chosen reference point to the origin;
2. perform the rotation or scaling;
3. translate back.

If the reference point is `M`, then a rotation around `M` has the structure

`T(M) R T(-M)`.

Read this from right to left: first move `M` to the origin, then rotate, then restore the original location.

### Concrete example

A door should rotate around its hinge, not around its center. Translate the hinge to the origin, rotate the door, then translate the hinge back to its world position.

### Check yourself

Why does `T(M) R T(-M)` rotate around `M` instead of around the world origin?

## 9. Arbitrary-axis rotation and the idea of alignment

Source focus: slides 22-24

Rotating around x, y, or z is easy because the standard rotation matrices are already known. Rotating around an arbitrary axis is more complicated.

The lecture constructs the transformation as a sequence:

- move the axis center to the origin;
- rotate the axis until it aligns with a standard axis;
- apply the desired standard-axis rotation;
- undo the alignment rotations;
- translate back.

This is an important general problem-solving strategy in graphics:

**transform a difficult problem into a simple coordinate system, solve it there, then transform back.**

The vector tools on slides 23-24 support this idea. Normalization turns a direction into a unit vector. The cross product constructs a vector perpendicular to two given vectors. Those operations help build orthogonal coordinate frames.

### Concrete example

If you need a local z-axis to point in some arbitrary direction `d`, normalize `d` and use it as one basis axis. Then construct perpendicular axes using cross products.

### Check yourself

Why is it useful to align an arbitrary rotation axis with a standard coordinate axis before rotating?

## 10. Orthogonal bases: building a coordinate frame from geometry

Source focus: slides 25-34

The long directed-line-segment and direction-of-flight examples are easier to understand as **basis construction** problems.

An orthonormal basis consists of three unit vectors that are mutually perpendicular. If those three vectors are assembled into a rotation matrix, the matrix describes an orientation.

The lecture shows two ways to solve alignment tasks:

- compute explicit rotation angles step by step;
- directly construct an orthogonal matrix from normalized direction vectors and cross products.

The second approach is often conceptually cleaner. If one axis must point along a known direction, normalize that direction. Then use a second independent direction and a cross product to construct a perpendicular axis. A final cross product can produce the third axis.

This is exactly what the direction-of-flight example does: it aligns one model axis with the desired flight direction while constructing the remaining axes so the orientation remains orthogonal.

### Degenerate case

Cross products fail when the two input directions are parallel, because the cross product becomes the zero vector. The lecture explicitly notes this for the case where the desired flight direction is parallel to the chosen reference up direction.

This is not a minor detail: many camera and orientation algorithms need a fallback axis for such degenerate cases.

### Check yourself

Why can a cross product not define a new perpendicular axis if its two input vectors are parallel?

## 11. Active transformation versus coordinate-system change

Source focus: slides 35-39

The lecture then introduces an alternative interpretation: instead of saying "the object moved," you can say "the coordinate system used to describe the object changed."

These are two views of closely related mathematics.

Suppose a point `P` has coordinates in local system `CS_j`, but you want its coordinates in world system `CS_i`. The lecture writes a transformation `M_{i<-j}` for the change from `CS_j` to `CS_i`.

The notation is useful because it makes the direction explicit:

`P^(i) = M_{i<-j} P^(j)`.

The inverse changes back:

`M_{j<-i} = (M_{i<-j})^-1`.

And transformations through intermediate systems compose:

`M_{i<-j} M_{j<-k} = M_{i<-k}`.

This is the same matrix-composition idea as before, now interpreted as movement between coordinate frames.

### Concrete example

A wheel mesh has coordinates in wheel-local space. The car places the wheel into car-local space. The car is then placed into world space. The final world transform is the product of those frame-to-frame transformations.

### Check yourself

What does the arrow in `M_{world<-local}` tell you?

## 12. Model, view, and projection: where Lecture 3 fits into the full pipeline

Source focus: slides 43-44

The lecture connects its transformation math back to OpenGL. Modern OpenGL does not automatically manage your model/view matrices; you usually compute them in application code, often with a library such as GLM, and pass the resulting matrices to shaders.

Three conceptual transformations are important:

- **model transformation**: local object coordinates -> world coordinates;
- **view transformation**: world coordinates -> camera/view coordinates;
- **projection transformation**: view coordinates -> clip coordinates.

Lecture 3 focuses mainly on the first two ideas and on the general mathematics of transformations. Projection is treated in the next lecture.

A common combined matrix in shader code is

`P V M`.

Applied to a local-space vertex `v`, the rightmost model matrix acts first, then the view matrix, then the projection matrix:

`clip_position = P V M v`.

### Check yourself

Why does the model matrix usually depend on the object, while the view matrix is usually shared by all objects rendered from the same camera?

## 13. Modeling by transformation reuse

Source focus: slides 45-51

The cylinder and portico examples show why transformations are powerful for modeling.

Instead of creating custom geometry for every column, pedestal, roof, and floor piece, the application can start from a small set of reusable primitives. Then each primitive is translated, rotated, and scaled into the required place.

A "unit cylinder" can become a tall thin column, a short pedestal, or part of another structure simply by changing its transformation matrix.

This is hierarchical modeling in spirit: complex scenes are assembled from simpler reusable pieces whose transformations define their relationships.

### Concrete example

To arrange many identical columns around a circle, keep one column mesh. For column `i`, compute an angle, place the column at the corresponding circle position with translation, and orient it as needed with rotation. The geometry stays the same; only the transformation changes.

### Check yourself

Why is reusable primitive geometry plus transformation matrices more scalable than manually modeling each repeated object separately?

## 14. The most important transformation mistakes

The lecture's material leads to a small set of recurring errors:

### Mistake 1: ignoring the coordinate system

A vector of numbers is not enough. `(1,0,0)` could mean local x, world x, view x, or something else. Mixing spaces can make correct formulas produce wrong geometry.

### Mistake 2: multiplying matrices in the wrong order

`T R` and `R T` usually mean different geometric operations.

### Mistake 3: forgetting the reference point

Rotation and scaling happen around the origin of the current coordinate system. If the intended pivot is elsewhere, you must account for it.

### Mistake 4: confusing points and directions

In homogeneous coordinates, points and pure directions behave differently under translation. A point uses `w=1`; a direction is commonly represented with `w=0`, so translation should not change it.

### Mistake 5: constructing a basis from nearly parallel vectors

Cross products become tiny or zero when directions are parallel or almost parallel, producing unstable orientation matrices.

## 15. Put the whole lecture together

The full conceptual chain is:

`local model vertices`

`-> basic affine transformations`

`-> matrix composition`

`-> chosen reference point / basis`

`-> coordinate-system changes`

`-> model and view transforms in the rendering pipeline`.

The lecture is really teaching one reusable idea: **geometry is represented numerically, and transformations let us change the interpretation and placement of that geometry in a controlled, composable way.**

If you remember only formulas, the chapter feels like matrix manipulation. If you remember the geometric questions, the formulas become tools:

- Where should the object move? -> translation.
- How large should it be? -> scaling.
- Which direction should it face? -> rotation.
- Around which pivot? -> translate to origin, transform, translate back.
- How do several steps combine? -> matrix multiplication.
- Which coordinate system are the numbers expressed in? -> frame transformation.

## Minimum concept map

`local vertex -> affine matrix -> transformed vertex`

`translation / rotation / scaling -> composition -> reference-point handling -> coordinate-system change -> model/view transforms`

Before moving on to projection, you should be able to explain why matrix order matters and how a local-space vertex becomes a world- or view-space vertex without reading the slide formulas aloud.