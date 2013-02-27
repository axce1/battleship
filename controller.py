import view

def vistrel(z, ship, mx, my):
    x = (mx-390)/30
    y = my/30 - 1
    if z.delFromKorabli(x,y) == 'tada':
        view.drawEnemyShip(view.DISPLAYSURF,ship, x,y)
    else:
        print 'mozilla'

