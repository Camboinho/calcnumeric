from numpy import linspace
import numpy as np

# Sendo x0 a aproximação inicial, foi variado pra 0, 0.5 e 1000 (letras a, b e c)

x0 = 0.5

f = eval('lambda x:' + 'np.sin(x**(1/2)) - x')
g = eval('lambda x:' + 'np.sin(x**(1/2))')

it = 0
x, xn = x0, x0 + 1

e = abs(x-xn)/abs(x)

print('i\t x\t\t f(x)\t\t ER')
print('{0:d}\t {1:f}\t {2:f}\t {3:e}'.format(it, x, f(x), e))

while e >= 0.0001:
    it += 1
    xn = x
    x = g(xn)
    e = abs(x-xn)/abs(x)
    print('{0:d}\t {1:f}\t {2:f}\t {3:e}'.format(it, x, f(x), e))

print('Raiz: ', x)
