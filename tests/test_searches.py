''' Tests for the array/list search algorithms'''

import sys
import pytest
sys.path.append("..")
from ..core import searches

def setup_module(module):
    '''set up state for running the search module algorithm tests'''
    print('setup_module       module:{!s}'.format(module.__name__))

def teardown_module(module):
    '''teardown for module'''
    print('teardown_module    module:{!s}'.format(module.__name__))


def setup_function(function):
    '''set up function states'''
    print('setup_function     function:{!s}'.format(function.__name__))

def teardown_function(function):
    '''teardown for function'''
    print('teardown_function  function:{!s}'.format(function.__name__))


TESTDATA = [
    ([1], 0, -1),
    ([1], 1, 0),
    ([1, 2], 2, 1),
    ([1, 2], 10, -1),
    ([1, 2, 3, 4, 5], 2, 1),
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], -10, -1),
    ([1, 2, 3, 4, 5], 5, 4),
    ([1, 2, 3, 4, 5], 1, 0),
    ([-1, 2, 3, 4, 5], 2, 1)
    ]

MIN_TEST_DATA = [
    ([1, 2, 3, 4, 5, 8], 0),
    ([6, 6, 3, 4, 5, 8], 2),
    ([1], 0),
    ([1, 1, 1], 0),
    ([6, 6, 3, 3, 5, -8], 5)
]

@pytest.mark.parametrize("test_arr, value, value_idx", TESTDATA)
def test_list(test_arr, value, value_idx):
    '''Tests search on ideally formatted array'''
    print('test_binary_search')
    print('test array:', test_arr)
    print('test value:', value, 'test value index:', value_idx)
    assert searches.binary_search(test_arr, value) == value_idx

@pytest.mark.parametrize("test_arr, value_idx", MIN_TEST_DATA)
def test_min_search(test_arr, value_idx):
    '''Tests search on ideally formatted array'''
    print('test min')
    print('test array:', test_arr)
    print('test value index:', value_idx)
    assert searches.min_search(test_arr) == value_idx
