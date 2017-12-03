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

def insertion_sort(arr_in):
    '''Implementation of the selection sort.
    Sorts the array in place'''

    for i in range(1, len(arr_in)):
        val = arr_in[i]
        idx = i

        for j in range(i, 0, -1):

            if val < arr_in[j - 1]:
                arr_in[j] = arr_in[j - 1]
                idx -= 1
            else:
                break

        arr_in[idx] = val

def insertion_sort2(arr_in):
    '''Implementation of the selection sort.
    Sorts the array in place'''

    for i in range(1, len(arr_in)):
        val = arr_in[i]
        j = i

        while (j - 1 >= 0) and (arr_in[j - 1] > val):
            arr_in[j] = arr_in[j - 1]
            j -= 1

        arr_in[j] = val


def merge_sort(arr_in):
    '''Implementation of merge sort.
    Sorts the array in place'''
    lhs = 0
    rhs = len(arr_in) - 1
    arr_cop = [val for val in arr_in]

    merge_sort_partition_(arr_in, arr_cop, lhs, rhs)

def merge_sort_partition_(arr_in, arr_cop, lhs, rhs):
    '''Recursion and divide step of merge sort.
    Sorts the array in place'''
    if rhs > lhs:
        #mid index
        mid = (rhs + lhs)//2

        #divide
        merge_sort_partition_(arr_in, arr_cop, lhs, mid)
        merge_sort_partition_(arr_in, arr_cop, mid + 1, rhs)

        #merging and sorting
        merge_sort_combine_(arr_in, arr_cop, lhs, mid, rhs)

def merge_sort_combine_(arr_in, arr_cop, lhs, mid, rhs):
    '''Combine step of merge sort.
    Sorts the array in place'''
    left = lhs
    right = mid + 1
    i = lhs

    while (left <= mid) and (right <= rhs):
        if arr_cop[left] <= arr_cop[right]:
            arr_in[i] = arr_cop[left]
            i += 1
            left += 1
        else:
            arr_in[i] = arr_cop[right]
            i += 1
            right += 1

    if left <= mid:
        arr_in[i:rhs+1] = arr_cop[left:mid+1]
    if right <= rhs:
        arr_in[i:rhs+1] = arr_cop[right:rhs+1]

    arr_cop[lhs:rhs+1] = [val for val in arr_in[lhs:rhs+1]]



def quick_sort(arr_in):
    '''Basic implementation of quick sort algorithm'''
    lhs = 0
    rhs = len(arr_in) - 1

    quick_sort_(arr_in, lhs, rhs)

def quick_sort_(arr_in, lhs, rhs):
    '''Quick sort core logic '''
    if rhs > lhs:

        #partition all elemnts lower than the pivot to the left
        pivot_idx = quick_sort_partition(arr_in, lhs, rhs)

        #recursively sort the partitioned halves
        quick_sort_(arr_in, lhs, pivot_idx - 1)
        quick_sort_(arr_in, pivot_idx + 1, rhs)

def quick_sort_partition(arr_in, lhs, rhs):
    '''Quick sort partitioning step
    Move all elements less than the pivot value
    to the left side of the pivot'''
    pivot = lhs
    pivot_val = arr_in[rhs]

    for i in range(lhs, rhs):
        if arr_in[i] <= pivot_val:
            swap_elems(arr_in, pivot, i)
            pivot += 1

    swap_elems(arr_in, pivot, rhs)
    return pivot

# ---------------- sort helpers -----------------

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
