import numpy as np

# Método da falsa posição


def falsa_posicao(f, x0, x1, erro):

    f = eval('lambda x:' + f)
    x2 = x1
    it = 0

    while (min(abs(x1-x0), abs(x2)) > erro):
        it += 1

        x2 = ((f(x1) * x0)-(f(x0) * x1)) / (f(x1) - f(x0))
        print("(it = {0:d}) f(x2)={1:f}  | x2={2:f}  | erro={1:f}".format(
            it, f(x2), x2, abs(x2-x1)))

        if f(x2) == 0:
            print(f"Resultado: {x2} // iterações: {it}  // precisão: {erro}")
            return x2
        elif abs(x2-x1) < erro:
            x0 = x2
        else:
            x1 = x2
    else:
        print(f"Resultado: {x2} // iterações: {it}  // precisão: {erro}")
        return x2


f = '(320000/(1+(31*np.exp(-0.09*x)))) - 1.45*((80000*(np.exp(-0.05*x)))+110000)'

falsa_posicao(f, 39, 45, 0.001)
