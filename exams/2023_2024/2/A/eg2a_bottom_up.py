from egz2atesty import runtests

inf = float("inf")


def wired(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    dp = [[inf for _ in range(n)] for __ in range(n)]

    for i in range(n - 1):
        dp[i][i + 1] = 1 + abs(T[i] - T[i + 1])

    for interval in range(4, n + 1, 2):
        for i in range(n - interval + 1):
            j = i + interval - 1
            dp[i][j] = min(
                dp[i + 1][j - 1] + 1 + abs(T[i] - T[j]),
                min(dp[i][k] + dp[k + 1][j] for k in range(i + 1, j, 2)),
            )

    return dp[0][n - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wired, all_tests=True)
