from math import inf

from egz1Atesty import runtests


def battle(P, K, R):
    n = len(K)
    m = len(P)

    # Krawędzie: (katapulta_index, procesor_index, katapulta_pos, procesor_pos)
    edges = []

    for i in range(n):  # dla każdej katapulty
        for j in range(m):  # dla każdego procesora
            if P[j] > K[i] and P[j] - K[i] <= R[i]:
                edges.append((i, j, K[i], P[j]))

    # Sortowanie: najpierw pozycja katapulty, potem pozycja procesora
    edges.sort(key=lambda x: (x[2], x[3]))

    used_k = set()  # użyte katapulty
    used_p = set()  # użyte procesory
    match_count = 0

    for ki, pi, _, _ in edges:
        if ki not in used_k and pi not in used_p:
            used_k.add(ki)
            used_p.add(pi)
            match_count += 1

    return match_count


runtests(battle, all_tests=True)
