from egz2btesty import runtests
from collections import deque

inf = float("inf")


def build_adjacency_list(edges, a):
    # O(m)
    graph = [[] for _ in range(a + 1)]
    # O(m)
    for x, y, d, typ in edges:
        graph[x].append((y, d, typ))
        graph[y].append((x, d, typ))

    return graph


def tory_amos(E, A, B):
    a = max(max(x, y) for x, y, d, typ in E)
    graph = build_adjacency_list(E, a)
    queue = deque()
    times = [[inf] * 2 for _ in range(a + 1)]
    times[A][0] = 0
    times[A][1] = 0

    types = {"P": 0, "I": 1}

    for station, d, t in graph[A]:
        n = types[t]
        if times[station][n] > d:
            times[station][n] = d
            queue.append((d, station, n, d))  # delay, stacja, rozstaw kol, czas

    while queue:
        p, station, t, time = queue.popleft()

        if times[station][t] < time:
            continue

        if p:
            queue.append((p - 1, station, t, time))
            continue

        for new_station, d, new_t in graph[station]:
            n = types[new_t]
            # print(n)
            if n == t:
                delay = 10 + d if n == 0 else 5 + d
            else:
                delay = 20 + d

            new_time = times[station][t] + delay

            if times[new_station][n] > new_time:
                times[new_station][n] = new_time
                queue.append((delay, new_station, n, new_time))

    # print(times)
    return min(times[B])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(tory_amos, all_tests=True)
