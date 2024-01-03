#!/usr/bin/python3
"""Define the MyList class that inherits from list."""


class MyList(list):
    """Inherits from list and contains print_sorted method"""

    def print_sorted(self):
        print(sorted(self))
