from pygame import *
from pygame.sprite import *
import pygame
import math 
import time 
import random 
import os, sys
from pygame.locals import *
 
# Define some colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
 
# Size of break-out blocks

snake_width = 20
snake_height = 20
x_pos = 0
y_pos = 0
x_delta = 0
y_delta = 0
clock = pygame.time.Clock()
exit_program = False

init()
mixer.music.load ("violin.wav")
mixer.music.play(-1)

class Paddle (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([snake_width,snake_height])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 710
    def update (self):
        self.rect.x = x_pos
        self.rect.y = y_pos
        screen.fill(black)

    def within_right_bound (self):
        return self.x <= 1000
    def within_left_bound(self):
        self.x >= 0





pygame.init()
screen = pygame.display.set_mode([1000, 750])
pygame.display.set_caption('Pygame Breakout Robert Bracci')
font = pygame.font.Font(None, 60)
background = pygame.Surface(screen.get_size())
pygame.display.update()

allsprites = pygame.sprite.Group()
paddle = Paddle()
allsprites.add(paddle)



while not exit_program:
    clock.tick(30)
   
    Paddle()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True

    if event.type == pygame.KEYDOWN:
        x_pos_=0;
        y_pos=0;
        if event.key == pygame.K_LEFT:
            x_pos -= 10
        if event.key == pygame.K_RIGHT:
            x_pos += 10
        if event.key == pygame.K_UP:
            y_pos -= 10
        if event.key == pygame.K_DOWN:
            y_pos += 10

    # x_pos +=x_delta
    # y_pos +=y_delta
  
    allsprites.update()
    allsprites.draw(screen)
    pygame.display.flip()
pygame.quit()




