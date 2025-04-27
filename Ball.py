import pygame

class Ball(pygame.sprite.Sprite):
    sizeX = 14
    sizeY = 14
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
        self.mask = pygame.mask.from_surface(self.image)
        self.startX = pos[0]
        self.startY = pos[1]
        self.resetWanted = False

    def update(self, dt):
        if (self.resetWanted):
            self.rect.move(self.startX, self.startY)
            self.actualSpeed = 0
            self.movement.x = 0
            self.movement.y = 0
            self.resetWanted = False
            return

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
    
    def resetBall(self):
        self.resetWanted = True
        

        
