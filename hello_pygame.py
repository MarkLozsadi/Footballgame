import pygame

def main():
    # Initialize Pygame
    pygame.init()
    
    # Create window: width × height
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mark's Football game!")
    
    footballField = pygame.image.load("images/footballField.png").convert()
    footballField = pygame.transform.scale(footballField, (800,600))
    p1 = pygame.image.load("images/Ronaldo.png").convert_alpha()
    p1 = pygame.transform.scale(p1, (80,80))

    screen.blit(footballField, (0,0))

    # Main loop control flag
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(p1, (100,100))

        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
