#!/usr/bin/python3
"""
module that write into a file

Functions:
    append_write: function that reads a text file (UTF8) and prints it
        to stdout
"""


def append_write(filename="", text=""):
    """
    function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: name of the file
        text: text to print

    Returns:
        (int) number of characters written
    """
    with open("filename", "a") as outFile:
        outFile.write(text)

    outFile.close()

    return len(text)
