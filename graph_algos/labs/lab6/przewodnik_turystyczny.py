 # 5 Przewodnik turystyczny: Podaj sciezke z s do t gdzie waga jej najmniejszej krawedzi jak najwieksza.

# Umieszczamy w kolejce priorytetowej typu max
# Stosujemy strukture union_find i sciagmy maksymalna krawedz oraz u.max, v.max wraz z nia
# Sprawdzamy czy s i t maja tego samego reprezentanta, jezli tak to budujemy sciezke
# i zwracamy ja oraz wage najmniejszej krawedzi w tej sciezce


import heapq


# union_find
class Node:
    def __init__(self, val):
        self.parent = self
        self.val = val
        self.rank = 0

    #O(logV)
    def find(self) -> "Node":
        if self != self.parent:
            self.parent = self.parent.find()
        return self.parent

    #O(logV)
    def union(self, y: "Node") -> None:
        root1 = self.find()
        root2 = y.find()
        if root1 == root2:
            return

        if root1.rank < root2.rank:
            root2.parent = root1
        else:
            root2.parent = root1
            if root2.rank == root1.rank:
                root1.rank += 1


def przewodnik_turystyczny(M: list[list[list[int, float]]], s: int, t: int) -> (float, list[int]):
    n = len(M)
    edges = []
    parent = [None] * n

    # O(E)
    for v in range(n):
        for [u, w] in M[v]:
            edges.append([w, v, u])

    nodes = [Node(i) for i in range(n)]

    #O(ElogV)
    while edges:
        w, v, u = heapq._heappop_max(edges)

        if nodes[v].find() != nodes[u].find():
            parent[nodes[u].find().val] = nodes[v].find().val
            nodes[v].union(nodes[u])

        if nodes[s].find() == nodes[t].find():
            path = []
            run = t
            while run != s and run != None:
                path.append(run)
                run = parent[run]

            path.append(s)

            return w, path[::-1]
    return -1

# Overall O(ElogV)

if __name__ == "__main__":
    G = [
        [[1, 5], [2, 4]],
        [[0, 5], [2, 2]],
        [[0, 4], [1, 2]],
    ]

    print(przewodnik_turystyczny(G, 0, 1))
    print(przewodnik_turystyczny(G, 0, 2))
