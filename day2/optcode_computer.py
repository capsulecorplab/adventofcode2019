################################################################################
# Filename:
# optcode_computer.py
#
# Prerequisites:
# * Python3
#
# CLI usage:
# $ cd day2/
# $ python3 optcode_computer.py
#
# Python REPL usage:
# >>> from optcode_computer import compute
# >>> compute([1, 0, 0, 0, 99])
# [2, 0, 0, 0, 99]
# >>>
################################################################################

from typing import List


def compute(optcode: List[int]) -> List[int]:
    for i, e in enumerate(optcode):
        if i % 4 == 0:
            if e == 1:
                op = lambda x, y: x + y
            elif e == 2:
                op = lambda x, y: x * y
            elif e == 99:
                break
            else:
                raise Exception("Unknown element", e, "at index", i)
        elif i % 4 == 1:
            i1 = optcode[e]
        elif i % 4 == 2:
            i2 = optcode[e]
        elif i % 4 == 3:
            optcode[e] = op(i1, i2)
    return optcode


if __name__ == "__main__":
    from itertools import permutations

    # Part One
    with open("input.txt", "r") as f:
        optcode = list(map(lambda s: int(s), f.read().replace("\n", "").split(",")))
    optcode[1] = 12
    optcode[2] = 2
    compute(optcode)
    print(optcode[0])

    # Part Two
    for perm in permutations(range(100), 2):
        with open("input.txt", "r") as f:
            optcode = list(map(lambda s: int(s), f.read().replace("\n", "").split(",")))
        optcode[1] = perm[0]
        optcode[2] = perm[1]
        if compute(optcode)[0] == 19690720:
            print(100 * optcode[1] + optcode[2])
            break
