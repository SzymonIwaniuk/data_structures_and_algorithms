from random import randint

"""
Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T , tak
aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
podać złożoność czasową i pamięciową zaproponowanego algorytmu.
"""


def partition(T: list, l: int, r: int) -> int:
    mid = (l + r) // 2
    # swap
    T[mid], T[r] = T[r], T[mid]
    pivot = T[r]
    i = l - 1

    for j in range(l, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quicksort(T: list, l: int, r: int) -> any:
    if l < r:
        pivot_ind = partition(T, l, r)
        quicksort(T, l, pivot_ind - 1)
        quicksort(T, pivot_ind + 1, r)


def Median(T: list) -> list:
    # Linearyzacja tablicy O(N^2) pamieciowa O(N^2)
    N = len(T)
    new_tab = [0] * (N * N)

    # print(new_tab)

    for i in range(N):
        for j in range(N):
            new_tab[i * N + j] = T[i][j]

    # print(new_tab)
    # Sortowanie quicksortem O(N^2log(N^2)) = O(N^2log(N))
    quicksort(new_tab, 0, N * N - 1)
    # print(new_tab)
    # Wpisywanie wyniku do tablicy
    i = j = N - 1
    cnt1 = 0
    cnt2 = N * N - 1

    while i >= 0 and j >= 0:
        tmp_i = i
        tmp_j = j
        tmp_m = 0
        tmp_n = 0

        while tmp_i < N and tmp_m < N:
            T[tmp_m][tmp_i] = new_tab[cnt2]
            cnt2 -= 1
            tmp_i += 1
            tmp_m += 1

        while tmp_j < N and tmp_n < N:
            T[tmp_j][tmp_n] = new_tab[cnt1]
            cnt1 += 1
            tmp_j += 1
            tmp_n += 1

        i -= 1
        j -= 1

    return T


table = [[5, 12, 17, 5], [2, 3, 19, 8], [7, 9, 6, 11], [2, 15, 10, 18]]


# testy------------------------------------------------------------------------>
print(Median(table))

T = Median(table)
for i in range(len(T)):
    print(T[i])


# A = [randint(0, 20) for _ in range(10)]
# print(A)
# quicksort(A, 0, len(A) - 1)
# print(A)
