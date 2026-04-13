import pytest
import fuel
from fuel import convert,gauge

def test_fuel_convert_results():
    assert convert("1/2") == 50


def test_fuel_gauge_results():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_fuel_splitting():
    with pytest.raises(ValueError):
        convert("2-3")


def test_fuel_integers():
    with pytest.raises(ValueError):
        convert("a/3")


def test_fuel_negative_integers():
    with pytest.raises(ValueError):
        convert("-1/-3")

def test_fuel_negative_fractions():
    with pytest.raises(ValueError):
        convert("-2/3")


def test_fuel_greater_numerators():
    with pytest.raises(ValueError):
        convert("4/3")


def test_fuel_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

