#!/usr/bin/python3


class MyList(list):
    """Class my_list"""
    pass

    def print_sorted(self):
        """Method that sort a given list"""

        print(sorted(list(self)))
