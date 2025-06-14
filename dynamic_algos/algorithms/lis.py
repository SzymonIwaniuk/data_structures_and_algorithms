"""
Longest Increasing Subsequence - LIS
1. Znalezienie funkcji ktora bedziemy obliczac
f(i) dlugosc najdluzszego rosnacego podciagu konczacego sie na A[i]
g(i) max z f(i) do indeksu i
2. Wyznaczenie rownania rekurencyjnego dla tej funkcji
f(i) = max(f(j) + 1 | j < i ∧ A[j] < A[i])
g(i) = max(f(0), f(1) ... f(i - 1))
3. Obliczenie wyniku
g(len(A))
4. Implementacja
#O(n^2)
"""


def lis(A: list[int]) -> int:
    n = len(A)
    F = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                F[i] = max(F[i], F[j] + 1)

    return max(F)


""" https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/ """


def better_lis(A: list[int]) -> int:
    n = len(A)
    answer = []
    answer.append(A[0])

    for i in range(1, n):
        if A[i] > answer[-1]:
            answer.append(A[i])

        else:
            low = 0
            high = len(answer) - 1

            while low < high:
                mid = (low + high) // 2

                if answer[mid] < A[i]:
                    low = mid + 1

                else:
                    high = mid

            answer[low] = A[i]

    return len(answer)


if __name__ == "__main__":
    A = [7, 3, 4, 2, 6, 9, 5, 9, 1]
    print(lis(A))
    print(better_lis(A))
