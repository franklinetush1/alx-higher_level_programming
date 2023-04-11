0. Lookup

0-lookup.py: Python function that returns a list of available attributes and methods of an objects.
1. My list

1-my_list.py: Python class MyList that inherits from list. Includes:
Public instance method def print_sorted(self): that prints the list in ascending sorted order (assumes all list elements are ints).
2. Exact same object

2-is_same_class.py: Python function that returns True if an object is exactly an instance of a specified class; otherwise False.
3. Same class or inherit from

3-is_kind_of_class.py: Python function that returns True if an object is an instance or inherited instance of a specified class; otherwise False.
4. Only sub class of

4-inherits_from.py: Python function that returns True if an object is an inherited instance (either directly or indirectly) from a specified class; otherwise False.
5. Geometry module

5-base_geometry.py: An empty Python class BaseGeometry.
6. Improve Geometry

6-base_geometry.py: Python class BaseGeometry. Builds on 5-base_geometry.py with:
Public instance method def area(self): that raises an Exception with the message area() is not implemented.
7. Integer validator

7-base_geometry.py: Python class BaseGeometry. Builds on 6-base_geometry.py with:
Public instance method def integer_validator(self, name, value): that validates the parameter value.
Assumes the parameter name is always a string.
The parameter value must be an int, otherwise, a TypeError exception is raised with the message <name> must be an integer.
The parameter value must be greater than 0, otherwise, a ValueError exception is raised with the message <value> must be greater than 0
