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
- `scripts/build_course_text.py` - reproducible exporter for rebuilding `course_full_text.txt`

## AI Study Files

Use these files depending on the context window:

- `course_text_parts/00_START_HERE.txt` - loading guide and source manifest
- `course_text_parts/03_lectures/` - one text file per lecture chapter
- `course_text_parts/04_assignments/` - one text file per exercise
- `course_text_parts/06_exam_preparation_addendum.txt` - chapter index, formula/notation candidates, visual slide inventory, and AI prompts
- `course_text_parts/98_size_limited_full_text_slices/` - sequential slices under 75 KB each; together they exactly reconstruct `course_full_text.txt`
- `course_text_parts/INDEX.txt` - list of all generated text chunks

Coverage checks are stored in `course_build_audit.json`.

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
