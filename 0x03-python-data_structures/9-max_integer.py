#!/usr/bin/python3
def max_integer(my_list=[]):
    """Check largest integer in the list"""
    if len(my_list) == 0:
        return None
    else:
        maxi = 0
        for num in my_list:
            if num > maxi:
                maxi = num
        return maxi
