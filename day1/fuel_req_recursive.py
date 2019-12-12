################################################################################
# Filename:
# fuel_req_recursive.py
#
# Prerequisites:
# * Python3
#
# CLI usage:
# $ cd day1/
# $ python3 fuel_req_recursive.py
#
# Python REPL usage:
# >>> from fuel_req_recursive import m_fuel
# >>> m_fuel(1969)
# 966
# >>>
################################################################################


m_fuel = (
    lambda mass: int(mass / 3 - 2) + m_fuel(int(mass / 3 - 2))
    if int(mass / 3 - 2) > 0
    else 0
)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        dump = f.read().split("\n")

    masses = []
    for _ in dump:
        try:
            masses.append(int(_))
        except:
            pass
    print(sum(list(map(lambda mass: m_fuel(mass), masses))))
