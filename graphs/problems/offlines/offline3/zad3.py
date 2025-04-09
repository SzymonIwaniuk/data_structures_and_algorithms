from zad3testy import runtests
from collections import deque


def longer(G: list[list[int]], s: int, t: int) -> any:
    # step 1: bfs
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

    # step 2: check is exist path from s -> t
    if not visited[t]:
        return None

    # step 3: check vertex neightbours in t -> s path
    # O(V + E)

    t_copy = t
    while t_copy != None:
        for u in G[t]:
            if parent[u] != t_copy and distance[u] >= distance[t_copy]:
                return (parent[t_copy], t_copy)
        t_copy = parent[t_copy]

    return None

    # Total complexity O(V + E)


if __name__ == "__main__":

    # zmien all_tests na True zeby uruchomic wszystkie testy
    runtests(longer, all_tests=True)

    # G = [ [1, 2],
    #     [0, 2],
    #     [0, 1] ]
    # print(longer(G,0,2))
