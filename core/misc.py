"""This module contains miscellenous pratice algorithms

The module contains common algorithms in python as practice
"""
#! /usr/bin/env python

def get_fib(nth_fib):
    '''Returns the nth fibonnacci number with innefficient recursion'''
    if nth_fib <= 0:
        return 0
    elif nth_fib == 1:
        return 1
    else:
        return get_fib(nth_fib - 1) + get_fib(nth_fib - 2)

def get_fib_iter(nth_fib):
    '''Returns the nth fibonnacci number with iterative loop'''
    first, second = 0, 1

    for _ in range(nth_fib): #is this use of _ pythonic? Google results unclear
        first, second = second, first + second

    return first

def get_fib_recur_iter(nth_fib):
    '''Returns the nth fibonnacci number with recursive loop'''
    return fib_recur_iter(nth_fib, 0, 1)
def fib_recur_iter(nth_fib, first, second):
    '''Helper for function "get_fib_recur_iter"
    nth_fib serves as a counter
    first is the current fibonacci value at each call
    The value is built up as in the iterative method'''
    if nth_fib == 0:
        return first
    return fib_recur_iter(nth_fib - 1, second, first + second)

def get_fib_recur_memo(nth_fib):
    '''Returns the nth fibonnacci number with recursive and memoisation'''
    memo = {0: 0, 1:1}
    return fib_recur_memo(nth_fib, memo)

def fib_recur_memo(nth_fib, memo):
    '''Helper for function "get_fib_recur_memo" '''
    if nth_fib in memo:
        return memo[nth_fib]

    memo[nth_fib] = (fib_recur_memo(nth_fib - 1, memo)
                     + fib_recur_memo(nth_fib - 2, memo))
    return memo[nth_fib]

def is_palindrome(str_in):
    '''Checks if a string is a palindrome
    str_in - a string not containing punctuation aside from spaces'''
    plain_str = str_in.replace(' ', '').lower()
    rev_str = ''.join(reversed(plain_str))

    if rev_str == plain_str:
        return True
    return False

def is_palindrome2(str_in):
    '''Checks if a string is a palindrome
    str_in - a string not containing punctuation aside from spaces'''
    plain_str = str_in.replace(' ', '').lower()

    return is_palindrome_helper(plain_str)

def is_palindrome_helper(plain_str):

    if (len(plain_str) == 1) or (len(plain_str) == 0):
        return True
    elif plain_str[0] == plain_str[-1]:
        return is_palindrome_helper(plain_str[1:-1])
    return False


if __name__ == '__main__':
    # Run automated tests
    import pytest
    pytest.main(['-sv', '../tests'])
