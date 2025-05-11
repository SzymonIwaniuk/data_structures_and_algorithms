from math import sqrt


def fib(n: int) -> int:
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_dyn(n: int) -> int:
    F = [0] * (n + 1)
    F[0] = 1
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]

    return F[n]


def fib_dyn_two(n: int) -> int:
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b

    return a


def fib_multiplying(n: int) -> int:
    golden = (1 + sqrt(5)) / 2
    return round((golden ** (n + 1)) / sqrt(5))


if __name__ == "__main__":
    print(fib(5))
    print(fib_dyn(5))
    print(fib_dyn_two(5))
    print(fib_multiplying(5))
