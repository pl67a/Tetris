import sys
import random
import pygame
from pygame.locals import *
from const import *
from block import *


pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
DISPLAYSURF.fill((255, 255, 255))

P = Block(BlockType.RED, (400, 200))
Q = Block(BlockType.BLUE, (400, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill((255, 255, 255))
    P.update()
    Q.update()
    P.draw(DISPLAYSURF)
    Q.draw(DISPLAYSURF)
    pygame.display.update()
