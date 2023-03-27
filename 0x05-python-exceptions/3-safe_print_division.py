#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (ZeroDivisionError, TypeError):
        div = None
    finally:
        print("Inside result: {}".format(div))
        return(div)
