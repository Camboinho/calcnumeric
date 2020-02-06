from matplotlib import pyplot as plt

Q = 20.0
g = 9.81


def A(y): return (3.0 * y) + ((y ** 2)/2.0)


def B(y): return 3.0 + y


def f(y): return 1 - (((Q ** 2.0) / (g * A(y) ** 3.0)) * B(y))


pontos = 100

a, b = 1, 5
incremento = (abs(a)+abs(b)) / pontos

valores, posicoes = [], []
n = 1
i = 0
while i < pontos:
    posicoes.append(n)
    valores.append(f(n))
    n += incremento
    i += 1

plt.axhline(y=0, ls='--', color='r')
plt.plot(posicoes, valores, color='b')
plt.show()
