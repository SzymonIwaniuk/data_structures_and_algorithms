from egz3btesty import runtests

def binarysearch(P, left):
    pass

def uncool(P):
    n = len(P)
    P = list(enumerate(P))
    P.sort(key=lambda x: (x[1][0], x[1][1]))
    # prev = None
    # indexes = []
    # j = -1

    # for i in range(n):
    #     num = P[i][1][0]
    #     if num != prev:
    #         indexes.append(i)
    #         j += 1
    #     else:
    #         indexes[j] += 1
    #     prev = num

    #print(indexes)

    for i in range(n - 1):
        ind_i = P[i][0]

        a_1, b_1 = P[i][1]
        #left = indexes[i + 1]
        for j in range(i + 1, n):
            ind_j = P[j][0]
            a_2, b_2 = P[j][1]

            if a_1 < b_2 and a_2 < b_1 and a_1 < a_2 and b_1 < b_2:
                #print(a_1, b_1)
                #print(a_2, b_2)
                return (ind_i, ind_j)





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(uncool, all_tests=True)
