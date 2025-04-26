import heapq


def min_dijkstra(G: list[list[list[int, float]]], s: int, t: int) -> (float, list[int]):
    n = len(G)
    visited = [-1] * n
    parent = [None] * n
    distance = [float("inf")] * n
    Q = [[float("inf"), s]]

    while Q:
        d, v = heapq._heappop_max(Q)
        if visited[v] == 1:
            continue
        visited[v] = 1

        for [u, w] in G[v]:
            if visited[u] == -1:
                distance[u] = min(w, distance[v])
                visited[u] = 0
                parent[u] = v

            else:
                if w > distance[u]:
                    parent[u] = v
                    distance[u] = w

            Q.append([w, u])

    path = []
    run = t
    while run != s:
        path.append(run)
        run = parent[run]
    path.append(s)
    return distance[t], path[::-1]


if __name__ == "__main__":
    G1 = [
        [[1, 5], [2, 4]],
        [[0, 5], [2, 2]],
        [[0, 4], [1, 2]],
    ]

    G2 = [
        [[1, 10], [4, 5]],
        [[0, 10], [2, 8], [3, 4]],
        [[2, 8], [3, 7]],
        [[1, 4], [2, 7], [4, 6]],
        [[0, 5], [4, 6]],
    ]
    print(min_dijkstra(G1, 0, 1))
    print(min_dijkstra(G2, 0, 3))
