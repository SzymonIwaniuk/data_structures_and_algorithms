from egz2Btesty import runtests

"""
Autor rozwiazania: Szymon Iwaniuk
Rozwiazanie polega na zachlannym dodawaniu do stacka prawego konca przedzialow jezeli spelniaja warunek ze dla
kolejnych [0, u], [0, v] ; v < u. Jezeli nie to szukam w stacku zmodyfikowanym binary searchem indexu
rownego liczbie v badz wiekszej oraz aktualizuje top. Moge to zrobic poniewaz elementu w stacku sa w porzadku scisle malejacym.
Wykonuje to w czasie logn poniewaz na biezaco aktualizuje dlugosc stacka top. l to zmienna pomocnicza w ktorej trzymam
dlugosc calej tablicy. Zlozonosc algorytmu oceniam na nlogn
"""


def bin_search(arr, num, top):
    left = 0
    right = top

    while left < right:
        # print(left, right)
        mid = (left + right) // 2

        if arr[mid] == num:
            return mid

        if arr[mid] < num:
            right = mid

        else:
            left = mid + 1

    return left


def bitgame(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    if n == 0:
        return 0

    stack = [T[0]]
    top = 1
    l = 1

    for i in range(1, n):
        # print(stack, top, l, i)
        if T[i] < stack[top - 1]:
            if top == l:
                stack.append(T[i])
                l += 1
            else:
                stack[top] = T[i]
            top += 1

        else:
            j = bin_search(stack, T[i], top - 1)
            top = j

    return top


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(bitgame, all_tests=True)
