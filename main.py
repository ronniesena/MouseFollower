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
    
    ronnie = unit.unit("ronnie", IMAGES_DIR + "ronnie")
    rob    = unit.unit("rob", IMAGES_DIR + "rob")
    alyssa = unit.unit("alyssa", IMAGES_DIR + "alyssa")
    zoe    = unit.unit("zoe", IMAGES_DIR + "zoe")

    player = ronnie
    
    robsHouse = scene.scene(IMAGES_DIR + "background.png")
    tv = pygame.image.load(IMAGES_DIR + "tvback.png")
    counter = 0
   
    
    while 1:
        msElapse = clock.tick(30)
        Mouse.update()
        useList = player.idleList
        key = pygame.key.get_pressed()
        
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
                    robsHouse.pressed = False
                
        
            
                    
        
             
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
      
        
        
        
            
        print player.x,  player.y
        print robsHouse.zCounter
  
        
        #TODO: IF THERE IS NO MSG AVAILABLE DONT PRINT THE TEXT BOX..
            
       

        
                
                
        player.update(screen, useList)
        screen.blit(tv, (380,305))
        if robsHouse.pressed == True:
            robsHouse.printText(screen, player)
        
        
        
        
        
        
        pygame.display.flip()
if __name__ == '__main__': 
        main()
    