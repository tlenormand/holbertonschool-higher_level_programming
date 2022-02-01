#!/usr/bin/python3
"""
module that returns an object (Python data structure) represented
by a JSON string

Functions:
    from_json_string: function that returns an object represented
        by a JSON string
"""

import json


def from_json_string(my_str):
    """
    function that returns an object represented by a JSON string

    Args:
        my_obj: objet

    Returns:
        (obj) object represented by a JSON string
    """
    return json.loads(my_str)
