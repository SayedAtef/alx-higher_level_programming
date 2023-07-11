#!/usr/bin/python3
"""from_json_string module"""
import json


def from_json_string(my_str):
    """
    from_json_string - returns an object represented by a JSON string:
    Args:
        my_str: json string
    Return: object
    """
    return json.loads(my_str)
