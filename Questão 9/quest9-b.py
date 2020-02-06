import numpy as np


def pivotamentoLU(matrix):
    n, m = matrix.shape
    P = np.identity(n)
    L = np.identity(n)
    U = matrix.copy()
    PF = np.identity(n)
    LF = np.zeros((n, n))
    for k in range(0, n - 1):
        index = np.argmax(abs(U[k:, k]))
        index = index + k

        if index != k:
            P = np.identity(n)
            P[[index, k], k:n] = P[[k, index], k:n]
            U[[index, k], k:n] = U[[k, index], k:n]
            PF = np.dot(P, PF)
            LF = np.dot(P, LF)
        L = np.identity(n)

        for j in range(k+1, n):
            L[j, k] = -(U[j, k] / U[k, k])
            LF[j, k] = (U[j, k] / U[k, k])
        U = np.dot(L, U)
    np.fill_diagonal(LF, 1)
    return PF, LF, U


A = [[0.4, -0.1, 0, -0.1], [-0.1, 0.3, -0.2, 0],
     [0, -0.2, 0.26666, -0.06666], [-0.1, 0, -0.06666, 0.21666]]
A = np.array(A)
P1, L1, U1 = pivotamentoLU(A)

print(P1)
print(L1)
print(U1)
