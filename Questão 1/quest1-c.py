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


f = '1-(((20**2)/(9.81*((3*x + ((x**2)/2))**3)))*(3+x))'

falsa_posicao(f, 0.6, 2.6, 0.0001)
