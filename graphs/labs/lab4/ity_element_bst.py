"""
Jak zmodyfikowac BST tak, zeby w czasie O(h)
dalo sie znajdowac i-ty element co do wieklosci
"""


class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.smaller = None


def ity_element_bst(p: BSTNode, i: int) -> any:
    while p:
        if p.smaller == i + 1:
            return p.val

        elif p.smaller < i:
            i -= p.smaller + 1
            p = p.right

        else:
            p = p.left

    return None
