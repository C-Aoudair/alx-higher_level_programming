#!/usr/bin/python3
"""  Define is_same_class function  """


def is_same_class(obj, a_class):
    """Check if an object is an instance of a class
    Args:
        obj: The object to be checked.
        a_class: The class to check with.
    Return: True if the object is an instance of the class, otherwise Fulse.
    """

    if type(obj) is a_class:
        return True
    return False
