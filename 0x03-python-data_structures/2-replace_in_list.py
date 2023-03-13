#!/usr/bin/python3
if __name__ == "__main__":
    def replace_in_list(my_list, idx, element):
        """Replaces an element of a list at a specific position"""
        length = len(my_list)
        if idx <= length:
            my_list[idx] = element
            return(my_list)
        elif idx < 0:
            return(my_list)
        else:
            return(my_list)
