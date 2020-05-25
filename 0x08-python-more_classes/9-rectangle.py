#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle():
    """Constructor method and
        public classes attributes
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            Instance attributes
            Args:
                width: (int) Rectangle width
                height: (int) Rectangle height
        """
        self.width = width
        self.height = height
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
        """Perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width) + 2 * (self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Implementing a staticmethod
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Implementing a classmethod
        """
        return cls(size, size)

    def __str__(self):
        """Representation of a string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for item in range(self.__height):
            string += str(self.print_symbol) * self.__width
            string += '\n'
        string = string[:-1]
        return string

    def __repr__(self):
        """String representation of rectangle
        """
        return self.print_symbol

    def __del__(self):
        """Deconstrutor method
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
