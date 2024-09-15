import pytest
from twttr import shorten


def test_shorten_vowels():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Apple") == "ppl"
    assert shorten("Android") == "ndrd"
    assert shorten("Ubiquitous") == "bqts"

def test_shorten_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("aPpLe") == "PpL"
    assert shorten("AnDrOiD") == "nDrD"

def test_shorten_no_vowels():
    assert shorten("Rhythm") == "Rhythm"
    assert shorten("Syzygy") == "Syzygy"

def test_shorten_with_numbers():
    assert shorten("1234") == "1234"
    assert shorten("Twi77er") == "Tw77r"

def test_shorten_with_punctuation():
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("CS50's problem set.") == "CS50's prblm st."
