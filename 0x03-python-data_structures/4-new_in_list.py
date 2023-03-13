#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific position without
    modifying the original list"""
    length = len(my_list)
    ne_list = my_list[:]
    if idx <= length:
        ne_list[idx] = element
        return(ne_list)
    elif idx < 0:
        return(my_list)
    else:
        return(my_list)
