from math import floor, inf
from queue import PriorityQueue

from egz1atesty import runtests


def edges_to_list(E):
    n = max(max(u, v) for u, v, _ in E)

    G = [[] for _ in range(n + 1)]

    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))

    return G


def dijkstra(G, s, t):
    n = len(G)
    d = [inf] * n

    PQ = PriorityQueue()
    PQ.put((0, s))
    d[s] = 0

    while PQ.not_empty:
        u_w, u = PQ.get()

        if u == t:
            break
        if u_w > d[u]:
            continue

        for v, w in G[u]:
            c = d[u] + w
            if d[v] > c:
                d[v] = c
                PQ.put((c, v))

    return d


def armstrong(B, G, s, t):
    A = edges_to_list(G)
    n = len(A)
    bikes = [1] * n  # 1 w przypadku braku roweru lub chodu pieszo

    for i, p, q in B:
        count = p / q
        if bikes[i] > count:
            bikes[i] = count

    d1 = dijkstra(A, s, t)  # od s do t
    min_cost = d1[t]  # w przypadku gdyby nie wsiadla na rower
    d2 = dijkstra(A, t, s)  # od t do s

    for i in range(n):
        cost = d1[i] + d2[i] * bikes[i]
        if cost < min_cost:
            min_cost = cost

    return floor(min_cost) if min_cost != inf else inf


if __name__ == "__main__":
    # zmien all_tests na True zeby uruchomic wszystkie testy
    runtests(armstrong, all_tests=True)
