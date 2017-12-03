"""
The module contains common algorithms implemented in python for practice
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

    for _ in range(nth_fib): #is this use of '_' pythonic? Google results unclear
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
    '''Tests if the string of lower case letters is a palindrome
    Recursively compares the first and last letter,
    returning false if not equal, calling itself on the inner characters
    if equal until the length is 1 or 0 and then return True'''
    if (len(plain_str) == 1) or (len(plain_str) == 0):
        return True
    elif plain_str[0] == plain_str[-1]:
        return is_palindrome_helper(plain_str[1:-1])
    return False

def anagram_checker1(str_in1, str_in2):
    '''Returns True if str_in1 and str_in2 are anagrams'''

    result = True

    tally_str1 = letter_tally(str_in1)
    tally_str2 = letter_tally(str_in2)

    if set(tally_str1) == set(tally_str2):
        for key in tally_str1:
            if tally_str1[key] == tally_str2[key]:
                pass
            else:
                result = False
    else:
        result = False

    return result

def letter_tally(str_in):
    '''helper function for anagram checker 1.
    returns a dictionary with the unique letters as keys and
    the number of occurances as the values'''
    tally = {}
    for letter in str_in:
        if letter in tally:
            tally[letter] += 1
        else:
            tally[letter] = 1
    return tally

if __name__ == '__main__':
    # Run automated tests
    import pytest
    pytest.main(['-sv', '../tests/test_misc.py'])
