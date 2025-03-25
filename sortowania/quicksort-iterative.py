def quicksort_iterative(T, l, r):

    size = r - l + 1
    stack = [0] * (size)
    top = 0

    stack[top] = l
    top += 1
    stack[top] = r

    while top >= 0:

        r = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(T, l, r)

        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        if p + 1 < r:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = r


def partition(T, l, r):
    pivot = T[r]
    i = l - 1

    for j in range(l, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


T = [2, 3, 5, 6, 9, 1, 4, 10, 18]

quicksort_iterative(T, 0, 8)
print(T)
