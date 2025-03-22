from math import floor
from quicksort import quicksort

def bucketsort(T):
    l = len(T)
    buckets = [[] for i in range(l)]

    for i in range(l):
        index = int(l * T[i])
        buckets[index].append(T[i])

    for bucket in buckets:
        quicksort(bucket,0,len(bucket)-1)

    index = 0
    for bucket in buckets:
        for num in bucket:
            T[index] = num
            index += 1

    return T


T = [0.1 , 0.3 , 0.2, 0.2, 0.5 , 0.4 , 0.7 , 0.9 , 0.8 , 0.6 , 0.0]
print(bucketsort(T))

