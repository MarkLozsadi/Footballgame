
import sys
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
        self.side = side.lower()
        if (side.lower() == "left"):
            self.rect = pygame.Rect(Net.leftPosX, Net.posY, Net.sizeX, Net.sizeY)
        elif (side.lower() == "right"):
            self.rect = pygame.Rect(Net.rightPosX, Net.posY, Net.sizeX, Net.sizeY)
        else:
            print("The Net does not have a aproper left/right side parameter!")
            sys.exit(1)
        self.image = pygame.Surface((0, 0), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.others = []
        self.goalCounter = 0
        self.BallPartiallyIn = False
        self.label = None

    def update(self, dt):
        for sp in pygame.sprite.spritecollide(self, self.others, dokill=False):
            if isinstance(sp, Ball):
                if (self.goal(sp)):
                    self.goalCounter += 1
                    sp.resetBall()
                    self.BallPartiallyIn = False
                    self.updateLabel()
                self.checkBallCollisionToNet(sp)

    def setOtherSprites(self, sprites:pygame.sprite.Group):
        self.others = sprites.copy()
        self.others.remove(self)

    def checkBallCollisionToNet(self, ball:Ball):
        if (self.rect.colliderect(ball.rect)):
            overlap = ball.rect.clip(self.rect)
            if (overlap.width < overlap.height):
                if (self.BallPartiallyIn):
                    pass
                # → we overlapped more vertically than horizontally,
                #    so it’s a left/right “side” collision
                elif (ball.rect.centerx < self.rect.centerx):
                    # Hit the net’s left side!
                    if (self.side == "left"):
                        ball.rect.x = Net.leftPosX - ball.sizeX
                    if (self.side == "right"):
                        self.BallPartiallyIn = True
                else:
                    # Hit the net’s right side!
                    if (self.side == "left"):
                        self.BallPartiallyIn = True
                    if (self.side == "right"):
                        ball.rect.x = Net.rightPosX 
            else:
                # → we overlapped more horizontally, so it’s a top/bottom hit
                if (ball.rect.centery < self.rect.centery):
                    # Hit the net’s top face (front)!
                    ball.rect.y = Net.posY - ball.sizeY
                else:
                    # Hit the net’s bottom face (back)!
                    ball.rect.y = Net.posY + Net.sizeY
        else:
            self.BallPartiallyIn = False



    def goal(self, ball:Ball):
        ballUpperRightX = ball.rect.x + ball.rect.width
        ballUpperRightY = ball.rect.y
        ballLowerRightY = ball.rect.y + ball.rect.height
        netUpperRightX  = self.rect.x + self.rect.width 
        netUpperRightY  = self.rect.y
        netLowerRightX  = self.rect.y + self.rect.height
        
        # check if the ball is fully in the net
        if ((netUpperRightX >= ballUpperRightX) 
            and self.rect.x <= ball.rect.x
            and netUpperRightY <= ballUpperRightY
            and netLowerRightX >= ballLowerRightY):
            return True  
        return False
    
    def setGoalCounterLabel(self, label:pygame.sprite.Sprite):
        self.label = label
    
    def updateLabel(self):
        if (self.label is not None):
            self.label.set(self.label.initialText + str(self.goalCounter))