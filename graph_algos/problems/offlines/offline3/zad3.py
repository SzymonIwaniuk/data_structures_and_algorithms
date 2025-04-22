from zad3testy import runtests
from collections import deque

def longer( G: list[list[int]], s: int, t: int ) -> any:
    #step 1: bfs
    # O(V + E)
    n = len(G)
    distance = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[s] = True
    parent = [None for _ in range(n)]
    queue = deque()
    queue.append(s)

    while queue:
        v = queue.popleft()
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                distance[u] = distance[v] + 1
                queue.append(u)

    #step 2: check is exist path from s -> t
    if not visited[t]:
        return None

    #step 3: check vertex neightbours in t -> s path
    #O(V + E)
    t_copy = t
    prev = None

    while t_copy != None:
        another_edges = 0
        flag = False
        for u in G[t_copy]:
            if distance[u] >= distance[t_copy] and parent[t_copy] != u and prev != u:
                flag = True
            if distance[u] <= distance[t_copy] - 1 and parent[t_copy] != u:
                another_edges += 1
        if another_edges == 0 and flag:
            return(parent[t_copy], t_copy)
        prev = t_copy
        t_copy = parent[t_copy]

    return None

    #Total complexity O(V + E)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )

if __name__ == '__main__':
    # G = [ [1, 2],
    #     [0, 2],
    #     [0, 1] ]
    # print(longer(G,0,2))
    pass