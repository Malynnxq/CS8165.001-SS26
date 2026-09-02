# Lecture 01 - Introduction Copy-Paste Prompts

## 01-00 - Whole Lecture Explanation And Resources

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
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

## 01-01 - Compact Rule Expansion

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.

Task:
Expand the compact rule into a full explanation.
Define every symbol, word, stage, variable, or operation in simple English.
Give one numerical, geometric, or OpenGL-related example if the topic allows it.
Explain the common mistakes that happen when students memorize the rule without understanding it.
Create completion questions, ordering questions, and one small calculation or reasoning task.
Include the answer key.
If you have web access, find one human-written resource that explains the same rule or algorithm.
```

## 01-02 - Trap Repair

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus trap: Do not confuse an image representation with the geometric cause of the image.

Task:
Explain why this wrong idea sounds plausible.
Show the correct distinction with a small example.
Create a table with wrong statement, why it is tempting, corrected statement, and exam clue.
Create ten true-false-with-correction questions.
Include the answer key.
Keep the language simple enough for B1 English.
```

## 01-03 - Assignment Connection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus assignment: 00 Introduction to C++.

Task:
Connect the lecture topic to the assignment.
List the exact concepts the assignment probably tests.
Explain what source code, OpenGL state, buffer, shader, transformation, image result, or algorithmic step I should look for.
Create a checklist I can use while browsing assignment sources.
Create closed-format questions about the assignment connection.
Include the answer key.
Avoid asking me to write long open answers.
```

## 01-04 - Human-Written Resource Search

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
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

## 01-05 - Strict Closed-Format Examiner

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
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

## 01-S01 - Section: Course Organization

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Course Organization.
Source location: Slides around 6-15.
Section meaning: Lecture slides give the vocabulary; exercises force you to connect that vocabulary to code and visible output..
Section check: Can you list the five exercise themes and connect each one to a later lecture chapter?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 01-S02 - Section: Computer Graphics Overview

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Computer Graphics Overview.
Source location: Section 1.2.
Section meaning: Graphics is controlled image generation. Interactive graphics is controlled image generation under a strict time budget..
Section check: What changes when a renderer must be interactive rather than offline?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 01-S03 - Section: Pixel-Based Representations

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Pixel-Based Representations.
Source location: Section 1.3.
Section meaning: A raster image is already the answer. It contains color samples, not the geometric reasons behind them..
Section check: Why can a pixel image be easy to display but hard to reinterpret as a 3D scene?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 01-S04 - Section: 3D Models

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: 3D Models.
Source location: Section 1.4.
Section meaning: A model is not an image. It is a cause from which many possible images can be generated..
Section check: Which model attributes can influence final color besides vertex positions?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 01-S05 - Section: Algorithmic Paradigms

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Algorithmic Paradigms.
Source location: Section 1.5.
Section meaning: Rasterization asks, 'Which samples does this primitive cover?' Ray casting asks, 'What does this sample see?'.
Section check: Which paradigm fits OpenGL's standard real-time pipeline most directly?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 01-T01 - Term: raster image

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: raster image.
Course definition: A grid of stored pixel samples; it is already an image, not a 3D scene.

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

## 01-T02 - Term: pixel

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: pixel.
Course definition: A discrete image sample containing color or channel values.

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

## 01-T03 - Term: color depth

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: color depth.
Course definition: The number of bits used to represent color values, controlling precision and memory size.

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

## 01-T04 - Term: 3D model

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: 3D model.
Course definition: A structured description of geometry and attributes that can generate many possible images.

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

## 01-T05 - Term: primitive

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: primitive.
Course definition: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.

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

## 01-T06 - Term: interactive graphics

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 01 - Introduction.
Source chunk: course_text_parts/03_lectures/01_introduction.txt.
Core idea: Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.
Process chain: scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis.
Important terms: raster image: A grid of stored pixel samples; it is already an image, not a 3D scene.; pixel: A discrete image sample containing color or channel values.; color depth: The number of bits used to represent color values, controlling precision and memory size.; 3D model: A structured description of geometry and attributes that can generate many possible images.; primitive: A basic geometric object such as a point, line, or triangle used by the rendering pipeline.; interactive graphics: Rendering where images must update quickly enough to respond to input or animation..
Compact rule: image memory = width x height x bits per pixel, then divide by 8 for bytes.
Main trap: Do not confuse an image representation with the geometric cause of the image.
Assignment connection: 00 Introduction to C++.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: interactive graphics.
Course definition: Rendering where images must update quickly enough to respond to input or animation.

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
