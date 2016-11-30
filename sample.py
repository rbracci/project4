import math
import pygame
 
# Define some colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
 
# Size of break-out blocks
block_width = 74
block_height = 20
paddle_width = 200
paddle_height = 30
x = 400
y = 710
width=20
diameter=20
aa= 500
b= 690

class Paddle:
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([paddle_width,paddle_height])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 710
    def update (self):
        if self.moving_right and self.within_right_bound():
            self.x +=10
        elif self.moving_left and self.within_left_bound():
            self.x -=10

    def within_right_bound (self):
        return self.x <= 1000
    def within_left_bound(self):
        self.x >= 0


class Ball (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([width,diameter])
        self.image.fill(blue)
        self.rect =self.image.get_rect()
        self.rect.x = aa #WHY is it self.x and not self.
        self.rect.y = b
 
class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


pygame.init()
screen = pygame.display.set_mode([1000, 750])
pygame.display.set_caption('Pygame Breakout Robert Bracci')
font = pygame.font.Font(None, 60)
background = pygame.Surface(screen.get_size())

blocks = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
paddle = Paddle()
allsprites.add(paddle)
ball = Ball()
allsprites.add(ball)

top = 20
blockcount = 13
for row in range(6):
    for column in range(0, blockcount):
        block = Block(white, column * (block_width +3), top)
        blocks.add(block)
        allsprites.add(block)
    top += block_height +3
clock = pygame.time.Clock()
game_over = False
exit_program = False

while not exit_program:
    clock.tick(30)
    screen.fill(black)
    Paddle()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.moving_left =True
            elif event.key == pygame.K_RIGHT:
                paddle.moving_right = True
            elif event.type == pygame.K_UP:
                if event.key == pygame.K_LEFT:
                    paddle.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    paddle.moving_right=False



  

    allsprites.draw(screen)
    pygame.display.flip()
pygame.quit()




