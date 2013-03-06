from pygame.locals import *
from time import sleep
import draw
import ships
import control
import pygame
import sys

owncolor = draw.OWNSHIPCOLOR
enemycolor = draw.ENEMYSHIPCOLOR

draw.showStartScreen()
draw.drawBoard()

ownship = ships.workShip()
enemyship = ships.workShip()

OwnListShip = ownship.createListShips()
EnemyListShip = enemyship.createListShips()

draw.drawAllShip(ownship)
control.jabber_send(ownship,enemyship)
#control.jabber_send(enemyship)
waitInput = True

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if (30 < mousey or mousey > 330) and (390 < mousex or mousex > 690):
                control.vistrel(ownship, enemyship, mousex, mousey)
                waitInput = False
        if not waitInput:
            control.compTurn(enemyship,ownship)
            waitInput = True
        pygame.display.update()
    sleep(0.05)


