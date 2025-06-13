def orchard(T, m):
    n = len(T)
    INF = float('inf')

    dp = [[INF] * m for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(m):
            if dp[i][j] < INF:
                new_j = (j + T[i]) % m
                dp[i+1][new_j] = min(dp[i+1][new_j], dp[i][j])

                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)


    return dp[n][0]





T = [2, 2, 7, 5, 11, 7]
m = 5

print(orchard(T, m))