#!/usr/bin/python3
def element_at(my_list, idx):
    """Retreives an element from a list"""
    length = len(my_list)
    if idx <= length:
        return(my_list[idx])
    elif idx < 0:
        return(my_list)
    else:
        return(my_list)
