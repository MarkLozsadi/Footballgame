import pygame  
from Ball import Ball
import copy

class Player(pygame.sprite.Sprite):
    sizeX = 30
    sizeY = 41

    hasBallSpeedFactor = 0.7

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
        self.shootKey = pygame.K_RCTRL
        self.others   = pygame.sprite.Group()
        self.movement = pygame.Vector2(0, 0)
        self.mask     = pygame.mask.from_surface(self.image)
        self.wantToShoot = False

    def update(self, dt):
        self.movement = pygame.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if (keys[self.leftKey]):  self.movement.x -= 1
        if (keys[self.rightKey]): self.movement.x += 1
        if (keys[self.upKey]):    self.movement.y -= 1
        if (keys[self.downKey]):  self.movement.y += 1
        if (keys[self.shootKey]): self.wantToShoot = True

        # normalize diagonal movement
        if self.movement.x != 0 and self.movement.y != 0:
            self.movement = self.movement.normalize()
        
        self.movement.x *= self.speed * dt
        self.movement.y *= self.speed * dt

        self.move()
        self.wantToShoot = False
        
    def setKeys(self, up, down, left, right, shoot):
        self.upKey    = up
        self.downKey  = down
        self.leftKey  = left
        self.rightKey = right
        self.shootKey = shoot
    
    def setOtherSprites(self, sprites:pygame.sprite.Group):
        self.others = sprites.copy()
        self.others.remove(self)
               
    def move(self):
        ballNeedToMove = False
        ball = None
        if (self.movement.x != 0 or self.movement.y != 0):
            clone = self.shallow_clone()
            clone.rect.move_ip(self.movement.x, self.movement.y)  # create a “would‐be” rect
            for sp in pygame.sprite.spritecollide(clone, self.others, dokill=False, collided=pygame.sprite.collide_mask):
                if isinstance(sp, Ball):
                    ballNeedToMove = True
                    ball = sp
                else:
                    self.movement.x = 0  # X‐movement blocked: zero it out
                    self.movement.y = 0  # Y‐movement blocked: zero it out
            if (ballNeedToMove):
                if (self.wantToShoot):
                    ball.shot(self.movement.x, self.movement.y)
                else:
                    self.movement *= self.hasBallSpeedFactor
                    ball.rect.move_ip(self.movement.x, self.movement.y)

        self.rect.move_ip(self.movement)
    
    def shallow_clone(self):
        new = copy.copy(self)                # copies the object, but references same image/rect/etc
        #new.image = sprite.image.copy()        # now give it its own Surface
        new.rect  = self.rect.copy()         # and its own Rect
        new.mask  = self.mask.copy()         # and its own Mask
        # copy other mutable attrs as needed…
        return new
