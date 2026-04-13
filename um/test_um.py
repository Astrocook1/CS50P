import pytest
from um import count

def test_normal():
    assert count("Um thanks, I appreciate you") == 1
    assert count("House") == 0

def test_in_words():
    assert count("This is yummy") == 0

def test_punctuations_and_spaces():
    assert count("Beans,um,rice") == 1
    assert count("Rice and um stew") == 1
