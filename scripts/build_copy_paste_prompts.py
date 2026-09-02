from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "exam_materials" / "copy_paste_prompts"

sys.path.insert(0, str(ROOT / "scripts"))
import build_exam_materials as exam_materials  # noqa: E402


def slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def term_list(topic: dict) -> str:
    return "; ".join(f"{term}: {definition}" for term, definition in topic["terms"])


def base_context(topic: dict) -> str:
    return "\n".join(
        [
            "Course: CS8165.001 Interactive Computer Graphics.",
            f"Lecture: {topic['id']} - {topic['title']}.",
            f"Source chunk: {exam_materials.lecture_for(topic)['source']}.",
            f"Core idea: {topic['core']}",
            f"Process chain: {topic['chain']}.",
            f"Important terms: {term_list(topic)}.",
            f"Compact rule: {topic['formula']}.",
            f"Main trap: {topic['trap']}",
            f"Assignment connection: {topic['assignment']}.",
            "Learner profile: English around B1, terminology is difficult, verbs and collocations must be explained.",
            "Answer style: straight to the point, no motivational introduction, no document meta commentary, no broad essay task.",
            "Study style: prefer multiple choice, matching, completion, ordering, labeling, and short correction with answer keys.",
        ]
    )


def prompt_block(prompt_id: str, title: str, body: str) -> str:
    return "\n".join(
        [
            f"## {prompt_id} - {title}",
            "",
            "```text",
            body.strip(),
            "```",
            "",
        ]
    )


def explain_prompt(topic: dict) -> str:
    return f"""
{base_context(topic)}

Task:
Explain this lecture topic from zero to exam-ready understanding.
Start with the concrete problem in computer graphics.
Then explain each step of the process chain.
For every important term, explain the meaning, the role in the chain, and one common English verb or collocation used with it.
Add one small everyday analogy only if it makes the technical relation clearer.
End with ten closed-format questions and an answer key.
If you have web access, also find two human-written resources from university notes, official documentation, or textbooks, and explain exactly which part of this lecture each resource supports.
"""


def section_prompt(topic: dict, section: dict) -> str:
    return f"""
{base_context(topic)}

Focus section: {section['title']}.
Source location: {section['slides']}.
Section meaning: {section['mental_model']}.
Section check: {section['check']}.

Task:
Teach only this section.
Explain what problem the section solves, what data or object enters it, what operation happens, what result leaves it, and what later graphics step uses that result.
Rewrite the difficult English into B1-level English.
List the most important verbs and collocations in this section.
Create eight closed-format checks: two multiple-choice, two matching pairs, two fill-in blanks, one ordering task, and one trap question.
Include the answer key.
If you have web access, find one human-written learning source for this exact section and connect it to the course terms above.
"""


def term_prompt(topic: dict, term: str, definition: str) -> str:
    return f"""
{base_context(topic)}

Focus term: {term}.
Course definition: {definition}

Task:
Explain this term as a graphics concept, not as a dictionary word.
Show where it appears in the process chain.
Explain what it is often confused with.
Give five B1-level example sentences using correct English collocations.
Create a matching task that distinguishes this term from five related terms.
Create five multiple-choice questions with near-miss distractors.
Include the answer key and one sentence explaining each answer.
If you have web access, find one human-written source that explains this term clearly and state why it is reliable.
"""


def formula_prompt(topic: dict) -> str:
    return f"""
{base_context(topic)}

Focus compact rule: {topic['formula']}.

Task:
Expand the compact rule into a full explanation.
Define every symbol, word, stage, variable, or operation in simple English.
Give one numerical, geometric, or OpenGL-related example if the topic allows it.
Explain the common mistakes that happen when students memorize the rule without understanding it.
Create completion questions, ordering questions, and one small calculation or reasoning task.
Include the answer key.
If you have web access, find one human-written resource that explains the same rule or algorithm.
"""


def trap_prompt(topic: dict) -> str:
    return f"""
{base_context(topic)}

Focus trap: {topic['trap']}

Task:
Explain why this wrong idea sounds plausible.
Show the correct distinction with a small example.
Create a table with wrong statement, why it is tempting, corrected statement, and exam clue.
Create ten true-false-with-correction questions.
Include the answer key.
Keep the language simple enough for B1 English.
"""


def assignment_prompt(topic: dict) -> str:
    return f"""
{base_context(topic)}

Focus assignment: {topic['assignment']}.

Task:
Connect the lecture topic to the assignment.
List the exact concepts the assignment probably tests.
Explain what source code, OpenGL state, buffer, shader, transformation, image result, or algorithmic step I should look for.
Create a checklist I can use while browsing assignment sources.
Create closed-format questions about the assignment connection.
Include the answer key.
Avoid asking me to write long open answers.
"""


def resource_prompt(topic: dict) -> str:
    return f"""
{base_context(topic)}

Task:
Find human-written learning materials for this topic.
Prioritize university lecture notes, official OpenGL or graphics documentation, textbook chapters, and course pages by named instructors.
Avoid AI-generated summaries, SEO blogs, and shallow tutorials unless they contain a useful diagram or code example.
For each resource, give the title, author or institution if visible, link, why it is relevant, which course terms it supports, and which parts I should ignore if they go beyond CS8165.
Then create a reading sequence from easiest to most precise.
Finish with ten closed-format questions that check whether I understood the resources in relation to this course.
"""


def mastery_prompt(topic: dict) -> str:
    return f"""
{base_context(topic)}

Task:
Act as a strict closed-format examiner for this lecture.
Ask one question at a time.
Allowed formats: multiple choice, matching, fill in the blank, ordering, diagram labeling checklist, true or false with correction, and OpenGL debugging choice.
After each answer, grade it as correct, partly correct, or wrong.
Then give the exact missing concept, the corrected distinction, and the next question.
Do not ask broad essay questions.
Cover every important term, the process chain, the compact rule, the assignment connection, and the main trap.
"""


def lecture_prompts(topic: dict) -> list[tuple[str, str, str]]:
    lecture = exam_materials.lecture_for(topic)
    prompts: list[tuple[str, str, str]] = [
        (f"{topic['id']}-00", "Whole Lecture Explanation And Resources", explain_prompt(topic)),
        (f"{topic['id']}-01", "Compact Rule Expansion", formula_prompt(topic)),
        (f"{topic['id']}-02", "Trap Repair", trap_prompt(topic)),
        (f"{topic['id']}-03", "Assignment Connection", assignment_prompt(topic)),
        (f"{topic['id']}-04", "Human-Written Resource Search", resource_prompt(topic)),
        (f"{topic['id']}-05", "Strict Closed-Format Examiner", mastery_prompt(topic)),
    ]
    for index, section in enumerate(lecture["sections"], start=1):
        prompts.append(
            (
                f"{topic['id']}-S{index:02d}",
                f"Section: {section['title']}",
                section_prompt(topic, section),
            )
        )
    for index, (term, definition) in enumerate(topic["terms"], start=1):
        prompts.append(
            (
                f"{topic['id']}-T{index:02d}",
                f"Term: {term}",
                term_prompt(topic, term, definition),
            )
        )
    return prompts


def lecture_file(topic: dict) -> str:
    return f"{topic['id']}_{slug(topic['title'])}_copy_paste_prompts.md"


def assignment_prompts() -> str:
    lines = ["# Assignment Copy-Paste Prompts", ""]
    for number, title, source, lectures, concepts in exam_materials.ASSIGNMENTS:
        body = f"""
Course: CS8165.001 Interactive Computer Graphics.
Assignment: {number} - {title}.
Assignment source: {source}.
Connected lectures: {lectures}.
Concepts: {concepts}.
Learner profile: English around B1, terminology and software collocations are difficult.
Answer style: straight to the point, no motivational introduction, no document meta commentary.

Task:
Explain what this assignment is testing.
List the lecture concepts needed before attempting it.
Explain the important source-code or OpenGL words in simple English.
Create a browse-checklist for the assignment files.
Create ten closed-format questions about the assignment: multiple choice, matching, ordering, fill-in, and debugging.
Include the answer key.
If you have web access, find one human-written tutorial or official documentation page that supports the assignment concepts.
"""
        lines.append(prompt_block(f"A-{number}", title, body))
    return "\n".join(lines)


def final_coverage_prompts() -> str:
    topic_lines = "\n".join(
        f"- Lecture {topic['id']} {topic['title']}: {topic['core']} Terms: {', '.join(term for term, _ in topic['terms'])}."
        for topic in exam_materials.TOPICS
    )
    body = f"""
Course: CS8165.001 Interactive Computer Graphics.
Full topic coverage:
{topic_lines}

Learner profile: English around B1.
Preferred exam style: closed-format tasks instead of broad open essays.

Task:
Create a complete exam readiness map.
Group all topics by rendering pipeline role.
Identify all concepts that are easy to confuse.
Create a final mixed closed-format exam with at least sixty questions.
Use multiple choice, matching, fill-in, ordering, diagram labeling, formula reasoning, and OpenGL debugging.
Include a full answer key and a short correction note for every answer.
Do not skip any lecture listed above.
"""
    repair = """
Course: CS8165.001 Interactive Computer Graphics.
Learner profile: English around B1.

Task:
I will paste my mistake log below.
Convert every mistake into repair work.
For each mistake, identify the lecture, concept, correct distinction, simpler English explanation, one matching task, one fill-in task, one multiple-choice question, and one next reading target.
Include answer keys.
Avoid broad open essay questions.

Mistake log:
"""
    return "\n".join(
        [
            "# Final Coverage Copy-Paste Prompts",
            "",
            prompt_block("F-01", "Complete Exam Readiness Map", body),
            prompt_block("F-02", "Mistake Log Repair Generator", repair),
        ]
    )


def readme() -> str:
    lines = [
        "# Copy-Paste Prompt Workbook",
        "",
        "Reading order:",
        "",
    ]
    for topic in exam_materials.TOPICS:
        lines.append(f"{topic['id']}. `{lecture_file(topic)}`")
    lines.extend(
        [
            "11. `11_assignment_copy_paste_prompts.md`",
            "12. `12_final_coverage_prompts.md`",
            "",
            "Prompt count:",
            "",
        ]
    )
    total = 0
    for topic in exam_materials.TOPICS:
        count = len(lecture_prompts(topic))
        total += count
        lines.append(f"- Lecture {topic['id']}: {count}")
    total += len(exam_materials.ASSIGNMENTS) + 2
    lines.append(f"- Total: {total}")
    return "\n".join(lines)


def manifest() -> str:
    lecture_counts = {topic["id"]: len(lecture_prompts(topic)) for topic in exam_materials.TOPICS}
    data = {
        "pack": "copy_paste_prompts",
        "lecture_count": len(exam_materials.TOPICS),
        "assignment_prompt_count": len(exam_materials.ASSIGNMENTS),
        "final_prompt_count": 2,
        "lecture_prompt_counts": lecture_counts,
        "total_prompt_count": sum(lecture_counts.values()) + len(exam_materials.ASSIGNMENTS) + 2,
        "files": ["README.md", *[lecture_file(topic) for topic in exam_materials.TOPICS], "11_assignment_copy_paste_prompts.md", "12_final_coverage_prompts.md", "manifest.json"],
    }
    return json.dumps(data, indent=2)


def update_parent_manifest() -> None:
    parent = OUT.parent / "manifest.json"
    if not parent.exists():
        return
    data = json.loads(parent.read_text(encoding="utf-8"))
    files = data.setdefault("files", [])
    prompt_files = [f"copy_paste_prompts/{name}" for name in json.loads(manifest())["files"]]
    for name in prompt_files:
        if name not in files:
            files.append(name)
    data["copy_paste_prompt_count"] = json.loads(manifest())["total_prompt_count"]
    parent.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT / "README.md", readme())
    for topic in exam_materials.TOPICS:
        lines = [f"# Lecture {topic['id']} - {topic['title']} Copy-Paste Prompts", ""]
        for prompt_id, title, body in lecture_prompts(topic):
            lines.append(prompt_block(prompt_id, title, body))
        write(OUT / lecture_file(topic), "\n".join(lines))
    write(OUT / "11_assignment_copy_paste_prompts.md", assignment_prompts())
    write(OUT / "12_final_coverage_prompts.md", final_coverage_prompts())
    write(OUT / "manifest.json", manifest())
    update_parent_manifest()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
