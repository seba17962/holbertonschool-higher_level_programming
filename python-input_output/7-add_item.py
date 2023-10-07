#!/usr/bin/python3
"""script that adds all
arguments to a Python list,
and then save them to a file
"""
import json
import os
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists('add_item.json'):
    with open('add_item.json', 'r') as f:
        list_args = load_from_json_file(f)
else:
    list_args = []

for arg in argv[1:]:
    list_args.append(arg)

save_to_json_file(list_args, 'add_item.json')
