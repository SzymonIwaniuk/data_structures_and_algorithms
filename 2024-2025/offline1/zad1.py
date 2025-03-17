from zad1testy import runtests

def merge(left, mid, right, T):
    len_l = mid - left + 1
    len_r = right - mid
    left_T = T[left:mid+1]
    right_T = T[mid+1:right+1]
    left_ind = right_ind = 0
    main_ind = left

    while left_ind < len_l and right_ind < len_r:
        if left_T[left_ind] <= right_T[right_ind]:
            T[main_ind] = left_T[left_ind]
            left_ind += 1
        else:
            T[main_ind] = right_T[right_ind]
            right_ind += 1

        main_ind += 1

    while left_ind < len_l:
        T[main_ind] = left_T[left_ind]
        left_ind += 1
        main_ind += 1

    while right_ind < len_r:
        T[main_ind] = right_T[right_ind]
        right_ind += 1
        main_ind += 1

def mergesort(left, right, T):
    mid = (right + left) // 2
    if left < right:
        mid = (right + left) // 2
        mergesort(left, mid, T)
        mergesort(mid + 1, right, T)
        merge(left, mid, right, T)

    return T

#print(mergesort(0, len(T)-1, T))

def strong_string(T):
    n = len(T)

    #sprawdzenie czy wyraz badz jego revers jest wczesniej w kolejnosci leksykograficznej
    A = [0 for _ in range(n)]

    for i in range(n):
        word = T[i]
        if  word < word[::-1]:
            A[i] = word
        else:
            A[i] = word[::-1]


    sorted_A = mergesort(0, len(T)-1, A)

    power = maxi = 1
    for i in range(1,n):
        maxi = max(power, maxi)
        if sorted_A[i-1] == sorted_A[i]:
            power += 1
        else:
            power = 1

    return maxi


# Odkomentuj by uruchomic duze testy
runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
#runtests( strong_string, all_tests=True)

