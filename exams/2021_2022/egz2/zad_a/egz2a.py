from egz2atesty import runtests
from math import log2, ceil


def insert(current, tree, coal_amount, first_element):
    if current >= first_element:
        tree[current] -= coal_amount
        return current - first_element

    left = 2 * current + 1
    right = 2 * current + 2

    if tree[left] >= coal_amount:
        i = insert(left, tree, coal_amount, first_element)
    else:
        i = insert(right, tree, coal_amount, first_element)

    tree[current] = max(tree[left], tree[right])
    return i


def coal(A, T):
    n = len(A)
    p = ceil(log2(n))
    tree = [T for node in range(2 ** (p + 1) - 1)]
    first_element = 2**p - 1

    ans = None
    for coal_amount in A:
        answer = insert(0, tree, coal_amount, first_element)

    return answer


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(coal, all_tests=True)
