from math import inf

from egz2btesty import runtests


def parking(X, Y):
    n = len(X)
    m = len(Y)
    dp = [[None] * (m + 1) for _ in range(n)]

    def parking_rec(i, j):
        if i == n:
            return 0

        if j == m:
            return inf

        if dp[i][j] != None:
            return dp[i][j]

        min_dist = inf
        min_dist = min(
            abs(X[i] - Y[j]) + parking_rec(i + 1, j + 1), parking_rec(i, j + 1)
        )

        dp[i][j] = min_dist
        return min_dist

    return parking_rec(0, 0)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
