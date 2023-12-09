#!/usr/bin/python3
"""Define save_to_json_file function."""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.
    Args:
        my_obj: The object must be written.
        filename: The name of the file to write in.
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
