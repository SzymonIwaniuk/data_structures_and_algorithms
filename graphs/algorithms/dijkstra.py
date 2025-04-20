from queue import PriorityQueue


def djikstra(G: list[list[list[int, float]]], s: int) -> list[float]:
    n = len(G)
    parent = [None] * n
    distance = [float("inf")] * n
    distance[s] = 0
    Q = PriorityQueue()
    Q.put([0, s])

    while Q.qsize() > 0:
        u = Q.get()[1]

        for v, w in G[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                parent[v] = u
                Q.put([distance[v], v])
    return distance


if __name__ == "__main__":

    G1 = [[[1, 3], [3, 4]], [[0, 3], [2, 1]], [[1, 1], [3, 2]], [[2, 2], [0, 4]]]
    print(djikstra(G1, 0))
