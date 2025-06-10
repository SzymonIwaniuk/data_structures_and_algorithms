def binsearch(seq, num):
    l = len(seq)
    i = 0
    j = l - 1

    while i <= j:
        print(j ,i)
        mid = (i + j) // 2

        if seq[mid] > num:
            j = mid - 1

        else:
            i = mid + 1

    return i


def mosty(T):
    n = len(T)
    mosty = sorted(T, key = lambda x:(x[0], x[1]))
    mosty_2 = [mosty[i][1] for i in range(n)]
    seq = [mosty_2[0]]

    for i in range(1,n):
        if mosty_2[i] >= seq[-1]:
            seq.append(mosty_2[i])

        else:
            ind = binsearch(seq, mosty_2[i])
            seq[ind] = mosty_2[i]


    return len(seq)


if __name__ == '__main__':
    M = [(1, 2), (2, 3), (2, 4), (3, 0)]
    print(mosty(M))
