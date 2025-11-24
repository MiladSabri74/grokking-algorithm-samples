import pytest
from binary_search import binary_search

sorted_list = [3,4,6,7,8,11,22,34,56,190]

def test_found_first():
    assert binary_search(sorted_list, 3) == 0

def test_found_last():
    assert binary_search(sorted_list, 190) == 9

def test_found_middle():
    assert binary_search(sorted_list, 22) == 6

def test_not_found_first():
    assert binary_search(sorted_list, 1) == -1

def test_not_found_last():
    assert binary_search(sorted_list, 200) == -1

def test_not_found_middle():
    assert binary_search(sorted_list, 33) == -1