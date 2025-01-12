import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glEnd()

def main():
    pygame.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(-1, 1, -1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)

        draw_triangle()

        pygame.display.flip()

        pygame.time.wait(10)
main()