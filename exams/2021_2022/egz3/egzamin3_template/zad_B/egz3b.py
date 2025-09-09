from egz3btesty import runtests
def maze(L):
    n = len(L)
    dp = [[-1 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        if L[i][0] == '#':
            break

        dp[i][0] = i

    for c in range(1, n):
        up = [-1] * n
        down = [-1] * n

        for r in range(n):
            if L[r][c] == '#':
                continue

            # z lewej
            if dp[r][c-1] != -1:
                up[r] = max(up[r], dp[r][c-1] + 1)

            # z gory
            if r > 0 and up[r-1] != -1:
                up[r] = max(up[r], up[r-1] + 1)

        for r in range(n-1, -1, -1):
            if L[r][c] == '#':
                continue

            if dp[r][c-1] != -1:
                down[r] = max(down[r], dp[r][c-1] + 1)

            # z dolu
            if r < n-1 and down[r+1] != -1:
                down[r] = max(down[r+1] + 1, down[r])

        for r in range(n):
            dp[r][c] = max(up[r], down[r])

    return dp[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True)
