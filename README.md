# CS8165.001 SS26 - Interactive Computer Graphics

Private backup of the Moodle course export `CS8165.001-SS26_1787682614.zip`.

## Structure

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
- `course_build_audit.json` - machine-readable coverage report for source files, PDF pages, chunks, and validation checks
- `study_pack/` - exam-preparation pack with chapter guides, formula checklist, visual review guide, exam drill, Anki TSV, study plan, and reusable AI prompts
- `practice_pack/` - interactive practice pack with cloze texts, matching tables, MC questions, sequencing tasks, math/algorithm drills, diagram prompts, OpenGL drills, and a roadmap from 0 to exam-ready
- `practice_pack/repetition_variants/` - repeated practice rounds with the same concepts but different wording and task layouts
- `overprep_pack/` - closed-format overpreparation pack with MC/mock exams, mistake log, concept-confusion pairs, diagram label workbook, OpenGL debugging drills, one-pagers, spaced repetition, and final readiness checklist
- `reader_pack/` - readable original-language narrative reader, PDF, clickable workbook, and language audit
- `lecture_readers/` - readable commented version for each individual lecture, with one PDF per lecture and one combined PDF
- `scripts/build_course_text.py` - reproducible exporter for rebuilding `course_full_text.txt`
- `scripts/build_study_pack.py` - reproducible generator for rebuilding `study_pack/`
- `scripts/build_practice_pack.py` - reproducible generator for rebuilding `practice_pack/`
- `scripts/build_overprep_pack.py` - reproducible generator for rebuilding `overprep_pack/`
- `scripts/build_reader_pack.py` - reproducible generator for rebuilding `reader_pack/`
- `scripts/build_lecture_readers.py` - reproducible generator for rebuilding `lecture_readers/`

## Language Policy

- Raw extracted course material keeps its original exported language.
- The lecture/course content is primarily English, so `reader_pack/` is written in English.
- German Moodle interface text or notices remain German only when they are original source text.
- Some older helper files contain German study instructions because they were generated from German user requests. For original-language AI input, start with `reader_pack/narrative_reader.md` and the matching source chunks in `course_text_parts/03_lectures/`.
- For human-readable lecture study, start with `lecture_readers/pdf/CS8165_complete_lecture_readers.pdf` or the individual files in `lecture_readers/markdown/`.

## AI Study Files

Use these files depending on the context window:

- `course_text_parts/00_START_HERE.txt` - loading guide and source manifest
- `course_text_parts/03_lectures/` - one text file per lecture chapter
- `course_text_parts/04_assignments/` - one text file per exercise
- `course_text_parts/06_exam_preparation_addendum.txt` - chapter index, formula/notation candidates, visual slide inventory, and AI prompts
- `course_text_parts/98_size_limited_full_text_slices/` - sequential slices under 75 KB each; together they exactly reconstruct `course_full_text.txt`
- `course_text_parts/INDEX.txt` - list of all generated text chunks

Coverage checks are stored in `course_build_audit.json`.

## Exam Study Pack

Start here:

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

The study pack is derived from the course chunks and does not invent missing old exams, recordings, or official solutions.

## Interactive Practice Pack

Use these for active learning and copy-paste generators:

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

1. **Setup:** Open `course_build_audit.json` and confirm all checks are `true`.
2. **Readable Start:** Read `lecture_readers/pdf/CS8165_complete_lecture_readers.pdf` or the individual lecture PDFs.
3. **Chapter Companion:** Use `reader_pack/narrative_reader.md` as the shorter overview and `reader_pack/interactive_workbook.html` for clickable checks.
4. **Orientation:** Read `course_text_parts/00_START_HERE.txt`, then `study_pack/README.md`.
5. **Core Understanding:** Work through `lecture_readers/markdown/` and `study_pack/chapter_guides/` from chapter 01 to 10.
6. **Raw Source Check:** For each lecture, load the matching file from `course_text_parts/03_lectures/`.
7. **Active Recall:** Use `practice_pack/cloze_source_texts.md`, `practice_pack/matching_pairs.tsv`, and `study_pack/flashcards_anki.tsv`.
8. **Non-Boring Repetition:** Use `practice_pack/repetition_variants/round_01`, then `round_02`, then `round_03`. These repeat the same concepts with changed wording and task surfaces.
9. **Math/Algorithms:** Work through `study_pack/formulas_and_derivations.md` and `practice_pack/math_algorithm_drills.md`.
10. **Visuals:** Use `study_pack/visual_review_guide.md` and `practice_pack/diagram_graphics_prompts.md`; open the original PDF pages for diagrams.
11. **OpenGL/Software:** Use `practice_pack/opengl_software_drills.md`, inspect `course_text_parts/05_opengl_starter_project.txt`, and use the software labs in `reader_pack/interactive_workbook.html`.
12. **Exam Simulation:** Use `study_pack/exam_drill.md`, `practice_pack/multiple_choice.md`, and `practice_pack/sequencing_tasks.md`.
13. **Closed-Format Overprep:** Use `overprep_pack/mock_exams/`, `overprep_pack/concept_confusion_pairs.md`, and `overprep_pack/closed_format_oral_exam_mode.md`. Prefer selecting, matching, filling, ordering, and labeling over vague open answers.
14. **Mistake Repair:** Log every wrong answer in `overprep_pack/mistake_log.md` and reset it into the spaced-repetition schedule.
15. **Final Pass:** Use `overprep_pack/final_readiness_checklist.md`. Revisit every weak spot until you can explain it with definition, pipeline role, diagram, algorithm/formula, OpenGL relation, and typical pitfall.

## Closed-Format Overprep

Use this if you dislike open mock-exam essays:

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

## Rebuild Full Text Export

Run this from the repository root:

```powershell
python scripts/build_course_text.py
```

This rebuilds `course_full_text.txt`, `course_text_parts/`, and `course_build_audit.json`.

To rebuild the exam study pack:

```powershell
python scripts/build_study_pack.py
```

To rebuild the interactive practice pack:

```powershell
python scripts/build_practice_pack.py
```

To rebuild the closed-format overprep pack:

```powershell
python scripts/build_overprep_pack.py
```

To rebuild the original-language reader pack:

```powershell
python scripts/build_reader_pack.py
```

To rebuild the detailed lecture readers and PDFs:

```powershell
python scripts/build_lecture_readers.py
```
