def maze(L):
    n = len(L)
    memo1 = [[float('-inf') for _ in range(n)] for _ in range(n)]
    memo2 = [[False for _ in range(n)] for _ in range(n)]
    memo2[0][0] = True
    moves = [(1,0), (-1,0), (0,1)]


    def dfs(i, j, steps):
        memo1[i][j] = steps
        #print(i,j,steps)
        for x, y in moves:
            if 0 <= i + x < n and 0 <= j + y < n and memo1[i+x][j+y] < memo1[i][j]:
                if L[i+x][j+y] == '.' and memo2[i+x][j+y] is False:
                    memo2[i+x][j+y] = True
                    dfs(i + x, j + y, steps + 1)
                    memo2[i+x][j+y] = False


    dfs(0,0,0)

    for i in range(n):
        print(memo1[i])
    return - 1 if memo1[n-1][n-1] == float('-inf') else memo1[n-1][n-1]

L = [ "....",
      "..#.",
      "..#.",
      "...." ]

L2 = ['....#...##',
     '...#....##',
     '#.........',
     '.......#..',
     '.......##.',
     '...#....#.',
     '#....#....',
     '##.....#.#',
     '..........',
     '......#...']
#print(maze(L))
print(maze(L2))