from collections import deque

"""
Prosze zaimplementowac testowanie czy graf jest dwudzielny uzywajac BFS dla
reprezentacji listowej.
"""
# Dziala w przypadku kiedy graf jest spojny, dla grafu niespojnego trzeba
# przejsc po nieodwiedzonych wierzcholkach


def is_bipartite(G):
    n = len(G)
    Q = deque()
    visited = [False for _ in range(n)]
    colors = [0 for _ in range(n)]
    visited[0] = True
    Q.append(0)

    while Q:
        u = Q.popleft()

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                colors[v] = 1 - colors[u]
                Q.append(v)

            elif visited[v] and colors[v] == colors[u]:
                return False

    return True


G = [[2, 3, 4], [3, 4], [0], [0, 1], [0, 1]]


print(is_bipartite(G))
