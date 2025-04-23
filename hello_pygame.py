import pygame

def main():
    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Create window: width × height
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mark's Football game!")
    
    footballField = pygame.image.load("images/footballField.png").convert()
    footballField = pygame.transform.scale(footballField, (800,600))
    
    p1 = Player("images/Ronaldo.png", (100, 100), (80,80))
    p2 = Player("images/Messi.png",   (400, 400), (80,80))
    
    sprites = pygame.sprite.Group(p1, p2)
    screen.blit(footballField, (0,0))

    # Main loop control flag
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    p1.rect.x += p1.speed
                elif event.key == pygame.K_LEFT:
                    p1.rect.x -= p1.speed
                elif event.key == pygame.K_UP:
                    p1.rect.y -= p1.speed
                elif event.key == pygame.K_DOWN:
                    p1.rect.y += p1.speed
        
        
        dt = clock.tick(15) / 1000.0 # to get seconds
        sprites.clear(screen, footballField)
        sprites.update(dt)
        sprites.draw(screen)

        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()


def update_sprite(target_surf, image_surf, center_pos, angle):
    """
    Rotate image_surf by angle about its center, then blit it so that
    its center is at center_pos on target_surf.
    """
    # Rotate the image.
    rotated_image = pygame.transform.rotate(image_surf, angle)
    # Build a rect with the same center as where we want it on screen.
    new_rect = rotated_image.get_rect(center=center_pos)
    # Blit to screen.
    target_surf.blit(rotated_image, new_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, pos, resize=(0,0)):
        super().__init__()  # initialize the base Sprite
        # load and store the image
        self.image = pygame.image.load(image_path).convert_alpha()
        if (resize != (0,0)):
            self.image = pygame.transform.scale(self.image, resize)
        # create a rect for positioning
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0
        self.speed = 4

    def update(self, dt):
        # called once per frame; dt is the time since last frame
        # e.g. move right at 100 pixels/sec:
        #self.rect.x += 10 * dt
        pass


if __name__ == "__main__":
    main()
