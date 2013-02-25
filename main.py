from pygame.locals import *
from time import sleep
import view
import model
import pygame
import sys

owncolor = view.OWNSHIPCOLOR
enemycolor = view.ENEMYSHIPCOLOR

view.drawBoard()
view.drawBoard(360)

ownship = model.workShip()
enemyship = model.workShip()

OwnListShip = ownship.createListShips()
EnemyListShip = enemyship.createListShips()

view.drawAllShip(OwnListShip, owncolor, 'own')
view.drawAllShip(EnemyListShip, enemycolor, 'enemy')

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
        pygame.display.update()
    sleep(0.05)


