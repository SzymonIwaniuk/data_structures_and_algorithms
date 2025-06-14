from typing import List


def orchard(T: List[int], m: int) -> int:
    n = len(T)
    F = [[0 for _ in range(m)] for _ in range(n)]

    # warunek brzegowy

    F[0][T[0] % m] = T[0]

    for i in range(1, n):
        for j in range(m):
            rest = (F[i - 1][j] + T[i]) % m
            F[i][rest] = max(F[i - 1][j] + T[i], F[i][rest])
        F[i][0] = max(F[i][0], F[i - 1][0])

    # print(F)
    return F[n - 1][0]


if __name__ == "__main__":
    T = [2, 2, 7, 5, 1, 14, 7]
    m = 7

    print(orchard(T, m))
