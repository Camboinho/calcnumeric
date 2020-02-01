# Método de Newton

from numpy import linspace
from matplotlib.pyplot import plot
import numpy as np

def newton(x0,f,df,tol,nmax,var,plotar):

    f = eval('lambda x:' + f)
    df = eval('lambda x:' + df)

    it = 0 # contador de iteracoes

    # imprime estimativa inicial
    print('Estimativa inicial: x0 = {0}\n'.format(x0))  

    # Loop 
    for i in range(0,nmax):
        
        x = x0 - f(x0)/df(x0) # funcao de iteracao 
        
        e = abs(x-x0)/abs(x) # erro
        
        # tabela
        print('{0:d}  {1:f}  {2:f}  {3:f}  {4:e}'.format(i,x,f(x),df(x),e))
        
        if e < tol:
            break
        x0 = x                
        
    if i == nmax:
        print('Solução não obtida em {0:d} iterações'.format(nmax))
    else:
        print('Solução obtida: x = {0:.10f}'.format(x))

    # plotagem
    if plotar:        
        delta = 3*x
        dom = linspace(x-delta,x+delta,30)
        plot(dom,f(dom),x,f(x),'ro')

    return x
      
    
# parametros    
x0 = 10 # estimativa inicial
tol = 0.001 # tolerancia
nmax = 20 # numero maximo de iteracoes
f = '(320000/(1+(31*np.exp(-0.09*x)))) - 1.45*((80000*(np.exp(-0.05*x)))+110000)'   # funcao
df = '(5800*np.exp(-0.05*x)) + (((892800*np.exp(-0.09*x))) / (((31*np.exp(-0.09*x)) + 1))**2)'   # derivada dafuncao
var = 'x'
plotar = True

# chamada da função
xm = newton(x0,f,df,tol,nmax,var,plotar)

# -----------------------------------------------------------------------------------------------------------

#Método da falsa posição

def falsa_posicao(f, intervalo=[0,1], erro=0.001):
  
  f = eval('lambda x:' + f)
  x0 = intervalo[0]
  x1 = intervalo[1]
  x2 = x1
  it = 0

  while (min(abs(x1-x0), abs(x2)) > erro) and (it < 100):
    it += 1

    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
   
    if f(x2) == 0:
      print(f"falsa posição: resultado exato para x = {x2} em {it} iterações com precisão de {erro}");
      return x2
    elif abs(x2-x1) < erro:
      x0 = x2
    else:
      x1 = x2
  else:
    print(f"falsa posição - resultado final: {x2} em {it} iterações com precisao de {erro}")
    return x2
    

falsa_posicao(f, intervalo=[39,45], erro=0.001)