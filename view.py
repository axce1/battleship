from pygame.locals import *
from time import sleep
import controller
import model
import pygame
import sys

owncolor = controller.OWNSHIPCOLOR
enemycolor = controller.ENEMYSHIPCOLOR

controller.drawBoard()
controller.drawBoard(360)

ownship = model.workShip()
enemyship = model.workShip()

OwnListShip = ownship.createListShips('own')
EnemyListShip = enemyship.createListShips('enemy')

controller.drawAllShip(OwnListShip, owncolor)
controller.drawAllShip(EnemyListShip, enemycolor)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
        pygame.display.update()
    sleep(0.05)


