#!/usr/bin/python3
""" script that adds all arguments to a Python list
and saves them to a file:"""
import sys
import os.path


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

py_list = []
if os.path.exists("add_item.json"):
    py_list = load("add_item.json")

for arg in sys.argv[1:]:
    py_list.append(arg)

save(py_list, "add_item.json")
