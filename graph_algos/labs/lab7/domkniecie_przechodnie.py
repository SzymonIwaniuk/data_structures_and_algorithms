# 4. Domkniecie przechodnie grafu G skierowanego to taki graf G' ze jesli G ma sciezke z u do v to G' ma krawedz z u do v
# Chcemy algorytm obliczajacy domkniecie przechodnie reprezentacja macierzowa
# algorytm floyda - warshalla

from copy import deepcopy


def domkniecie_przechodnie(G: list[list[int]]) -> list[list[int]]:
    n = len(G)
    S = deepcopy(G)

    for i in range(n):
        for v in range(n):
            for u in range(n):
                if S[v][i] and S[i][u]:
                    S[v][u] = 1
    return S


if __name__ == "__main__":
    G1 = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]

    G2 = [[0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 1, 0]]

    print(domkniecie_przechodnie(G1))
    print(domkniecie_przechodnie(G2))
