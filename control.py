import draw
import random
import pygame
from pygame.locals import *

def vistrel(ownship, ship, mx, my):
    y = (mx-390)/30
    x = my/30 - 1
    ship.delFromKorabli(x,y)
    for i in ship.korabli:
        if (x,y) not in i.hitspace:
            ship.bumspace.add((x,y))
    draw.reDrawAll(ownship, ship, draw.DISPLAYSURF)


def compTurn(enemyship,ship):
    x = random.randint(0,9)
    y = random.randint(0,9)

    ship.delFromKorabli(x,y)
    for i in ship.korabli:
        if (x,y) not in i.hitspace:
            ship.bumSpace(x,y)
    draw.reDrawAll(ship,enemyship,draw.DISPLAYSURF)


def checkForKeyPress():
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0: # or event.type == MOUSEBUTTONUP:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        pygame.quit()
    return keyUpEvents[0].key
