#!/usr/bin/python3
i = 0
j = 1
while i < 8:
    while j < 10:
        print("{:d}{:d}, ".format(i, j), end='')
        j += 1
    i += 1
    j = i + 1
print("{:d}{:d}".format(i, j))
