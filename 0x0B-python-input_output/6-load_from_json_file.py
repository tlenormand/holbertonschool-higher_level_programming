#!/usr/bin/python3
"""
module that creates an Object from a “JSON file

Functions:
    load_from_json_file: function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”

    Args:
        filename: text file

    Returns:
        None
    """
    with open(filename) as outFile:
        lineRead = outFile.read()

    outFile.close()

    return json.loads(lineRead)
