#version 150

uniform float zoom = 1.0;
uniform vec2 zoomPosition = vec2(0.0, 0.0);

in vec2 position;
in vec2 complex;

out vec2 fragComplex;

void main()
{
    // Question 2b
    // TODO: Adjust complex range.
    fragComplex = complex;
    // Question 2b
    // TODO: Adjust quad positions.
    gl_Position = vec4(position, 0, 1);
}
