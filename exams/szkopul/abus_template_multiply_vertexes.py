from heapq import heappop, heappush
from math import ceil, inf
from typing import List, Tuple


def build_adjacency_list(
    edges: List[Tuple[int, int, int]],
    n: int,
) -> List[List[Tuple[int, int]]]:

    graph = [[] for _ in range(n)]

    for v, u, d in edges:
        graph[v].append((u, d))
        graph[u].append((v, d))

    return graph


def abus(
    KR: List[Tuple[int, int, int]],
    OD: List[int],
    B: int,
    s: int,
    t: int,
) -> int:

    n = len(OD)
    graph = build_adjacency_list(KR, n)
    bottles_of_water = [[inf] * (B + 1) for _ in range(n)]

    # time = pierwszy cykl odjazdow autobusow od aktualnej stacji
    # (current_bottles_of_water, station, time, current_cups_of_water)
    queue = [(1, -B, OD[s], s)]

    while queue:
        water, cups, time, station = heappop(queue)
        cups = -cups

        if bottles_of_water[station][cups] <= water:
            continue

        bottles_of_water[station][cups] = water

        for next_station, distance in graph[station]:
            """Czas odjazdu do nastepnej stacji = wielokrotnosc czasu odjazdu
            autobosow z aktualnej stacji ktory jest wiekszy lub rowny od aktualnego
            czasu (OD[station] * ceil(time / OD[station]) pomniejszone o aktualny czas
            (time)
            """
            departure = OD[station] * ceil(time / OD[station]) - time

            """Nowy czas = suma aktualnego + dystansu do nastepnej stacji + czasu odjazdu"""
            new_time = time + distance + departure

            # print(station, next_station, cups, distance + departure, time)

            """Sprawdzenie warunku czy starcza kubkow z woda do przejazdu"""
            if distance + departure <= cups:
                new_cups = cups - distance - departure
                heappush(queue, (water, -new_cups, new_time, next_station))

            else:
                """Jezeli nie to sprawdzenie czy kupno nowej wody pozwala dostac sie
                do nastepnej stacji
                """
                if B >= distance + departure:
                    new_cups = B - distance - departure
                    heappush(queue, (water + 1, -new_cups, new_time, next_station))

    # print(bottles_of_water)
    return min(bottles_of_water[t]) if min(bottles_of_water[t]) != inf else -1


"""
Prosimy o niemodyfikowanie poniższego kodu :)
"""

line = input()
data = list(map(int, line.strip().split()))
E, V, b, s, t = data[:5]
KR = []
for i in range(5, 5 + E * 3, 3):
    KR.append((data[i], data[i + 1], data[i + 2]))
OD = data[len(data) - V : len(data)]
print(abus(KR, OD, b, s, t))
