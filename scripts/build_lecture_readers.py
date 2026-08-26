from __future__ import annotations

import html
import json
import re
import shutil
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "lecture_readers"
MD_OUT = OUT / "markdown"
PDF_OUT = OUT / "pdf"


LECTURES = [
    {
        "id": "01",
        "title": "Introduction",
        "source": "course_text_parts/03_lectures/01_introduction.txt",
        "opening": "This lecture is the orientation layer for the whole course. It explains why interactive computer graphics is a pipeline problem: a scene must be represented, processed under time constraints, sampled into an image, and displayed fast enough for interaction.",
        "sections": [
            {
                "title": "Course Organization",
                "slides": "Slides around 6-15",
                "commentary": [
                    "The organizational slides matter because they explain how the theory and programming parts fit together. The exercises are not separate from the lecture; they are the practical version of the same pipeline ideas. When the course says that slides are generally not self-explanatory, that is a warning: the bullet points are anchors, not a textbook.",
                    "Treat every exercise sheet as an applied checkpoint. Rendering pipeline, primitive types, shaders, transformations, projection, clipping, and rasterization are introduced in the lectures and then turned into OpenGL tasks. If a topic appears both in a lecture and an exercise, it is more likely to be exam relevant.",
                ],
                "mental_model": "Lecture slides give the vocabulary; exercises force you to connect that vocabulary to code and visible output.",
                "check": "Can you list the five exercise themes and connect each one to a later lecture chapter?",
            },
            {
                "title": "Computer Graphics Overview",
                "slides": "Section 1.2",
                "commentary": [
                    "Computer graphics is about generating images from descriptions. The description can be pixel-based, object-based, physically motivated, artistic, or algorithmic. The common thread is that the computer must decide what color belongs at image samples.",
                    "Interactive graphics adds a time constraint. The image is not computed once and admired; it must respond to camera motion, user input, animation, and changing state. That is why real-time rendering often uses approximations and specialized GPU stages.",
                ],
                "mental_model": "Graphics is controlled image generation. Interactive graphics is controlled image generation under a strict time budget.",
                "check": "What changes when a renderer must be interactive rather than offline?",
            },
            {
                "title": "Pixel-Based Representations",
                "slides": "Section 1.3",
                "commentary": [
                    "A pixel-based representation stores an image directly as samples on a grid. It is easy to display and edit locally, but it does not know the underlying 3D scene. If you zoom into a raster image, you reveal the sampling grid, not more geometry.",
                    "This is the first place where sampling becomes important. Resolution, color depth, aliasing, and frame time are not cosmetic details. They decide what information can be represented and how much data must be processed per second.",
                ],
                "mental_model": "A raster image is already the answer. It contains color samples, not the geometric reasons behind them.",
                "check": "Why can a pixel image be easy to display but hard to reinterpret as a 3D scene?",
            },
            {
                "title": "3D Models",
                "slides": "Section 1.4",
                "commentary": [
                    "A 3D model is a structured description of objects before they become pixels. It may contain vertices, primitives, topology, normals, materials, textures, and transformations. Unlike a pixel image, it can be viewed from different camera positions.",
                    "The course mostly follows object-based rendering: start from model data, transform it, project it, rasterize it, shade it, test visibility, and finally update pixels. Later chapters explain these steps one by one.",
                ],
                "mental_model": "A model is not an image. It is a cause from which many possible images can be generated.",
                "check": "Which model attributes can influence final color besides vertex positions?",
            },
            {
                "title": "Algorithmic Paradigms",
                "slides": "Section 1.5",
                "commentary": [
                    "The lecture contrasts ways to generate images. Rasterization works from objects toward pixels and is the dominant real-time pipeline. Ray-based methods work from image samples into the scene and are powerful for visibility and lighting but can be more expensive.",
                    "Do not memorize these paradigms as names only. Ask what direction information flows. Does the algorithm start from geometry and find covered pixels, or from pixels/rays and find visible geometry? That direction explains the strengths and weaknesses.",
                ],
                "mental_model": "Rasterization asks, 'Which samples does this primitive cover?' Ray casting asks, 'What does this sample see?'",
                "check": "Which paradigm fits OpenGL's standard real-time pipeline most directly?",
            },
        ],
    },
    {
        "id": "02",
        "title": "Rendering Pipeline",
        "source": "course_text_parts/03_lectures/02_rendering-pipeline.txt",
        "opening": "This lecture turns the vague idea of rendering into a concrete sequence. It is the most important debugging map in the course: if an image is wrong, the pipeline tells you where the error could have entered.",
        "sections": [
            {
                "title": "Rendering Process",
                "slides": "Section 2.1",
                "commentary": [
                    "Object-based rendering starts with scene objects represented as primitives. The pipeline transforms vertices, assembles primitives, rasterizes them into fragments, and lets only some fragments become pixels. The important detail is that the representation changes at every stage.",
                    "The application stage prepares data and state. The geometry stage handles positions and primitives. The rasterization stage creates fragments and applies fragment operations. This separation helps you explain both theory questions and black-screen OpenGL bugs.",
                ],
                "mental_model": "Vertices become primitives, primitives become fragments, and fragments compete to become pixel updates.",
                "check": "What is the difference between a fragment and a final pixel?",
            },
            {
                "title": "OpenGL Overview",
                "slides": "Section 2.2",
                "commentary": [
                    "OpenGL is an API for controlling a graphics pipeline. It is not a renderer by itself in the sense of a single command that understands your scene. You create a context, provide buffers, set state, compile shaders, bind objects, and issue draw calls.",
                    "Modern OpenGL is stateful and shader-based. Many errors happen because the programmer assumes that a later call carries more information than it really does. The GPU uses the currently bound objects and current state at draw time.",
                ],
                "mental_model": "OpenGL draw calls consume the state machine as it exists right now.",
                "check": "Why can binding the wrong vertex array or shader program produce a valid draw call with wrong output?",
            },
            {
                "title": "OpenGL Rendering",
                "slides": "Section 2.3",
                "commentary": [
                    "Older OpenGL exposed a fixed-function style where many transformations and lighting choices were configured through predefined calls. Modern OpenGL expects you to write shader programs and explicitly manage data flow.",
                    "This is not just historical trivia. It explains why shader code, vertex attributes, uniforms, and buffer objects are central in the exercises. If the shader expects an attribute and the vertex layout does not provide it, the pipeline has no magic fallback.",
                ],
                "mental_model": "Modern OpenGL makes the data path explicit; that gives control but also creates responsibility.",
                "check": "Which data usually goes into vertex attributes, and which data usually goes into uniforms?",
            },
            {
                "title": "OpenGL Rendering Pipeline",
                "slides": "Section 2.4",
                "commentary": [
                    "The vertex shader runs per vertex and usually outputs clip-space position plus attributes for later interpolation. Primitive assembly groups vertices into points, lines, or triangles. Clipping handles geometry outside the view volume. Rasterization creates fragments.",
                    "The fragment shader computes candidate fragment output, often using interpolated attributes, uniforms, and textures. After that, tests and operations such as depth testing, stencil testing, blending, and masking decide what reaches the framebuffer.",
                ],
                "mental_model": "Programmable shaders compute values; fixed pipeline stages decide coverage, interpolation, tests, and output rules.",
                "check": "If your geometry appears in wireframe but colors are wrong, which stages become suspicious?",
            },
            {
                "title": "Fragment Tests, Framebuffer, and Pixel-Based Rendering",
                "slides": "Sections 2.5-2.7",
                "commentary": [
                    "Fragment tests are the gatekeepers after shading. A fragment can have a perfectly valid color and still fail because depth, stencil, scissor, masking, or blending state prevents a visible update. This is why final pixels are a subset of generated fragments.",
                    "The framebuffer stores the final render targets: color buffers, depth buffers, stencil buffers, or custom attachments. Pixel-based rendering starts from image data instead of geometric primitives, which is useful for image processing but conceptually different from the object-to-pixel pipeline.",
                ],
                "mental_model": "The framebuffer is the destination; fragment operations are the rules for writing into it.",
                "check": "Why can two fragments with different colors produce only one visible pixel color?",
            },
        ],
    },
    {
        "id": "03",
        "title": "Geometric Transformations",
        "source": "course_text_parts/03_lectures/03_geometric-transformations.txt",
        "opening": "This lecture explains how geometry moves between coordinate systems. Almost every later topic assumes that you can track where a point or vector currently lives.",
        "sections": [
            {
                "title": "Mathematical Foundations",
                "slides": "Section 3.1",
                "commentary": [
                    "The lecture uses vectors and matrices to express geometric operations. A vector can represent a point position, a direction, an offset, or an attribute depending on context. A matrix expresses a linear map or, with homogeneous coordinates, an affine transformation.",
                    "The central exam habit is to name the coordinate space. A point in model coordinates and a light direction in view coordinates cannot be mixed safely. Many visual bugs are coordinate-space bugs.",
                ],
                "mental_model": "A numeric vector is incomplete until you know what coordinate system it belongs to.",
                "check": "Why is a normal vector not transformed exactly like a point under all transformations?",
            },
            {
                "title": "Affine Transformations",
                "slides": "Section 3.2",
                "commentary": [
                    "Affine transformations include translation, rotation, scaling, shearing, and combinations of these. Homogeneous coordinates allow translation to be represented in matrix form together with other transformations.",
                    "Translation moves positions but not pure directions. Rotation changes orientation while preserving lengths if it is a proper rotation. Scaling can change lengths and can also affect normals. These distinctions matter later in lighting.",
                ],
                "mental_model": "Use 4D homogeneous coordinates so that a single matrix pipeline can move 3D points through the scene.",
                "check": "What does the homogeneous w component let a transformation matrix express?",
            },
            {
                "title": "Composition of Transformations",
                "slides": "Section 3.3",
                "commentary": [
                    "Composition means applying several transformations in sequence. The order matters because matrix multiplication is generally not commutative. Rotating an object around its own origin and then translating it is different from translating it and then rotating around the world origin.",
                    "When you read a formula such as projection * view * model * position, read it from right to left for the point: first model, then view, then projection. The resulting matrix chain is compact, but the conceptual steps remain separate.",
                ],
                "mental_model": "Matrix chains are compressed stories of movement through coordinate spaces.",
                "check": "Why can swapping model and view matrices destroy the intended camera/object relation?",
            },
            {
                "title": "Coordinate System Change",
                "slides": "Section 3.4",
                "commentary": [
                    "A transformation can be read actively as moving an object, or passively as changing the coordinate frame used to describe it. Both interpretations are valid, but mixing them carelessly causes sign and order errors.",
                    "The view matrix is a classic example: conceptually you position a camera, but the pipeline usually transforms the world by the inverse of the camera transform so that the camera becomes the origin of view space.",
                ],
                "mental_model": "Moving the camera one way is equivalent to moving the world the opposite way for rendering.",
                "check": "Why is the view transform often related to the inverse camera transform?",
            },
            {
                "title": "Transformations in OpenGL",
                "slides": "Section 3.5",
                "commentary": [
                    "Modern OpenGL does not automatically manage the old matrix stacks. You usually compute model, view, and projection matrices in application code and pass them to shaders as uniforms.",
                    "The vertex shader is where the final clip-space position is normally computed. That means a wrong matrix uniform, wrong multiplication order, or wrong convention can make geometry vanish even though buffers and draw calls are correct.",
                ],
                "mental_model": "The shader is the place where abstract transformation math becomes GPU execution.",
                "check": "Which matrix would you inspect first if an object follows the camera instead of staying in the world?",
            },
        ],
    },
    {
        "id": "04",
        "title": "Geometric Projection",
        "source": "course_text_parts/03_lectures/04_geometric-projection.txt",
        "opening": "This lecture explains how a 3D view becomes a 2D image. Projection is where camera geometry, homogeneous coordinates, clipping planes, depth precision, and viewport mapping meet.",
        "sections": [
            {
                "title": "Linear Perspective and Planar Projections",
                "slides": "Sections 4.1-4.2",
                "commentary": [
                    "Perspective projection models the visual effect that farther objects appear smaller. Orthographic projection removes this distance-based size change and keeps parallel lines parallel. Both are useful, but they communicate different spatial relationships.",
                    "Planar projection means mapping points onto an image plane. The lecture's art examples are not decoration; they show that projection is a geometric rule for constructing an image from a viewpoint.",
                ],
                "mental_model": "Projection is the rule that turns 3D positions into image-plane positions.",
                "check": "What visual cue does perspective projection add that orthographic projection lacks?",
            },
            {
                "title": "Camera Modeling",
                "slides": "Section 4.3",
                "commentary": [
                    "A virtual camera is defined by position, orientation, projection type, viewing volume, and image/viewport settings. The view transform places the world relative to the camera. The projection transform maps that view into clip coordinates.",
                    "Near and far clipping planes are part of the camera model. They decide what range of depths is represented and strongly affect depth buffer precision. A careless near/far setup can create z-fighting even if the scene geometry is correct.",
                ],
                "mental_model": "A camera is not only an eye position; it is also a volume and a mapping rule.",
                "check": "Why can changing the near plane affect depth artifacts?",
            },
            {
                "title": "Specifying Projections in OpenGL",
                "slides": "Section 4.4",
                "commentary": [
                    "In OpenGL, projection is usually encoded in a projection matrix sent to a shader. The matrix maps view-space coordinates to clip space. Clipping and the perspective divide then lead toward normalized device coordinates.",
                    "Aspect ratio and field of view must match the intended viewport. If the aspect ratio is wrong, objects appear stretched. If the field of view is extreme, the image can look distorted even though the math is functioning.",
                ],
                "mental_model": "The projection matrix is the camera lens encoded as linear algebra in homogeneous coordinates.",
                "check": "What symptom suggests that the projection aspect ratio does not match the window?",
            },
            {
                "title": "Orthographic and Perspective Derivations",
                "slides": "Sections 4.5-4.6",
                "commentary": [
                    "The derivations are there to explain where the matrix entries come from. Orthographic projection maps a box-shaped view volume into normalized coordinates. Perspective projection maps a frustum and uses the homogeneous component for the later divide.",
                    "You do not need to treat these matrices as random formulas. Each part maps a coordinate range into a standard range. The perspective matrix additionally arranges w so that the perspective divide creates foreshortening.",
                ],
                "mental_model": "Projection matrices normalize a viewing volume; perspective also prepares the divide by w.",
                "check": "What does the perspective divide do to x and y coordinates?",
            },
            {
                "title": "Viewport Transformation",
                "slides": "Section 4.7",
                "commentary": [
                    "After normalized device coordinates, the viewport transform maps the normalized range to actual window coordinates. This is the last geometric mapping before rasterization uses the target grid.",
                    "Separating projection from viewport mapping helps debugging. A wrong projection can produce wrong normalized coordinates; a wrong viewport can map otherwise valid coordinates into the wrong part of the window.",
                ],
                "mental_model": "Projection decides normalized position; viewport decides where that position lands on the screen.",
                "check": "Why is resizing a window related to both viewport and projection settings?",
            },
        ],
    },
    {
        "id": "05",
        "title": "Clipping",
        "source": "course_text_parts/03_lectures/05_clipping.txt",
        "opening": "This lecture focuses on algorithms that remove or trim geometry against boundaries. Clipping is a geometric operation before rasterization, not a visibility test between overlapping objects.",
        "sections": [
            {
                "title": "Cohen-Sutherland Line Clipping",
                "slides": "Section 5.1",
                "commentary": [
                    "Cohen-Sutherland assigns outcodes to line endpoints based on which side of the clipping window they lie on. These codes allow quick accept, quick reject, or partial clipping. The algorithm is efficient because many cases are decided before computing intersections.",
                    "The exam-friendly idea is the logic of region codes: if both endpoints are inside, keep the segment. If the bitwise AND of the outcodes is nonzero, both endpoints share an outside region and the segment can be rejected. Otherwise, compute an intersection and continue.",
                ],
                "mental_model": "Outcodes are a cheap classification before doing intersection math.",
                "check": "What does a nonzero bitwise AND of two endpoint outcodes imply?",
            },
            {
                "title": "Cyrus-Beck Line Clipping",
                "slides": "Section 5.2",
                "commentary": [
                    "Cyrus-Beck treats the line parametrically and clips against convex boundaries. Instead of repeatedly using region codes, it finds entering and leaving parameter values along the line.",
                    "The key is to reason about the line parameter t. A clipped line segment is not a new unrelated line; it is a restricted interval of the original parametric line. Boundary tests shrink that interval.",
                ],
                "mental_model": "Clipping a parametric line means narrowing the valid t interval.",
                "check": "Why does Cyrus-Beck naturally require convex clipping regions?",
            },
            {
                "title": "Sutherland-Hodgman Polygon Clipping",
                "slides": "Section 5.3",
                "commentary": [
                    "Sutherland-Hodgman clips a polygon against one boundary at a time. For each edge of the polygon, it decides whether vertices are inside or outside and emits zero, one, or two vertices depending on transitions across the boundary.",
                    "This algorithm is easiest to understand as a stream processor. Feed in a polygon, clip it against the left boundary, feed the result into the right boundary, and so on. Each boundary can add intersection vertices.",
                ],
                "mental_model": "Polygon clipping is repeated edge-by-edge filtering plus intersection insertion.",
                "check": "When can polygon clipping increase the number of vertices?",
            },
            {
                "title": "Weiler-Atherton and Greiner-Hormann",
                "slides": "Sections 5.4-5.5",
                "commentary": [
                    "These algorithms address more complex polygon clipping scenarios, especially when polygon relationships are not as simple as convex-window clipping. They organize intersections and traversal rules to produce correct output boundaries.",
                    "For preparation, focus on why simpler algorithms are not enough. Complex polygon intersection can require following alternating boundaries of subject and clipping polygons. That is a topology problem, not only a line-intersection problem.",
                ],
                "mental_model": "Complex polygon clipping is about traversing boundary networks after intersections are known.",
                "check": "Why are intersection ordering and traversal rules important for polygon clipping?",
            },
        ],
    },
    {
        "id": "06",
        "title": "Rasterization",
        "source": "course_text_parts/03_lectures/06_rasterization.txt",
        "opening": "This lecture explains how continuous primitives become discrete fragments on a grid. Rasterization is the bridge from geometric descriptions to sample-based image generation.",
        "sections": [
            {
                "title": "Line Rasterization",
                "slides": "Section 6.1",
                "commentary": [
                    "A mathematical line has infinitely many points, but a raster display has a finite grid. Line rasterization decides which grid cells or samples best approximate the ideal line. The algorithm must balance accuracy, speed, and consistency.",
                    "Incremental algorithms avoid recomputing expensive formulas for every pixel. The important idea is to step along one axis and update an error term that decides when to step along the other axis.",
                ],
                "mental_model": "Rasterizing a line means approximating a continuous path by grid decisions.",
                "check": "Why are incremental error updates useful in line rasterization?",
            },
            {
                "title": "Triangle Edge Rasterization",
                "slides": "Section 6.2",
                "commentary": [
                    "Triangles are the core primitive in real-time rendering. Edge functions or half-space tests decide whether a sample lies inside the triangle. This allows the rasterizer to test coverage systematically.",
                    "Coverage is not final visibility. A covered sample becomes a fragment candidate. Depth testing, stencil testing, blending, and other operations still decide whether the framebuffer changes.",
                ],
                "mental_model": "Triangle rasterization answers the question: which samples are inside this projected triangle?",
                "check": "What later stage can reject a fragment after triangle coverage succeeds?",
            },
            {
                "title": "Region Filling",
                "slides": "Section 6.3",
                "commentary": [
                    "Region filling generalizes the idea of determining interior samples. The algorithm must identify connected areas or spans that should receive color. This connects rasterization to scan conversion and image-space reasoning.",
                    "The practical issue is avoiding gaps, double fills, or inconsistent boundary handling. Small choices at edges can become visible artifacts when many primitives meet.",
                ],
                "mental_model": "Filling is about turning boundary descriptions into consistent interior samples.",
                "check": "Why can inconsistent edge rules create cracks between adjacent primitives?",
            },
            {
                "title": "Scanline-Based Triangle Rasterization",
                "slides": "Section 6.4",
                "commentary": [
                    "Scanline rasterization processes horizontal rows of the image. For each row that crosses a triangle, the algorithm finds the covered interval and fills the span. Attribute interpolation can be updated along edges and across each span.",
                    "The method is intuitive because it follows the memory layout of many images. It also demonstrates why interpolation is tied to rasterization: once you know a sample location inside the primitive, you can interpolate depth, color, normals, or texture coordinates.",
                ],
                "mental_model": "Each scanline asks: where does this triangle enter and leave this row?",
                "check": "Which attributes might be interpolated while filling triangle spans?",
            },
            {
                "title": "Tile-Based Triangle Rasterization",
                "slides": "Section 6.5",
                "commentary": [
                    "Tile- or block-based approaches group pixels into small regions. This can improve locality and parallel work distribution. Modern GPUs often reason in blocks or tiles internally because rendering is massively parallel.",
                    "For the exam, connect this to efficiency. The mathematical goal is still coverage, but the implementation is organized to use hardware resources well.",
                ],
                "mental_model": "Block-based rasterization keeps the same coverage problem but changes the work organization.",
                "check": "Why is block organization attractive for parallel graphics hardware?",
            },
        ],
    },
    {
        "id": "07",
        "title": "Visibility Determination",
        "source": "course_text_parts/03_lectures/07_visibility-determination.txt",
        "opening": "This lecture asks which surfaces are visible from a viewpoint. Rasterization can generate many fragment candidates, but visibility decides which ones should affect the image.",
        "sections": [
            {
                "title": "Object-Based Algorithms",
                "slides": "Section 7.1",
                "commentary": [
                    "Object-based visibility algorithms reason about geometry before or while comparing surfaces. They can sort, split, or reject objects based on spatial relations. This is different from simply letting every fragment fight in the depth buffer.",
                    "The value of object-based reasoning is reducing work or establishing correct order. The difficulty is that geometry can overlap in complicated ways, so simple global ordering is not always possible.",
                ],
                "mental_model": "Object-based visibility tries to solve visibility with geometry before final pixels are written.",
                "check": "Why can intersecting polygons make simple depth sorting fail?",
            },
            {
                "title": "Binary Space Partitioning",
                "slides": "Section 7.2",
                "commentary": [
                    "A BSP tree recursively divides space with planes. Once built, it can help traverse geometry in a view-dependent order. This is useful for visibility and ordering because the tree encodes spatial relationships.",
                    "The cost is preprocessing and possible splitting of geometry. BSP is a good example of trading memory and setup work for faster or more structured visibility decisions later.",
                ],
                "mental_model": "A BSP tree stores a recursive answer to 'which side of this plane is the geometry on?'",
                "check": "Why can building a BSP tree require splitting polygons?",
            },
            {
                "title": "Warnock Algorithm",
                "slides": "Section 7.3",
                "commentary": [
                    "Warnock's algorithm works in image space by subdividing regions until visibility is simple enough to decide. If a region is ambiguous, split it. If it is simple, fill it.",
                    "This illustrates a general graphics strategy: recursively reduce a hard global problem into smaller local problems. The algorithm is less central in modern OpenGL practice than the depth buffer, but it helps contrast image-space and object-space approaches.",
                ],
                "mental_model": "When a region is too complicated, subdivide until the answer becomes simple.",
                "check": "What makes Warnock's algorithm image-space rather than object-space?",
            },
            {
                "title": "Depth Buffer Algorithm",
                "slides": "Section 7.4",
                "commentary": [
                    "The depth buffer stores the closest accepted depth at each sample or pixel. For each fragment, compare its depth to the stored depth. If it passes, update the color and depth; otherwise discard it.",
                    "The strength of the depth buffer is simplicity and hardware efficiency. The weakness is precision: depth values are finite, and projection distributes precision unevenly. Bad near/far settings can create z-fighting.",
                ],
                "mental_model": "The depth buffer is a per-sample competition for closest visible fragment.",
                "check": "Why should the near plane not be unnecessarily close to the camera?",
            },
            {
                "title": "Depth Extensions and Ray Casting",
                "slides": "Sections 7.5-7.6",
                "commentary": [
                    "Depth buffer extensions refine or adapt depth-based visibility, for example by handling precision, transparency, or multiple layers more carefully. Standard depth testing alone is not a complete solution for every visibility situation.",
                    "Ray casting takes the opposite direction from rasterization: for each image sample, cast a ray into the scene and find the closest intersection. This naturally solves primary visibility but requires intersection work instead of raster coverage work.",
                ],
                "mental_model": "Rasterization pushes primitives to pixels; ray casting pulls visibility from pixels into the scene.",
                "check": "Why is transparency harder than opaque nearest-surface visibility?",
            },
        ],
    },
    {
        "id": "08",
        "title": "Local Illumination",
        "source": "course_text_parts/03_lectures/08_local-illumination.txt",
        "opening": "This lecture explains how visible surface points receive color from local light, material, normal, and view information. It is about shading a point, not solving all global light transport.",
        "sections": [
            {
                "title": "Physics of Light",
                "slides": "Section 8.1",
                "commentary": [
                    "The physics slides provide intuition for light as energy interacting with surfaces. For this course, the goal is not full physical simulation but a usable model for real-time rendering.",
                    "Important terms are reflection, absorption, wavelength/color, intensity, and direction. These terms become shader inputs or material parameters later. The simplified model must still preserve the relation between light direction, surface orientation, and observed brightness.",
                ],
                "mental_model": "Shading is an approximation of light-surface interaction that is cheap enough for rendering.",
                "check": "Why does surface orientation affect diffuse brightness?",
            },
            {
                "title": "Light Sources",
                "slides": "Section 8.2",
                "commentary": [
                    "Light source models define where light comes from and how its direction and intensity are computed. Directional lights approximate distant sources with parallel rays. Point lights emit from a position and often include attenuation. Spotlights add a directional cone.",
                    "In shader code, the type of light determines how you compute the light vector. A directional light can use a fixed direction; a point light requires subtracting the surface position from the light position.",
                ],
                "mental_model": "Different light types mainly change how the light direction and intensity are computed at the surface point.",
                "check": "What is the difference between a directional light vector and a point light vector?",
            },
            {
                "title": "Material Models",
                "slides": "Section 8.3",
                "commentary": [
                    "A material model tells the shader how a surface responds to light. Diffuse material scatters light broadly; specular material creates view-dependent highlights; ambient terms approximate background illumination.",
                    "Material coefficients are not arbitrary decoration. They scale the contribution of each lighting term. If the specular coefficient is zero, the surface should not show a specular highlight under that model.",
                ],
                "mental_model": "Light asks what arrives; material answers how the surface reacts.",
                "check": "Which material parameter would you adjust to reduce shiny highlights?",
            },
            {
                "title": "Phong Illumination Model",
                "slides": "Section 8.4",
                "commentary": [
                    "The Phong illumination model combines ambient, diffuse, and specular terms. Diffuse lighting uses the angle between normal and light direction. Specular lighting also depends on the viewer because highlights move with the view direction.",
                    "The formula is less important than the decomposition. Ambient is a rough constant approximation. Diffuse is orientation-dependent matte reflection. Specular is view-dependent shininess. A correct answer should name the vectors and normalize them.",
                ],
                "mental_model": "Phong-style lighting is a sum of simple terms, each modeling a different visual effect.",
                "check": "Why does the specular term depend on the view direction?",
            },
            {
                "title": "Shading",
                "slides": "Section 8.5",
                "commentary": [
                    "Shading decides where the illumination calculation is evaluated and how results are interpolated. Flat shading uses one value per primitive. Gouraud shading evaluates at vertices and interpolates colors. Phong shading interpolates normals and evaluates lighting per fragment.",
                    "Per-fragment shading is more expensive but can represent highlights more accurately. This connects directly to the pipeline: interpolation during rasterization provides the data used by the fragment shader.",
                ],
                "mental_model": "The shading method decides what is computed at vertices and what is computed at fragments.",
                "check": "Why can Gouraud shading miss a small specular highlight?",
            },
        ],
    },
    {
        "id": "09",
        "title": "Texturing",
        "source": "course_text_parts/03_lectures/09_texturing.txt",
        "opening": "This lecture treats textures as sampled data for shading, not merely images glued onto objects. It connects UV coordinates, sampling, filtering, mipmaps, OpenGL texture state, and advanced texture uses.",
        "sections": [
            {
                "title": "Texture Objects, Texels, Formats, and Color Space",
                "slides": "Section 9.1",
                "commentary": [
                    "A texture object stores sampled data on the GPU. A texel is one stored texture sample. The texture format decides what channels and numeric representation the samples use. Color space matters because color values may be stored nonlinearly, especially for sRGB images.",
                    "The key shift is to stop thinking of texture as only a picture. Textures can store color, normals, depth, lookup data, environment information, or volume data. The shader decides how the sampled values are interpreted.",
                ],
                "mental_model": "A texture is a GPU-accessible sampled data field.",
                "check": "Why can the same texture mechanism store both color maps and normal maps?",
            },
            {
                "title": "Texture Coordinates, UV Mapping, and Wrapping",
                "slides": "Section 9.2",
                "commentary": [
                    "Texture coordinates map surface points to locations in texture space. UV coordinates are usually interpolated across primitives during rasterization and then used by the fragment shader to sample a texture.",
                    "Wrapping rules decide what happens outside the normal coordinate range. Repeat, clamp, mirrored repeat, and border behavior are not visual afterthoughts; they define the sampling function outside the base domain.",
                ],
                "mental_model": "UVs are the address system that lets a fragment look up texture data.",
                "check": "What artifact might appear if a wrapping mode is wrong at the edge of a surface?",
            },
            {
                "title": "Sampling, Filtering, Mipmaps, and Anisotropy",
                "slides": "Section 9.3",
                "commentary": [
                    "Sampling turns continuous texture coordinates into values from discrete texels. Nearest filtering selects a nearby texel and can look blocky. Linear filtering blends nearby texels and looks smoother. Minification is harder because many texels may map to one pixel.",
                    "Mipmaps store prefiltered lower-resolution versions of a texture. They reduce aliasing and shimmer when textures are seen at small scale. Anisotropic filtering improves quality when a texture is viewed at a steep angle where footprint shape is elongated.",
                ],
                "mental_model": "Filtering reconstructs values; mipmaps choose an appropriate scale before reconstruction.",
                "check": "Why does a distant checkerboard shimmer without mipmapping?",
            },
            {
                "title": "Modern OpenGL Texture Pipeline",
                "slides": "Section 9.4",
                "commentary": [
                    "In modern OpenGL, textures are represented by texture objects, bound to texture units, connected to sampler uniforms, and accessed in shaders. The shader does not sample a filename; it samples a bound texture through a sampler.",
                    "Texture bugs often come from state mismatches: wrong active texture unit, wrong sampler uniform, missing mipmaps for a mipmap filter, wrong wrap mode, or wrong internal format.",
                ],
                "mental_model": "OpenGL texturing is a chain: object data -> texture unit -> sampler uniform -> shader lookup.",
                "check": "Why can a texture appear black when the shader code is mathematically correct?",
            },
            {
                "title": "Normal Mapping",
                "slides": "Section 9.5",
                "commentary": [
                    "Normal mapping stores normal directions in a texture so that lighting can vary at a finer scale than the geometry. The surface may have few triangles, but the shader receives detailed normals per fragment.",
                    "The hard part is coordinate space. Normal maps are often defined in tangent space, so the shader must transform or interpret them with the correct tangent, bitangent, and normal basis.",
                ],
                "mental_model": "Normal mapping changes the lighting normal, not the actual mesh silhouette.",
                "check": "Why does normal mapping not change the geometric outline of an object?",
            },
            {
                "title": "Environment Mapping and 3D Textures",
                "slides": "Sections 9.6-9.7",
                "commentary": [
                    "Environment mapping uses textures to represent surrounding illumination or reflections. A direction, not a surface UV alone, can be used to sample an environment map. This is a texture lookup driven by view/reflection geometry.",
                    "3D textures and volume rendering extend the same sampled-data idea into three dimensions. Instead of sampling a 2D image, the shader samples a volume. This is useful for data such as medical scans, density fields, or procedural volumetric effects.",
                ],
                "mental_model": "Textures are general sampled data; the coordinate dimensionality depends on the problem.",
                "check": "What coordinate type would you use to sample a 3D texture?",
            },
        ],
    },
    {
        "id": "10",
        "title": "Shadows",
        "source": "course_text_parts/03_lectures/10_shadows.txt",
        "opening": "This lecture explains shadows as a visibility problem from the light source. A point is lit if the light can see it; it is shadowed if another object blocks that visibility.",
        "sections": [
            {
                "title": "Definitions",
                "slides": "Section 10.1",
                "commentary": [
                    "A shadow is not simply a dark texture. It is evidence that light visibility is blocked. Important distinctions include hard versus soft shadows, umbra versus penumbra, and geometric versus precomputed approaches.",
                    "For real-time graphics, shadows are usually approximated. The approximation must answer a visibility question cheaply enough for interactive rendering.",
                ],
                "mental_model": "Shadows are light-space visibility made visible in the camera image.",
                "check": "Why is shadow computation related to visibility determination?",
            },
            {
                "title": "Ground Plane Shadows",
                "slides": "Section 10.2",
                "commentary": [
                    "Ground plane shadows project an object onto a receiving plane. This is simple and can look convincing in restricted scenes, but it assumes a known planar receiver and does not handle general shadowing between arbitrary objects.",
                    "The method is useful pedagogically because it makes the geometric nature of shadows explicit: a light source, an occluder, and a receiver define where the shadow lands.",
                ],
                "mental_model": "A planar shadow is projected geometry on a known receiver.",
                "check": "What scene limitation makes ground plane shadows less general than shadow maps?",
            },
            {
                "title": "Light Maps",
                "slides": "Section 10.3",
                "commentary": [
                    "Light maps store precomputed lighting or shadow information in textures. They can be efficient at runtime, but they are limited when lights, objects, or geometry move dynamically.",
                    "This is another example of a recurring graphics tradeoff: precompute for speed, but lose flexibility. Real-time rendering often mixes precomputed and dynamic techniques.",
                ],
                "mental_model": "A light map spends storage and preprocessing to save runtime shading work.",
                "check": "Why are light maps less suitable for fully dynamic moving lights?",
            },
            {
                "title": "Shadow Volumes",
                "slides": "Section 10.4",
                "commentary": [
                    "Shadow volumes construct the volume of space blocked from a light by an occluder. The camera view can then determine whether visible points lie inside that volume. Stencil buffer techniques are often associated with this method.",
                    "The strength is geometric precision for hard shadows. The cost is handling silhouette edges, volume construction, and robust stencil operations. It is a good contrast to shadow maps, which are image-based from the light view.",
                ],
                "mental_model": "A shadow volume is the 3D region where the light cannot reach.",
                "check": "Why are silhouette edges important for constructing shadow volumes?",
            },
            {
                "title": "Shadow Maps",
                "slides": "Section 10.5",
                "commentary": [
                    "Shadow mapping renders the scene from the light's point of view and stores depth. During the camera pass, a surface point is transformed into light space and compared against the stored depth. If it is farther than what the light saw, it is in shadow.",
                    "This method is practical and widely used, but it has artifacts. Shadow acne comes from precision/self-comparison issues. Bias can reduce acne but too much bias causes detached shadows. Resolution, filtering, and light projection strongly affect quality.",
                ],
                "mental_model": "Shadow maps reuse the depth-buffer idea, but from the light's camera.",
                "check": "What exactly is stored in a shadow map?",
            },
        ],
    },
]


def paragraph(text: str, style):
    from reportlab.platypus import Paragraph

    return Paragraph(html.escape(text), style)


def source_stats(rel: str) -> dict[str, int]:
    text = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
    return {
        "bytes": len(text.encode("utf-8")),
        "pages": text.count("[Seite "),
    }


def extract_slide_summaries(rel: str) -> list[dict[str, str]]:
    text = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
    chunks = re.split(r"\[Seite (\d+)\]", text)
    slides: list[dict[str, str]] = []
    for index in range(1, len(chunks), 2):
        page = chunks[index]
        body = chunks[index + 1]
        lines = [clean_line(line) for line in body.splitlines()]
        lines = [line for line in lines if useful_slide_line(line)]
        title = choose_slide_title(lines)
        clue = content_cue(lines, title)
        category = slide_category(title, clue)
        slides.append(
            {
                "page": page,
                "title": title,
                "cue": clue,
                "category": category,
                "professor": professor_explanation(category, title, clue),
                "commentary": slide_comment(category, title, clue),
                "why": slide_why(category),
                "check": slide_check(category, title),
            }
        )
    return slides


def clean_line(line: str) -> str:
    line = unicodedata.normalize("NFKC", line)
    replacements = {
        "(cid:127)": "-",
        "(cid:521)": "x",
        "(cid:520)": "x",
        "(cid:3)": " ",
        "": "-",
        "–": "-",
        "—": "-",
        "„": '"',
        "“": '"',
        "”": '"',
        "’": "'",
        " o f ": " of ",
    }
    for old, new in replacements.items():
        line = line.replace(old, new)
    line = re.sub(r"\(cid:\d+\)", "", line)
    line = re.sub(r"\b224\s*=\s*28\s*x\s*28\s*x\s*28\b", "2^24 = 2^8 x 2^8 x 2^8", line)
    line = re.sub(r"\b24 Bit\b", "24-bit", line)
    line = re.sub(r"\b18\.874\.368b\b", "18,874,368 bits", line)
    line = re.sub(r"\b2\.359\.296B\b", "2,359,296 bytes", line)
    line = re.sub(r"\b2,25MiB\b", "2.25 MiB", line)
    line = re.sub(r"\s+", " ", line)
    return line.strip()


def useful_slide_line(line: str) -> bool:
    if not line:
        return False
    lower = line.lower()
    skip_fragments = [
        "seiten-metadaten",
        "interactive computer graphics",
        "visual computing group",
        "institute of media informatics",
        "summer term 2026",
        "timo ropinski",
        "chapter ",
        "references",
    ]
    if any(fragment in lower for fragment in skip_fragments):
        return False
    if re.fullmatch(r"\d{2}/\d{2}/\d{4}\s*\d*", line):
        return False
    if re.fullmatch(r"\d+", line):
        return False
    if re.fullmatch(r"[xyzuvwXYZUVW]", line):
        return False
    if len(line) <= 2 and not line.isdigit():
        return False
    return True


def choose_slide_title(lines: list[str]) -> str:
    if not lines:
        return "Visual or title slide"
    for line in lines:
        if line.startswith("-"):
            continue
        if len(line) <= 95:
            return line
    return lines[0][:95]


def content_cue(lines: list[str], title: str) -> str:
    cue_lines = []
    for line in lines:
        if line == title and not cue_lines:
            continue
        if len(line) > 140:
            line = line[:137] + "..."
        cue_lines.append(line)
        if len(cue_lines) >= 5:
            break
    if not cue_lines:
        return "No object-level text was extracted from this page; the page is primarily title, image, diagram, or layout content."
    return " / ".join(cue_lines)


def slide_category(title: str, clue: str) -> str:
    title_text = title.lower()
    text = f"{title} {clue}".lower()
    if any(token in title_text for token in ["references", "literature", "sources used"]):
        return "reference"
    if any(token in title_text for token in ["history", "milestone", "contest result"]):
        return "history"
    if any(token in title_text for token in ["raster image", "pixel-based", "color depth", "image size", "memory"]):
        return "pixeldata"
    if any(token in title_text for token in ["3d model", "models", "modeling", "geometric primitive"]):
        return "model"
    if any(token in text for token in ["cast ray", "castray", "ray march", "ray casting", "ray tracing"]):
        return "visibility"
    if "outline" in text:
        return "outline"
    if "course" in text or "teacher" in text or "exercise" in text:
        return "organization"
    if "object-based rendering" in text or "geometry-based rendering" in text or "rendering process" in text or "rendering pipeline" in text:
        return "pipeline"
    if "opengl" in text or "shader" in text or "buffer" in text or "framebuffer" in text:
        return "opengl"
    if "transform" in text or "matrix" in text or "coordinate" in text:
        return "transform"
    if "clipping" in text or "cohen" in text or "sutherland" in text or "cyrus" in text or "weiler" in text or "greiner" in text:
        return "clipping"
    if "raster" in text or "scanline" in text or "triangle" in text or "line " in text or "filling" in text:
        return "rasterization"
    if "visibility" in text or "depth" in text or "z-buffer" in text or "ray" in text or "bsp" in text or "warnock" in text:
        return "visibility"
    if "projection" in text or "camera" in text or "viewport" in text or "perspective" in text or "orthographic" in text:
        return "projection"
    if "light" in text or "illumination" in text or "phong" in text or "material" in text or "shading" in text or "normal" in text:
        return "illumination"
    if "texture" in text or "mipmap" in text or "sampling" in text or "filter" in text or "uv" in text or "environment" in text:
        return "texturing"
    if "shadow" in text:
        return "shadows"
    return "general"


def slide_comment(category: str, title: str, clue: str) -> str:
    prefix = f"This slide is about {title}. "
    comments = {
        "outline": "The listed items define the lecture sequence: the topic begins with a problem statement, introduces the required objects or algorithms, and then connects them to rendering or implementation consequences.",
        "organization": "The slide connects lecture theory with exercise work, programming practice, and assessment expectations. The named dates, exercises, or course components indicate where the concept will reappear.",
        "history": "The slide places the technical topic into the historical development of computer graphics, showing how artistic perspective, display technology, interaction, and rendering algorithms evolved together.",
        "pixeldata": "The slide describes image data as discrete samples: pixels, color channels, bit depth, memory layout, and the amount of storage needed for a raster image.",
        "model": "The slide describes scene objects before rendering: geometric models, primitives, vertices, topology, attributes, and the representation used as input to the pipeline.",
        "reference": "The slide lists source material or chapter references that support the technical content and give names for further reading.",
        "pipeline": "Scene or model data moves through a sequence of representations: vertices, primitives, fragments, tests, and framebuffer updates. Each named object is one stage in that conversion.",
        "opengl": "The OpenGL objects and calls shown here control GPU state, bound resources, shader interfaces, buffer contents, or framebuffer access at draw time.",
        "transform": "The transformation objects on the slide move points, vectors, or coordinate frames from one space into another using matrices or affine operations.",
        "projection": "The projection objects on the slide convert view-space geometry into clip coordinates, normalized coordinates, and finally screen-related positions.",
        "clipping": "The clipping objects on the slide classify geometry against boundaries and produce accepted, rejected, or newly intersected primitive pieces.",
        "rasterization": "The rasterization objects on the slide convert ideal geometric primitives into covered samples or fragments with interpolated attributes.",
        "visibility": "The visibility method on the slide decides which surface, fragment, ray hit, or image region is visible from the current viewpoint.",
        "illumination": "The lighting objects on the slide combine normals, light directions, view directions, material coefficients, and shading locations to compute color.",
        "texturing": "The texturing objects on the slide define sampled data, coordinates, filtering rules, mip levels, and shader interpretation of fetched values.",
        "shadows": "The shadow objects on the slide represent visibility from the light source: occluders block light, receivers show the result, and the algorithm stores or computes that relation.",
        "general": "The slide names a concrete relation between input data, an operation, and an output that another graphics stage can consume.",
    }
    return prefix + comments[category] + f" Concrete items shown: {clue}"


def professor_explanation(category: str, title: str, clue: str) -> str:
    cue_sentence = f"On the slide, the concrete items are: {clue.rstrip('.;:')}"
    if clue.startswith("No object-level text was extracted"):
        return (
            f"The slide '{title}' is primarily a visual, title, transition, or diagram page rather than a text-heavy concept slide. "
            f"Its role is to place the next concept into the lecture flow and give a visual anchor for the topic that follows. "
            f"{cue_sentence}. In the surrounding lecture sequence, this kind of page usually marks a shift of attention: from one pipeline stage to another, from a general idea to an algorithm, or from theory to an implementation detail."
        )
    explanations = {
        "outline": (
            f"The outline '{title}' gives the lecture its internal logic. The listed topics are the objects that will be connected during the chapter: first the problem space, then the mathematical or algorithmic tools, then the implementation consequences. "
            f"{cue_sentence}. The order matters because later items rely on earlier definitions. For example, an OpenGL mechanism is much easier to understand once the corresponding pipeline object or mathematical operation has already been introduced. "
            f"The outline is therefore a compact dependency graph of the lecture rather than a collection of isolated labels."
        ),
        "history": (
            f"The slide '{title}' explains the historical background behind the graphics concept. Computer graphics did not appear as one finished pipeline; it developed from older ideas such as artistic perspective, color representation, display hardware, interactive systems, and increasingly programmable rendering algorithms. "
            f"The historical objects on the slide are people, systems, dates, or milestones, and each milestone marks a capability that later became normal in graphics software. "
            f"{cue_sentence}. This history matters because it shows why the course combines mathematics, image representation, hardware acceleration, and interaction. Modern real-time rendering is the result of these threads converging into a pipeline that can generate images fast enough for user input."
        ),
        "pixeldata": (
            f"The slide '{title}' explains raster images as concrete stored data. A raster image is a rectangular grid of pixels. Each pixel stores one or more channel values, such as red, green, blue, and sometimes alpha. "
            f"Color depth tells us how many bits are available per pixel or per channel, and that immediately determines both the number of representable colors and the memory footprint of the image. "
            f"{cue_sentence}. The object relation is pixel count, bits per pixel, color range, and memory size. This is why a simple image-resolution question is also a performance question: more pixels and more bits mean more memory traffic, more storage, and more work for display or image-processing operations."
        ),
        "model": (
            f"The slide '{title}' explains how scene objects exist before they are rendered. A 3D model is not an image yet; it is a structured description of geometry and attributes. "
            f"The central objects are vertices, edges, faces, triangles or other primitives, and sometimes additional data such as normals, texture coordinates, colors, materials, or connectivity. "
            f"{cue_sentence}. This matters because the rendering pipeline needs this representation as input. The model describes what exists in the scene, while later stages decide where it appears, which parts are visible, how it is sampled into fragments, and how it is shaded into final pixel colors."
        ),
        "reference": (
            f"The slide '{title}' collects the source material behind the chapter. References are not rendering objects themselves, but they identify the books, papers, or external resources from which the lecture's terminology and algorithms are drawn. "
            f"{cue_sentence}. In practical terms, a reference slide marks the boundary of the chapter and tells us where the formal definitions, derivations, or extended examples can be found if a topic needs more depth than the lecture slides provide."
        ),
        "organization": (
            f"The slide '{title}' describes the practical objects of the course: lectures, exercise sheets, programming tasks, project work, teachers, dates, tools, or submission structure. "
            f"These objects are part of the learning system around the graphics content. The lecture introduces a concept, the exercise turns it into code or a calculation, and the project combines several such concepts into a working renderer. "
            f"{cue_sentence}. The important relation is between topic, practice format, and skill. A rendering concept that appears in an exercise is not just background vocabulary; it becomes something that can be recognized in C/C++ code, OpenGL calls, shader inputs, or debugging situations."
        ),
        "pipeline": (
            f"The slide '{title}' explains rendering as a chain of object transformations. At the beginning there is scene information: models, vertices, primitives, attributes, camera state, and rendering state. "
            f"The geometry part of the pipeline changes where the objects are and how they are represented; vertices become positioned data, vertices are assembled into primitives, and primitives are prepared for conversion to the image grid. "
            f"{cue_sentence}. The important story is that the same scene information changes form several times. A triangle is first model data, then transformed geometry, then a projected primitive, then a set of fragments, and finally only some of those fragments become pixel updates. "
            f"This is why the pipeline is not just a drawing diagram; it is the explanation for where image errors can enter."
        ),
        "opengl": (
            f"The slide '{title}' explains how OpenGL exposes the rendering pipeline through explicit objects and state. A context owns the current rendering state; buffers hold vertex, index, texture, or pixel data; shader programs define programmable processing; textures and samplers provide sampled data; framebuffers receive the result. "
            f"OpenGL does not render from intention, it renders from the objects that are bound and the state that is active at the moment of the draw call. "
            f"{cue_sentence}. The concrete relation is API command, GPU resource, shader interface, and visible result. A small mismatch in this relation, such as a wrong buffer layout, missing uniform, wrong texture unit, or disabled depth test, can produce a perfectly valid draw call with a completely wrong image."
        ),
        "transform": (
            f"The slide '{title}' explains how geometric objects move through coordinate systems. A point has a location, a vector has a direction and magnitude, a normal describes surface orientation, and a coordinate frame defines how these quantities are measured. "
            f"A transformation matrix changes the description of these objects: translation moves points, rotation changes orientation, scaling changes size, and composition combines several operations into one matrix product. "
            f"{cue_sentence}. The central relation is source space, transformation, and target space. In computer graphics this relation is everywhere: object space becomes world space, world space becomes view space, and view space becomes clip space. "
            f"A formula is only meaningful after the two coordinate spaces around it are clear."
        ),
        "projection": (
            f"The slide '{title}' explains how camera geometry turns a 3D scene into image coordinates. In view space, objects are described relative to the camera. The projection matrix then maps that camera-centered geometry into clip space, where the viewing volume and clipping boundaries can be handled consistently. "
            f"Perspective projection uses the homogeneous coordinate so that the later divide by w creates foreshortening: farther objects occupy less image space. Orthographic projection removes that depth-based size change and keeps parallel structures visually parallel. "
            f"{cue_sentence}. The object chain is view-space position, projection matrix, clip coordinate, normalized device coordinate, and viewport coordinate. The slide is therefore connecting camera setup, visual appearance, and the numeric coordinate pipeline that rasterization later consumes."
        ),
        "clipping": (
            f"The slide '{title}' explains clipping as a geometric boundary operation. A line segment, polygon, or triangle is compared with a window, plane, or volume. "
            f"The part inside the valid region survives, the part outside is removed, and a primitive crossing the boundary receives newly computed intersection points. "
            f"{cue_sentence}. The objects involved are the original primitive, the clipping boundary, an inside/outside classification, intersection points, and the resulting clipped primitive. "
            f"The core idea is not simply deleting geometry; clipping can reshape geometry so that the rasterizer receives only the meaningful visible portion."
        ),
        "rasterization": (
            f"The slide '{title}' explains the moment where continuous geometry becomes a discrete image problem. A mathematical line or triangle is not made of pixels, but the screen is a grid of samples. "
            f"Rasterization decides which samples are covered by the projected primitive and creates fragments for those samples. At the same time, values attached to the primitive, such as depth, color, normals, or texture coordinates, are interpolated so that each fragment has the data needed for shading. "
            f"{cue_sentence}. The important distinction is that rasterization creates candidates. A fragment exists because a primitive covered a sample, but final visibility still depends on depth testing, stencil testing, blending, masking, and framebuffer operations."
        ),
        "visibility": (
            f"The slide '{title}' explains the problem of deciding which surface is actually visible from the current viewpoint. Many primitives can project to the same image region, but only the nearest relevant surface should determine the opaque color at a pixel. "
            f"Different algorithms solve this relation in different spaces: object-space methods sort or split geometry, image-space methods subdivide regions, ray methods query visibility along viewing rays, and the depth buffer compares per-fragment depth values. "
            f"{cue_sentence}. The object-level relation is viewpoint, candidate surface, visibility rule, and visible result. This relation is the reason that fragment generation and final pixel color are not the same thing."
        ),
        "illumination": (
            f"The slide '{title}' explains how a visible surface point receives color from local lighting. The surface normal gives the orientation of the surface. The light vector gives the direction from which illumination arrives. "
            f"The view vector connects the surface point to the observer, and the material parameters decide how strongly the surface reacts with ambient, diffuse, or specular reflection. "
            f"{cue_sentence}. The object-level relation is light source, surface point, normal, material response, and computed color. The visual behavior changes when any of these objects changes: a rotated normal changes diffuse brightness, a different view vector moves the specular highlight, and different material coefficients change the perceived surface type."
        ),
        "texturing": (
            f"The slide '{title}' explains textures as sampled data fields used during shading. A texture is not only a picture; it is a structured array of texels that can store color, normals, depth, material values, environment data, or volume data. "
            f"A fragment supplies texture coordinates, the texture object supplies stored samples, sampler state controls wrapping and filtering, and the shader decides what the fetched value means. "
            f"{cue_sentence}. The object-level relation is coordinate, texture memory, sampling rule, and shader interpretation. This relation explains why texture bugs often look visual but originate from data addressing, filtering state, mipmap completeness, or a mismatch between stored values and shader expectations."
        ),
        "shadows": (
            f"The slide '{title}' explains a shadow as a visibility relation from the light source. A surface point is lit when the light can reach it directly, and it is shadowed when another object blocks the path from the light to that point. "
            f"The central objects are therefore the light, the occluder, the receiver, and some representation of light-space visibility. Depending on the method, that representation can be projected geometry, a precomputed light map, a shadow volume, or a shadow map storing depth from the light. "
            f"{cue_sentence}. The object-level relation is light, blocker, receiver, stored visibility information, and the darkened region visible in the final camera image."
        ),
        "general": (
            f"The slide '{title}' introduces a graphics object, operation, or relation that belongs to the rendering workflow. The named terms describe what data enters the step, what operation changes or classifies that data, and what result is passed onward. "
            f"{cue_sentence}. The object-level relation is input, operation, output, and later use. This is the basic shape of most computer graphics concepts: data is represented in one form, processed by a rule or algorithm, and then consumed by the next stage of image generation."
        ),
    }
    return explanations[category]


def slide_why(category: str) -> str:
    reasons = {
        "outline": "Outlines tell you the dependency order. They are the safest way to avoid learning isolated bullet points.",
        "organization": "Course logistics often reveal which topics are practiced, assessed, or expected in code.",
        "history": "Historical slides explain why the current pipeline exists and which older problems led to modern graphics concepts.",
        "pixeldata": "Pixel-data slides connect visual output to memory size, bandwidth, precision, and image-processing cost.",
        "model": "Model slides explain the input objects that later transformations, projection, rasterization, and shading operate on.",
        "reference": "Reference slides provide the source trail for definitions, algorithms, and deeper explanations.",
        "pipeline": "Pipeline understanding lets you localize rendering errors instead of guessing randomly.",
        "opengl": "OpenGL bugs are usually state, binding, shader-interface, or buffer-layout bugs, so API details matter.",
        "transform": "A wrong coordinate-space assumption can make correct formulas produce wrong images.",
        "projection": "Projection controls both image composition and depth precision, so it affects visibility and rasterization later.",
        "clipping": "Clipping decides what geometry is allowed to reach rasterization and can create new boundary vertices.",
        "rasterization": "Rasterization determines fragment generation; without it, shading and fragment tests have nothing to operate on.",
        "visibility": "Visibility decides which generated candidates are actually seen from the current viewpoint.",
        "illumination": "Lighting formulas are only meaningful when their vectors and material terms are interpreted correctly.",
        "texturing": "Texture sampling is a major source of visual detail and a common source of artifacts.",
        "shadows": "Shadow algorithms reuse visibility ideas, but from the light's point of view.",
        "general": "Even a sparse slide usually names a relation you must be able to explain in words.",
    }
    return reasons[category]


def slide_check(category: str, title: str) -> str:
    checks = {
        "outline": f"Can you explain where '{title}' fits in the lecture order and what later section depends on it?",
        "organization": f"Can you connect '{title}' to an exercise, project task, or exam-preparation action?",
        "history": f"Can you name the graphics capability or idea represented by '{title}' and why it mattered historically?",
        "pixeldata": f"Can you compute or explain the pixel count, color depth, or memory relation in '{title}'?",
        "model": f"Can you name the geometric objects and attributes represented by '{title}' before rendering begins?",
        "reference": f"Can you identify which source or topic '{title}' points to for deeper study?",
        "pipeline": f"Can you name the input and output representation for '{title}' in the rendering pipeline?",
        "opengl": f"Can you name the OpenGL object, state, shader stage, or buffer involved in '{title}'?",
        "transform": f"Can you state the coordinate space before and after '{title}'?",
        "projection": f"Can you explain how '{title}' changes positions before rasterization?",
        "clipping": f"Can you decide what is accepted, rejected, or newly intersected in '{title}'?",
        "rasterization": f"Can you explain which samples/fragments are generated by '{title}'?",
        "visibility": f"Can you decide whether '{title}' works per object, per image region, per ray, or per fragment?",
        "illumination": f"Can you identify the normal, light vector, view vector, and material term relevant to '{title}'?",
        "texturing": f"Can you identify the sampled data, coordinate, and filtering/state issue in '{title}'?",
        "shadows": f"Can you explain what the light can or cannot see in '{title}'?",
        "general": f"Can you turn '{title}' into a causal sentence instead of repeating the slide title?",
    }
    return checks[category]


def lecture_markdown(lecture: dict) -> str:
    stats = source_stats(lecture["source"])
    slides = extract_slide_summaries(lecture["source"])
    lines = [
        f"# Lecture {lecture['id']} - {lecture['title']}",
        "",
        f"Source chunk: `{lecture['source']}`",
        f"Extracted slide pages in source chunk: {stats['pages']}",
        "",
        "This file is an explanatory reading version of the lecture. It keeps the course language in English and adds the missing commentary that the slide deck assumes was spoken in class. It is not a replacement for the original slides; use it next to the source chunk.",
        "",
        "## Big Picture",
        "",
        lecture["opening"],
        "",
        "## How To Read This Lecture",
        "",
        "- First read the big picture and the mental models.",
        "- Then open the source chunk and compare the slide bullets to the commentary.",
        "- After each section, answer the check question without notes.",
        "- If the check feels vague, revisit the source pages listed for that section.",
        "",
    ]
    lines.extend(
        [
            "## Per-Slide Commentary",
            "",
            "Every extracted slide page gets its own reading note. This is the part to use when the original PDF is too terse or visually dense.",
            "",
        ]
    )
    for slide in slides:
        lines.extend(
            [
                f"### Page {slide['page']} - {slide['title']}",
                "",
                f"Source cue: {slide['cue']}",
                "",
                f"Professor-style explanation: {slide['professor']}",
                "",
                f"Technical commentary: {slide['commentary']}",
                "",
                f"Why it matters: {slide['why']}",
                "",
                f"Check yourself: {slide['check']}",
                "",
            ]
        )
    for index, section in enumerate(lecture["sections"], start=1):
        lines.extend(
            [
                f"## {lecture['id']}.{index} {section['title']}",
                "",
                f"Source location: {section['slides']}",
                "",
                "### Commentary",
                "",
            ]
        )
        for item in section["commentary"]:
            lines.extend([item, ""])
        lines.extend(
            [
                "### Mental Model",
                "",
                section["mental_model"],
                "",
                "### Check Yourself",
                "",
                section["check"],
                "",
            ]
        )
    lines.extend(
        [
            "## End-of-Lecture Summary",
            "",
            f"If you remember only one thing from Lecture {lecture['id']}, remember this: {lecture['opening']}",
            "",
            "Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.",
            "",
        ]
    )
    return "\n".join(lines)


def write_markdown_files() -> None:
    for lecture in LECTURES:
        filename = f"{lecture['id']}_{slug(lecture['title'])}_reader.md"
        (MD_OUT / filename).write_text(lecture_markdown(lecture), encoding="utf-8")


def slug(text: str) -> str:
    return text.lower().replace(" ", "-")


def build_pdf_for_lecture(lecture: dict, output_path: Path) -> None:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.platypus import PageBreak, SimpleDocTemplate, Spacer, Table, TableStyle

    styles = getSampleStyleSheet()
    styles["Title"].fontName = "Helvetica-Bold"
    styles["Heading1"].fontName = "Helvetica-Bold"
    styles["Heading2"].fontName = "Helvetica-Bold"
    styles["BodyText"].fontName = "Helvetica"
    styles["BodyText"].fontSize = 10.2
    styles["BodyText"].leading = 13.8

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#596870"))
        canvas.drawString(1.6 * cm, 1.05 * cm, f"Lecture {lecture['id']} - {lecture['title']}")
        canvas.drawRightString(A4[0] - 1.6 * cm, 1.05 * cm, f"Page {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=1.6 * cm,
        rightMargin=1.6 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title=f"Lecture {lecture['id']} - {lecture['title']} Reader",
    )
    story = lecture_story(lecture, styles, include_title=True)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def lecture_story(lecture: dict, styles, include_title: bool):
    from reportlab.lib import colors
    from reportlab.lib.units import cm
    from reportlab.platypus import PageBreak, Spacer, Table, TableStyle

    stats = source_stats(lecture["source"])
    slides = extract_slide_summaries(lecture["source"])
    story = []
    if include_title:
        story.append(paragraph(f"Lecture {lecture['id']} - {lecture['title']}", styles["Title"]))
    else:
        story.append(paragraph(f"Lecture {lecture['id']} - {lecture['title']}", styles["Heading1"]))
    story.append(Spacer(1, 8))
    story.append(paragraph(lecture["opening"], styles["BodyText"]))
    story.append(Spacer(1, 10))
    meta = Table(
        [
            ["Source chunk", lecture["source"]],
            ["Extracted slide pages", str(stats["pages"])],
            ["Reader purpose", "Commentary and causal explanation for human reading"],
        ],
        colWidths=[4.2 * cm, 11.0 * cm],
    )
    meta.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#cbd6dc")),
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#edf3f1")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
            ]
        )
    )
    story.append(meta)
    story.append(Spacer(1, 12))
    story.append(paragraph("How to read this lecture", styles["Heading2"]))
    for item in [
        "Read the section commentary before looking at the raw slide bullets.",
        "Use the mental model as the short version you should remember.",
        "Answer the check question without notes before continuing.",
    ]:
        story.append(paragraph(f"- {item}", styles["BodyText"]))
    story.append(Spacer(1, 8))
    story.append(paragraph("Per-slide commentary", styles["Heading1"]))
    story.append(paragraph("Each extracted slide page gets its own note. Use this section as the spoken commentary that the terse slide deck is missing.", styles["BodyText"]))
    for slide in slides:
        slide_table = Table(
            [
                [paragraph(f"Page {slide['page']}", styles["BodyText"]), paragraph(slide["title"], styles["BodyText"])],
                [paragraph("Source cue", styles["BodyText"]), paragraph(slide["cue"], styles["BodyText"])],
                [paragraph("Professor-style explanation", styles["BodyText"]), paragraph(slide["professor"], styles["BodyText"])],
                [paragraph("Technical commentary", styles["BodyText"]), paragraph(slide["commentary"], styles["BodyText"])],
                [paragraph("Why it matters", styles["BodyText"]), paragraph(slide["why"], styles["BodyText"])],
                [paragraph("Check yourself", styles["BodyText"]), paragraph(slide["check"], styles["BodyText"])],
            ],
            colWidths=[3.0 * cm, 12.2 * cm],
        )
        slide_table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#d5dde1")),
                    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#edf3f1")),
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f6f8f8")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ]
            )
        )
        story.append(slide_table)
        story.append(Spacer(1, 6))
    story.append(Spacer(1, 10))
    for index, section in enumerate(lecture["sections"], start=1):
        story.append(paragraph(f"{lecture['id']}.{index} {section['title']}", styles["Heading1"]))
        story.append(paragraph(f"Source location: {section['slides']}", styles["BodyText"]))
        story.append(Spacer(1, 5))
        story.append(paragraph("Commentary", styles["Heading2"]))
        for item in section["commentary"]:
            story.append(paragraph(item, styles["BodyText"]))
            story.append(Spacer(1, 5))
        story.append(paragraph("Mental model", styles["Heading2"]))
        story.append(paragraph(section["mental_model"], styles["BodyText"]))
        story.append(paragraph("Check yourself", styles["Heading2"]))
        story.append(paragraph(section["check"], styles["BodyText"]))
        story.append(Spacer(1, 9))
    story.append(paragraph("End-of-lecture summary", styles["Heading1"]))
    story.append(paragraph(f"If you remember only one thing from Lecture {lecture['id']}, remember this: {lecture['opening']}", styles["BodyText"]))
    story.append(paragraph("Before moving on, you should be able to explain the lecture without reading slide bullets aloud. Use the vocabulary from the slides, but add causal links: why a step exists, what data it consumes, what it produces, and what can go wrong.", styles["BodyText"]))
    if not include_title:
        story.append(PageBreak())
    return story


def build_combined_pdf() -> None:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.platypus import PageBreak, SimpleDocTemplate, Spacer

    styles = getSampleStyleSheet()
    styles["Title"].fontName = "Helvetica-Bold"
    styles["Heading1"].fontName = "Helvetica-Bold"
    styles["Heading2"].fontName = "Helvetica-Bold"
    styles["BodyText"].fontName = "Helvetica"
    styles["BodyText"].fontSize = 10.2
    styles["BodyText"].leading = 13.8

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#596870"))
        canvas.drawString(1.6 * cm, 1.05 * cm, "CS8165.001 Complete Lecture Readers")
        canvas.drawRightString(A4[0] - 1.6 * cm, 1.05 * cm, f"Page {doc.page}")
        canvas.restoreState()

    output_path = PDF_OUT / "CS8165_complete_lecture_readers.pdf"
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=1.6 * cm,
        rightMargin=1.6 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title="CS8165.001 Complete Lecture Readers",
    )
    story = [
        paragraph("CS8165.001 Complete Lecture Readers", styles["Title"]),
        Spacer(1, 10),
        paragraph("Readable commentary for each lecture in the course's primary language. This document is designed to make the raw slides human-readable while keeping links back to the extracted source chunks.", styles["BodyText"]),
        Spacer(1, 14),
        paragraph("Contents", styles["Heading1"]),
    ]
    for lecture in LECTURES:
        story.append(paragraph(f"Lecture {lecture['id']} - {lecture['title']}", styles["BodyText"]))
    story.append(PageBreak())
    for lecture in LECTURES:
        story.extend(lecture_story(lecture, styles, include_title=False))
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def write_readme() -> None:
    lines = [
        "# Lecture Readers",
        "",
        "This folder contains a readable version of every lecture. The raw slide extraction is still the source of truth, but these files add the missing explanatory commentary that makes the material usable for human study. Every extracted slide page has its own commentary block with a source cue, professor-style explanation, technical commentary, relevance note, and check question.",
        "",
        "Language: English. The lecture material is primarily English, so the generated commentary stays in English.",
        "",
        "## Files",
        "",
        "- `markdown/` - one readable Markdown file per lecture, with per-slide commentary",
        "- `pdf/` - one PDF per lecture plus `CS8165_complete_lecture_readers.pdf`, with per-slide commentary",
        "- `lecture_reader_manifest.json` - generated coverage manifest",
        "",
        "## Recommended Reading Route",
        "",
        "1. Read one lecture reader PDF or Markdown file.",
        "2. Open the referenced source chunk in `course_text_parts/03_lectures/`.",
        "3. Answer every `Check yourself` question without notes.",
        "4. Put weak spots into `overprep_pack/mistake_log.md`.",
        "5. Then use `practice_pack/` and `overprep_pack/` for closed-format repetition.",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_manifest() -> None:
    manifest = {
        "pack": "lecture_readers",
        "language": "English",
        "lecture_count": len(LECTURES),
        "lectures": [
            {
                "id": lecture["id"],
                "title": lecture["title"],
                "source": lecture["source"],
                "source_exists": (ROOT / lecture["source"]).exists(),
                "markdown": f"markdown/{lecture['id']}_{slug(lecture['title'])}_reader.md",
                "pdf": f"pdf/{lecture['id']}_{slug(lecture['title'])}_reader.pdf",
                "sections": len(lecture["sections"]),
                "source_pages": source_stats(lecture["source"])["pages"],
            }
            for lecture in LECTURES
        ],
        "combined_pdf": "pdf/CS8165_complete_lecture_readers.pdf",
    }
    (OUT / "lecture_reader_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    MD_OUT.mkdir(parents=True)
    PDF_OUT.mkdir(parents=True)
    write_markdown_files()
    for lecture in LECTURES:
        build_pdf_for_lecture(lecture, PDF_OUT / f"{lecture['id']}_{slug(lecture['title'])}_reader.pdf")
    build_combined_pdf()
    write_readme()
    write_manifest()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
