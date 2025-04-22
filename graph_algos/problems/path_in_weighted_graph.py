"""
Czy w ważonym G istnieje ścieżka s -> t po krawędziach o malejących wagach.
"""


def path(G: list[list[int]], s: int, t: int):

    visited = [False for _ in range(len(G))]

    def dfs(G, s):
        lenght = len(G[s])
        for j in range(1, lenght):
            u = G[s][j]
            if visited[u] == False and G[s][0] > G[u][0]:
                if u == t:
                    return True

                else:
                    visited[u] = True
                    if dfs(G, u):
                        return True
                    visited[u] = False

    if dfs(G, s):
        return True
    else:
        return False


if __name__ == "__main__":

    # keep weight on index 0 in each vertex
    G1 = [[7, 1], [6, 0, 2, 3], [4, 1, 3, 4], [10, 1, 2, 4], [1, 2, 3]]
    G2 = [[7, 1], [6, 0, 2, 3], [4, 1, 3, 4], [10, 1, 2, 4], [10, 2, 3]]
    print(path(G1, 0, 4))
    print(path(G1, 4, 0))
    print(path(G1, 1, 4))
    print(path(G2, 1, 4))
