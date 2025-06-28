from collections import deque


def kurt(D: list[str]) -> int:
    n = len(D)

    S = [[float("inf")] * n for _ in range(n)]
    S[0][0] = 0
    Q = deque()
    Q.append((0, 0, False))

    while Q:
        r, k, hit_wall = Q.popleft()
        steps = S[r][k]
        print(r, k, hit_wall)
        r_copy = r
        k_copy = k

        while r_copy + 1 < n and D[r_copy + 1][k] != "#":
            r_copy += 1

        if (
            not hit_wall
            and r_copy + 2 < n
            and D[r_copy + 2][k] != "#"
            and S[r_copy + 2][k] > steps + 1
        ):
            S[r_copy + 2][k] = steps + 1
            Q.append((r_copy + 2, k, True))
        elif S[r_copy][k] > steps + 1:
            S[r_copy][k] = steps + 1
            Q.append((r_copy, k, hit_wall))

        while k_copy + 2 < n:
            if D[r][k_copy + 1] == "#":
                break
            k_copy += 1

        if D[r][k_copy + 1] == "#":
            if hit_wall == False and k_copy + 2 < n:
                k_copy += 2
                S[r][k_copy] = steps + 1
                Q.append((r, k_copy, True))
        else:
            S[r][k_copy] = steps + 1
            Q.append((r, k_copy, hit_wall))

    for i in range(4):
        print(S[i])


if __name__ == "__main__":
    D = ["000##", "##000", "000##", "00##0", "00000"]

    print(kurt(D))
