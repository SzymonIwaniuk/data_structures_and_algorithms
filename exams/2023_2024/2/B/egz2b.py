from collections import deque

from egz2btesty import runtests

inf = float("inf")


# 0 - 1 BFS
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
            queue.appendleft((station, d, n))  # stacja, czas, rozstaw kol

    while queue:
        station, time, t = queue.popleft()

        for new_station, d, new_t in graph[station]:
            n = types[new_t]

            if n == t:
                delay = 10 + d if n == 0 else 5 + d
            else:
                delay = 20 + d

            new_time = time + delay

            if times[new_station][n] > new_time:
                times[new_station][n] = new_time
                if delay <= 10:
                    queue.appendleft((new_station, new_time, n))
                else:
                    queue.append((new_station, new_time, n))

    # print(times)
    return min(times[B])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(tory_amos, all_tests=True)
