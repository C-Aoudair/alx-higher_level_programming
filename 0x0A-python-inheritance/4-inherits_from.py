#!/usr/bin/python3
"""  Define  inherits_from function  """


def  inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from.
    Args:
        obj: The object to be checked.
        a_class: The class to check with.
    Return: True if the object is an instance of a class that inherited from,
            the specified class, otherwise Fulse.
    """

    return issubclass(obj, a_class)
