from collections import deque


def find_cycle(G: list[list[int]]) -> bool:
    l = len(G)
    q = deque()
    visited = [-1] * l  # Tablica na visited i parent
    q.append(0)
    visited[0] = 0

    while len(q) > 0:
        v = q.popleft()
        for u in G[v]:
            if visited[u] == -1:
                visited[u] = v
                q.append(u)
            elif visited[v] != u:
                return True
    return False


if __name__ == "__main__":

    G1 = [[1], [0, 2, 3, 6], [1, 3], [1, 2, 4], [3, 5], [4, 6], [5, 1]]
    G2 = [[1], [0]]
    G3 = [[1], [0, 2], [1, 3], [2]]
    G4 = [[1, 2], [0, 2], [0, 1]]

    print(find_cycle(G4))
