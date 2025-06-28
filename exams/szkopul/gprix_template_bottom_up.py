from math import inf
from typing import List

"""Dijkstra tu nie dziala xp"""


def grand_prix(
    D: List[int],
    C: List[int],
    k: int,
    s: int,
) -> int:

    D = [0] + D + [s]
    C = [0] + C + [inf]
    n = len(D)
    dp = [[inf] * (k + 1) for _ in range(n)]
    dp[0][k] = 0

    for i in range(1, n):
        distance = D[i] - D[i - 1]
        # print(i, i - 1, max(i-4, -1))
        # for station in range(i - 1, max(i-4, -1), -1):
        #     dp[i][0] = min(dp[i][0], dp[station][k])

        for j in range(distance, k + 1):
            dp[i][j - distance] = min(dp[i][j - distance], dp[i - 1][j])

        for station in range(max(0, i - 3), i):
            dp[i][0] = min(dp[i][0], dp[station][k])

        for fuel in range(1, k + 1):
            dp[i][fuel] = min(dp[i][fuel], dp[i][fuel - 1] + C[i])

    return min(dp[n - 1])


# if __name__ == '__main__':
#     D = [2, 6, 8, 9, 11, 12]
#     C = [5, 3, 1, 4, 2, 9]
#     k = 5
#     s = 15
#     print(grand_prix(D, C, k, s))


"""
Uprzejmie prosimy o niemodyfikowanie kodu poniżej :)
"""

line = input()
data = list(map(int, line.strip().split()))
n = data[0]
k = data[1]
s = data[2]
D = data[3 : 3 + n]
C = data[3 + n : 3 + 2 * n]
sol = grand_prix(D, C, k, s)
print(sol)
