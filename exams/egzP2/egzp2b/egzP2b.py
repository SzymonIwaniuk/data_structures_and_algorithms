from egzP2btesty import runtests
from math import log10


def build_dict(D):
    trie = {"": {"cnt": 0}}

    for word in D:
        word = word[::-1]
        trie[""]["cnt"] += 1
        node = trie[""]
        for ch in word:
            if ch not in node:
                node[ch] = {"cnt": 1}
            else:
                node[ch]["cnt"] += 1
            node = node[ch]

    return trie


def count_suffix(trie, suffix):
    # Empty suffix means all words
    if suffix == "":
        return trie[""]["cnt"]

    node = trie[""]
    for char in suffix[::-1]:  # reversed suffix = prefix in trie
        if char in node:
            node = node[char]
        else:
            return 0
    return node["cnt"]


def kryptograf(D, Q):
    trie = build_dict(D)
    product = 1
    for q in Q:
        c = count_suffix(trie, q)
        product *= c if c > 0 else 1  # avoid zero product
    return log10(product)

    # O(qnm)


# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests=2)
