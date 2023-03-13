#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete value at a given index"""
    if idx < 0 or idx > len(my_list):
        return(my_list)
    else:
        del my_list[idx]
        return(my_list)
