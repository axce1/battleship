import draw

def vistrel(ownship, ship, mx, my):
    y = (mx-390)/30
    x = my/30 - 1
    print x, y
    if ship.delFromKorabli(x,y) == 'tada':
        print 'tada'
       # draw.drawEnemyShip(draw.DISPLAYSURF, ship, x, y)
    else:
        print 'mozilla'
    draw.reDrawAll(ownship, ship, draw.OWNSHIPCOLOR, 'own', draw.DISPLAYSURF, x,y)

