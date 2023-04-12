#!/usr/bin/python3
"""Function that writes to a text file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    args:
        filename:name of file to be written to
        text:text to be written
    returns:
        the number of characters written:"""
    with open(filename, 'w', encoding='utf-8') as f:
        no_of_chars = f.write(text)
    return(no_of_chars)
