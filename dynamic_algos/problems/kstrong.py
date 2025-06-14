from typing import List


# O(n^3logn)
def kstrong(T: List[int], k: int) -> int:
    n = len(T)

    arrays = [[] for _ in range(n**2)]

    for i in range(n):
        for j in range(i + 1, n + 1):
            array = T[i:j]
            arrays[i * n + j - i] = array

    sorted_arrays = [sorted(subarray) for subarray in arrays]
    # print(sorted_arrays)
    maxi = float("-inf")

    for i in sorted_arrays:
        if i != []:
            l = len(i)
            k_copy = k
            summ = 0
            for j in i:
                # print(j)
                if j < 0 and k_copy > 0:
                    k_copy -= 1
                else:
                    summ += j

            maxi = max(maxi, summ)

    return maxi


if __name__ == "__main__":
    T = [-20, 5, -1, 10, 2, -8, 10]
    k = 1
    print(kstrong(T, k))


# O(n^2logn)
