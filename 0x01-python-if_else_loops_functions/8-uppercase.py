#!/usr/bin/python3
def uppercase(str):
    for m in str:
        if ord(m) >= ord('a') and ord(m) <= ord('z'):
            character = chr(ord(m) - 32)
        else:
            character = m
        print("{:s}".format(character), end="")
    print('')
