''' Tests for the array/list sort algorithms'''

import sys
import random
import pytest
sys.path.append("..")
from ..core import sorts

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
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ([1, 1, 3, 3, 6, 6, 8, 8], [1, 1, 3, 3, 6, 6, 8, 8]),
    ([1.1, 0.9, 0.99, 1, 1.01], [0.9, 0.99, 1, 1.01, 1.1])
    ]

SORT_FUNCS = [
    (sorts.bubble_sort),
    (sorts.selection_sort),
    (sorts.insertion_sort),
    (sorts.insertion_sort2),
    (sorts.merge_sort),
    (sorts.merge_sort),
    (sorts.quick_sort)
    ]

@pytest.fixture(scope='function')
def test_arr(request):
    '''Shuffles the test data'''
    random.seed = 19
    random.shuffle(request.param)
    return request.param

@pytest.mark.parametrize("sort_func", SORT_FUNCS)
@pytest.mark.parametrize("test_arr, ordered_arr",
                         TEST_DATA, indirect=['test_arr'])
def test_sorts(test_arr, ordered_arr, sort_func):
    '''Tests sort on ideally formatted array'''
    print('testing ' + sort_func.__name__)
    print('test array:', test_arr)
    print('sorted array:', ordered_arr)
    sort_func(test_arr)
    print(sort_func.__name__ + ' sorted array:\n\t', test_arr)
    assert test_arr == ordered_arr
