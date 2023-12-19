#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for m in range(x):
            print("{}".format(my_list[m]), end="")
    except IndexError:
        return m
    else:
        return x
    finally:
        print("")
