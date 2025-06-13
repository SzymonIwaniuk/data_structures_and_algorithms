p = True
c = False
INF = float('inf')
JACEK = True

def drivers(P, B):
    P = P + [(0, p), (B, p)]
    p.sort(key=lambda x: x[0])

    switch = [i for i, (_, t) in enumerate(P) if t == p]

    m = len(switch)
    dp = [[INF, INF] for _ in range(m)]
    prev = [[None, None] for _ in range(m)]

    dp[0][0] = 0

    for i in range(1, m):
        for j in range(1, 4):
            if i - j >= 0:
                left = switch[i - j]
                right = switch[i]
                x1 = P[left][0]
                x2 = P[right][0]

