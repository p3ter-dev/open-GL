import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math

maze = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]



def draw_cube(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glutSolidCube(1)  # Requires PyOpenGL and GLUT
    glPopMatrix()

def render_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:  # Draw walls
                draw_cube(col, 0, row)  # Translate based on grid position
# Player position
player_x, player_z = 1.5, 1.5  # Start inside the maze

def move_player(key):
    global player_x, player_z
    step = 0.1  # Movement step size

    if key == glfw.KEY_W:  # Move forward
        if maze[int(player_z - step)][int(player_x)] == 0:  # Check collision
            player_z -= step
    if key == glfw.KEY_S:  # Move backward
        if maze[int(player_z + step)][int(player_x)] == 0:
            player_z += step
    if key == glfw.KEY_A:  # Move left
        if maze[int(player_z)][int(player_x - step)] == 0:
            player_x -= step
    if key == glfw.KEY_D:  # Move right
        if maze[int(player_z)][int(player_x + step)] == 0:
            player_x += step

# Register the key callback
glfw.set_key_callback(window, move_player)

def update_camera():
    glLoadIdentity()
    gluLookAt(player_x, 1.0, player_z,  # Eye position
              player_x, 1.0, player_z - 1,  # Look-at position
              0.0, 1.0, 0.0)  # Up direction

def check_win():
    exit_x, exit_z = 3.5, 3.5  # Exit position
    if abs(player_x - exit_x) < 0.1 and abs(player_z - exit_z) < 0.1:
        print("You win!")
        glfw.set_window_should_close(window, True)
