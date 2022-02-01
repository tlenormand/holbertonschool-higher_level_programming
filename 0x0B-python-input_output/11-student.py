#!/usr/bin/python3
"""
module class Student

Class:
    Student
"""

import json


class Student:
    """
    class Student that defines a student

    Functions:
        __init__: init a student
        to_json: retrieves a dictionary representation of a Student instance
        reload_from_json: replaces all attributes of the Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        init a student

        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved

        Args:
            attrs: attributes

        Returns: a dictionary representation of a Student instance

        """
        if type(attrs) is list:
            return {x: self.__dict__.get(x)
                    for x in attrs if x in self.__dict__}

        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance

        Args:
            json: new dictionary

        Returns:
            None
        """
        for x, y in json.items():
            setattr(self, x, y)
