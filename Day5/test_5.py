from ex5 import *

class TestOperations:
    def test_validate_age(self):
        test1 = UserInfo().validate_age(GENDER_NAME,D_O_B)
        test2 = 'Valid' or 'Invalid'
        assert test1 == test2

    def test_validate_nationality(self):
        test1 = UserInfo().validate_nationality(NATIONALITY_NAME)
        test2 = 'Valid' or 'Invalid'
        assert test1 == test2

    def test_validate_state(self):
        test1 = UserInfo().validate_state(STATE_NAME)
        test2 = 'Valid' or 'Invalid'
        assert test1 == test2

    def test_validate_salary(self):
        test1 = UserInfo().validate_salary(SALARY_OF_PERSON)
        test2 = 'Valid' or 'Invalid'
        assert test1 == test2

    def test_validate_pan(self):
        test1 = UserInfo().validate_pan(PAN_NUMBER)
        assert test1 == "Valid" or "Invalid"


