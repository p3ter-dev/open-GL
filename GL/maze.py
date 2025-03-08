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
    glutSolidCube(1)
    glPopMatrix()

def render_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                draw_cube(col, 0, row)

player_x, player_z = 1.5, 1.5

def move_player(key):
    global player_x, player_z
    step = 0.1

    if key == glfw.KEY_W:
        if maze[int(player_z - step)][int(player_x)] == 0:
            player_z -= step
    if key == glfw.KEY_S:
        if maze[int(player_z + step)][int(player_x)] == 0:
            player_z += step
    if key == glfw.KEY_A:
        if maze[int(player_z)][int(player_x - step)] == 0:
            player_x -= step
    if key == glfw.KEY_D:
        if maze[int(player_z)][int(player_x + step)] == 0:
            player_x += step


glfw.set_key_callback(window, move_player)

def update_camera():
    glLoadIdentity()
    gluLookAt(player_x, 1.0, player_z,
              player_x, 1.0, player_z - 1,
              0.0, 1.0, 0.0)

def check_win():
    exit_x, exit_z = 3.5, 3.5
    if abs(player_x - exit_x) < 0.1 and abs(player_z - exit_z) < 0.1:
        print("You win!")
        glfw.set_window_should_close(window, True)
