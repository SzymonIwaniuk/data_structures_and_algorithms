def inwerstor(T):
    maxi = 0
    n = len(T)

    for i in range(n-1):
        tmp = T[i]
        for j in range(i+1, n):
            tmp = min(tmp, T[j])
            print(i,j,tmp,j-i + 1)
            current = tmp * (j - i + 1)
            maxi = max(maxi, current)


    return maxi

T = [2, 1, 5, 6, 2, 3]

print(inwerstor(T))


def zad(T):
    n=len(T)
    maxi=0
    for i in range(n-1):
        min=T[i]
        for j in range(i+1,n):
            if T[j]< min:
                min=T[j]
            print(i,j,min,j-i + 1)
            suma=(j-i+1)*min
            print(suma)
            if suma>maxi:
                maxi=suma
    return maxi

T=[2,1,5,6,2,3]
print(zad(T))