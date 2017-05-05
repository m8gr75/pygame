import pygame

import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
DKGREEN = (0, 100, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        height = 15
        width = 15
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pygame.init()
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Move Sprite With Keyboard')

player = Player(150, 50)

all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(player)
clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= player.rect.width
            elif event.key == pygame.K_RIGHT:
                player.rect.x += player.rect.width
            elif event.key == pygame.K_UP:
                player.rect.y -= player.rect.height
            elif event.key == pygame.K_DOWN:
                player.rect.y += player.rect.height

    # -- Draw everything
    # Clear screen
    screen.fill(WHITE)

    # Draw sprites
    all_sprite_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(40)

pygame.quit()
