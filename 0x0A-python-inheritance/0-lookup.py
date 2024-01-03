#!/usr/bin/python3
"""Defines the lookup function."""


def lookup(obj):
    """Return a list of an object's available atrributes."""

    return (dir(obj))
