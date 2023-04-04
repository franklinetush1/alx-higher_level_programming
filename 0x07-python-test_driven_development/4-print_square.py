#!/usr/bin/python3
"""Function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters
    Args:
        text: the string
    Raises:
        TypeError: If text input is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cpy = text[:]

    for a in ".?:":
        txt = cpy.split(a)
        cpy = ""
        for b in txt:
            c = b.strip(" ")
            cpy = a + b if cpy == "" else cpy + "\n\n" + b + a

    print(cpy[:-3], end="")
