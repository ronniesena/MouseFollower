import pygame, os, sys, unit
 

class scene(object):
    def __init__(self, imgPath):
        self.IMAGES_DIR = os.getcwd() + "\\images\\"
        
        self.x = 0
        self.y = 0
        self.zCounter = 0
        self.printCounter = 0
        
        self.background = pygame.image.load(imgPath)
        self.key = pygame.key.get_pressed()
        self.pressed = False
        self.msgAvail = False
           
        self.textbox = pygame.image.load(self.IMAGES_DIR + "textbox.png")
        
        self.fontType = pygame.font.SysFont("Pixelated Regular", 30)

        self.ronnieCoffee = self.fontType.render("RONNIE: Ooh! French Vanilla!", 0, (0,0,0,))
        self.alyssaCoffee = self.fontType.render("ALYSSA: Yuck! There's sugar in this coffee!", 0, (0,0,0))
        #self.text = self.fontType.render(" ", 0, (0,0,0,))
        
    
    def update(self, surface):
    
        surface.blit(self.background, (0,0))
        


    def checkIfMsg(self, player):
        #COFFE DIALOG
        self.msgAvail = True
        if (player.x >= 80 and player.x <= 140 and player.y == 205 and player.y == 205):
            if player.name == "ronnie":
                self.text = self.ronnieCoffee
            elif player.name == "alyssa":
                self.text = self.alyssaCoffee
            else:
                self.msgAvail = False
                

                
                
                
            
        else:
            self.msgAvail = False


    def printText(self, surface, player):
        
        
        if self.zCounter <= 10:
            self.zBox = pygame.image.load(self.IMAGES_DIR + "zbutton.png")
        elif self.zCounter >= 10:
            self.zBox = pygame.image.load(self.IMAGES_DIR + "zbutton2.png")
            
        self.zCounter += 1
        if self.zCounter == 20:
            self.zCounter = 0
        
        
  
        
        
        
        
        if self.msgAvail == True:
            surface.blit(self.textbox, (10,320))
            surface.blit(self.text, (35,350))
            surface.blit(self.zBox,(570, 420))
        
       
                    
        
        
            

            
        