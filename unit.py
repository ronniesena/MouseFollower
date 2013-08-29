import pygame, sys, os

class unit(pygame.sprite.Sprite):
    def __init__(self, name, filePath):
        self.x = 0
        self.y = 205
        self.idleList = []
        self.walkList = []
        self.index = 0
        self.walkIndex = 0
        self.counter = 0
        self.isFlipped = False
        self.name = name

        
        #Load files to idleList
        for item in os.listdir(filePath + "\\idle"):
            tempImage = pygame.image.load(filePath + "\\idle\\" + item).convert()
            tempImage.set_colorkey((255,0,255))
            self.idleList.append(tempImage)
            
        #Load files to walkList
        for item in os.listdir(filePath + "\\walk"):
            tempImage = pygame.image.load(filePath + "\\walk\\" + item).convert()
            tempImage.set_colorkey((255,0,255))
            self.walkList.append(tempImage)
            
        
        
    def update(self, surface, imgList):
       
        
        
        
        #Using a counter to make the image switch slower.
        if self.counter == 10:
        
    
            if imgList == self.idleList:   
                self.index += 1
                if self.index >= len(imgList):
                    self.index = 0
                self.image = self.idleList[self.index]
                
                
                
            elif imgList == self.walkList:
                self.walkIndex += 1
                if self.walkIndex >= len(imgList):
                    self.walkIndex = 0
                self.image = self.walkList[self.walkIndex]
            
                    
            self.counter = 0
            
        self.counter += 1
        
        
        if imgList == self.walkList:
            self.image = imgList[self.walkIndex]
        elif imgList == self.idleList:
            self.image = imgList[self.index]
        
        
        if self.isFlipped == True:
        
            self.image = pygame.transform.flip(self.image, 1, 0)
        
        surface.blit(self.image, (self.x, self.y))
        
    