#Code By: Theodore Ruth
import pygame, sys
from pygame.locals import *
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5

TILESIZE = 20
MAPWIDTH = 5
MAPHEIGHT =5
tilemap = [[GRASS, COAL, DIRT, DIRT, ROCK], [WATER, WATER, GRASS, LAVA, LAVA], [COAL, LAVA, ROCK, GRASS, WATER], [DIRT, GRASS, ROCK, COAL, COAL], [GRASS, WATER, LAVA, LAVA, DIRT]]
textures = {
        DIRT : pygame.image.load('images/minecraft_dirt.jpg'),
        GRASS : pygame.image.load('images/minecraft_grass.png'),
        WATER : pygame.image.load('images/minecraft_water.jpg'),
        COAL : pygame.image.load('images/minecraft_coal 2.0.png'),
        ROCK : pygame.image.load('images/minceraft_rock.png'),
        LAVA : pygame.image.load('images/minecraft_lava.jpg')}
pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
pygame.display.set_caption('Adding Images: Theodore Ruth')
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	for row in range(MAPHEIGHT):
		for column in range (MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))
	pygame.display.update()


