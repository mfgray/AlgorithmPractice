"""This is the sort algorithm module

The module contains common sort algorithms in python as practice
"""
#! /usr/bin/env python



def bubble_sort(arr_in):
    '''Implementation of the bubble sort.
    Sorts the array in place'''

    for i, _ in enumerate(arr_in):
        for j in range(len(arr_in) - i - 1):
            if arr_in[j] > arr_in[j+1]:
                swap_elems(arr_in, j+1, j)

def selection_sort(arr_in):
    '''Implementation of the selection sort.
    Sorts the array in place'''
    for i, _ in enumerate(arr_in):
        low_idx = i

        for j in range(i + 1, len(arr_in)):
            if arr_in[j] < arr_in[low_idx]:
                low_idx = j

        swap_elems(arr_in, i, low_idx)

def swap_elems(arr_in, index1, index2):
    '''Helper that swaps the position of the array entries by index
    arr_in - the array for with the elements to be swapped
    index1 - index of one of the elements to be swapped
    index2 - index of the second element to be swapped
    '''
    temp_stored_value = arr_in[index2]
    arr_in[index2] = arr_in[index1]
    arr_in[index1] = temp_stored_value


if __name__ == '__main__':
    # Run automated tests
    import pytest
    pytest.main(['-sv', '../tests/test_sorts.py'])
