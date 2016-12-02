import pygame
pygame.init();
#alsdfj
class Block(pygame.sprite.Sprite):
    ##

class Ball(pygame.sprite.Sprite):
##
def main():
    ball_img = pyglet.resource.image('ball.png')
    paddle_imgs = [pyglet.resource.image('paddle1.png'),
                   pyglet.resource.image('paddle2.png')]
    wall_imgs = [pyglet.resource.image('vertical_wall.png'),
                 pyglet.resource.image('horizontal_wall.png'),
                 pyglet.resource.image('brick.png')]
    window = GameWindow(ball_img,paddle_imgs, wall_imgs)
    pyglet.app.run()
main()

# Size of break-out blocks
block_width = 22
block_height =13

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Events")

#pygame.display.flip() 		#similar to a flip book, updates entire surface
pygame.display.update()		#only updates portion specified

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

gameDisplay.fill(white)
	#look up draw.rect()
pygame.draw.rect(gameDisplay, black, [400,300, 10, 100])
pygame.draw.rect(gameDisplay, red, [100,100, 50, 50])

gameDisplay.fill(blue, rect=[200,200, 20,20])


gameDisplay.fill(blue, rect=[50,50, 20,20])
pygame.draw.circle(gameDisplay, red, (50,100), 20, 0)
pygame.draw.lines(gameDisplay, red, False, [(100,100), (150,200), (200,100)], 1)

pygame.display.update()		
#required
pygame.quit()
quit()	