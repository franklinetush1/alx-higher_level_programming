#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Check if number is divisible by 2"""
    multiple = []
    for num in my_list:
        if num % 2 == 0:
            multiple.append(True)
        else:
            multiple.append(False)
    return (multiple)
