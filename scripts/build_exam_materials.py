from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "exam_materials"

sys.path.insert(0, str(ROOT / "scripts"))
import build_lecture_readers as lecture_readers  # noqa: E402


TOPICS = [
    {
        "id": "01",
        "title": "Introduction",
        "core": "Computer graphics generates images from descriptions; interactive graphics adds a strict time budget and a feedback loop with the user.",
        "chain": "scene or image description -> representation choice -> sampling or rendering process -> visible image -> interaction or analysis",
        "assignment": "00 Introduction to C++",
        "terms": [
            ("raster image", "A grid of stored pixel samples; it is already an image, not a 3D scene."),
            ("pixel", "A discrete image sample containing color or channel values."),
            ("color depth", "The number of bits used to represent color values, controlling precision and memory size."),
            ("3D model", "A structured description of geometry and attributes that can generate many possible images."),
            ("primitive", "A basic geometric object such as a point, line, or triangle used by the rendering pipeline."),
            ("interactive graphics", "Rendering where images must update quickly enough to respond to input or animation."),
        ],
        "trap": "Do not confuse an image representation with the geometric cause of the image.",
        "formula": "image memory = width x height x bits per pixel, then divide by 8 for bytes",
    },
    {
        "id": "02",
        "title": "Rendering Pipeline",
        "core": "Rendering is a sequence of representation changes: models become vertices, primitives, fragments, tested fragments, and finally framebuffer updates.",
        "chain": "application data -> geometry stage -> primitive assembly -> rasterization -> fragment operations -> framebuffer",
        "assignment": "01 Rendering Pipeline",
        "terms": [
            ("application stage", "CPU-side preparation of models, scene data, interaction, animation, and rendering state."),
            ("geometry stage", "Pipeline stage that transforms vertices and prepares primitives."),
            ("rasterization", "Conversion of projected primitives into fragment candidates on a sample grid."),
            ("fragment", "A candidate pixel contribution produced by rasterization before final tests and blending."),
            ("framebuffer", "Memory target that stores color, depth, stencil, or related per-pixel results."),
            ("double buffering", "Using front and back buffers so drawing can happen off-screen before display swap."),
        ],
        "trap": "Do not collapse the whole pipeline into 'the GPU draws it'; name the intermediate representations.",
        "formula": "vertices -> primitives -> fragments -> tests -> pixels",
    },
    {
        "id": "03",
        "title": "Geometric Transformations",
        "core": "Transformations change how points, vectors, normals, and coordinate frames are expressed across model, world, view, and clip-related spaces.",
        "chain": "object/model coordinates -> model matrix -> world coordinates -> view matrix -> camera/view coordinates",
        "assignment": "03 Geometric Transformations",
        "terms": [
            ("homogeneous coordinates", "Coordinates with an additional component that make translation and projection expressible by matrices."),
            ("translation", "A transformation that moves points by an offset; direction vectors are not shifted the same way."),
            ("rotation", "A transformation that changes orientation while preserving distances."),
            ("scaling", "A transformation that changes size and can distort normals if handled incorrectly."),
            ("matrix composition", "Combining transformations by multiplication, where order matters."),
            ("normal transformation", "Transforming surface normals consistently, often requiring inverse-transpose logic under non-uniform scaling."),
        ],
        "trap": "Do not multiply matrices without naming source space, target space, and order.",
        "formula": "p_world = M_model * p_model; p_view = V * p_world",
    },
    {
        "id": "04",
        "title": "Geometric Projection",
        "core": "Projection maps camera-space geometry into clip coordinates and then normalized device coordinates before viewport mapping.",
        "chain": "view-space position -> projection matrix -> clip coordinates -> perspective divide -> NDC -> viewport coordinates",
        "assignment": "04 Projections and Clipping",
        "terms": [
            ("view volume", "The 3D region visible to the camera before mapping to the screen."),
            ("orthographic projection", "Projection without perspective foreshortening; parallel lines stay parallel."),
            ("perspective projection", "Projection where farther objects appear smaller after division by the homogeneous component."),
            ("clip coordinates", "Coordinates produced before clipping and perspective divide."),
            ("perspective divide", "Division by w that produces normalized device coordinates."),
            ("viewport transformation", "Mapping normalized device coordinates to window or screen coordinates."),
        ],
        "trap": "Do not confuse projection with viewport mapping; the perspective divide sits between them.",
        "formula": "p_clip = P * p_view; p_ndc = p_clip.xyz / p_clip.w",
    },
    {
        "id": "05",
        "title": "Clipping",
        "core": "Clipping classifies geometry against boundaries and keeps, rejects, or cuts primitives before rasterization.",
        "chain": "primitive -> boundary tests -> inside/outside classification -> intersections -> clipped primitive",
        "assignment": "04 Projections and Clipping",
        "terms": [
            ("clipping", "Removing or cutting geometry outside a valid window, plane, or volume."),
            ("Cohen-Sutherland", "Line clipping method using region/outcodes to reject, accept, or clip line segments."),
            ("Sutherland-Hodgman", "Polygon clipping method that processes polygon vertices against clipping boundaries."),
            ("Cyrus-Beck", "Parametric line clipping method using entering and leaving parameter intervals."),
            ("outcode", "A compact code describing where a point lies relative to clipping boundaries."),
            ("intersection point", "New boundary point created when a primitive crosses a clipping edge or plane."),
        ],
        "trap": "Do not describe clipping as only deletion; crossing primitives can create new vertices.",
        "formula": "line point p(t) = p0 + t * (p1 - p0), then restrict t to the visible interval",
    },
    {
        "id": "06",
        "title": "Rasterization",
        "core": "Rasterization converts continuous projected geometry into discrete fragment candidates and interpolated per-fragment attributes.",
        "chain": "projected primitive -> sample coverage -> fragment generation -> attribute interpolation -> fragment tests",
        "assignment": "05 Rasterization",
        "terms": [
            ("scan conversion", "Determining which discrete samples are covered by an ideal geometric primitive."),
            ("triangle coverage", "Testing which pixel/sample positions lie inside a triangle."),
            ("barycentric coordinates", "Weights relative to triangle vertices used for inside tests and interpolation."),
            ("interpolation", "Computing per-fragment values from vertex attributes."),
            ("aliasing", "Artifacts caused when continuous signals are sampled too coarsely."),
            ("fragment candidate", "A potential contribution to the framebuffer, not yet a guaranteed visible pixel."),
        ],
        "trap": "Do not call every generated fragment a final pixel.",
        "formula": "attribute = alpha * a0 + beta * a1 + gamma * a2, with alpha + beta + gamma = 1",
    },
    {
        "id": "07",
        "title": "Visibility Determination",
        "core": "Visibility algorithms decide which candidate surface is actually seen from the current viewpoint.",
        "chain": "many projected or intersected candidates -> comparison rule -> visible surface or fragment -> final image contribution",
        "assignment": "Rasterization and integrated rendering tasks",
        "terms": [
            ("depth buffer", "Per-pixel storage of depth values used to keep the nearest visible fragment."),
            ("z-buffer algorithm", "Image-space visibility method comparing fragment depths at each pixel."),
            ("Painter's algorithm", "Object-order visibility method based on drawing farther objects before nearer objects."),
            ("BSP tree", "Space-partitioning structure that can support visibility ordering."),
            ("Warnock algorithm", "Image-space subdivision method for resolving visible surfaces in regions."),
            ("ray casting", "Finding visible surfaces by tracing rays from image samples into the scene."),
        ],
        "trap": "Do not confuse generating a fragment with proving that it is visible.",
        "formula": "visible fragment = candidate with passing depth/visibility test at the sample",
    },
    {
        "id": "08",
        "title": "Local Illumination",
        "core": "Local illumination computes color from surface orientation, light direction, view direction, and material response.",
        "chain": "surface point + normal + light + view + material -> lighting equation -> shaded color",
        "assignment": "Rendering contest and shader-related tasks",
        "terms": [
            ("surface normal", "Vector describing surface orientation and controlling diffuse/specular response."),
            ("ambient term", "Approximate base illumination independent of direct light direction."),
            ("diffuse reflection", "View-independent light response based on the angle between normal and light direction."),
            ("specular reflection", "View-dependent highlight term based on reflection or half-vector alignment."),
            ("Phong model", "Local illumination model combining ambient, diffuse, and specular components."),
            ("material coefficient", "Parameter controlling how strongly a surface responds to lighting terms."),
        ],
        "trap": "Do not mix up normal, light direction, and view direction; each changes a different lighting term.",
        "formula": "color = ambient + diffuse + specular",
    },
    {
        "id": "09",
        "title": "Texturing",
        "core": "Texturing uses coordinates and sampler state to fetch stored data and interpret it in a shader.",
        "chain": "fragment coordinates -> texture coordinates -> sampler/filter/wrap state -> texel fetch -> shader meaning",
        "assignment": "Rendering contest and texture/shader tasks",
        "terms": [
            ("texture", "Sampled data array used for color, normals, material data, depth, or other shader inputs."),
            ("texel", "A stored sample in texture memory."),
            ("UV coordinates", "Coordinates that map surface locations to texture space."),
            ("filtering", "Rule for reconstructing values between texels, such as nearest or linear filtering."),
            ("mipmap", "Precomputed lower-resolution texture levels used to reduce aliasing and improve sampling."),
            ("environment mapping", "Using texture lookup to approximate surrounding reflections or distant lighting."),
        ],
        "trap": "Do not reduce texturing to pasting an image onto geometry.",
        "formula": "sampled value = texture(sampler, uv), then shader interprets the value",
    },
    {
        "id": "10",
        "title": "Shadows",
        "core": "Shadows are visibility tests from the light source, not only dark shapes seen by the camera.",
        "chain": "light -> possible blocker -> receiver point -> light-space visibility test -> lit or shadowed result",
        "assignment": "Rendering contest and integrated lighting tasks",
        "terms": [
            ("shadow", "Reduced direct illumination where an object blocks light from reaching a receiver."),
            ("occluder", "Object that blocks light."),
            ("receiver", "Surface where the shadow appears."),
            ("shadow map", "Depth image rendered from the light's point of view for later visibility comparison."),
            ("shadow volume", "Volume of space hidden from a light by an occluder."),
            ("projective shadow", "Shadow construction based on projecting geometry onto a receiver."),
        ],
        "trap": "Do not explain a shadow only from the camera view; the key test is light-space visibility.",
        "formula": "point is shadowed if something is closer to the light along the same light ray",
    },
]


ASSIGNMENTS = [
    ("00", "Introduction to C++", "course_text_parts/04_assignments/00_introduction-to-cpp.txt", "01, 02", "C++ basics, build workflow, OpenGL preparation"),
    ("01", "Rendering Pipeline", "course_text_parts/04_assignments/01_rendering-pipeline.txt", "02", "pipeline stages, draw loop, framebuffer result"),
    ("02", "Primitive Types / Shaders", "course_text_parts/04_assignments/02_primitive-types-shaders.txt", "02, 06", "primitives, vertex shader, fragment shader, fragment output"),
    ("03", "Geometric Transformations", "course_text_parts/04_assignments/03_geometric-transformations.txt", "03", "matrix transforms, model placement, coordinate spaces"),
    ("04", "Projections and Clipping", "course_text_parts/04_assignments/04_projections-and-clipping.txt", "04, 05", "projection, view volume, clipping"),
    ("05", "Rasterization", "course_text_parts/04_assignments/05_rasterization.txt", "06, 07", "coverage, interpolation, fragment generation, visibility relation"),
    ("Bonus", "Rendering Contest", "course_text_parts/04_assignments/Bonus_rendering-contest.txt", "02, 03, 04, 06, 08, 09, 10", "integrated rendering, lighting, texturing, shadows, visual quality"),
]


def ensure_out() -> None:
    if OUT.exists():
        for path in OUT.rglob("*"):
            if path.is_file():
                path.unlink()
    OUT.mkdir(exist_ok=True)


def write(path: str, text: str) -> None:
    target = OUT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip() + "\n", encoding="utf-8")


def slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def mc_block(correct: str, distractors: list[str], seed: int) -> tuple[list[str], str]:
    options = [correct] + distractors[:3]
    offset = seed % len(options)
    rotated = options[offset:] + options[:offset]
    lines = [f"{letter}. {option}" for letter, option in zip("ABCD", rotated)]
    answer = "ABCD"[rotated.index(correct)]
    return lines, answer


def chain_cloze(chain: str, seed: int) -> tuple[str, str]:
    steps = chain.split(" -> ")
    if len(steps) < 3:
        return chain.replace(steps[-1], "____"), steps[-1]
    hide_index = 1 + (seed % (len(steps) - 2))
    answer = steps[hide_index]
    steps[hide_index] = "____"
    return " -> ".join(steps), answer


def lecture_for(topic: dict) -> dict:
    for lecture in lecture_readers.LECTURES:
        if lecture["id"] == topic["id"]:
            return lecture
    raise KeyError(topic["id"])


def source_page_count(lecture: dict) -> int:
    return lecture_readers.source_stats(lecture["source"])["pages"]


def chapter_filename(topic: dict) -> str:
    return f"chapters/{topic['id']}_{slug(topic['title'])}_exam_chapter.md"


NUMBER_WORDS = {
    "01": "one",
    "02": "two",
    "03": "three",
    "04": "four",
    "05": "five",
    "06": "six",
    "07": "seven",
    "08": "eight",
    "09": "nine",
    "10": "ten",
}


def plain_chapter_filename(topic: dict) -> str:
    return f"chapters_plain/{topic['id']}_{slug(topic['title'])}_plain_text.txt"


def bridge_chapter_filename(topic: dict) -> str:
    return f"chapters_bridge/{topic['id']}_{slug(topic['title'])}_b1_bridge.md"


def chain_as_words(topic: dict) -> str:
    return topic["chain"].replace(" -> ", ", then ")


def everyday_bridge(topic: dict) -> str:
    examples = {
        "01": "You already know that a phone or laptop screen is made of many small picture points. This lecture connects that everyday idea to the more technical idea of computer graphics.",
        "02": "You already know a factory line, where one station does one job and gives the result to the next station. The rendering pipeline works in a similar way.",
        "03": "You already know moving, turning, and resizing objects from normal software. This lecture explains the mathematical version of those actions.",
        "04": "You already know that a camera turns a three dimensional scene into a flat picture. Projection is the graphics version of that idea.",
        "05": "You already know cropping a photo or cutting away the part of a picture that is outside a window. Clipping is the geometric version of that idea.",
        "06": "You already know that a screen is a grid. Rasterization explains how smooth geometric shapes become decisions on that grid.",
        "07": "You already know that a nearer object can hide a farther object. Visibility determination is the formal version of that simple fact.",
        "08": "You already know that a surface looks brighter when it faces a lamp and darker when it turns away. Local illumination explains this with vectors and material values.",
        "09": "You already know that an image can be placed on a surface, like a label on a bottle. Texturing is the graphics version, but it is more general than a simple sticker.",
        "10": "You already know that a shadow appears when something blocks light. The important course idea is that this is a visibility question from the light, not only from the camera.",
    }
    return examples[topic["id"]]


def plain_text(text: str) -> str:
    replacements = [
        ("cannot", "cannot"),
        ("can't", "cannot"),
        ("won't", "will not"),
        ("n't", " not"),
        ("->", " then "),
        ("=>", " therefore "),
        ("<=", " less than or equal to "),
        (">=", " greater than or equal to "),
        ("=", " equals "),
        ("+", " plus "),
        ("*", " times "),
        ("/", " or "),
        ("_", " "),
        ("-", " "),
        (";", ","),
        (":", ","),
        ("`", ""),
        ("\"", ""),
        ("'", ""),
        ("(", ", "),
        (")", ", "),
        ("[", ", "),
        ("]", ", "),
        ("#", " "),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    text = re.sub(r"[^A-Za-z.,!?\s]", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" +([.,!?])", r"\1", text)
    text = re.sub(r"([.,!?])([A-Za-z])", r"\1 \2", text)
    text = re.sub(r"\s+\n", "\n", text)
    text = re.sub(r"\n\s+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()
    if text and text[-1] not in ".!?":
        text += "."
    return text


def sentence(text: str) -> str:
    return plain_text(text)


def plain_chapter_text(topic: dict) -> str:
    lecture = lecture_for(topic)
    number_word = NUMBER_WORDS[topic["id"]]
    chain_words = topic["chain"].replace(" -> ", ", then ")
    lines = [
        sentence(f"Lecture {number_word} is about {topic['title']}."),
        "",
        sentence(
            f"The central idea is this. {topic['core']} The useful mental chain is {chain_words}. This chain matters because every later question in the chapter becomes easier when you know what enters a step, what changes inside the step, and what leaves the step."
        ),
        "",
        sentence(
            "Before the details, keep the full rendering story in mind. Scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. This chapter is one focused part of that larger story."
        ),
        "",
    ]
    for section_index, section in enumerate(lecture["sections"], start=1):
        ordinal = [
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "tenth",
        ][section_index - 1]
        lines.extend(
            [
                sentence(f"The {ordinal} idea in this lecture is {section['title']}."),
                "",
            ]
        )
        for paragraph in section["commentary"]:
            lines.extend([sentence(paragraph), ""])
        lines.extend(
            [
                sentence(f"The study meaning is this. {section['mental_model']}"),
                "",
                sentence(f"A useful closed check is this question. {section['check']}"),
                "",
            ]
        )
    lines.extend(
        [
            sentence("The most important vocabulary should be learned as connected roles in the system, not as isolated dictionary entries."),
            "",
        ]
    )
    for term, definition in topic["terms"]:
        lines.extend(
            [
                sentence(
                    f"The term {term} means this. {definition} It belongs here because it participates in the chain {chain_words}. In an exam question, connect the term to the data it receives, the operation it supports, the output it influences, and the later step that depends on it."
                ),
                "",
            ]
        )
    lines.extend(
        [
            sentence(f"The compact rule for this chapter is {topic['formula']}."),
            "",
            sentence(
                "Do not treat the compact rule as a slogan. A formula or algorithm is useful only when you can name the input, the decision or computation, the output, and the reason that output is needed later."
            ),
            "",
            sentence(
                f"This chapter connects most directly to the assignment {topic['assignment']}. The assignment matters because it turns lecture vocabulary into a visible or code level task. When you inspect the assignment, ask which part of the chain is being practiced, {chain_words}."
            ),
            "",
            sentence(
                f"The main exam trap is this. {topic['trap']} This trap is dangerous because it sounds close to the truth. Test every tempting answer against the full chain, input, operation, output, and next use. If one of those pieces is missing, the answer is probably a distractor."
            ),
            "",
            sentence(
                "A strong answer names the problem this chapter solves, the important representation, the operation or rule, the output representation, the next rendering stage, one assignment or software connection, and one typical mistake with the corrected distinction."
            ),
            "",
            sentence(
                f"You are done with this chapter only when you can recognize a new question as belonging to {topic['title']}, rebuild the chain {chain_words}, and choose the correct answer even when the wording changes."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def bridge_phrase_bank(topic: dict) -> list[tuple[str, str, str, str]]:
    chain_words = chain_as_words(topic)
    return [
        (
            "to represent something",
            "to show something in a certain form.",
            "In graphics, the same object can be represented as pixels, vertices, fragments, texture values, or depth values.",
            "subject, verb, object, result.",
        ),
        (
            "to convert A into B",
            "to change information from one form into another form.",
            f"The course often says that one stage converts data into the next stage of this process: {chain_words}.",
            "input, conversion, output.",
        ),
        (
            "to map A to B",
            "to connect one space, value, or position to another space, value, or position.",
            "If a lecture says that coordinates are mapped, it means that the same thing is described in a new place or scale.",
            "source space, mapping rule, target space.",
        ),
        (
            "to determine whether",
            "to decide if something is true or false.",
            "Graphics algorithms often determine whether a point is inside, visible, covered, lit, or shadowed.",
            "object, test, true or false result.",
        ),
        (
            "to pass a test",
            "to satisfy a rule and continue to the next step.",
            "A fragment can pass a depth test or fail it, so it may or may not become visible.",
            "candidate, test rule, accepted or rejected result.",
        ),
        (
            "to depend on",
            "to need something else before it can work correctly.",
            f"The later part of the chapter depends on the earlier part of this chain: {chain_words}.",
            "later step, required earlier step.",
        ),
        (
            "to store a value",
            "to keep a value in memory so that it can be used later.",
            "Buffers, textures, and framebuffers store values for rendering.",
            "storage object, stored value, later access.",
        ),
        (
            "at draw time",
            "at the exact moment when the GPU receives the draw command.",
            "In OpenGL, the current state at draw time is very important.",
            "current state, draw command, GPU result.",
        ),
    ]


def simple_topic_problem(topic: dict) -> str:
    return (
        f"This lecture asks a practical question. What must the computer know, change, test, or store so that the topic called {topic['title']} works in a rendering system?"
    )


def bridge_chapter_text(topic: dict) -> str:
    lecture = lecture_for(topic)
    chain_steps = topic["chain"].split(" -> ")
    chain_words = chain_as_words(topic)
    lines = [
        f"# Lecture {topic['id']} - {topic['title']} B1 Bridge",
        "",
        "## 1. Starting Point",
        "",
        simple_topic_problem(topic),
        "",
        "## 2. Everyday Bridge",
        "",
        everyday_bridge(topic),
        "",
        f"The main idea in easier English is this: {topic['core']}",
        "",
        "A graphics lecture usually explains a process. A process means that something starts in one form, changes several times, and ends in another form.",
        "",
        "For this lecture, the process is:",
        "",
    ]
    for index, step in enumerate(chain_steps, start=1):
        connector = "This is the start." if index == 1 else "This comes after the previous step."
        lines.extend(
            [
                f"{index}. {step}. {connector}",
                "",
            ]
        )
    lines.extend(
        [
        "## 3. English Bridge",
        "",
        ]
    )
    for phrase, meaning, example, pattern in bridge_phrase_bank(topic):
        lines.extend(
            [
                f"### {phrase}",
                "",
                f"Meaning: {meaning}",
                "",
                f"Course example: {example}",
                "",
                f"Pattern: {pattern}",
                "",
            ]
        )
    lines.extend(
        [
            "## 4. Terminology Bridge",
            "",
            "The important words are not random vocabulary. Each word has a job in the rendering story.",
            "",
        ]
    )
    for term, definition in topic["terms"]:
        lines.extend(
            [
                f"### {term}",
                "",
                f"Simple meaning: {definition}",
                "",
            f"Why it is here: this word helps explain {topic['title'].lower()}. It connects to this process: `{chain_words}`.",
                "",
                f"Good sentence pattern: `{term}` is used when the system needs to describe, change, test, store, or use this kind of information.",
                "",
            ]
        )
    lines.extend(
        [
            "## 5. Step By Step Bridge",
            "",
        ]
    )
    for section_index, section in enumerate(lecture["sections"], start=1):
        lines.extend(
            [
                f"### {topic['id']}.{section_index} {section['title']}",
                "",
                f"Core sentence: this section explains one part of {topic['title'].lower()}.",
                "",
                f"Main connection: {section['mental_model']}",
                "",
                "Slower English:",
                "",
            ]
        )
        for paragraph in section["commentary"]:
            lines.extend([f"{plain_text(paragraph)}", ""])
        lines.extend(
            [
                "Verb pattern: prepares, handles, creates, applies, computes, decides, stores, maps, tests, and converts connect the action to the data, stage, value, or result.",
                "",
            ]
        )
        lines.extend(
            [
                f"Check: {section['check']}",
                "",
            ]
        )
    lines.extend(
        [
            "## 6. Reading The Main Chapter After This",
            "",
            f"The most dangerous misunderstanding in this lecture is: {topic['trap']}",
            "",
            f"The compact rule is: {topic['formula']}",
            "",
        ]
    )
    return "\n".join(lines)


def chapter_text(topic: dict) -> str:
    lecture = lecture_for(topic)
    terms = topic["terms"]
    first_term, first_definition = terms[0]
    lines = [
        f"# Lecture {topic['id']} - {topic['title']} Exam Chapter",
        "",
        f"Source lecture chunk: `{lecture['source']}`",
        f"Extracted source pages: {source_page_count(lecture)}",
        f"Primary assignment connection: {topic['assignment']}",
        "",
        "## 1. What Problem This Chapter Solves",
        "",
        f"{topic['core']} The chapter exists because this part of computer graphics answers a specific missing question in the full rendering story. The compact chain is `{topic['chain']}`. If you can recite the chain but cannot explain why each arrow exists, you have memorized the wording rather than understood the topic.",
        "",
        f"The first anchor term is `{first_term}`: {first_definition} This term is not isolated vocabulary. It is part of the data flow of the chapter, and its meaning becomes useful only when you can say what information it consumes, what it produces, and which later rendering step depends on it.",
        "",
        "## 2. Required Background",
        "",
        "Before reading this chapter, make sure you can already explain the basic rendering pipeline in one sentence: scene data is prepared, transformed, projected, converted to fragments, tested, shaded or combined, and finally written into a framebuffer. Every chapter in this course is one piece of that larger story.",
        "",
        f"For this lecture, the required background is the ability to follow this relation: `{topic['chain']}`. Each arrow means that the representation changes. The exam can test the name of a concept, but stronger questions usually test whether you know what changed and why that change was necessary.",
        "",
        "## 3. The Chapter Explained",
        "",
    ]
    for section_index, section in enumerate(lecture["sections"], start=1):
        lines.extend(
            [
                f"### {topic['id']}.{section_index} {section['title']}",
                "",
                f"Source location: {section['slides']}",
                "",
            ]
        )
        for paragraph in section["commentary"]:
            lines.extend([paragraph, ""])
        lines.extend(
            [
                f"Study meaning: {section['mental_model']}",
                "",
                f"Closed check: {section['check']}",
                "",
            ]
        )
    lines.extend(
        [
            "## 4. Key Terms In Plain Language",
            "",
            "Learn these terms as roles in a system, not as dictionary entries.",
            "",
        ]
    )
    for term, definition in terms:
        lines.extend(
            [
                f"### {term}",
                "",
                f"{definition} In an exam answer, connect `{term}` to the chapter chain: `{topic['chain']}`. Say where it appears, what it affects, and what would break if you misunderstood it.",
                "",
            ]
        )
    lines.extend(
        [
            "## 5. Formula, Algorithm, Or Compact Rule",
            "",
            f"`{topic['formula']}`",
            "",
            "Do not treat this as a slogan. A compact rule is useful only if you can unpack every symbol or step. For formulas, name the units and the coordinate space. For algorithms, name the input, the decision rule, and the output. For OpenGL-related concepts, name the object, state, binding, shader stage, or framebuffer effect involved.",
            "",
            "## 6. Assignment Connection",
            "",
            f"This chapter connects most directly to `{topic['assignment']}`. The assignment is important because it turns lecture vocabulary into a visible or code-level task. When you inspect the assignment text or extracted source files, ask which part of the chain is being practiced: `{topic['chain']}`.",
            "",
            "Use the assignment as a diagnostic. If you can read the chapter but cannot predict what the assignment code is supposed to do, then the concept is still passive knowledge. Repair that by writing the exact missing step into `overprep_pack/mistake_log.md`.",
            "",
            "## 7. Typical Exam Traps",
            "",
            f"Main trap: {topic['trap']}",
            "",
            "The trap is dangerous because it usually sounds close to the truth. High exam performance depends on catching these near-misses quickly. When a multiple-choice option looks plausible, test it against the full chain: input, operation, output, next use. If one of those links is missing or wrong, the option is probably a distractor.",
            "",
            "## 8. What A Strong Answer Must Contain",
            "",
            "- The problem this chapter solves.",
            "- The important data or object representation.",
            "- The operation, algorithm, formula, or API mechanism.",
            "- The output representation.",
            "- The next pipeline stage or later use.",
            "- One assignment or OpenGL/software connection.",
            "- One typical mistake and the corrected distinction.",
            "",
            "## 9. Closed-Format Self-Test",
            "",
            f"1. Complete the chain: `{chain_cloze(topic['chain'], int(topic['id']))[0]}`",
            f"2. Match `{terms[1][0]}` to its role: {terms[1][1]}",
            f"3. Select the dangerous misconception: {topic['trap']}",
            f"4. Explain in one sentence why `{terms[2][0]}` belongs in this chapter.",
            "",
            "## 10. End Condition",
            "",
            f"You are done with Lecture {topic['id']} only when you can read a new question, recognize that it belongs to `{topic['title']}`, and reconstruct the relevant part of `{topic['chain']}` without looking. Then verify with the drills in `exam_materials/` and the corresponding source chunk.",
            "",
        ]
    )
    return "\n".join(lines)


def combined_chapters() -> str:
    lines = [
        "# CS8165 Complete Exam Chapters",
        "",
        "This file combines the ten generated exam chapters. Use the individual files in `exam_materials/chapters/` when you want a cleaner one-chapter reading session.",
        "",
    ]
    for topic in TOPICS:
        lines.append(f"- Lecture {topic['id']} - {topic['title']}: `{chapter_filename(topic)}`")
    lines.append("")
    for topic in TOPICS:
        lines.append(chapter_text(topic))
        lines.append("")
    return "\n".join(lines)


def combined_plain_chapters() -> str:
    lines = []
    for topic in TOPICS:
        lines.append(plain_chapter_text(topic))
        lines.append("")
    return "\n".join(lines)


def combined_bridge_chapters() -> str:
    lines = [
        "# CS8165 B1 Bridge Chapters",
        "",
    ]
    for topic in TOPICS:
        lines.append(f"- Lecture {topic['id']} - {topic['title']}: `{bridge_chapter_filename(topic)}`")
    lines.append("")
    for topic in TOPICS:
        lines.append(bridge_chapter_text(topic))
        lines.append("")
    return "\n".join(lines)


def reading_route() -> str:
    lines = [
        "# 00 - Reading Route",
        "",
        "## The Order",
        "",
        "1. Read one lecture in `lecture_readers/markdown/` or the combined PDF.",
        "2. Open the matching raw source chunk in `course_text_parts/03_lectures/`.",
        "3. Check every slide cue against the Professor-style explanation.",
        "4. Open the matching assignment text and extracted source package.",
        "5. Do closed-format practice: cloze, matching, sequencing, MC, diagram labels, OpenGL debugging.",
        "6. Log every wrong answer in the mistake log.",
        "7. Repeat with changed wording from the repetition variants.",
        "",
        "## Completion Rule",
        "",
        "A topic is not finished when it feels familiar. It is finished when you can identify it under new wording, connect it to the pipeline, solve a closed-format task, and explain the common trap.",
        "",
    ]
    for topic in TOPICS:
        lines.extend(
            [
                f"## Lecture {topic['id']} - {topic['title']}",
                "",
                f"Core idea: {topic['core']}",
                "",
                f"Concept chain: `{topic['chain']}`",
                "",
                f"Assignment connection: {topic['assignment']}",
                "",
                f"Formula or compact rule: `{topic['formula']}`",
                "",
                f"High-risk trap: {topic['trap']}",
                "",
                "Before moving on, you must be able to match each term to its role:",
                "",
            ]
        )
        for term, definition in topic["terms"]:
            lines.append(f"- `{term}` - {definition}")
        lines.append("")
    return "\n".join(lines)


def mastery_checklists() -> str:
    lines = [
        "# 01 - Mastery Checklists By Lecture",
        "",
        "Use these checklists after reading a chapter and before doing mixed exam simulation.",
        "",
    ]
    for topic in TOPICS:
        lines.extend(
            [
                f"## Lecture {topic['id']} - {topic['title']}",
                "",
                "- [ ] I can state the core problem this lecture solves.",
                "- [ ] I can explain the data entering the topic.",
                "- [ ] I can explain the operation, algorithm, or transformation.",
                "- [ ] I can name the output representation.",
                "- [ ] I can place the topic in the rendering pipeline.",
                "- [ ] I can connect it to the listed assignment.",
                "- [ ] I can solve a closed-format question about it.",
                "- [ ] I can identify the common trap.",
                "",
                f"Core chain to recite: `{topic['chain']}`",
                "",
                f"Trap to avoid: {topic['trap']}",
                "",
                "Terms to know:",
                "",
            ]
        )
        for term, definition in topic["terms"]:
            lines.append(f"- [ ] `{term}` - {definition}")
        lines.append("")
    return "\n".join(lines)


def cloze_inputs() -> str:
    lines = [
        "# 02 - Cloze Generator Inputs",
        "",
        "Copy one block at a time into a cloze generator. These texts are coherent by design: they include cause, data, operation, output, and common trap.",
        "",
    ]
    for topic in TOPICS:
        term_sentence = " ".join(f"{term} means {definition}" for term, definition in topic["terms"])
        lines.extend(
            [
                f"## Lecture {topic['id']} - {topic['title']}",
                "",
                f"{topic['core']} The concept chain is {topic['chain']}. {term_sentence} A compact rule for this lecture is: {topic['formula']}. The assignment connection is {topic['assignment']}. The main trap is: {topic['trap']}",
                "",
                "Suggested blanks: " + ", ".join(term for term, _ in topic["terms"]) + f", {topic['formula']}",
                "",
            ]
        )
    return "\n".join(lines)


def matching_pairs() -> str:
    rows = ["lecture_id\tlecture_title\tterm\tdefinition\tmatch_reason\tcommon_distractor"]
    for topic in TOPICS:
        for term, definition in topic["terms"]:
            rows.append(
                "\t".join(
                    [
                        topic["id"],
                        topic["title"],
                        term,
                        definition,
                        f"Belongs to the chain: {topic['chain']}",
                        topic["trap"],
                    ]
                )
            )
    return "\n".join(rows)


def matching_tasks() -> str:
    lines = [
        "# 03 - Matching Tasks",
        "",
        "Match each term to the correct role. Use the TSV file for import into tools; use this Markdown file for manual practice.",
        "",
    ]
    for topic in TOPICS:
        lines.extend([f"## Lecture {topic['id']} - {topic['title']}", "", "Terms:", ""])
        for index, (term, _) in enumerate(topic["terms"], start=1):
            lines.append(f"{index}. {term}")
        lines.extend(["", "Definitions:", ""])
        for letter, (_, definition) in zip("ABCDEF", topic["terms"]):
            lines.append(f"{letter}. {definition}")
        lines.extend(["", f"Trap check: {topic['trap']}", ""])
    return "\n".join(lines)


def closed_format_drills() -> str:
    lines = [
        "# 04 - Closed-Format Drills",
        "",
        "Answers are at the end.",
        "",
    ]
    answers: list[str] = []
    q = 1
    for topic_index, topic in enumerate(TOPICS, start=1):
        options, answer = mc_block(
            topic["core"],
            [
                "The lecture is mainly a list of unrelated definitions.",
                "The lecture is only relevant for historical context.",
                "The lecture can be ignored if the final image looks correct.",
            ],
            topic_index,
        )
        first_term, first_def = topic["terms"][0]
        second_term, _ = topic["terms"][1]
        lines.extend(
            [
                f"## Lecture {topic['id']} - {topic['title']}",
                "",
                f"Q{q}. Which statement best describes the core idea?",
                "",
                *options,
                "",
            ]
        )
        answers.append(f"Q{q}: {answer}")
        q += 1
        cloze, missing = chain_cloze(topic["chain"], topic_index)
        lines.extend(
            [
                f"Q{q}. Complete the chain:",
                "",
                f"`{cloze}`",
                "",
            ]
        )
        answers.append(f"Q{q}: {missing}. Full chain: `{topic['chain']}`")
        q += 1
        options, answer = mc_block(
            first_def,
            [
                f"Same meaning as `{second_term}`.",
                "A final exam score calculation.",
                "A file organization convention only.",
            ],
            topic_index + 1,
        )
        lines.extend(
            [
                f"Q{q}. Match the term `{first_term}`.",
                "",
                *options,
                "",
            ]
        )
        answers.append(f"Q{q}: {answer}")
        q += 1
        options, answer = mc_block(
            topic["trap"],
            [
                "The concept has an input, operation, output, and later use.",
                f"It connects to {topic['assignment']}.",
                "It can be practiced with matching and sequencing tasks.",
            ],
            topic_index + 2,
        )
        lines.extend(
            [
                f"Q{q}. Select the dangerous misconception.",
                "",
                *options,
                "",
            ]
        )
        answers.append(f"Q{q}: {answer}")
        q += 1
    lines.extend(["# Answer Key", ""])
    lines.extend(answers)
    return "\n".join(lines)


def sequencing_tasks() -> str:
    lines = [
        "# 05 - Sequencing And Pipeline Tasks",
        "",
        "Put the listed items in the correct conceptual order. Answers are at the end.",
        "",
    ]
    answers = []
    for index, topic in enumerate(TOPICS, start=1):
        steps = topic["chain"].split(" -> ")
        scrambled = steps[1::2] + steps[0::2]
        lines.extend(
            [
                f"## S{index} - Lecture {topic['id']} {topic['title']}",
                "",
                "Scrambled steps:",
                "",
            ]
        )
        for step in scrambled:
            lines.append(f"- {step}")
        lines.extend(["", "Correct order:", "", "- [ ] Fill this in without notes.", ""])
        answers.append(f"S{index}: " + " -> ".join(steps))
    lines.extend(["# Answer Key", ""])
    lines.extend(answers)
    return "\n".join(lines)


def diagram_tasks() -> str:
    lines = [
        "# 06 - Diagram Label Tasks",
        "",
        "Use these as drawing or labeling tasks. They avoid vague essays: label the objects and arrows.",
        "",
    ]
    for topic in TOPICS:
        steps = topic["chain"].split(" -> ")
        lines.extend(
            [
                f"## Lecture {topic['id']} - {topic['title']}",
                "",
                "Draw boxes for:",
                "",
            ]
        )
        for step in steps:
            lines.append(f"- {step}")
        lines.extend(
            [
                "",
                "Label arrows with:",
                "",
                "- what changes",
                "- what data is preserved",
                "- what can go wrong",
                "",
                f"Trap label that must appear somewhere: {topic['trap']}",
                "",
            ]
        )
    return "\n".join(lines)


def opengl_debugging() -> str:
    cases = [
        ("Black screen after draw call", "OpenGL state/binding", "Check context, bound VAO/VBO, shader program, viewport, clear color, framebuffer target."),
        ("Object appears but does not move", "Transformations", "Check model/view/projection matrix update and multiplication order."),
        ("Triangle has wrong colors", "Rasterization/shader interpolation", "Check vertex attributes, layout locations, interpolation, and fragment shader output."),
        ("Texture looks blocky or wrong", "Texturing", "Check UV coordinates, texture binding, sampler filtering, wrapping, mipmap completeness, and shader sampler uniform."),
        ("Near object is hidden behind far object", "Visibility", "Check depth buffer creation, depth test enable, depth clear, and depth function."),
        ("Lighting changes when camera moves incorrectly", "Local illumination", "Check normal transformation, coordinate space consistency, light vector, and view vector."),
        ("Shadow appears detached or inverted", "Shadows", "Check light-space transform, depth comparison, bias, and which object acts as occluder or receiver."),
    ]
    lines = [
        "# 07 - OpenGL And Software Debugging Drills",
        "",
        "Closed-format debugging practice. Choose the most likely conceptual area and the first checks.",
        "",
    ]
    answers = []
    for index, (symptom, area, check) in enumerate(cases, start=1):
        lines.extend(
            [
                f"## D{index}. {symptom}",
                "",
                "Choose the best diagnosis:",
                "",
                "A. The issue is most likely only historical background.",
                f"B. The issue belongs to {area}.",
                "C. The issue can be solved by memorizing the slide title.",
                "D. The issue proves rasterization is not involved in rendering.",
                "",
                "First checks:",
                "",
                "- [ ] Write the checks here before looking at the answer.",
                "",
            ]
        )
        answers.append(f"D{index}: B. {check}")
    lines.extend(["# Answer Key", ""])
    lines.extend(answers)
    return "\n".join(lines)


def assignment_workbook() -> str:
    lines = [
        "# 08 - Assignment Workbook",
        "",
    ]
    for ident, title, source, chapters, concepts in ASSIGNMENTS:
        exists = (ROOT / source).exists()
        lines.extend(
            [
                f"## Assignment {ident} - {title}",
                "",
                f"Source text: `{source}`",
                f"Source exists: `{exists}`",
                f"Related lectures: {chapters}",
                f"Core concepts: {concepts}",
                "",
                "Before attempting:",
                "",
                "- [ ] I can name the lecture concepts required.",
                "- [ ] I can explain the relevant pipeline stage.",
                "- [ ] I can identify the likely OpenGL/code object involved.",
                "- [ ] I can predict the expected visible result.",
                "",
                "After attempting:",
                "",
                "- [ ] I can state which concept was tested.",
                "- [ ] I can state what failed when I got stuck.",
                "- [ ] I added the exact gap to `overprep_pack/mistake_log.md`.",
                "",
                "Closed-format self-test:",
                "",
                f"1. This assignment mainly tests: A. {concepts} B. unrelated Moodle navigation C. only memorized dates D. only file naming",
                "2. The best repair action after a mistake is: A. log the exact missing concept B. reread everything randomly C. skip the exercise D. memorize the filename",
                "",
            ]
        )
    return "\n".join(lines)


def final_exam() -> str:
    lines = [
        "# 09 - Final Mixed Closed-Format Exam",
        "",
        "Mixed topics, no chapter hints in the question text. Answers are at the end.",
        "",
    ]
    answers = []
    q = 1
    for topic_index, topic in enumerate(TOPICS, start=1):
        options, answer = mc_block(
            topic["chain"],
            [
                "final image -> arbitrary labels -> unrelated definitions -> memory cleanup",
                "exam score -> lecture title -> Moodle page -> no technical relation",
                "pixels -> source code comments -> no pipeline stages -> final answer",
            ],
            topic_index,
        )
        lines.extend(
            [
                f"Q{q}. Choose the correct chain:",
                "",
                *options,
                "",
            ]
        )
        answers.append(f"Q{q}: {answer} ({topic['title']})")
        q += 1
        term, definition = topic["terms"][2]
        options, answer = mc_block(
            definition,
            [
                topic["trap"],
                "A GitHub repository organization detail.",
                "A non-technical lecture transition.",
            ],
            topic_index + 1,
        )
        lines.extend(
            [
                f"Q{q}. Which definition matches `{term}`?",
                "",
                *options,
                "",
            ]
        )
        answers.append(f"Q{q}: {answer} ({topic['title']})")
        q += 1
    lines.extend(["# Answer Key", ""])
    lines.extend(answers)
    return "\n".join(lines)


def mistake_drills() -> str:
    return """# 10 - Mistake Log Repair Drills

## Repair Template

Topic:
Wrong answer:
Correct answer:
The exact confusion was:
The correct distinction is:
Source file to reread:
Closed-format repair task:
Review date 1:
Review date 2:
Review date 3:

## Convert Mistakes Into Closed-Format Tasks

If the mistake is a confused definition:

- Make a matching pair.
- Add one distractor that is close but wrong.
- Add one sentence explaining the distinction.

If the mistake is a wrong order:

- Make a sequencing task.
- Add the correct pipeline chain.
- Add one trap order that looks plausible but is wrong.

If the mistake is a formula issue:

- Make a fill-in task for variables.
- Make a units task, especially bits vs bytes or coordinate spaces.
- Make one numerical example.

If the mistake is OpenGL/software:

- Write the symptom.
- Choose the likely state, buffer, shader, texture, framebuffer, or depth issue.
- Write the first three checks.

## Minimum Standard

A repaired mistake must become at least one new closed-format question.
"""


def ai_prompt_bank() -> str:
    return """# 11 - AI Prompt Bank For This Course

Use these prompts with the files in this repository.

## Lecture To Exam Chapter

```text
Use only the attached course text unless you clearly mark outside knowledge.
Transform this lecture into a complete exam-oriented chapter for someone who missed the lecture.
Keep every course term.
Explain the missing links between slide bullets.
For every concept, include: problem, data/object, operation, output, next pipeline stage, typical trap, and assignment connection.
Prefer closed-format checks over vague open essay questions.
```

## Assignment To Concept Checklist

```text
Attached assignment text and matching lecture chapter.
Identify the exact lecture concepts required.
Create a checklist of prerequisite knowledge.
Create MC, matching, sequencing, diagram-label, and code-reading questions that test those concepts.
Do not ask broad open questions unless they have a precise answer key.
```

## Mistake Log Repair

```text
Here is my mistake log.
Group the mistakes by concept.
For each concept, generate closed-format repair drills: MC, matching, cloze, sequencing, and one near-miss distractor.
Tell me exactly which lecture reader and assignment source I must revisit.
```
"""


def manifest() -> str:
    data = {
        "pack": "exam_materials",
        "purpose": "reading-first exam preparation materials optimized for closed-format practice",
        "lecture_count": len(TOPICS),
        "assignment_count": len(ASSIGNMENTS),
        "files": [
            "README.md",
            "chapters_bridge/CS8165_all_b1_bridge_chapters.md",
            *[bridge_chapter_filename(topic) for topic in TOPICS],
            "chapters/CS8165_all_exam_chapters.md",
            *[chapter_filename(topic) for topic in TOPICS],
            "chapters_plain/CS8165_all_plain_text_chapters.txt",
            *[plain_chapter_filename(topic) for topic in TOPICS],
            "00_reading_route.md",
            "01_mastery_checklists.md",
            "02_cloze_generator_inputs.md",
            "03_matching_pairs.tsv",
            "03_matching_tasks.md",
            "04_closed_format_drills.md",
            "05_sequencing_and_pipeline_tasks.md",
            "06_diagram_label_tasks.md",
            "07_opengl_debugging_drills.md",
            "08_assignment_workbook.md",
            "09_final_mixed_closed_exam.md",
            "10_mistake_log_repair_drills.md",
            "11_ai_prompt_bank.md",
        ],
        "source_reader_manifest": "lecture_readers/lecture_reader_manifest.json",
        "lecture_pages": sum(item["source_pages"] for item in json.loads((ROOT / "lecture_readers" / "lecture_reader_manifest.json").read_text(encoding="utf-8"))["lectures"]),
        "generated_chapter_count": len(TOPICS),
    }
    return json.dumps(data, indent=2)


def readme() -> str:
    return """# Exam Materials

Reading order:

1. `chapters_bridge/CS8165_all_b1_bridge_chapters.md` or one file from `chapters_bridge/`
2. `chapters_plain/CS8165_all_plain_text_chapters.txt` or one file from `chapters_plain/`
3. `chapters/CS8165_all_exam_chapters.md` or one file from `chapters/`
4. `00_reading_route.md`
5. `01_mastery_checklists.md`
6. `08_assignment_workbook.md`
7. `02_cloze_generator_inputs.md`
8. `03_matching_pairs.tsv` and `03_matching_tasks.md`
9. `05_sequencing_and_pipeline_tasks.md`
10. `04_closed_format_drills.md`
11. `06_diagram_label_tasks.md`
12. `07_opengl_debugging_drills.md`
13. `09_final_mixed_closed_exam.md`
14. `10_mistake_log_repair_drills.md`
15. `11_ai_prompt_bank.md`
"""


def main() -> None:
    ensure_out()
    write("README.md", readme())
    for topic in TOPICS:
        write(bridge_chapter_filename(topic), bridge_chapter_text(topic))
        write(chapter_filename(topic), chapter_text(topic))
        write(plain_chapter_filename(topic), plain_chapter_text(topic))
    write("chapters_bridge/CS8165_all_b1_bridge_chapters.md", combined_bridge_chapters())
    write("chapters/CS8165_all_exam_chapters.md", combined_chapters())
    write("chapters_plain/CS8165_all_plain_text_chapters.txt", combined_plain_chapters())
    write("00_reading_route.md", reading_route())
    write("01_mastery_checklists.md", mastery_checklists())
    write("02_cloze_generator_inputs.md", cloze_inputs())
    write("03_matching_pairs.tsv", matching_pairs())
    write("03_matching_tasks.md", matching_tasks())
    write("04_closed_format_drills.md", closed_format_drills())
    write("05_sequencing_and_pipeline_tasks.md", sequencing_tasks())
    write("06_diagram_label_tasks.md", diagram_tasks())
    write("07_opengl_debugging_drills.md", opengl_debugging())
    write("08_assignment_workbook.md", assignment_workbook())
    write("09_final_mixed_closed_exam.md", final_exam())
    write("10_mistake_log_repair_drills.md", mistake_drills())
    write("11_ai_prompt_bank.md", ai_prompt_bank())
    write("manifest.json", manifest())
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
