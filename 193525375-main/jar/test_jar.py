import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar1 = Jar(10)
    assert jar1.capacity == 10

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(6)
    jar.deposit(8)
    jar.withdraw(6)
    assert jar.size == 2

