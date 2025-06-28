from egz1btesty import runtests
from math import inf


def planets(D, C, T, E):
    n = len(D)
    dp = [[inf] * (E + 1) for _ in range(n)]

    def planets_rec(i, b):
        if i == n - 1:
            return 0

        if dp[i][b] != inf:
            return dp[i][b]

        min_cost = inf
        distance = D[i + 1] - D[i]

        for fuel in range(b, E + 1):
            if fuel == 0 and T[i][0] != i:
                min_cost = min(min_cost, T[i][1] + planets_rec(T[i][0], 0))
            get_fuel = fuel - b

            if fuel >= distance:
                min_cost = min(
                    min_cost, get_fuel * C[i] + planets_rec(i + 1, fuel - distance)
                )

        dp[i][b] = min_cost
        return min_cost

    return planets_rec(0, 0)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
