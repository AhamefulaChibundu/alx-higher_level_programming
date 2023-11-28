#!/usr/bin/python3
for m in range(ord('a'), ord('z') + 1):
    if m != ord('e') and m != ord('q'):
        print("{:c}".format(m), end="")
