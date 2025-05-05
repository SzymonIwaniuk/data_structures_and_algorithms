def ispath(G, u, path, n, visited, gate, find):
        if len(path) == n and 0 in G[u][gate]:
            return True

        for v in G[u][gate]:
            if not visited[v] and not find:
                if u not in G[v][0]:
                    visited[v] = True
                    path.append(v)
                    find = ispath(G, v, path, n, visited, 0, find)
                    if find:
                        return find
                    visited[v] = False
                    path.pop()
                elif u not in G[v][1]:
                    visited[v] = True
                    path.append(v)
                    find = ispath(G, v, path, n, visited, 1, find)
                    if find:
                        return find
                    visited[v] = False
                    path.pop()

        return False

def droga( G ):
    n = len(G)
    find = False
    visited = [False] * n
    path = [0]
    visited[0] = True
    res = ispath(G, 0, path, n, visited, 0, find)

    if res: return path
    else: return None

G = [ ([1],[2,3,4]),
([0],[2,5,6]),
([1,5,6],[0,3,4]),
([0,2,4],[5,7,8]),
([0,2,3],[6,7,9]),
([1,2,6],[3,7,8]),
([1,2,5],[4,7,9]),
([4,6,9],[3,5,8]),
([3,5,7],[9]),
([4,6,7],[8]) ]

print(droga(G))