def partition(A, low, high):
    pivot = A[high]
    i = low - 1

    for j in range(low,high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[high] = A[high], A[i+1]
    return i+1

def quicksort(A,low,high):
    if low < high:
        pivot_index = partition(A,low,high)
        quicksort(A,low,pivot_index - 1)
        quicksort(A,pivot_index + 1, high)


A = [7,2,1,6,8,5,3,4,32,2,3,3]

quicksort(A,0,len(A)-1)
print(A)
