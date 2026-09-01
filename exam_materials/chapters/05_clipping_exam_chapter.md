# Lecture 05 - Clipping Exam Chapter

Source lecture chunk: `course_text_parts/03_lectures/05_clipping.txt`
Extracted source pages: 56
Primary assignment connection: 04 Projections and Clipping

## 1. What Problem This Chapter Solves

Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization. The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.

The first anchor term is `clipping`: Removing or cutting geometry outside a valid window, plane, or volume. This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.

## 2. Required Background

Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.

For this lecture, the required background is the ability to follow this relation: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.

## 3. The Chapter Explained

### 05.1 Cohen-Sutherland Line Clipping

Source location: Section 5.1

Cohen-Sutherland assigns outcodes to line endpoints based on which side of the clipping window they lie on. These codes allow quick accept, quick reject, or partial clipping. The algorithm is efficient because many cases are decided before computing intersections.

The exam-friendly idea is the logic of region codes: if both endpoints are inside, keep the segment. If the bitwise AND of the outcodes is nonzero, both endpoints share an outside region and the segment can be rejected. Otherwise, compute an intersection and continue.

Study meaning: Outcodes are a cheap classification before doing intersection math.

Closed check: What does a nonzero bitwise AND of two endpoint outcodes imply?

### 05.2 Cyrus-Beck Line Clipping

Source location: Section 5.2

Cyrus-Beck treats the line parametrically and clips against convex boundaries. Instead of repeatedly using region codes, it finds entering and leaving parameter values along the line.

The key is to reason about the line parameter t. A clipped line segment is not a new unrelated line; it is a restricted interval of the original parametric line. Boundary tests shrink that interval.

Study meaning: Clipping a parametric line means narrowing the valid t interval.

Closed check: Why does Cyrus-Beck naturally require convex clipping regions?

### 05.3 Sutherland-Hodgman Polygon Clipping

Source location: Section 5.3

Sutherland-Hodgman clips a polygon against one boundary at a time. For each edge of the polygon, it decides whether vertices are inside or outside and emits zero, one, or two vertices depending on transitions across the boundary.

This algorithm is easiest to understand as a stream processor. Feed in a polygon, clip it against the left boundary, feed the result into the right boundary, and so on. Each boundary can add intersection vertices.

Study meaning: Polygon clipping is repeated edge-by-edge filtering plus intersection insertion.

Closed check: When can polygon clipping increase the number of vertices?

### 05.4 Weiler-Atherton and Greiner-Hormann

Source location: Sections 5.4-5.5

These algorithms address more complex polygon clipping scenarios, especially when polygon relationships are not as simple as convex-window clipping. They organize intersections and traversal rules to produce correct output boundaries.

For preparation, focus on why simpler algorithms are not enough. Complex polygon intersection can require following alternating boundaries of subject and clipping polygons. That is a topology problem, not only a line-intersection problem.

Study meaning: Complex polygon clipping is about traversing boundary networks after intersections are known.

Closed check: Why are intersection ordering and traversal rules important for polygon clipping?

## 4. Key Terms In Plain Language

Learn these terms as roles in a system, not as dictionary entries.

### clipping

Removing or cutting geometry outside a valid window, plane, or volume. In an exam answer, connect `clipping` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

### Cohen-Sutherland

Line clipping method using region/outcodes to reject, accept, or clip line segments. In an exam answer, connect `Cohen-Sutherland` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

### Sutherland-Hodgman

Polygon clipping method that processes polygon vertices against clipping boundaries. In an exam answer, connect `Sutherland-Hodgman` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

### Cyrus-Beck

Parametric line clipping method using entering and leaving parameter intervals. In an exam answer, connect `Cyrus-Beck` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

### outcode

A compact code describing where a point lies relative to clipping boundaries. In an exam answer, connect `outcode` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

### intersection point

New boundary point created when a primitive crosses a clipping edge or plane. In an exam answer, connect `intersection point` to the chapter chain: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`. Say where it appears, what it affects, and what would break if you misunderstood it.

## 5. Formula, Algorithm, Or Compact Rule

`line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval`

Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.

## 6. Assignment Connection

This chapter connects most directly to `04 Projections and Clipping`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive`.

Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.

## 7. Typical Exam Traps

Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.

The trap is dangerous because it usually sounds close to the truth. High exam performance depends on catching these near-misses quickly. When a multiple-choice option looks plausible, test it against the full chain: input, operation, output, next use. If one of those links is missing or wrong, the option is probably a distractor.

## 8. What A Strong Answer Must Contain

- The problem this chapter solves.
- The important data or object representation.
- The operation, algorithm, formula, or API mechanism.
- The output representation.
- The next pipeline stage or later use.
- One assignment or OpenGL/software connection.
- One typical mistake and the corrected distinction.

## 9. Closed-Format Self-Test

1. Complete the chain: `primitive -> boundary tests -> inside/outside classification -> ____ -> clipped primitive`
2. Match `Cohen-Sutherland` to its role: Line clipping method using region/outcodes to reject, accept, or clip line segments.
3. Select the dangerous misconception: Do not describe clipping as only deletion; crossing primitives can create new vertices.
4. Explain in one sentence why `Sutherland-Hodgman` belongs in this chapter.

## 10. End Condition

You are done with Lecture 05 only when you can read a new question, recognize that it belongs to `Clipping`, and reconstruct the relevant part of `primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.
