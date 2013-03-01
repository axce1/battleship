import draw

def vistrel(ownship, ship, mx, my):
    x = (mx-390)/30
    y = my/30 - 1
    if ship.delFromKorabli(x,y) == 'tada':
        print 'tada'
       # draw.drawEnemyShip(draw.DISPLAYSURF, ship, x, y)
    else:
        print 'mozilla'
    draw.reDrawAll(ownship, ship, draw.OWNSHIPCOLOR, 'own', draw.DISPLAYSURF, x,y)

