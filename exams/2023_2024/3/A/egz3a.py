from collections import deque

from egz3atesty import runtests


def mykoryza(G: list[list[int, int]], T: list[int], d: int) -> int:
    n = len(G)
    l = len(T)

    times = [float("inf")] * n
    parent = [None] * n
    Q = deque()
    overall_time = 0

    # parent[t] = i indeks zainfekowanego drzewa w tablicy T

    for i in range(l):
        times[T[i]] = 0
        parent[T[i]] = i
        Q.append((0, T[i]))

    while Q:
        time, tree = Q.popleft()

        if time + 1 < overall_time:
            overall_time = time + 1

            for new_tree in G[tree]:
                if times[new_tree] > time + 1:
                    times[new_tree] = time + 1
                    parent[new_tree] = parent[tree]
                    Q.appendleft((time + 1, new_tree))

                elif times[new_tree] == times[tree]:
                    if parent[tree] < parent[new_tree]:
                        parent[new_tree] = parent[tree]
        else:
            for new_tree in G[tree]:
                if times[new_tree] > time + 1:
                    times[new_tree] = time + 1
                    parent[new_tree] = parent[tree]
                    Q.append((time + 1, new_tree))

    summ = 0
    for i in range(n):
        if parent[i] == d:
            summ += 1

    return summ


# zmien all_tests na True zeby uruchomic wszystkie testy


if __name__ == "__main__":
    from egz3atesty import runtests

    runtests(mykoryza, all_tests=True)
