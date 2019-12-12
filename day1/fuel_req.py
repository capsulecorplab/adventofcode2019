################################################################################
# Filename:
# fuel_req.py
#
# Prerequisites:
# * Python3
#
# CLI usage:
# $ cd day1/
# $ python3 fuel_req.py
#
# Python REPL usage:
# >>> from fuel_req import m_fuel
# >>> m_fuel(1969)
# 654
# >>>
################################################################################

m_fuel = lambda mass: int(mass / 3 - 2)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        dump = f.read().split("\n")

    masses = []

    for _ in dump:
        try:
            masses.append(int(_))
        except:
            pass

    print(sum(list(map(m_fuel, masses))))
