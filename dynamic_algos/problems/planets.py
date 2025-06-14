from typing import List, Tuple


INF = float("inf")


def planets(D: List[int], C: List[Tuple[int, int]], T: List[int], E: int) -> int:
    n = len(D)
    dp = [[INF] * (E + 1) for i in range(n)]

    # edge case
    for i in range(E + 1):
        dp[0][i] = i * C[0]

    teleport, price = T[0]

    if dp[teleport][0] > price:
        dp[teleport][0] = price

    for planet in range(1, n):
        distance = D[planet] - D[planet - 1]

        for fuel in range(E + 1):
            index = 0
            if fuel + distance <= E:
                index += 1
                dp[planet][fuel] = min(
                    dp[planet][fuel], dp[planet - 1][fuel + distance]
                )

            else:
                dp[planet][fuel] = min(
                    dp[planet][fuel], dp[planet][fuel - 1] + C[planet]
                )

        teleport, price = T[planet]

        if dp[teleport][0] > dp[planet][0] + price:
            dp[teleport][0] = dp[planet][0] + price

    # for i in range(n):
    # print(dp[i])

    return min(dp[n - 1])


if __name__ == "__main__":
    D = [0, 5, 10, 20]
    C = [2, 1, 3, 9]
    T = [(2, 3), (3, 7), (2, 10), (3, 10)]
    E = 10
    print(planets(D, C, T, E))
    T2 = [(3, 2), (3, 7), (2, 10), (3, 10)]
    E2 = 20
    print(planets(D, C, T2, E2))
