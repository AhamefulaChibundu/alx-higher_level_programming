#!/usr/bin/python3
"""
This module is a function that adds two numbers
"""


def add_integer(a, b=98):
    """ Function that adds two integer and/or float numbers
    Arguments:
        a: first number
        b: second number
    Returns:
        The addition of the two given numbers
        If second number is not given it 98 would be assigned
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
