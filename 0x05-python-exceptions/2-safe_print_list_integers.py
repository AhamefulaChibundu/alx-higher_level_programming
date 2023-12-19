#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        length = 0
        for nums in range(x):
            if isinstance(my_list[nums], int):
                length += 1
                print("{:d}".format(my_list[nums]), end="")
    except TypeError as err:
        print(err)
    else:
        print("")
        return length
