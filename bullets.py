import pygame
import random
from pygame.locals import*
import sys
import time
# --- Global constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ADDENEMY = pygame.USEREVENT + 3
pygame.time.set_timer(ADDENEMY, 4000) #secondi
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
score = 0

class Stars(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super(Stars, self).__init__()

        self.image = pygame.Surface([3, 3])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect(center=(
                random.randint(0, 700), random.randint(0, 500))
            )



    def update(self):
        """ Move the bullet. """
        self.rect.y += 3


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super(Bullet, self).__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()


    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super(Block, self).__init__()
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
            self.kill()
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super(Player, self).__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Set the player x position to the mouse x position
        self.rect.x = pos[0]

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("BULLTES")
font = pygame.font.SysFont("serif", 15)
clock = pygame.time.Clock()
done = True

all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
star_list = pygame.sprite.Group()
block = Block(WHITE, 20, 15)

def Generate():

    numb = random.randint(0, 10)
    return numb
    # This represents a block


    # Add the block to the list of objects


block_list.add(block)
all_sprites_list.add(block)
player = Player()
all_sprites_list.add(player)
player.rect.y = 450


def game_over():
    screen.fill(WHITE)


    text = font.render("Game Over, click to restart", True, BLACK)
    center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
    center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
    screen.blit(text, [center_x, center_y])

    pygame.display.flip()
    pygame.time.delay(1000)



while done:




    star = Stars()
    star.rect.x = random.randrange(SCREEN_WIDTH)
    star.rect.y = random.randrange(-300, SCREEN_HEIGHT)
    star_list.add(star)
    all_sprites_list.add(star)

    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = False
            elif event.key == pygame.K_SPACE:
                bullet1 = Bullet()
                bullet2 = Bullet()
            # Set the bullet so it is where the player is
                bullet1.rect.x = player.rect.x + 5
                bullet1.rect.y = player.rect.y
            # Add the bullet to the lists
                bullet2 = Bullet()
            # Set the bullet so it is where the player is
                bullet2.rect.x = player.rect.x + 15
                bullet2.rect.y = player.rect.y

                all_sprites_list.add(bullet1)
                bullet_list.add(bullet1)
                all_sprites_list.add(bullet2)
                bullet_list.add(bullet2)
        elif event.type == ADDENEMY:
              x = Generate()
              for i in range(x):
                  block = Block(RED, 20, 15)
                  block_list.add(block)
                  all_sprites_list.add(block)


    all_sprites_list.update()
    for bullet in bullet_list:

        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            

        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
    player_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    if player_hit_list:
        done = False
        all_sprites_list.remove(player)
        game_over()

    all_sprites_list.draw(screen)
    clock.tick(20)
    textS= font.render("Score: " + str(score), True, GREEN)
    screen.blit(textS, (400, 1))
    pygame.display.flip()
