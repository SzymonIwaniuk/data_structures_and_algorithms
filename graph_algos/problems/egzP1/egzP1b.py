from egzP1btesty import runtests
from collections import deque


def convert_to_list(G):
    u, maxi, p = G[-1]
    G_copy = [[] for i in range(maxi + 1)]

    for u, v, d in G:
        G_copy[u].append((v, d))
        G_copy[v].append((u, d))

    return G_copy


def turysta(G, D, L):
    G_copy = convert_to_list(G)
    n = len(G_copy)

    distance = [[float("inf")] * 5 for _ in range(n)]
    distance[D][0] = 0

    Q = deque()
    Q.append((0, D))

    while Q:
        amount, v = Q.popleft()
        if amount + 1 > 4:
            continue

        for u, d in G_copy[v]:
            if distance[u][amount + 1] > distance[v][amount] + d:
                distance[u][amount + 1] = distance[v][amount] + d
                Q.append((amount + 1, u))

    return distance[L][4]

if __name__ == '__main__':
    runtests(turysta)
