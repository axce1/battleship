import draw
import random

def vistrel(ownship, ship, mx, my):
    y = (mx-390)/30
    x = my/30 - 1
   # print x, y
    if ship.delFromKorabli(x,y) == 'tada':
        print 'tada'
       # draw.drawEnemyShip(draw.DISPLAYSURF, ship, x, y)
    else:
        print 'mozilla'
    draw.reDrawAll(ownship, ship, draw.DISPLAYSURF, x, y)

def compTurn(enemyship,ship):
    x = random.randint(0,9)
    y = random.randint(0,9)
    draw.drawBum(x*30,y*30)

    print x,y

    ship.delFromKorabli(x,y)
    draw.reDrawAll(ship,enemyship,draw.drawShip,x,y)


