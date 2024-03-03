#!/usr/bin/python3
""" contains find_peak function"""


def find_peak(list_of_integers):
    '''
        Finds the peak in a list of numbers
    '''

    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers)

    middle = (length - 1) // 2

    if (list_of_integers[middle] > list_of_integers[middle - 1] and
    list_of_integers[middle] > list_of_integers[middle + 1]):
        return list_of_integers[middle]

    if list_of_integers[middle] > list_of_integers[middle + 1]:
        return find_peak(list_of_integers[:middle])
    else:
        return find_peak(list_of_integers[middle + 1:])
