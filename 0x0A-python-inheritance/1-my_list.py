#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """
    class MyList that inherits from list

    Functions:
        __init__: init a Mylist
        print_sorted: prints the list sorted, ascending sort
    """
    def __init__(self, data=list()):
        """
        init a Mylist

        Args:
            data (int): data of my list

        Returns: None
        """
        self.list = list(data)

    def print_sorted(self):
        """
        prints the list sorted, ascending sort

        Returns: None
        """
        print("{}".format(sorted(self)))
