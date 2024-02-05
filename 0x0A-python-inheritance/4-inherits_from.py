#!/usr/bin/python3
"""this func defines an inherited class-checking method."""


def inherits_from(obj, a_class):
    """this func checks if an object is an inherited instance of a class.
    Args:
        obj (any): object to check
        a_class (type): class to compare.
    Returns:
        boolean of inheritance.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
