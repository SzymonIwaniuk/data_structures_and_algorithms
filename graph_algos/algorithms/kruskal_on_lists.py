from typing import List, Tuple


def convert_to_edges(
    G: List[List[Tuple[int, int]]], n: int
) -> List[Tuple[int, int, int]]:
    E = []
    for v in range(n):
        for u, d in G[v]:
            if v < u:
                E.append((v, u, d))

    return E


def kruskal(G: List[List[Tuple[int, int]]]) -> List[Tuple[int, int, int]]:
    n = len(G)
    p = [i for i in range(n)]
    r = [0] * n
    mst = []

    E = convert_to_edges(G, n)
    E.sort(key=lambda x: x[2])

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])

        return p[x]

    def union(x: int, y: int) -> None:
        x = find(x)
        y = find(y)

        if x == y:
            return
        if r[x] > r[y]:
            p[y] = x
        else:
            p[x] = y
            if r[x] == r[y]:
                r[y] += 1

    for u, v, w in E:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
            if len(mst) == n - 1:
                break

    return mst
