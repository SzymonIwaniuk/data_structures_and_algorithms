from zad3testy import runtests
from math import inf
from math import inf


def common_part(array, k):
    indexes = []
    intersection = [-inf, inf]
    max_l = 0

    for i in range(k):
        a1, b1 = intersection
        a2, b2 = array[i][1]
        indexes.append(array[i][0])
        start = max(a1, a2)
        end = min(b1, b2)

        if start < end:
            intersection = [start, end]
            max_l = end - start
        else:
            return 0, []

    return max_l, indexes


def kintersect( A, k ):
    max_intersect = -1
    res = []
    A = sorted(enumerate(A), key=lambda x: x[1][0])
    # print(A)
    n = len(A)
    # print(A)
    # print(current_array)

    for i in range(n - k + 1):
        current_array = A[i:i + k]
        l, indexes = common_part(current_array, k)
        #print(l, indexes)
        if l > max_intersect:
            max_intersect = l
            res = indexes

    return res





runtests(kintersect)
