from datetime import date
from seasons import calculate_minutes
import inflect


def test_calculate_minutes():
    birth = date(2000, 1, 1)
    today = date(2022, 1, 1)
    assert calculate_minutes(birth, today) == 11571840  # Minutos exactos en 22 años

    birth = date(1995, 1, 1)
    today = date(2000, 1, 1)
    assert calculate_minutes(birth, today) == 2629440  # Minutos exactos en 5 años

    birth = date(1998, 6, 20)
    today = date(2000, 1, 1)
    assert calculate_minutes(birth, today) == 806400  # Minutos entre dos fechas específicas


def test_convert_minutes_to_words():
    p = inflect.engine()

    # Verifica que la función convierte el número de minutos en palabras correctamente
    assert p.number_to_words(525600, andword="").capitalize() == "Five hundred twenty-five thousand, six hundred"
    assert p.number_to_words(1051200, andword="").capitalize() == "One million, fifty-one thousand, two hundred"
    assert p.number_to_words(2629440, andword="").capitalize() == "Two million, six hundred twenty-nine thousand, four hundred forty"
    assert p.number_to_words(6092640, andword="").capitalize() == "Six million, ninety-two thousand, six hundred forty"
    assert p.number_to_words(806400, andword="").capitalize() == "Eight hundred six thousand, four hundred"
