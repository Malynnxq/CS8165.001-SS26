# Start Here - Reading-First 100 Percent Exam System

This is the central route through the repository if you were not in the lectures, like reading, and want to prepare as close to 100 percent as possible.

No method can guarantee 100 percent. The system below is designed to remove known gaps: missing lecture commentary, weak links between topics, ignored exercises, passive reading, and practice that is too easy.

## What This Repository Already Gives You

- A readable lecture book: `lecture_readers/pdf/CS8165_complete_lecture_readers.pdf`
- Individual readable lecture chapters: `lecture_readers/markdown/`
- A shorter narrative overview: `reader_pack/narrative_reader.md`
- Raw source chunks for AI input: `course_text_parts/`
- Assignment pages as text: `course_text_parts/04_assignments/`
- Original exercise ZIPs: `assignment_zips/`
- Extracted exercise source code and PDFs: `assignment_sources/`
- Cloze source texts: `practice_pack/cloze_source_texts.md`
- Matching data: `practice_pack/matching_pairs.tsv`
- Multiple-choice and sequencing practice: `practice_pack/multiple_choice.md`, `practice_pack/sequencing_tasks.md`
- Math, graphics, and OpenGL drills: `practice_pack/math_algorithm_drills.md`, `practice_pack/opengl_software_drills.md`
- Closed-format mock exams: `overprep_pack/mock_exams/`
- Mistake tracking: `overprep_pack/mistake_log.md`

## The Main Rule

Do not learn slide bullets as isolated facts.

For every topic, force this chain:

`Problem -> data/object -> operation/algorithm -> output -> next pipeline stage -> typical mistake -> assignment connection`

If you cannot fill that chain, the topic is not finished.

## Phase 0 - Confirm The Material Is Complete

Open these first:

1. `course_build_audit.json`
2. `course_text_parts/00_START_HERE.txt`
3. `README.md`
4. `assignment_zips/README.md`
5. `assignment_sources/README.md`

Goal of this phase:

- Confirm that the repository has lectures, assignments, extracted text, practice files, and original exercise packages.
- Notice the only known assignment ZIP gap: `Exercise5.zip` was not found in Downloads during the previous local search. The exercise text for rasterization still exists in `course_text_parts/04_assignments/05_rasterization.txt`.

## Phase 1 - Read Like A Book, Not Like Slides

Start with:

1. `lecture_readers/pdf/CS8165_complete_lecture_readers.pdf`
2. If the PDF feels too long, use one chapter at a time from `lecture_readers/markdown/`
3. Use `reader_pack/narrative_reader.md` only as the shorter companion overview

For each lecture, read in this order:

1. Big Picture
2. Per-Slide Commentary
3. Professor-style explanation
4. Exam-grade answer
5. Common trap
6. Check yourself

Do not skip the per-slide sections. They replace the missing spoken lecture commentary.

## Phase 2 - Reconnect The Raw Slides

After reading a lecture chapter, open the matching raw extracted lecture text in `course_text_parts/03_lectures/`.

Your task is to verify:

- Every important word from the slide appears in your understanding.
- The readable chapter did not make you forget the original wording.
- You can explain why the slide items are grouped together.

Use this test:

`Can I explain the slide without reading the slide aloud?`

If the answer is no, reread the slide's Professor-style explanation and Common trap.

## Phase 3 - Attach Every Lecture To Exercises

Use `study_pack/exercise_concept_map.md` as the bridge between theory and assignments.

Then inspect:

- Assignment text: `course_text_parts/04_assignments/`
- Original ZIP packages: `assignment_zips/`
- Extracted code and PDFs: `assignment_sources/`

The exercise workflow is:

1. Read the assignment text.
2. Identify the lecture concepts required.
3. Open the extracted assignment PDF or source code.
4. Predict what knowledge the exercise tests.
5. Try the task without looking for a solution.
6. Log every missing concept in `overprep_pack/mistake_log.md`.

The important question is not "Did I finish the exercise?".

The important question is:

`Which exact concept did I fail to recognize or apply?`

## Phase 4 - Feed Your Text Tools In The Right Order

Use your cloze generator only after you have read the explanatory chapters.

Best source files for copy-paste tools:

- Cloze generator: `practice_pack/cloze_source_texts.md`
- Premade blanks: `practice_pack/premade_cloze_texts.md`
- Matching generator: `practice_pack/matching_pairs.tsv`
- MC practice: `practice_pack/multiple_choice.md`
- Ordering tasks: `practice_pack/sequencing_tasks.md`
- Formula and algorithm drills: `practice_pack/math_algorithm_drills.md`
- Diagram prompts: `practice_pack/diagram_graphics_prompts.md`
- OpenGL/software checks: `practice_pack/opengl_software_drills.md`

Recommended order:

1. Cloze for vocabulary and formulas.
2. Matching for definition-to-concept recognition.
3. Sequencing for pipeline and algorithm order.
4. MC for fast closed-format decision making.
5. Diagram labeling for visual understanding.
6. OpenGL debugging drills for applied software knowledge.

Do not use cloze as your main proof of competence. Cloze checks recognition. Exams often require transfer.

## Phase 5 - Repeat Without Getting Bored

Use the repetition variants:

1. `practice_pack/repetition_variants/round_01`
2. `practice_pack/repetition_variants/round_02`
3. `practice_pack/repetition_variants/round_03`

These repeat the same concepts with changed wording and changed task surfaces. This matters because a single familiar wording can create false confidence.

Rule:

If you only know the answer when the sentence looks familiar, you have memorized phrasing, not the concept.

## Phase 6 - Move From Reading To Closed-Format Exam Work

Because you dislike vague open mock-exam answers, use the closed-format material first:

- `overprep_pack/mock_exams/`
- `overprep_pack/closed_format_oral_exam_mode.md`
- `overprep_pack/concept_confusion_pairs.md`
- `overprep_pack/diagram_label_workbook.md`
- `overprep_pack/code_reading_debugging_drills.md`

Preferred task types:

- Select the correct statement.
- Match term and definition.
- Fill a missing word, number, formula component, or pipeline stage.
- Put steps in order.
- Label a diagram.
- Choose which OpenGL state or buffer causes a bug.
- Identify the wrong statement and correct it.

Only after this should you do broader open explanation tasks.

## Phase 7 - The Mistake Log Is Your Main Weapon

Every wrong answer goes into `overprep_pack/mistake_log.md`.

Each entry must say:

- Source file
- Task type
- Topic
- Wrong answer
- Correct answer
- Why you missed it
- Fix rule
- Review dates

Good mistake:

`I confused fragment with pixel because I forgot that fragments are only candidates before depth/stencil/blending/framebuffer operations.`

Bad mistake:

`I did not understand rasterization.`

The first one can be repaired. The second one is too vague.

## Phase 8 - Final Readiness Test

Use `overprep_pack/final_readiness_checklist.md`.

A topic is exam-ready only if you can do all of this without notes:

- Define the concept.
- Explain why it exists.
- Name its input data.
- Name its output data.
- Place it in the rendering pipeline.
- Connect it to at least one assignment or OpenGL/software detail.
- Solve a closed-format question about it.
- Explain a typical mistake.
- Recognize the concept under different wording.

## Daily Study Loop

Use this loop for one lecture or topic block:

1. Read the relevant `lecture_readers` chapter.
2. Verify with the raw source chunk.
3. Open the matching assignment text/source.
4. Do cloze or matching for basic recall.
5. Do sequencing, MC, diagram, math, or OpenGL drills.
6. Add errors to the mistake log.
7. Review previous mistake-log entries.
8. Stop only when the checklist says the topic is ready.

## Best File Order From Zero To Exam-Ready

1. `START_HERE_100_PERCENT.md`
2. `course_build_audit.json`
3. `lecture_readers/pdf/CS8165_complete_lecture_readers.pdf`
4. `lecture_readers/markdown/01_introduction_reader.md`
5. Continue through `lecture_readers/markdown/10_shadows_reader.md`
6. `study_pack/exercise_concept_map.md`
7. `course_text_parts/04_assignments/`
8. `assignment_sources/`
9. `practice_pack/cloze_source_texts.md`
10. `practice_pack/matching_pairs.tsv`
11. `practice_pack/sequencing_tasks.md`
12. `practice_pack/multiple_choice.md`
13. `practice_pack/math_algorithm_drills.md`
14. `practice_pack/opengl_software_drills.md`
15. `practice_pack/repetition_variants/`
16. `overprep_pack/mock_exams/`
17. `overprep_pack/mistake_log.md`
18. `overprep_pack/final_readiness_checklist.md`

## What To Ask AI With This Repository

Use prompts like these:

```text
Use only the attached course text and assignment text unless you clearly mark outside knowledge.
Transform this lecture into an exam-oriented explanation.
Keep every course term.
Explain the missing links between slide bullets.
Create closed-format tasks: MC, matching, cloze, sequencing, diagram labeling, and debugging.
After each answer, state which source chunk supports it.
```

```text
Here is my mistake log.
Group the mistakes by concept.
Tell me which lecture sections and assignments I must revisit.
Generate closed-format repair drills for only those weak spots.
```

```text
Take this assignment source and identify the exact lecture concepts required.
Create a checklist of knowledge needed before attempting it.
Create MC, matching, and code-reading questions that test those concepts.
```

## End Condition

You are not done when the text feels understandable.

You are done when you can handle a new task under exam conditions:

- unfamiliar wording
- no chapter hint
- no notes
- mixed topics
- time pressure
- closed-format traps

That is the difference between "I read the course" and "I can score very high on the exam".
