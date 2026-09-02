# Lecture 07 - Visibility Determination Copy-Paste Prompts

## 07-00 - Whole Lecture Explanation And Resources

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
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

## 07-01 - Compact Rule Expansion

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus compact rule: visible fragment = candidate with passing depth/visibility test at the sample.

Task:
Expand the compact rule into a full explanation.
Define every symbol, word, stage, variable, or operation in simple English.
Give one numerical, geometric, or OpenGL-related example if the topic allows it.
Explain the common mistakes that happen when students memorize the rule without understanding it.
Create completion questions, ordering questions, and one small calculation or reasoning task.
Include the answer key.
If you have web access, find one human-written resource that explains the same rule or algorithm.
```

## 07-02 - Trap Repair

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus trap: Do not confuse generating a fragment with proving that it is visible.

Task:
Explain why this wrong idea sounds plausible.
Show the correct distinction with a small example.
Create a table with wrong statement, why it is tempting, corrected statement, and exam clue.
Create ten true-false-with-correction questions.
Include the answer key.
Keep the language simple enough for B1 English.
```

## 07-03 - Assignment Connection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus assignment: Rasterization and integrated rendering tasks.

Task:
Connect the lecture topic to the assignment.
List the exact concepts the assignment probably tests.
Explain what source code, OpenGL state, buffer, shader, transformation, image result, or algorithmic step I should look for.
Create a checklist I can use while browsing assignment sources.
Create closed-format questions about the assignment connection.
Include the answer key.
Avoid asking me to write long open answers.
```

## 07-04 - Human-Written Resource Search

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
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

## 07-05 - Strict Closed-Format Examiner

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
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

## 07-S01 - Section: Object-Based Algorithms

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Object-Based Algorithms.
Source location: Section 7.1.
Section meaning: Object-based visibility tries to solve visibility with geometry before final pixels are written..
Section check: Why can intersecting polygons make simple depth sorting fail?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 07-S02 - Section: Binary Space Partitioning

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Binary Space Partitioning.
Source location: Section 7.2.
Section meaning: A BSP tree stores a recursive answer to 'which side of this plane is the geometry on?'.
Section check: Why can building a BSP tree require splitting polygons?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 07-S03 - Section: Warnock Algorithm

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Warnock Algorithm.
Source location: Section 7.3.
Section meaning: When a region is too complicated, subdivide until the answer becomes simple..
Section check: What makes Warnock's algorithm image-space rather than object-space?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 07-S04 - Section: Depth Buffer Algorithm

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Depth Buffer Algorithm.
Source location: Section 7.4.
Section meaning: The depth buffer is a per-sample competition for closest visible fragment..
Section check: Why should the near plane not be unnecessarily close to the camera?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 07-S05 - Section: Depth Extensions and Ray Casting

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Depth Extensions and Ray Casting.
Source location: Sections 7.5-7.6.
Section meaning: Rasterization pushes primitives to pixels; ray casting pulls visibility from pixels into the scene..
Section check: Why is transparency harder than opaque nearest-surface visibility?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 07-T01 - Term: depth buffer

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: depth buffer.
Course definition: Per-pixel storage of depth values used to keep the nearest visible fragment.

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

## 07-T02 - Term: z-buffer algorithm

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: z-buffer algorithm.
Course definition: Image-space visibility method comparing fragment depths at each pixel.

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

## 07-T03 - Term: Painter's algorithm

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: Painter's algorithm.
Course definition: Object-order visibility method based on drawing farther objects before nearer objects.

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

## 07-T04 - Term: BSP tree

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: BSP tree.
Course definition: Space-partitioning structure that can support visibility ordering.

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

## 07-T05 - Term: Warnock algorithm

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: Warnock algorithm.
Course definition: Image-space subdivision method for resolving visible surfaces in regions.

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

## 07-T06 - Term: ray casting

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 07 - Visibility Determination.
Source chunk: course_text_parts/03_lectures/07_visibility-determination.txt.
Core idea: Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.
Process chain: many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution.
Important terms: depth buffer: Per-pixel storage of depth values used to keep the nearest visible fragment.; z-buffer algorithm: Image-space visibility method comparing fragment depths at each pixel.; Painter's algorithm: Object-order visibility method based on drawing farther objects before nearer objects.; BSP tree: Space-partitioning structure that can support visibility ordering.; Warnock algorithm: Image-space subdivision method for resolving visible surfaces in regions.; ray casting: Finding visible surfaces by tracing rays from image samples into the scene..
Compact rule: visible fragment = candidate with passing depth/visibility test at the sample.
Main trap: Do not confuse generating a fragment with proving that it is visible.
Assignment connection: Rasterization and integrated rendering tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: ray casting.
Course definition: Finding visible surfaces by tracing rays from image samples into the scene.

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
