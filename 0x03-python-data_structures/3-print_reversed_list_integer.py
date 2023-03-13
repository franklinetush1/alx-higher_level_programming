#!/usr/bin/python3
if __name__ == "__main__":
    def print_reversed_list_integer(my_list=[]):
        """ prints all integers of a list, in reverse order"""
        start = len(my_list) - 1
        while start >= 0:
            print("{}".format(my_list[start]))
            start -= 1
