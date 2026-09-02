# Lecture 10 - Shadows Copy-Paste Prompts

## 10-00 - Whole Lecture Explanation And Resources

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
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

## 10-01 - Compact Rule Expansion

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus compact rule: point is shadowed if something is closer to the light along the same light ray.

Task:
Expand the compact rule into a full explanation.
Define every symbol, word, stage, variable, or operation in simple English.
Give one numerical, geometric, or OpenGL-related example if the topic allows it.
Explain the common mistakes that happen when students memorize the rule without understanding it.
Create completion questions, ordering questions, and one small calculation or reasoning task.
Include the answer key.
If you have web access, find one human-written resource that explains the same rule or algorithm.
```

## 10-02 - Trap Repair

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.

Task:
Explain why this wrong idea sounds plausible.
Show the correct distinction with a small example.
Create a table with wrong statement, why it is tempting, corrected statement, and exam clue.
Create ten true-false-with-correction questions.
Include the answer key.
Keep the language simple enough for B1 English.
```

## 10-03 - Assignment Connection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus assignment: Rendering contest and integrated lighting tasks.

Task:
Connect the lecture topic to the assignment.
List the exact concepts the assignment probably tests.
Explain what source code, OpenGL state, buffer, shader, transformation, image result, or algorithmic step I should look for.
Create a checklist I can use while browsing assignment sources.
Create closed-format questions about the assignment connection.
Include the answer key.
Avoid asking me to write long open answers.
```

## 10-04 - Human-Written Resource Search

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
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

## 10-05 - Strict Closed-Format Examiner

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
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

## 10-S01 - Section: Definitions

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Definitions.
Source location: Section 10.1.
Section meaning: Shadows are light-space visibility made visible in the camera image..
Section check: Why is shadow computation related to visibility determination?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 10-S02 - Section: Ground Plane Shadows

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Ground Plane Shadows.
Source location: Section 10.2.
Section meaning: A planar shadow is projected geometry on a known receiver..
Section check: What scene limitation makes ground plane shadows less general than shadow maps?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 10-S03 - Section: Light Maps

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Light Maps.
Source location: Section 10.3.
Section meaning: A light map spends storage and preprocessing to save runtime shading work..
Section check: Why are light maps less suitable for fully dynamic moving lights?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 10-S04 - Section: Shadow Volumes

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Shadow Volumes.
Source location: Section 10.4.
Section meaning: A shadow volume is the 3D region where the light cannot reach..
Section check: Why are silhouette edges important for constructing shadow volumes?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 10-S05 - Section: Shadow Maps

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Shadow Maps.
Source location: Section 10.5.
Section meaning: Shadow maps reuse the depth-buffer idea, but from the light's camera..
Section check: What exactly is stored in a shadow map?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 10-T01 - Term: shadow

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: shadow.
Course definition: Reduced direct illumination where an object blocks light from reaching a receiver.

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

## 10-T02 - Term: occluder

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: occluder.
Course definition: Object that blocks light.

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

## 10-T03 - Term: receiver

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: receiver.
Course definition: Surface where the shadow appears.

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

## 10-T04 - Term: shadow map

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: shadow map.
Course definition: Depth image rendered from the light's point of view for later visibility comparison.

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

## 10-T05 - Term: shadow volume

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: shadow volume.
Course definition: Volume of space hidden from a light by an occluder.

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

## 10-T06 - Term: projective shadow

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 10 - Shadows.
Source chunk: course_text_parts/03_lectures/10_shadows.txt.
Core idea: Shadows are visibility tests from the light source, not only dark shapes seen by the camera.
Process chain: light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result.
Important terms: shadow: Reduced direct illumination where an object blocks light from reaching a receiver.; occluder: Object that blocks light.; receiver: Surface where the shadow appears.; shadow map: Depth image rendered from the light's point of view for later visibility comparison.; shadow volume: Volume of space hidden from a light by an occluder.; projective shadow: Shadow construction based on projecting geometry onto a receiver..
Compact rule: point is shadowed if something is closer to the light along the same light ray.
Main trap: Do not explain a shadow only from the camera view; the key test is light-space visibility.
Assignment connection: Rendering contest and integrated lighting tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: projective shadow.
Course definition: Shadow construction based on projecting geometry onto a receiver.

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
