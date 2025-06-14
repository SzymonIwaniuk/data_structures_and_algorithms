from typing import List


def wired(T: List[int]) -> int:
    n = len(T)
    dp = [[float("inf")] * n for _ in range(n)]

    for i in range(n - 1):
        dp[i][i + 1] = 1 + abs(T[i] - T[i + 1])

    for lenght in range(4, n + 1, 2):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = min(
                dp[i + 1][j - 1] + 1 + abs(T[i] - T[j]),
                min(dp[i][k] + dp[k + 1][j] for k in range(i + 1, j, 2)),
            )

    return dp[0][n - 1]
