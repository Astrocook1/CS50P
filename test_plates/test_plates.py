import plates
from plates import is_valid

def test_plates_length():
    assert is_valid("A") == False
    assert is_valid("AAAA222") == False
    assert is_valid("AA") == True

def test_plates_starts_with_letters():
    assert is_valid("A2") == False
    assert is_valid("AB") == True

def test_plates_numbers_at_the_end():
    assert is_valid("ABC2D") == False
    assert is_valid("ABC23") == True

def test_plates_punctuation():
    assert is_valid("AA?22") == False
    assert is_valid("AA 22") == False

def test_plates_zeros():
    assert is_valid("ABC023") == False
    assert is_valid("ABC230") == True
