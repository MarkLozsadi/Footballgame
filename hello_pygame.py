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
            
        dt = clock.tick(30) / 1000.0 # to get seconds
        sprites.clear(screen, footballField)
        sprites.update(dt)
        sprites.draw(screen)

        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()


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
        self.speed = 150

    def update(self, dt):
        movement = pygame.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT]):  movement.x -= 1
        if (keys[pygame.K_RIGHT]): movement.x += 1
        if (keys[pygame.K_UP]):    movement.y -= 1
        if (keys[pygame.K_DOWN]):  movement.y += 1

        # normalize diagonal movement
        if movement.x != 0 and movement.y != 0:
            movement = movement.normalize()
        
        self.rect.move_ip(movement * self.speed * dt)

if __name__ == "__main__":
    main()
