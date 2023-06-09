#!/usr/bin/python3
"""rectangle class module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialize the attrubutes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """get the area"""
        return self.__width * self.__height

    def __str__(self):
        """return the next string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
