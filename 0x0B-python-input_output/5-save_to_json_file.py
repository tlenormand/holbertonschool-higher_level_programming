#!/usr/bin/python3
"""
module that writes an Object to a text file, using a JSON representation

Functions:
    save_to_json_file: writes an Object to a text file, using a
        JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation

    Args:
        my_obj: objet
        filename: text file

    Returns:
        None
    """
    with open(filename, "w") as outFile:
        json.dump(my_obj, outFile)

    outFile.close()
