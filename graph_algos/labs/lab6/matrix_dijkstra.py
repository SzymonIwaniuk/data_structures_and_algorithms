# 1 Algorytm dijkstry reprezentacja macierzowa


def dijkstra(G: list[list[int]], s: int) -> list[int]:
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    distance = [float("inf")] * n
    distance[s] = 0

    for i in range(n):
        mini = float("inf")
        v = None
        for j in range(n):
            if distance[j] < mini and not visited[j]:
                mini = distance[j]
                v = j

        if v == None:
            break

        visited[v] = True

        for u in range(n):
            if G[v][u] > 0:
                relax(v, u, G, distance, parent)

    return distance, parent


def relax(
    u: int, v: int, G: list[list[int]], distance: list[float], parent: list[int]
) -> None:
    if distance[v] > distance[u] + G[v][u]:
        distance[v] = distance[u] + G[v][u]
        parent[v] = u


# 2 Odtwarzanie / wypisywanie najkrotszej sciezki na podstawie listy parentow


def path_s_to_t(s: int, t: int, parent: list[int]) -> list[int]:
    path = []
    while t != None:
        path.append(t)
        t = parent[t]
    return path[::-1]


if __name__ == "__main__":

    G1 = [[0, 3, 0, 4], [3, 0, 1, 0], [0, 1, 0, 2], [4, 0, 2, 0]]
    weights, parents = dijkstra(G1, 0)
    print(weights)
    print(path_s_to_t(0, 3, parents))
