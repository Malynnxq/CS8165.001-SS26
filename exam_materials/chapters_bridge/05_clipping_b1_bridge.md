# Lecture 05 - Clipping B1 Bridge

Read this before the normal exam chapter if the English feels too dense. This version does not replace the main chapter. It prepares you for it.

## 1. Starting Point

This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called Clipping works in a rendering system?

## 2. Everyday Bridge

You already know cropping a photo or cutting away the part of a picture that is outside a window. Clipping is the geometric version of that idea.

The main idea in easier English is this: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.

A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.

For this lecture, the process is:

1. primitive. This is the start.

2. boundary tests. This comes after the previous step.

3. inside/outside classification. This comes after the previous step.

4. intersections. This comes after the previous step.

5. clipped primitive. This comes after the previous step.

When you read the main chapter, do not try to memorize the whole sentence first. Ask three smaller questions. What goes in? What changes? What comes out?

## 3. English Bridge

These phrases appear often in computer graphics texts. Learn them as small sentence patterns.

### to represent something

Meaning: to show something in a certain form.

Course example: In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.

How to read it: if you see `to represent something`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to convert A into B

Meaning: to change information from one form into another form.

Course example: The course often says that one stage converts data into the next stage of this process: primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive.

How to read it: if you see `to convert A into B`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to map A to B

Meaning: to connect one space, value, or position to another space, value, or position.

Course example: If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.

How to read it: if you see `to map A to B`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to determine whether

Meaning: to decide if something is true or false.

Course example: Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.

How to read it: if you see `to determine whether`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to pass a test

Meaning: to satisfy a rule and continue to the next step.

Course example: A fragment can pass a depth test or fail it, so it may or may not become visible.

How to read it: if you see `to pass a test`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to depend on

Meaning: to need something else before it can work correctly.

Course example: The later part of the chapter depends on the earlier part of this chain: primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive.

How to read it: if you see `to depend on`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### to store a value

Meaning: to keep a value in memory so that it can be used later.

Course example: Buffers, textures, and framebuffers store values for rendering.

How to read it: if you see `to store a value`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

### at draw time

Meaning: at the exact moment when the GPU receives the draw command.

Course example: In OpenGL, the current state at draw time is very important.

How to read it: if you see `at draw time`, look for the thing before the verb and the thing after the verb. The first thing usually gives the input or object. The second thing usually gives the result, rule, or dependency.

## 4. Terminology Bridge

The important words are not random vocabulary. Each word has a job in the rendering story.

### clipping

Simple meaning: Removing or cutting geometry outside a valid window, plane, or volume.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `clipping` is used when the system needs to describe, change, test, store, or use this kind of information.

### Cohen-Sutherland

Simple meaning: Line clipping method using region/outcodes to reject, accept, or clip line segments.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `Cohen-Sutherland` is used when the system needs to describe, change, test, store, or use this kind of information.

### Sutherland-Hodgman

Simple meaning: Polygon clipping method that processes polygon vertices against clipping boundaries.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `Sutherland-Hodgman` is used when the system needs to describe, change, test, store, or use this kind of information.

### Cyrus-Beck

Simple meaning: Parametric line clipping method using entering and leaving parameter intervals.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `Cyrus-Beck` is used when the system needs to describe, change, test, store, or use this kind of information.

### outcode

Simple meaning: A compact code describing where a point lies relative to clipping boundaries.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `outcode` is used when the system needs to describe, change, test, store, or use this kind of information.

### intersection point

Simple meaning: New boundary point created when a primitive crosses a clipping edge or plane.

Why it is here: this word helps explain clipping. It connects to this process: `primitive, then boundary tests, then inside/outside classification, then intersections, then clipped primitive`.

Good sentence pattern: `intersection point` is used when the system needs to describe, change, test, store, or use this kind of information.

## 5. Step By Step Bridge

Each part below connects a lecture section to easier English. Read the easy sentence first. Then read the explanation. Then read the same part in the normal chapter.

### 05.1 Cohen-Sutherland Line Clipping

Easy sentence: this section explains one part of clipping.

Main connection: Outcodes are a cheap classification before doing intersection math.

What this means in slower English:

Cohen Sutherland assigns outcodes to line endpoints based on which side of the clipping window they lie on. These codes allow quick accept, quick reject, or partial clipping. The algorithm is efficient because many cases are decided before computing intersections.

The exam friendly idea is the logic of region codes, if both endpoints are inside, keep the segment. If the bitwise AND of the outcodes is nonzero, both endpoints share an outside region and the segment can be rejected. Otherwise, compute an intersection and continue.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: What does a nonzero bitwise AND of two endpoint outcodes imply?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 05.2 Cyrus-Beck Line Clipping

Easy sentence: this section explains one part of clipping.

Main connection: Clipping a parametric line means narrowing the valid t interval.

What this means in slower English:

Cyrus Beck treats the line parametrically and clips against convex boundaries. Instead of repeatedly using region codes, it finds entering and leaving parameter values along the line.

The key is to reason about the line parameter t. A clipped line segment is not a new unrelated line, it is a restricted interval of the original parametric line. Boundary tests shrink that interval.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why does Cyrus-Beck naturally require convex clipping regions?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 05.3 Sutherland-Hodgman Polygon Clipping

Easy sentence: this section explains one part of clipping.

Main connection: Polygon clipping is repeated edge-by-edge filtering plus intersection insertion.

What this means in slower English:

Sutherland Hodgman clips a polygon against one boundary at a time. For each edge of the polygon, it decides whether vertices are inside or outside and emits zero, one, or two vertices depending on transitions across the boundary.

This algorithm is easiest to understand as a stream processor. Feed in a polygon, clip it against the left boundary, feed the result into the right boundary, and so on. Each boundary can add intersection vertices.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: When can polygon clipping increase the number of vertices?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

### 05.4 Weiler-Atherton and Greiner-Hormann

Easy sentence: this section explains one part of clipping.

Main connection: Complex polygon clipping is about traversing boundary networks after intersections are known.

What this means in slower English:

These algorithms address more complex polygon clipping scenarios, especially when polygon relationships are not as simple as convex window clipping. They organize intersections and traversal rules to produce correct output boundaries.

For preparation, focus on why simpler algorithms are not enough. Complex polygon intersection can require following alternating boundaries of subject and clipping polygons. That is a topology problem, not only a line intersection problem.

Language help: in this section, look for verbs such as prepares, handles, creates, applies, computes, decides, stores, maps, tests, or converts. The verb tells you what is happening. The object after the verb is usually the data, stage, value, or result that the course wants you to understand.

Check question in simple form: Why are intersection ordering and traversal rules important for polygon clipping?

If you cannot answer it yet, go back to the process and ask what goes in, what changes, and what comes out.

## 6. Reading The Main Chapter After This

Now read the normal chapter for this lecture. When a sentence feels hard, do not translate every word first. First mark the verb. Then mark the technical noun. Then ask how the noun moves through the process.

The most dangerous misunderstanding in this lecture is: Do not describe clipping as only deletion; crossing primitives can create new vertices.

The compact rule is: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval

You are ready for the main version when you can explain the process with simple English, recognize the important course words, and understand the verbs that connect the words.
