from egz1atesty import runtests
from heapq import heappush, heappop, heapify


def build_graph(G, n):
    graph = [[] for i in range(n)]

    for u, v, d in G:
        graph[u].append((v, d))
        graph[v].append((u, d))

    return graph


def best_bike(B, n):
    bikes = [1 for _ in range(n)]

    for i, p, q in B:
        efficiency = p / q
        bikes[i] = min(bikes[i], efficiency)

    return bikes


def dijkstra(graph, s, n):
    distance = [float("inf")] * n
    distance[s] = 0
    queue = [(0, s)]

    while queue:
        time, u = heappop(queue)

        for v, d in graph[u]:
            if time + d <= distance[v]:
                distance[v] = time + d
                heappush(queue, (time + d, v))

    return distance


def armstrong(B, G, s, t):
    n = max(max(u, v) for u, v, d in G) + 1
    graph = build_graph(G, n)
    bikes = best_bike(B, n)
    from_s = dijkstra(graph, s, n)
    from_t = dijkstra(graph, t, n)
    result = float("inf")

    for i in range(n):
        result = min(result, from_s[i] + from_t[i] * bikes[i])

    return int(result)


runtests(armstrong, all_tests=True)
