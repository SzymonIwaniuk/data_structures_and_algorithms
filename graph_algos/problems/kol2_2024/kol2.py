from collections import deque

from kol2testy import runtests


def convert_to_list(G: list[(int, int, int)]) -> list[list[list[int, int]]]:
    n = len(G)
    vertexes = 0

    for v, u, d in G:
        vertexes = max(v, u, vertexes)

    G_list = [[] for _ in range(vertexes + 1)]

    for v, u, d in G:
        G_list[v].append([u, d])
        G_list[u].append([v, d])

    # print(G_list[1])
    return G_list


def warrior(G: list[(int, int, int)], s: int, t: int) -> int:
    G_list = convert_to_list(G)
    n = len(G_list)
    times = [[float("inf")] * 17 for _ in range(n)]
    times[s][0] = 0
    Q = deque()
    Q.append((s, 0))

    while Q:
        v, exhaust = Q.popleft()
        # print(time, v)
        curr_time = times[v][exhaust]

        for u, d in G_list[v]:
            if exhaust + d <= 16:
                if curr_time + d < times[u][exhaust + d]:
                    times[u][exhaust + d] = curr_time + d
                    Q.appendleft([u, exhaust + d])
            else:
                if curr_time + 8 + d < times[u][d]:
                    times[u][d] = curr_time + 8 + d
                    Q.append([u, d])

    # print(times)
    return min(times[t])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(warrior, all_tests=True)
