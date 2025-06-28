from zad1testy import runtests


def chaos_index(T):
    indexed = list(enumerate(T))
    indexed.sort(key=lambda x: x[1])

    max_chaos = 0
    for sorted_index, (original_index, value) in enumerate(indexed):
        diff = abs(original_index - sorted_index)
        max_chaos = max(max_chaos, diff)

    return max_chaos


# if __name__ == "__main__":
#     T = [0, 2, 1.1, 2]
#     print(chaos_index(T))
runtests(chaos_index)
