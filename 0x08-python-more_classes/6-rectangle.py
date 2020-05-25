#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle():
    """Constructor method and
        public class attribute
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
            Instance attributes
            Args:
                width: (int) Rectangle width
                height: (int) Rectangle height
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter, retrieve the width of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retrieve the area of a rectangle
        """
        return int(self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width) + 2 * (self.__height)

    def __str__(self):
        """Representation of a string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for item in range(self.__height):
            string += '#' * self.__width
            string += '\n'
        string = string[:-1]
        return string

    def __repr__(self):
        """String representation of rectangle
        """
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        """Deconstrutor method
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
