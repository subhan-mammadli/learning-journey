from seasons import calculate
import pytest
def test_valid():
    assert calculate("1988-04-04") == "Nineteen million, seven hundred eighty-one thousand, two hundred eighty minutes"
    assert calculate("1978-09-09") == "Twenty-four million, eight hundred fourteen thousand eighty minutes"
    assert calculate("2012-11-07") == "Six million, eight hundred forty-five thousand, seven hundred sixty minutes"

def test_invalid():
    with pytest.raises(SystemExit):
        assert calculate("2025-13-01") == "Invalid date"
    with pytest.raises(SystemExit):
        assert calculate("04 April, 1988") == "Invalid date"
    with pytest.raises(SystemExit):
        assert calculate("2025-12-32") == "Invalid date"

