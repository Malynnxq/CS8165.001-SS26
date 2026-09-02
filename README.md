# CS8165.001 SS26 - Interactive Computer Graphics

Private backup of the Moodle course export `CS8165.001-SS26_1787682614.zip`.

## Structure

- `START_HERE_100_PERCENT.md` - central reading-first route from raw Moodle material to exam-ready practice
- `index.html` - course overview from Moodle
- `lectures/` - lecture pages and renamed slide PDFs
- `assignments/` - exercise pages
- `assignment_zips/` - original downloaded ZIP packages for Exercises 1-4
- `assignment_sources/` - extracted contents of the Exercise 1-4 ZIPs for direct GitHub browsing
- `forums/` - exported forum pages
- `course/` - course administration pages such as group selection
- `examples/` - downloadable starter projects and sample files
- `assets/` - shared Moodle styling
- `course_full_text.txt` - complete structured text export for AI-assisted exam preparation, including extracted slide text, page metadata, formula/notation candidates, a chapter index, exercise index, visual slide inventory, and starter-code contents
- `course_text_parts/` - split text export for AI workflows
- `study_pack/` - exam-preparation pack with chapter guides, formula checklist, visual review guide, exam drill, Anki TSV, study plan, and reusable AI prompts
- `practice_pack/` - interactive practice pack with cloze texts, matching tables, MC questions, sequencing tasks, math/algorithm drills, diagram prompts, OpenGL drills, and a roadmap from 0 to exam-ready
- `exam_materials/` - generated reading-first exam material pack with standalone copy-paste prompts, B1 bridge chapters, plain prose chapters, structured exam chapters, checklists, cloze inputs, matching TSV, closed-format drills, assignment workbook, and final mixed exam
- `practice_pack/repetition_variants/` - repeated practice rounds with the same concepts but different wording and task layouts
- `overprep_pack/` - closed-format overpreparation pack with MC/mock exams, mistake log, concept-confusion pairs, diagram label workbook, OpenGL debugging drills, one-pagers, spaced repetition, and final readiness checklist
- `reader_pack/` - readable original-language narrative reader, PDF, clickable workbook, and language audit
- `lecture_readers/` - readable commented version for each individual lecture, with one PDF per lecture and one combined PDF

## Language Policy

- Raw extracted course material keeps its original exported language.
- The lecture/course content is primarily English, so `reader_pack/` is written in English.
- German Moodle interface text or notices remain German only when they are original source text.
- Some older helper files contain German study instructions because they were generated from German user requests. For original-language AI input, start with `reader_pack/narrative_reader.md` and the matching source chunks in `course_text_parts/03_lectures/`.
- For human-readable lecture study, start with `lecture_readers/pdf/CS8165_complete_lecture_readers.pdf` or the individual files in `lecture_readers/markdown/`.

## AI Study Files

Reading files by context size:

- `course_text_parts/00_START_HERE.txt` - loading guide and source manifest
- `course_text_parts/03_lectures/` - one text file per lecture chapter
- `course_text_parts/04_assignments/` - one text file per exercise
- `course_text_parts/06_exam_preparation_addendum.txt` - chapter index, formula/notation candidates, visual slide inventory, and AI prompts
- `course_text_parts/98_size_limited_full_text_slices/` - sequential slices under 75 KB each; together they exactly reconstruct `course_full_text.txt`
- `course_text_parts/INDEX.txt` - list of all generated text chunks

## Exam Study Pack

Reading order:

- `exam_materials/README.md`
- `exam_materials/copy_paste_prompts/README.md`
- `exam_materials/chapters_bridge/CS8165_all_b1_bridge_chapters.md`
- `exam_materials/chapters_plain/CS8165_all_plain_text_chapters.txt`
- `exam_materials/chapters/CS8165_all_exam_chapters.md`
- `reader_pack/README.md`
- `reader_pack/narrative_reader.md`
- `reader_pack/original_language_ai_bundle.txt`
- `reader_pack/icg_narrative_reader.pdf`
- `reader_pack/interactive_workbook.html`
- `reader_pack/language_audit.md`
- `lecture_readers/README.md`
- `lecture_readers/pdf/CS8165_complete_lecture_readers.pdf`
- `lecture_readers/markdown/`
- `study_pack/README.md`
- `study_pack/ai_prompts.md`
- `study_pack/chapter_guides/`
- `study_pack/exam_drill.md`
- `study_pack/flashcards_anki.tsv`
- `study_pack/visual_review_guide.md`

## Interactive Practice Pack

Active learning and copy-paste generators:

- `practice_pack/cloze_source_texts.md` - coherent source texts for cloze generators
- `practice_pack/premade_cloze_texts.md` - same topics with blanks already inserted
- `practice_pack/matching_pairs.tsv` - importable term/definition/chapter table
- `practice_pack/matching_tasks.md` - manual matching grouped by chapter
- `practice_pack/multiple_choice.md` - MC questions with answers
- `practice_pack/sequencing_tasks.md` - order-the-steps tasks
- `practice_pack/math_algorithm_drills.md` - math and algorithm explanation drills
- `practice_pack/diagram_graphics_prompts.md` - drawing and visual explanation tasks
- `practice_pack/opengl_software_drills.md` - OpenGL/software understanding checks
- `practice_pack/interactive_practice_menu.md` - daily active-recall loop
- `practice_pack/repetition_variants/` - 3 rounds of repeated cloze, matching, MC, and sequencing variants
- `practice_pack/roadmap_0_to_100.md` - full route from zero to exam-ready

## Roadmap From 0 To Exam-Ready

1. **B1 Bridge First:** Read `exam_materials/chapters_bridge/CS8165_all_b1_bridge_chapters.md`, or read the matching single file in `exam_materials/chapters_bridge/` before each lecture. This connects everyday knowledge to graphics concepts and explains important verbs, collocations, and technical terms.
2. **Plain Reading:** Read `exam_materials/chapters_plain/CS8165_all_plain_text_chapters.txt`, or the matching single file in `exam_materials/chapters_plain/`. This gives you smooth English prose without Markdown, formulas, arrows, or code-like notation.
3. **Structured Exam Chapter:** Read the matching file in `exam_materials/chapters/`. This is the precision layer with problem, chain, terminology, compact rules, assignment connection, exam traps, answer criteria, and closed self-tests.
4. **Copy-Paste Prompt Work:** Open `exam_materials/copy_paste_prompts/README.md`, then work through the matching lecture prompt file. Each prompt is self-contained and can be copied into a separate AI chat.
5. **Slide-Level Detail:** Read `lecture_readers/pdf/CS8165_complete_lecture_readers.pdf` or the individual files in `lecture_readers/markdown/` when you need professor-style slide-by-slide explanation.
6. **Raw Lecture Text:** Read the matching original text chunk in `course_text_parts/03_lectures/` after the easier versions, so the original wording becomes less intimidating.
7. **Assignment Reading:** Read the matching assignment in `course_text_parts/04_assignments/`, then browse `assignment_sources/` and `assignment_zips/` where available.
8. **Checklist Gate:** Read and use `exam_materials/01_mastery_checklists.md`. Do not move on from a lecture until you can identify the topic, its pipeline role, its main terms, and its common trap.
9. **Cloze Practice:** Copy passages from `exam_materials/02_cloze_generator_inputs.md` or `practice_pack/cloze_source_texts.md` into a cloze generator.
10. **Matching Practice:** Use `exam_materials/03_matching_pairs.tsv`, `exam_materials/03_matching_tasks.md`, and `practice_pack/matching_pairs.tsv` to drill terms, definitions, chapters, and roles.
11. **Ordering Practice:** Use `exam_materials/05_sequencing_and_pipeline_tasks.md` and `practice_pack/sequencing_tasks.md` to learn process order, especially for pipeline, projection, clipping, rasterization, and visibility.
12. **Closed-Format Drills:** Use `exam_materials/04_closed_format_drills.md`, `practice_pack/multiple_choice.md`, and `overprep_pack/mock_exams/`. Prefer multiple choice, matching, completion, ordering, labeling, and debugging tasks over broad open essays.
13. **Math, Algorithms, And Diagrams:** Use `study_pack/formulas_and_derivations.md`, `practice_pack/math_algorithm_drills.md`, `exam_materials/06_diagram_label_tasks.md`, and `practice_pack/diagram_graphics_prompts.md`.
14. **OpenGL And Software:** Use `exam_materials/07_opengl_debugging_drills.md`, `practice_pack/opengl_software_drills.md`, `course_text_parts/05_opengl_starter_project.txt`, and the software labs in `reader_pack/interactive_workbook.html`.
15. **Non-Boring Repetition:** Use `practice_pack/repetition_variants/round_01`, then `round_02`, then `round_03`. These repeat the same concepts with changed wording and different task forms.
16. **Mistake Repair:** Log every wrong answer in `overprep_pack/mistake_log.md`, then turn it into repair work with `exam_materials/10_mistake_log_repair_drills.md`.
17. **Final Simulation:** Use `exam_materials/09_final_mixed_closed_exam.md`, `study_pack/exam_drill.md`, and the mock exams in `overprep_pack/mock_exams/`.
18. **Final Pass:** Use `overprep_pack/final_readiness_checklist.md`. Revisit every weak spot until you can recognize the concept under new wording, choose the correct closed-format answer, and explain the corrected distinction in simple English.

## Closed-Format Overprep

- `overprep_pack/mock_exams/` - 3 closed-format mock exams
- `overprep_pack/mistake_log.md` - structured error tracking
- `overprep_pack/closed_format_oral_exam_mode.md` - AI examiner prompt that avoids broad essay questions
- `overprep_pack/concept_confusion_pairs.md` - clipping vs culling, fragment vs pixel, etc.
- `overprep_pack/diagram_label_workbook.md` - drawing tasks as label checklists
- `overprep_pack/code_reading_debugging_drills.md` - OpenGL/software debugging MC
- `overprep_pack/one_pager_cheat_sheets.md` - chapter one-pagers
- `overprep_pack/spaced_repetition_schedule.md`
- `overprep_pack/final_readiness_checklist.md`

## Lecture Slides

- `lectures/01-introduction/slides/01-introduction.pdf`
- `lectures/02-rendering-pipeline/slides/02-rendering-pipeline.pdf`
- `lectures/03-geometric-transformations/slides/03-geometric-transformations.pdf`
- `lectures/04-geometric-projection/slides/04-geometric-projection.pdf`
- `lectures/05-clipping/slides/05-clipping.pdf`
- `lectures/06-rasterization/slides/06-rasterization.pdf`
- `lectures/07-visibility-determination/slides/07-visibility-determination.pdf`
- `lectures/08-local-illumination/slides/08-local-illumination.pdf`
- `lectures/09-texturing/slides/09-texturing.pdf`
- `lectures/10-shadows/slides/10-shadows.pdf`

Keep this repository private unless you have permission to publish the course materials.
