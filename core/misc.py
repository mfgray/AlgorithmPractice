"""This module contains miscellenous pratice algorithms

The module contains common algorithms in python as practice
"""
#! /usr/bin/env python

def get_fib(nth_fib):
    '''Returns the nth fibonnacci number'''

    if nth_fib <= 0:
        return 0
    elif nth_fib == 1:
        return 1
    else:
        return get_fib(nth_fib - 1) + get_fib(nth_fib - 2)




if __name__ == '__main__':
    # Run automated tests
    import pytest
    pytest.main(['-sv', '../tests'])
