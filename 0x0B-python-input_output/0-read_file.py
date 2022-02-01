#!/usr/bin/python3
"""
module that read and print a file

Functions:
    read_file: function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: name of the file

    Returns:
        None
    """
    with open("filename", "r") as outFile:
        print(outFile.read(), end="")
