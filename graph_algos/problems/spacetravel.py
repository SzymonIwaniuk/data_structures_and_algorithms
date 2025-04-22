"""
Układ planetarny Algon składa się z n planet o numerach od 0 do n − 1. Niestety własności
fizyczne układu powodują, że nie da się łatwo przelecieć między dowolnymi dwiema planetami. Na
szczęście mozolna eksploracja kosmosu doprowadziła do stworzenia listy E dopuszczalnych bezpo-
średnich przelotów. Każdy element listy E to trójka postaci (u, v, t), gdzie u i v to numery planet
(można założyć, że u < v) a t to czas podróży między nimi (przelot z u do v trwa tyle samo co
z v do u). Dodatkową nietypową własnością układu Algon jest to, że niektóre planety znajdują
się w okolicy osobliwości. Znajdując się przy takiej planecie możliwe jest zagięcie czasoprzestrzeni
umożliwiające przedostanie się do dowolnej innej planety leżącej przy osobliwości w czasie zerowym.
Zadanie polega na zaimplementowaniu funkcji:
def spacetravel( n, E, S, a, b )
która zwraca najkrótszy czas podróży z planety a do planety b, mając do dyspozycji listę możliwych
bezpośrednich przelotów E oraz listę S planet znajdujących się koło osobliwości. Jeśli trasa nie
istnieje, to funkcja powinna zwrócić None.
"""

import heapq
from typing import Tuple


def spacetravel(
    n: int, E: list[Tuple[int, int, float]], S: list[int], a: int, b: int
) -> float:

    Algon = convert_to_list(n, E, S)
    distance = [float("inf")] * (n + 1)
    distance[a] = 0
    visited = [False] * (n + 1)
    Q = [(0, a)]

    while len(Q) > 0:
        d, u = heapq.heappop(Q)
        if visited[u]:
            continue
        visited[u] = True

        for v, w in Algon[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                heapq.heappush(Q, (distance[v], v))

    return distance[b] if distance[b] != float("inf") else None


def convert_to_list(
    n: int, E: list[Tuple[int, int, float]], S: list[int]
) -> list[list[list[int, float]]]:

    G = [[] for _ in range(n + 1)]
    for v, u, d in E:
        G[v].append((u, d))
        G[u].append((v, d))

    l = len(S)
    blackhole = n

    for s in S:
        G[s].append((blackhole, 0))
        G[blackhole].append((s, 0))

    return G


if __name__ == "__main__":
    # tests
    E1 = [
        (0, 1, 5),
        (1, 2, 21),
        (1, 3, 1),
        (2, 4, 7),
        (3, 4, 13),
        (3, 5, 16),
        (4, 6, 4),
        (5, 6, 1),
    ]
    S1 = [0, 2, 3]
    a1 = 1
    b1 = 5
    n1 = 7
    print(spacetravel(n1, E1, S1, a1, b1))
    a2 = 1
    b2 = 2
    print(spacetravel(n1, E1, S1, a2, b2))
