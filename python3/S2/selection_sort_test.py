import pytest
from selection_sort import selection_sort

def test_sorted_ascending_list():
    assert selection_sort([3,4,6,7,8,11], True) == [3,4,6,7,8,11]

def test_sorted_descending_list():
    assert selection_sort([9,8,5,4,3,2], False) == [9,8,5,4,3,2]

def test_unsorted_ascending_list():
    assert selection_sort([6,4,3,11,8,7], True) == [3,4,6,7,8,11]

def test_unsorted_descending_list():
    assert selection_sort([2,8,5,4,9,3], False) == [9,8,5,4,3,2]

def test_empty_ascending_list():
    assert selection_sort([], True) == []

def test_empty_descending_list():
    assert selection_sort([], False) == []