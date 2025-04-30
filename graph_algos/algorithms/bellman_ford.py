def bellman_ford(G: list[list[list[int, float]]], s: int) -> list[float]:
    n = len(G)
    distance = [float('inf')] * n
    parent = [None] * n
    distance[s] = 0

    # for i in range(|V| - 1)
    for i in range(n - 1):
        # (u, v) ∈ E
        for v in range(n):
            for u, d in G[v]:
                print(v, u, d)
                relax(u, v, d, distance, parent)

    # Verifaction of negative cycles
    for v in range(n):
        for u, d in G[v]:
            if distance[u] > distance[v] + d:
                return -1

    return distance

def relax(u, v, d, distance, parent):
    if distance[u] > distance[v] + d:
        distance[u] = distance[v] + d
        parent[u] = v

if __name__ == '__main__':
    G = [
    [(1, 2), (2, 4)],
    [(2, 1), (3, 7)],
    [(4, 3)],
    [(4, 1)],
    []
    ]

    G_negative_cycle = [
    [(1, 5)],
    [(2, -3)],
    [(3, 2)],
    [(1, -4)],
    ]

    print(bellman_ford(G,0))
    print(bellman_ford(G_negative_cycle,0))
