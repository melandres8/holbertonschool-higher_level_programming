#!/usr/bin/python3
""" Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from
        Base class module
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method and using
            the constructor method from
            Base module
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """ Below here I'm defining getter and setter
        properties.
    """
    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Area function
        """
        return self.__width * self.__height

    def display(self):
        """ Printing rectangles
        """
        for item2 in range(self.__y):
            print()
        for item in range(self.__height):
            print(" " * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """ String representation
        """
        strgn = "[{}] ({}) ".format(type(self).__name__, self.id)
        strgn += "{}/{} ".format(self.__x, self.__y)
        if type(self) is Rectangle:
            strgn += "- {}/{}".format(self.__width, self.__height)
        else:
            strgn += "- {}".format(self.__height)
        return strgn

    def update(self, *args, **kwargs):
        """ Assigning args
        """
        if args:
            inst = ['id', 'width', 'height', 'x', 'y']
            for idx, attr in enumerate(args):
                if idx < 5:
                    setattr(self, inst[idx], attr)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Dictionary representation
        """
        inst = ['id', 'width', 'height', 'x', 'y']
        return {i: getattr(self, i) for i in inst}
