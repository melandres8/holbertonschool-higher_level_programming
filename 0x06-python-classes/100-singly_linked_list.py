#!/usr/bin/python3
"""Singly linked list"""


class Node():
    """Constructor method __init__"""
    def __init__(self, data, next_node=None):
        """
        Instances
        Attributes:
            Args:
                data (int): data to insert in a node
                next_node (Node): This is a new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList():
    """A new class to create a SLL"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert a node and Sorted a linked list"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return

        temp = self.__head
        if temp.data > value:
            new_node.next_node = temp
            self.__head = new_node
            return

        while temp.next_node:
            if temp.next_node.data > value:
                break
            temp = temp.next_node

        new_node.next_node = temp.next_node
        temp.next_node = new_node

    def __str__(self):
        """Returning the representation of a list"""
        data = []
        current = self.__head
        while current is not None:
            data.append(current.data)
            current = current.next_node
        return '\n'.join(str(i) for i in data)
