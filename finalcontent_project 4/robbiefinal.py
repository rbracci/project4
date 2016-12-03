from pygame import *
from pygame.sprite import *
import pygame
import random, time
import os, sys
from pygame.locals import *

#Size of Screen we are creating
Width = 800
Height = 600

#creating initial colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
blue = (0, 0, 255)

#Other initial values
tokenspeed = 10
pacmanspeed = 5
height_of_screen = 800
x_position = 400
y_position = 500
hits = 0
lost_life = 1
clock = pygame.time.Clock()
DELAY = 1000

#this object falls from the screen and is harder to get making it worth more points
class Token(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("token.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False

	def regenerate_top(self):
		self.rect.y = random.randrange(-400,-20)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 20
		if self.rect.y > 610:
			self.regenerate_top()
		self.colliderect = False

#One of three bombs that falls from the screen to create a game over
class Bomb(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("bomb.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False
		self.rect.x = 0
		self.rect.y = 0

	def regenerate_top(self):
		self.rect.y = random.randrange(-400, -20)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 10
		if self.rect.y > 610:
			self.regenerate_top()
		self.colliderect = False

#One of three bombs that falls from the screen to create a game over
class Bomb2(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("bomb.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False
		self.rect.x = 0
		self.rect.y = 0

	def regenerate_top(self):
		self.rect.y = random.randrange(-400, -20)
		self.rect.x = random.randrange(0, Height)


	def update(self):
		self.rect.y += 10
		if self.rect.y > 610:
			self.regenerate_top()
		self.colliderect = False

#One of three bombs that falls from the screen to create a game over
class Bomb3(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("bomb.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False
		self.rect.x = 0
		self.rect.y = 0

	def regenerate_top(self):
		self.rect.y = random.randrange(-400, -20)
		self.rect.x = random.randrange(0, Height)

	# def fall_collide_with(self, pacman):
	# 	if self.rect.colliderect(pacman.rect) == True:
	# 		game_over = True

	def update(self):
		self.rect.y += 10
		if self.rect.y > 610:
			self.regenerate_top()
		self.colliderect = False

#One of four ghosts that falls from the screen. If you hit the original ghosts they increase your score
#I generated ghosts below in a for loop that are decoys in attempt to try to get the player to die more easily
class Ghost1(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("ghost1.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False

	def regenerate_top(self):
		self.rect.y = random.randrange(-400, -20)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 6
		if self.rect.y > 610:
			self.regenerate_top()
		self.colliderect = False

#One of four ghosts that falls from the screen.
class Ghost2(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("ghost2.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False

	def regenerate_top(self):
		self.rect.y = random.randrange(-400, -20)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 5
		if self.rect.y > 610:
			self.regenerate_top()
		self.colliderect = False

#One of four ghosts that falls from the screen.
class Ghost3(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("ghost3.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False

	def regenerate_top(self):
		self.rect.y = random.randrange(-400, -20)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 7
		if self.rect.y > 610:
			self.regenerate_top()
		self.colliderect = False

#One of four ghosts that falls from the screen.
class Ghost4(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("ghost4.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.colliderect = False

	def regenerate_top(self):
		self.rect.y = random.randrange(-400, -20)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 6
		if self.rect.y > 610:
			self.regenerate_top()
		self.colliderect = False


#Pacman moves right and left to collect the ghosts and tokens! If he hits the bombs the game is over
#I got pacman to shoot, but couldnt figure out how to destroy the bombs when pacman hit them
#I kept the shoot feature in to show additional work I did; I got some of it working but didn't have time to finish the rest of it
class Pacman(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("pacman.bmp").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = 700
		self.rect.y = 300


	def update(self):
		self.rect.x = x_position
		if self.rect.right>Width:
			self.rect.right = Width
		self.rect.y = y_position
		if self.rect.left <0:
			self.rect.left = 0



	def hit(self, target):
		return self.rect.colliderect(target)

#This bullet class comes out of pacman!
class Bullet(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = pygame.Surface([2,8])
		self.image.fill(blue)
		self.rect = self.image.get_rect()

		
	def update(self):
		self.rect.y -= 10

#initializing pygame and the screen display and the title of the game
init()
gameDisplay = display.set_mode((Width, Height))
screen = gameDisplay
display.set_caption("Robbie Pacman Game")
f = font.Font(None, 25)

#initializing all the classes and adding them to a sprites group
ghost1 = Ghost1()
ghost2 = Ghost2()
ghost3 = Ghost3()
ghost4 = Ghost4()
bombs = pygame.sprite.Group()
bomb1=Bomb()
token = Token()
bomb2 = Bomb2()
bomb3 = Bomb3()
pacman = Pacman()
bullet = Bullet()
sprites = RenderPlain(pacman, token,bomb1,ghost1,ghost2,ghost3,ghost4,bullet, bomb2, bomb3)#addscore
bullet_list = RenderPlain(bullet)



#sound that plays in the background of my game
pygame.mixer.music.load("violin.wav")
pygame.mixer.music.play(-1)
gun = pygame.mixer.Sound("gun.wav")

#create decoy ghosts that do not actually make the score go up
for ghost in range(1):
	sprites.add(Ghost1())
	pygame.display.update()

for ghost in range(1):
	sprites.add(Ghost2())
	pygame.display.update()

for ghost in range(1):
	sprites.add(Ghost3())
	pygame.display.update()

for ghost in range(1):
	sprites.add(Ghost4())
	pygame.display.update()

end_it = False
while (end_it==False):
	screen.fill(blue)
	font=pygame.font.SysFont(None, 22)
	hello=font.render("Please Click the Screen to Start!", 1, (100,200, 120))
	howto = font.render("How to play: Dodge the bombs and eat the ghosts! Some ghosts are fake and don't increase your score", 1, (100,200, 120))
	rules = font.render("Controls: left_key:move left, right_key:move right, up_key:shoots", 1 , (100,200, 120))
	for event in pygame.event.get():
		if event.type==MOUSEBUTTONDOWN:
			end_it=True
	screen.blit(hello,(250,250))
	screen.blit(rules, (20, 300))
	screen.blit(howto, (20, 330))
	pygame.display.flip()

gameExit = False
game_over =False
while not gameExit:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True


			#shoots the bullet from the pacman image
			#unfortunately I couldnt get the bullet to destroy the image I wanted
			#The code I tried to use to eliminate the image is below!
			#Additionally I added sound to go with the bullet when it shoots!
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				gun.play()
				new_bullet = Bullet()
				new_bullet.rect.x = pacman.rect.x 
				new_bullet.rect.y = pacman.rect.y
				sprites.add(new_bullet)
				bullet_list.add(new_bullet)

	# for new_bullet in bullet_list:
	# 	hitting_bomb = bullter_list.rect.colliderect(bomb1)
	# 	if new_bullet.colliderect(bomb1):
	# 		hitting_bomb.kill()
	# 		#new_bullet.remove(bullet)
	# 		#sprites.remove(bullet)

	# 	if bullet.rect.y < -10:
	# 		bullet_list.remove(bullet)
	# 		sprites.remove(bullet)

	#moves pacman left and right
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_position -= 11
		if event.key == pygame.K_RIGHT:
			x_position += 11
		
			#How the scoring works for when pacman hits one of the objects
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
		elif pacman.hit(bomb1):
			lost_life -=1
			gameExit = True

		# if new_hit in Ghost1:
		# 	if pacman.rect.colliderect(new_hit):
		# 		print("hit")


		#terminates the program if pacman hits one of these three bombs and tells us gameover and the score
	if pacman.rect.colliderect(bomb1):
		game_over = True
		screen.fill(black)
		onscreen = f.render('Gameover...Better Luck Next Time. You had a total score of' + str(hits)+ ' points!', True , white)
		screen.blit(onscreen, (85 , 300)) 
		pygame.display.update()
		print('bye') 
		pygame.time.delay(1000)


	if pacman.rect.colliderect(bomb2):
		game_over = True
		screen.fill(black)
		onscreen = f.render('Gameover...Better Luck Next Time. You had a total score of' + str(hits)+ ' points!', True , white)
		screen.blit(onscreen, (85 , 300)) 
		pygame.display.update()
		print('bye') 
		pygame.time.delay(1000)


	if pacman.rect.colliderect(bomb3):
		game_over = True
		screen.fill(black)
		onscreen = f.render('Gameover...Better Luck Next Time. You had a total score of' + str(hits)+ ' points!', True , white)
		screen.blit(onscreen, (85 , 300)) 
		pygame.display.update()
		print('bye') 
		pygame.time.delay(1000)

#updates the screen, score, sprites, and everything else being called above
	clock.tick(100)
	screen.fill(white)
	t = f.render("Score =" + str(hits), False, (0,0,0))
	r = f.render("Lives =" + str(lost_life), False,(0,0,0))
	screen.blit(t, (700, 0))
	screen.blit(r, (600,0))
	token.update()
	pacman.update()
	sprites.update()
	sprites.draw(screen)
	display.update()
pygame.quit()
quit()





