from typing import List, Tuple
from math import inf


def wyprawy(WI: List[Tuple[int, int, int]]) -> int:
    sorted_wyprawy = sorted(WI, key=lambda x: (x[0], -x[1]))
    # print(sorted_wyprawy)
    n = len(WI)
    saved_electricity = -inf

    for i in range(n):
        start, end, electricity = sorted_wyprawy[i]
        current_electricity = electricity
        current_end = end

        for j in range(i + 1, n):
            next_start, next_end, next_electricity = sorted_wyprawy[j]

            if next_start >= current_end:
                current_electricity += next_electricity
                prev = next_end

        saved_electricity = max(saved_electricity, current_electricity)

    return saved_electricity


if __name__ == "__main__":
    WI = [(1, 5, 100), (3, 4, 70), (2, 4, 90), (4, 7, 60), (4, 5, 10)]
    print(wyprawy(WI))
