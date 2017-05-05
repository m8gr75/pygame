
import pygame
import sys, random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
DKGREEN = (0, 100, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
            super(Player, self).__init__()
            width = 20
            height = 15
            self.image= pygame.Surface([width, height])
            self.image.fill(RED)
            self.rect = self.image.get_rect()
    def update(self):
         pos = pygame.mouse.get_pos()
         x = pos[0]
         y = pos[1]
         self.rect.x = x
         self.rect.y = y




pygame.init()
size =[700, 500]
screen = pygame.display.set_mode(size)

pygame.mouse.set_visible(False)
done = False
clock = pygame.time.Clock()

player = Player()

all_sp_list= pygame.sprite.Group()
all_sp_list.add(player)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLACK)
    all_sp_list.update()
    all_sp_list.draw(screen)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
