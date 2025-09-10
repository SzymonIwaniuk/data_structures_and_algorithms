from zad1testy import runtests


def bisect(seq, num, top):
    l = 0
    r = top

    while l < r:
        mid = (l + r) // 2

        if seq[mid][0] == num:
            return mid
        elif seq[mid][0] < num:
            r = mid
        else:
            l = mid + 1

    return l


def mr(X):
    n = len(X)

    lds = [1] * n
    lds_parent = [None] * n
    stack_lds = [(X[0], 0)]
    top_lds = 1

    for i in range(1, n):
        if X[i] < stack_lds[-1][0]:
            top_lds += 1
            lds[i] = top_lds
            lds_parent[i] = stack_lds[-1][1]
            stack_lds.append((X[i], i))

        else:
            j = bisect(stack_lds, X[i], top_lds - 1)
            stack_lds[j] = (X[i], i)
            lds[i] = j

            if j > 0:
                #print(lds_parent[i], stack_lds[j-1][1])
                lds_parent[i] = stack_lds[j-1][1]


    lis = [1] * n
    lis_parent = [None] * n
    stack_lis = [(X[-1], n-1)]
    top_lis = 1

    for i in range(n-2, -1, -1):
        if X[i] < stack_lis[-1][0]:
            top_lis += 1
            lis[i] = top_lis
            lis_parent[i] = stack_lis[-1][1]
            stack_lis.append((X[i], i))

        else:
            j = bisect(stack_lis, X[i], top_lis - 1)
            # print(stack_lis, j, X[i])
            stack_lis[j] = (X[i], i)
            lis[i] = j

            if j > 0:
                #print(lis_parent[i], stack_lis[j-1][1])
                lis_parent[i] = stack_lis[j-1][1]

    #print(stack_lis)

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
