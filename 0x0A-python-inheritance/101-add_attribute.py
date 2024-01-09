#!/usr/bin/python3
"""
    101-add_attribute: add_attribute()
"""


def add_attribute(clas, name, value):
    """
        adds a new attribute if possible.
    """
    if hasattr(clas, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(clas, name, value)
