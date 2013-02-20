from pygame.locals import *
import controller
import model
import pygame
import sys

controller.drawBoard()
controller.drawBoard(350)

ownship = model.workShip()
enemyship = model.workShip()

OwnListShip = ownship.createListShips()
EnemyListShip = enemyship.createListShips()

print OwnListShip

controller.drawAllShip(OwnListShip)
controller.drawAllShip(EnemyListShip)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
      #  if event.type == MOUSEBUTTONUP:
            #mousex, mousey = event.pos
            #print mousex, mousey
            #vistrel(mousex,mousey)
    pygame.display.update()


