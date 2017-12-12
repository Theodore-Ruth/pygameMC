#Code By: Theodore Ruth
#Imports for game code
import pygame, sys
import random
from pygame.locals import *

#Constants
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5
DIAMOND = 6

TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (143, 143, 143)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


#Resources for the avaible list to choose from
resources = [DIRT, GRASS, WATER, COAL, ROCK, LAVA, DIAMOND]

#Creates a tilemap with images from the textures dictionary
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range (MAPHEIGHT)]

#Textures dictionary for reference to the images used as textures
textures = {
		DIRT : pygame.image.load('images/minecraft_dirt.jpg'), 
		GRASS : pygame.image.load('images/minecraft_grass.png'), 
		WATER : pygame.image.load('images/minecraft_water.jpg'), 
		COAL : pygame.image.load('images/minecraft_coal 2.0.png'), 
		ROCK : pygame.image.load('images/minceraft_rock.png'), 
		LAVA : pygame.image.load('images/minecraft_lava.jpg'),
                DIAMOND : pygame.image.load('images/minecraft_diamond.jpg')
}

#Inventory Dictionary to show the inventory
inventory = {
	DIRT : 0,
	GRASS : 0,
	WATER : 0,
	COAL : 0,
	ROCK : 0,
	LAVA : 0,
	DIAMOND : 0
}
#Initiates the pygame code and the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 50))
pygame.display.set_caption('Adding an Inventory: Theodore Ruth')

#Adds the player to the screen
PLAYER = pygame.image.load('images/player.jpg').convert_alpha()
playerPos = [0, 0]

#Creates map where some resources are rarer than others
for rw in range(MAPHEIGHT):

	for cl in range(MAPWIDTH):
		randomNumber = random.randint(0, 140)
		if randomNumber == 0:
			tile = DIAMOND
		elif randomNumber >= 1 and randomNumber <= 10:
			tile = COAL
		elif randomNumber >= 11 and randomNumber <= 25:
			tile = WATER
		elif randomNumber >= 26 and randomNumber <= 46:
			tile = ROCK
		elif randomNumber >= 47 and randomNumber <= 80:
			tile = GRASS
		elif randomNumber >= 81 and randomNumber <= 83:
			tile = LAVA
		else:
			tile = DIRT
		tilemap[rw][cl] = tile

#For the inventory font
INVFONT = pygame.font.Font('freesansbold.ttf', 18)

#Game Loop
while True:

	#Checking to see if the player wants to QUIT
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit
			
		#Waiting for the user to hit a key and reacts accordingly
		elif event.type == KEYDOWN:
			#Moving events
			if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH - 1:
				playerPos[0] += 1
			if (event.key == K_LEFT) and playerPos[0] > 0:
				playerPos[0] -= 1
			if (event.key == K_UP) and playerPos[1] > 0:
				playerPos[1] -= 1
			if (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT - 1:
				playerPos[1] += 1
			
			#Getting and Item event
			if event.key == K_SPACE:
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				inventory[currentTile] += 1
				tilemap[playerPos[1]][playerPos[0]] = DIRT
				print(inventory)
				
			#Placing Events
			if (event.key == K_1):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[DIRT] > 0:
					inventory[DIRT] -= 1
					tilemap[playerPos[1]][playerPos[0]] = DIRT
					inventory[currentTile] += 1
			if (event.key == K_2):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[GRASS] > 0:
					inventory[GRASS] -= 1
					tilemap[playerPos[1]][playerPos[0]] = GRASS
					inventory[currentTile] += 1
			if (event.key == K_3):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[WATER] > 0:
					inventory[WATER] -= 1
					tilemap[playerPos[1]][playerPos[0]] = WATER
					inventory[currentTile] += 1
			if (event.key == K_4):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[COAL] > 0:
					inventory[COAL] -= 1
					tilemap[playerPos[1]][playerPos[0]] = COAL
					inventory[currentTile] += 1
			if (event.key == K_5):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[ROCK] > 0:
					inventory[ROCK] -= 1
					tilemap[playerPos[1]][playerPos[0]] = ROCK
					inventory[currentTile] += 1
			if (event.key == K_6):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[LAVA] > 0:
					inventory[LAVA] -= 1
					tilemap[playerPos[1]][playerPos[0]] = LAVA
					inventory[currentTile] += 1
			if (event.key == K_7):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[DIAMOND] > 0:
					inventory[DIAMOND] -= 1
					tilemap[playerPos[1]][playerPos[0]] = DIAMOND
					inventory[currentTile] += 1
			
	#Displays the Tilemap
	for row in range(MAPHEIGHT):
		for column in range (MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))
	
	#Updates player position
	DISPLAYSURF.blit(PLAYER, (playerPos[0] * TILESIZE, playerPos[1] * TILESIZE))
	
	#Updates the players inventory
	placePosition = 10
	for item in resources:
		DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT * TILESIZE + 20))
		placePosition += 30
		textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
		DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 20))
		placePosition += 50
	
	#Updates the display
	pygame.display.update()
