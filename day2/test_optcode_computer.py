################################################################################
# Filename:
# test_optcode_computer.py
#
# Prerequisites:
# * Python3
#
# Requirements:
# * pytest
#
# CLI usage:
# $ cd day2/
# $ pytest -v test_optcode_computer.py
################################################################################

import pytest
from optcode_computer import compute


def test_compute1():
    assert compute([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]


def test_compute2():
    assert compute([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]


def test_compute3():
    assert compute([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]


def test_compute4():
    assert compute([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def test_compute5():
    assert compute([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [
        3500,
        9,
        10,
        70,
        2,
        3,
        11,
        0,
        99,
        30,
        40,
        50,
    ]
