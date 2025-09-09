from typing import List

from kol3testy import runtests

INF = float("inf")


def parkiet(B: List[List[int]], C: List[List[int]], s: int) -> int:
    n = len(B)
    m = len(B[0])
    dp = [[INF] * (m + 1) for _ in range(n)]

    def parkiet_rek(i: int, j: int) -> int:
        if C[i][j] <= s:
            return 0

        if dp[i][j] != INF:
            return dp[i][j]

        mini = INF
        # print(i,j,steps)
        if j + 1 < m:
            tmp = C[i][j] - C[i][j + 1]

            if tmp <= s:
                mini = min(mini, parkiet_rek(i, j + 1) + 1)

        if i + 1 < n:
            tmp = C[i][j] - C[i + 1][j]

            if tmp <= s:
                mini = min(mini, parkiet_rek(i + 1, j) + 1)

        dp[i][j] = mini
        return mini

    parkiet_rek(0, 0)
    return dp[0][0]


if __name__ == "__main__":
    runtests(parkiet, all_tests=True)
