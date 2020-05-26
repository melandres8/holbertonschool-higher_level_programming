#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """_slots__ allow us to explicitly declare data members
    (like properties) and deny the creation of __dict__ and __weakref__
    (unless explicitly declared in __slots__ or available in a parent.)
    """
    __slots__ = ['first_name']
