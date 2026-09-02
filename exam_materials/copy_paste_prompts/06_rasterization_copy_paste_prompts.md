# Lecture 06 - Rasterization Copy-Paste Prompts

## 06-00 - Whole Lecture Explanation And Resources

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
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

## 06-01 - Compact Rule Expansion

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.

Task:
Expand the compact rule into a full explanation.
Define every symbol, word, stage, variable, or operation in simple English.
Give one numerical, geometric, or OpenGL-related example if the topic allows it.
Explain the common mistakes that happen when students memorize the rule without understanding it.
Create completion questions, ordering questions, and one small calculation or reasoning task.
Include the answer key.
If you have web access, find one human-written resource that explains the same rule or algorithm.
```

## 06-02 - Trap Repair

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus trap: Do not call every generated fragment a final pixel.

Task:
Explain why this wrong idea sounds plausible.
Show the correct distinction with a small example.
Create a table with wrong statement, why it is tempting, corrected statement, and exam clue.
Create ten true-false-with-correction questions.
Include the answer key.
Keep the language simple enough for B1 English.
```

## 06-03 - Assignment Connection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus assignment: 05 Rasterization.

Task:
Connect the lecture topic to the assignment.
List the exact concepts the assignment probably tests.
Explain what source code, OpenGL state, buffer, shader, transformation, image result, or algorithmic step I should look for.
Create a checklist I can use while browsing assignment sources.
Create closed-format questions about the assignment connection.
Include the answer key.
Avoid asking me to write long open answers.
```

## 06-04 - Human-Written Resource Search

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
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

## 06-05 - Strict Closed-Format Examiner

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
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

## 06-S01 - Section: Line Rasterization

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Line Rasterization.
Source location: Section 6.1.
Section meaning: Rasterizing a line means approximating a continuous path by grid decisions..
Section check: Why are incremental error updates useful in line rasterization?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 06-S02 - Section: Triangle Edge Rasterization

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Triangle Edge Rasterization.
Source location: Section 6.2.
Section meaning: Triangle rasterization answers the question: which samples are inside this projected triangle?.
Section check: What later stage can reject a fragment after triangle coverage succeeds?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 06-S03 - Section: Region Filling

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Region Filling.
Source location: Section 6.3.
Section meaning: Filling is about turning boundary descriptions into consistent interior samples..
Section check: Why can inconsistent edge rules create cracks between adjacent primitives?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 06-S04 - Section: Scanline-Based Triangle Rasterization

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Scanline-Based Triangle Rasterization.
Source location: Section 6.4.
Section meaning: Each scanline asks: where does this triangle enter and leave this row?.
Section check: Which attributes might be interpolated while filling triangle spans?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 06-S05 - Section: Tile-Based Triangle Rasterization

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Tile-Based Triangle Rasterization.
Source location: Section 6.5.
Section meaning: Block-based rasterization keeps the same coverage problem but changes the work organization..
Section check: Why is block organization attractive for parallel graphics hardware?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 06-T01 - Term: scan conversion

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: scan conversion.
Course definition: Determining which discrete samples are covered by an ideal geometric primitive.

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

## 06-T02 - Term: triangle coverage

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: triangle coverage.
Course definition: Testing which pixel/sample positions lie inside a triangle.

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

## 06-T03 - Term: barycentric coordinates

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: barycentric coordinates.
Course definition: Weights relative to triangle vertices used for inside tests and interpolation.

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

## 06-T04 - Term: interpolation

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: interpolation.
Course definition: Computing per-fragment values from vertex attributes.

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

## 06-T05 - Term: aliasing

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: aliasing.
Course definition: Artifacts caused when continuous signals are sampled too coarsely.

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

## 06-T06 - Term: fragment candidate

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 06 - Rasterization.
Source chunk: course_text_parts/03_lectures/06_rasterization.txt.
Core idea: Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.
Process chain: projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests.
Important terms: scan conversion: Determining which discrete samples are covered by an ideal geometric primitive.; triangle coverage: Testing which pixel/sample positions lie inside a triangle.; barycentric coordinates: Weights relative to triangle vertices used for inside tests and interpolation.; interpolation: Computing per-fragment values from vertex attributes.; aliasing: Artifacts caused when continuous signals are sampled too coarsely.; fragment candidate: A potential contribution to the framebuffer, not yet a guaranteed visible pixel..
Compact rule: attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1.
Main trap: Do not call every generated fragment a final pixel.
Assignment connection: 05 Rasterization.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: fragment candidate.
Course definition: A potential contribution to the framebuffer, not yet a guaranteed visible pixel.

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
