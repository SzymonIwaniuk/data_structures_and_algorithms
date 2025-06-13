def gen_adjacency_list(n, m, M, ng):
    G = [[] for _ in range(ng)]
    trl = [[0] * m for _ in range(n)] # translacja

    k = 0
    for i in range(n):
        for j in range(m):
            trl[i][j] = k
            k += 1

    for i in range(n):
        for j in range(m):
            u = trl[i][j]
            if j - 1 > -1 and M[i][j - 1] > M[i][j]:
                G[u].append(trl[i][j - 1])
            if j + 1 < n and M[i][j + 1] > M[i][j]:
                G[u].append(trl[i][j + 1])
            if i - 1 > -1 and M[i - 1][j] > M[i][j]:
                G[u].append(trl[i - 1][j])
            if i + 1 < n and M[i + 1][j] > M[i][j]:
                G[u].append(trl[i + 1][j])

    return G


def toposort(G, n):
    visited = [False] * n
    sorted_graph = []

    def dfs_visit(G, u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                dfs_visit(G,v)

        sorted_graph.append(u)


    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)

    sorted_graph.reverse()
    return sorted_graph

def trip(M):
    n, m = len(M), len(M[0])
    ng = n * m
    G = gen_adjacency_list(n, m, M, ng)
    sorted = toposort(G, ng)
    F = [1] * ng

    for i in range(ng - 2, -1, -1): # dynamiczne
        u = sorted[i]
        for v in G[u]:
            if F[u] < F[v] + 1: F[u] = F[v] + 1

    res = 0
    for val in F:
        if val > res: res = val

    return res

if __name__ == '__main__':
    M = [ [7,6,5,12],
        [8,3,4,11],
        [9,1,2,10] ]

    print(trip(M))


