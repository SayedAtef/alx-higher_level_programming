#!/usr/bin/python3

def uniq_add(my_list=[]):
    list_unique = set(my_list)
    number = 0

    for i in list_unique:
        number += i

    return (number)
