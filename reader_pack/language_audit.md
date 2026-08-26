# Language Audit

- `raw_source_language_policy`: Preserve original extracted course text exactly as source material. The course is primarily English; Moodle interface or notification text may be German when exported that way.
- `generated_reader_pack_language`: English, because it is the primary language of the lecture material.
- `older_generated_pack_note`: Some earlier helper files contain German study instructions because they were generated from German user requests. They are support material, not raw source text. Use reader_pack for original-language guided reading.
- `complete_source_anchor`: course_full_text.txt and course_text_parts/

Practical rule: if you feed files to another AI and want original-language output, start with `reader_pack/narrative_reader.md`, then add the matching lecture chunk from `course_text_parts/03_lectures/`.