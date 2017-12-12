#Code By: Theodore Ruth
import pygame, sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((300,300))

pygame.display.set_caption('Introduction to Pygame: Theodore Ruth')

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (0, 0, 70, 20))
	pygame.draw.circle(DISPLAYSURF, (255, 0, 0), (200, 200), 50, 0)
	pygame.draw.ellipse(DISPLAYSURF, (0, 0, 255), (10, 50, 20, 70), 0)
	pygame.draw.arc(DISPLAYSURF, (0, 255, 0), (100, 50, 20, 20), 45, 50, 1)
	pygame.display.update()
