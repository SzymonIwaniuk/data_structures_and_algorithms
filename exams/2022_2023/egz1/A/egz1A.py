from heapq import heappop, heappush
from math import inf
from typing import List, Tuple

from egz1Atesty import runtests


def gold(G: List[Tuple[int, int]], V: List[int], s: int, t: int, r: int) -> int:
    n = len(G)
    costs = [[inf] * 2 for _ in range(n)]

    queue = [(0, s, 0)]  # koszt, aktualny_zamek, czy obrobil zamek = 1

    while queue:
        cost, castle, robbed = heappop(queue)
        # print(cost)
        if costs[castle][robbed] < cost:
            continue

        costs[castle][robbed] = cost

        if robbed == 0:
            heappush(queue, (cost - V[castle], castle, 1))

        for new_castle, fee in G[castle]:
            if robbed == 0:
                heappush(queue, (cost + fee, new_castle, robbed))
            else:
                heappush(queue, (cost + (2 * fee) + r, new_castle, robbed))

    # print(costs)
    return min(costs[t])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)
