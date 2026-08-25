# CS8165.001 SS26 - Interactive Computer Graphics

Private backup of the Moodle course export `CS8165.001-SS26_1787682614.zip`.

## Structure

- `index.html` - course overview from Moodle
- `lectures/` - lecture pages and renamed slide PDFs
- `assignments/` - exercise pages
- `forums/` - exported forum pages
- `course/` - course administration pages such as group selection
- `examples/` - downloadable starter projects and sample files
- `assets/` - shared Moodle styling
- `course_full_text.txt` - complete structured text export for AI-assisted exam preparation, including extracted slide text, page metadata, formula/notation candidates, a chapter index, exercise index, visual slide inventory, and starter-code contents
- `course_text_parts/` - split text export for AI workflows
- `course_build_audit.json` - machine-readable coverage report for source files, PDF pages, chunks, and validation checks
- `study_pack/` - exam-preparation pack with chapter guides, formula checklist, visual review guide, exam drill, Anki TSV, study plan, and reusable AI prompts
- `practice_pack/` - interactive practice pack with cloze texts, matching tables, MC questions, sequencing tasks, math/algorithm drills, diagram prompts, OpenGL drills, and a roadmap from 0 to exam-ready
- `scripts/build_course_text.py` - reproducible exporter for rebuilding `course_full_text.txt`
- `scripts/build_study_pack.py` - reproducible generator for rebuilding `study_pack/`
- `scripts/build_practice_pack.py` - reproducible generator for rebuilding `practice_pack/`

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

- `study_pack/README.md`
- `study_pack/ai_prompts.md`
- `study_pack/chapter_guides/`
- `study_pack/exam_drill.md`
- `study_pack/flashcards_anki.tsv`
- `study_pack/visual_review_guide.md`

The study pack is derived from the course chunks and does not invent missing old exams, recordings, or official solutions.

## Interactive Practice Pack

Use these for active learning and copy-paste generators:

- `practice_pack/cloze_source_texts.md` - coherent source texts for Lueckentext/cloze generators
- `practice_pack/premade_cloze_texts.md` - same topics with blanks already inserted
- `practice_pack/matching_pairs.tsv` - importable term/definition/chapter table
- `practice_pack/matching_tasks.md` - manual matching grouped by chapter
- `practice_pack/multiple_choice.md` - MC questions with answers
- `practice_pack/sequencing_tasks.md` - order-the-steps tasks
- `practice_pack/math_algorithm_drills.md` - math and algorithm explanation drills
- `practice_pack/diagram_graphics_prompts.md` - drawing and visual explanation tasks
- `practice_pack/opengl_software_drills.md` - OpenGL/software understanding checks
- `practice_pack/interactive_practice_menu.md` - daily active-recall loop
- `practice_pack/roadmap_0_to_100.md` - full route from zero to exam-ready

## Roadmap From 0 To Exam-Ready

1. **Setup:** Open `course_build_audit.json` and confirm all checks are `true`.
2. **Orientation:** Read `course_text_parts/00_START_HERE.txt`, then `study_pack/README.md`.
3. **Core Understanding:** Work through `study_pack/chapter_guides/` from chapter 01 to 10.
4. **Raw Source Check:** For each chapter, load the matching file from `course_text_parts/03_lectures/`.
5. **Active Recall:** Use `practice_pack/cloze_source_texts.md`, `practice_pack/matching_pairs.tsv`, and `study_pack/flashcards_anki.tsv`.
6. **Math/Algorithms:** Work through `study_pack/formulas_and_derivations.md` and `practice_pack/math_algorithm_drills.md`.
7. **Visuals:** Use `study_pack/visual_review_guide.md` and `practice_pack/diagram_graphics_prompts.md`; open the original PDF pages for diagrams.
8. **OpenGL/Software:** Use `practice_pack/opengl_software_drills.md` and inspect `course_text_parts/05_opengl_starter_project.txt`.
9. **Exam Simulation:** Use `study_pack/exam_drill.md`, `practice_pack/multiple_choice.md`, and `practice_pack/sequencing_tasks.md`.
10. **Final Pass:** Revisit every weak spot until you can explain it with definition, pipeline role, diagram, algorithm/formula, and typical pitfall.

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
