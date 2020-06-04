#!/usr/bin/python3
""" Student to JSON
"""


class Student():
    """ Student class
    """
    def __init__(self, first_name, last_name, age):
        """ Constructor method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dict representation
            of a Student instance
        """
        dic = dict()
        if type(attrs) == list:
            for k, v in self.__dict__.items():
                if k in attrs:
                    dic[k] = v
        else:
            return self.__dict__
        return dic
