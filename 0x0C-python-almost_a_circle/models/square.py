#!/usr/bin/python3
""" Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter """
        return self.height

    @size.setter
    def size(self, value):
        """ setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigning attributes"""
        inst = ['id', 'size', 'x', 'y']
        if not args:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            for idx, attr in enumerate(args):
                setattr(self, inst[idx], attr)

    def to_dictionary(self):
        """ Dictionary representation
        """
        inst = ['id', 'size', 'x', 'y']
        return {i: getattr(self, i) for i in inst}
