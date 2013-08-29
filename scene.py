import pygame, os, sys, unit
 

class scene(object):
    def __init__(self, imgPath):
        IMAGES_DIR = os.getcwd() + "\\images\\"
        
        self.x = 0
        self.y = 0
        self.background = pygame.image.load(imgPath)
        self.key = pygame.key.get_pressed()
        self.pressed = False
        self.fontType = pygame.font.SysFont("Pixelated Regular", 30)
        self.textbox = pygame.image.load(IMAGES_DIR + "textbox.png")
        self.msgAvail = False
        
        self.ronnieCoffee = self.fontType.render("RONNIE: Ooh! French Vanilla!", 0, (0,0,0,))
        self.alyssaCoffee = self.fontType.render("ALYSSA: Yuck! There's sugar in this coffee!", 0, (0,0,0))
        #self.text = self.fontType.render(" ", 0, (0,0,0,))
        
    def update(self, surface):
    
        surface.blit(self.background, (0,0))
        


    def checkIfMsg(self, player):
        #COFFE DIALOG
        if (player.x >= 80 and player.x <= 140 and player.y == 205 and player.y == 205):
            if player.name == "ronnie":
                self.text = self.ronnieCoffee
            elif player.name == "alyssa":
                self.text = self.alyssaCoffee
            self.msgAvail = True
     
        
        
        
        
        
        else:
            self.msgAvail = False


    def printText(self, surface, player):
        if self.msgAvail == True:
            surface.blit(self.textbox, (10,320))
            surface.blit(self.text, (35,350))
        
       
                    
        
        
            

            
        