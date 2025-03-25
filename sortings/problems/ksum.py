"""
Dana jest n-elementowa tablica liczb naturalnych T oraz dodatnie liczby naturalne k i p, gdzie
k ≤ p ≤ n. Niech zi będzie k-tym największym spośród elementów: T[i], T[i+1], ..., T[i+p-1].
Innymi słowy, zi to k-ty największy element w T w przedziale indeksów od i do i + p − 1 włącznie.

Doprecyzowanie: Rozważmy tablicę [17,25,25,30]. W tej tablicy 1-wszy największy element
to 30, 2-gi największy element to 25, 3-ci największy element to także 25 (drugie wystąpienie), a
4-ty największy element to 17.

Proszę zaimplementować funkcję ksum(T, k, p), która dla tablicy T (o rozmiarze n elementów) i
dodatnich liczb naturalnych k i p (k ≤ p ≤ n) wylicza i zwraca wartość sumy:
z0 + z1 + z2 + . . . + zn−p
Przykład. Dla wejścia:
T = [7,9,1,5,8,6,2,12]
k = 4
p = 5
wywołanie ksum(T, k, p) powinno zwrócić wartość 17 (odpowiadającą sumie 5 + 5 + 2 + 5).
Algorytm powinien być możliwie jak najszybszy. Proszę uzasadnić poprawność zaproponowanego
algorytmu oraz oszacować jego złożoność czasową i pamięciową
"""


def partition(A, low, high):
    pivot = A[high]
    i = low - 1

    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1


def quickselect(A, low, high, k):
    if low <= high:
        pivot_index = partition(A, low, high)
        if pivot_index == k:
            return A[pivot_index]
        elif pivot_index < k:
            return quickselect(A, pivot_index + 1, high, k)
        else:
            return quickselect(A, low, pivot_index - 1, k)


def ksum(T, k, p):
    n = len(T)
    suma = 0
    prev_r = None
    prev = None
    for i in range(n - p + 1):
        A = T[i : i + p]
        lval = A[p - 1]

        if prev_r == None:
            # print(A)
            # print(quickselect(A,0,p-1,k))
            prev_r = A[0]
            b = quickselect(A, 0, p - 1, p - k)
            suma += b
            prev = b

        elif lval > prev and prev_r > prev:
            suma += prev
            prev_r = A[0]
        elif lval < prev and prev_r < prev:
            suma += prev
            prev_r = A[0]
        else:
            prev_r = A[0]
            b = quickselect(A, 0, p - 1, p - k)
            suma += b
            prev = b

    return suma


runtests(ksum, all_tests=True)
