import view

def vistrel(ownship, ship, mx, my):
    x = (mx-390)/30
    y = my/30 - 1
    if ship.delFromKorabli(x,y) == 'tada':
        print 'tada'
       # view.drawEnemyShip(view.DISPLAYSURF, ship, x, y)
    else:
        print 'mozilla'
    view.reDrawAll(ownship, ship, view.OWNSHIPCOLOR, 'own', view.DISPLAYSURF, x,y)

