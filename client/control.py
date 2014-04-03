import draw
import random
import pygame
from pygame.locals import *


def vistrel(ownship, ship, mx, my):
    y = (mx-390)/30
    x = my/30 - 1
    ship.delFromKorabli(x,y)
    bumbum(ship,x,y)
    draw.reDrawAll(ownship, ship, draw.DISPLAYSURF)


def compTurn(enemyship,ship):
    x = random.randint(0,9)
    y = random.randint(0,9)

    ship.delFromKorabli(x,y)
    bumbum(ship,x,y)
    draw.reDrawAll(ship,enemyship,draw.DISPLAYSURF)


def bumbum(ship,f,n):
    allshipspace = set([])
    for k in ship.korabli:
        for (i,j) in k.hitspace:
            allshipspace.add((i,j))
        for (i,j) in k.cells:
            allshipspace.add((i,j))
    if (f,n) not in allshipspace:
        ship.bumspace.add((f,n))


def checkForKeyPress():
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0: # or event.type == MOUSEBUTTONUP:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        pygame.quit()
    return keyUpEvents[0].key


import pickle
import xmpp

def jabber_send(myclient, ownship, enemyship, wait):
    remote_user = "bship1@default.rs"
    m = pickle.dumps([ownship,enemyship,wait])
    mymsg=xmpp.protocol.Message(remote_user, m)
    myclient.send(mymsg)

