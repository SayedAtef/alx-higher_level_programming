#!/usr/bin/python3
"""mofule my list"""

class MyList(list):
    """Class my_list"""
    pass

    def print_sorted(self):
        """Method that sort a given list"""

        print(sorted(list(self)))
