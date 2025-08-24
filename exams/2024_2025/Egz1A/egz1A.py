from egz1Atesty import runtests
from typing import List


def battle(P: List[int], K: List[int], R: List[int]) -> int:
   # Step 1 - counting sort
   n = max(max(K), max(P))
   arr = [0] * (n + 1)
   for i in P:
      arr[i] = (i, 'p', None)

   K = list(zip(K, R))
   for i, j in K:
      arr[i] = (i, 'k', j)

   sorted_arr = []
   for tup in arr:
      if tup != 0:
         sorted_arr.append(tup)

   # print(sorted_arr)

   # Step 2 - modified brackets problem
   res = 0
   stack = []

   for pos, typ, ran in sorted_arr:
      if typ == 'k':
         stack.append((pos, ran))

      else:
         while stack and stack[-1][0] + stack[-1][1] < pos:
            stack.pop()

         if stack:
            stack.pop()
            res += 1

   return res

runtests(battle, all_tests=True)
