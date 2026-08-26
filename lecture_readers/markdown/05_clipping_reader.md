# Lecture 05 - Clipping

Source chunk: `course_text_parts/03_lectures/05_clipping.txt`
Extracted slide pages in source chunk: 56

This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.

## Big Picture

This lecture focuses on algorithms that remove or trim geometry against boundaries. Clipping is a geometric operation before rasterization, not a visibility test between overlapping objects.

## How To Read This Lecture

- First read the big picture and the mental models.
- Then open the source chunk and compare the slide bullets to the commentary.
- After each section, answer the check question without notes.
- If the check feels vague, revisit the source pages listed for that section.

## Slide Walkthrough

This section adds a short reading comment for every extracted slide page. Use it when the original PDF page is too terse.

- Page 1: **Untitled slide**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 2: **Clipping Projected Geometry 1/2**
  - Reading comment: Read this as a coordinate-space step. Name the input space, the matrix or operation, and the output space.
- Page 3: **Clipping Projected Geometry 2/2**
  - Reading comment: Read this as pipeline state and data flow. Ask which OpenGL object or shader stage owns the data at this point.
- Page 4: **5.1 Cohen-Sutherland Line Clipping**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 5: **5.1 Cohen-Sutherland Line Clipping**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 6: **Brute-Force Line Clipping 1/2**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 7: **Brute-Force Line Clipping 2/2**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 8: **Endpoint Analysis 1/2**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 9: **Endpoint Analysis 2/2**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 10: **Binary Coding of Half-Planes 1/3**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 11: **Binary Coding of Half-Planes 2/3**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 12: **Binary Coding of Half-Planes 3/3**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 13: **Pseudo Code**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 14: **Example**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 15: **Evaluation**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 16: **5.2 Cyrus-Beck Line Clipping**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 17: **Cyrus-Beck Line Clipping**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 18: **Parametric Line Representation**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 19: **Intersection Point Calculation 1/2**
  - Reading comment: Read this as continuous-to-discrete conversion. Ask which samples are covered and which attributes are interpolated.
- Page 20: **Intersection Point Calculation 2/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 21: **Determine Relevant t-Values**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 22: **Pseudo Code**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 23: **Axis-Parallel Clipping Region**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 24: **Comparison with Cohen-Sutherland**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 25: **5.3 Sutherland-Hodgman Polygon Clipping**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 26: **Sutherland-Hodgman Polygon Clipping 1/2**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 27: **Sutherland-Hodgman Polygon Clipping 2/2**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 28: **Four Cases**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 29: **Proceeding**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 30: **Pipeline Version**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 31: **Pseudo Code**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 32: **Inside Test**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 33: **Intersection Computation**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 34: **5.4 Weiler-Atherton Polygon Clipping**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 35: **Weiler-Atherton Polygon Clipping**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 36: **Example Run**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 37: **Intersection Types**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 38: **Contour Processing**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 39: **Evaluation**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 40: **5.5 Greiner-Hormann Polygon Clipping**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 41: **Greiner-Hormann**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 42: **Chalk Wagon Metaphor**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 43: **Contour Detection**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 44: **Set Operations**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 45: **Data Structure 1/2**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 46: **Data Structure 2/2**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 47: **Proceeding**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 48: **Pseudo Code**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 49: **Winding Number 1/3**
  - Reading comment: Read this as an occlusion decision. Decide whether the method works in object space, image space, or per-fragment depth space.
- Page 50: **Winding Number 2/3**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 51: **Winding Number 3/3**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 52: **Special Cases**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 53: **Evaluation**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 54: **by exploiting binary outcodes**
  - Reading comment: Read this as boundary logic. Identify what is inside, what is outside, and when new intersection vertices are created.
- Page 55: **Literature and other sources used in this chapter**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?
- Page 56: **Addison-Wesley 2013.**
  - Reading comment: Read this slide by connecting the bullet terms causally: what problem is being solved, what data is used, and what output is produced?

## 05.1 Cohen-Sutherland Line Clipping

Source location: Section 5.1

### Commentary

Cohen-Sutherland assigns outcodes to line endpoints based on which side of the clipping window they lie on. These codes allow quick accept, quick reject, or partial clipping. The algorithm is efficient because many cases are decided before computing intersections.

The exam-friendly idea is the logic of region codes: if both endpoints are inside, keep the segment. If the bitwise AND of the outcodes is nonzero, both endpoints share an outside region and the segment can be rejected. Otherwise, compute an intersection and continue.

### Mental Model

Outcodes are a cheap classification before doing intersection math.

### Check Yourself

What does a nonzero bitwise AND of two endpoint outcodes imply?

## 05.2 Cyrus-Beck Line Clipping

Source location: Section 5.2

### Commentary

Cyrus-Beck treats the line parametrically and clips against convex boundaries. Instead of repeatedly using region codes, it finds entering and leaving parameter values along the line.

The key is to reason about the line parameter t. A clipped line segment is not a new unrelated line; it is a restricted interval of the original parametric line. Boundary tests shrink that interval.

### Mental Model

Clipping a parametric line means narrowing the valid t interval.

### Check Yourself

Why does Cyrus-Beck naturally require convex clipping regions?

## 05.3 Sutherland-Hodgman Polygon Clipping

Source location: Section 5.3

### Commentary

Sutherland-Hodgman clips a polygon against one boundary at a time. For each edge of the polygon, it decides whether vertices are inside or outside and emits zero, one, or two vertices depending on transitions across the boundary.

This algorithm is easiest to understand as a stream processor. Feed in a polygon, clip it against the left boundary, feed the result into the right boundary, and so on. Each boundary can add intersection vertices.

### Mental Model

Polygon clipping is repeated edge-by-edge filtering plus intersection insertion.

### Check Yourself

When can polygon clipping increase the number of vertices?

## 05.4 Weiler-Atherton and Greiner-Hormann

Source location: Sections 5.4-5.5

### Commentary

These algorithms address more complex polygon clipping scenarios, especially when polygon relationships are not as simple as convex-window clipping. They organize intersections and traversal rules to produce correct output boundaries.

For preparation, focus on why simpler algorithms are not enough. Complex polygon intersection can require following alternating boundaries of subject and clipping polygons. That is a topology problem, not only a line-intersection problem.

### Mental Model

Complex polygon clipping is about traversing boundary networks after intersections are known.

### Check Yourself

Why are intersection ordering and traversal rules important for polygon clipping?

## End-of-Lecture Summary

If you remember only one thing from Lecture 05, remember this: This lecture focuses on algorithms that remove or trim geometry against boundaries. Clipping is a geometric operation before rasterization, not a visibility test between overlapping objects.

Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.
