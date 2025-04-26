# 6 Stacje benzynowe: Mamy mape miast i miasta s i t. W niektorych miastach mamy stacje paliw z cenami za litr,
# wagi krawedzi sa wyrazone w kilometrach
# Samochod pali 1l/1km, pojemnosc baku D i w kazdym miescie tankujemy ile chcemy. Zadanie znalezc najtansza trase.

import heapq


def gas_stations(
    G: list[list[list[int, int]]], P: list[any], D: int, s: int, t: int
) -> int:
    n = len(G)
    parent = [None] * n
    visited = [False] * n
    visited[s] = True
    cost = [[float("inf")] * (D + 1) for _ in range(n)]
    cost[s][0] = 0
    Q = [[0, s, 0]]

    while Q:
        current_cost, city, fuel = heapq.heappop(Q)

        if city == t:
            return current_cost

        if P[city] is not None and fuel < D:
            for new_city, distance in G[city]:
                if distance > fuel:
                    fuel_needed = distance - fuel
                    new_fuel = fuel + fuel_needed
                    if new_fuel <= D:
                        new_cost = current_cost + fuel_needed * P[city]
                        if new_cost < cost[city][new_fuel]:
                            cost[city][new_fuel] = new_cost
                            heapq.heappush(Q, [new_cost, city, new_fuel])

        for new_city, distance in G[city]:
            if distance <= fuel:
                new_fuel = fuel - distance
                if current_cost < cost[new_city][new_fuel]:
                    cost[new_city][new_fuel] = current_cost
                    heapq.heappush(Q, [current_cost, new_city, new_fuel])

    return -1


if __name__ == "__main__":
    G = [[(1, 5), (2, 10)], [(0, 5), (2, 7)], [(0, 10), (1, 7)]]
    P = [2, 3, 1]
    D = 10
    s = 0
    t = 2

    print(gas_stations(G, P, D, s, t))
