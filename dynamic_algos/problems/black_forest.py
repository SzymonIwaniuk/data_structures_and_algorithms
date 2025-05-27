"""
Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
składa się z n drzew rosnących na pozycjach 0,..., n-1. Dla każdego i € {0,...,n—1} znany jest zysk c_i, jaki
można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
John znajdzie optymalny plan wycinki.
"""

# f(i) = największy zysk ze ściętych drzew do pozycji i (nie koniecznie drzewo z pozycji i zostało ścięte)
# f(i) = max { f(i - 1), f(i - 2) + C[i] } - albo nie ścinamy drzewa, albo ścinamy

# przypadki graniczne:
# f(0) = C[0]
# f(1) = max {f(0), C[1]}

# wynik f(n - 1)

# Powinna wystarczyć tylko jedna tablica, gdzie nadpisujemy z każdym następnym.

# O(n)

from typing import List


def black_forest(C: List[int]) -> int:
    l = len(C)
    income = [0 for _ in range(l)]
    income[0] = C[0]
    income[1] = max(income[0], C[1])

    for i in range(2, l):
        income[i] = max(income[i - 1], income[i - 2] + C[i])

    return income[l - 1]


if __name__ == "__main__":
    T = [1, 8, 3, 4, 5, 1, 2]
    print(black_forest(T))
    T = [1, 8, 3, 4, 5, 2, 0, 0, 0, 0]
    print(black_forest(T))
    T = [1, 0, 8, 0, 3, 0, 4, 0, 5, 0, 2]
    print(black_forest(T))
    T = [1, 8, 3, 4, 5, 1, 2]
    print(black_forest(T))
    T = [8, 1, 3, 4, 5, 1, 2]
    print(black_forest(T))
    T = [8, 12, 3, 4, 7, 1, 2, 10]
    print(black_forest(T))
