import pygame
from Ball import Ball

class Net(pygame.sprite.Sprite):
    
    sizeX = 22
    sizeY = 98
    posY  = 250
    leftPosX  = 26
    rightPosX = 754

    def __init__(self, side:str):
        super().__init__()  # initialize the base Sprite
        # load and store the image
        if (side.lower() == "left"):
            self.rect = pygame.Rect(Net.leftPosX, Net.posY, Net.sizeX, Net.sizeY)
        elif (side.lower() == "right"):
            self.rect = pygame.Rect(Net.rightPosX, Net.posY, Net.sizeX, Net.sizeY)
        self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.others = []
        self.goalCounter = 0

    def update(self, dt):
        for sp in pygame.sprite.spritecollide(self, self.others, dokill=False):
            if isinstance(sp, Ball):
                if (self.goal(sp)):
                    self.goalCounter += 1
                    sp.resetBall()

    def setOtherSprites(self, sprites:pygame.sprite.Group):
        self.others = sprites.copy()
        self.others.remove(self)

    def goal(self, ball:Ball):
        ballUpperRightX = ball.rect.x + ball.rect.width
        ballUpperRightY = ball.rect.y
        ballLowerRightY = ball.rect.y + ball.rect.height
        netUpperRightX  = self.rect.x + self.rect.width 
        netUpperRightY  = self.rect.y
        netLowerRightX  = self.rect.y + self.rect.height
        
        # check if the ball is fully in the net
        if ((netUpperRightX > ballUpperRightX) 
            and self.rect.x < ball.rect.x
            and netUpperRightY < ballUpperRightY
            and netLowerRightX > ballLowerRightY):
            return True  
        return False
    
    
