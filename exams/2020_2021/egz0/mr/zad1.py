from zad1testy import runtests

def mr(X):
    n = len(X)

    lds = [1] * n
    lds_parent = [None] * n
    for i in range(n):
        for j in range(i):
            if X[j] > X[i] and lds[j] + 1 > lds[i]:
                lds[i] = lds[j] + 1
                lds_parent[i] = j

    lis = [1] * n
    lis_parent = [None] * n
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if X[j] > X[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1
                lis_parent[i] = j


    max_l = 0
    index = 0
    for i in range(n):
        l = lds[i] + lis[i] - 1
        if l > max_l:
            max_l = l
            index = i

    left_part = []
    idx = index
    while idx is not None:
        left_part.append(X[idx])
        idx = lds_parent[idx]
    left_part.reverse()

    right_part = []
    idx = lis_parent[index]
    while idx is not None:
        right_part.append(X[idx])
        idx = lis_parent[idx]

    return left_part + right_part


runtests(mr)
