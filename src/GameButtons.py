import pygame

class ControlButton:
    def __init__(self,imgPath,aspectRatio,height) -> None:
        self.imgPath = imgPath
        self.aspectRatio = aspectRatio
        self.h = height
        self.w = int(self.aspectRatio * self.h)
        
        self.btnEntity = pygame.image.load(self.imgPath).convert()
        self.btnEntity = pygame.transform.scale(self.btnEntity,(self.w,self.h))
    def spawn(self,screen,x,y):
        self.x=x
        self.y = y
        screen.blit(self.btnEntity,(x,y))
    def isClicked(self,mouse_pos):
        if (mouse_pos[0] >= self.x and mouse_pos[0] <= (self.x+self.w) and mouse_pos[1] >= self.y and mouse_pos[1] <= (self.y+self.h)):
            return True
        return False