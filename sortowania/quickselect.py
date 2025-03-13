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



A = [7,2,1,6,8,5,3,4,1,32,2,3,3]

print(quickselect(A,0,len(A) - 1, 1))
print(A)