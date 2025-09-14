from math import ceil, log2
from collections import deque


"""
Implementation of a structure based on a interval tree that allows summing
array values from index i to j and swapping the array element in O(logn).
"""


# Class for tree node
class Node:
    def __init__(self, val: int):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val

    # Changing leaf value == changing subarray sum
    def change_value(self, num: int):
        diff = num - self.val

        while True:
            self.val += diff
            if self.parent is None:
                break

            self = self.parent


# Modified interval tree
class IntervalTree:
    def __init__(self, tab):
        l = len(tab)
        # Define a buffor whose size is a power of 2 for easier tree construction
        # + ensuring that adding an item has O(1) amortized complexity.
        self.buffor_length = 2 ** (ceil(log2(l)))
        # List of tree leaves
        self.leafs = [
            Node(tab[i]) if i < l else Node(0) for i in range(self.buffor_length)
        ]
        self.root = self._build(self.leaves)

    # Build tree
    def _build(self, leaves):
        # We can skip queue
        queue = deque(leaves)

        while queue:
            node1 = queue.popleft()
            if not queue:
                return node1

            node2 = queue.popleft()

            new_node = Node(node1.val + node2.val)

            new_node.left = node1
            new_node.right = node2
            node1.parent = new_node
            node2.parent = new_node

            queue.append(new_node)

    # Subsum from index i to j
    def subsum(self, i, j):
        def _subsum_rec(node, l, r, cur_i, cur_j):
            if cur_j < l or cur_i > r:
                return 0
            if cur_i <= l and cur_j >= r:
                return node.val

            mid = (l + r) // 2

            return _subsum_rec(node.left, l, mid, cur_i, cur_j) + _subsum_rec(
                node.right, mid + 1, r, cur_i, cur_j
            )

        return _subsum_rec(self.root, 0, self.buffor_length - 1, i, j)


if __name__ == "__main__":
    array = [3, 1, 2, 5, 4, 7]

    # instance creation
    interval_tree = IntervalTree(array)

    print(interval_tree.root.left.val)
    print(interval_tree.root.right.val)
    print(interval_tree.root.right.left.val)
    print(interval_tree.root.right.right.val)

    # change val
    interval_tree.leaves[1].change_value(5)
    print(interval_tree.leaves[1].val)
    print(interval_tree.leaves[1].parent.val)

    # sum T[i] + T[i + 1] ... + T[j] inclusive
    print(interval_tree.subsum(0, 2))
    print(interval_tree.subsum(3, 5))
