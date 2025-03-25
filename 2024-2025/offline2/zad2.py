from zad2testy import runtests

"""
Dana jest tablica T zawierająca liczby naturalne. Proszę napisać funkcję count inversions(T),
która dla tablicy zwraca liczbę inwersji w tablicy.
Na przykład dla wejścia:
T = [1,20,6,4,5]
wywołanie count inversion(T) powinno zwrócić 5. Algorytm powinien być możliwie jak najszyb-
szy. Proszę podać złożoność czasową i pamięciową zaproponowanego algorytmu.
"""

# 1----------------------------------------------------------------------------->
# class BSTNode:
#     def __init__ (self, val=None, right=None, left=None):
#         self.val = val
#         self.right = right
#         self.left = left
#         self.smaller = 0


# def count_inversions(A: list) -> int:
#     l = len(A)
#     root = BSTNode(A[0])
#     suma = 0

#     for i in range(1,l):
#         cur = root
#         self_inv = 0
#         #print(A[i])

#         while True:

#             if A[i] < cur.val:
#                 cur.smaller += 1

#                 if cur.left != None:
#                     cur = cur.left
#                 else:
#                     cur.left = BSTNode(A[i])
#                     break

#             else:
#                 self_inv += cur.smaller

#                 if A[i] > cur.val:
#                     self_inv += 1
#                 if cur.right != None:
#                     cur = cur.right
#                 else:
#                     cur.right = BSTNode(A[i])
#                     break

#         suma += self_inv
#     return suma
# T = [1,20,6,4,5]
# #print(count_inversions(T))

# 2------------------------------------------------------------------------------>


def merge(A: list, l: int, r: int) -> int:
    global INV_CNT

    mid = (l + r) // 2
    len1 = mid - l + 1
    len2 = r - mid
    l_A = A[l : mid + 1]
    r_A = A[mid + 1 : r + 1]
    l_ind = r_ind = 0
    main_ind = l

    while l_ind < len1 and r_ind < len2:
        if l_A[l_ind] <= r_A[r_ind]:
            A[main_ind] = l_A[l_ind]
            l_ind += 1
        else:
            A[main_ind] = r_A[r_ind]
            INV_CNT += len1 - l_ind
            r_ind += 1

        main_ind += 1

    while l_ind < len1:
        A[main_ind] = l_A[l_ind]
        main_ind += 1
        l_ind += 1

    while r_ind < len2:
        A[main_ind] = r_A[r_ind]
        main_ind += 1
        r_ind += 1


def mergesort(A, l, r):
    if l < r:
        mid = (l + r) // 2
        mergesort(A, l, mid)
        mergesort(A, mid + 1, r)
        merge(A, l, r)


def count_inversions(A):
    global INV_CNT
    INV_CNT = 0
    mergesort(A, 0, len(A) - 1)
    return INV_CNT


# T = [1,21,3,5,4]
# print(count_inversions(T))

# Odkomentuj by uruchomic duze testy
runtests(count_inversions, all_tests=True)

# Zakomentuj gdy uruchamiasz duze testy
# runtests( count_inversions, all_tests=False )
