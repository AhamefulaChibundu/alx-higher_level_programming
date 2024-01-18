#!/usr/bin/python3
def uniq_add(my_list=[]):
    integers = set(my_list)   # set -> for collection without duplicates
    total = 0
    for integer in integers:
        total += integer
    return total
