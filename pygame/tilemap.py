#Code By: Theodore Ruth
import pygame, sys
from pygame.locals import *
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5

BROWN = (153, 76, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (142, 142, 142)

TILESIZE = 50
MAPWIDTH = 5
MAPHEIGHT =5
tilemap = [[GRASS, COAL, DIRT, DIRT, ROCK], [WATER, WATER, GRASS, LAVA, LAVA], [COAL, LAVA, ROCK, GRASS, WATER], [DIRT, GRASS, ROCK, COAL, COAL], [GRASS, WATER, LAVA, LAVA, DIRT]]
colors = {
DIRT : BROWN,
GRASS : GREEN, 
WATER : BLUE, 
COAL : BLACK, 
ROCK : GREY, 
LAVA : RED}
pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
pygame.display.set_caption('Creating a Tilemap: Theodore Ruth')
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	for row in range(MAPHEIGHT):
		for column in range (MAPWIDTH):
			pygame.draw.rect (DISPLAYSURF, colors[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

	pygame.display.update()
