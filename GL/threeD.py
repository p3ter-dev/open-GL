import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import math

vertex_src = """
#version 330 core
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;

uniform mat4 rotation;

out vec3 v_color;

void main() {
    gl_Position = rotation * vec4(a_position, 1.0);
    v_color = a_color;
}
"""

fragment_src = """
#version 330 core
in vec3 v_color;
out vec4 out_color;

void main() {
    out_color = vec4(v_color, 1.0);
}
"""

vertices = [
    -0.5, -0.5, -0.5,   0.0, 0.0, 1.0,
     0.5, -0.5, -0.5,   1.0, 0.0, 0.0,
     0.5,  0.5, -0.5,   1.0, 1.0, 1.0,
    -0.5,  0.5, -0.5,   0.0, 0.0, 1.0,

    -0.5, -0.5,  0.5,   0.0, 1.0, 0.0,
     0.5, -0.5,  0.5,   0.5, 0.0, 0.5,
     0.5,  0.5,  0.5,   0.0, 1.0, 0.0,
    -0.5,  0.5,  0.5,   0.5, 0.0, 0.5,

    -0.5, -0.5, -0.5,   0.0, 0.0, 0.0,
    -0.5, -0.5,  0.5,   0.5, 0.0, 0.5,
    -0.5,  0.5,  0.5,   0.5, 0.0, 0.5,
    -0.5,  0.5, -0.5,   0.0, 0.0, 0.0,

     0.5, -0.5, -0.5,   1.0, 0.0, 0.0,
     0.5, -0.5,  0.5,   1.0, 0.8, 0.0,
     0.5,  0.5,  0.5,   1.0, 0.8, 0.0,
     0.5,  0.5, -0.5,   1.0, 0.0, 0.0,

    -0.5,  0.5, -0.5,   0.0, 0.0, 1.0,
     0.5,  0.5, -0.5,   0.6, 0.6, 0.6,
     0.5,  0.5,  0.5,   0.6, 0.6, 0.6,
    -0.5,  0.5,  0.5,   0.0, 0.0, 1.0,

    -0.5, -0.5, -0.5,   1.0, 0.0, 0.0,
     0.5, -0.5, -0.5,   0.0, 0.0, 1.0,
     0.5, -0.5,  0.5,   1.0, 0.0, 0.0,
    -0.5, -0.5,  0.5,   0.0, 0.0, 1.0
]

indices = [
    0, 1, 2, 2, 3, 0,
    4, 5, 6, 6, 7, 4,
    0, 4, 7, 7, 3, 0,
    1, 5, 6, 6, 2, 1,
    3, 2, 6, 6, 7, 3,
    0, 1, 5, 5, 4, 0
]

if not glfw.init():
    raise Exception("GLFW could not be initialized!")

window = glfw.create_window(800, 600, "Rotating 3D Cube", None, None)
if not window:
    glfw.terminate()
    raise Exception("GLFW window could not be created!")

glfw.make_context_current(window)

shader = compileProgram(
    compileShader(vertex_src, GL_VERTEX_SHADER),
    compileShader(fragment_src, GL_FRAGMENT_SHADER)
)

vertices = np.array(vertices, dtype=np.float32)
indices = np.array(indices, dtype=np.uint32)

VAO = glGenVertexArrays(1)
VBO = glGenBuffers(1)
EBO = glGenBuffers(1)

glBindVertexArray(VAO)

glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
glEnableVertexAttribArray(0)

glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
glEnableVertexAttribArray(1)

glUseProgram(shader)

rotation_loc = glGetUniformLocation(shader, "rotation")

glEnable(GL_DEPTH_TEST)

angle = 0.0
while not glfw.window_should_close(window):
    glfw.poll_events()
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    angle += 0.01
    rotation = np.array([
        [math.cos(angle), 0, math.sin(angle), 0],
        [0, 1, 0, 0],
        [-math.sin(angle), 0, math.cos(angle), 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)
    
    glUniformMatrix4fv(rotation_loc, 1, GL_FALSE, rotation)
    
    glBindVertexArray(VAO)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)
    
    glfw.swap_buffers(window)

glfw.terminate()
