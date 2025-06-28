from egz2atesty import runtests

inf = float("inf")


def wired(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    F = [[None for i in range(n)] for i in range(n)]

    def _F(i, j):
        nonlocal F, T
        if F[i][j] != None:
            return F[i][j]
        elif i == j:
            return +inf
        elif i + 2 == j:
            return +inf
        elif i + 1 == j:
            return abs(T[i + 1] - T[i]) + 1
        elif j < i:
            return 0

        cur = +inf
        for n_prim in range(i, j, 2):
            cur = min(
                cur,
                _F(i, n_prim - 1) + _F(n_prim + 1, j - 1) + 1 + abs(T[j] - T[n_prim]),
            )
        F[i][j] = cur
        return cur

    return _F(0, n - 1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wired, all_tests=True)
