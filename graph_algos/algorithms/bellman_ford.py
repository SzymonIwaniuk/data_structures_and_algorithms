def bellman_ford(vertices, edge_list, source):
    dist = [float('inf')] * vertices
    dist[source] = 0
    for _ in range(vertices - 1):
        for u, v, weight in edge_list:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    for u, v, weight in edge_list:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            return None
    return dist

if __name__ == "__main__":
    vertices = 5
    edge_list = [
        (0, 1, 6),
        (0, 2, 7),
        (1, 2, 8),
        (1, 3, -4),
        (1, 4, 5),
        (2, 3, 9),
        (2, 4, -3),
        (3, 1, 7),
        (4, 0, 2),
        (4, 3, 7)
    ]
    source = 0
    distances = bellman_ford(vertices, edge_list, source)
