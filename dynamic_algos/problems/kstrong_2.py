from heapq import heappush, heappop

INF = float('inf')

def kstrong(T, k):
    n = len(T)
    INF = float('inf')
    dp = [[-INF] * (k + 1) for _ in range(n)]

    # Bazowe przypadki
    dp[0][0] = T[0]
    if k >= 1:
        dp[0][1] = 0  # Usuwamy pierwszy element

    for i in range(1, n):
        for z in range(k + 1):
            # 1) Kontynuacja podciągu bez usuwania elementu i
            if dp[i-1][z] != -INF:
                dp[i][z] = max(dp[i][z], dp[i-1][z] + T[i])

            # 2) Kontynuacja podciągu z usunięciem elementu i
            if z > 0 and dp[i-1][z-1] != -INF:
                dp[i][z] = max(dp[i][z], dp[i-1][z-1])

        # 3) Rozpoczęcie nowego podciągu od i-tego elementu (bez usunięć)
        dp[i][0] = max(dp[i][0], T[i])
        # 4) Rozpoczęcie nowego podciągu od i-tego elementu (z usunięciem i-tego elementu)
        if k >= 1:
            dp[i][1] = max(dp[i][1], 0)

    return max(max(row) for row in dp)


# Testy:
T1 = [-20, 5, -1, 10, 2, -8, 10]
T2 = [-20, 20, 3, -3, 1]

print(kstrong(T1, 1))  # 26
print(kstrong(T2, 1))  # 21
print(kstrong(T2, 2))  # 24
