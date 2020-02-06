import numpy as np


def f(x): return (320000/(1+(31*np.exp(-0.09*x)))) - \
    1.45*((80000*(np.exp(-0.05*x)))+110000)


pontos = 100

a, b = 20, 50
incremento = (abs(a) + abs(b)) / pontos

valores, posicoes = [], []
n = a
i = 0
while i < pontos:
    posicoes.append(n)
    valores.append(f(n))
    n += incremento
    i += 1

plt.axhline(y=0, ls='--', color='r')
plt.plot(posicoes, valores, color='b', label='função')
plt.legend()
plt.show()
