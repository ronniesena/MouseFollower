import pygame, sys

class mouse(object):
    def __init__(self):
        self.m1 = False
        
        
            
    def update(self):
        self.Mcoord = pygame.mouse.get_pos()
        self.Mcoordx = pygame.mouse.get_pos()[0] - 20
        self.Mcoordy = pygame.mouse.get_pos()[1] - 30
        
        
        #Mouse button 1 gets pressed
        if pygame.mouse.get_pressed()[0]:
            self.m1 = True
        else:
            self.m1 = False
            
            
        
        

        
    