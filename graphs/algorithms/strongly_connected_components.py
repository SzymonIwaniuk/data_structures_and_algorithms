def reverse_edges(G: list[list[int]]) -> list[list[int]]:
    n = len(G)
    reversed_edges = [[] for _ in range(n)]

    for v in range(n):
        for u in G[v]:
            reversed_edges[u].append(v)

    return reversed_edges


def strongly_connected_compontens(G: list[list[int]]) -> list[list[int]]:

    n = len(G)
    order = []
    visited = [False for _ in range(n)]

    # step 1: Wykonaj DFS zapisujac czas przetworzenia
    def dfs1(G: list[list[int]], v: int) -> None:
        for u in G[v]:
            if visited[u] == False:
                visited[u] = True
                dfs1(G, u)
        order.append(v)

    for v in range(n):
        if visited[v] == False:
            dfs1(G, v)

    # step 2: Odwroc kierunek wszystkich krawedzi
    reversed_g = reverse_edges(G)

    # step 3: Wykonaj DFS uruchamiajac dfs_visit w glownej petli w kolejnosci malejacych czasow przetworzenia
    connected_commponents = []
    visited = [False for _ in range(n)]

    def dfs2(reversed_g: list[list[int]], v: int, commponent: list[int]) -> None:
        visited[v] = True
        commponent.append(v)
        for u in reversed_g[v]:
            if visited[u] == False:
                dfs2(reversed_g, u, commponent)

    for v in order[::-1]:
        if visited[v] == False:
            commponent = []
            dfs2(reversed_g, v, commponent)
            connected_commponents.append(commponent)

    return connected_commponents


if __name__ == "__main__":
    G = [[1], [2], [0, 3], [4], [5], [3, 6], [7], [8], [6]]
    print(strongly_connected_compontens(G))
