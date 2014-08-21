import pygame, sys, os

class unit(pygame.sprite.Sprite):
    def __init__(self, name, filePath, maxHP):
        self.x = 0
        self.y = 205
        self.idleList = []
        self.walkList = []
        self.index = 0
        self.walkIndex = 0
        self.counter = 0
        self.isFlipped = False
        self.name = name
        self.maxHP = maxHP
        self.currentHP = maxHP
        self.isHit = False
        self.rect = pygame.Rect(self.x,self.y, 56,128)
        self.hitCounter = 16
        self.bounceCounter = 10
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


    def bounceBack(self): #Bounceback distance etc
        if self.bounceCounter > 0:
            if self.bounceCounter >= 5:
                self.y -= 5
            else:
                self.y += 5
            self.x -= 10 #Speed Of bounceBack
            self.bounceCounter -= 1





    def immuneCount(self): #Countdown for "hit" state.
        self.isHit = True

        if self.hitCounter > 0 and self.currentHP:
            self.hitCounter -= 1
        else:
            self.hitCounter = 16
            self.isHit = False

    def update(self, surface, imgList, x, y):

        self.x = x
        self.y = y


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
        
        self.rect = pygame.Rect(self.x,self.y, 56,128)

        if self.isFlipped == True:
        
            self.image = pygame.transform.flip(self.image, 1, 0)
        
        
        
        
        
        surface.blit(self.image, (self.x, self.y))
        
    