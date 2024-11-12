import pygame
from OpenGL.GL import glGetString, GL_VERSION

# Initialize pygame and create an OpenGL context
pygame.init()
pygame.display.set_mode((1, 1), pygame.OPENGL | pygame.DOUBLEBUF)

# Retrieve and print the OpenGL version
version = glGetString(GL_VERSION)
print(f"OpenGL version: {version.decode()}")
