"""
Dany jest ważony, nieskierowany graf G oraz dwumilowe buty - specjalny sposób poruszania się
po grafie. Dwumilowe buty umożliwiają pokonywanie ścieżki złożonej z dwóch krawędzi grafu tak,
jakby była ona pojedynczą krawędzią o wadze równej maksimum wag obu krawędzi ze ścieżki. Ist-
nieje jednak ograniczenie - pomiędzy każdymi dwoma użyciami dwumilowych butów należy przejść
w grafie co najmniej jedną krawędź w sposób zwyczajny. Macierz G zawiera wagi krawędzi w grafie,
będące liczbami naturalnymi, wartość 0 oznacza brak krawędzi.
Proszę opisać, zaimplementować i oszacować złożoność algorytmu znajdowania najkrótszej ścieżki
w grafie z wykorzystaniem mechanizmu dwumilowych butów.
Rozwiązanie należy zaimplementować w postaci funkcji:
def jumper(G, s, w):
...
która zwraca długość najkrótszej ścieżki w grafie G pomiędzy wierzchołkami s i w, zgodnie z
zasadami używania dwumilowych butów.
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę przedstawić złożoność
czasową oraz pamięciową użytego algorytmu.
"""

from queue import PriorityQueue


def jumper(G: list[list[int]], s: int, w: int) -> int:
    n = len(G)
    Q = PriorityQueue()
    Q.put([0, s])
    parent = [None] * n
    visited = [False] * n
    distance = [float("inf")] * n
    distance[s] = 0

    # djikstra 1
    while Q.qsize() > 0:
        u = Q.get()[1]
        if visited[u]:
            continue
        visited[u] = True
        for v in range(n):
            if distance[v] > distance[u] + G[u][v] and G[u][v] != 0:
                distance[v] = distance[u] + G[u][v]
                parent[v] = u
                Q.put([distance[v], v])

    if distance[w] == float("inf"):
        return distance[w]
    else:
        fastest_path = distance[w]

    def find_fastest_path(flag: bool, len_path: int, current: int) -> None:
        nonlocal fastest_path
        if current == s:
            fastest_path = min(len_path, fastest_path)

        else:
            if not flag and parent[parent[current]]:
                edge = distance[current] - distance[parent[current]]
                prev_edge = (
                    distance[parent[current]] - distance[parent[parent[current]]]
                )
                find_fastest_path(
                    True, len_path - min(edge, prev_edge), parent[parent[current]]
                )

            find_fastest_path(False, len_path, parent[current])

    find_fastest_path(False, fastest_path, w)

    return fastest_path


if __name__ == "__main__":
    G1 = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 7, 0],
        [0, 0, 7, 0, 8],
        [0, 0, 0, 8, 0],
    ]

    G2 = [
        [0, 2, 0, 5, 0, 0],
        [2, 0, 4, 0, 0, 0],
        [0, 4, 0, 1, 6, 0],
        [5, 0, 1, 0, 3, 0],
        [0, 0, 6, 3, 0, 7],
        [0, 0, 0, 0, 7, 0],
    ]

    G3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    G4 = [
        [0, 4, 0, 0, 0],
        [4, 0, 1, 2, 0],
        [0, 1, 0, 0, 3],
        [0, 2, 0, 0, 5],
        [0, 0, 3, 5, 0],
    ]

    G5 = [
        [0, 2, 0, 0, 0, 10],
        [2, 0, 3, 0, 0, 0],
        [0, 3, 0, 1, 0, 0],
        [0, 0, 1, 0, 4, 0],
        [0, 0, 0, 4, 0, 6],
        [10, 0, 0, 0, 6, 0],
    ]

    G6 = [
        [0, 1, 2, 0, 0, 0, 0],
        [1, 0, 0, 3, 0, 0, 0],
        [2, 0, 0, 4, 5, 0, 0],
        [0, 3, 4, 0, 0, 6, 0],
        [0, 0, 5, 0, 0, 1, 2],
        [0, 0, 0, 6, 1, 0, 1],
        [0, 0, 0, 0, 2, 1, 0],
    ]

    print(jumper(G1, 0, 4))
    print(jumper(G2, 0, 5))
    print(jumper(G3, 0, 3))
    print(jumper(G4, 0, 4))
    print(jumper(G5, 0, 4))
    print(jumper(G6, 0, 6))
