from kol2testy import runtests
from heapq import heappush, heappop
from typing import Tuple

"""
Szymon Filip Iwaniuk
Moje rozwiązanie wykorzystuje zmodyfikowany algorytm Dijkstry.
Na początku zamieniam listę krawędzi na reprezentację listową (listę sąsiedztwa).
Podczas działania algorytmu, jeżeli sąsiad aktualnie przetwarzanego wierzchołka jest resortem,
to nie dodajemy go do kolejki. W przeciwnym razie dodajemy go normalnie. Rozwiązanie działa poprawnie,
ponieważ algorytm nie rozwija ścieżek prowadzących dalej od resortów — przetwarza je tylko do momentu
dotarcia do danego resortu. Na końcu działania algorytmu dla każdego wierzchołka zawierającego resort
sumujemy koszt dojścia * 2 (ponieważ zakładamy również powrót). Złożoność czasowa: O(E log V).
"""


def convert_to_list(flights: list[Tuple[int, int, int]]) -> list[list[Tuple[int, int]]]:

    maxi = 0
    for u, v, d in flights:
        maxi = max(maxi, u, v)

    G = [[] for _ in range(maxi + 1)]
    for u, v, d in flights:
        G[v].append((u, d))
        G[u].append((v, d))

    return G


def dijkstra(
    start_city: int, G: list[list[Tuple[int, int]]], resorts: list[int]
) -> int:

    n = len(G)
    costs = [float("inf") for _ in range(n)]
    costs[start_city] = 0
    visited = [False for _ in range(n)]
    Q = [(0, start_city)]
    sum_of_costs = 0

    for r in resorts:
        visited[r] = True

    while Q:

        cur_cost, v = heappop(Q)
        if costs[v] < cur_cost:
            continue

        for u, cost in G[v]:
            if costs[u] > costs[v] + cost:
                costs[u] = costs[v] + cost
                if not visited[u]:
                    heappush(Q, (costs[u], u))

    for r in resorts:
        sum_of_costs += costs[r] * 2
    return sum_of_costs


def lets_roll(
    start_city: int, flights: list[Tuple[int, int, int]], resorts: list[int]
) -> int:

    G = convert_to_list(flights)
    return dijkstra(start_city, G, resorts)


runtests(lets_roll, all_tests=True)
