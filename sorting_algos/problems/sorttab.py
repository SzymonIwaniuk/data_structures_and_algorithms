"""
Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały wyge-
nerowane z pewnego rozkładu losowego. Rozkład ten mamy zadany jako k przedziałów
[a1, b1], [a2, b2], . . . , [ak, bk] takich, że i-ty przedział jest wybierany z prawdopodobieństwem
ci, a liczba z przedziału (x ∈ [ai, bi]) jest losowana zgodnie z rozkładem jednostajnym. Przedziały
mogą na siebie nachodzić. Liczby ai, bi są liczbami naturalnymi ze zbioru {1, . . . , N }.
Proszę zaimplementować funkcję SortTab(T, P) sortująca podaną tablicę i zwracająca posortowa-
ną tablicę jako wynik. Pierwszy argument to tablica do posortowania a drugi to opis przedziałów
w postaci:
P = [(a_1,b_1,c_1), (a_2,b_2,c_2), ..., (a_k,b_k,c_k)]}.
Na przykład dla wejścia:
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
P = [(1, 5, 0.75) , (4, 8, 0.25)]
po wywołaniu SortTab(T,P) tablica zwrócona w wyniku powinna mieć postaci:
T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]
Algorytm powinien być możliwie jak najszybszy. Proszę podać złożoność czasową i pamięciową
zaproponowanego algorytmu.
"""

from math import ceil, floor

P = [(1, 5, 0.75), (4, 8, 0.25)]
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]


def SortTab(T, P):
    mini = 1e10
    maxi = -1e10
    l = len(P)

    for i in range(
        l
    ):  # Znajdujemy najmniejszy i najwiekszy element we wszystkich przedzialach prawdopodobienstwa
        tuplee = P[i]
        if tuplee[0] < mini:
            mini = tuplee[0]
        if tuplee[1] > maxi:
            maxi = tuplee[1]

    tab = [[i, i + 1, 0] for i in range(mini, maxi)]  # tablica przedzialow
    # print(tab)

    for i in range(l):  # prawdopodobienstwa wylosowania liczby z kazdego przedzialu
        tuplee = P[i]
        low = tuplee[0]
        high = tuplee[1]
        proability = (1 / (high - low)) * tuplee[2]

        for j in range(low - 1, high - 1):
            tab[j][2] += proability

    n = len(T)
    # print(tab)
    buckets = [
        [] for j in range(int(tab[i][2] * n) * (maxi - mini))
    ]  # tworzenie talicy wiader zgodnie z prawdopodobienstwem
    # print(buckets)

    for i in range(n):
        el = T[i]
        low = floor(el)
        print(el, low)
        buckets[low - 1].append(el)  # append ma zlozonosc O(1) wiec calosc O(n)

    # print(buckets)

    # Jezeli kubelki maja 1-2 elementy to przepisywanie elementow jest O(n)
    final_array = [0] * n
    p = 0
    for bucket in buckets:
        d = len(bucket)
        if d > 1:
            for i in range(1, d):
                for j in range(i, 0, -1):
                    if bucket[j] < bucket[j - 1]:
                        bucket[j], bucket[j - 1] = bucket[j - 1], bucket[j]
                    else:
                        break

        for s in range(d):
            final_array[p] = bucket[s]
            p += 1

    return final_array

    # Calosc O(n) jezeli liczby sa generowane zgodnie z warunkami przedstawionymi w zadaniu


print(SortTab(T, P))
