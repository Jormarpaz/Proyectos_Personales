import pytest
from plates import is_valid

def test_valid_length():
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_starts_with_letters():
    assert is_valid("AB123") == True
    assert is_valid("A12345") == False
    assert is_valid("123ABC") == False

def test_no_invalid_characters():
    assert is_valid("ABC123") == True
    assert is_valid("AB@123") == False
    assert is_valid("AB 123") == False

def test_correct_number_position():
    assert is_valid("AB123") == True
    assert is_valid("AB012") == False
    assert is_valid("AB12C3") == False

def test_no_leading_zero():
    assert is_valid("AB123") == True
    assert is_valid("AB012") == False
    assert is_valid("AB0") == False
