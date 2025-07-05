from heapq import heappop, heappush
from typing import List, Tuple

from zad2testy import runtests


def robot(L: List[List[str]], A: Tuple[int, int], B: Tuple[int, int]) -> int:
    # 3 poziomy przyspieszenia, 4 możliwe kierunki, szerokość labiryntu, wysokość labiryntu
    DP = [
        [[[-1] * 3 for _ in range(4)] for _ in range(len(L[0]))] for _ in range(len(L))
    ]

    # czas, położenie x, położenie y, kierunek, poziom przyspieszenia
    queue = [(0, A[0], A[1], 0, 0)]

    possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seconds = [60, 40, 30]

    while queue:
        time, x, y, direction, idx = heappop(queue)
        if (x, y) == B:
            return time
        if DP[y][x][direction][idx] != -1 or L[y][x] == "X":
            continue
        DP[y][x][direction][idx] = time
        heappush(queue, (time + 45, x, y, (direction + 1) % 4, 0))
        heappush(queue, (time + 45, x, y, (direction + 3) % 4, 0))
        x += possible_moves[direction][0]
        y += possible_moves[direction][1]
        heappush(queue, (time + seconds[idx], x, y, direction, min(idx + 1, 2)))


runtests(robot)
