INF = float("inf")


def parkiet(B, C, s):
    n = len(B)
    m = len(B[0])
    # dp = [INF * (m+1) for _ in range(n)]

    def parkiet_rek(i, j, steps):
        if C[i][j] <= s:
            return steps

        if i == n - 1 and j == m - 1 and B[i][j] > s:
            return -1

        mini = INF
        print(i, j, steps)
        for x in range(j + 1, m):
            tmp = C[i][j] - C[i][x]

            if tmp <= s:
                value = parkiet_rek(i, x, steps + 1)
                if value < mini:
                    mini = value

        for y in range(i + 1, n):
            tmp = C[i][j] - C[y][j]

            if tmp <= s:
                value = parkiet_rek(y, j, steps + 1)
                if value < mini:
                    mini = value

        return mini

    return parkiet_rek(0, 0, 0)

    # return dp[0][0]


B = [
    (2, 1, 3),
    (1, 3, 1),
    (2, 3, 3),
]

C = [(20, 15, 8), (13, 10, 4), (8, 6, 3)]

s = 5

print(parkiet(B, C, s))
