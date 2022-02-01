#!/usr/bin/python3
"""
module class Student

Class:
    Student
"""


class Student:
    """
    class Student that defines a student

    Functions:
        __init__: init a student
        to_json: retrieves a dictionary representation of a Student instance
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

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance

        Returns: a dictionary representation of a Student instance
        """
        return self.__dict__
