from egz3btesty import runtests
from math import log2, ceil

class SegmentTree:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.r = float('-inf')
        self.idx = -1
        self.left = None
        self.right = None


    def update(self, pos, value, index):
        if self.lo == self.hi:
            self.r = value
            self.idx = index
            return
        mid = (self.lo + self.hi) // 2
        if pos <= mid
            if not self.left:
                self.left = SegmentTree(self.lo, mid)
            self.left.update(pos, value, index)

        else:
            if not self.right:
                self.right = SegmentTree(mid + 1, self.hi)
            self.right.update(pos, value, index)

        l_r = self.left.r if self.left else float('-inf')
        l_idx = self.left.idx if self.left else -1
        r_r = self.right.r if self.right else float('-inf')
        r_idx = self.right.idx if self.right else -1

        if l_r >= r_r:
            self.r, self.idx = l_r, l_idx
        else:
            self.r, self.idx = r_r, r_idx








    def query()


runtests(uncool, all_tests=False)