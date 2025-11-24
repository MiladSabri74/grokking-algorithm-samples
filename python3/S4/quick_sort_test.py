import pytest
from quick_sort import quick_sort

def test_unsorted_list():
    assert (quick_sort([3,5,4,1,7]) == [1,3,4,5,7])

def test_sorted_list():
    assert (quick_sort([1,3,4,5,7]) == [1,3,4,5,7])