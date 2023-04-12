#!/usr/bin/python3
"""Function that appends text to a file"""


def append_write(filename="", text=""):
    """function that appends text to a file
    args:
        filename:name of file to be written to
        text:text to be written
    returns:
        the number of characters appended:"""
    with open(filename, 'a', encoding='utf-8') as f:
        no_of_chars = f.write(text)
    return(no_of_chars)
