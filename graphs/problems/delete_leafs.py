from collections import deque

"""
Chepeast delete all leafs in btree
"""

#          A        A - B = 2
#         / \       B - D = 1
#        B   C      B - E = 5
#       / \         A - C = 3
#      D   E        Answer: 5


class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def delete(p: BTNode) -> int:
    if p is None:
        return 0

    total = 0

    for child in [p.left, p.right]:
        if child:
            cost_in_subtree = delete(child)
            cost_cut_edge = p.val - child.val
            total += min(cost_in_subtree, cost_cut_edge)

    return total
