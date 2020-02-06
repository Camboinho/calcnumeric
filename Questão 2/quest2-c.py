# Método de Newton


def newton(x0, f, df, erro):

    f = eval('lambda x:' + f)
    df = eval('lambda x:' + df)

    it = 0

    print('Estimativa inicial: x0 = {0}\n'.format(x0))

    while(1):
        it += 1

        x = x0 - f(x0)/df(x0)  # Função de iteração

        e = abs(x-x0)/abs(x)  # Erro

        print('{0:d}  {1:f}  {2:f}  {3:f}  {4:e}'.format(it, x, f(x), df(x), e))

        if(e <= erro):
            break

        x0 = x

    print('Solução obtida: x = {0:.10f}'.format(x))

    return x


df = '(5800*np.exp(-0.05*x)) + (((892800*np.exp(-0.09*x))) / (((31*np.exp(-0.09*x)) + 1))**2)'

f = '(320000/(1+(31*np.exp(-0.09*x)))) - 1.45*((80000*(np.exp(-0.05*x)))+110000)'

newton(5, f, df, 0.001)
