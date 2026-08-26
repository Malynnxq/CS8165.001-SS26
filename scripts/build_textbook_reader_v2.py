from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "lecture_readers_v2"
MD_OUT = OUT / "markdown"


LECTURE_02 = {
    "title": "Lecture 02 — The Rendering Pipeline",
    "source": "course_text_parts/03_lectures/02_rendering-pipeline.txt",
    "purpose": (
        "A stand-alone teaching chapter for a student who missed the lecture. "
        "It groups related slides into concepts, defines prerequisites before use, "
        "and explains why each stage exists instead of paraphrasing slide bullets."
    ),
    "sections": [
        {
            "title": "1. The problem rendering has to solve",
            "slides": "2, 5–9",
            "body": [
                "A 3D scene is not an image. In memory, an object is represented by data: positions of vertices, geometric primitives such as triangles, and additional attributes such as colors, normals, or texture coordinates. A display, however, needs a two-dimensional grid of pixel values. Rendering is the process that converts the first representation into the second.",
                "The conversion cannot happen in one step because several different questions have to be answered. Where is each object in the world? Where is the camera? Where does a 3D point appear on the 2D image? Which screen samples are covered by a triangle? If several surfaces compete for the same screen position, which one is visible? What color should the visible surface have? The rendering pipeline exists because these questions are easier and faster to solve as a sequence of specialized stages.",
                "The most useful mental model for this lecture is therefore not a list of OpenGL functions. It is a change of representation: scene data → vertices → primitives → fragments → framebuffer pixels. Each arrow means that some information is transformed, generated, or filtered before the next stage can work on it.",
            ],
            "example": "Imagine one triangle. At first it is only three 3D vertex positions. After transformation and projection, those positions describe where the triangle lies relative to the camera and screen. Rasterization then asks which discrete screen samples lie inside that projected triangle and creates fragment candidates. Visibility and blending rules decide which candidates finally modify the framebuffer.",
            "check": "Why is a fragment only a candidate for a pixel update rather than automatically a final pixel?",
        },
        {
            "title": "2. Application, geometry, and rasterization stages",
            "slides": "6–9",
            "body": [
                "The application stage runs conceptually before the GPU pipeline. It prepares the scene: which objects exist, where they are, how they move, and which data should be sent for rendering. The slides also mention animation, collision detection, and occlusion culling. These are scene-level decisions rather than the later per-fragment work of the rasterizer.",
                "The geometry stage works on geometric descriptions. It transforms vertices between coordinate systems, assembles vertices into primitives, may create additional geometry through tessellation, projects 3D geometry toward the image, and clips geometry that lies outside the relevant viewing region. The key point is that the geometry stage still reasons about points, vertices, and primitives—not pixels.",
                "Rasterization is the bridge from continuous geometry to the discrete image grid. A mathematical triangle covers a continuous region, while the framebuffer contains discrete sample locations. Rasterization determines which samples the projected primitive covers and creates a fragment for each covered sample. Interpolated values such as depth, color, normals, or texture coordinates can travel with each fragment so later processing has local data to work with.",
                "After rasterization, fragments can still be rejected or combined. Depth testing can reject a fragment hidden behind a closer one. Stencil or masking rules can forbid a write. Blending can combine a fragment's color with an existing framebuffer value. This explains the slide statement that only a subset of generated fragments becomes visible pixel updates.",
            ],
            "example": "Two triangles overlap on screen. Rasterization may produce a fragment from each triangle at the same pixel position. If the blue triangle is closer to the camera, the depth test can accept its fragment and reject the red triangle's fragment. Both fragments existed; only one changed the visible result.",
            "check": "What representation is handled before rasterization, and what representation exists immediately after rasterization?",
        },
        {
            "title": "3. OpenGL is an API that controls the pipeline",
            "slides": "10–17",
            "body": [
                "OpenGL is not a scene description language that understands objects such as 'car', 'camera', or 'sun'. It is a graphics API: the application creates resources, changes rendering state, provides shader programs and data, and issues drawing commands. The driver and GPU then execute the requested pipeline work.",
                "This explains why the slides emphasize the OpenGL context. A context contains the rendering state that is currently active. OpenGL is stateful: a draw call depends not only on its explicit arguments but also on which program, buffers, vertex arrays, textures, framebuffer, and tests are active at that moment. A call can therefore be syntactically valid and still draw the wrong thing because the surrounding state is wrong.",
                "The slides compare OpenGL with Vulkan because the two APIs expose different levels of control. OpenGL hides more low-level synchronization and resource management, making the fundamentals easier to learn. Vulkan exposes more explicit control and can reduce overhead in large engines, but the cost is substantially more setup and bookkeeping. For this course, OpenGL is mainly the vehicle for learning the rendering concepts.",
            ],
            "example": "If the correct vertex data exists in GPU memory but the wrong VAO is bound when glDrawArrays is called, OpenGL does not infer what you intended. It renders using the active state. This is why state is part of the input to a draw call.",
            "check": "Why can two identical glDrawArrays calls produce different images when executed under different OpenGL state?",
        },
        {
            "title": "4. Why modern OpenGL stores geometry on the GPU",
            "slides": "21–33",
            "body": [
                "Older immediate-mode OpenGL allowed an application to send vertex commands while drawing. The slides point out the performance problem: geometry had to cross from CPU-side application memory toward the GPU repeatedly. Modern OpenGL instead encourages the application to upload reusable vertex data once and draw from GPU-resident buffers many times.",
                "A Vertex Buffer Object (VBO) stores raw vertex data in GPU-accessible buffer memory. A Vertex Array Object (VAO) stores the description of how vertex attributes should be interpreted for drawing. The distinction is important: a VBO answers 'what bytes are stored?', while the VAO records how those bytes are connected to vertex attribute inputs.",
                "glBufferData allocates buffer storage and optionally copies data into it. glVertexAttribPointer describes an attribute layout: which attribute index is being supplied, how many components each vertex has, what the component type is, how far apart consecutive vertices are in memory (stride), and where the attribute starts (offset). glEnableVertexAttribArray activates that attribute source.",
                "The stride/offset idea becomes essential when several attributes are interleaved. A vertex might be stored as position followed by color: x,y,z,r,g,b, then the next vertex. The position attribute and color attribute read from the same buffer with the same stride but different offsets.",
            ],
            "example": "For vertices stored as [x,y,z,r,g,b], each vertex occupies six floats. Position can use size=3, stride=6*sizeof(float), offset=0; color can use size=3, the same stride, and offset=3*sizeof(float). The buffer is the same; the interpretation differs.",
            "check": "What information belongs to a VBO, and what information is configured through the VAO/vertex attribute layout?",
        },
        {
            "title": "5. What a draw call actually triggers",
            "slides": "27–36",
            "body": [
                "glDrawArrays does not itself contain the complete scene. Its arguments say how to interpret a sequence of vertex records as primitives, but the actual work depends on the active program, vertex array configuration, buffers, and pipeline state. For GL_TRIANGLES, groups of three vertices are assembled into triangles; other primitive modes assemble points, lines, strips, loops, or patches differently.",
                "Once a draw call starts, the data moves into the rendering pipeline. Programmable stages run shader code; fixed-function stages perform standardized operations such as primitive assembly, clipping, rasterization, interpolation, and fragment tests. The division matters because some behavior is controlled by your GLSL code while other behavior is controlled by API state.",
                "A vertex shader runs for vertex inputs and must ultimately produce a clip-space position in gl_Position. Values it outputs can later be interpolated across a primitive. After vertex processing and primitive assembly, clipping removes or cuts geometry outside the clip volume, and rasterization creates fragments for the surviving projected primitives.",
            ],
            "example": "If the triangle shape is correct but its color is wrong, the vertex positions and primitive assembly may already be working. The bug becomes more likely to be in an attribute connection, interpolation, fragment shader, texture input, or later blending state. The pipeline becomes a debugging map.",
            "check": "Which parts of the pipeline are programmable by shaders, and which important operations remain fixed-function?",
        },
        {
            "title": "6. Fragment processing and the framebuffer",
            "slides": "Sections 2.5–2.6",
            "body": [
                "A fragment represents a candidate contribution at a framebuffer sample. It can carry a computed color, depth, and other values, but the framebuffer is not changed until the relevant tests and operations permit the write.",
                "The depth buffer stores depth information used to decide which surface is nearer at a sample. The stencil buffer can support masking and more complex acceptance rules. Blending combines a new fragment value with the color already stored, which is especially important for transparency-like effects. Color masks or scissor tests can further restrict writes.",
                "The framebuffer is therefore the destination of rendering, not merely another intermediate object. It contains attachments such as color, depth, or stencil buffers. The image displayed in a window ultimately comes from a color attachment after the pipeline has resolved all of the candidate contributions.",
            ],
            "example": "A fragment shader can output bright green, yet nothing visible appears if the fragment fails the depth test or if color writes are disabled. 'The fragment shader ran' and 'the framebuffer changed' are different statements.",
            "check": "Name two reasons a valid fragment-shader output might never become a visible framebuffer color.",
        },
        {
            "title": "7. Put the entire chain together",
            "slides": "2, 35–36 and the chapter as a whole",
            "body": [
                "Start with application-side scene data. Upload reusable vertex attributes into buffers and configure how those bytes map to shader inputs. Bind the relevant OpenGL state and issue a draw call. Vertex processing transforms the incoming vertices. Primitive assembly groups them into geometric primitives. Clipping keeps the part relevant to the viewing volume. Rasterization converts projected primitives into fragment candidates. Fragment processing computes candidate values. Fragment tests and operations decide whether and how those candidates update framebuffer attachments. The framebuffer then contains the raster image that can be presented to the display.",
                "This chain is the conceptual backbone for the rest of the course. Later lectures zoom into individual arrows: transformations explain how vertices move between coordinate systems; projection explains the camera-to-image mapping; clipping explains boundary handling; rasterization explains sample generation; visibility explains which candidates are seen; illumination and texturing explain how colors are computed; shadows reuse visibility from the light's point of view.",
                "When learning later chapters, always ask two questions: What representation enters this operation? What representation leaves it? If you can answer those questions, the many algorithms and OpenGL calls stop being isolated facts and become parts of one system.",
            ],
            "example": "One triangle's story is: CPU-side vertex array → GPU buffer → vertex shader inputs → transformed vertices → triangle primitive → clipped/projected triangle → rasterized fragments → fragment-shader outputs → depth/blending decisions → framebuffer pixels.",
            "check": "Explain the complete life of one triangle from CPU-side data to a visible pixel without using the slide deck.",
        },
    ],
}


def render_markdown(lecture: dict) -> str:
    lines = [
        f"# {lecture['title']}",
        "",
        f"Source: `{lecture['source']}`",
        "",
        lecture["purpose"],
        "",
        "## How this reader differs from the old version",
        "",
        "This reader does **not** create one generic explanation per slide. Related slides are grouped into one teaching sequence. New terms are defined before they are relied on, and examples are used to make abstract stages concrete.",
        "",
    ]
    for section in lecture["sections"]:
        lines.extend([f"## {section['title']}", "", f"Based on slides: {section['slides']}", ""])
        for paragraph in section["body"]:
            lines.extend([paragraph, ""])
        lines.extend(["### Concrete example", "", section["example"], "", "### Check yourself", "", section["check"], ""])
    lines.extend([
        "## Minimum concept map",
        "",
        "`scene data → GPU vertex data → vertices → primitives → clipping/projection → rasterization → fragments → fragment tests/operations → framebuffer → displayed image`",
        "",
        "If one arrow in this chain is unclear, revisit the corresponding section before memorizing OpenGL function names.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    MD_OUT.mkdir(parents=True, exist_ok=True)
    output = MD_OUT / "02_rendering-pipeline_textbook.md"
    output.write_text(render_markdown(LECTURE_02), encoding="utf-8")
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
