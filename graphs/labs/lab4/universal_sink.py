def universal_sink(G: list[list[int]]) -> int:
    n = len(G)
    v = 0

    for i in range(1, n):
        if G[v][i] == 1:
            v = i

    for j in range(n):
        if j != v:
            if G[v][j] != 0 or G[j][v] != 1:
                return -1

    return v


if __name__ == "__main__":

    G1 = [[0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 1, 0, 0]]

    G2 = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]

    print(universal_sink(G1))
