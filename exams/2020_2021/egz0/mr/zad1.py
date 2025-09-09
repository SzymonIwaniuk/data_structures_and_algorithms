from zad1testy import runtests

def mr( X ):
    n = len(X)
    left = [[1, 0] for _ in range(n)] # decreasing
    right = [[1, 0] for _ in  range(n)] # increasing

    for i in range(1, n):
        if X[i-1] > X[i]:
            left[i][0] = left[i-1][0] + 1
            left[i][1] = left[i-1][1]
        else:
            left[i][0] = left[i-1][0]
            left[i][1] = left[i-1][1] + 1

    for i in range(n-2,-1,-1):
        if X[i+1] > X[i]:
            right[i][0] = right[i+1][0] + 1
            right[i][1] = right[i+1][1]
        else:
            right[i][0] = right[i+1][0]
            right[i][1] = right[i+1][1] + 1


    max_len = 0
    peak = 0
    for i in range(n):
        length = left[i][0] + right[i][0] - 1
        if length > max_len:
            max_len = length
            peak = i

    res = []

    # malejąca część
    i = peak
    dec_count = left[peak][0]
    while dec_count > 0:
        res.append(X[i])
        # pomijamy elementy zgodnie z left[i][1]
        if left[i][1] > 0:
            i -= left[i][1] + 1
        else:
            i -= 1
        dec_count -= 1
    res = res[::-1]  # odwróć malejącą część

    # rosnąca część (bez szczytu)
    i = peak + 1
    inc_count = right[peak][0] - 1
    while inc_count > 0:
        res.append(X[i])
        if right[i][1] > 0:
            i += right[i][1] + 1
        else:
            i += 1
        inc_count -= 1

    return res

runtests( mr )