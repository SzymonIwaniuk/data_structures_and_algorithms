def euler_cycle(G: list[list[int]]) -> list[int]:
    cycle = []
    n = len(G)

    def dfs_visit(G: list[list[int]], v: int) -> any:
        for u in G[v]:
            G[v].remove(u)
            G[u].remove(v)
            dfs_visit(G, u)
        if G[v] == []:
            cycle.append(v)

    dfs_visit(G, 0)

    return cycle


if __name__ == "__main__":

    G1 = [[1, 2], [0, 2], [1, 0]]
    G2 = [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]]
    print(euler_cycle(G2))
