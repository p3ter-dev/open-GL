import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import math

# Vertex Shader
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

# Fragment Shader
fragment_src = """
#version 330 core
in vec3 v_color;
out vec4 out_color;

void main() {
    out_color = vec4(v_color, 1.0);
}
"""

# Cube vertices and colors
# Cube vertices with Marvel-inspired colors
vertices = [
    # Positions         # Colors (Marvel-inspired)
    -0.5, -0.5, -0.5,   0.0, 0.0, 1.0,   # Blue (Captain America - Back face)
     0.5, -0.5, -0.5,   1.0, 0.0, 0.0,   # Red
     0.5,  0.5, -0.5,   1.0, 1.0, 1.0,   # White
    -0.5,  0.5, -0.5,   0.0, 0.0, 1.0,   # Blue

    -0.5, -0.5,  0.5,   0.0, 1.0, 0.0,   # Green (Hulk - Front face)
     0.5, -0.5,  0.5,   0.5, 0.0, 0.5,   # Purple
     0.5,  0.5,  0.5,   0.0, 1.0, 0.0,   # Green
    -0.5,  0.5,  0.5,   0.5, 0.0, 0.5,   # Purple

    -0.5, -0.5, -0.5,   0.0, 0.0, 0.0,   # Black (Black Panther - Left face)
    -0.5, -0.5,  0.5,   0.5, 0.0, 0.5,   # Purple
    -0.5,  0.5,  0.5,   0.5, 0.0, 0.5,   # Purple
    -0.5,  0.5, -0.5,   0.0, 0.0, 0.0,   # Black

     0.5, -0.5, -0.5,   1.0, 0.0, 0.0,   # Red (Iron Man - Right face)
     0.5, -0.5,  0.5,   1.0, 0.8, 0.0,   # Gold
     0.5,  0.5,  0.5,   1.0, 0.8, 0.0,   # Gold
     0.5,  0.5, -0.5,   1.0, 0.0, 0.0,   # Red

    -0.5,  0.5, -0.5,   0.0, 0.0, 1.0,   # Blue (Thor - Top face)
     0.5,  0.5, -0.5,   0.6, 0.6, 0.6,   # Silver
     0.5,  0.5,  0.5,   0.6, 0.6, 0.6,   # Silver
    -0.5,  0.5,  0.5,   0.0, 0.0, 1.0,   # Blue

    -0.5, -0.5, -0.5,   1.0, 0.0, 0.0,   # Red (Spider-Man - Bottom face)
     0.5, -0.5, -0.5,   0.0, 0.0, 1.0,   # Blue
     0.5, -0.5,  0.5,   1.0, 0.0, 0.0,   # Red
    -0.5, -0.5,  0.5,   0.0, 0.0, 1.0    # Blue
]


# Indices for drawing cube faces
indices = [
    0, 1, 2, 2, 3, 0,  # Back face
    4, 5, 6, 6, 7, 4,  # Front face
    0, 4, 7, 7, 3, 0,  # Left face
    1, 5, 6, 6, 2, 1,  # Right face
    3, 2, 6, 6, 7, 3,  # Top face
    0, 1, 5, 5, 4, 0   # Bottom face
]

# Initialize GLFW
if not glfw.init():
    raise Exception("GLFW could not be initialized!")

window = glfw.create_window(800, 600, "Rotating 3D Cube", None, None)
if not window:
    glfw.terminate()
    raise Exception("GLFW window could not be created!")

glfw.make_context_current(window)

# Compile shaders and create program
shader = compileProgram(
    compileShader(vertex_src, GL_VERTEX_SHADER),
    compileShader(fragment_src, GL_FRAGMENT_SHADER)
)

# Convert data to numpy arrays
vertices = np.array(vertices, dtype=np.float32)
indices = np.array(indices, dtype=np.uint32)

# Create and bind Vertex Array Object and buffers
VAO = glGenVertexArrays(1)
VBO = glGenBuffers(1)
EBO = glGenBuffers(1)

glBindVertexArray(VAO)

glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

# Enable vertex attributes
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
glEnableVertexAttribArray(0)

glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
glEnableVertexAttribArray(1)

glUseProgram(shader)

# Set the rotation uniform
rotation_loc = glGetUniformLocation(shader, "rotation")

# Enable depth testing
glEnable(GL_DEPTH_TEST)

# Main application loop
angle = 0.0
while not glfw.window_should_close(window):
    glfw.poll_events()
    
    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Calculate rotation
    angle += 0.01
    rotation = np.array([
        [math.cos(angle), 0, math.sin(angle), 0],
        [0, 1, 0, 0],
        [-math.sin(angle), 0, math.cos(angle), 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)
    
    # Send rotation to the shader
    glUniformMatrix4fv(rotation_loc, 1, GL_FALSE, rotation)
    
    # Draw the cube
    glBindVertexArray(VAO)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)
    
    glfw.swap_buffers(window)

# Terminate GLFW
glfw.terminate()
