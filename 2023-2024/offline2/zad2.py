from zad2testy import runtests

def partition(A, low, high):
    pivot = A[high]
    i = low - 1

    for j in range(low,high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[high] = A[high], A[i+1]
    return i+1

def quickselect(A, low, high, k):
    if low <= high:
        pivot_index = partition(A, low, high)
        if pivot_index == k:
            return A[pivot_index]
        elif pivot_index < k:
            return quickselect(A, pivot_index + 1, high, k)
        else:
            return quickselect(A, low, pivot_index - 1, k)



def ksum(T, k, p):
    n = len(T)
    suma =  0
    prev_r = None
    prev = None
    for i in range(n - p + 1):
        A = T[i:i+p]
        lval = A[p-1]

        if prev_r == None:
            # print(A)
            # print(quickselect(A,0,p-1,k))
            prev_r = A[0]
            b = quickselect(A,0,p-1,p-k)
            suma += b
            prev = b

        elif lval > prev and prev_r > prev:
            suma += prev
            prev_r = A[0]
        elif lval < prev and prev_r < prev:
            suma += prev
            prev_r = A[0]
        else:
            prev_r = A[0]
            b = quickselect(A,0,p-1,p-k)
            suma += b
            prev = b

    return suma

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )

