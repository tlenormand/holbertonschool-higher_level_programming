#!/usr/bin/python3
char = 122
while char > 96:
    if char % 2 != 0:
        alphabet = char - 32
    else:
        alphabet = char
    print("{}".format(chr(alphabet)), end="")
    char -= 1
