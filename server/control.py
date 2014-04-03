import draw
import random
import pygame
from pygame.locals import *


def vistrel(ownship, enemyship, mx, my):
    y = (mx-390)/30
    x = my/30 - 1
    enemyship.delFromKorabli(x,y)
    bumbum(enemyship,x,y)
    #bumbum(ownship, x, y)
    #print (enemyship.bumspace)
    draw.reDrawAll(ownship, enemyship, draw.DISPLAYSURF)


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

def jabber_send(cclient, ownship,enemyship,wait):
    remote_user = "bship2@default.rs"
    m = pickle.dumps([ownship,enemyship,wait])
    mymsg=xmpp.protocol.Message(remote_user, m)
    cclient.send(mymsg)

