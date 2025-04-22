"""
Cesarzowa Bajtocji zgubiła w napisie s swój ulubiony palindrom. Cesarzowa nikomu nie mówiła jaki
jest jej ulubiony palindrom i wiadomo jedynie, że jest bardzo długi oraz składa się z nieparzystej
liczby liter alfabetu łacińskiego. Postanowiono odnaleźć zaginiony palindrom cesarzowej. W tym
celu należy zaimplementować funkcję:
def ceasar( s )
która na wejściu otrzymuje słowo s (składające się wyłącznie z małych liter alfabetu łacińskiego)
i zwraca długość najdłuższego spójnego podsłowa, które jest palindromem i którego długość
jest nieparzysta. Użyty algorytm powinien być możliwie jak najszybszy. Proszę uzasadnić jego
poprawność i oszacować złożoność obliczeniową.
Przykład. Dla słowa:
akontnoknonabcddcba
wynikiem jest 7 (kontnok; proszę zwrócić uwagę, że abcddcba jest dłuższym palindromem, ale jest
długości parzystej więc na pewno nie jest zagubionym palindromem cesarzowej)
"""


def ceasar(s):
    n = len(s)
    max_lenght = 0

    for mid in range(1, n - 1):
        maxi = min(mid, abs(n - 1 - mid))
        lenght = 2 * maxi + 1
        i = mid - maxi
        j = mid + maxi

        while i != j:
            if s[i] != s[j]:
                lenght -= 2

            i += 1
            j -= 1

        max_lenght = max(max_lenght, lenght)

    # O(n^2)

    return max_lenght


print(ceasar("akontnoknonabcddcba"))
