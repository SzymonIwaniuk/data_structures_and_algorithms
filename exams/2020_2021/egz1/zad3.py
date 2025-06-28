from zad3testy import runtests
from math import inf
import sys

sys.setrecursionlimit(10000)
def common_part(a, b):
    if a == () or b == ():
        return 0, ()
    a1, b1 = a
    a2, b2 = b

    start = max(a1, a2)
    end = min(b1, b2)

    if start < end:
        return end - start, (start, end)
    else:
        return 0, ()


def kintersect( A, k ):
  n = len(A)
  memo = {}

  def _kintersect_rec(i, j, p, l):
    if p == ():
        return [], -1

    if j == k:
      return [], l

    elif i == n or (n - i + j < k):
      return [], -1

    key = (i, j, p[0], p[1])
    if key in memo:
        return memo[key]

    new_l, array = common_part(p, A[i])
    res_1 = _kintersect_rec(i + 1, j + 1, array, new_l)
    res_2 = _kintersect_rec(i + 1, j, p, l)

    a = None
    b = 0
    if res_1[1] > res_2[1]:
        res = (res_1[0] + [i], res_1[1])
    else:
        res = res_2

    memo[key] = res
    return res

  out = _kintersect_rec(0, 0, (-inf, inf), 0)
  return out[0]

runtests(kintersect)
