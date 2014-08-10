import sys, os, pygame, mouse, unit, scene
pygame.init()
def main():

    clock = pygame.time.Clock()
    IMAGES_DIR = os.getcwd() + "\\images\\"
    icon = pygame.image.load(IMAGES_DIR + "icon.png")
    pygame.display.set_icon(icon)
    reso = (640,480)
    screen = pygame.display.set_mode(reso)
    pygame.display.set_caption(".::TEAL CONCRETE::.")
    Mouse = mouse.mouse()
    
    ronnie = unit.unit("ronnie", IMAGES_DIR + "ronnie",10)
    rob    = unit.unit("rob", IMAGES_DIR + "rob",10)
    alyssa = unit.unit("alyssa", IMAGES_DIR + "alyssa",10)
    zoe    = unit.unit("zoe", IMAGES_DIR + "zoe",10)
    monster= unit.unit("monster",  IMAGES_DIR + "monster", 5)
    monster.x = 340
    charSelected = False
    
    
    garage = scene.scene(IMAGES_DIR + "garage.png")
    robsHouse = scene.scene(IMAGES_DIR + "background.png")
    tv = pygame.image.load(IMAGES_DIR + "tvback.png")
    arrow = pygame.image.load(IMAGES_DIR + "arrow.png")
    
    
    
    counter = 0
   
    def isHit(): #TRYING TO CREATE A STATE OF INVISIBLITY WHEN HIT.. 
        hitCounter = 5
        if player.rect.colliderect(monster.rect) or hitCounter > 0:
            hitCounter -= 1
            return True
            
        else:
            return False
        
        
    
    
    
    def charSelection():
        
        fontType = pygame.font.SysFont("Pixelated Regular", 55)
        textbox = pygame.image.load(IMAGES_DIR + "textbox.png")
        
        
        garage.update(screen)
        ronnie.isFlipped = True
        
        ronnie.update(screen, ronnie.idleList, 475, 300)
        
        rob.update(screen, rob.idleList, 100, 280)
        
        alyssa.update(screen, alyssa.idleList, 380, 260)
        
        zoe.update(screen, zoe.idleList, 260, 240)
    
        screen.blit(textbox, (25,5))
        screen.blit(fontType.render("SELECT YOUR CHARACTER", 0, (0,0,0,)), (55,45))
    
    
    arrowCoord = [(130,210), (290,170), (410, 190), (480, 230)]
    arrowIndex = 0
    
    
    
    
    
    
    
    while 1:
        msElapse = clock.tick(30)
        Mouse.update()
        
        key = pygame.key.get_pressed()
        
        #Character Selection Screen
        if charSelected == False:
            
            
            charSelection()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_RIGHT:
                        if arrowIndex < 3:
                            arrowIndex += 1
                    elif event.key == pygame.K_LEFT:
                        if arrowIndex > 0:
                            arrowIndex -= 1
                        
            
                    if event.key == pygame.K_z:
                        if arrowIndex == 0:
                            player = rob
                        elif arrowIndex == 1:
                            player = zoe
                        elif arrowIndex == 2:
                            player = alyssa
                        elif arrowIndex == 3:
                            player = ronnie
                            
                        player.health = 10
                        charSelected = True
                        player.x = 0
                        player.y = 205            
            
            screen.blit(arrow, arrowCoord[arrowIndex])
            
            
        #Main Game 
        else:
            useList = player.idleList
            robsHouse.update(screen)
            robsHouse.checkIfMsg(player)
            
        
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                        
                    if event.key == pygame.K_z and robsHouse.pressed == False and robsHouse.msgAvail == True:
                        robsHouse.pressed = True
                    elif event.key == pygame.K_z and robsHouse.pressed == True:
                        robsHouse.list1 = []
                        robsHouse.list2 = []
                        #robsHouse.text = ""
                        robsHouse.textCounter = 0
                        robsHouse.pressed = False
                        
                    elif event.key == pygame.K_ESCAPE:
                        charSelected = False
                    elif event.key == pygame.K_f:
                        player.health -= 5
                    
            
                
                        
            
                 
            #If "z" isnt pressed down, then move.. if not you cant move
            if robsHouse.pressed == False:     
                if key[pygame.K_RIGHT]:
                    if player.x < (reso[0] - 128):
                        player.isFlipped = False
                        useList = player.walkList
                        player.x += 10
                elif key[pygame.K_LEFT]:
                    if player.x > 0:
                        player.isFlipped = True
                        useList = player.walkList
                        player.x -= 10
                    
                if key[pygame.K_UP]:
                    if player.y > 205:
                        useList = player.walkList
                        player.y -= 5
                elif key[pygame.K_DOWN]:
                    if player.y < 355:
                        useList = player.walkList
                        player.y += 5
          
            
            if player.health <= 0:
                charSelected = False
                                
            
                
            monster.update(screen, monster.idleList, monster.x, monster.y)
            
            player.update(screen, useList, player.x, player.y)
            
            if player.rect.colliderect(monster.rect):
                player.health -= 1
                player.x -= 20
            screen.blit(tv, (380,305))
            #TRYING TO MAKE YOU GET KNOCKED BACKIF YOU HIT AN ENEMY
            if robsHouse.pressed == True:
                robsHouse.printText(screen, player)
            
            
                
            
            print player.health
            print player.rect
            print monster.rect
            
        
        
        
        pygame.display.flip()
if __name__ == '__main__': 
        main()
    