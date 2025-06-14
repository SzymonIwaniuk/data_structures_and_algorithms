from typing import List


def min_cost(O: List[int], C: List[int], T: int, L: int) -> int:
    n = len(O)

    parkings = list(zip(O, C))
    parkings.sort()

    positions = [0] + [p[0] for p in parkings] + [L]
    costs = [0] + [p[1] for p in parkings] + [0]
    # print(positions)
    # print(costs)
    n = len(positions)
    INF = float("inf")
    dp = [[INF, INF] for _ in range(n)]
    dp[0][0] = 0

    for i in range(1, n):
        for j in range(i):
            dist = positions[i] - positions[j]

            if dist <= T:
                dp[i][0] = min(dp[i][0], dp[j][0] + costs[i])

                dp[i][1] = min(dp[i][1], dp[j][1] + costs[i])

            elif dist <= 2 * T:
                dp[i][1] = min(dp[i][1], dp[j][0] + costs[i])

    return min(dp[-1][0], dp[-1][1])


if __name__ == "__main__":
    O = [17, 20, 11, 5, 12]
    C = [9, 7, 7, 7, 3]
    T = 7
    L = 25
    print(min_cost(O, C, T, L))
