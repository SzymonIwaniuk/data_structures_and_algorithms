"""
Prosze zaimplementowac testowanie czy graf jest spojny uzywajac
DFS dla reprezentacji macierzowej
"""


def is_connected(G: list[list[int]]) -> bool:
    n = len(G)
    visited = [False for _ in range(n)]
    visited[0] = True

    def dfs_visit(v):
        nonlocal visited, G, n

        for n_v in range(n):
            if G[v][n_v] == 1 and not visited[n_v]:
                visited[n_v] = True
                dfs_visit(n_v)

    dfs_visit(0)

    if False in visited:
        return False

    return True


if __name__ == "__main__":

    G1 = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]

    G2 = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]

    print(is_connected(G1))
    print(is_connected(G2))
