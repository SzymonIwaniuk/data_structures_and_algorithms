"""
Dany jest ciąg przedziałów domkniętych L = [[a1, b1], . . . , [an, bn]]. Początki i końce przedziałów
są liczbami naturalnymi. Poziomem przedziału c ∈ L nazywamy liczbę przedziałów w L, które w
całości zawierają się w c (nie licząc samego c). Proszę zaproponować i zaimplementować algorytm,
który zwraca maksimum z poziomów przedziałów znajdujących się w L. Proszę uzasadnić popraw-
ność algorytmu i oszacować jego złożoność obliczeniową.
Algorytm należy zaimplementować jako funkcję postaci:
def depth( L ):
...
która przyjmuje listę przedziałów L i zwraca maksimum z poziomów przedziałów w L.
Przykład. Dla listy przedziałów:
L = [ [1, 6],
[5, 6],
[2, 5],
[8, 9],
[1, 6]]
wynikiem jest liczba 3.
"""

L = [[1, 6], [5, 6], [2, 5], [8, 9], [1, 6]]


def partition(T, l, r):
    i = l - 1

    for j in range(l, r):
        if T[j][0] < T[r][0]:
            i += 1
            T[i], T[j] = T[j], T[i]

        elif T[j][0] == T[r][0]:
            if T[j][1] >= T[r][1]:
                T[i], T[j] = T[j], T[i]
                i += 1

        T[i + 1], T[r] = T[r], T[i + 1]

        return i + 1


def quicksort(T, l, r):
    if l < r:
        q = partition(T, l, r)
        quicksort(T, l, q - 1)
        quicksort(T, q + 1, r)


def depth(L):
    P = L.copy()
    n = len(P)

    quicksort(P, 0, n - 1)
    print(P)

    cnt = -1
    maxi = 0
    current = P[0]

    for x, y in P:
        if current[1] >= y:
            cnt += 1
        else:
            maxi = max(cnt, maxi)
            cnt = 0
            current = [x, y]

    return maxi


print(depth(L))
