from egz3atesty import runtests
from typing import List, Tuple


def snow(T: int, I: List[Tuple[int, int]]) -> int:
    # Create empty array length 2n for start and end of snow fall
    n = len(I)
    array = [0, 0] * n

    # start = -1
    # end = 1
    # Because next we want sort this array so start must be before end in case of start == end
    for i in range(n):
        array[i] = (I[i][0], -1)
        array[n + i] = (I[i][1], 1)

    array.sort()
    result = current = 0

    # If start increase current height of snow else decrease
    for i, j in array:
        if j == -1:
            current += 1
            result = max(result, current)
        else:
            current -= 1

    return result

    # Complexity O(nlogn)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
