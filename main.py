import pygame,math,random
from map import coords,_W,_H
from Player import Player
from log import *

pygame.init()

def main():
    scr = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Bounce 2")
    clock = pygame.time.Clock()

    P_COORDS = (50,(H//2)+_H-109)
    player = Player(scr,P_COORDS)

  
    SPEED_WALLS = 5
    run = True
    while run:
        clock.tick(FPS)
        scr.fill("black")
        

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            elif i.type == pygame.KEYUP:
                player.vx=0 

        player.update()

        if int(player.coords[0]) >= W//2+30:
            SPEED_WALLS+=5
            [pygame.draw.rect(scr,"green",(x-SPEED_WALLS,y,_W,_H),1) for x,y in coords]
        else: 
            SPEED_WALLS = 5
            [pygame.draw.rect(scr,"green",(x,y,_W,_H),1) for x,y in coords]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and -1<player.v1<=0:
            player.v1+=1000
        if keys[pygame.K_LEFT]:
            player.vx=-500
        if keys[pygame.K_RIGHT]:
            player.vx=500
        print(player.coords[2])
        pygame.display.update()

        
        

    pygame.quit()

if __name__ == "__main__":
    main()