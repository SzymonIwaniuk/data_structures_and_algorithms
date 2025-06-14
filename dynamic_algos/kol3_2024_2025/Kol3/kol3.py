from kol3testy import runtests
from typing import List


"""
Szymon Iwaniuk
Stosujac podejscie zachlanne odcinam najwiekszy mozliwy kawalek deski spelniajacy warunki zadania aktualizuje
wspolrzedne od ktorych zaczynam ta sama procedure dla 'nowej' deski oraz aktualizuje cnt.
Dowodem na zachlanne rozwiazanie jest to ze po odcieciu najwiekszej mozliwej deski uzyskuje ta sama instancje problemu
tylko z powiekszonym cnt o jeden. Na koncu zwracam wynik. Zlozonosc czasowa algorytmu szacuje na O(n^2*m) v O(m^2*n).
"""


INF = float("inf")


def parkiet(B: List[List[int]], C: List[List[int]], s: int) -> int:
    # n = len(B)
    # m = len(B[0])
    # cnt = 0
    # x, y = 0, 0
    # prev = (None, None)

    # while x != n - 1 and y != m - 1:
    #     if x == prev[0] and y == prev[1]:
    #         return -1

    #     if C[x][y] <= s:
    #         return cnt + 1

    #     current1 = 0
    #     current2 = 0

    #     for i in range(x, m):
    #         #print(C[x][y] - C[x][i])
    #         if C[x][y] - C[x][i] <= s and C[x][y] - C[x][i] >= current1:
    #             current1 = C[x][y] - C[x][i]
    #             new_y1 = i
    #             new_x1 = x

    #     for j in range(y, n):
    #         #print(C[x][y] - C[j][y])
    #         if C[x][y] - C[j][y] <= s and C[x][y] - C[j][y] >= current2:
    #             current2 = C[x][y] - C[j][y]
    #             new_y2 = y
    #             new_x2 = j

    #     if current1 >= current2:
    #         prev = (x, y)
    #         x = new_x1
    #         y = new_y1
    #     else:
    #         prev = (x, y)
    #         x = new_x2
    #         y = new_y2

    #     #print(x, y, C[x][y])
    #     cnt += 1

    # return cnt + 1

    # INF = float('inf')
    # dp = [[INF] * m for _ in range(n)]
    # dp[0][0] = 0

    # while x != n - 1 and y != m - 1:
    #     for i in range(n-1):
    #             if C[i][j] - C[i][j] <= s:
    #                 dp[i][j] = min(dp[i][j], dp[i][j] + 1)

    #     for

    # for i in range(n):
    #     print(dp)

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
