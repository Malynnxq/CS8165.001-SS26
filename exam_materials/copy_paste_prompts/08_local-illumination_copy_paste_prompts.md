# Lecture 08 - Local Illumination Copy-Paste Prompts

## 08-00 - Whole Lecture Explanation And Resources

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
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

## 08-01 - Compact Rule Expansion

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus compact rule: color = ambient + diffuse + specular.

Task:
Expand the compact rule into a full explanation.
Define every symbol, word, stage, variable, or operation in simple English.
Give one numerical, geometric, or OpenGL-related example if the topic allows it.
Explain the common mistakes that happen when students memorize the rule without understanding it.
Create completion questions, ordering questions, and one small calculation or reasoning task.
Include the answer key.
If you have web access, find one human-written resource that explains the same rule or algorithm.
```

## 08-02 - Trap Repair

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.

Task:
Explain why this wrong idea sounds plausible.
Show the correct distinction with a small example.
Create a table with wrong statement, why it is tempting, corrected statement, and exam clue.
Create ten true-false-with-correction questions.
Include the answer key.
Keep the language simple enough for B1 English.
```

## 08-03 - Assignment Connection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus assignment: Rendering contest and shader-related tasks.

Task:
Connect the lecture topic to the assignment.
List the exact concepts the assignment probably tests.
Explain what source code, OpenGL state, buffer, shader, transformation, image result, or algorithmic step I should look for.
Create a checklist I can use while browsing assignment sources.
Create closed-format questions about the assignment connection.
Include the answer key.
Avoid asking me to write long open answers.
```

## 08-04 - Human-Written Resource Search

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
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

## 08-05 - Strict Closed-Format Examiner

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
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

## 08-S01 - Section: Physics of Light

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Physics of Light.
Source location: Section 8.1.
Section meaning: Shading is an approximation of light-surface interaction that is cheap enough for rendering..
Section check: Why does surface orientation affect diffuse brightness?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 08-S02 - Section: Light Sources

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Light Sources.
Source location: Section 8.2.
Section meaning: Different light types mainly change how the light direction and intensity are computed at the surface point..
Section check: What is the difference between a directional light vector and a point light vector?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 08-S03 - Section: Material Models

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Material Models.
Source location: Section 8.3.
Section meaning: Light asks what arrives; material answers how the surface reacts..
Section check: Which material parameter would you adjust to reduce shiny highlights?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 08-S04 - Section: Phong Illumination Model

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Phong Illumination Model.
Source location: Section 8.4.
Section meaning: Phong-style lighting is a sum of simple terms, each modeling a different visual effect..
Section check: Why does the specular term depend on the view direction?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 08-S05 - Section: Shading

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Shading.
Source location: Section 8.5.
Section meaning: The shading method decides what is computed at vertices and what is computed at fragments..
Section check: Why can Gouraud shading miss a small specular highlight?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 08-T01 - Term: surface normal

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: surface normal.
Course definition: Vector describing surface orientation and controlling diffuse/specular response.

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

## 08-T02 - Term: ambient term

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: ambient term.
Course definition: Approximate base illumination independent of direct light direction.

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

## 08-T03 - Term: diffuse reflection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: diffuse reflection.
Course definition: View-independent light response based on the angle between normal and light direction.

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

## 08-T04 - Term: specular reflection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: specular reflection.
Course definition: View-dependent highlight term based on reflection or half-vector alignment.

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

## 08-T05 - Term: Phong model

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: Phong model.
Course definition: Local illumination model combining ambient, diffuse, and specular components.

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

## 08-T06 - Term: material coefficient

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 08 - Local Illumination.
Source chunk: course_text_parts/03_lectures/08_local-illumination.txt.
Core idea: Local illumination computes color from surface orientation, light direction, view direction, and material response.
Process chain: surface point + normal + light + view + material -> lighting equation -> shaded color.
Important terms: surface normal: Vector describing surface orientation and controlling diffuse/specular response.; ambient term: Approximate base illumination independent of direct light direction.; diffuse reflection: View-independent light response based on the angle between normal and light direction.; specular reflection: View-dependent highlight term based on reflection or half-vector alignment.; Phong model: Local illumination model combining ambient, diffuse, and specular components.; material coefficient: Parameter controlling how strongly a surface responds to lighting terms..
Compact rule: color = ambient + diffuse + specular.
Main trap: Do not mix up normal, light direction, and view direction; each changes a different lighting term.
Assignment connection: Rendering contest and shader-related tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: material coefficient.
Course definition: Parameter controlling how strongly a surface responds to lighting terms.

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
