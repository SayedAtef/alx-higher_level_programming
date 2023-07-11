#!/usr/bin/python3
"""class_to_json method"""


def class_to_json(obj):
    """
        returns representation with a simple data structure.
    """
    return obj.__dict__
