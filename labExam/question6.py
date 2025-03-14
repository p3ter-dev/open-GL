from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    """
    Draws a line between two points (x1, y1) and (x2, y2) using OpenGL.
    """
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


if __name__ == "__main__":
    import pygame
    from pygame.locals import *

    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluOrtho2D(-400, 400, -300, 300)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)
        draw_line(-200, -100, 200, 100)
        pygame.display.flip()

    pygame.quit()
    