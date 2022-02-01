#!/usr/bin/python3
"""
module that write into a file

Functions:
    write_file: function that reads a text file (UTF8) and prints it to stdout
"""


def write_file(filename="", text=""):
    """
    function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: name of the file
        text: text to print

    Returns:
        (int) number of characters written
    """
    with open("filename", "w") as outFile:
        outFile.write(text)

    return len(text)
