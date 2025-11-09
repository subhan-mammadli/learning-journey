from numb3rs import validate


def test_valid_ip():
    assert validate("192.168.0.1") == True
    assert validate("10.0.0.254") == True
    assert validate("255.255.255.255") == True

def test_invalid_ip():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False
    assert validate("cat") == False

