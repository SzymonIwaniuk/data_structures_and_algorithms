"""
Dany jest zbiór P = {p1, . . . , pn} punktów na płaszczyźnie. Współrzędne punktów to liczby naturalne
ze zbioru {1, . . . , n}. Mówimy, że punkt pi = (xi, yi) dominuje punkt pj = (xj , yj ) jeśli zachodzi:
xi > xj oraz yi > yj . Siłą danego punktu jest to ile punktów dominuje. Zadanie polega na implementacji funkcji:
dominance( P ) która na wejściu otrzymuje listę P zawierającą n punktów (każdy reprezentowany jako para liczb ze
zbioru {1, . . . , n}) i zwraca siłę najsilniejszego z nich. Funkcja powinna być możliwie jak najszybsza.
Przykład. Dla wejścia: P = [(1,3), (3,4), (4,2), (2,2)] wynikiem jest 2. Punkt o współrzędnych (3, 4)
dominuje punkty o współrzędnych (1, 3) oraz (2, 2).
"""


def modified_partition(P, low, high):
    pivot = P[high]
    i = low - 1

    for j in range(low, high):
        if P[j][0] < pivot[0]:
            i += 1
            P[i], P[j] = P[j], P[i]

        elif P[j][0] == pivot[0]:
            if P[j][1] <= pivot[1]:
                i += 1
                P[i], P[j] = P[j], P[i]

    P[i + 1], P[high] = P[high], P[i + 1]
    return i + 1


def modified_quicksort(P, low, high):
    if low < high:
        pivot_index = modified_partition(P, low, high)
        modified_quicksort(P, low, pivot_index - 1)
        modified_quicksort(P, pivot_index + 1, high)


def dominance(P):
    high = len(P) - 1
    low = 0
    modified_quicksort(P, low, high)  # O(nlogn)
    maxi = 0
    t = []

    for x, y in P:  # O(n^2)
        strenght = sum(1 for prev_y in t if prev_y < y)
        maxi = max(maxi, strenght)
        t.append(y)

    return maxi


# calosc pesymistycznie O(n^2)
