''' Tests for the array/list sort algorithms'''

import sys
import random
import pytest
sys.path.append("..")
from core import sorts

def setup_module(module):
    '''set up state for running the sort module algorithm tests'''
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

TEST_DATA = [
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([-1, 2], [-1, 2]),
    ([1, 2, 3], [1, 2, 3]),
    (list(range(20)), list(range(20))),
    ([1, 1, 1, 1, 1, 2, 555], [1, 1, 1, 1, 1, 2, 555]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1])
    ]

@pytest.fixture(scope='function')
def test_arr(request):
    '''Shuffles the test data'''
    random.seed = 19
    random.shuffle(request.param)
    return request.param

@pytest.mark.parametrize("test_arr, ordered_arr",
                         TEST_DATA, indirect=['test_arr'])
def test_bubble(test_arr, ordered_arr):
    '''Tests search on ideally formatted array'''
    print('test_bubble_sort')
    print('test array:', test_arr)
    print('sorted array:', ordered_arr)
    sorts.bubble_sort(test_arr)
    print('bubble sorted array:', test_arr)
    assert test_arr == ordered_arr
