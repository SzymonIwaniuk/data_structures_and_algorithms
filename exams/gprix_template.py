from math import inf

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

    def grand_prix_rec(station: int, fuel: int) -> int:
        # print(station, fuel)
        if station == n - 1:
            return 0

        if dp[station][fuel] != inf:
            return dp[station][fuel]

        min_cost = inf
        distance = D[station + 1] - D[station]

        for new_fuel in range(fuel, k + 1):
            fuel_cost = (new_fuel - fuel) * C[station]

            if new_fuel >= distance:
                min_cost = min(
                    min_cost,
                    grand_prix_rec(station + 1, new_fuel - distance) + fuel_cost,
                )

            if new_fuel == k:
                for new_station in range(station + 1, min(station + 4, n)):
                    min_cost = min(min_cost, grand_prix_rec(new_station, 0) + fuel_cost)

        dp[station][fuel] = min_cost
        return min_cost

    grand_prix_rec(0, k)
    # print(dp)
    return dp[0][k]


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
