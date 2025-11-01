import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_convert_invalid():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("-3/4")
    with pytest.raises(ValueError):
        convert("5/4")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
