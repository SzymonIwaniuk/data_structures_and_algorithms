from collections import deque

def projects(n, L):
    # O(m)
    dependent = set()
    for u, v in L:
        dependent.add(u)

    # O(n)
    independent = set()
    for i in range(n):
        if i not in dependent:
            independent.add(i)

    graph = [[] for _ in range(n)]

    for u, v in L:
        graph[v].append(u)

    visited = set(independent)
    times = [float('inf') for _ in range(n)]
    for v in visited:
        times[v] = 1

    queue = deque(list(independent))

    # O(n + m)
    while queue:
        v = queue.popleft()

        for u in graph[v]:
            if u not in visited:
                visited.add(u)
                queue.append(u)
                times[u] = times[v] + 1

    return max(times)

if __name__ == '__main__':
    n = 4
    L = [(3, 1), (1, 2), (1, 0)]
    print(projects(n, L))