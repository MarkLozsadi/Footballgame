import pygame

class Ball(pygame.sprite.Sprite):
    sizeX = 32
    sizeY = 32
    shotSpeed = 300
    deceleration = 8
    
    def __init__(self, image_path, pos):
        super().__init__()  # initialize the base Sprite
        # load and store the image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (Ball.sizeX, Ball.sizeY))
        # create a rect for positioning
        self.rect = self.image.get_rect(center=pos)
        self.movement = pygame.Vector2(0, 0)
        self.movement.x = 0
        self.movement.y = 0
        self.actualSpeed = 0

    def update(self, dt):
        # normalize diagonal movement
        if (self.movement.x != 0 or self.movement.y != 0):
            self.movement = self.movement.normalize()
        self.decelerateBall()
        self.rect.move_ip(self.movement * dt * self.actualSpeed)
    
    def shot(self, dx, dy):
        self.movement.x = dx
        self.movement.y = dy
        self.actualSpeed = Ball.shotSpeed

    def decelerateBall(self):
        self.actualSpeed -= Ball.deceleration
        if (self.actualSpeed <= 0):
            self.actualSpeed = 0
            self.movement.x = 0
            self.movement.y = 0

        
