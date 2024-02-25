#!/usr/bin/python3
"""class to make base """

import json


class Base():
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns string rep of list_dictionaries"""
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """list of objects to a JSON file"""
        list_objs = list_objs or []
        new_dictionary = [object.to_dictionary() for object in list_objs]
        json_string = cls.to_json_string(new_dictionary)
        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as file:
            return (file.write(json_string))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the json string rep"""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(
            dictionary['size'])
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load objects from JSON file and return list of objects."""
        file_name = cls.__name__ + ".json"
        objects = []

        try:
            with open(file_name, "r") as file:
                list_dicts = cls.from_json_string(file.read())
                objects = [cls.create(**obj_dict) for obj_dict in list_dicts]
        except FileNotFoundError:
            pass

        return objects
