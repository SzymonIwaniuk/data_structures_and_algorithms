def topological_sort(G: list[list[int]]) -> list[int]:
    n = len(G)
    reversed_array = []

    def dfs_visit(G: list[list[int]], v: int) -> any:
        for u in G[v]:
            if visited[u] == False:
                visited[u] = True
                dfs_visit(G, u)
        reversed_array.append(v)

    visited = [False for _ in range(n)]

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            dfs_visit(G, i)

    return reversed_array[::-1]


if __name__ == "__main__":

    G = [[1, 2], [3, 4], [4], [], [5], []]
    print(topological_sort(G))
