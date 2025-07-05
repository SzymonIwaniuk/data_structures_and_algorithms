from heapq import heappop, heappush
from typing import List

INF = float("inf")


def kstrong(T: List[int], k: int) -> int:
    n = len(T)
    INF = float("inf")
    dp = [[-INF] * (k + 1) for _ in range(n)]

    dp[0][0] = T[0]
    if k >= 1:
        dp[0][1] = 0

    for i in range(1, n):
        for z in range(k + 1):
            if dp[i - 1][z] != -INF:
                dp[i][z] = max(dp[i][z], dp[i - 1][z] + T[i])

            if z > 0 and dp[i - 1][z - 1] != -INF:
                dp[i][z] = max(dp[i][z], dp[i - 1][z - 1])

        dp[i][0] = max(dp[i][0], T[i])
        if k >= 1:
            dp[i][1] = max(dp[i][1], 0)

    return max(max(row) for row in dp)


if __name__ == "__main__":
    T1 = [-20, 5, -1, 10, 2, -8, 10]
    T2 = [-20, 20, 3, -3, 1]

    print(kstrong(T1, 1))
    print(kstrong(T2, 1))
    print(kstrong(T2, 2))
