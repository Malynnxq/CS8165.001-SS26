# Lecture 04 - Geometric Projection Copy-Paste Prompts

## 04-00 - Whole Lecture Explanation And Resources

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
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

## 04-01 - Compact Rule Expansion

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.

Task:
Expand the compact rule into a full explanation.
Define every symbol, word, stage, variable, or operation in simple English.
Give one numerical, geometric, or OpenGL-related example if the topic allows it.
Explain the common mistakes that happen when students memorize the rule without understanding it.
Create completion questions, ordering questions, and one small calculation or reasoning task.
Include the answer key.
If you have web access, find one human-written resource that explains the same rule or algorithm.
```

## 04-02 - Trap Repair

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.

Task:
Explain why this wrong idea sounds plausible.
Show the correct distinction with a small example.
Create a table with wrong statement, why it is tempting, corrected statement, and exam clue.
Create ten true-false-with-correction questions.
Include the answer key.
Keep the language simple enough for B1 English.
```

## 04-03 - Assignment Connection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
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

## 04-04 - Human-Written Resource Search

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
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

## 04-05 - Strict Closed-Format Examiner

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
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

## 04-S01 - Section: Linear Perspective and Planar Projections

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Linear Perspective and Planar Projections.
Source location: Sections 4.1-4.2.
Section meaning: Projection is the rule that turns 3D positions into image-plane positions..
Section check: What visual cue does perspective projection add that orthographic projection lacks?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 04-S02 - Section: Camera Modeling

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Camera Modeling.
Source location: Section 4.3.
Section meaning: A camera is not only an eye position; it is also a volume and a mapping rule..
Section check: Why can changing the near plane affect depth artifacts?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 04-S03 - Section: Specifying Projections in OpenGL

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Specifying Projections in OpenGL.
Source location: Section 4.4.
Section meaning: The projection matrix is the camera lens encoded as linear algebra in homogeneous coordinates..
Section check: What symptom suggests that the projection aspect ratio does not match the window?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 04-S04 - Section: Orthographic and Perspective Derivations

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Orthographic and Perspective Derivations.
Source location: Sections 4.5-4.6.
Section meaning: Projection matrices normalize a viewing volume; perspective also prepares the divide by w..
Section check: What does the perspective divide do to x and y coordinates?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 04-S05 - Section: Viewport Transformation

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Viewport Transformation.
Source location: Section 4.7.
Section meaning: Projection decides normalized position; viewport decides where that position lands on the screen..
Section check: Why is resizing a window related to both viewport and projection settings?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 04-T01 - Term: view volume

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: view volume.
Course definition: The 3D region visible to the camera before mapping to the screen.

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

## 04-T02 - Term: orthographic projection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: orthographic projection.
Course definition: Projection without perspective foreshortening; parallel lines stay parallel.

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

## 04-T03 - Term: perspective projection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: perspective projection.
Course definition: Projection where farther objects appear smaller after division by the homogeneous component.

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

## 04-T04 - Term: clip coordinates

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: clip coordinates.
Course definition: Coordinates produced before clipping and perspective divide.

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

## 04-T05 - Term: perspective divide

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: perspective divide.
Course definition: Division by w that produces normalized device coordinates.

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

## 04-T06 - Term: viewport transformation

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 04 - Geometric Projection.
Source chunk: course_text_parts/03_lectures/04_geometric-projection.txt.
Core idea: Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.
Process chain: view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates.
Important terms: view volume: The 3D region visible to the camera before mapping to the screen.; orthographic projection: Projection without perspective foreshortening; parallel lines stay parallel.; perspective projection: Projection where farther objects appear smaller after division by the homogeneous component.; clip coordinates: Coordinates produced before clipping and perspective divide.; perspective divide: Division by w that produces normalized device coordinates.; viewport transformation: Mapping normalized device coordinates to window or screen coordinates..
Compact rule: p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w.
Main trap: Do not confuse projection with viewport mapping; the perspective divide sits between them.
Assignment connection: 04 Projections and Clipping.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: viewport transformation.
Course definition: Mapping normalized device coordinates to window or screen coordinates.

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
