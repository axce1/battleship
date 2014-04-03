from pygame.locals import *
from time import sleep
import draw
import ships
import control
import pygame
import sys

import pickle
from jabber import jinstance

owncolor = draw.OWNSHIPCOLOR
enemycolor = draw.ENEMYSHIPCOLOR

draw.showStartScreen()
draw.drawBoard()

ownship = ships.workShip()
enemyship = ships.workShip()

OwnListShip = ownship.createListShips()
EnemyListShip = enemyship.createListShips()

def msgparser(connect_object, message):
    global ownship, enemyship, waitInput
    mess = pickle.loads(message.getBody())
    ownship =  mess[1]
    draw.drawAllShip(ownship)
    enemyship = mess[0]
    waitInput = mess[2]
    draw.reDrawAll(ownship, enemyship, draw.DISPLAYSURF)
    pygame.display.update()


draw.drawAllShip(ownship)
c = jinstance()
c.RegisterHandler('message', msgparser)
control.jabber_send(c, ownship, enemyship, wait=False)
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


