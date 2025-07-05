from math import inf

from zad9testy import runtests


def min_cost(O, C, T, L):
    parkings_with_costs = list(zip(O, C))
    parkings_with_costs.sort(key=lambda x: x[0])
    positions = [(0, 0)] + parkings_with_costs + [(L, 0)]
    n = len(positions)
    costs = [[inf] * 2 for _ in range(n)]

    def dp(i, is_used):
        if i == n - 1:
            return 0

        if costs[i][is_used] != inf:
            return costs[i][is_used]

        k = m = i
        k += 1
        m += 1

        mini = inf
        parking_cost = positions[i][1]

        while k < n and positions[k][0] - positions[i][0] <= T:
            mini = min(mini, dp(k, is_used) + parking_cost)
            k += 1

        if is_used == 0:
            while m < n and positions[m][0] - positions[i][0] <= 2 * T:
                mini = min(mini, dp(m, 1) + parking_cost)
                m += 1

        costs[i][is_used] = mini
        return mini

    return dp(0, 0)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)
