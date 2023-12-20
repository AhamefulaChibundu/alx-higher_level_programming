#!/usr/bin/python3
"""
Defines a square by: based on 1-square.py
"""


class Square:
    """
    Define a Square class
    Attributes:
        None
    """
    def __init__(self, size=0):
        """
        __init__ Initialises the attributes of Square
        Attributes:
            size (int): The size of a square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
