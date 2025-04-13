"""
Prosze zaimplementowac drzewo BST w ktorym dostepne sa operacje
a) znajdowanie nastepnika danego elementu
b) wstawianie
"""


class BSTNode:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.right = None
        self.left = None


# Znajdowanie nastepnika elementu


def succ(w: BSTNode) -> int:
    if w.right != None:
        w = w.right
        while w.left != None:
            w = w.left
        return w

    else:
        while w.parent != None and w.parent.right == w:
            w = w.parent
        return w.parent


# Wstawianie elementu do BST


def insert(w: BSTNode, x: int) -> None:
    while True:
        if w.val <= x:
            if w.right is None:
                w.right = BSTNode(x)
                break
            else:
                w = w.right

        else:
            if w.left is None:
                w.left = BSTNode(x)
            else:
                w = w.left
                break


if __name__ == "__main__":

    root = BSTNode(10)
    node5 = BSTNode(5)
    node15 = BSTNode(15)
    node3 = BSTNode(3)
    node7 = BSTNode(7)
    node20 = BSTNode(20)

    root.left = node5
    root.right = node15
    node5.parent = root
    node15.parent = root

    node5.left = node3
    node5.right = node7
    node3.parent = node5
    node7.parent = node5

    node15.right = node20
    node20.parent = node15

    print(succ(node5).val)
    insert(root, 8)
