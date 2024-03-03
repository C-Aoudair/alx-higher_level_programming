#!/usr/bin/python3
""" contains find_peak function"""


def find_peak(myList):
    '''
        Finds the peak in a list of numbers
    '''

    if not myList:
        return None

    left = 0
    right = len(myList) - 1

    while left < right:

        middle = (left + right) // 2

        if (myList[middle] > myList[middle - 1] and
                myList[middle] > myList[middle + 1]):
            break

        if myList[middle + 1] > myList[middle - 1]:
            left = middle + 1
        else:
            right = middle

    return myList[left]
