from typing import List


def getMinOperations(n: int, computationalTime: List[int]) -> int:
    computationalTime.sort(reverse=True)

    i = 0
    operations = 0

    while i != n:
        if computationalTime[i] % 2 == 1:
            i += 1

        else:
            tmp = computationalTime[i]
            operations += 1

            for j in range(i, n):
                if computationalTime[j] == tmp:
                    computationalTime[j] = tmp // 2

    return operations


if __name__ == "__main__":
    n1 = 4
    computationalTime1 = [2, 4, 8, 16]
    n2 = 4
    computationalTime2 = [8, 2, 5, 6]
    print(getMinOperations(n1, computationalTime1))
    print(getMinOperations(n2, computationalTime2))
