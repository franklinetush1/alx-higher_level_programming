#!/usr/bin/python3
def print_last_digit(number):
    """Print the last digit of a number and return it."""
    num = abs(number) % 10
    print(f"{num}", end="")
    return num
