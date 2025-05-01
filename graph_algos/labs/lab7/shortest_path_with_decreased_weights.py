# 3. Najkrotsze sciezki przy malejacych krawedziach

from heapq import heappop, heappush
from typing import Tuple


def modified_dijkstra(G: list[list[Tuple[int, float]]], s: int) -> list[float]:
    n = len(G)
    distance = [float("inf")] * n
    Q = [(0, s, float("inf"))]

    while Q:
        d, v, prev_w = heappop(Q)
        if d >= distance[v]:
            continue

        distance[v] = d

        for u, w in G[v]:
            if w < prev_w:
                heappush(Q, (d + w, u, w))

    return distance


# O(ElogE) ~ O(ElogV)

if __name__ == "__main__":
    G1 = [
        [(1, 10), (2, 6), (3, 5)],
        [(0, 10), (3, 15)],
        [(0, 6), (3, 4)],
        [(0, 5), (1, 15), (2, 4), (4, 2)],
        [(3, 2)],
    ]

    G2 = [[(1, 10), (2, 6), (3, 5)], [(0, 10)], [(3, 4)], [(0, 5), (1, 5), (2, 4)], []]

    G3 = [[(1, 10), (2, 6)], [(3, 5)], [(3, 4)], [(4, 3)], []]

    print(modified_dijkstra(G1, 0))
    print(modified_dijkstra(G2, 0))
    print(modified_dijkstra(G3, 0))
