import pygame
import sys

def main():
    pygame.init()
    width, height = 500, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Triangle Shape")
    white = (255, 255, 255)
    screen.fill(white)
    blue = (0, 0, 255)
    top_triangle = [(250, 100), (200, 200), (300, 200)] 
    bottom_left_triangle = [(200, 200), (150, 300), (250, 300)]  
    bottom_right_triangle = [(300, 200), (250, 300), (350, 300)]
    pygame.draw.polygon(screen, blue, top_triangle)
    pygame.draw.polygon(screen, blue, bottom_left_triangle)
    pygame.draw.polygon(screen, blue, bottom_right_triangle) 
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
