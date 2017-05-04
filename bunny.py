import pygame
from pygame.locals import *
import math
#http://greenteapress.com/thinkpython/html/index.html
# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

# 3 - Load images
player = pygame.image.load("dude.png")
keys = [False, False, False, False]
playerpos=[100,100]

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)

    # 7 - update the screen

    # 8 - loop through the events

        # check if the event is the X button
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        else:
            if event.type == pygame.KEYDOWN:

                if event.key==pygame.K_UP:
                    keys[0]=True
                elif event.key==pygame.K_LEFT:
                    keys[1]=True
                elif event.key==pygame.K_DOWN:
                    keys[2]=True
                elif event.key==pygame.K_RIGHT:
                   keys[3]=True
            if event.type == pygame.KEYUP:

                if event.key==pygame.K_UP:
                    keys[0]=False
                elif event.key==pygame.K_LEFT:
                    keys[1]=False
                elif event.key==pygame.K_DOWN:
                   keys[2]=False
                elif event.key==pygame.K_RIGHT:
                  keys[3]=False


    if keys[0]:
        playerpos[1]-=2

    elif keys[2]:
        playerpos[1]+=2
    if keys[1]:
        playerpos[0]-=2
    elif keys[3]:
        playerpos[0]+=2

    screen.blit(playerrot, playerpos1)
    pygame.display.flip()
