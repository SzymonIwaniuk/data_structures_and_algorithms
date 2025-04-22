# 3 Graf nieskierowany G, gdzie kazda krawedz ma inna wage ze zbioru (1,...). Czy istnieje sciezka s -> t po krawedziach o malejacych wagach?


def path(G: list[list[int]], s: int, t: int) -> bool:
    n = len(G)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        for v in G[u][1:]:
            if not visited[v] and G[u][0] > G[v][0]:
                dfs(v)

    dfs(s)
    return visited[t]


if __name__ == "__main__":
    G1 = [[7, 1], [6, 0, 2, 3], [4, 1, 3, 4], [10, 1, 2, 4], [1, 2, 3]]
    G2 = [[7, 1], [6, 0, 2, 3], [4, 1, 3, 4], [10, 1, 2, 4], [10, 2, 3]]

    print(path(G1, 0, 4))
    print(path(G1, 4, 0))
    print(path(G1, 1, 4))
    print(path(G2, 1, 4))
