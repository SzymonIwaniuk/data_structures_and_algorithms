# Task: Please propose an algorithm that finds the shortest paths in the DAG.

from typing import Tuple


def topological_sort(G: list[list[Tuple[int, float]]]) -> list[int]:
    n = len(G)
    visited = [False] * n
    sorted_vertexes = []

    for v in range(n):
        if not visited[v]:
            stack = [(v, False)]

            while len(stack) > 0:
                u, status = stack.pop()
                if status:
                    sorted_vertexes.append(u)
                else:
                    if not visited[u]:
                        visited[u] = True
                        stack.append((u, True))
                        for i in range(len(G[u]) - 1, -1, -1):
                            w = G[u][i][0]
                            if not visited[w]:
                                stack.append((w, False))

    return sorted_vertexes[::-1]


def shortest_paths_in_dag(
    G: list[list[Tuple[int, float]]], sorted_vertexes: list[int], s: int
) -> list[float]:
    n = len(G)
    distance = [float("inf")] * n
    distance[s] = 0

    for v in sorted_vertexes:
        for i in G[v]:
            u, d = i
            if distance[u] > distance[v] + d:
                distance[u] = distance[v] + d

    return distance


if __name__ == "__main__":
    G = [[(1, 5), (2, 3)], [(3, 2), (4, 6)], [(4, 4)], [], [(5, 1)], []]

    sorted_graph = topological_sort(G)
    print(sorted_graph)
    print(shortest_paths_in_dag(G, sorted_graph, 0))
