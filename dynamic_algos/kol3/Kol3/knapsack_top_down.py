def knapsack_top_down(P, B):
    n = len(P)
    dp = [False for _ in range(B+1)]

    def knapsack(b):
        if b == 0 or dp[b] == True:
            return True

        for i in range(n):
            if b - P[i] >= 0:
                if knapsack(b - P[i]):
                    dp[b] = True
                    return True

    if knapsack(B):
        return True
    return False

print(knapsack_top_down([3,3], 5))



