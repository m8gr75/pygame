import pygame
from pygame.locals import*
import random
import sys

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ADDENEMY = pygame.USEREVENT + 3
size = [700, 500]
screen_width = 700
screen_height = 500
pygame.time.set_timer(ADDENEMY, 2000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("USER EVENT")
clock = pygame.time.Clock()
done = True
missing = True
list1 = []
count = 0
fontobj = pygame.font.Font("freesansbold.ttf", 15)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super(Enemy, self).__init__()
        self.miss = 0
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.ellipse(self.image,color, [0,0,width,height])

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect(center=(
            random.randint(0, 700), random.randint(200, 500))
        )


    def update(self):
        self.rect.move_ip(0, -3)
        if self.rect.top < 0:
            missing = False
            list1.append(1)
            self.kill()

            #print missing
            #return missing





class Player(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super(Player, self).__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #pygame.draw.rect(self.image, color, (200, 200), (width, height))
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y

        self.rect = self.image.get_rect()
        self.rect.topleft = [100, 0]

        """ Called each frame. """
    def update(self, pressed_keys):


        if pressed_keys[K_LEFT]:
            if self.rect.left >= 0:
                self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)

            # Keep player on the screen
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 700:
                self.rect.right = 700
            if self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom >= 500:
                self.rect.bottom = 500

all_sprites_list = pygame.sprite.Group()
enemy_sprites_list = pygame.sprite.Group()


#    enemy = Enemy(WHITE, 20, 15)

#    enemy.rect.x = random.randrange(screen_width)
#    enemy.rect.y = random.randrange(screen_height)

#    enemy_sprites_list.add(enemy)
#    all_sprites_list.add(enemy)


player = Player(WHITE, 35, 15)
all_sprites_list.add(player)


conto = 0

while done:
    screen.fill(BLACK)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = False
        elif event.type == ADDENEMY:

            enemy= Enemy(WHITE, 20, 15)
            enemy_sprites_list.add(enemy)
            all_sprites_list.add(enemy)
            #enemy.update()


    # Limit to 20 frames per second

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemy_sprites_list.update()

    x = sum(list1)

    textS= fontobj.render("Missing: " + str(x), True, WHITE)

    screen.blit(textS, (400, 400))
    all_sprites_list.draw(screen)
    pygame.display.flip()

    # Go ahead and update the screen with what we've drawn.

    clock.tick(10)
