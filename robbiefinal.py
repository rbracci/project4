from pygame import *
from pygame.sprite import *
import pygame
import random, time
import os, sys
from pygame.locals import *

Width = 800
Height = 600


DELAY = 1000;
#creating initial colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (255, 153, 204)

tokenspeed = 10
pacmanspeed = 5

height_of_screen = 800
x_position = 400
y_position = 500

clock = pygame.time.Clock()


class Token(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("token.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False

	def back_to_top(self):
		self.rect.y = random.randrange(-300,-20)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 10
		if self.rect.y > 610:
			self.back_to_top()
		self.colliderect = False

class Bomb(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("bomb.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False
		self.rect.x = 0
		self.rect.y = 0

	def back_to_top(self):
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(0, Height)

	def fall_collide_with(self, pacman):
		if self.rect.colliderect(pacman.rect) == True:
			game_over = True

	def update(self):
		self.rect.y += 10
		if self.rect.y > 610:
			self.back_to_top()
		self.colliderect = False

class Ghost1(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("ghost1.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False

	def back_to_top(self):
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 6
		if self.rect.y > 610:
			self.back_to_top()
		self.colliderect = False

class Ghost2(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("ghost2.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False

	def back_to_top(self):
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 5
		if self.rect.y > 610:
			self.back_to_top()
		self.colliderect = False

class Ghost3(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("ghost3.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False

	def back_to_top(self):
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 7
		if self.rect.y > 610:
			self.back_to_top()
		self.colliderect = False


class Ghost4(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("ghost4.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False

	def back_to_top(self):
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 6
		if self.rect.y > 610:
			self.back_to_top()
		self.colliderect = False



class Pacman(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("pacman.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = 700
		self.rect.y = 300


	def update(self):
		self.rect.x = x_position
		self.rect.y = y_position

	def hit(self, target):
		return self.rect.colliderect(target)


class Bullet(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = pygame.Surface([4,10])
		self.image.fill(red)
		self.rect = self.image.get_rect()

		
	def update(self):
		self.rect.y -= 10


init()

gameDisplay = display.set_mode((Width, Height))
screen = gameDisplay
display.set_caption("Robbie Game")

f = font.Font(None, 25)
ghost1 = Ghost1()
ghost2 = Ghost2()
ghost3 = Ghost3()
ghost4 = Ghost4()
bomb=Bomb()
token = Token()
print("dd")
#score = Score()
print("ddddd")
pacman = Pacman()
bullet = Bullet()
sprites = RenderPlain(pacman, token,bomb,ghost1,ghost2,ghost3,ghost4,bullet)#addscore
bullet_list = RenderPlain(bullet)


hits = 0
lost_life = 1

pygame.mixer.music.load("violin.wav")
pygame.mixer.music.play(-1)


for pic in range(5):
	sprites.add(Ghost1())
	pygame.display.update()



gameExit = False
game_over =False
while not gameExit:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True


		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				new_bullet = Bullet()
				new_bullet.rect.x = pacman.rect.x 
				new_bullet.rect.y = pacman.rect.y
				sprites.add(new_bullet)
				bullet_list.add(new_bullet)
		if new_hit in Ghost1:
			if pacman.rect.colliderect(new_hit):
				print("hit")

		# if pacman.rect.colliderect(bomb):
		# 	print(pacman.rect.x, pacman.rect.y, bomb.rect.x, bomb.rect.y)
		# 	print("gameover")
		# 	game_over = True

		# if game_over == True:
		# 	print("Terminated")
		# 	score.gameover(screen)
		

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_position -= 10
		if event.key == pygame.K_RIGHT:
			x_position += 10

		if pacman.hit(token) and token.colliderect == False:
			hits += 2
			token.colliderect = True
		if pacman.hit(ghost1) and ghost1.colliderect ==False:
			hits += 1
			ghost1.colliderect = True
		if pacman.hit(ghost2) and ghost2.colliderect ==False:
			hits += 1
			ghost2.colliderect = True
		if pacman.hit(ghost3)and ghost3.colliderect ==False:
			hits += 1
			ghost3.colliderect = True
		if pacman.hit(ghost4) and ghost4.colliderect ==False:
			hits += 1
			ghost4.colliderect = True
		elif pacman.hit(bomb):
			lost_life -=1
			gameExit = True



	clock.tick(100)
	screen.fill(white)
	t = f.render("Score =" + str(hits), False, (0,0,0))
	r = f.render("Lives =" + str(lost_life), False,(0,0,0))
	screen.blit(t, (700, 0))
	screen.blit(r, (600,0))
	token.update()
	pacman.update()

	sprites.update()
	# score.draw(screen)
	sprites.draw(screen)

	display.update()
pygame.quit()
quit()





