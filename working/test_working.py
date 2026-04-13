import pytest
from working import convert

def test_normal():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"

def test_incorrect_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
        convert("12:00 AM to 13:00 PM")

def test_correct_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

