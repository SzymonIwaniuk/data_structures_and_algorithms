from kol3testy import runtests

def parkiet(B, C, s):
    n = len(B)
    m = len(B[0])

    i,j=0,0
    while(i<n-1 and j<m-1):
        ile_sekow_poz = C[i][j]-C[i+1][j]
        if(ile_sekow_poz<=s):   # deski poziome <- priorytet
            i+=1
        elif(C[i][j]-C[i][j+1]<=s): # deski pionowe
            j+=1
        else:
            return -1   #nie da sie odciac deski

    # print(i,j)

    if(i!=n-1):
        while(i<n-1):
            if(C[i][j]>s):  # w pozostałej desce jest za dużo sęków
                i+=1
            else:
                break   #to co zostało jest akceptowalne
    if(j!=m-1):
        while(j<m-1):
            if(C[i][j]>s):
                j+=1
            else:
                break

    if(C[i][j]>s):  #odcielismy ile mozemy i dalej nie spełnia warunku
        return -1

    wynik1 = i+j
    i,j=0,0
    while(i<n-1 and j<m-1):
        ile_sekow_poz = C[i][j]-C[i+1][j]
        if(C[i][j]-C[i][j+1]<=s): # deski pionowe <- priorytet
            j+=1
        elif(ile_sekow_poz<=s):   # deski poziome
            i+=1
        else:
            return -1   #nie da sie odciac deski

    # print(i,j)

    if(i!=n-1):
        while(i<n-1):
            if(C[i][j]>s):  # w pozostałej desce jest za dużo sęków
                i+=1
            else:
                break   #to co zostało jest akceptowalne
    if(j!=m-1):
        while(j<m-1):
            if(C[i][j]>s):
                j+=1
            else:
                break

    if(C[i][j]>s):  #odcielismy ile mozemy i dalej nie spełnia warunku
        return -1

    return min(i+j,wynik1)

runtests(parkiet, all_tests = True)