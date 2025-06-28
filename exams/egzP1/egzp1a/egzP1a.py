from egzP1atesty import runtests 
from math import inf


def titanic( W, M, D ):
    coded_msg = ''

    for ch in W:
        coded_msg += M[ord(ch) - ord('A')][1]

    m = len(coded_msg)

    avaiable = {M[i][1]: M[i][0] for i in D}
    memo = {}

    def _titanic_rec(i, to_code):
        if i == m:
            if to_code == '':
                return 0

            elif to_code in avaiable:
                return 1

            else:
                return inf

        if (i, to_code) in memo:
            return memo[(i, to_code)]

        mini = inf
        can_change = avaiable.get(to_code, False)

        if can_change:
            mini = min(mini ,_titanic_rec(i + 1, coded_msg[i]) + 1)

        mini = min(mini, _titanic_rec(i + 1, to_code + coded_msg[i]))

        memo[(i, to_code)] = mini
        return mini

    out = _titanic_rec(1, coded_msg[0])
    return out

runtests ( titanic, recursion= True )