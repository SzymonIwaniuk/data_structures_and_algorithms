def DFS(G, s):
    visited = [False] * len(G)
    parent = [None] * len(G)

    def dfs_visit(G, u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G, v)

    dfs_visit(G, s)

    if False in visited:
        return False

    return visited, parent


if __name__ == "__main__":
    G = [[1], [2], [3, 4], [2, 4, 5], [2, 3], [3]]
    print(DFS(G, 0))
