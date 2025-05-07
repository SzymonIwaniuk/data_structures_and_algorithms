from heapq import heappop, heappush
from typing import Tuple


def convert_to_list(
    G: list[Tuple[int, int, int]],
) -> list[list[list[Tuple[int, int]], None]]:
    maxi = 0
    for v, u, d in G:
        maxi = max(v, u, maxi)

    G_copy = [[[], None] for _ in range(maxi + 1)]
    for v, u, d in G:
        G_copy[v][0].append((u, d))
        G_copy[u][0].append((v, d))

    return G_copy


def most_effective_bike(
    G: list[list[list[Tuple[int, int]], None]],
    B: list[Tuple[int, int, int]],
) -> list[list[list[Tuple[int, int]], (None | float)]]:

    for i, p, q in B:
        if G[i][1] != None:
            G[i][1] = min(p / q, G[i][1])
        else:
            if p / q < 1:
                G[i][1] = p / q

    return G


def armstrong(
    B: list[Tuple[int, int, int]],
    G: list[Tuple[int, int, int]],
    s: int,
    t: int,
) -> int:
    G_copy = convert_to_list(G)
    G_copy = most_effective_bike(G_copy, B)
    n = len(G_copy)

    distance = [[float("inf"), float("inf")] for _ in range(n)]
    distance[s][0] = 0
    Q = [(0, s, None)]

    # Dijkstra
    while Q:
        dist, v, bike = heappop(Q)
        if dist > min(distance[v]):
            continue

        if bike != None:
            for u, d in G_copy[v][0]:
                if distance[u][1] > distance[v][1] + d * G_copy[bike][1]:
                    distance[u][1] = distance[v][1] + d * G_copy[bike][1]
                    heappush(Q, (distance[u][1], u, bike))

        else:
            for u, d in G_copy[v][0]:
                if distance[u][0] > distance[v][0] + d:
                    distance[u][0] = distance[v][0] + d
                    heappush(Q, (distance[u][0], u, None))

                if G_copy[v][1] != None:
                    if distance[u][1] > distance[v][0] + d * G_copy[v][1]:
                        distance[u][1] = distance[v][0] + d * G_copy[v][1]
                        heappush(Q, (distance[u][1], u, v))

    return int(min(distance[t]))


# zmien all_tests na True zeby uruchomic wszystkie testy
if __name__ == "__main__":
    from egz1atesty import runtests

    runtests(armstrong, all_tests=True)
