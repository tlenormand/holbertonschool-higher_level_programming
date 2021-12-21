#!/usr/bin/python3
for char in range(122, 96, -1):
    if char % 2 != 0:
        print("{}".format(chr(char - 32)), end="")
    else:
        print("{}".format(chr(char)), end="")
