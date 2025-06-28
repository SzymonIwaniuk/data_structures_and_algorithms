from egz2atesty import runtests


def dominance(P):
    max_x = max(P, key=lambda p: p[0])[0]
    max_y = max(P, key=lambda p: p[1])[1]

    GRTTY = [0] * (max_y + 1)
    SMLRTX = [0] * (max_x + 1)
    EQLTX = [0] * (max_x + 1)

    for x, y in P:
        GRTTY[y] += 1
        SMLRTX[x] += 1
        EQLTX[x] += 1

    for x in range(1, max_x + 1):
        SMLRTX[x] += SMLRTX[x - 1]
    for y in range(max_y - 1, -1, -1):
        GRTTY[y] += GRTTY[y + 1]

    max_strength = 0

    for x, y in P:
        max_strength = max(max_strength, SMLRTX[x] - GRTTY[y] - EQLTX[x] + 1)

    return max_strength


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance, all_tests=True)
