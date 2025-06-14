from typing import List


def knapsack(W: List[int], P: List[int], B: int) -> int:
    n = len(W)

    F = [[0 for b in range(B + 1)] for i in range(n)]
    for b in range(W[0], B + 1):
        F[0][b] = P[0]

    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]

            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])

    return F[n - 1][B]


if __name__ == "__main__":
    W = [2, 3, 4, 5]
    P = [3, 4, 5, 6]
    B = 5

    print(knapsack(W, P, B))
