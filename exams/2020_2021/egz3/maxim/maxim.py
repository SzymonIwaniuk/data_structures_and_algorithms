from zad3testy import runtests
from math import log2, ceil

def find(cur_node, search_node):
    if search_node == 1:
        return cur_node.key

    else:
        path = bin(search_node)[3:]

        for child in path:
            if child == '1':
                cur_node = cur_node.right

            else:
                cur_node = cur_node.left

        return cur_node.key


def maxim( T, C ):
    """tu prosze wpisac wlasna implementacje"""
    maxi = float('-inf')

    for idx in C:
        maxi = max(maxi, find(T, idx))

    return maxi


runtests( maxim )


