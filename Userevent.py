import pygame
from pygame.locals import*
import random
import sys

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 127)
RED = (255, 0, 0)
ADDENEMY = pygame.USEREVENT + 3
size = [700, 500]
screen_width = 700
screen_height = 500
pygame.time.set_timer(ADDENEMY, 2000) #secondi
screen = pygame.display.set_mode(size)
pygame.display.set_caption("USER EVENT")
clock = pygame.time.Clock()
missing = True
done = True
pause = False
list1 = []
fontobj = pygame.font.Font("freesansbold.ttf", 15)
largeText = pygame.font.SysFont("comicsansms",115)

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
            random.randint(0, 700), random.randint(0, 250))
        )


    def update(self):
        self.rect.move_ip(0, 3)
        if self.rect.bottom > 500:
            missing = False
            list1.append(1)
            self.kill()
    def killenemy(self):
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
        self.rect.bottomleft = [0, 495]

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
player_list = pygame.sprite.Group()

#    enemy = Enemy(WHITE, 20, 15)

#    enemy.rect.x = random.randrange(screen_width)
#    enemy.rect.y = random.randrange(screen_height)

#    enemy_sprites_list.add(enemy)
#    all_sprites_list.add(enemy)


player = Player(WHITE, 35, 15)
player_list.add(player)
all_sprites_list.add(player)
score = 0

def text_objects(text, font):
    textSurface = font.render(text, True, GREEN)
    return textSurface, textSurface.get_rect()

def paused(stop):
    largeText = pygame.font.SysFont("comicsansms",115)
    #textP= font.render("PAUSE ", True, GREEN)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((screen_width/2),(screen_height/2))
    screen.blit(TextSurf, TextRect)

    while stop:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_p:
                    stop = False


        pygame.display.update()
        clock.tick(15)

while done:
    screen.fill(BLACK)

    enemy= Enemy(WHITE, 20, 15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = False
            elif event.key == K_p:
                pause = True
                paused(pause)
        elif event.type == ADDENEMY:
            enemy_sprites_list.add(enemy)
            all_sprites_list.add(enemy)
            #enemy.update()
    # Limit to 20 frames per second

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemy_sprites_list.update()

    x = sum(list1)


    clock.tick(10)
    #all_sprites_list.draw(screen)
    for entity in all_sprites_list:
        screen.blit(entity.image, entity.rect)

    hits = pygame.sprite.groupcollide(player_list, enemy_sprites_list, False, True)
    if hits:
        score +=1
    textM= fontobj.render("Missing: " + str(x), True, RED)
    screen.blit(textM, (500, 1))
    textS= fontobj.render("Score: " + str(score), True, GREEN)
    screen.blit(textS, (400, 1))
    pygame.display.flip()

    # Go ahead and update the screen with what we've drawn.
