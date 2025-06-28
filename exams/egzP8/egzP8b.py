def convert_to_matrix(G, S, n):
    for v in range(n):
        for u, d in G[v]:
            S[v][u] = d
            S[u][v] = d

    for i in range(n):
        for j in range(n):
            if S[i][j] == 0:
                S[i][j] = float("inf")

    return S


# O(n^3)
def robot(G, P):
    n = len(G)
    l = len(P)
    distance = 0
    S = [[0] * n for _ in range(n)]
    S = convert_to_matrix(G, S, n)

    # Floyd - Warshall
    for k in range(n):
        for v in range(n):
            for u in range(n):
                S[v][u] = min(S[v][u], S[v][k] + S[k][u])

    for i in range(l - 1):
        p = P[i]
        p_next = P[i + 1]

        distance += S[p][p_next]

    return distance


if __name__ == "__main__":
    from egzP8btesty import runtests

    runtests(robot, all_tests=True)
