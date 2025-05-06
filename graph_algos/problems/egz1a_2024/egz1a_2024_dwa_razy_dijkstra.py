from heapq import heappush, heappop
from egz1atesty import runtests
from typing import Tuple


def convert_to_list(
    G: list[Tuple[int, int, int]],
) -> list[list[Tuple[int, int]]]:
    maxi = 0

    for v, u, d in G:
        maxi = max(v, u, maxi)

    G_copy = [[] for _ in range(maxi + 1)]

    for v, u, d in G:
        G_copy[v].append((u, d))
        G_copy[u].append((v, d))

    return G_copy


def dijkstra(
    G: list[list[Tuple[int, int]]],
    s: int
) -> list[int]:

    n = len(G)
    distance = [float("inf") for _ in range(n)]
    distance[s] = 0
    Q = [(0, s)]

    while Q:

        cur_dist, v = heappop(Q)

        if cur_dist > distance[v]:
            continue

        for u, d in G[v]:
            dist = cur_dist + d
            if dist < distance[u]:
                distance[u] = dist
                heappush(Q, (dist, u))

    return distance


def armstrong(
    B: list[Tuple[int, int, int]],
    G: list[Tuple[int, int, int]],
    s: int,
    t: int,
) -> int:
    G_copy = convert_to_list(G)

    distance1 = dijkstra(G_copy, s)
    distance2 = dijkstra(G_copy, t)
    mini = distance1[t]

    for v, p, q in B:
        # Run from s to v (distance1[v]) -> pick up bike -> ride from v to t on bike (distance2[v] * p / q)
        mini = min(mini, distance1[v] + (distance2[v] * p / q))

    return int(mini)


if __name__ == "__main__":
    runtests(armstrong, all_tests=True)
