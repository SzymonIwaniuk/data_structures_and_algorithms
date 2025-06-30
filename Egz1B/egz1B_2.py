from egz1Btesty import runtests
'''
Szymon Iwaniuk
Moje rozwiazanie opiera sie na tym, iz z tresci zadania wynika ze jest to DAG, wiec buduje i sortuje graf
topologicznie, a nastepnie od tylu sprawdzam czy istnieja mosty w aktualnym potgrafie od wierzcholka i,
jezeli tak to uzupelniam slownik na mosty i update'tuje licznik na koncu zwracam liczbe mostow.
Zlozonosc rozwiazania szacuje na czyli O(EV + V^2).
'''

def critical(V, E):
    def build_graph(E, V):
        graph = [[] for _ in range(V)]
        for u, v in E:
            graph[u].append(v)
        return graph

    graph = build_graph(E, V)

    def lengauer_tarjan_dominator(graph, s):
        V = len(graph)
        semi = [0] * V
        idom = [-1] * V
        parent = [-1] * V
        vertex = [0] * V
        label = list(range(V))
        ancestor = [-1] * V
        bucket = [[] for _ in range(V)]
        time = 0

        def dfs(v):
            nonlocal time
            time += 1
            semi[v] = time
            vertex[time - 1] = v
            for w in graph[v]:
                if semi[w] == 0:
                    parent[w] = v
                    dfs(w)

        dfs(s)

        def compress(u):
            if ancestor[ancestor[u]] != -1:
                compress(ancestor[u])
                if semi[label[ancestor[u]]] < semi[label[u]]:
                    label[u] = label[ancestor[u]]
                ancestor[u] = ancestor[ancestor[u]]

        def eval(u):
            if ancestor[u] == -1:
                return label[u]
            else:
                compress(u)
                if semi[label[u]] < semi[label[ancestor[u]]]:
                    return label[u]
                else:
                    return label[ancestor[u]]

        for i in range(time - 1, 0, -1):
            w = vertex[i]
            for v in graph[w]:
                if semi[v] == 0:
                    continue
                u = eval(v)
                if semi[u] < semi[w]:
                    semi[w] = semi[u]
            bucket_vertex = vertex[semi[w] - 1]
            bucket[bucket_vertex].append(w)
            ancestor[w] = parent[w]
            for v in bucket[parent[w]]:
                u = eval(v)
                if semi[u] < semi[v]:
                    idom[v] = u
                else:
                    idom[v] = parent[w]
            bucket[parent[w]].clear()

        for i in range(1, time):
            w = vertex[i]
            if idom[w] != vertex[semi[w] - 1]:
                idom[w] = idom[idom[w]]

        idom[s] = -1

        critical = set()
        for v in range(V):
            if idom[v] != -1:
                critical.add((idom[v], v))

        return critical

    all_critical_edges = set()
    for s in range(V):
        critical = lengauer_tarjan_dominator(graph, s)
        all_critical_edges.update(critical)

    return len(all_critical_edges)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)
