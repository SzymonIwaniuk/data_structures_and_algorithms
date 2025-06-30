from egz3btesty import runtests
from math import inf
from heapq import heappush, heappop


def gen_kunlucky_set(T, k, max_num):
    kset = set()
    x = k
    i = 1

    while x <= max_num:
        kset.add(x)
        x = x + (x % i) + 7
        i += 1

    return kset


def kunlucky(T, k):
    n = len(T)

    kset = gen_kunlucky_set(T, k, n)  # liczby z zakresu [1, ..., n], więc max_num = n
    queue = []
    max_len = 0
    k_cnt = 0
    current_len = 0

    for i in range(n):
        if T[i] in kset:
            if k_cnt > 1:
                j = heappop(queue)
                max_len = max(max_len, current_len)
                current_len = i - j - 1
                heappush(queue, i)
            else:
                k_cnt += 1
                heappush(queue, i)

        current_len += 1

    # Edge case gdy spojny podciag lezy az do konca
    max_len = max(max_len, current_len)

    return max_len


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kunlucky, all_tests= True)
