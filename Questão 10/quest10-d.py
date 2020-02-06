def gaussSeidel(A, b, x, N, erro):
    maxIterations = 1000000
    xprev = [0.0 for i in range(N)]

    for i in range(maxIterations):
        for j in range(N):
            xprev[j] = x[j]
        for j in range(N):
            somatorio = 0.0
            for k in range(N):
                if (k != j):

                    somatorio = somatorio + A[j][k] * x[k]

            x[j] = (b[j] - somatorio) / A[j][j]

        diff1norm = 0.0
        oldnorm = 0.0
        for j in range(N):
            diff1norm = diff1norm + abs(x[j] - xprev[j])
            oldnorm = oldnorm + abs(xprev[j])
        if oldnorm == 0.0:
            oldnorm = 1.0
        norm = diff1norm / oldnorm

        if (norm < erro) and i != 0:
            print("Converge para:  [", end="")
            for j in range(N - 1):
                print(x[j], ",", end="")
                print()
            print(x[N - 1], "]. Levou", i + 1, "iteracoes")
            return
    print("Nao converge")


A = [[-0.866, 0, 0.707, 0, 0, 0, 0],
     [0, -1, 0, 1, 0, 0, 0],
     [-0.5, 0, -0.707, 0, 0, 0, 0],
     [0, 0, -0.707, -1, 0, 0, 0],
     [0.5, 0, 0, 0, 1, 0, 0],
     [0, 0, 0.707, 0, 0, 1, 0],
     [0.866, 0, 0, 0, 0, 0, 1]]

b = [-700, -500, 1100, 0, 0, 0, 0]

x = [0, 0, 0, 0, 0, 0, 0]


gaussSeidel(A, b, x, 7, 0.0001)
