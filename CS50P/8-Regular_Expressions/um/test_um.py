from um import count

def test_single_um():
    assert count("um") == 1

def test_multiple_ums():
    assert count("um, hello, um world, um.") == 3

def test_no_um():
    assert count("hello, world!") == 0

def test_um_as_substring():
    assert count("yummy umbridge umbrella") == 0

def test_case_insensitive():
    assert count("Um, uM, UM.") == 3
