################################################################################
# Filename:
# test_fuel.py
#
# Prerequisites:
# * Python3
#
# Requirements:
# * pytest
#
# CLI usage:
# $ cd day1/
# $ pytest -v test_fuel.py
################################################################################

import pytest
from fuel_req import m_fuel


def test_fuel_req1():
    assert m_fuel(12) == 2


def test_fuel_req2():
    assert m_fuel(14) == 2


def test_fuel_req3():
    assert m_fuel(1969) == 654


def test_fuel_req4():
    assert m_fuel(100756) == 33583
