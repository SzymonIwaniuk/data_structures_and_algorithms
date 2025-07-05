from typing import List

from kol3testy import runtests

INF = float("inf")


def parkiet(B: List[List[int]], C: List[List[int]], s: int) -> int:
    n = len(B)
    m = len(B[0])
    dp = [[INF] * (m + 1) for _ in range(n)]

    def parkiet_rek(i: int, j: int, steps: int) -> int:
        if C[i][j] <= s:
            return steps

        elif B[i][j] > s:
            return -1

        if dp[i][j] != INF:
            return dp[i][j]

        mini = INF
        # print(i,j,steps)
        for x in range(j + 1, m):
            tmp = C[i][j] - C[i][x]

            if tmp <= s:
                mini = min(mini, parkiet_rek(i, x, steps + 1))

        for y in range(i + 1, n):
            tmp = C[i][j] - C[y][j]

            if tmp <= s:
                mini = min(mini, parkiet_rek(y, j, steps + 1))

        dp[i][j] = mini
        return mini

    parkiet_rek(0, 0, 0)
    return dp[0][0]


if __name__ == "__main__":
    runtests(parkiet, all_tests=True)
