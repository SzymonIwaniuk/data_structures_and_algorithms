from heapq import heappop, heappush
from math import inf
from typing import List, Optional, Tuple

from egz1atesty import runtests


def build_adjacency_list(
    G: List[Tuple[int, int, int]], n: int
) -> List[List[Tuple[int, int]]]:
    graph = [[] for _ in range(n)]

    for u, v, w in G:
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph


def best_bike(B: List[Tuple[int, int, int]], n: int) -> List[Optional[int]]:
    best_bikes = [None for _ in range(n)]

    for i, p, q in B:
        if best_bikes[i] == None or best_bikes[i] > p / q:
            best_bikes[i] = p / q

    return best_bikes


def armstrong(
    B: List[Tuple[int, int, int]], G: List[Tuple[int, int, int]], s: int, t: int
) -> int:
    n = max(max(u, v) for u, v, w in G)
    graph = build_adjacency_list(G, n + 1)
    best_bikes = best_bike(B, n + 1)
    times = [[inf, inf] for _ in range(n + 1)]
    queue = [(0, s, 0, 1)]

    # print(graph)
    # print(best_bikes)
    while queue:
        time, v, bike, efficency = heappop(queue)
        if times[v][bike] < time:
            continue

        times[v][bike] = time

        # print(time, v, bike, efficency)

        for u, distance in graph[v]:
            if bike == 0 and best_bikes[v] != None and best_bikes[v] < 1:
                get_bike = best_bikes[v]
                heappush(queue, (time + distance * get_bike, u, 1, get_bike))
            heappush(queue, (time + distance * efficency, u, bike, efficency))

    # print(times[t])
    return int(min(times[t]))


if __name__ == "__main__":
    # zmien all_tests na True zeby uruchomic wszystkie testy
    runtests(armstrong, all_tests=True)
