from typing import List


def pijemy(k: int, PIWO: List[int]) -> List[int]:
    n = len(PIWO)
    count_piwo = [0] * k

    for i in range(n):
        count_piwo[PIWO[i] - 1] += 1

    count_piwo = list(enumerate(count_piwo, 1))
    count_piwo.sort(key=lambda x: x[1], reverse=True)

    for i in range(k):
        count_piwo[i] = list(count_piwo[i])

    # print(count_piwo)
    new_piwo = [0] * n
    index = 0

    for i in range(0, n, 2):
        if count_piwo[index][1] > 0:
            new_piwo[i] = count_piwo[index][0]
            count_piwo[index][1] -= 1
        else:
            index += 1
            new_piwo[i] = count_piwo[index][0]
            count_piwo[index][1] -= 1

    for i in range(1, n, 2):
        if count_piwo[index][1] > 0:
            new_piwo[i] = count_piwo[index][0]
            count_piwo[index][1] -= 1
        else:
            index += 1
            new_piwo[i] = count_piwo[index][0]
            count_piwo[index][1] -= 1

    return new_piwo


if __name__ == "__main__":
    PIWO = [1, 2, 1, 1, 1, 3, 3, 3, 2, 3]
    k = 3
    print(pijemy(k, PIWO))
    PIWO = [1, 1, 1, 2, 2, 3]
    k = 3
    print(pijemy(k, PIWO))
    PIWO = [1, 1, 1, 1, 2, 2, 3, 3]
    k = 3
    print(pijemy(k, PIWO))
