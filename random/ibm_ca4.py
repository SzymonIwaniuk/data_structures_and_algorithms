def substring(s: str):
    n = len(s)
    if n == 0:
        return s

    new_string = ""

    for i in range(n):
        if s[i] != "a":
            new_string += chr(ord(s[i]) - 1)
        elif i == 0:
            new_string = "Z"
        else:
            break

    return new_string + s[i:]


# print(substring('hackerrank'))
# print(substring('abckerrank'))


def networks(speed, minComps, speedThreshold):
    n = len(speed)
    used = [False for i in range(n)]
    networks = 0
    i = 0

    while i <= n - minComps:
        sum_speed = 0
        found = False

        for j in range(i, min(i + minComps, n)):
            sum_speed += speed[j]

        if sum_speed >= speedThreshold:
            networks += 1
            i += minComps
            found = True

        else:
            for j in range(i + minComps, n):
                sum_speed += speed[j]
                if sum_speed >= speedThreshold:
                    networks += 1
                    i = j + 1
                    found = True
                    break

            if not found:
                i += 1

    return networks


speed = [5, 7, 9, 12, 10, 13, 15, 17]
minComps = 2
speedThreshold = 15

# print(networks(speed,minComps,speedThreshold))


def binary(pwd: str):
    n = len(pwd)

    if n % 2 == 1:
        return "IMPOSSIBLE"

    i = 0
    flips = 0

    while i < n:
        window = pwd[i : i + 2]
        if len(set(window)) != 1:
            flips += 1
        i += 2

    return flips


pwd = "0110011100"
print(binary(pwd))
pwd = "0010"
print(binary(pwd))


def stock(arr, d):
    n = len(arr)
    arr.sort()
    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k]) % d == 0:
                    result += 1

    return result


arr = [3, 3, 4, 7, 8]
d = 5
print(stock(arr, d))


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(f"{i}")

    return 0


print(fizzbuzz(15))


def getMaxOccurences(components, minLength, maxLength, maxUnique):
    n = len(components)
    appers = {}

    for i in range(n - minLength):
        for j in range(minLength + i, min(maxLength + i + 1, n)):
            substring = components[i:j]
            unique = set(substring)

            if len(unique) <= maxUnique:
                if not substring in appers:
                    appers[substring] = 0

                appers[substring] += 1

    return max(appers, key=appers.get)


components = "abcdbcde"
minLength = 3
maxLength = 3
maxUnique = 3

print(getMaxOccurences(components, minLength, maxLength, maxUnique))
