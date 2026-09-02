# Lecture 05 - Clipping Copy-Paste Prompts

## 05-00 - Whole Lecture Explanation And Resources

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Task:
Explain this lecture topic from zero to exam-ready understanding.
Start with the concrete problem in computer graphics.
Then explain each step of the process chain.
For every important term, explain the meaning, the role in the chain, and one common English verb or collocation used with it.
Add one small everyday analogy only if it makes the technical relation clearer.
End with ten closed-format questions and an answer key.
If you have web access, also find two human-written resources from university notes, official documentation, or textbooks, and explain exactly which part of this lecture each resource supports.
```

## 05-01 - Compact Rule Expansion

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.

Task:
Expand the compact rule into a full explanation.
Define every symbol, word, stage, variable, or operation in simple English.
Give one numerical, geometric, or OpenGL-related example if the topic allows it.
Explain the common mistakes that happen when students memorize the rule without understanding it.
Create completion questions, ordering questions, and one small calculation or reasoning task.
Include the answer key.
If you have web access, find one human-written resource that explains the same rule or algorithm.
```

## 05-02 - Trap Repair

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.

Task:
Explain why this wrong idea sounds plausible.
Show the correct distinction with a small example.
Create a table with wrong statement, why it is tempting, corrected statement, and exam clue.
Create ten true-false-with-correction questions.
Include the answer key.
Keep the language simple enough for B1 English.
```

## 05-03 - Assignment Connection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus assignment: 04 Projections and Clipping.

Task:
Connect the lecture topic to the assignment.
List the exact concepts the assignment probably tests.
Explain what source code, OpenGL state, buffer, shader, transformation, image result, or algorithmic step I should look for.
Create a checklist I can use while browsing assignment sources.
Create closed-format questions about the assignment connection.
Include the answer key.
Avoid asking me to write long open answers.
```

## 05-04 - Human-Written Resource Search

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Task:
Find human-written learning materials for this topic.
Prioritize university lecture notes, official OpenGL or graphics documentation, textbook chapters, and course pages by named instructors.
Avoid AI-generated summaries, SEO blogs, and shallow tutorials unless they contain a useful diagram or code example.
For each resource, give the title, author or institution if visible, link, why it is relevant, which course terms it supports, and which parts I should ignore if they go beyond CS8165.
Then create a reading sequence from easiest to most precise.
Finish with ten closed-format questions that check whether I understood the resources in relation to this course.
```

## 05-05 - Strict Closed-Format Examiner

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Task:
Act as a strict closed-format examiner for this lecture.
Ask one question at a time.
Allowed formats: multiple choice, matching, fill in the blank, ordering, diagram labeling checklist, true or false with correction, and OpenGL debugging choice.
After each answer, grade it as correct, partly correct, or wrong.
Then give the exact missing concept, the corrected distinction, and the next question.
Do not ask broad essay questions.
Cover every important term, the process chain, the compact rule, the assignment connection, and the main trap.
```

## 05-S01 - Section: Cohen-Sutherland Line Clipping

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Cohen-Sutherland Line Clipping.
Source location: Section 5.1.
Section meaning: Outcodes are a cheap classification before doing intersection math..
Section check: What does a nonzero bitwise AND of two endpoint outcodes imply?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 05-S02 - Section: Cyrus-Beck Line Clipping

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Cyrus-Beck Line Clipping.
Source location: Section 5.2.
Section meaning: Clipping a parametric line means narrowing the valid t interval..
Section check: Why does Cyrus-Beck naturally require convex clipping regions?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 05-S03 - Section: Sutherland-Hodgman Polygon Clipping

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Sutherland-Hodgman Polygon Clipping.
Source location: Section 5.3.
Section meaning: Polygon clipping is repeated edge-by-edge filtering plus intersection insertion..
Section check: When can polygon clipping increase the number of vertices?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 05-S04 - Section: Weiler-Atherton and Greiner-Hormann

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Weiler-Atherton and Greiner-Hormann.
Source location: Sections 5.4-5.5.
Section meaning: Complex polygon clipping is about traversing boundary networks after intersections are known..
Section check: Why are intersection ordering and traversal rules important for polygon clipping?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 05-T01 - Term: clipping

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: clipping.
Course definition: Removing or cutting geometry outside a valid window, plane, or volume.

Task:
Explain this term as a graphics concept, not as a dictionary word.
Show where it appears in the process chain.
Explain what it is often confused with.
Give five B1-level example sentences using correct English collocations.
Create a matching task that distinguishes this term from five related terms.
Create five multiple-choice questions with near-miss distractors.
Include the answer key and one sentence explaining each answer.
If you have web access, find one human-written source that explains this term clearly and state why it is reliable.
```

## 05-T02 - Term: Cohen-Sutherland

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: Cohen-Sutherland.
Course definition: Line clipping method using region/outcodes to reject, accept, or clip line segments.

Task:
Explain this term as a graphics concept, not as a dictionary word.
Show where it appears in the process chain.
Explain what it is often confused with.
Give five B1-level example sentences using correct English collocations.
Create a matching task that distinguishes this term from five related terms.
Create five multiple-choice questions with near-miss distractors.
Include the answer key and one sentence explaining each answer.
If you have web access, find one human-written source that explains this term clearly and state why it is reliable.
```

## 05-T03 - Term: Sutherland-Hodgman

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: Sutherland-Hodgman.
Course definition: Polygon clipping method that processes polygon vertices against clipping boundaries.

Task:
Explain this term as a graphics concept, not as a dictionary word.
Show where it appears in the process chain.
Explain what it is often confused with.
Give five B1-level example sentences using correct English collocations.
Create a matching task that distinguishes this term from five related terms.
Create five multiple-choice questions with near-miss distractors.
Include the answer key and one sentence explaining each answer.
If you have web access, find one human-written source that explains this term clearly and state why it is reliable.
```

## 05-T04 - Term: Cyrus-Beck

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: Cyrus-Beck.
Course definition: Parametric line clipping method using entering and leaving parameter intervals.

Task:
Explain this term as a graphics concept, not as a dictionary word.
Show where it appears in the process chain.
Explain what it is often confused with.
Give five B1-level example sentences using correct English collocations.
Create a matching task that distinguishes this term from five related terms.
Create five multiple-choice questions with near-miss distractors.
Include the answer key and one sentence explaining each answer.
If you have web access, find one human-written source that explains this term clearly and state why it is reliable.
```

## 05-T05 - Term: outcode

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: outcode.
Course definition: A compact code describing where a point lies relative to clipping boundaries.

Task:
Explain this term as a graphics concept, not as a dictionary word.
Show where it appears in the process chain.
Explain what it is often confused with.
Give five B1-level example sentences using correct English collocations.
Create a matching task that distinguishes this term from five related terms.
Create five multiple-choice questions with near-miss distractors.
Include the answer key and one sentence explaining each answer.
If you have web access, find one human-written source that explains this term clearly and state why it is reliable.
```

## 05-T06 - Term: intersection point

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 05 - Clipping.
Source chunk: course_text_parts/03_lectures/05_clipping.txt.
Core idea: Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.
Process chain: primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive.
Important terms: clipping: Removing or cutting geometry outside a valid window, plane, or volume.; Cohen-Sutherland: Line clipping method using region/outcodes to reject, accept, or clip line segments.; Sutherland-Hodgman: Polygon clipping method that processes polygon vertices against clipping boundaries.; Cyrus-Beck: Parametric line clipping method using entering and leaving parameter intervals.; outcode: A compact code describing where a point lies relative to clipping boundaries.; intersection point: New boundary point created when a primitive crosses a clipping edge or plane..
Compact rule: line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval.
Main trap: Do not describe clipping as only deletion; crossing primitives can create new vertices.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: intersection point.
Course definition: New boundary point created when a primitive crosses a clipping edge or plane.

Task:
Explain this term as a graphics concept, not as a dictionary word.
Show where it appears in the process chain.
Explain what it is often confused with.
Give five B1-level example sentences using correct English collocations.
Create a matching task that distinguishes this term from five related terms.
Create five multiple-choice questions with near-miss distractors.
Include the answer key and one sentence explaining each answer.
If you have web access, find one human-written source that explains this term clearly and state why it is reliable.
```
