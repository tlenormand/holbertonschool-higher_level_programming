#!/usr/bin/python3
"""
module that creates an Object from a “JSON file

Functions:
    class_to_json: function that returns the dictionary description with
        simple data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object

    Args:
        obj: instance of a Class

    Returns:
        list, dictionary, string, integer and boolean
    """
    return obj.__dict__
