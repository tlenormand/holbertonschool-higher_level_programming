#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data

        if next_node != "None" and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node


    @data.setter
    def data(self, value):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data

    @next_node.setter
    def next_node(self, value):
        if next_node != "None" and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node




class SinglyLinkedList:
