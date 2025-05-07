def dfs_euler(G: list[list[int]]) -> list[int]:
    n = len(G)
    U = [0 for _ in range(n)]
    cycle = []

    def dfs_visit(G: list[list[int]], v: int) -> any:
        while U[v] < n:
            u = U[v]
            U[v] += 1
            if G[v][u] == 1:
                G[v][u] = G[u][v] = 0
                dfs_visit(G, u)
        cycle.append(v)

    dfs_visit(G, 0)

    return cycle


if __name__ == "__main__":
    G1 = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
    ]
    print(dfs_euler(G1))
