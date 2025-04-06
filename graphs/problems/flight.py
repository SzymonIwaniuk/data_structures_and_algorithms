def flight(L, x, y, t):
    l = len(L)
    vertexs = L[l - 1][1]
    G = [[] for i in range(L[0][0], L[l - 1][1] + 1)]

    # zbudowanie grafu O(E), bo L to lista krawedzi
    for v in L:
        k, l, m = v
        G[k].append([l, m])
        G[l].append([k, m])

    n = len(G)
    visited = [False] * n
    visited[x] = True

    # dfs w reprezentacji listowej O(V + E)
    def dfs(G, v, minh, maxh, visited, i):
        if i >= n + 1:
            return False

        lenght = len(G[v])

        for j in range(lenght):
            u, height = G[v][j]
            n_minh = min(minh, height)
            n_maxh = max(maxh, height)

            if u == y:
                mean = (n_maxh + n_minh) / 2
                if mean - t <= n_minh and mean + t >= n_maxh:
                    return True
                else:
                    return False

            if visited[u] == False:
                visited[u] = True
                if dfs(G, u, n_minh, n_maxh, visited, i + 1):
                    return True
                visited[u] = False

    if dfs(G, x, float("inf"), -float("inf"), visited, 0):
        return True
    else:
        return False

    # Calosc O(V + E)


if __name__ == "__main__":

    L = [
        (0, 1, 2000),
        (0, 2, 2100),
        (1, 3, 2050),
        (2, 3, 2300),
        (2, 5, 2300),
        (3, 4, 2400),
        (3, 5, 1990),
        (4, 6, 2500),
        (5, 6, 2100),
    ]

    print(flight(L, 5, 2, 60))
