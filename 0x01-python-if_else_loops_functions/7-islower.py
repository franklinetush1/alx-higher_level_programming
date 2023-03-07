#!/usr/bin/python3
def islower(c):
    """Check for lowercase characters."""
    if ord(str(c)) in range(97, 123):
        return True
    else:
        return False
