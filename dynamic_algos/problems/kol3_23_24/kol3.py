from kol3testy import runtests
from typing import List


def orchard(T: List[int], m: int) -> int:
    n = len(T)
    F = [[-1 for _ in range(m)] for _ in range(n)]

    # warunek brzegowy
    F[0][T[0] % m] = 1
    F[0][0] = 0

    for i in range(1, n):
        for j in range(m):
            if F[i - 1][j] >= 0:
                if F[i][j] < F[i - 1][j]:
                    F[i][j] = F[i - 1][j]

                rest = (j + T[i]) % m
                if F[i][rest] < F[i - 1][j] + 1:
                    F[i][rest] = F[i - 1][j] + 1

    return n - F[n - 1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
