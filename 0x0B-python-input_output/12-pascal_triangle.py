#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Function that returns a list of lists of integers
    representing the Pascal’s triangle"""
    if n <= 0:
        return []

    tri_arr = [[1]]
    while len(tri_arr) != n:
        arr = [1]
        a = tri_arr[-1]

        for x in range(len(a) - 1):
            arr.append(a[x] + a[x + 1])
        arr.append(1)
        tri_arr.append(arr)
    return (tri_arr)
