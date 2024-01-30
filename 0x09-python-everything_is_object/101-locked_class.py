#!/usr/bin/python3
"""This guy defines a locked class"""


class LockedClass:
    """
    and it only allows instatiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
