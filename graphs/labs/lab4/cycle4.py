"""
Prosze podac algorytm znajdujacy cykl czteroelementowy w czasie O(n^3)
(reprezentacja macierzowa)
"""

# Generujemy wszystkie 2 elementowe podzbiory wierzcholkow z ktorymi dany
# wierzcholek jest polaczony i szukamy takiej samej pary.


def cycle4(G: list[list[int]]) -> bool:
    n = len(G)
    tab = []

    for i in range(n):
        for j in range(n):
            for k in range(j + 1, n):
                if G[i][j] == 1 and G[i][k] == 1:
                    tab.extend([j, k])

    # sprawdzamy pary

    l = len(tab)
    for i in range(0, l - 2, 2):
        v1, u1 = tab[i], tab[i + 1]

        for j in range(2, l, 2):
            v2, u2 = tab[j], tab[j + 1]
            if v1 == v2 and u1 == u2:
                return True

    return False


if __name__ == "__main__":

    G = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]

    G1 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ]

    print(cycle4(G))
