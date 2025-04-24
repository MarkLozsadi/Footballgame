import pygame  

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