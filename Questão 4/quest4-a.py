from math import sin, cos, e


def f(x): return (7 * sin(x) * (e ** (x * -1))) - 1


def df(x): return (7 * (e ** (x * -1)) * (cos(x) - sin(x)))


pontos = 100

a, b = -7, -0
incremento = (abs(a) + abs(b)) / pontos

valores, posicoes, derivadas = [], [], []
n = a
i = 0
while i < pontos:
    posicoes.append(n)
    valores.append(f(n))
    derivadas.append(df(n))
    n += incremento
    i += 1

plt.axhline(y=0, ls='--', color='r')
plt.plot(posicoes, valores, color='b', label='função')
plt.plot(posicoes, derivadas, color='g', label='derivada')
plt.legend()
plt.show()
