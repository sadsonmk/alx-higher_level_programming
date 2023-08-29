#!/usr/bin/python3
"""Defines the node and the singly linked list"""


class Node:
    """Defines the node"""

    def __init__(self, data, next_node=None):
        """constructor function to initialise a new node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieves the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data attribute"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node attribute"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initialises a new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position"""

        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curr = self.__head
            while curr.next_node is not None and curr.next_node.data < value:
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """The string representation of the list"""
        curr = self.__head
        output = []
        while curr is not None:
            output.append(str(curr.data))
            curr = curr.next_node
        result = "\n".join(output)
        return result
