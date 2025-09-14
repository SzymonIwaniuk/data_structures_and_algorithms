from math import inf
from egz3btesty import runtests


def get_kunlucky_set(k, n):
    kunlucky_set = {}
    i = 1

    while k <= n:
        kunlucky_set[k] = True
        k = k + (k % i) + 7
        i += 1

    return kunlucky_set


def kunlucky(T, k):
    n = len(T)
    kunlucky_set = get_kunlucky_set(k, n)
    j = 0
    k_cnt = 0
    res = 0

    for i in range(n):
        if T[i] in kunlucky_set:
            if k_cnt + 1 > 2:
                while T[j] not in kunlucky_set:
                    j += 1
                j += 1
            else:
                k_cnt += 1
        res = max(res, i - j + 1)

    res = max(res, i - j + 1)
    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kunlucky, all_tests=True)
