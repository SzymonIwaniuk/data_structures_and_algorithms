from typing import List
from egz1btesty import runtests


def kstrong(T: List[int], k: int) -> int:
    n = len(T)
    dp = [[float("-inf")] * (k + 1) for _ in range(n)]

    def rec(i, s):
        if dp[i][s] != float("-inf"):
            return dp[i][s]

        if i < 0:
            return 0

        x = T[i]

        maxi = max(x, x + rec(i - 1, s))

        if x < 0 and s > 0:
            maxi = max(maxi, rec(i - 1, s - 1))

        dp[i][s] = maxi
        return dp[i][s]

    rec(n - 1, k)
    return max(max(dp[i]) for i in range(n))


if __name__ == "__main__":
    # zmien all_tests na True zeby uruchomic wszystkie testy
    runtests(kstrong, all_tests=True)
