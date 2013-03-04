import draw
import random
import pygame
from pygame.locals import *

def vistrel(ownship, ship, mx, my):
    y = (mx-390)/30
    x = my/30 - 1
    ship.delFromKorabli(x,y)
    ship.bumSpace(x,y)
    draw.reDrawAll(ownship, ship, draw.DISPLAYSURF, x, y)


def compTurn(enemyship,ship):
    x = random.randint(0,9)
    y = random.randint(0,9)

    if ship.delFromKorabli(x,y)== 'tada':
        print '1'
    else:
        ship.bumSpace(x,y)
    draw.reDrawAll(ship,enemyship,draw.DISPLAYSURF,x,y)


def checkForKeyPress():
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0: # or event.type == MOUSEBUTTONUP:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        pygame.quit()
    return keyUpEvents[0].key
