from um import count


def test_valid():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("yummy") == 0
