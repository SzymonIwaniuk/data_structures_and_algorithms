from egz1Btesty import runtests
from collections import deque


def build_graph(E, V):
    graph = [[] for i in range(V)]

    for u, v in E:
        graph[u].append(v)

    return graph


def critical(V, E):
    graph = build_graph(E, V)
    counts = [[0]*V for i in range(V)]
    edges = [[False]*V for i in range(V)]

    for u, v in E:
        edges[u][v] = True

    def dfs(start, u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(start, v)
            counts[start][v] += 1

    for u in range(V):
        visited = [False] * V
        dfs(u, u)

    critical = 0

    for i in range(V):
        for j in range(V):
            if counts[i][j] == 1 and edges[i][j]:
                critical += 1

    return critical






    # return bridges(graph, V)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests=True)
