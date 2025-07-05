from collections import deque
from math import inf

from egz3atesty import runtests


def build_graph(G, n):
    graph = [[] for i in range(n)]

    for u in range(n):
        for v in range(u, n):
            if G[u][v] != -1:
                graph[u].append((v, G[u][v]))
                graph[v].append((u, G[u][v]))

    return graph


def goodknight(G, s, t):
    n = len(G)
    graph = build_graph(G, n)
    queue = deque()
    queue.append((0, 0, s))
    times = [[inf] * 17 for _ in range(n)]
    times[s][0] = 0

    while queue:
        time, exhaust, castle = queue.popleft()
        # print(time)

        for (
            new_castle,
            dist,
        ) in graph[castle]:
            new_exhuast = exhaust + dist
            if new_exhuast > 16:
                new_time = time + 8 + dist
                if times[new_castle][dist] > new_time:
                    times[new_castle][dist] = new_time
                    queue.append((new_time, dist, new_castle))

            else:
                new_time = time + dist
                if times[new_castle][new_exhuast] > new_time:
                    times[new_castle][new_exhuast] = new_time
                    queue.appendleft((new_time, new_exhuast, new_castle))

    return min(times[t])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(goodknight, all_tests=True)
