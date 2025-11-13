from jar import Jar
import pytest


def test_init():
    jar = Jar()

    assert jar.capacity == 12
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)

    jar = Jar(13)
    with pytest.raises(ValueError):
        jar.size = 14

    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.size = 11

    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.size = -1


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(11)
    assert jar.deposit(10) == None

    jar = Jar(11)
    assert jar.deposit(9) == None

    with pytest.raises(ValueError):
        Jar().deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)

    assert jar.withdraw(10) == None
    assert jar.withdraw(1) == None

    with pytest.raises(ValueError):
        jar.withdraw(13)
