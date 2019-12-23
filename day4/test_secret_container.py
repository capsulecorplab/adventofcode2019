from secret_container import PasswordCracker
import pytest


class Test1:
    @pytest.fixture
    def pc(self):
        return PasswordCracker()

    def test_meets_criteria(self, pc):
        assert pc._meets_criteria(111111) == True

    def test_isincreasing(self, pc):
        assert pc._isincreasing(223450) == False

    def test_hasdouble(self, pc):
        assert pc._hasdouble(123789) == False

    def test_no_of_pw_combinations(self, pc):
        assert pc.no_of_pw_combinations(382345, 843167) == 460
