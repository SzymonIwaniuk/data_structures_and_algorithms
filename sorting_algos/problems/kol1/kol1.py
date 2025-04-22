from random import randint
from kol1testy import runtests


# O(n)
def partition(T, l, r):
    pivot_index = randint(l, r)
    T[pivot_index], T[r] = T[r], T[pivot_index]

    i = l - 1

    for j in range(l, r):
        if T[j] <= T[r]:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


# O(n)
def quickselect(T, l, r, k):
    pivot = partition(T, l, r)

    if pivot == k:
        return pivot
    if pivot < k:
        return quickselect(T, pivot + 1, r, k)
    else:
        return quickselect(T, l, pivot - 1, k)


# O(nlogn)
def quicksort(T, l, r):
    if l < r:
        pivot_ind = partition(T, l, r)
        quicksort(T, l, pivot_ind - 1)
        quicksort(T, pivot_index + 1, l)


# O(n^2), ale dla bucket sorta z rozkładem jednostajnym O(1)
def insertion_sort(T):
    n = len(T)

    for i in range(n):
        key = T[i]
        j = i - 1

        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1

        T[j + 1] = key


# O(n) dla tablicy z wartościami z rozkładu jednostajnego.
def bucket_sort(T):
    n = len(T)
    buckets = [[] for _ in range(n)]

    max_v = max(T)
    min_v = min(T)
    span = max_v - min_v

    for i in range(n):
        bucket_index = int(((T[i] - min_v) / span) * (n - 1))
        buckets[bucket_index].append(T[i])

    k = 0

    for bucket in buckets:
        if len(bucket) <= 32:
            insertion_sort(bucket)
        else:
            quicksort(bucket, 0, len(bucket) - 1)

        for i in range(len(bucket)):
            T[k] = bucket[i]
            k += 1


def ogrodzenie(M, D, T):
    n = len(T)

    mid = quickselect(T, 0, n - 1, n // 2)

    plug = T[:mid]
    rzep = T[mid:]

    bucket_sort(plug)
    bucket_sort(rzep)

    cnt = 0

    for i in range(1, len(plug)):
        if plug[i] - plug[i - 1] >= D:
            cnt += 1

    for i in range(1, len(rzep)):
        if rzep[i] - rzep[i - 1] >= D:
            cnt += 1

    if rzep[0] - plug[len(plug) - 1] >= D:
        cnt += 1

    return cnt


runtests(ogrodzenie, all_tests=True)
