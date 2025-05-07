### Arbitraz | Kantor
# Mamy waluty o nr od 1 do n
# K[x][y] = ile waluty y dostaje za x
### Czy istnieje seria transakcji gdzie za jednostke pewnej waluty dostaje jej wiecej niz jeden

# Case 1: Kazda walute mozna wymienic na kazda
## Inizjalizacja grafu: budujemy graf gdzie krawedz pomiedzy walutami to logarytm z 1 przez wartosc wymiany
## Korzystamy z wlasnosci logarytmu i sprawdzamy czy kurs log(1/waluta_x * 1/waluta_y) jest mniejszy niz 0 poniewaz
## traktujemy nasza tablice sasiedztwa jako graf pelny czyli kazda para wierzcholkow, w tym wypadku walut jest polaczona
## (wymienialna)

# Case 2: Nie kazda walute mozna wymienic na kazda
## Inizjalizacja grafu: budujemy graf gdzie krawedz pomiedzy walutami to logarytm z 1 przez wartosc wymiany
## Korzystamy z algorytmu Floyda-Warshalla i sprawdzamy czy znalezlismy 'ujemny' kurs z tej samej waluty na ta sama

from math import log


# Case 1
def kantor(K: list[list[int]]) -> bool:
    n = len(K)
    for v in range(n):
        for u in range(n):
            if log((1 / K[v][u]) * (1 / K[u][v])) < 0:
                return True

    return False


# Case 2
def kantor_2(K: list[list[int]]) -> bool:
    n = len(K)

    for i in range(n):
        for j in range(n):
            if K[i][j]:
                K[i][j] = log(1 / K[i][j])

    for k in range(n):
        for v in range(n):
            for u in range(n):
                if K[v][k] and K[k][u]:
                    exchange_rate = K[v][k] + K[k][u]
                    if K[v][u] == None or exchange_rate < K[v][u]:
                        K[v][u] = exchange_rate

    for i in range(n):
        if K[i][i] != None and K[i][i] < 0:
            return True

    return False


if __name__ == "__main__":
    K1 = [[1.0, 2.0, 0.5], [0.5, 1.0, 0.25], [2.0, 4.5, 1.0]]

    K2 = [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

    K3 = [[1.0, 2.0, None], [0.5, 1.0, 4.0], [1.5, None, 1.0]]

    K4 = [[1.0, 0.9, None], [1.1, 1.0, 0.95], [None, None, 1.0]]

    print(kantor(K1))
    print(kantor(K2))
    print(kantor_2(K3))
    print(kantor_2(K4))
