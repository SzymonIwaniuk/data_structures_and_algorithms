import numpy as np

'''
Kopiec dla tablicy przechowujacej ilosc elementow na indeksie "0"
'''

def left(i):
    return 2*i

def right(i):
    return 2*i+1

def parent(i):
    return i//2

#Wstawiamy element na koniec kopca i jezeli jest ne > parent wynosimy go do gory
def insert(T, ne):
    n = len(T)

    T[0] += 1
    ind = T[0]

    if n == T[0]:
        return
    else:
        T[ind] = ne

    while ind > 1 and T[ind] > T[parent(ind)]:
        T[ind], T[parent(ind)] = T[parent(ind)], T[ind]
        ind = parent(ind)

arr = np.empty(10)
T = [8,3,4,1,5,6]
for i in range(len(T)):
    arr[i] = T[i]
insert(arr,5)
print(arr)

