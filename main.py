from pygame.locals import *
from time import sleep
import draw
import ships
import control
import pygame
import sys

owncolor = draw.OWNSHIPCOLOR
enemycolor = draw.ENEMYSHIPCOLOR

draw.drawBoard()
draw.drawBoard(360)

ownship = ships.workShip()
enemyship = ships.workShip()

OwnListShip = ownship.createListShips()
EnemyListShip = enemyship.createListShips()

draw.drawAllShip(ownship.korabli, owncolor, 'own')
#draw.drawAllShip(enemyship.korabli, enemycolor, 'enemy')

#for i in enemyship.korabli:
#    print i.cells

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            control.vistrel(ownship.korabli, enemyship, mousex, mousey)
        pygame.display.update()
    sleep(0.05)


