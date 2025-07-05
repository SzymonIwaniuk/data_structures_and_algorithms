from collections import deque
from heapq import heappop, heappush


def convert_to_list(G, n):
    new_list = [[] for _ in range(n)]

    for v in range(n - 1):
        for u in range(v + 1, n):
            d = G[v][u]
            if d:
                new_list[v].append((u, d))
                new_list[u].append((v, d))

    return new_list


def double_jumps(G, n):
    jumps = [[] for _ in range(n)]

    for s in range(n):
        Q = deque()
        d = [float("inf")] * n

        for v, w in G[s]:
            Q.append((v, w))

        while len(Q) > 0:
            u, prev_w = Q.popleft()

            for v, w in G[u]:
                jump_w = w if w > prev_w else prev_w
                if d[v] > jump_w:
                    d[v] = jump_w

        for v in range(n):
            if d[v] != float("inf"):
                jumps[s].append((v, d[v]))

    return jumps


def jumper(G, s, w):
    n = len(G)
    G = convert_to_list(G, n)
    jumps = double_jumps(G, n)
    d1 = [float("inf") for _ in range(n)]

    PQ = [(0, s)]
    d1[s] = 0
    d2 = d1[:]

    while len(PQ) > 0:
        u_w, u = heappop(PQ)

        if u == w:
            break
        if u_w > d1[u] and u_w > d2[u]:
            continue

        for v, c in G[u]:
            tmp_d = (d1[u] if d1[u] < d2[u] else d2[u]) + c
            if d1[v] > tmp_d:
                d1[v] = tmp_d
                heappush(PQ, (tmp_d, v))

        for v, c in jumps[u]:
            tmp_d = d1[u] + c
            if d2[v] > tmp_d:
                d2[v] = tmp_d
                heappush(PQ, (tmp_d, v))

    return d1[w] if d1[w] < d2[w] else d2[w]


if __name__ == "__main__":
    G1 = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 7, 0],
        [0, 0, 7, 0, 8],
        [0, 0, 0, 8, 0],
    ]

    G2 = [
        [0, 2, 0, 5, 0, 0],
        [2, 0, 4, 0, 0, 0],
        [0, 4, 0, 1, 6, 0],
        [5, 0, 1, 0, 3, 0],
        [0, 0, 6, 3, 0, 7],
        [0, 0, 0, 0, 7, 0],
    ]

    G3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    G4 = [
        [0, 4, 0, 0, 0],
        [4, 0, 1, 2, 0],
        [0, 1, 0, 0, 3],
        [0, 2, 0, 0, 5],
        [0, 0, 3, 5, 0],
    ]

    G5 = [
        [0, 2, 0, 0, 0, 10],
        [2, 0, 3, 0, 0, 0],
        [0, 3, 0, 1, 0, 0],
        [0, 0, 1, 0, 4, 0],
        [0, 0, 0, 4, 0, 6],
        [10, 0, 0, 0, 6, 0],
    ]

    G6 = [
        [0, 1, 2, 0, 0, 0, 0],
        [1, 0, 0, 3, 0, 0, 0],
        [2, 0, 0, 4, 5, 0, 0],
        [0, 3, 4, 0, 0, 6, 0],
        [0, 0, 5, 0, 0, 1, 2],
        [0, 0, 0, 6, 1, 0, 1],
        [0, 0, 0, 0, 2, 1, 0],
    ]

    print(jumper(G1, 0, 4))
    print(jumper(G2, 0, 5))
    print(jumper(G3, 0, 3))
    print(jumper(G4, 0, 4))
    print(jumper(G5, 0, 4))
    print(jumper(G6, 0, 6))
