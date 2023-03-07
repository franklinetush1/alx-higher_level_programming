#!/usr/bin/python3
def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space."""
    for num in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif num % 3 == 0 and num!= 0:
            print(f"Fizz", end=" ")
        elif num % 5 == 0 and num!= 0:
            print(f"Buzz", end=" ")
        else:
            print("{} ".format(number), end="")
