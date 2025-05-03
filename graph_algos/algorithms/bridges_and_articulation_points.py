from typing import Tuple


def bridges(G: list[list[int]]) -> (list[Tuple[int, int]], list[int]):
    n = len(G)
    time = 0

    parents = [None] * n
    d = [float("inf")] * n
    low = [float("inf")] * n
    bridges = []
    aps_tmp = [False] * n

    def DFSVisit(G, u):
        nonlocal time

        children = 0

        d[u] = time
        low[u] = time

        time += 1

        for v in G[u]:
            if d[v] == float("inf"):
                parents[v] = u
                children += 1
                low[u] = min(low[u], DFSVisit(G, v))

                if parents[u] is None and children > 1:
                    aps_tmp[u] = True

                elif parents[u] is not None and low[v] >= d[u]:
                    aps_tmp[u] = True

            elif v != parents[u]:
                low[u] = min(low[u], d[v])

        if low[u] == d[u] and parents[u] != None:
            bridges.append((u, parents[u]))

        return low[u]

    for u in range(n):
        if d[u] == float("inf"):
            DFSVisit(G, u)

    aps = []
    for i in range(n):
        if aps_tmp[i]:
            aps.append(i)

    return bridges, aps


if __name__ == "__main__":
    G = [
        [3, 9],
        [2, 3],
        [1, 3, 4],
        [0, 1, 2],
        [2, 5, 6, 8],
        [4, 6],
        [4, 5, 7],
        [6, 8],
        [4, 7],
        [0],
    ]

    print(bridges(G))
