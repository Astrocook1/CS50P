from project import check_choice, check_account, password_checker
import pytest


def test_check_choice():
    assert check_choice("Y") == True

    with pytest.raises(ValueError):
        check_choice("Of course")

def test_check_account():
    assert check_account("CS50") == ("CS50", False)
    assert check_account("Non-existing") == ("Non-existing", False)

def test_password_checker():
    assert password_checker("CS50", "CS50pass") == True
    assert password_checker("CS50", "CS50password") == False
