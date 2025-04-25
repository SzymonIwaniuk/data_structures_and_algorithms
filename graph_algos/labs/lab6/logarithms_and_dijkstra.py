# The length of a path is the product of its weights.
# Task: Propose the fastest/best algorithm to find the shortest paths.
# 1 step: converting weights to logarithms
# 2 step: using the product of logarithms and dijkstra


from math import log, exp
import heapq


def conv_to_logs(
    G: list[list[list[int, float]]], n: int
) -> list[list[list[int, float]]]:
    for i in range(n):
        v = G[i]
        for j in range(len(v)):
            u, w = v[j]
            G[i][j][1] = log(w)

    return G


def conv_to_floats(distance: list[float], n: int) -> list[float]:
    for i in range(n):
        v = distance[i]
        distance[i] = exp(v)

    return distance


def djikstra_multiplicative(G: list[list[list[int, float]]], s: int) -> list[float]:
    n = len(G)
    G = conv_to_logs(G, n)
    parent = [None] * n
    distance = [float("inf")] * n
    distance[s] = 0
    visited = [False] * n
    Q = [(0, s)]
    i = 0

    while len(Q) > 0 and i < n:
        u = heapq.heappop(Q)[1]
        if visited[u]:
            continue
        visited[u] = True
        i += 1

        for v, w in G[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                parent[v] = u
                heapq.heappush(Q, (distance[v], v))

    return conv_to_floats(distance, n)


if __name__ == "__main__":

    G1 = [[[1, 3], [3, 4]], [[0, 3], [2, 1]], [[1, 1], [3, 2]], [[2, 2], [0, 4]]]
    print(djikstra_multiplicative(G1, 0))

    G2 = [
        [[1, 2.5], [2, 3.1]],
        [[0, 2.5], [3, 1.8], [4, 2.2]],
        [[0, 3.1], [4, 1.5]],
        [[1, 1.8], [5, 2.0]],
        [[1, 2.2], [2, 1.5], [5, 3.3]],
        [[3, 2.0], [4, 3.3]],
    ]
    print(djikstra_multiplicative(G2, 0))
