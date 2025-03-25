def counting_sort(A):
    mini = min(A)
    k = max(A) - min(A) + 1
    count = [0] * k

    for element in A:
        count[element - mini] += 1

    res = []

    for i in range(len(count)):
        el = [i] * count[i]
        res += el

    return res


A = [7, 2, 1, 3, 4, 5, 0, 6]

print(counting_sort(A))
