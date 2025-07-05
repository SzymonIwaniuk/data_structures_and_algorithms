from math import inf

from egz1btesty import runtests


def planets(D, C, T, E):
    n = len(D)
    dp = [[inf for _ in range(E + 1)] for _ in range(n)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(E + 1):
            if j != 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + C[i])

            if i < n - 1:
                dist = D[i + 1] - D[i]
                if j - dist >= 0:
                    dp[i + 1][j - dist] = min(dp[i + 1][j - dist], dp[i][j])

            if T[i][0] != i:
                dp[T[i][0]][0] = min(dp[i][0] + T[i][1], dp[T[i][0]][0])

    return min(dp[n - 1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
