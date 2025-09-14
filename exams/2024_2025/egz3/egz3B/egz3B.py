from egz3Btesty import runtests

"""
Autor rozwiazania: Szymon Iwaniuk
Opis: Moje rozwiazanie opiera sie na klasycznym tablicowym dynamiku. Tworze tablice dp dla indeksow 'i' oraz
'zdrowia' od 0 d do W poniewaz zdrowie moze byc == 0. Nastepnie ustawiam dp[0][W] = 0 (pominiecie wyscigu) oraz
dp[0][W-Z[0]] na X[0] (podjecie wyscigu). Nastepnie przechodze po kolejnych indeksach jezeli dp[i-1][z] == float('-inf')
to znaczy ze nie dotarlismy do 'i-1' indeksu przy 'z' zdrowia z jakimkolwiek wynikiem wiec go pomijam. Nastepnie aktualizuje
dp[i][z] o maksimum z (dp[i][z], dp[i-1][z]) co odpowiada nie robieniu niczego. Nastepnie jezeli mozliwe aktualizuje dp[i][low] oraz dp[i][high]
co odpowiada kolejno podjeciu wyscigu lub pojsciu do spa. Na koncu zwracam max z dp[n-1]. Zlozonoc algorytmu oceniam
na O(n*W) poniewaz tworze tablice o wielkosci n*(W+1) oraz aktualizuje ja dwiema pentlami ktore daja n*(W+1).

"""


def kom(X, Z, W):
    n = len(X)

    dp = [[float("-inf") for i in range(W + 1)] for j in range(n)]
    dp[0][W - Z[0]] = X[0]
    dp[0][W] = 0

    for i in range(1, n):
        # next_dp = [float('-inf') for _ in range(W+1)]
        for z in range(W + 1):
            if dp[i - 1][z] == float("-inf"):
                continue

            # if dp[z] > next_dp[z]:
            #     next_dp[z] = dp[z]

            # if dp[i-1][z] > dp[i][z]:
            #   dp[i][z] = dp[i-1][z]
            #

            dp[i][z] = max(dp[i][z], dp[i - 1][z])

            high = z + Z[i]
            low = z - Z[i]

            if low >= 0:
                dp[i][low] = max(dp[i][low], dp[i - 1][z] + X[i])
                # print(dp[i], low, dp[i][low])
            if high <= W:
                dp[i][high] = max(dp[i][high], dp[i - 1][z] - X[i])

    return max(dp[n - 1])

    # def rec(i, )


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kom, all_tests=True)
