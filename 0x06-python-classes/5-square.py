#!/usr/bin/python3
"""
Defines a square by: based on 4-square.py
"""


class Square:
    """
    Defines a Square class
    Attributes:
        No Attribute
    """
    def __init__(self, size=0):
        """
        Initialization the attributes of Square
        Attributes:
            size (int): The size of a square
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the value
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        print in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for m in range(self.__size):
                for n in range(self.__size):
                    print("#", end="")
                print()
