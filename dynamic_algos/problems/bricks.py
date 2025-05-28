"""
Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a,b]. Dany jest ciąg klocków [a1,b1],
[a2,b2], ..., [an,bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
się w całości na klocku, który spadł tuż przed nim.
"""

# f(i) - maksymalna wysokosc wiezy skonstruowanej uzywajac klockow do indeksu i
# n - max f = wynik

# f(i) = max { (f[0, i - 1] jeżeli przedział a_i zawiera się w przedziale a_i-1) + 1 }

from typing import List


def bricks(a: List[List[int, int]]) -> int:
    n = len(a)
    F = [0] * n

    for i in range(n):
        F[i] = 1
        for j in range(i):
            F[i] = max(
                F[i], F[j] + 1 if a[i][0] >= a[j][0] and a[i][1] <= a[j][1] else 0
            )

    return n - max(F)


if __name__ == "__main__":
    ranges = [[0, 5], [1, 4], [-3, 7], [2, 3], [2, 6], [4, 6], [2, 3]]
    print(bricks(ranges))
    ranges = [
        (0, 10),
        (1, 10),
        (2, 6),
        (6, 7),
        (11, 20),
        (11, 19),
        (12, 18),
        (13, 19),
        (14, 20),
    ]
    (bricks(ranges))
