from pygame.locals import *
from time import sleep
import draw
import ships
import control
import pygame
import sys

from jabber import jinstance

owncolor = draw.OWNSHIPCOLOR
enemycolor = draw.ENEMYSHIPCOLOR

draw.showStartScreen()
draw.drawBoard()

ownship = ships.workShip()
enemyship = ships.workShip()

OwnListShip = ownship.createListShips()
EnemyListShip = enemyship.createListShips()

draw.drawAllShip(ownship)
c = jinstance()
control.jabber_send(c, ownship, enemyship, wait=False)
#control.jabber_send(ownship,enemyship,wait=False)
#control.jabber_send(enemyship)
waitInput = True

while True:
    c.Process(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if (30<mousey<330) and (390<mousex<690):
                control.vistrel(ownship, enemyship, mousex, mousey)
                control.jabber_send(c, ownship, enemyship, wait=True)
                waitInput = False
        if not waitInput:
            #control.compTurn(enemyship,ownship)
            waitInput = True
        pygame.display.update()
    sleep(0.05)


