from math import inf
from typing import List

from egz1btesty import runtests


def kstrong(T: List[int], k: int) -> int:
    n = len(T)

    dp = [[None] * (k + 1) for _ in range(n)]

    def kstrong_rec(index, skipped):
        if index < 0:
            return 0

        if dp[index][skipped] is not None:
            return dp[index][skipped]

        x = T[index]
        result = x

        result = max(result, x + kstrong_rec(index - 1, skipped))

        if x < 0 and skipped > 0:
            result = max(result, kstrong_rec(index - 1, skipped - 1))

        dp[index][skipped] = result
        return result

    maxi = -inf
    for i in range(n):
        for j in range(k + 1):
            maxi = max(maxi, kstrong_rec(i, j))

    return maxi


if __name__ == "__main__":
    # zmien all_tests na True zeby uruchomic wszystkie testy
    runtests(kstrong, all_tests=True)
