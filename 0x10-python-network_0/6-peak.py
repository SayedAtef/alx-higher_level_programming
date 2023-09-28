#!/usr/bin/python3
"""Finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """Finds a peak in a list of integers"""
    l_o_i = list_of_integers
    # if there is no list of integers return None
    if l_o_i == [] or l_o_i is None:
        return None
    length = len(l_o_i)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if l_o_i[mid] > l_o_i[mid - 1] and l_o_i[mid] > l_o_i[mid + 1]:
            return l_o_i[mid]
        if l_o_i[mid - 1] > l_o_i[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return l_o_i[start]
