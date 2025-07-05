from collections import deque

from egz3atesty import runtests


def goodknight(G, s, t):
    n = len(G)
    times = [[float("inf") for _ in range(17)] for _ in range(n)]
    # print(times)
    times[s][0] = 0
    Q = deque()
    Q.append((0, s))

    while Q:
        exhaust, v = Q.popleft()
        for u in range(n):
            time = G[v][u]
            # print(exhaust, v, time)
            if time != -1:
                if exhaust + time <= 16:

                    # print(exhaust + time)
                    if times[u][exhaust + time] > times[v][exhaust] + time:
                        times[u][exhaust + time] = times[v][exhaust] + time
                        Q.appendleft((exhaust + time, u))

                else:
                    if times[u][time] > times[v][exhaust] + 8 + time:
                        times[u][time] = times[v][exhaust] + 8 + time
                        Q.append((time, u))

        # print(times)
    return min(times[t])


# zmien all_tests na True zeby uruchomic wszystkie testy
if __name__ == "__main__":
    from egz3atesty import runtests

    runtests(goodknight, all_tests=True)
    # G = [ [ -1, 3, 8,-1,-1,-1 ], # 0
    # [ 3,-1, 3, 6,-1,-1 ], # 1
    # [ 8, 3,-1,-1, 5,-1 ], # 2
    # [ -1, 6,-1,-1, 7, 8 ], # 3
    # [ -1,-1, 5, 7,-1, 8 ], # 4
    # [ -1,-1,-1, 8, 8,-1 ]] # 5
    # s = 0
    # t = 5
    # print(goodknight(G, s, t))
