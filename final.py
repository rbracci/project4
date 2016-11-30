import pygame

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
block_width = 150
block_height = 30
x = 425
y = 710
width=20
diameter=20
aa= 500
b= 690
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((1000,750)) #initialize with a tuple
screen = gameDisplay
screen.fill(white)
#lets add a title, aka "caption"
pygame.display.set_caption("Breakout Game by Robert Bracci")

#pygame.display.flip() 		#similar to a flip book, updates entire surface



class Paddle(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([block_width,block_height])
		self.image.fill(red)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
# brick_width=100
# brick_height=20
# class BRICKS (pygame.sprite.Sprite):
# 	def __init__(self):
# 		super().__init__()	
# 		y_ofs = 35
# 		self.bricks = []
# 		for i in range(7):
# 			x_ofs = 35
# 			for j in range(8):
# 				self.bricks.append(pygame.Rect(x_ofs,y_ofs,brick_width,brick_height))
# 				x_ofs += brick_width + 10
# 				y_ofs += brick_height + 5
# 	def draw_bricks(self):
# 		for brick in self.bricks:
# 			self.image=pygame.Surface(brick)
# 			self.image.fill(green)
# 			self.rect = self.image.get_rect()
# 			self.rect.x = brick

			
        


	
class Ball (pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([width,diameter])
		self.image.fill(blue)
		self.rect =self.image.get_rect()
		self.rect.x = aa #WHY is it self.x and not self.
		self.rect.y = b





# Clock to limit speed
clock = pygame.time.Clock()
		
allsprites = pygame.sprite.Group()
paddle = Paddle()
allsprites.add(paddle)
ball = Ball()
allsprites.add(ball)
# Bricks= BRICKS()
# allsprites.add(Bricks)



gameExit = False
while not gameExit:
	Block()
	Ball()
	# BRICKS()
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True


	allsprites.update()
	allsprites.draw(screen)
	pygame.display.update()

