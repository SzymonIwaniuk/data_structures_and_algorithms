from egzP7atesty import runtests


# PROBLEM PRZEPLYWOWY NIE OMAWIANY W ROKU 2024-2025
def dfs_visit(s, visited, T):
    for p in T[s]:
        if p != None:
            if not visited[p]:
                visited[p] = True
                if match[p] == -1 or dfs_visit(match[p], visited, T):
                    match[p] = s
                    return True

    return False


def akademik(T):
    n = len(T)
    global match
    match = [-1] * n
    mini = n

    for s in range(n):
        visited = [False] * n
        if dfs_visit(s, visited, T):
            print(match)
            mini -= 1

    print(match)
    return mini


runtests(akademik)

# if __name__ == '__main__':
# T = [(2, 3, None), (0, 1, 3), (0, 2, None), (1, 3, 4), (2, 3, None)]
# print(akademik(T))
