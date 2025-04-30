from typing import Tuple

class Union_find:
    def __init__(self, n):
        self.rank = [1 for _ in range(n)]
        self.parent = [i for i in range(n)]

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return self.parent[x]

    def union(self, x, y):
        x_node = self.parent[x]
        y_node = self.parent[y]

        if x_node != y_node:
            if self.rank[x_node] < self.rank[y_node]:
                self.parent[x_node] = y_node
            elif self.rank[x_node] > self.rank[y_node]:
                self.parent[y_node] = x_node
            else:
                self.parent[y_node] = x_node
                self.rank[x_node] += 1

def kruskal(G: list[list[Tuple[int,float]]]) -> list[Tuple[int,int]]:
    n = len(G)
    E = []
    for v in range(n):
        for u, d in G[v]:
                if v < u:
                    E.append([v, u, d])

    E.sort(key = lambda edge: edge[2])

    union_find = Union_find(n)
    mst = []

    for v, u, d in E:
        if union_find.find(v) != union_find.find(u):
            union_find.union(v, u)
            mst.append((v, u))

    return mst

if __name__ == '__main__':
    G = [
    [(1, 10), (2, 6), (3, 5)],
    [(0, 10), (3, 15)],
    [(0, 6), (3, 4)],
    [(0, 5), (1, 15), (2, 4), (4, 2)],
    [(3, 2)]
    ]

    print(kruskal(G))

