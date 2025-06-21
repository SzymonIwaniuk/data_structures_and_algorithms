from collections import deque
from math import inf


def kurt(D):
    n = len(D)
    queue = deque()
    queue.appendleft((0, 0, False, 0))
    tab_for_steps = [[inf] * n for _ in range(n)]

    while queue:
        i, j, hit_wall, steps = queue.pop()
        print(i, j, hit_wall, steps)
        if tab_for_steps[i][j] < steps:
            continue

        tab_for_steps[i][j] = steps

        i_copy = i + 1
        j_copy = j + 1
        hit_wall_copy = hit_wall

        while i_copy < n:
            print(i_copy, j)
            if i_copy + 1 < n and D[i_copy + 1][j] == "#":
                if hit_wall is False:
                    i_copy += 2
                    deque.appendleft((i_copy, j, True, steps + 1))
                    break

            if tab_for_steps[i_copy][j] > steps + 1:
                break
            else:
                tab_for_steps[i_copy][j] = steps + 1

            i_copy += 1

        if i_copy == n - 1:
            deque.appendleft((i_copy, j, hit_wall, steps + 1))

            if j_copy + 1 < n and D[i][j_copy] == "#":
                if hit_wall is False:
                    j_copy += 2
                    hit_wall = True
                    continue
                else:
                    deque.appendleft((i, j_copy, hit_wall, steps + 1))
                    break

            if tab_for_steps[i][j_copy] > steps + 1:
                break
            else:
                tab_for_steps[i][j_copy] = steps + 1

            j_copy += 1

            deque.appendleft((i, j_copy, hit_wall, steps + 1))

    # print(tab_for_steps)
    return tab_for_steps[n - 1][n - 1]


if __name__ == "__main__":
    D = ["000##", "##000", "000##", "00##0", "00000"]

    print(kurt(D))
