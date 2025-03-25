from math import log10
from random import randint


def digits(n):
    return int(log10(n)) + 1


def countingsort(A, divisor):
    counter_length = 10
    n = len(A)
    counter = [0] * counter_length

    for num in A:
        counter[(num // divisor) % 10] += 1

    for i in range(1, counter_length):
        counter[i] += counter[i - 1]

    output = [0] * n
    for i in range(n - 1, -1, -1):
        output[counter[(A[i] // divisor) % 10] - 1] = A[i]
        counter[(A[i] // divisor) % 10] -= 1

    for i in range(n):
        A[i] = output[i]


def radixsort(A):
    if not A:
        return A

    k = digits(max(A))

    for i in range(k):
        countingsort(A, 10**i)

    return A


A = [randint(1, 101) for _ in range(15)]
print(A)
print(radixsort(A))
