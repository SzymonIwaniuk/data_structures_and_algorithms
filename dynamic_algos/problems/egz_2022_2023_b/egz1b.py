from egz1btesty import runtests

INF = float('inf')

def planets( D, C, T, E ):
    # tu prosze wpisac wlasna implementacje
    n = len(D)
    dp = [[INF] * (E+1) for i in range(n)]

    # edge case
    for i in range(E+1):
        dp[0][i] = i * C[0]


    for planet in range(n):
        for fuel in range(E+1):
            if dp[planet][fuel] == INF:
                continue

            if fuel < E:
                if dp[planet][fuel+1] > dp[planet][fuel] + C[planet]:
                    dp[planet][fuel+1] = dp[planet][fuel] + C[planet]

            for next_planet in range(planet + 1, n):
                dist = D[next_planet] - D[planet]
                if dist > fuel:
                    break

                if dp[next_planet][fuel - dist] > dp[planet][fuel]:
                    dp[next_planet][fuel - dist] = dp[planet][fuel]

            if fuel == 0:
                target, price = T[planet]
                if target >= planet:
                    if dp[target][0] > dp[planet][0] + price:
                        dp[target][0] = dp[planet][0] + price

    #for i in range(n):
        #print(dp[i])

    return min(dp[n-1])



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
