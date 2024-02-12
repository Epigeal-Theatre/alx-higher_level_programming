#!/usr/bin/python3
"""this func defines a module appends a string."""


def append_write(filename="", text=""):
    """we append a string to the end of a UTF8 text file.
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
