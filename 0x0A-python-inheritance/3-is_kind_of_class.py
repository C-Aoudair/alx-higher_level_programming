#!/usr/bin/python3
"""  Define is_kind_of_class function  """


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or an instance
        of a class that inherited from.
    Args:
        obj: The object to be checked.
        a_class: The class to check with.
    Return: True if the object is an instance or instance of a class that
            inherited from , the specified class, otherwise Fulse.
    """

    return isinstance(obj, a_class)
