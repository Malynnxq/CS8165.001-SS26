# Lecture 09 - Texturing Copy-Paste Prompts

## 09-00 - Whole Lecture Explanation And Resources

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
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

## 09-01 - Compact Rule Expansion

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus compact rule: sampled value = texture(sampler, uv), then shader interprets the value.

Task:
Expand the compact rule into a full explanation.
Define every symbol, word, stage, variable, or operation in simple English.
Give one numerical, geometric, or OpenGL-related example if the topic allows it.
Explain the common mistakes that happen when students memorize the rule without understanding it.
Create completion questions, ordering questions, and one small calculation or reasoning task.
Include the answer key.
If you have web access, find one human-written resource that explains the same rule or algorithm.
```

## 09-02 - Trap Repair

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus trap: Do not reduce texturing to pasting an image onto geometry.

Task:
Explain why this wrong idea sounds plausible.
Show the correct distinction with a small example.
Create a table with wrong statement, why it is tempting, corrected statement, and exam clue.
Create ten true-false-with-correction questions.
Include the answer key.
Keep the language simple enough for B1 English.
```

## 09-03 - Assignment Connection

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus assignment: Rendering contest and texture/shader tasks.

Task:
Connect the lecture topic to the assignment.
List the exact concepts the assignment probably tests.
Explain what source code, OpenGL state, buffer, shader, transformation, image result, or algorithmic step I should look for.
Create a checklist I can use while browsing assignment sources.
Create closed-format questions about the assignment connection.
Include the answer key.
Avoid asking me to write long open answers.
```

## 09-04 - Human-Written Resource Search

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
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

## 09-05 - Strict Closed-Format Examiner

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
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

## 09-S01 - Section: Texture Objects, Texels, Formats, and Color Space

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Texture Objects, Texels, Formats, and Color Space.
Source location: Section 9.1.
Section meaning: A texture is a GPU-accessible sampled data field..
Section check: Why can the same texture mechanism store both color maps and normal maps?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 09-S02 - Section: Texture Coordinates, UV Mapping, and Wrapping

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Texture Coordinates, UV Mapping, and Wrapping.
Source location: Section 9.2.
Section meaning: UVs are the address system that lets a fragment look up texture data..
Section check: What artifact might appear if a wrapping mode is wrong at the edge of a surface?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 09-S03 - Section: Sampling, Filtering, Mipmaps, and Anisotropy

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Sampling, Filtering, Mipmaps, and Anisotropy.
Source location: Section 9.3.
Section meaning: Filtering reconstructs values; mipmaps choose an appropriate scale before reconstruction..
Section check: Why does a distant checkerboard shimmer without mipmapping?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 09-S04 - Section: Modern OpenGL Texture Pipeline

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Modern OpenGL Texture Pipeline.
Source location: Section 9.4.
Section meaning: OpenGL texturing is a chain: object data -> texture unit -> sampler uniform -> shader lookup..
Section check: Why can a texture appear black when the shader code is mathematically correct?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 09-S05 - Section: Normal Mapping

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Normal Mapping.
Source location: Section 9.5.
Section meaning: Normal mapping changes the lighting normal, not the actual mesh silhouette..
Section check: Why does normal mapping not change the geometric outline of an object?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 09-S06 - Section: Environment Mapping and 3D Textures

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus section: Environment Mapping and 3D Textures.
Source location: Sections 9.6-9.7.
Section meaning: Textures are general sampled data; the coordinate dimensionality depends on the problem..
Section check: What coordinate type would you use to sample a 3D texture?.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
```

## 09-T01 - Term: texture

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: texture.
Course definition: Sampled data array used for color, normals, material data, depth, or other shader inputs.

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

## 09-T02 - Term: texel

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: texel.
Course definition: A stored sample in texture memory.

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

## 09-T03 - Term: UV coordinates

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: UV coordinates.
Course definition: Coordinates that map surface locations to texture space.

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

## 09-T04 - Term: filtering

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: filtering.
Course definition: Rule for reconstructing values between texels, such as nearest or linear filtering.

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

## 09-T05 - Term: mipmap

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: mipmap.
Course definition: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.

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

## 09-T06 - Term: environment mapping

```text
Course: CS8165.001 Interactive Computer Graphics.
Lecture: 09 - Texturing.
Source chunk: course_text_parts/03_lectures/09_texturing.txt.
Core idea: Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.
Process chain: fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning.
Important terms: texture: Sampled data array used for color, normals, material data, depth, or other shader inputs.; texel: A stored sample in texture memory.; UV coordinates: Coordinates that map surface locations to texture space.; filtering: Rule for reconstructing values between texels, such as nearest or linear filtering.; mipmap: Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling.; environment mapping: Using texture lookup to approximate surrounding reflections or distant lighting..
Compact rule: sampled value = texture(sampler, uv), then shader interprets the value.
Main trap: Do not reduce texturing to pasting an image onto geometry.
Assignment connection: Rendering contest and texture/shader tasks.
Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.
Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.
Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.

Focus term: environment mapping.
Course definition: Using texture lookup to approximate surrounding reflections or distant lighting.

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
