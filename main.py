import pygame
import pygame.constants
import sys
from pygame.locals import *

#set game clock
clock = pygame.time.Clock()

#initialize the game
pygame.init()

WINDOW_SIZE = (840,400)
CAMERA_SIZE = (WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2)

#create display
screen = pygame.display.set_mode(WINDOW_SIZE)

#scale the game
display = pygame.Surface(CAMERA_SIZE)

#set the player sprite
playerSprite = pygame.image.load("res/ScooterTheJumpingDude.png")

#dirt tile
dirtSprite = pygame.image.load("res/StoneAndDirt.png")

#grass tile
dirtGrassSprite = pygame.image.load('res/StoneDirtAndGrass.png')

#gameMap[y][x]

gameMap = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]



#movement variables
movingRight = False
movingLeft = False
playerSpeed = 5
playerVertMomentum = 0

#intital player location
player_location = [50,50]

#player collision
playerRect = pygame.Rect(player_location[0],player_location[1],playerSprite.get_width(),playerSprite.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)

# region Game Loop----------------------------------------------
while True:
	#clear the previous frame with another color
	display.fill((146,132,23))
	
	
	#Render the player
	display.blit(playerSprite,player_location)
	
	
	# region Player Movement, collison, and rendering --------------
 
	
	playerVertMomentum += 0.2 #gravity
	player_location[1] += playerVertMomentum
	
	#set collision player collision box location
	playerRect.x = player_location[0]
	playerRect.y = player_location[1]
	
	
	
	# region Input
	#move the player left and right
	if movingRight:
		player_location[0] += playerSpeed
	if movingLeft:
		player_location[0] -= playerSpeed

	#check for input
	for event in pygame.event.get():
		#if player closes the game end the game
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		#input check if pressed down
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				movingRight = True
			if event.key == K_LEFT:
				movingLeft = True
		#input check if key up
		if event.type == KEYUP:
			if event.key == K_RIGHT:
				movingRight = False
			if event.key == K_LEFT:
				movingLeft = False
	#endregion
	# endregion --------------
	
	surf = pygame.transform.scale(display, WINDOW_SIZE)
	screen.blit(surf, (0,0))
 
 
	pygame.display.update() #update the display
	clock.tick(60) #keep 60 fps
# endregion Game Loop --------------------------

