#!/usr/bin/python3
"""class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """this func checks if an object is an instance or inherited instance of class.
    Args:
        obj (any): placeholder for the object to check.
        a_class (type): class to compare the type of obj to.
    Returns:
        Booleans of an instance.
    """
    if isinstance(obj, a_class):
        return True
    return False
