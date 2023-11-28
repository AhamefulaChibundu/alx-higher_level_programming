#!/usr/bin/python3
for first_digit in range(9):
    for second_digit in range((first_digit + 1), 10):
        if first_digit == 8:
            print("{}{}".format(first_digit, second_digit))
        else:
            print("{}{}".format(first_digit, second_digit), end=", ")
