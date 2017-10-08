"""This is the search algorithm module

The module contains common search algorithms in python as practice
"""
#! /usr/bin/env python

def binary_search(input_array, value):
    '''Returns the index of 'value' in the input array or -1 if 'value'
    is not contained in the array subject to the constraint that the
    input array contains no duplicates and is in ascending order
    '''

    low = 0
    high = len(input_array) - 1

    while low <= high:
        '''core logic: repeatedly check if middle index is the value and
        return the index if it is. If not, sets either hi or lo, as appropriate,
         to the mid index
        and loops again '''

        mid = (low + high) // 2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == '__main__':
    # Run automated tests
    import pytest
    pytest.main(['-sv', '../tests/test_searches.py'])
