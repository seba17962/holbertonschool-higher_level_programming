#!/usr/bin/python3
"""script that adds all
arguments to a Python list,
and then save them to a file
"""
import os
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists('add_item.json'):
    list_args = load_from_json_file('add_item.json')
else:
    list_args = []

for arg in argv[1:]:
    list_args.append(arg)

save_to_json_file(list_args, 'add_item.json')
