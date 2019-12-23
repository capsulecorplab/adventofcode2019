################################################################################
# Filename:
# secret_container.py
#
# Prerequisites:
# * Python3
#
# CLI usage:
# $> cd day4/
# $> python3 secret_container.py
#
# Python REPL usage:
# >>> from secret_container import PasswordCracker
# >>> pc = PasswordCracker()
# >>> pc.no_of_pw_combinations(382345, 843167)
# 460
# >>> pc.no_of_pw_combinations(382345, 843167, part=2)
# 290
# >>>
################################################################################

import re


class PasswordCracker:
    @classmethod
    def no_of_pw_combinations(
        cls, lower_bound: int, upper_bound: int, part: int = 1
    ) -> int:
        pw_combinations = []
        for pw in range(lower_bound, upper_bound + 1):
            if cls._meets_criteria(pw, part):
                pw_combinations.append(pw)
        return len(pw_combinations)

    @classmethod
    def _meets_criteria(cls, pw: int, part: int = 1) -> bool:
        if part == 1:
            return len(str(pw)) > 0 and cls._isincreasing(pw) and cls._hasdouble(pw)
        elif part == 2:
            return (
                len(str(pw)) > 0
                and cls._isincreasing(pw)
                and cls._hasdouble_not_of_larger_group(pw)
            )

    @staticmethod
    def _isincreasing(pw: int) -> bool:
        pw_str = str(pw)
        i_0 = 0
        for e in pw_str:
            if i_0 > int(e):
                return False
            i_0 = int(e)
        return True

    @staticmethod
    def _hasdouble_not_of_larger_group(pw: int) -> bool:
        pw_str = str(pw)
        two_or_more = []
        for _ in range(10):
            regex = re.findall(str(_), pw_str)
            if len(regex) >= 2:
                two_or_more.append(len(regex))
        if 2 in two_or_more:
            return True
        return False

    @staticmethod
    def _hasdouble(pw: int) -> bool:
        pw_str = str(pw)
        regex = re.findall("11|22|33|44|55|66|77|88|99|00", pw_str)
        return len(regex) > 0


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        password_range = [int(pw) for pw in re.findall("\d{6}", f.read())]

    lower_bound = password_range[0]
    upper_bound = password_range[1]

    pc = PasswordCracker()
    print(pc.no_of_pw_combinations(lower_bound, upper_bound))
    print(pc.no_of_pw_combinations(lower_bound, upper_bound, 2))
