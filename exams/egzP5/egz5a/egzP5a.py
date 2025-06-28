from egzP5atesty import runtests 
from math import inf


def inwestor ( T ):
    n = len(T)
    best = 0

    for i in range(n):
        min_num = inf

        for j in range(i, n):
            min_num = min(min_num, T[j])
            best = max(best, min_num * (j - i + 1))

    return best

runtests ( inwestor, all_tests=True)