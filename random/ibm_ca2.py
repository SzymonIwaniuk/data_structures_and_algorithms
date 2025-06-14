def question1(s: str) -> int:

    left = 0
    right = 0

    for brace in s:
        if brace == "(":
            left += 1
        else:
            if left > 0:
                left -= 1
            else:
                right += 1

    return left + right


def question2(s: str) -> str:
    n = len(s)

    if n % 2 == 1:
        mid = n // 2
    else:
        mid = -1

    ind = None

    for i in range(n):
        if i == mid:
            continue

        else:
            if s[i] != "a":
                ind = i
                break

    if ind != None:
        return s[0:i] + "a" + s[i + 1 : n]

    else:
        return "IMPOSSIBLE"


if __name__ == "__main__":
    s1 = "(()))"
    print(question1(s1))
    s2 = "))(("
    print(question1(s2))
    s = "mom"
    print(question2(s))
    s = "aaabbaaa"
    print(question2(s))
    s = "aoa"
    print(question2(s))
    s = "aaaoaaa"
    print(question2(s))
