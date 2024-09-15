from bank import value
import pytest


def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0

def test_value_h():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("Hola") == 20

def test_value_other():
    assert value("goodbye") == 100
    assert value("Goodbye") == 100
    assert value("Greetings") == 100
    assert value("123hello") == 100
    assert value("Ahoy") == 100
