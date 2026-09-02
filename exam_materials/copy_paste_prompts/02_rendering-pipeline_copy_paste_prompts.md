# Lecture 02 - Rendering Pipeline Copy-Paste Prompts

## 02-00 - Whole Lecture Explanation And Resources

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
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

## 02-01 - Compact Rule Expansion

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus compact rule: vertices -> primitives -> fragments -> tests -> pixels.

Task:
Expand the compact rule into a full explanation.
Define every symbol, word, stage, variable, or operation in simple English.
Give one numerical, geometric, or OpenGL-related example if the topic allows it.
Explain the common mistakes that happen when students memorize the rule without understanding it.
Create completion questions, ordering questions, and one small calculation or reasoning task.
Include the answer key.
If you have web access, find one human-written resource that explains the same rule or algorithm.
```

## 02-02 - Trap Repair

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.

Task:
Explain why this wrong idea sounds plausible.
Show the correct distinction with a small example.
Create a table with wrong statement, why it is tempting, corrected statement, and exam clue.
Create ten true-false-with-correction questions.
Include the answer key.
Keep the language simple enough for B1 English.
```

## 02-03 - Assignment Connection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus assignment: 01 Rendering Pipeline.

Task:
Connect the lecture topic to the assignment.
List the exact concepts the assignment probably tests.
Explain what source code, OpenGL state, buffer, shader, transformation, image result, or algorithmic step I should look for.
Create a checklist I can use while browsing assignment sources.
Create closed-format questions about the assignment connection.
Include the answer key.
Avoid asking me to write long open answers.
```

## 02-04 - Human-Written Resource Search

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
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

## 02-05 - Strict Closed-Format Examiner

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
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

## 02-S01 - Section: Rendering Process

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Rendering Process.
Source location: Section 2.1.
Section meaning: Vertices become primitives, primitives become fragments, and fragments compete to become pixel updates..
Section check: What is the difference between a fragment and a final pixel?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 02-S02 - Section: OpenGL Overview

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: OpenGL Overview.
Source location: Section 2.2.
Section meaning: OpenGL draw calls consume the state machine as it exists right now..
Section check: Why can binding the wrong vertex array or shader program produce a valid draw call with wrong output?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 02-S03 - Section: OpenGL Rendering

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: OpenGL Rendering.
Source location: Section 2.3.
Section meaning: Modern OpenGL makes the data path explicit; that gives control but also creates responsibility..
Section check: Which data usually goes into vertex attributes, and which data usually goes into uniforms?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 02-S04 - Section: OpenGL Rendering Pipeline

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: OpenGL Rendering Pipeline.
Source location: Section 2.4.
Section meaning: Programmable shaders compute values; fixed pipeline stages decide coverage, interpolation, tests, and output rules..
Section check: If your geometry appears in wireframe but colors are wrong, which stages become suspicious?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 02-S05 - Section: Fragment Tests, Framebuffer, and Pixel-Based Rendering

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Fragment Tests, Framebuffer, and Pixel-Based Rendering.
Source location: Sections 2.5-2.7.
Section meaning: The framebuffer is the destination; fragment operations are the rules for writing into it..
Section check: Why can two fragments with different colors produce only one visible pixel color?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 02-T01 - Term: application stage

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: application stage.
Course definition: CPU-side preparation of models, scene data, interaction, animation, and rendering state.

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

## 02-T02 - Term: geometry stage

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: geometry stage.
Course definition: Pipeline stage that transforms vertices and prepares primitives.

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

## 02-T03 - Term: rasterization

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: rasterization.
Course definition: Conversion of projected primitives into fragment candidates on a sample grid.

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

## 02-T04 - Term: fragment

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: fragment.
Course definition: A candidate pixel contribution produced by rasterization before final tests and blending.

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

## 02-T05 - Term: framebuffer

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: framebuffer.
Course definition: Memory target that stores color, depth, stencil, or related per-pixel results.

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

## 02-T06 - Term: double buffering

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 02 - Rendering Pipeline.
Source chunk: course_text_parts/03_lectures/02_rendering-pipeline.txt.
Core idea: Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.
Process chain: application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer.
Important terms: application stage: CPU-side preparation of models, scene data, interaction, animation, and rendering state.; geometry stage: Pipeline stage that transforms vertices and prepares primitives.; rasterization: Conversion of projected primitives into fragment candidates on a sample grid.; fragment: A candidate pixel contribution produced by rasterization before final tests and blending.; framebuffer: Memory target that stores color, depth, stencil, or related per-pixel results.; double buffering: Using front and back buffers so drawing can happen off-screen before display swap..
Compact rule: vertices -> primitives -> fragments -> tests -> pixels.
Main trap: Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.
Assignment connection: 01 Rendering Pipeline.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: double buffering.
Course definition: Using front and back buffers so drawing can happen off-screen before display swap.

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
