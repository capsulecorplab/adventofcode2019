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


class Test2:
    @pytest.fixture
    def pc(self):
        return PasswordCracker()

    def test_meets_criteria(self, pc):
        assert pc._meets_criteria(112233, part=2) == True
        assert pc._meets_criteria(123444, part=2) == False
        assert pc._meets_criteria(111122, part=2) == True
        assert pc._meets_criteria(111222, part=2) == False

    def test_no_of_pw_combinations(self, pc):
        assert pc.no_of_pw_combinations(382345, 843167, part=2) == 290
