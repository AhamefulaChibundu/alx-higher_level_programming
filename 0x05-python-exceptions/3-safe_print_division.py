#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        my_quotient = a / b
    except (ZeroDivisionError, FloatingPointError):
        my_quotient = None
    finally:
        print("Inside result: {}".format(my_quotient))
        return my_quotient
