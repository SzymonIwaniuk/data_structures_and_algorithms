# 1. Transport atomowy
# Dwoch technikow A i B niesie ladunek atomowy.
# Nie moga zblizyc sie na okreslona odleglosc d, jeden idzie z s->t, drugi z t->s
# W jednym kroku rusza sie jeden albo obaj tzn. albo A wedruje z s->t albo B wedruje z t->s albo razem
# Czy technicy moga dotrzec do celu nie zblizajac sie na odleglosc d
# Graf nieskierowany, wazony reprezentacja macierzowa
# O(V^4) zlozonosc akceptowalna
# O(V^3) zlozonosc wzorcowa

# Floyd-warshall dzieki czemu mamy odleglosci miedzy kazdym wierzcholkiem
# pary pozycji technika a i b ktory ma wieksze odleglosci dla kazdej pary sprawdzamy czy je mozna polaczyc
# Nastepnie bfs sprawdzamy czy jest sciezka z s do t

from collections import deque


def transport_atomowy(G: list[list[float]], d: float, s: int, t: int) -> bool:
    n = len(G)
    S = G.copy()

    for k in range(n):
        for v in range(n):
            for u in range(n):
                S[v][u] = min(S[v][u], S[v][k] + S[k][u])

    Q = deque()
    Q.append((s, t))
    visited = [[False for _ in range(n)] for _ in range(n)]

    while Q:
        v, u = Q.popleft()

        if (v, u) == (t, s):
            return True

        visited[v][u] = True

        for i in range(n):
            if not visited[i][u] and S[i][u] > d and S[u][i] > d:
                Q.append((i, u))
            if not visited[v][i] and S[v][i] > d and S[i][v] > d:
                Q.append((v, i))

    return False


# O(V^3)

if __name__ == "__main__":

    inf = float("inf")
    G = [[0, 2, inf, 1], [2, 0, 3, inf], [inf, 3, 0, 4], [1, inf, 4, 0]]

    print(transport_atomowy(G=G, d=2, s=0, t=2))
    print(transport_atomowy(G=G, d=3, s=0, t=2))
