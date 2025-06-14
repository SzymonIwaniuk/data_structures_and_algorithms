from typing import List


def inwerstor(T: List[int]) -> int:
    maxi = 0
    n = len(T)

    for i in range(n - 1):
        tmp = T[i]

        for j in range(i + 1, n):
            tmp = min(tmp, T[j])
            # print(i,j,tmp,j-i + 1)
            current = tmp * (j - i + 1)
            maxi = max(maxi, current)

    return maxi


if __name__ == "__main__":
    T = [2, 1, 5, 6, 2, 3]
    print(inwerstor(T))
