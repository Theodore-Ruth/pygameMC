#Code By: Theodore Ruth
import pygame, sys
import random
from pygame.locals import *
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

resources = [DIRT, GRASS, WATER, COAL, ROCK, LAVA, DIAMOND]
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range (MAPHEIGHT)]
textures = {
		DIRT : pygame.image.load('images/minecraft_dirt.jpg'), 
		GRASS : pygame.image.load('images/minecraft_grass.png'), 
		WATER : pygame.image.load('images/minecraft_water.jpg'), 
		COAL : pygame.image.load('images/minecraft_coal 2.0.png'), 
		ROCK : pygame.image.load('images/minceraft_rock.png'), 
		LAVA : pygame.image.load('images/minecraft_lava.jpg'),
                DIAMOND : pygame.image.load('images/minecraft_diamond.jpg')}

pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
pygame.display.set_caption('Events: Theodore Ruth')

PLAYER = pygame.image.load('images/player.jpg').convert_alpha()
playerPos = [0, 0]

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
		
while True:
	for event in pygame.event.get():
		print(event)
		if event.type == QUIT:
			pygame.quit()
			sys.exit
		elif event.type == KEYDOWN:
			if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH - 1:
				playerPos[0] += 1
			if (event.key == K_LEFT) and playerPos[0] > 0:
				playerPos[0] -= 1
			if (event.key == K_UP) and playerPos[1] > 0:
				playerPos[1] -= 1
			if (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT - 1:
				playerPos[1] += 1
			
	for row in range(MAPHEIGHT):
		for column in range (MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))
	DISPLAYSURF.blit(PLAYER, (playerPos[0] * TILESIZE, playerPos[1] * TILESIZE))
	pygame.display.update()
