from egz1Btesty import runtests

"""
Szymon Iwaniuk
Moje rozwiazanie opiera sie na tym, iz z tresci zadania wynika ze jest to DAG, wiec buduje i sortuje graf
topologicznie, a nastepnie od tylu sprawdzam czy istnieja mosty w aktualnym potgrafie od wierzcholka i,
jezeli tak to uzupelniam slownik na mosty i update'tuje licznik na koncu zwracam liczbe mostow.
Zlozonosc rozwiazania szacuje na czyli O(EV + V^2).
"""


def bridges(graph, V, u):
    time = 0

    parents = [None] * V
    d = [float("inf")] * V
    low = [float("inf")] * V
    bridges = []

    def dfs_visit(graph, u):
        nonlocal time

        d[u] = time
        low[u] = time

        time += 1

        for v in graph[u]:
            if d[v] == float("inf"):
                parents[v] = u
                low[u] = min(low[u], dfs_visit(graph, v))

            elif v != parents[u]:
                low[u] = min(low[u], d[v])

        if low[u] == d[u] and parents[u] != None:
            bridges.append((u, parents[u]))

        return low[u]

    dfs_visit(graph, u)

    return bridges


def toposort(graph, V):
    reversed_array = []

    def dfs_visit(graph, v):
        for u in graph[v]:
            if visited[v] == False:
                visited[u] = True
                dfs_visit(graph, u)

        reversed_array.append(v)

    visited = [False] * V

    for i in range(V):
        if visited[i] == False:
            visited[i] = True
            dfs_visit(graph, i)

    return reversed_array


def build_graph(E, V):
    graph = [[] for i in range(V)]

    for u, v in E:
        graph[u].append(v)

    return graph


def build_graph(E, V):
    graph = [[] for i in range(V)]

    for u, v in E:
        graph[u].append(v)

    return graph


def critical(V, E):
    n = len(E)
    graph = build_graph(E, V)
    sorted_vertex = toposort(graph, V)
    # print(sorted_vertex)
    bridges_cnt = 0
    bridges_dict = {}

    for i in sorted_vertex[::-1]:
        bridges_cur = bridges(graph, V, i)
        print(bridges_cur)

        for u, v in bridges_cur:
            if (u, v) not in bridges_dict:
                bridges_dict[(u, v)] = 1
                bridges_cnt += 1

    return bridges_cnt

    # return bridges(graph, V)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests=True)
