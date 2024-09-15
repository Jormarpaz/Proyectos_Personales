from numb3rs import validate

def test_valid():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("8.8.8.8") == True

def test_invalid_format():
    assert validate("275.3.6.28") == False  # fuera del rango
    assert validate("256.256.256.256") == False  # fuera del rango
    assert validate("192.168.1") == False  # solo tres números
    assert validate("192.168.1.1.1") == False  # cinco números
    assert validate("192.168.1.a") == False  # incluye una letra

def test_invalid_values():
    assert validate("-1.2.3.4") == False  # número negativo
    assert validate("300.100.100.100") == False  # fuera del rango
    assert validate("123.456.789.0") == False  # fuera del rango en múltiples partes
    assert validate("192.168.01.1") == True  # ceros a la izquierda no invalidan la dirección
