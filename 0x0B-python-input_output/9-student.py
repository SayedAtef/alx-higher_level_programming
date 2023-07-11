#!/usr/bin/python3
"""class Student."""


class Student:
    """
        A class students that defines a student:
        Attributes:
            first_name (str): name of student.
            last_name (str): name of student.
            age (int): age of student.
        Methods:
            __init__ - initialize Student instance.
            to_json - retrieves represntation of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """Initialise Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a representation of Student."""
        return self.__dict__
