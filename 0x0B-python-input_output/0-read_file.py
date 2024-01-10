#!/usr/bin/python3
"""This moudle is to open a file"""


def read_file(filename=""):
    """Reads a file that is encoded in utf-8"""
    with open(filename, encoding='utf-8') as m:
        text = m.read()
    print(text, end='')
