from egz3atesty import runtests


def snow(T, I):
    A = []
    for x,y in I:
        A.append((x,0))
        A.append((y,1))
    A.sort()

    n = len(A)
    sol, cnt = 0, 0
    for i in range(n):
        if A[i][1] == 0: cnt+=1
        else: cnt-=1
        sol = max(sol, cnt)

    return sol



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
