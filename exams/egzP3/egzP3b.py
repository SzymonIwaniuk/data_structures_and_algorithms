from egzP3btesty import runtests


def convert_to_edges(G, n):
    E = []
    suma = 0

    for v in range(n):
        for u, d in G[v]:
            if v < u:
                E.append((v, u, d))
                suma += d

    return E, suma


# Lekko zmodyfikowany kruskal z budowaniem Maximal Spanning Tree i warnukiem na jedno redundatne polaczenie
def lufthansa(G):
    n = len(G)
    p = [i for i in range(n)]
    r = [0] * n
    mst = []

    E, suma = convert_to_edges(G, n)
    E.sort(key=lambda x: -x[2])

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])

        return p[x]

    def union(x, y):
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

    maxi = 0
    for u, v, d in E:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, d))
            suma -= d
            if len(mst) == n:
                break

        # Warunek na 1 redundatne polaczenie
        else:
            maxi = max(d, maxi)

    return suma - maxi


runtests(lufthansa, all_tests=True)
