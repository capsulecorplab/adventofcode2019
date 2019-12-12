################################################################################
# Filename:
# test_fuel_req_recursive.py
#
# Prerequisites:
# * Python3
#
# Requirements:
# * pytest
#
# CLI usage:
# $ cd day1/
# $ pytest -v test_fuel_req_recursive.py
################################################################################

import pytest
from fuel_req_recursive import m_fuel


def test_fuel_req1():
    assert m_fuel(14) == 2


def test_fuel_req2():
    assert m_fuel(1969) == 966


def test_fuel_req3():
    assert m_fuel(100756) == 50346
