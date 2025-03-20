from zad2testy import runtests
'''
Algorytmy i Struktury Danych
Zadanie offline 2 (19.III.2025)
Format rozwiązań
Jak w zadaniu nr 1.
Testowanie rozwiązań
Żeby przetestować rozwiązanie zadania, należy wykonać polecenie: python zad2.py
Dana jest tablica T zawierająca liczby naturalne. Proszę napisać funkcję count inversions(T),
która dla tablicy zwraca liczbę inwersji w tablicy.
Na przykład dla wejścia:
T = [1,20,6,4,5]
wywołanie count inversion(T) powinno zwrócić 5. Algorytm powinien być możliwie jak najszyb-
szy. Proszę podać złożoność czasową i pamięciową zaproponowanego algorytmu.
'''
class BSTNode:
    def __init__ (self, val=None, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left
        self.smaller = 0



def count_inversions(A):
    l = len(A)
    root = BSTNode(A[0])
    suma = 0

    for i in range(1,l):
        cur = root
        self_inv = 0
        #print(A[i])

        while True:

            if A[i] < cur.val:
                cur.smaller += 1

                if cur.left != None:
                    cur = cur.left
                else:
                    cur.left = BSTNode(A[i])
                    break

            else:
                self_inv += cur.smaller

                if A[i] > cur.val:
                    self_inv += 1
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = BSTNode(A[i])
                    break

        suma += self_inv
    return suma
T = [1,20,6,4,5]
#print(count_inversions(T))







# Odkomentuj by uruchomic duze testy
runtests( count_inversions, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
#runtests( count_inversions, all_tests=False )
