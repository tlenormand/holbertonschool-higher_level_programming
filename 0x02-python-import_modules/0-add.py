#!/usr/bin/python3
"""imports function and prints the result"""

from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2

print("{} + {} = {}".format(a, b, add(a, b)))
