# length of s is N
# O(N)


BEGIN = "BEGIN"
END = "END"
GOOD = "GOOD"
BAD = "BAD"


def main(chain: str) -> str:
    if chain.find(BEGIN) == -1 or chain.find(END) == -1:
        return BAD

    chain_split = chain.split(";")
    chain_split = list(map(lambda x: x.split("-"), chain_split))

    if any(len(pair) != 2 for pair in chain_split):
        return BAD

    if any(node == END for node, _ in chain_split):
        return BAD

    if any(node == BEGIN for _, node in chain_split):
        return BAD

    dict_chain = {key: value for key, value in chain_split}
    visited = {key: False for key, value in chain_split}

    # print(dict_chain)
    # print(visited)
    current = BEGIN

    while current != END:

        if visited.get(current, True):
            return BAD

        visited[current] = True
        current = dict_chain[current]

    return GOOD


if __name__ == "__main__":

    example1 = "7-10;BEGIN-5;5-3;3-7;10-END"
    example2 = "BEGIN-END"
    example3 = "3-END"
    example4 = "BEGIN-5;END-3"
    example5 = "BEGIN;END-3"
    example6 = "BEGIN-3;3-END-END-END"

    print(main(example1))
    print(main(example2))
    print(main(example3))
    print(main(example4))
    print(main(example5))
    print(main(example6))
