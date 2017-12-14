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
WOOD = 4
FIRE = 5
SAND = 6
GLASS = 7
ROCK = 8
STONE = 9
BRICK = 10
LAVA = 11
DIAMOND = 12
CLOUD = 13
BIRD = 14


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

#Cloud and bird Constants
cloudx = random.randint(-300, 0)
cloudy = random.randint(0, MAPHEIGHT * TILESIZE)
cloud2x = random.randint(601, 901)
cloud2y = random.randint(0, MAPHEIGHT * TILESIZE)
cloud3x = random.randint(-300, 0)
cloud3y = random.randint(0, MAPHEIGHT * TILESIZE)

bird1x = random.randint(601, 901)
bird1y = random.randint(0, MAPHEIGHT * TILESIZE)
bird2x = random.randint(-300, 0)
bird2y = random.randint(0, MAPHEIGHT * TILESIZE)

fpsClock = pygame.time.Clock()


#Resources for the avaible list to choose from
resources = [DIRT, GRASS, WATER, COAL, WOOD, FIRE, SAND, GLASS, ROCK, STONE, BRICK, LAVA, DIAMOND]

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
		DIAMOND : pygame.image.load('images/minecraft_diamond.jpg'),
		GLASS : pygame.image.load('images/minecraft_glass.png'),
		BRICK : pygame.image.load('images/minecraft_brick.png'),
		WOOD : pygame.image.load('images/minecraft_wood.jpg'),
		FIRE : pygame.image.load('images/minecraft_fire.jpg'),
		SAND : pygame.image.load('images/minecraft_sand.jpg'),
		STONE : pygame.image.load('images/minecraft_stone.jpg'),
		CLOUD : pygame.image.load('images/cloud.png'),
		BIRD : pygame.image.load('images/bird.png')
}

#Inventory Dictionary to show the inventory
inventory = {
	DIRT : 0,
	GRASS : 0,
	WATER : 0,
	COAL : 0,
	WOOD : 0,
	FIRE : 0,
	SAND : 0,
	GLASS : 0,
	ROCK : 0,
	STONE: 0,
	BRICK: 0,
	LAVA : 0,
	DIAMOND : 0,
	
}

#Dictionary for the controls
controls = {
			DIRT : 96,
			GRASS : 49,
			WATER : 50,
			COAL : 51,
			WOOD : 52,
			FIRE : 53,
			SAND : 54,
			GLASS : 55,
			ROCK : 56,
			STONE : 57,
			BRICK : 48,
			LAVA: 45,
			DIAMOND : 61
}

#Crafting recipes
craft = {
			FIRE : {WOOD : 2, ROCK : 2},
			STONE : {ROCK : 2},
			GLASS : {FIRE : 1, SAND : 2},
			DIAMOND : {WOOD : 2, COAL : 3},
			BRICK : {ROCK : 2, FIRE : 1},
			SAND : {ROCK : 2},
			ROCK : {LAVA : 1, WATER : 1},
			LAVA : {STONE : 1, FIRE : 3},
			COAL : {WOOD : 1, FIRE : 1}
}

#Initiates the pygame code and the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 50))
pygame.display.set_caption('Crafting New Items: Theodore Ruth')
pygame.display.set_icon(pygame.image.load('images/player.jpg'))

#Adds the player to the screen
PLAYER = pygame.image.load('images/player.jpg').convert_alpha()
playerPos = [0, 0]

#Creates map where some resources are rarer than others
for rw in range(MAPHEIGHT):

	for cl in range(MAPWIDTH):
		randomNumber = random.randint(0, 100)
		if randomNumber == 0:
			tile = DIAMOND
		elif randomNumber >= 1 and randomNumber <= 5:
			tile = COAL
		elif randomNumber >= 6  and randomNumber <= 16 :
			tile = WATER
		elif randomNumber >= 17  and randomNumber <= 27 :
			tile = ROCK
		elif randomNumber >= 28 and randomNumber <= 50 :
			tile = GRASS
		elif randomNumber >= 51  and randomNumber <= 55 :
			tile = LAVA
		elif randomNumber >= 56 and randomNumber <= 60 :
			tile = WOOD
		elif randomNumber >= 61  and randomNumber <= 71:
			tile = SAND
		else:
			tile = DIRT
		tilemap[rw][cl] = tile

#For the inventory font
INVFONT = pygame.font.Font('freesansbold.ttf', 12)

#Game Loop
while True:
	DISPLAYSURF.fill(BLACK)
	#Checking to see if the player wants to QUIT
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
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
				
			#Key Events
			for key in controls:
				if (event.key == controls[key]):
				
					#Crafting event
					if pygame.mouse.get_pressed()[0]:
						if key in craft:
							canBeMade = True
							for i in craft[key]:
								if craft[key][i] > inventory[i]:
									canBeMade = False
									break
					
							if canBeMade == True:
								for i in craft[key]:
									inventory[i] -= craft[key][i]
									inventory[key] += 1
					
					#Placing event
					else:
						currentTile = tilemap[playerPos[1]][playerPos[0]]
						if inventory[key] > 0:
							inventory[key] -= 1
							inventory[currentTile] += 1
							tilemap[playerPos[1]][playerPos[0]] = key
			
			
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
		placePosition += 10
		textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
		DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 20))
		placePosition += 35
	
	#Updates the clouds and birds and moves them across the screen.
	DISPLAYSURF.blit(textures[CLOUD].convert_alpha(), (cloudx, cloudy))
	cloudx += 1.7
	if cloudx > MAPWIDTH * TILESIZE:
		cloudy = random.randint(0, MAPHEIGHT * TILESIZE)
		cloudx = -200
	
	DISPLAYSURF.blit(textures[CLOUD].convert_alpha(), (cloud2x, cloud2y))
	cloud2x -= 1.5
	if cloud2x < -1:
		cloud2y = random.randint(0, MAPHEIGHT * TILESIZE)
		cloud2x = 800
	
	DISPLAYSURF.blit(textures[CLOUD].convert_alpha(), (cloud3x, cloud3y))
	cloud3x += 1.25
	if cloud3x > MAPWIDTH * TILESIZE:
		cloud3y = random.randint(0, MAPHEIGHT * TILESIZE)
		cloud3x = -200
	
	DISPLAYSURF.blit(textures[BIRD].convert_alpha(), (bird1x, bird1y))
		
	bird1x -= 1.1
	if bird1x < -1:
		bird1y = random.randint(0, MAPHEIGHT * TILESIZE)
		bird1x = 800
	
	DISPLAYSURF.blit(textures[BIRD].convert_alpha(), (bird2x, bird2y))
	bird2x += 1.5
	if bird2x > MAPWIDTH * TILESIZE:
		bird2y = random.randint(0, MAPHEIGHT * TILESIZE)
		bird2x = -200
	
	#Updates the display
	pygame.display.update()
	fpsClock.tick(300)
	
