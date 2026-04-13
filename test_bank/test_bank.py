from bank import value

def test_bank_hello():
    assert value("Hello,Mark") == 0

def test_bank_h():
    assert value("Hi,David") == 20

def test_bank_others():
    assert value("Yo, Peter") == 100
