from egzP5btesty import runtests
from typing import Tuple


def convert_to_list(B):
    l = len(B)
    B_copy = []

    for v, u in B:
        if v > u:
            B_copy.append((v, u))
        else:
            B_copy.append((u, v))

    B_copy.sort(key=lambda edge: (edge[0], edge[1]), reverse=True)
    maxi = B_copy[0][0]

    G = [[] for _ in range(maxi + 1)]

    prev = (None, None)

    for v, u in B_copy:
        if (v, u) != prev:
            G[v].append(u)
            G[u].append(v)
        prev = (v, u)

    return G


def koleje(B):
    G = convert_to_list(B)
    n = len(G)

    time = 0
    parents = [None] * n
    d = [float("inf")] * n
    low = [float("inf")] * n
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

        return low[u]

    for u in range(n):
        if d[u] == float("inf"):
            DFSVisit(G, u)

    stations = 0
    for i in range(n):
        if aps_tmp[i]:
            stations += 1

    return stations


runtests(koleje, all_tests=True)
