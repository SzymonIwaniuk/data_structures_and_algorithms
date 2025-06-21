from math import inf
from heapq import heappush, heappop


def miasteczko_racing(D, C, k, s):
    D = [0] + D + [s]
    # print(D)
    C = [0] + C + [inf]
    # print(C)
    n = len(D)
    costs = [[inf] * (k + 1) for _ in range(n)]
    queue = [(0, 0, k)]

    while queue:
        current_cost, station, current_fuel = heappop(queue)

        if costs[station][current_fuel] < current_cost:
            continue

        costs[station][current_fuel] = current_cost

        if station == n - 1:
            continue

        new_cost = current_cost + (k - current_fuel) * C[station]
        for i in range(1, min(4, n - 1 - station)):
            heappush(queue, (new_cost, station + i, 0))

        for fuel in range(current_fuel, k + 1):
            distance = D[station + 1] - D[station]
            new_cost = current_cost + (fuel - current_fuel) * C[station]

            if distance <= fuel:
                heappush(queue, (new_cost, station + 1, fuel - distance))

    # print(costs)
    return min(costs[n - 1])


if __name__ == "__main__":
    D = [2, 6, 8, 9, 11, 12]
    C = [5, 3, 1, 4, 2, 9]
    k = 5
    s = 15
    print(miasteczko_racing(D, C, k, s))
