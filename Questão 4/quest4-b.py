from math import sin, cos, e

#Método de Newton

def newton(x0,f,df,erro):

    f = eval('lambda x:' + f)
    df = eval('lambda x:' + df)

    it = 0

    print('Estimativa inicial: x0 = {0}\n'.format(x0)) 

    while(1):
        it+=1

        x = x0 - f(x0)/df(x0) #Função de iteração
        
        e = abs(x-x0)/abs(x) #Erro
        
        print('{0:d}  {1:f}  {2:f}  {3:f}  {4:e}'.format(it,x,f(x),df(x),e))

        if(e <= erro):
          break

        x0 = x                

    print('Solução obtida: x = {0:.10f}'.format(x))

    return x

df= '7 * (e ** (x* -1)) * (cos(x) - sin(x))'

f= '(7 * sin(x) * (e ** (x * -1))) - 1'

newton(-4, f, df, 0.0001)   