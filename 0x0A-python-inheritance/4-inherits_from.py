#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Method that returns True if an object is an instance of a class
    that inherited from another object"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
