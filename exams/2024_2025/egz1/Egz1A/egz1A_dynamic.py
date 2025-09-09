from egz1Atesty import runtests
from typing import List


def battle(P: List[int], K: List[int], R: List[int]) -> int:
    catapults = list(zip(K, R))
    catapults = [('k', p, r) for p, r in catapults]
    processors = [('p', p) for p in P]
    both = catapults + processors
    both.sort(key=lambda t: t[1])

    n = len(both)

    def rec(i, j):
        if both[i][0] == 'p':
            return rec(i + 1, j)
        else:
            maxi = float('inf')

            if both[j-1][0] == 'p' rec(i + 1, j - 1) + 1

            rec(i + 1, j)
            rec(i, j - 1)







runtests(battle, all_tests=False)