from collections import deque

# 5 Czy mozna rozdzielic zadany graf na dwie kliki (grafy pelne)


# Rozwiazanie: Wystarczy sprawdzic czy dopelnienie grafu jest grafem dwudzielnym
def cliques(G):
    n = len(G)
    complement = [[] for v in range(n)]

    # Sasiedzi wierzcholka musza byc posortowani rosnaca np coutingsortem
    for v in range(n):
        neighbours = G[v]
        l = len(neighbours)
        i = 0
        for u in range(n):
            if u == v:
                continue
            if i < l and neighbours[i] == u:
                i += 1
            else:
                complement[v].append(u)

    return is_bipartite(complement)


def is_bipartite(G: list[list[int]]) -> bool:
    n = len(G)
    q = deque()

    # -1 not visited, 0 - color one, 1 - color two
    visited = [-1] * n

    for i in range(n):
        if visited[i] == -1:
            q.append(i)
            visited[i] = 0

            while q:
                v = q.pop()

                for u in G[v]:
                    if visited[u] == -1:
                        visited[u] = 1 - visited[v]
                        q.append(u)
                    elif visited[v] == visited[u]:
                        return False
    return True


if __name__ == "__main__":

    G1 = [[1, 3], [0, 2], [1, 3], [0, 2]]
    G2 = [[1, 2], [0, 2, 3], [0, 1, 4], [4, 5, 1], [3, 5, 2], [3, 4]]
    G3 = [[2, 3, 4], [3, 4], [3, 4], [0, 1, 2, 4], [0, 1, 2, 3]]

    print(cliques(G1))
    print(cliques(G2))
    print(cliques(G3))
