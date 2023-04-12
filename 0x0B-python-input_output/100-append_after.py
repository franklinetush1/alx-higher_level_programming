"""Insert text file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    """
    app = []
    with open(filename, 'r', encoding="utf-8") as ne:
        for line in ne:
            app += [line]
            if line.find(search_string) != -1:
                app += [new_string]

    with open(filename, 'w', encoding="utf-8") as ne:
        ne.write("".join(app))
