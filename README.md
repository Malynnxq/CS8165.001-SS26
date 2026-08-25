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
- `scripts/build_course_text.py` - reproducible exporter for rebuilding `course_full_text.txt`

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
