from zad9testy import runtests
from math import inf
from heapq import heappush, heappop


def binary_search(array, max_dist, left, right):

    while left < right:
        mid = (left + right) // 2

        if array[mid][0] > max_dist:
            right = mid
        else:
            left = mid + 1

    return left


def min_cost(O, C, T, L):
    parkings_with_costs = list(zip(O, C))
    parkings_with_costs.sort(key=lambda x: x[0])
    positions = [(0,0)] + parkings_with_costs + [(L, 0)]
    n = len(positions)
    costs = [[inf] * 2 for _ in range(n)]
    costs[0][0] = 0
    queue = [(0, 0, 0)]
    # print(positions)
    # print(binary_search(positions, 12, 2, n - 1))

    while queue:
        cost, i, is_used = heappop(queue)

        if costs[i][is_used] < cost:
            continue

        if i == n - 1:
            continue

        parking_cost = positions[i][1]
        max_distance = positions[i][0] + T
        max_ind = binary_search(positions, max_distance, i + 1, n)

        for j in range(i + 1, max_ind):
            if costs[j][is_used] > cost + parking_cost:
                costs[j][is_used] = cost + parking_cost
                heappush(queue, (cost + parking_cost, j, is_used))

        if is_used == 0:
            max_distance += T
            max_ind = binary_search(positions, max_distance, i + 1, n)
            for j in range(i + 1, max_ind):
                if costs[j][1] > cost + parking_cost:
                    costs[j][1] = cost + parking_cost
                    heappush(queue, (cost + parking_cost, j, 1))

    #print(costs)
    return min(costs[-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True)
