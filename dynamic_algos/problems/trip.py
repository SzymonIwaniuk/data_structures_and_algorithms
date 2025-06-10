def trip(M):
    m = len(M)
    n = len(M[0])

    memo = [[float('-inf') for _ in range(n)] for _ in range(m)]
    moves = [(-1,0), (0,-1), (1,0), (0,1)]
    steps = 0

    def dfs(i,j,s):
        nonlocal steps
        steps = max(steps, s)
        print(i, j)
        memo[i][j] = max(memo[i][j], s)

        for x, y in moves:
            ni = i + x
            nj = j + y

            if 0 <= ni < m and 0 <= nj < n and s >= memo[ni][nj]:
                dfs(ni, nj, s + 1)



    for i in range(m):
        for j in range(n):
            dfs(m,n,1)

    return steps

if __name__ == '__main__':
    M = [ [7,6,5,12],
        [8,3,4,11],
        [9,1,2,10] ]

    print(trip(M))


