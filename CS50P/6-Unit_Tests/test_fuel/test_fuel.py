import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    assert convert("1/1") == 100

def test_convert_exceptions():
    with pytest.raises(ValueError):
        convert("5/4")  # Numerator > denominator
    with pytest.raises(ValueError):
        convert("a/4")  # Non-integer numerator
    with pytest.raises(ValueError):
        convert("4/b")  # Non-integer denominator
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Zero denominator

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

if __name__ == "__main__":
    pytest.main()
