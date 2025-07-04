# kol2testy.py
from copy import deepcopy

from egz1atest_spec import ALLOWED_TIME, TEST_SPEC, gentest
from testy import *


def copyarg(arg):
    return deepcopy(arg)


def printarg(B, G, s, t):
    print("G   : ", limit(G))
    n = 0
    for u, v, w in G:
        n = max(n, u, v)
    print("B   : ", limit(B))
    print("|B| : ", len(B))
    print("|V| : ", n + 1)
    print("|E| : ", len(G))
    print("s   : ", s)
    print("t   : ", t)


def printhint(hint):
    print("Prawidlowy wynik : ", hint)


def printsol(sol):
    print("Wynik algorytmu  : ", sol)


def check(B, G, s, t, hint, sol):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good


def generate_tests(num_tests=None):
    global TEST_SPEC
    TESTS = []

    B = [(1, 1, 2), (2, 2, 3)]
    G = [(0, 1, 6), (1, 4, 7), (4, 3, 4), (3, 2, 4), (2, 0, 3), (0, 3, 6)]
    s = 0
    t = 4
    hint = 8
    newtest = {}
    newtest["arg"] = [B, G, s, t]
    newtest["hint"] = hint
    TESTS.append(newtest)

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    return TESTS


def runtests(f, all_tests=True):
    internal_runtests(
        copyarg,
        printarg,
        printhint,
        printsol,
        check,
        generate_tests,
        all_tests,
        f,
        ALLOWED_TIME,
    )
