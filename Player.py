import pygame  
from Ball import Ball
class Player(pygame.sprite.Sprite):
    sizeX = 80
    sizeY = 80

    def __init__(self, image_path, pos):
        super().__init__()  # initialize the base Sprite
        # load and store the image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (Player.sizeX, Player.sizeY))
        # create a rect for positioning
        self.rect = self.image.get_rect(center=pos)
        self.speed = 150.0
        self.leftKey  = pygame.K_LEFT
        self.rightKey = pygame.K_RIGHT
        self.upKey    = pygame.K_UP 
        self.downKey  = pygame.K_DOWN
        self.others   = []
        self.movement = pygame.Vector2(0, 0)


    def update(self, dt):
        self.movement = pygame.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if (keys[self.leftKey]):  self.movement.x -= 1
        if (keys[self.rightKey]): self.movement.x += 1
        if (keys[self.upKey]):    self.movement.y -= 1
        if (keys[self.downKey]):  self.movement.y += 1

        # normalize diagonal movement
        if self.movement.x != 0 and self.movement.y != 0:
            self.movement = self.movement.normalize()
        
        self.handle_collisions()
        self.rect.move_ip(self.movement * self.speed * dt)


    def setKeys(self, up, down, left, right):
        self.upKey    = up
        self.downKey  = down
        self.leftKey  = left
        self.rightKey = right
    
    def setOtherSprites(self, spriteGroup):
        self.others = spriteGroup

    def handle_collisions(self):
        # Player vs. Enemies
        for sp in pygame.sprite.spritecollide(self, self.others, dokill=False):
            if (isinstance(sp, Player)):
                self.movement = (0,0)
            elif (isinstance(sp, Ball)):
                pass