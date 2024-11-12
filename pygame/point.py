import pygame

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point in Peter's Pygame")

black = (0, 0, 0)
white = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    window.fill(black)
    pygame.draw.circle(window, white, (400, 300), 1)
    pygame.display.flip()

pygame.quit()
