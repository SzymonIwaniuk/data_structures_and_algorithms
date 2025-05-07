# Dziala dla grafu skierowanego w reprezentacji listowej!


def euler_cycle(G: list[list[int]]) -> list[int]:
    cycle = []
    n = len(G)

    # Tablica do spamietywania na ktorym aktualnie wierzcholku sie zatrzymalismy
    global where
    where = [0 for _ in range(n)]

    # O(nlogn)
    for i in range(n):
        G[i].sort()

    def dfs_visit(G: list[list[int]], v: int) -> any:
        while where[v] < len(G[v]):
            u = G[v][where[v]]
            where[v] += 1
            dfs_visit(G, u)
        else:
            cycle.append(v)

    dfs_visit(G, 0)

    return cycle


# Calosc: O(nlogn)

if __name__ == "__main__":

    G1 = [[1, 2], [0, 2], [1, 0]]
    G2 = [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]]
    G3 = [[3, 4], [3, 4], [3, 4], [2, 4], [2, 3]]
    print(euler_cycle(G3))
