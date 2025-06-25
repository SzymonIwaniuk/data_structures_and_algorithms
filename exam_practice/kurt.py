from collections import deque
from math import inf


def kurt(D):
    n = len(D)
    queue = deque()
    queue.appendleft((0, 0, 0, 0))
    tab_for_steps = [[[inf] * 2 for _ in range(n)] for __ in range(n)]

    while queue:
        i, j, hit_wall, steps = queue.pop()

        if i > n - 1 or j > n - 1:
            continue

        if tab_for_steps[i][j][hit_wall] < steps:
            continue

        tab_for_steps[i][j][hit_wall] = steps

        i_copy = i
        j_copy = j

        while i_copy < n - 2 and D[i_copy + 1][j] != '#':
            i_copy += 1

        if i_copy < n - 1 and D[i_copy + 1][j] == '#':
            if hit_wall == 0:
                queue.appendleft((i_copy + 2, j, 1, steps + 1))
            queue.appendleft((i_copy, j, hit_wall, steps + 1))
        else:
            queue.appendleft((i_copy, j, hit_wall, steps + 1))


        while j_copy < n - 1 and D[i][j_copy + 1] != '#':
            j_copy += 1

        #print(j_copy)
        if j_copy < n - 2 and D[i][j_copy + 1] == '#':
            if hit_wall == 0:
                queue.appendleft((i, j_copy + 2, 1, steps + 1))
            queue.appendleft((i, j_copy, hit_wall, steps + 1))

        else:
            queue.appendleft((j_copy, i, hit_wall, steps + 1))


    #print(tab_for_steps)
    return min(tab_for_steps[n - 1][n - 1]) if min(tab_for_steps[n - 1][n - 1]) != inf else -1


if __name__ == "__main__":
    D = ["000##", "##000", "000##", "00##0", "00000"]

    print(kurt(D))
