#!/usr/bin/python3


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """method to get area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate if a number is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
