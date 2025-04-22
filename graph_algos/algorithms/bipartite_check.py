from collections import deque


def bipartite(G):
    n = len(G)
    colors = [-1 for _ in range(n)]
    Q = deque()
    Q.append(0)
    colors[0] = 0

    while len(Q) > 0:
        u = Q.popleft()

        for v in G[u]:
            if colors[v] == -1:
                colors[v] = (colors[u] + 1) % 2
                Q.append(v)
            elif colors[v] == color[u]:
                return False

    return True
