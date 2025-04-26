import pygame
from Player import Player
from Ball import Ball

def main():
    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Create window: width × height
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mark's Football game!")
    
    footballField = pygame.image.load("images/footballField.png").convert()
    footballField = pygame.transform.scale(footballField, (800,600))
    
    p1 = Player("images/Ronaldo.png", (100, 100))
    p2 = Player("images/Messi.png",   (400, 400))
    p2.setKeys(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE)

    ball = Ball("images/ball.png", (screen.get_rect().centerx, screen.get_rect().centery))

    sprites = pygame.sprite.Group(p1, p2, ball)

    p1.setOtherSprites(sprites)
    p2.setOtherSprites(sprites)

    screen.blit(footballField, (0,0))

    # Main loop control flag
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        dt = clock.tick(30) / 1000.0 # to get seconds
        sprites.clear(screen, footballField)
        sprites.update(dt)
        sprites.draw(screen)

        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
