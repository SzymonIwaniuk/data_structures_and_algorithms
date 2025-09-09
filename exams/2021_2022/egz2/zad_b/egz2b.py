from egz2btesty import runtests

inf = float('-inf')

def magic( C ):
    n = len(C)
    dp = [-1] * n
    dp[0] = 0

    for i in range(n):
        cur_comnat = i
        chest = C[i][0]

        for j in range(1, 4):
            next_comnat = C[i][j][1]
            how_much_should_be = C[i][j][0]
            #print(cur_comnat, chest, next_comnat, how_much_should_be)
            #print(dp[cur_comnat])
            if next_comnat > cur_comnat and\
                dp[cur_comnat] != -1 and\
                chest - how_much_should_be <= 10:
                dp[next_comnat] = max(
                    dp[next_comnat],
                    dp[cur_comnat] + chest - how_much_should_be
                    )

    return dp[-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
