import pygame  

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
        self.leftKey  = pygame.K_LEFT
        self.rightKey = pygame.K_RIGHT
        self.upKey    = pygame.K_UP 
        self.downKey  = pygame.K_DOWN


    def update(self, dt):
        movement = pygame.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if (keys[self.leftKey]):  movement.x -= 1
        if (keys[self.rightKey]): movement.x += 1
        if (keys[self.upKey]):    movement.y -= 1
        if (keys[self.downKey]):  movement.y += 1

        # normalize diagonal movement
        if movement.x != 0 and movement.y != 0:
            movement = movement.normalize()
        
        self.rect.move_ip(movement * self.speed * dt)

    def setKeys(self, up, down, left, right):
        self.upKey    = up
        self.downKey  = down
        self.leftKey  = left
        self.rightKey = right