from collections import deque
from typing import Tuple


def convert_to_list(G: list[(int, int, int)]) -> list[list[Tuple[int, int]]]:
    vertexes = 0

    for v, u, d in G:
        vertexes = max(v, u, vertexes)

    G_list = [[] for _ in range(vertexes + 1)]

    for v, u, d in G:
        G_list[v].append((u, d))
        G_list[u].append((v, d))

    # print(G_list[1])
    return G_list


def warrior(G: list[Tuple[int, int, int]], s: int, t: int) -> int:

    n = len(G)
    G_list = convert_to_list(G)
    times = [[float("inf") for _ in range(17)] for _ in range(n)]
    times[s][0] = 0

    Q = deque()
    Q.append((0, s))

    while Q:
        exhaust, v = Q.popleft()
        for u, time in G_list[v]:
            if exhaust + time <= 16:
                if times[u][exhaust + time] > times[v][exhaust] + time:
                    times[u][exhaust + time] = times[v][exhaust] + time
                    Q.appendleft((exhaust + time, u))

            else:
                if times[u][time] > times[v][exhaust] + 8 + time:
                    times[u][time] = times[v][exhaust] + 8 + time
                    Q.append((time, u))

    return min(times[t])


if __name__ == "__main__":
    G = [
        (1, 5, 10),
        (4, 6, 12),
        (3, 2, 8),
        (2, 4, 4),
        (2, 0, 10),
        (1, 4, 5),
        (1, 0, 6),
        (5, 6, 8),
        (6, 3, 9),
    ]
    s = 0
    t = 6
    print(warrior(G, s, t))
