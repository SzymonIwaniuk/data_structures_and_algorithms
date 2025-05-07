from copy import deepcopy


def floyd_warshall(G: list[list[float]]) -> list[list[float]]:
    n = len(G)
    S = deepcopy(G)

    for k in range(n):
        for v in range(n):
            for u in range(n):
                S[v][u] = min(S[v][u], S[v][k] + S[k][u])

    return S


if __name__ == "__main__":

    G = [
        [0, 2, 4, float("inf"), float("inf"), float("inf")],
        [float("inf"), 0, 1, 7, float("inf"), float("inf")],
        [float("inf"), float("inf"), 0, float("inf"), 3, float("inf")],
        [float("inf"), float("inf"), float("inf"), 0, float("inf"), 1],
        [float("inf"), float("inf"), float("inf"), 2, 0, 5],
        [8, 6, float("inf"), float("inf"), float("inf"), 0],
    ]

    print(floyd_warshall(G))
