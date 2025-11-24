import pytest
from factorial import factorial

def test_factoial_0():
    assert (factorial(0) == 1)

def test_factoial_1():
    assert (factorial(1) == 1)

def test_factoial_5():
    assert (factorial(5) == 120)