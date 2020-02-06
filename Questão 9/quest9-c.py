import numpy as np


def pivotamentoTotal(A):
    m = len(A)
    U = A.copy().astype(float)
    L = np.eye(m)
    P = np.eye(m)
    Q = np.eye(m)
    for k in range(m):
        pivo = abs(U[k, k])
        maxindex_i = k
        maxindex_j = k

        for i in range(k, m):
            for j in range(k, m):
                if abs(U[i, j]) > pivo:
                    pivo = abs(U[i, j])
                    maxindex_i = i
                    maxindex_j = j
        Q[:, [k, maxindex_j]] = Q[:, [maxindex_j, k]]
        P[[k, maxindex_i]] = P[[maxindex_i, k]]

        for i in range(m):
            troca = U[maxindex_i, i]
            U[maxindex_i, i] = U[k, i]
            U[k, i] = troca
        for j in range(m):
            troca1 = U[j, maxindex_j]
            U[j, maxindex_j] = U[j, k]
            U[j, k] = troca1

        for i in range(k):
            troca0 = L[maxindex_i, i]
            L[maxindex_i, i] = L[k, i]
            L[k, i] = troca0
        for j in range(k):
            troca2 = L[j, maxindex_j]
            L[j, maxindex_j] = L[j, k]
            L[j, k] = troca2

        for j in range(k + 1, m):
            L[j, k] = float(U[j, k]) / U[k, k]
            for q in range(k, m):
                U[j, q] -= L[j, k] * U[k, q]

    return P, Q, L, U


A = [[0.4, -0.1, 0, -0.1], [-0.1, 0.3, -0.2, 0],
     [0, -0.2, 0.26666, -0.06666], [-0.1, 0, -0.06666, 0.21666]]
A = np.array(A)

P1, Q1, L1, U1 = pivotamentoTotal(A)

print(P1)
print(Q1)
print(L1)
print(U1)
