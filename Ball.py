import pygame

class Ball(pygame.sprite.Sprite):
    sizeX = 24
    sizeY = 24
    
    def __init__(self, image_path, pos):
        super().__init__()  # initialize the base Sprite
        # load and store the image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (Ball.sizeX, Ball.sizeY))
        # create a rect for positioning
        self.rect = self.image.get_rect(center=pos)
        self.speed = 0


    def update(self, dt):
        movement = pygame.Vector2(0, 0)
        # normalize diagonal movement
        if movement.x != 0 and movement.y != 0:
            movement = movement.normalize()
        self.rect.move_ip(movement * self.speed * dt)
