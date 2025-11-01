from plates import is_valid


def test_begins_with_letters_only():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C5") == False
    assert is_valid("1AAA") == False


def test_length():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("CS") == True
    assert is_valid("CS50") == True


def test_no_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS50!") == False
    assert is_valid("CS_50") == False
    assert is_valid("HELLO") == True


def test_number_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS5P0") == False
    assert is_valid("PI314") == True


def test_first_number_not_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("AB012") == False
    assert is_valid("AB123") == True
