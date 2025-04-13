# 2 Sciezka Hamiltona przebiega przez wszystkie wierzcholki grafu. Prosze zaproponowac algorytm znajdujacy sciezke w DAG'u.


def hamilton_path_in_dag(G: list[list[int]]) -> list[int]:
    n = len(G)
    sorted_arr = topological_sort(G)

    for v in range(n - 1):
        if not sorted_arr[v + 1] in G[v]:
            return False
    return True


def topological_sort(G: list[list[int]]) -> list[int]:
    n = len(G)
    reversed_array = []

    def dfs_visit(G: list[list[int]], v: int) -> any:
        for u in G[v]:
            if visited[u] == False:
                visited[u] = True
                dfs_visit(G, u)
        # Jezeli krawedz nie ma juz sasiadow dodaj ja do tablicy
        reversed_array.append(v)

    visited = [False for _ in range(n)]

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            dfs_visit(G, i)

    return reversed_array[::-1]


if __name__ == "__main__":
    G1 = [[1], [2], [3], []]
    G2 = [[1], [], [1], []]
    print(hamilton_path_in_dag(G1))
    print(hamilton_path_in_dag(G2))
