#!/usr/bin/python3
"""Difine to_json_string function"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string).
    Args:
        my_obj: The string object.
    Return: The JSON representation of my_obj.
    """
    import json

    return json.dumps(my_obj)
