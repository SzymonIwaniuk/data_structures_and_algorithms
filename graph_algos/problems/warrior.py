from collections import deque


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


def warrior(G: list[(int, int, int)], s: int, t: int) -> (int, list[int]):
    G_list = convert_to_list(G)
    n = len(G_list)
    times = [[[float("inf"), None, None]] * 17 for _ in range(n)]
    times[s][0] = [0, None, None]
    Q = deque()
    Q.append((s, 0))

    while Q:
        v, exhaust = Q.popleft()
        # print(time, v)
        curr_time, r, c = times[v][exhaust]
        print(times[v][exhaust])
        for u, d in G_list[v]:
            if exhaust + d <= 16:
                if curr_time + d < times[u][exhaust + d][0]:
                    times[u][exhaust + d] = curr_time + d, v, exhaust
                    Q.appendleft([u, exhaust + d])
            else:
                if curr_time + 8 + d < times[u][d][0]:
                    times[u][d] = curr_time + 8 + d, v, exhaust
                    Q.append([u, d])

    # print(times)

    time, row, column = min(times[t], key=lambda x: x[0])
    path = [t]

    while row != None and column != None:
        path.append(row)
        row = times[row][column][1]
    path.append(s)

    return time, path[::-1]


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
