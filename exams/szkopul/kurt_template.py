from collections import deque
from math import inf


def kurt(D):
    n = len(D)
    queue = deque()
    queue.appendleft((0, 0, 0, 0))
    tab_for_steps = [[[inf] * 2 for _ in range(n)] for __ in range(n)]

    while queue:
        i, j, hit_wall, steps = queue.pop()

        if i < 0 or i >= n or j < 0 or j >= n:
            continue

        if tab_for_steps[i][j][hit_wall] <= steps:
            continue

        tab_for_steps[i][j][hit_wall] = steps

        if i == n - 1 and j == n - 1:
            return steps

        i_copy = i

        while i_copy < n - 1 and D[i_copy + 1][j] != "#":
            i_copy += 1

        if i_copy < n - 1 and D[i_copy + 1][j] == "#":
            if hit_wall == 0 and i_copy + 2 < n and D[i_copy + 2][j] == "0":
                if tab_for_steps[i_copy + 2][j][1] > steps + 1:
                    queue.appendleft((i_copy + 2, j, 1, steps + 1))

            if tab_for_steps[i_copy][j][hit_wall] > steps + 1:
                queue.appendleft((i_copy, j, hit_wall, steps + 1))
        else:
            if tab_for_steps[i_copy][j][hit_wall] > steps + 1:
                queue.appendleft((i_copy, j, hit_wall, steps + 1))

        j_copy = j

        while j_copy < n - 1 and D[i][j_copy + 1] != "#":
            j_copy += 1

        if j_copy < n - 1 and D[i][j_copy + 1] == "#":
            if hit_wall == 0 and j_copy + 2 < n and D[i][j_copy + 2] == "0":
                if tab_for_steps[i][j_copy + 2][1] > steps + 1:
                    queue.appendleft((i, j_copy + 2, 1, steps + 1))

            if tab_for_steps[i][j_copy][hit_wall] > steps + 1:
                queue.appendleft((i, j_copy, hit_wall, steps + 1))
        else:
            if tab_for_steps[i][j_copy][hit_wall] > steps + 1:
                queue.appendleft((i, j_copy, hit_wall, steps + 1))

        i_copy = i

        while i_copy > 0 and D[i_copy - 1][j] != "#":
            i_copy -= 1

        if i_copy > 0 and D[i_copy - 1][j] == "#":
            if hit_wall == 0 and i_copy - 2 >= 0 and D[i_copy - 2][j] == "0":
                if tab_for_steps[i_copy - 2][j][1] > steps + 1:
                    queue.appendleft((i_copy - 2, j, 1, steps + 1))

            if tab_for_steps[i_copy][j][hit_wall] > steps + 1:
                queue.appendleft((i_copy, j, hit_wall, steps + 1))
        else:
            if tab_for_steps[i_copy][j][hit_wall] > steps + 1:
                queue.appendleft((i_copy, j, hit_wall, steps + 1))

        j_copy = j

        while j_copy > 0 and D[i][j_copy - 1] != "#":
            j_copy -= 1

        if j_copy > 0 and D[i][j_copy - 1] == "#":
            if hit_wall == 0 and j_copy - 2 >= 0 and D[i][j_copy - 2] == "0":
                if tab_for_steps[i][j_copy - 2][1] > steps + 1:
                    queue.appendleft((i, j_copy - 2, 1, steps + 1))

            if tab_for_steps[i][j_copy][hit_wall] > steps + 1:
                queue.appendleft((i, j_copy, hit_wall, steps + 1))
        else:
            if tab_for_steps[i][j_copy][hit_wall] > steps + 1:
                queue.appendleft((i, j_copy, hit_wall, steps + 1))

    return -1


"""
Prosimy nie modyfikować kodu poniżej :)
"""

n = int(input())
D = []
for _ in range(n):
    D.append(input())
sol = kurt(D)
print(sol)
