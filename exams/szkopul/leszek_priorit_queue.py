from queue import PriorityQueue
from math import inf, ceil
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


def leszek(
    KR: List[Tuple[int, int, int]],
    OD: List[int],
    B: int,
    s: int,
    t: int,
) -> int:

    n = len(OD)
    graph = build_adjacency_list(KR, n)
    bottles_of_water = [inf for _ in range(n)]

    # time = pierwszy cykl odjazdow autobusow od aktualnej stacji
    # (current_bottles_of_water, station, time, current_cups_of_water)
    queue = PriorityQueue()
    queue.put((1, -B, OD[s], s))

    while not queue.empty():
        water, cups, time, station = queue.get()
        cups = -cups

        if bottles_of_water[station] < water:
            continue

        bottles_of_water[station] = water

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
                queue.put((water, -new_cups, new_time, next_station))

            else:
                """Jezeli nie to sprawdzenie czy kupno nowej wody pozwala dostac sie
                do nastepnej stacji
                """
                if B >= distance + departure:
                    new_cups = B - distance - departure
                    queue.put((water + 1, -new_cups, new_time, next_station))

    # print(bottles_of_water)
    return bottles_of_water[t] if bottles_of_water[t] != inf else -1


if __name__ == "__main__":
    KR = [(0, 4, 4), (0, 1, 7), (1, 3, 6), (4, 3, 2), (1, 2, 1), (3, 2, 3)]
    OD = [1, 6, 1, 7, 4]
    B = 10
    s = 0
    t = 2
    print(leszek(KR, OD, B, s, t))
