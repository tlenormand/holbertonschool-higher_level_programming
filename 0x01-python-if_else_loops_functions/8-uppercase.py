#!/usr/bin/python3
def uppercase(str):

    for i in range(0, len(str)):
        char = ord(str[i])
        if char >= 97 and char <= 122:
            char -= 32
        STR = chr(char)
        print("{}".format(STR), end="")
    print("")
