import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

vertexes = np.array([
[0.5, 0.0, 0.0],
[-0.5, 0.0, 0.0],
[0, 0.5, 0.0]], dtype=np.float32)

glBufferData(GL_ARRAY_BUFFER, vertexes.nbytes, vertexes, GL_STATIC_DRAW)
