#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    nm = dir(hidden_4)
    for name in nm:
        if name[:2] != "__":
            print(name)
