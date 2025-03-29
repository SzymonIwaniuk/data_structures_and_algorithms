"""
Wierzcholek v w grafie skierowanym nazywamy tak zwanym dobrym
poczatkiem jezeli kazdy i inny wierzcholek mozna osiagnac sciezka
skierowana wychodzaca z v. Zaproponowac algorytm, ktory dla podanego
grafu stwierdza czy G posiada dobry poczatek; lista sasiedztwa;
"""


def beginning(G):
    def dfs_visit(i):
        nonlocal G, times, time, visited
        visited[i] = True

        for v in G[i]:
            if not visited[v]:
                dfs_visit(v)

        time += 1
        times[i] = time

    n = len(G)
    times = [-1 for _ in range(n)]
    time = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            dfs_visit(i)

    for i in range(n):
        if times[i] == n:
            s = i
            break

    visited = [False for _ in range(n)]
    time = 0
    dfs_visit(s)
    return time == n
