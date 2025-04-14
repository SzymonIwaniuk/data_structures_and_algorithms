# 4 Wierzcholek v jest dobrym poczatkiem jezli w grafie skierowanym mozna z niego dotrzec do kazdego innego wierzcholka. Wyznacz dobry poczatek.

"""
Zauwazamy ze kandydatem na dobry poczatek jest wierzcholek z najwyzszym czasem odwiedzenia w dfs,
poniewaz jezeli sprawdzamy wierzcholek ktory nie jest dobrym poczatkiem to przypiszemu mu aktualny czas
i nic sie nie stanie, a jezeli sprawdzamy dobry poczatek to najpierw przypiszemy czasy pozostalym wierzcholkom,
a dopiero na koncu jemu samemu.
"""


def beginning(G: list[list[int]]) -> int:
    def dfs_visit(i: int) -> None:
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
    if time == n:
        return s
    else:
        None
