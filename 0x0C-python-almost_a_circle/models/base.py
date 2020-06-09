#!/usr/bin/python3
""" Base module
"""
import json
from os import path


class Base():
    """ Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @property
    def id(self):
        """ getter """
        return self.__id

    @id.setter
    def id(self, value):
        """ setter """
        self.__id = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string
            representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation
            of list_objs to a file
        """
        with open(cls.__name__ + '.json', 'w') as file:
            if list_objs is None or list_objs == []:
                file.write('[]')
            else:
                items = [item.to_dictionary() for item in list_objs]
                file.write(cls.to_json_string(items))

    @staticmethod
    def from_json_string(json_string):
        """ that returns the list of the JSON
            string representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with
            all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            new = cls(3, 6)
        else:
            new = cls(3)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'r') as file:
            if path.exists(filename):
                l_dic = Base.from_json_string(file.read())
                return list(cls.create(**dic) for dic in l_dic)
            else:
                return []
