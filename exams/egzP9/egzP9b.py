def graph_preparation(
    G: list[list[int]], R: list[list[int]], n: int
) -> list[list[int]]:
    is_road = [[] for _ in range(n)]
    new_G = [[] for _ in range(n)]

    for i in range(n):
        for j in range(len(G[i])):
            is_road[i].append(True)

    for i in range(n):
        G[i].sort()
        R[i].sort()

    for i in range(n):
        j = 0
        k = 0
        l1 = len(G[i])
        l2 = len(R[i])

        while j < l1 and k < l2:
            if G[i][j] == R[i][k]:
                is_road[i][j] = False
                k += 1
                j += 1

            elif G[i][j] > R[i][k]:
                k += 1

            else:
                j += 1

    for i in range(n):
        for j in range(len(G[i])):
            if is_road[i][j]:
                new_G[i].append(G[i][j])

    return new_G


def dyrektor(G: list[list[int]], R: list[list[int]]) -> list[int]:
    n = len(G)

    # Funkcja dzialajaca w O(nlogn) ktora odtwarza graf bez remontowanych drog
    new_G = graph_preparation(G, R, n)

    cycle = []

    # Stack jest potrzebny, ponieaz po 2 tescie wystapi blad z glebokoscia rekurencji
    stack = [0]

    # Tablica do spamietywania na ktorym aktualnie sasiedzie sie zatrzymalismy w danym wierzcholku
    where = [0 for _ in range(n)]

    # O(nlogn)
    for i in range(n):
        new_G[i].sort()

    # Dfs ze stackiem
    while stack:
        v = stack[-1]
        if where[v] < len(new_G[v]):
            u = new_G[v][where[v]]
            where[v] += 1
            stack.append(u)
        else:
            cycle.append(stack.pop())

    return cycle[::-1]


if __name__ == "__main__":
    from egzP9btesty import runtests

    runtests(dyrektor, all_tests=True)
