''' Tests for the misc algorithms'''
import sys
import pytest
sys.path.append("..")

from ..core import misc

def setup_module(module):
    '''set up state for module algorithm tests'''
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
    (0, 0),
    (1, 1),
    (1, 1),
    (2, 1),
    (5, 5),
    (8, 21)
    ]

FIB_FUNCS = [
    (misc.get_fib),
    (misc.get_fib_iter),
    (misc.get_fib_recur_iter),
    (misc.get_fib_recur_memo)
]

@pytest.mark.parametrize("func", FIB_FUNCS)
@pytest.mark.parametrize("value_in, expected", TESTDATA)
def test_fib(value_in, expected, func):
    '''Tests search on ideally formatted array'''
    print('Test of' + func.__name__)
    print('test value:', value_in)
    print('expected result:', expected)
    assert func(value_in) == expected
