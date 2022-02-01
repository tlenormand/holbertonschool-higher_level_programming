#!/usr/bin/python3
"""
module that returns the JSON representation of an object

Functions:
    to_json_string: function that returns the JSON representation of an object
"""

import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object

    Args:
        my_obj: objet

    Returns:
        (string) JSON representation of an object
    """
    return json.dumps(my_obj)
