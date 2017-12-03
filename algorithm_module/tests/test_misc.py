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


FIB_TESTDATA = [
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

PAL_DATA = [
    ('Rat', False),
    ('Civic', True),
    ('Evil olive', True),
    ('a', True)
]

PAL_FUNCS = [
    (misc.is_palindrome),
    (misc.is_palindrome2)
]

ANA_DATA = [
    ('a', 'a', True),
    ('a', 'b', False),
    ('abc', 'bca', True),
    ('thethebirdbirddog', 'birdthedogthebird', True),
    ('thethebirdbirddog', 'facebook', False)
]

@pytest.mark.parametrize("func", FIB_FUNCS)
@pytest.mark.parametrize("value_in, expected", FIB_TESTDATA)
def test_fib(value_in, expected, func):
    '''Tests search on ideally formatted array'''
    print('Test of' + func.__name__)
    print('test value:', value_in)
    print('expected result:', expected)
    assert func(value_in) == expected

@pytest.mark.parametrize("pal_func", PAL_FUNCS)
@pytest.mark.parametrize('string_in, expected_bool', PAL_DATA)
def test_palindrome(string_in, expected_bool, pal_func):
    '''Test the palindrom checker'''
    assert pal_func(string_in) == expected_bool

@pytest.mark.parametrize('str_in1, str_in2, expected_bool', ANA_DATA)
def test_anagram(str_in1, str_in2, expected_bool):
    '''Test the anagram checker'''
    assert misc.anagram_checker1(str_in1, str_in2) == expected_bool
