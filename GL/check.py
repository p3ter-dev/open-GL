import pygame
from OpenGL.GL import glGetString, GL_VERSION

pygame.init()
pygame.display.set_mode((1, 1), pygame.OPENGL | pygame.DOUBLEBUF)

version = glGetString(GL_VERSION)
print(f"OpenGL version: {version.decode()}")
