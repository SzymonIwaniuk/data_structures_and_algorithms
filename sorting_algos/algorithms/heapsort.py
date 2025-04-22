from math import floor


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def buildheap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, i, n)


def heapify(T, i, n):
    l = left(i)
    r = right(i)
    maxi_ind = i

    if l < n and T[l] > T[maxi_ind]:
        maxi_ind = l

    if r < n and T[r] > T[maxi_ind]:
        maxi_ind = r

    if maxi_ind != i:
        T[i], T[maxi_ind] = T[maxi_ind], T[i]
        heapify(T, maxi_ind, n)


def heapsort(T):
    n = len(T)
    buildheap(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, 0, i)


from random import randint

t = [randint(1, 100) for i in range(10)]
print(t)
heapsort(t)
print(t)
