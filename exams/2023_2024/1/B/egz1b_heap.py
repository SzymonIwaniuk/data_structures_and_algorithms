from typing import List
from egz1btesty import runtests
from heapq import heappush, heappop, heapify


def kstrong(T: List[int], k: int) -> int:
    n = len(T)
    res = float("-inf")

    for i in range(n):
        smallest = []
        l_smallest = 0
        sum_smallest = 0
        total = 0

        for j in range(i, n):
            num = T[j]
            total += num
            if num < 0:
                if l_smallest < k:
                    sum_smallest += num
                    heappush(smallest, -num)
                    l_smallest += 1

                else:
                    biggest = -heappop(smallest)
                    if num < biggest:
                        heappush(smallest, -num)
                        sum_smallest = sum_smallest - biggest + num
                    else:
                        heappush(smallest, -biggest)

            res = max(res, total - sum_smallest)

    return res


if __name__ == "__main__":
    # zmien all_tests na True zeby uruchomic wszystkie testy
    runtests(kstrong, all_tests=True)
