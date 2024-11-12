import pygame as pg
import sys

pg.init()

width, height = 800, 600
window = pg.display.set_mode((width, height))
pg.display.set_caption("Pygame Window")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    window.fill((255, 255, 255))  
    pg.draw.circle(window, (0, 0, 0), (400, 50), 40)
    
    pg.display.flip()
print(pg.QUIT)
pg.quit()
sys.exit()
