import pygame
from Player import Player
from Ball import Ball
from Net import Net
from TextLabel import TextLabel 

def main():
    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Create window: width × height
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mark's Football game!")
    
    footballField = pygame.image.load("images/footballField.png").convert()
    footballField = pygame.transform.scale(footballField, (800,600))
    
    p1 = Player("images/Ronaldo.png", (150, 300))
    p2 = Player("images/Messi.png",   (650, 300))
    p2.setKeys(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE)
    ball = Ball("images/ball.png", (screen.get_rect().centerx, screen.get_rect().centery))
    leftNet  = Net("left")
    rightNet = Net("right")
    p1GoalCount = TextLabel("arial", 36, pos=(70, 0),  initial_value="Ronaldo = ")
    p2GoalCount = TextLabel("arial", 36, pos=(580, 0), initial_value="Messi = ")
    leftNet.setGoalCounterLabel(p2GoalCount)
    rightNet.setGoalCounterLabel(p1GoalCount)

    sprites = pygame.sprite.Group(p1, p2, ball, leftNet, rightNet, p1GoalCount, p2GoalCount)
    
    p1.setOtherSprites(sprites)
    p2.setOtherSprites(sprites)
    leftNet.setOtherSprites(sprites)
    rightNet.setOtherSprites(sprites)

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
