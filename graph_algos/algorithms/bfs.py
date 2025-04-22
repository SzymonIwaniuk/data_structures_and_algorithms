from queue import Queue


def BFS(G, s):
    visited = [False] * len(G)
    parent = [None] * len(G)
    Q = Queue()
    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                Q.put(v)

    return visited, parent


G = [[1], [2], [3, 4], [2, 4, 5], [2, 3], [3]]

print(BFS(G, 0))
