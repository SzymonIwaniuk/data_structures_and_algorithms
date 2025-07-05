from heapq import heappop, heappush
from typing import List

INF = float("inf")


def plan(T: List[int]) -> List[int]:
    n = len(T)
    fuel = 0
    heap = [(-T[0], 0)]
    result = []

    for i in range(1, n):
        if fuel == 0:
            oil, index = heappop(heap)
            fuel -= oil
            result += [index]

        fuel -= 1
        if T[i] > 0:
            heappush(heap, (-T[i], i))

    return result


def plan_dp(T: List[int]) -> List[int]:
    n = len(T)
    dp = [[INF for i in range(25)] for j in range(n)]
    dp[0][min(T[0], 24)] = 1
    decisions = [[None for i in range(25)] for j in range(n)]
    decisions[0][min(T[0], 24)] = (-1, -1)

    for i in range(1, n):
        for fuel in range(25):
            if dp[i - 1][fuel] == INF:
                continue

            if fuel > 0:
                if dp[i][fuel - 1] > dp[i - 1][fuel]:
                    dp[i][fuel - 1] = dp[i - 1][fuel]
                    decisions[i][fuel - 1] = (i - 1, fuel)

            if T[i] > 0 and fuel > 0:
                new_fuel = min(fuel - 1 + T[i], 24)
                if dp[i][new_fuel] > dp[i - 1][fuel] + 1:
                    dp[i][new_fuel] = dp[i - 1][fuel] + 1
                    decisions[i][new_fuel] = (i - 1, fuel)

    min_stops = INF
    index = -1
    for i in range(n):
        if dp[n - 1][i] < min_stops:
            min_stops = dp[n - 1][i]
            index = i

    path = []
    i, j = n - 1, index

    while (i, j) != (-1, -1):
        prev_i, prev_j = decisions[i][j]
        if prev_i == -1 or dp[i][j] > dp[prev_i][prev_j]:
            path.append(i)
        i, j = prev_i, prev_j

    return path[::-1]


if __name__ == "__main__":
    T = [3, 0, 2, 1, 0, 2, 5, 0]
    print(plan(T))
    print(plan_dp(T))
