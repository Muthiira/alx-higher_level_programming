#!/usr/bin/python3

""" defines a rectangle"""


from turtle import width


class Rectangle:
    """ defines a rectangle"""

    def __init__(self, width=0, height=0):
        """ defines width and height"""
        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    @property
    def width(self):
        """retrieves the width"""
        self.__width

    @width.setter
    def width(self, value):
        """ sets value of width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the width"""
        self.__height

    @height.setter
    def height(self, value):
        """ sets value of height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates area"""
        return self.__height * self.__width

    def perimeter(self):
        """calculates perimeter"""
        return 2 * (self.__height + self.__width)
