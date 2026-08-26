# Lecture Readers

This folder contains a readable version of every lecture. The raw slide extraction is still the source of truth, but these files add the missing explanatory commentary that makes the material usable for human study. Every extracted slide page has its own commentary block with a source cue, explanation, relevance note, and check question.

Language: English. The lecture material is primarily English, so the generated commentary stays in English.

## Files

- `markdown/` - one readable Markdown file per lecture, with per-slide commentary
- `pdf/` - one PDF per lecture plus `CS8165_complete_lecture_readers.pdf`, with per-slide commentary
- `lecture_reader_manifest.json` - generated coverage manifest

## Recommended Reading Route

1. Read one lecture reader PDF or Markdown file.
2. Open the referenced source chunk in `course_text_parts/03_lectures/`.
3. Answer every `Check yourself` question without notes.
4. Put weak spots into `overprep_pack/mistake_log.md`.
5. Then use `practice_pack/` and `overprep_pack/` for closed-format repetition.
