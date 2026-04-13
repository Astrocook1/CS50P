from numb3rs import validate

def test_no_of_dots():
    assert validate("2.2.2.2.2") == False
    assert validate("1.2.3.4") == True

def test_range_of_numbers():
    assert validate("1.2.3.555") == False
    assert validate("255.0.255.0") == True

def test_correct_notation():
    assert validate("3.4.5.88") == True
    assert validate("1..3.5") == False

def test_integers():
    assert validate("cat") == False
