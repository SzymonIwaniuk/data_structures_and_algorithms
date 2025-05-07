from collections import deque
from typing import Tuple

"""
Mamy sieć autostrad między miastami, niektóre z nich są płatne.
Kierowca chce przejechać tak, żeby zapłacić jak najmniej (Mamy graf z wagami 0 lub 1.
Szukamy najtańszej ścieżki s -> t.)
"""


def autostrady(G: list[list[Tuple[int, int]]], s: int, t: int) -> any:
    n = len(G)
    dist = [float("inf")] * n
    dist[s] = 0
    q = deque()
    q.append(s)

    while len(q) > 0:
        u = q.popleft()
        for v, cost in G[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                if cost == 0:
                    q.appendleft(v)
                else:
                    q.append(v)

    return dist[t]


if __name__ == "__main__":

    G = [[(1, 0), (2, 1)], [(2, 0), (3, 1)], [(3, 0)], []]
    print(autostrady(G, 0, 3))
