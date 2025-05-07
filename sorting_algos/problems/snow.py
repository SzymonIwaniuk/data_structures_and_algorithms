"""
System chłodzenia serwerów na pewnej uczelni wymaga stałych dostaw śniegu. Grupa zmotywowa-
nych profesorów odnalazła w wysokich górach wąwóz, z którego można przywieźć śnieg. Wąwóz jest
podzielony na n obszarów i ma wjazdy z zachodu i wschodu. Na każdym obszarze wąwozu znajduje
się pewna ilość śniegu, opisana w tablicy S. W szczególności S[0] to liczba metrów sześciennych
śniegu bezpośrednio przy zachodnim wjeździe, S[1] to liczba metrów sześciennych śniegu na kolej-
nym obszarze, a S[n − 1] to liczba metrów sześciennych śniegu przy wjeździe wschodnim (wiadomo,
że zawartość tablicy S to liczby naturalne). Profesorowie dysponują maszyną, która danego dnia
może zebrać śnieg ze wskazanego obszaru, wjeżdżając odpowiednio z zachodu lub wschodu. Niestety,
są trzy komplikacje

1. Po drodze do danego obszaru maszyna topi cały śnieg na tych obszarach, po których prze-
jeżdża (o ile nie został wcześniej zebrany). Na przykład jadąc z zachodu do obszaru 2 zeruje
wartości S[0] oraz S[1] (bo po nich przejeżdża) oraz S[2] (bo ten śnieg zbiera).

2. Każdego dnia maszyna może zebrać śnieg tylko z jednego, dowolnie wybranego obszaru, wjeż-
dzając albo z zachodu albo ze wschodu.

3. Ze względu na wysoką temperaturę, po każdym dniu na każdym obszarze topi się dokładnie
jeden metr sześcienny śniegu.

Zadanie polega na zaimplementowaniu funkcji:
def snow( S ) która zwraca ile metrów sześciennych maksmalnie można zebrać z wąwozu (zebrany śnieg jest
zabezpieczany i już się nie topi).
Rozważmy następujące dane:
S = [1,7,3,4,1]
wywołanie snow(S) powinno zwrócić liczbę 11. Możliwy plan zbierania śniegu to: zebranie 7m3
pierwszego dnia z obszaru 1 wjeżdżając z zachodu, zebranie 3m3 drugiego dnia z obszaru 3
wjeżdżając ze wschodu (1m3 się stopił po pierwszym dniu), oraz zebranie 1m3 trzeciego dnia
z obszaru 2 wjeżdżając z dowolnego kierunku (po dwóch dniach ilość śniegu na tym obszarze
zmniejszy się z 3m3 do 1m3).
Zadanie można rozwiązać w czasie O(n log n), gdzie n to rozmiar wąwozu
"""


def parent(i: int) -> int:
    return (i - 1) // 2


def left(i: int) -> int:
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def heapify(T: list, i: int, n: int) -> any:
    max_ind = i
    l = left(i)
    r = right(i)

    if l < n and T[max_ind] < T[l]:
        max_ind, l = l, max_ind

    if r < n and T[max_ind] < T[r]:
        max_ind, r = r, max_ind

    if max_ind != i:
        T[max_ind], T[i] = T[i], T[max_ind]
        heapify(T, max_ind, n)


def buildheap(T: list) -> any:
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, i, n)


def snow(S: list) -> int:
    n = len(S)
    tmp = 0
    suma = 0
    ind = n
    buildheap(S)

    while S[0] - tmp > 0 and n - tmp > 0:

        suma += S[0] - tmp
        ind -= 1
        S[0], S[ind] = S[ind], S[0]
        tmp += 1
        heapify(S, 0, ind)

    return suma
