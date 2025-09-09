from zad1testy import runtests


def tanagram(x, y, t):
    # nlogn
    n = len(x)
    m = len(y)

    if m != n:
        return False

    string_x = list(enumerate(list(x)))
    string_y = list(enumerate(list(y)))

    string_x.sort(key=lambda ch: ch[1])
    string_y.sort(key=lambda ch: ch[1])

    for i in range(n):
        pos1 = string_x[i][0]
        ch1 = string_x[i][1]
        pos2 = string_y[i][0]
        ch2 = string_y[i][1]


        if abs(pos1 - pos2) > t or ch1 != ch2:
            return False

    return True


if __name__ == '__main__':
    runtests(tanagram)