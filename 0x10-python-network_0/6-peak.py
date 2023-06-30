#!/usr/bin/python3
def find_peak(list_of_integers):
	"""Defines a peak-finding algorithm."""
    left, right = 0, len(list_of_integers) - 1
    
    while left < right:
        middle = left + (right - left) // 2
        if list_of_integers[middle] > list_of_integers[middle + 1] and list_of_integers[middle] > list_of_integers[middle - 1]:
            return list_of_integers[middle]        
        elif list_of_integers[middle] < list_of_integers[middle + 1]:
            left = middle + 1        
        else:
            right = middle - 1    
    return list_of_integers[left]
