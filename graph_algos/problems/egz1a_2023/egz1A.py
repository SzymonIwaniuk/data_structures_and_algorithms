from heapq import heappop, heappush
from typing import Tuple

def dijkstra_normal(G: list[Tuple[int ,int]], s: int) -> list[int]:
    n = len(G)
    cost_tab = [float('inf')] * n
    cost_tab[s] = 0
    Q = [(0, s)]

    while Q:
        cur_cost, v = heappop(Q)

        if cur_cost > cost_tab[v]:
            continue

        for u, cost in G[v]:
            if cost_tab[u] > cur_cost + cost:
                cost_tab[u] = cur_cost + cost
                heappush(Q, (cost_tab[u], u))

    return cost_tab


def dijkstra_robbed(G: list[Tuple[int ,int]], t: int, r: int) -> list[int]:
    n = len(G)
    cost_tab = [float('inf')] * n
    cost_tab[t] = 0
    Q = [(0, t)]

    while Q:
        cur_cost, v = heappop(Q)

        if cur_cost > cost_tab[v]:
            continue

        for u, cost in G[v]:
            if cost_tab[u] > cur_cost + cost * 2 + r:
                cost_tab[u] = cur_cost + cost * 2 + r
                heappush(Q, (cost_tab[u], u))

    return cost_tab

def gold(G: list[Tuple[int ,int]], V: list[int], s: int, t: int, r: int) -> int:
    lenght = len(V)
    cost_normal = dijkstra_normal(G, s)
    cost_robbed = dijkstra_robbed(G, t, r)
    # print(cost_normal)
    # print(cost_robbed)

    mini = float('inf')

    for i in range(lenght):
        mini = min(mini, cost_normal[i] + cost_robbed[i] - V[i], cost_normal[t])

    return mini

# zmien all_tests na True zeby uruchomic wszystkie testy
if __name__ == '__main__':
    from egz1Atesty import runtests
    runtests( gold, all_tests = True )

    # G = [[(1,9), (2,2)],
    # [(0,9), (3,2), (4,6)],
    # [(0,2), (3,7), (5,1)],
    # [(1,2), (2,7), (4,2), (5,3)],
    # [(1,6), (3,2), (6,1)],
    # [(2,1), (3,3), (6,8)],
    # [(4,1), (5,8)] ]
    # V = [25,30,20,15,5,10,0]
    # s = 0; t = 6; r = 3
    # print(gold(G, V, s, t, r))

