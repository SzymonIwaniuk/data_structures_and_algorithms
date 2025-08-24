from egz1Btesty import runtests
from typing import List, Tuple


def find_critical(graph, start, global_critical):
    n = len(graph)

    visited = [False] * n
    edges = [[] for _ in range(n)]

    def visit(u):
        visited[u] = True

        for v in graph[u]:
            edges[v].append((u, v)) # To zabija szybkość programu, bo chyba w tych ostatnich testach jest ogromna ilość wchodzących krawędzi do wierzchołków

            if not visited[v]:
                visit(v)

    visit(start)

    for found_edges in edges:
        if len(found_edges) == 1:
            global_critical[found_edges[0]] = True


def critical(V, E):
    graph = [[] for _ in range(V)]

    for u, v in E:
        graph[u].append(v)

    global_critical = {}

    # O(V)
    for s in range(V):
        if len(graph[s]) == 0:
            continue

        # O(V + E)
        find_critical(graph, s, global_critical)

    return len(global_critical)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests=True)
