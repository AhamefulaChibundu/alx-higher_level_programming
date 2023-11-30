#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_of_args = len(argv)
    if num_of_args == 1:
        print(f"{num_of_args -1} arguments.")
    elif num_of_args == 2:
        print(f"{num_of_args - 1} argument:")
    else:
        print(f"{num_of_args -1} arguments:")

    for m in range(1, num_of_args):
        print(f"{m}: {argv[m]}")
