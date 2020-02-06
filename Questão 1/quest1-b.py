def bissecao(f, x0, x1, erro):

    f = eval('lambda x:' + f)
    fx0 = f(x0)
    fx1 = f(x1)

    done = 0

    xm = (x1+x0)/2
    it = 1

    while abs(x0-x1) > erro and (not done):
        fxm = f(xm)
        print("(it = {0:d}) f(xm)={1:f}  | f(x0)={2:f}  | f(x1)={3:f}".format(
            it, fxm, fx0, fx1))

        if fx0*fxm < 0:          # Raiz está à esquerda
            x1 = xm
            fx1 = fxm
            xm = (x0+x1)/2
        elif fxm*fx1 < 0:       # Raiz está à direita
            x0 = xm
            fx0 = fxm
            xm = (x0+x1)/2
        else:                   # Raiz encontrada
            done = 1
        it += 1

    return xm


f = '1-(((20**2)/(9.81*((3*x + ((x**2)/2))**3)))*(3+x))'

bissecao(f, 0.6, 2.6, 0.001)
