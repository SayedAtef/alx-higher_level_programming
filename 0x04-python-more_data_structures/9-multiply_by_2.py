#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multi_by_two_dir = a_dictionary.copy()
    list_of_keys = list(multi_by_two_dir.keys())

    for i in list_of_keys:
        multi_by_two_dir[i] *= 2

    return (multi_by_two_dir)
