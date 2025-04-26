import pygame  
from Ball import Ball
import copy

class Player(pygame.sprite.Sprite):
    sizeX = 60
    sizeY = 82

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
        self.others   = pygame.sprite.Group()
        self.movement = pygame.Vector2(0, 0)
        self.mask     = pygame.mask.from_surface(self.image)


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
        
        self.movement.x *= self.speed * dt
        self.movement.y *= self.speed * dt

        self.handle_collisions()
        self.move()
        


    def setKeys(self, up, down, left, right):
        self.upKey    = up
        self.downKey  = down
        self.leftKey  = left
        self.rightKey = right
    
    def setOtherSprites(self, sprites:pygame.sprite.Group):
        self.others = sprites.copy()
        self.others.remove(self)

    def handle_collisions(self):
        # Player vs. Enemies
        for sp in pygame.sprite.spritecollide(self, self.others, dokill=False):
            if sp is self:
                continue
            elif (isinstance(sp, Ball)):
                pass
    
    def move(self):
        # 1) Try the X move
        if (self.movement.x != 0):
            clone = self.shallow_clone()
            clone.rect.move_ip(self.movement.x, 0)  # create a “would‐be” rect
            for sp in pygame.sprite.spritecollide(clone, self.others, dokill=False, collided=pygame.sprite.collide_mask):
                if isinstance(sp, Ball):
                    continue
                self.movement.x = 0  # X‐movement blocked: zero it out

        # 2) Try the Y move
        if (self.movement.y != 0):
            clone = self.shallow_clone()
            clone.rect.move_ip(self.movement.y, 0)  # create a “would‐be” rect
            for sp in pygame.sprite.spritecollide(clone, self.others, dokill=False, collided=pygame.sprite.collide_mask):
                if isinstance(sp, Ball):
                    continue
                self.movement.y = 0  # y‐movement blocked: zero it out
        self.rect.move_ip(self.movement)

    def _make_temp_moved_sprite(self, rect, x, y):
        
        temp = copy.deepcopy()
        temp.rect = rect
        return temp
    
    def shallow_clone(self):
        new = copy.copy(self)                # copies the object, but references same image/rect/etc
        #new.image = sprite.image.copy()        # now give it its own Surface
        new.rect  = self.rect.copy()         # and its own Rect
        new.mask  = self.mask.copy()         # and its own Mask
        # copy other mutable attrs as needed…
        return new
