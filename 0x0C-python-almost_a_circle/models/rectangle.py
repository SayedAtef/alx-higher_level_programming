#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def area(self):
        '''Area of this rectangle.'''
        return self.width * self.height

    def display(self):
        '''Prints string representation of this rectangle.'''
        st = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(st, end='')

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returs a dictionary with properties """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
