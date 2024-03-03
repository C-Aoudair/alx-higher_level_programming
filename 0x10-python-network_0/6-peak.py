#!/usr/bin/python3
"""Contains the find_peak function"""


def find_peak(list_of_integers):
    """Defines find_peak function"""

    if not list_of_integers:
        return None

    if (list_of_integers[0] > list_of_integers[1]):
        return list_of_integers[0]

    for i in range(1, len(list_of_integers) - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1] and
                list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]

    return list_of_integers[-1]
