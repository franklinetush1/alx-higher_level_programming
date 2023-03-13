#!/usr/bin/python3
def no_c(my_string):
    """ removes all characters c and C from a string."""
    new_string = my_string.translate({ord(a): None for a in "cC"})
    return new_string
