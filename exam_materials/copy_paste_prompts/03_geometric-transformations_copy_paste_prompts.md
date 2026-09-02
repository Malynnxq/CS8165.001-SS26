# Lecture 03 - Geometric Transformations Copy-Paste Prompts

## 03-00 - Whole Lecture Explanation And Resources

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
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

## 03-01 - Compact Rule Expansion

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus compact rule: p_world = M_model * p_model; p_view = V * p_world.

Task:
Expand the compact rule into a full explanation.
Define every symbol, word, stage, variable, or operation in simple English.
Give one numerical, geometric, or OpenGL-related example if the topic allows it.
Explain the common mistakes that happen when students memorize the rule without understanding it.
Create completion questions, ordering questions, and one small calculation or reasoning task.
Include the answer key.
If you have web access, find one human-written resource that explains the same rule or algorithm.
```

## 03-02 - Trap Repair

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus trap: Do not multiply matrices without naming source space, target space, and order.

Task:
Explain why this wrong idea sounds plausible.
Show the correct distinction with a small example.
Create a table with wrong statement, why it is tempting, corrected statement, and exam clue.
Create ten true-false-with-correction questions.
Include the answer key.
Keep the language simple enough for B1 English.
```

## 03-03 - Assignment Connection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus assignment: 03 Geometric Transformations.

Task:
Connect the lecture topic to the assignment.
List the exact concepts the assignment probably tests.
Explain what source code, OpenGL state, buffer, shader, transformation, image result, or algorithmic step I should look for.
Create a checklist I can use while browsing assignment sources.
Create closed-format questions about the assignment connection.
Include the answer key.
Avoid asking me to write long open answers.
```

## 03-04 - Human-Written Resource Search

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
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

## 03-05 - Strict Closed-Format Examiner

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
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

## 03-S01 - Section: Mathematical Foundations

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Mathematical Foundations.
Source location: Section 3.1.
Section meaning: A numeric vector is incomplete until you know what coordinate system it belongs to..
Section check: Why is a normal vector not transformed exactly like a point under all transformations?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 03-S02 - Section: Affine Transformations

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Affine Transformations.
Source location: Section 3.2.
Section meaning: Use 4D homogeneous coordinates so that a single matrix pipeline can move 3D points through the scene..
Section check: What does the homogeneous w component let a transformation matrix express?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 03-S03 - Section: Composition of Transformations

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Composition of Transformations.
Source location: Section 3.3.
Section meaning: Matrix chains are compressed stories of movement through coordinate spaces..
Section check: Why can swapping model and view matrices destroy the intended camera/object relation?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 03-S04 - Section: Coordinate System Change

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Coordinate System Change.
Source location: Section 3.4.
Section meaning: Moving the camera one way is equivalent to moving the world the opposite way for rendering..
Section check: Why is the view transform often related to the inverse camera transform?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 03-S05 - Section: Transformations in OpenGL

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Transformations in OpenGL.
Source location: Section 3.5.
Section meaning: The shader is the place where abstract transformation math becomes GPU execution..
Section check: Which matrix would you inspect first if an object follows the camera instead of staying in the world?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 03-T01 - Term: homogeneous coordinates

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: homogeneous coordinates.
Course definition: Coordinates with an additional component that make translation and projection expressible by matrices.

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

## 03-T02 - Term: translation

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: translation.
Course definition: A transformation that moves points by an offset; direction vectors are not shifted the same way.

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

## 03-T03 - Term: rotation

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: rotation.
Course definition: A transformation that changes orientation while preserving distances.

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

## 03-T04 - Term: scaling

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: scaling.
Course definition: A transformation that changes size and can distort normals if handled incorrectly.

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

## 03-T05 - Term: matrix composition

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: matrix composition.
Course definition: Combining transformations by multiplication, where order matters.

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

## 03-T06 - Term: normal transformation

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 03 - Geometric Transformations.
Source chunk: course_text_parts/03_lectures/03_geometric-transformations.txt.
Core idea: Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.
Process chain: object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates.
Important terms: homogeneous coordinates: Coordinates with an additional component that make translation and projection expressible by matrices.; translation: A transformation that moves points by an offset; direction vectors are not shifted the same way.; rotation: A transformation that changes orientation while preserving distances.; scaling: A transformation that changes size and can distort normals if handled incorrectly.; matrix composition: Combining transformations by multiplication, where order matters.; normal transformation: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling..
Compact rule: p_world = M_model * p_model; p_view = V * p_world.
Main trap: Do not multiply matrices without naming source space, target space, and order.
Assignment connection: 03 Geometric Transformations.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: normal transformation.
Course definition: Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling.

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
