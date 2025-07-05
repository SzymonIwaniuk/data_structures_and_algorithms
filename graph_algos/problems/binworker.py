from typing import List


def dfs_visit(w, visited):
    for m in M[w]:
        if not visited[m]:
            visited[m] = True
            if match[m] == -1 or dfs_visit(match[m], visited):
                match[m] = w
                return True
    return False


def binworker(M: List[List[int]]) -> int:
    n = len(M)
    global match
    match = [-1] * n
    maxi = 0

    for w in range(n):
        visited = [False] * n
        if dfs_visit(w, visited):
            maxi += 1
    return maxi


if __name__ == "__main__":
    M = [[0, 1, 3], [2, 4], [0, 2], [3], [3, 2]]  # 0  # 1  # 2  # 3  # 4
    print(binworker(M))
