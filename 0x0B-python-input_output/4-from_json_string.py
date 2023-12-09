#!/usr/bin/python3
"""Define from_json_string function."""


def from_json_string(my_str):
    """Returns an object representation by a JSON string.
    Args:
        my_str: The string must be converted from json.
    Return: Object (python data structure.
    """
    import json

    return json.loads(my_str)
