from jumpertesty import runtests
from heapq import heappush, heappop

def build_basic_graph(G, n):
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                graph[i].append((j, G[i][j]))

    return graph


def build_twomiles_graph(graph, n):
    twomiles_graph = [set() for _ in range(n)]

    for u in range(n):
        for v, d1 in graph[u]:
            for w, d2 in graph[v]:
                if w != u:
                    twomiles_graph[u].add((w, max(d1, d2)))
                    twomiles_graph[w].add((u, max(d1, d2)))

    twomiles_graph = [list(node) for node in twomiles_graph]
    return twomiles_graph


def jumper(G, s, w):
    n = len(G)
    normal_graph = build_basic_graph(G, n)
    twomiles_graph = build_twomiles_graph(normal_graph, n)

    distance = [[float('inf')] * 2 for _ in range(n)]
    distance[s][0] = 0
    distance[s][1] = 0
    queue = [(0, s, 0)]

    while queue:
        time, v, last = heappop(queue)

        if last == 0:
            for u, d in twomiles_graph[v]:
                if time + d < distance[u][1]:
                    distance[u][1] = time + d
                    heappush(queue, (time + d, u, 1))

        for u, d in normal_graph[v]:
            if time + d < distance[u][0]:
                distance[u][0] = time + d
                heappush(queue, (time + d, u, 0))

    # print(distance)
    return min(distance[w])

runtests(jumper)