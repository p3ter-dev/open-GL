import pygame
import sys

def main():
    
    pygame.init()

    
    width, height = 500, 400

    
    screen = pygame.display.set_mode((width, height))


    pygame.display.set_caption("My Pygame Canvas")

   
    white = (255, 255, 255)
    screen.fill(white)

 
    pygame.display.flip()

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    running = False


    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()