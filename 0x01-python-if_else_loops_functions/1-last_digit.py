#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
nb = "Last digit of " + str(number)
if lastDigit > 5:
    print(nb + f" is {lastDigit} and is greater than 5")
elif lastDigit == 0:
    print(nb + f" is {lastDigit} and is 0")
else:
    print(nb + f" is {lastDigit} and is less than 6 and not 0")
