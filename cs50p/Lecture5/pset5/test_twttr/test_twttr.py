from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""


def test_mixedcase():
    assert shorten("CS50") == "CS50"
    assert shorten("PyThOn") == "PyThn"


def test_numbers_and_symbols():
    assert shorten("123") == "123"
    assert shorten("h@ppy!") == "h@ppy!"
    assert shorten("t0day!") == "t0dy!"
