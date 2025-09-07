from zad1testy import runtests

def build_graph(I, n):
    graph = {}

    for i in range(n):
        a, b = I[i]
        if a not in graph:
            graph[a] = set()
        graph[a].add(i)

        if b not in graph:
            graph[b] = set()
        graph[b].add(i)

    return graph

def dfs(graph, start, I):
    visited_intervals = set()
    visited_points = set()

    def dfs_visit(p):
        if p in visited_points:
            return
        visited_points.add(p)
        for i in graph[p]:
            if i not in visited_intervals:
                visited_intervals.add(i)
                a, b = I[i]
                dfs_visit(a)
                dfs_visit(b)

    dfs_visit(start)
    return visited_intervals

def intuse( I, x, y ):
    """tu prosze wpisac wlasna implementacje"""
    n = len(I)
    graph = build_graph(I, n)
    usefull = []

    from_x = dfs(graph, x, I)

    from_y = dfs(graph, y, I)

    # print(from_x, from_y)
    usefull = list(from_x & from_y)

    return usefull


runtests( intuse )


