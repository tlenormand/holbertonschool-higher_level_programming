#!/usr/bin/python3
"""
module that contain the base classs

Class:
    Base: this class will be the “base” of all other classes in this project
"""

import csv
import json
from os.path import exists


class Base:
    """
    this class will be the “base” of all other classes in this project

    Functions:
        __init__: init a Base

    Classmethod:
        save_to_file: function that writes the JSON string representation
            of list_objs to a file
        create: function that that returns an instance with all
            attributes already set
        load_from_file: function that returns a list of instances

    Staticmethod:
        def to_json_string: function that returns the JSON string
            representation of list_dictionaries
        to_json_string: function that returns the list of the JSON string
            representation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init a Base

        Arguments:
            id: id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """
        function that writes the JSON string representation of
            list_objs to a file

        Arguments:
            list_objs: list of all objects to include into file

        Returns:
            None
        """
        dict = []
        string = ""

        if list_objs is None:
            list_objs = []

        for obj in list_objs:
            dict.append(obj.to_dictionary())

        string = cls.to_json_string(dict)

        with open(cls.__name__ + ".json", "w") as fd:
            fd.write(string)
        fd.close()

    @classmethod
    def create(cls, **dictionary):
        """
        function that that returns an instance with all attributes already set

        Arguments:
            dictionary: can be thought of as a double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)

        new.update(**dictionary)

        return new

    @classmethod
    def load_from_file(cls):
        """
        function that returns a list of instances

        Returns:
            a list of instances
        """
        list_json = []
        list_instance = []

        if exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json") as fd:
                list_json = cls.from_json_string(fd.read())
            fd.close()

            for i in list_json:
                list_instance.append(cls.create(**i))

        return list_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        function that writes the csv string representation of
            list_objs to a file

        Arguments:
            list_objs: list of all objects to include into file

        Returns:
            None
        """
        rectangle_list = ["id", "width", "height", "x", "y", "\0"]
        square_list = ["id", "size", "x", "y", "\0"]
        write_list = ""

        if list_objs is None:
            list_objs = []

        with open(cls.__name__ + ".csv", "w") as fd:
            if list_objs is None or list_objs == []:
                fd.write("")
            else:
                if cls.__name__ == "Rectangle":
                    write_list = rectangle_list
                elif cls.__name__ == "Square":
                    write_list = square_list

                list_dict = csv.DictWriter(fd, fieldnames=write_list)
                for obj in list_objs:
                    list_dict.writerow(obj.to_dictionary())

        fd.close()

    @classmethod
    def load_from_file_csv(cls):
        """
        function that returns a list of instances

        Returns:
            a list of instances
        """
        list_instance = []

        if exists(cls.__name__ + ".csv"):
            with open(cls.__name__ + ".csv", "r") as fd:
                list_csv = csv.reader(fd)
                for i in list_csv:
                    if cls.__name__ == "Rectangle":
                        new = {
                            "id": int(i[0]),
                            "width": int(i[1]),
                            "height": int(i[2]),
                            "x": int(i[3]),
                            "y": int(i[4])
                        }

                    if cls.__name__ == "Square":
                        new = {
                            "id": int(i[0]),
                            "size": int(i[1]),
                            "x": int(i[2]),
                            "y": int(i[3])
                        }

                    new_instance = cls.create(**new)
                    list_instance.append(new_instance)

        return list_instance

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        function that returns the JSON string representation of
            list_dictionaries

        Returns:
            the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        function that returns the list of the JSON string representation

        Arguments:
            json_string: string representing a list of dictionaries

        Returns:
            the list of the JSON string representation
        """
        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)
