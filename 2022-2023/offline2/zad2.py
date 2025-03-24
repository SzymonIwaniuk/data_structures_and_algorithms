from zad2testy import runtests


def parent(i: int) -> int:
    return (i - 1) // 2


def left(i: int) -> int:
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def heapify(T: list, i: int, n: int) -> any:
    max_ind = i
    l = left(i)
    r = right(i)

    if l < n and T[max_ind] < T[l]:
        max_ind, l = l, max_ind

    if r < n and T[max_ind] < T[r]:
        max_ind, r = r, max_ind

    if max_ind != i:
        T[max_ind], T[i] = T[i], T[max_ind]
        heapify(T, max_ind, n)


def buildheap(T: list) -> any:
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, i, n)


def snow(S: list) -> int:
    n = len(S)
    tmp = 0
    suma = 0
    ind = n
    buildheap(S)

    while S[0] - tmp > 0 and n - tmp > 0:

        suma += S[0] - tmp
        ind -= 1
        S[0], S[ind] = S[ind], S[0]
        tmp += 1
        heapify(S, 0, ind)

    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
