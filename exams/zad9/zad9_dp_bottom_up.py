from math import inf

from zad9testy import runtests


def min_cost(O, C, T, L):
    parkings_with_costs = list(zip(O, C))
    parkings_with_costs.sort(key=lambda x: x[0])
    positions = [(0,0)] + parkings_with_costs + [(L, 0)]
    n = len(positions)
    costs = [[inf] * 2 for _ in range(n)]
    costs[0][0] = 0
    h = k = 0

    while h < n:
        i = j = h
        l = k

        min_ind_T1 = h + 1
        min_ind_T2 = k + 1
        while i < n - and positions[i + 1][0] - positions[h][0] <= T:
            costs[0][i + 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True)
