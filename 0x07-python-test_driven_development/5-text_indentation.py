#!/usr/bin/python3
"""
Module composed by func that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """ Func prints 2 new lines after ".?:" characters
    Args:
        text: input string
    Returns:
        No return value
    Raises:
        TypeError: If text is not str
    """

    if type(text) is not str:
        raise TypeError("text must be string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
