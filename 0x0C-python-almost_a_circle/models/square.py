#!/usr/bin/python3
'''Module Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info about this square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) is not 0:
            list_atrib = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atrib[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atrib[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_atrib = ['id', 'size', 'x', 'y']
        dic_res = {}

        for key in list_atrib:
            if key == 'size':
                dic_res[key] = getattr(self, 'width')
            else:
                dic_res[key] = getattr(self, key)

        return dic_res
