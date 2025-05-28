from typing import List


def parking(X: List[int], Y: List[int]) -> int:
    n = len(X)
    m = len(Y)
    dp = [[float("inf") for i in range(m + 1)] for j in range(n + 1)]

    # Warunek brzegowy nie przypisujemy zadnego parkingu do wierzowca
    dp[0][0] = 0

    for x in range(n + 1):
        for y in range(m):
            dp[x][y + 1] = min(dp[x][y + 1], dp[x][y])

            if x < n:
                dp[x + 1][y + 1] = min(dp[x + 1][y + 1], dp[x][y] + abs(X[x] - Y[y]))

    return dp[n][m]


if __name__ == "__main__":
    X = [3, 6, 10, 14]
    Y = [1, 4, 5, 10, 11, 13, 17]

    print(parking(X, Y))
